#!/usr/bin/env python3
"""
Deterministic census for the Chinese Ayah Companion sweep.
Counts every letter, checks verse parity per surah, and pairs EN<->CN verses
for the mechanical fault patterns verified in the Surah 2 sampling.
Output: census-flags.json (candidate flags for crew review — NOT verdicts)
and a printed summary. Read-only: never writes to the manuscripts.
"""
import re, json, sys
from collections import Counter, defaultdict

CN_PATH = '/home/hatch/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md'
EN_PATH = '/home/hatch/workspace/original-recital/files/original-recital-FULL.txt'
OUT = '/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/census-flags.json'

CANON = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,
         112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,
         59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,
         52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,
         21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
assert sum(CANON) == 6236, sum(CANON)

# ---------- parse CN ----------
cn_text = open(CN_PATH, encoding='utf-8').read()
cn_verses = {}   # (surah, verse) -> chinese-only text (arabic stripped)
for m in re.finditer(r'\*\*(\d+):(\d+)\*\*\s*(.*?)(?=\n\*\*\d+:\d+\*\*|\Z)', cn_text, re.S):
    s, v, body = int(m.group(1)), int(m.group(2)), m.group(3)
    han = ''.join(re.findall(r'[\u4e00-\u9fff，。；：？！、""''（）《》·—…\d]', body))
    cn_verses[(s, v)] = han

# ---------- parse EN (Recital master: "N:M" line, AR: line, EN: line) ----------
en_text = open(EN_PATH, encoding='utf-8').read()
en_verses = {}
cur = None
for line in en_text.split('\n'):
    mm = re.fullmatch(r'(\d+):(\d+)', line.strip())
    if mm:
        cur = (int(mm.group(1)), int(mm.group(2)))
    elif cur and line.startswith('EN:'):
        en_verses[cur] = line[3:].strip()
        cur = None

print(f'CN verses parsed: {len(cn_verses)} | EN verses parsed: {len(en_verses)}')

# ---------- parity + letter counts ----------
parity_bad = []
cn_chars = Counter(); 
for s in range(1, 115):
    got = sum(1 for (ss, v) in cn_verses if ss == s)
    if got != CANON[s-1]:
        parity_bad.append((s, CANON[s-1], got))
    cn_chars[s] = sum(len(cn_verses[(s, v)]) for v in range(1, CANON[s-1]+1) if (s, v) in cn_verses)
total_cn_chars = sum(cn_chars.values())
total_ar_chars = len(re.findall(r'[\u0600-\u06FF]', cn_text))
total_en_words = len(re.findall(r"[A-Za-z']+", en_text))
print(f'parity failures: {parity_bad if parity_bad else "NONE — all 114 surahs exact"}')
print(f'CN han/punct chars total: {total_cn_chars} | Arabic chars in CN file: {total_ar_chars} | EN master words: {total_en_words}')

# ---------- paired mechanical checks ----------
flags = []
def flag(s, v, kind, detail):
    flags.append({'surah': s, 'verse': v, 'kind': kind, 'detail': detail})

for (s, v), en in en_verses.items():
    cn = cn_verses.get((s, v))
    if cn is None:
        flag(s, v, 'MISSING-CN', 'no CN verse parsed'); continue
    en_l = en
    # the Book -> should carry 这部
    if re.search(r'\b(the|God\'s|His|My|Our) Books?\b', en_l) and '经典' in cn and '这部' not in cn:
        flag(s, v, 'BOOK-NO-ZHEBU', cn[:40])
    # zakat -> 天课
    if 'zakat' in en_l and '天课' not in cn:
        flag(s, v, 'ZAKAT-NO-TIANKE', ('施舍' in cn and 'rendered 施舍') or cn[:40])
    # usury -> census only
    if 'usury' in en_l and '利息' in cn:
        flag(s, v, 'USURY-LIXI', 'EN usury -> CN 利息 (ruling item)')
    # tyrant(s) -> 恶魔
    if re.search(r'\btyrants?\b', en_l) and '恶魔' in cn:
        flag(s, v, 'TYRANT-EMO', cn[:40])
    # Talut -> 扫罗
    if 'Talut' in en_l and '扫罗' in cn:
        flag(s, v, 'TALUT-SAUL', cn[:40])
    # think -> 确信 (cognition override candidates)
    if re.search(r'\bthink\b', en_l) and '确信' in cn:
        flag(s, v, 'THINK-QUEXIN', cn[:40])
    # God's face -> 临在
    if re.search(r"God's face|face of God|His face", en_l) and '临在' in cn:
        flag(s, v, 'FACE-LINZAI', cn[:40])
    # divine We provided/gave -> singular 我 without 我们
    if re.search(r'\bWe (provided|gave|sent down|revealed|bestowed)\b', en_l) and '我们' not in cn and '我' in cn:
        flag(s, v, 'WE-FLATTENED', cn[:40])
    # quote balance inside the verse
    if cn.count('“') != cn.count('”'):
        flag(s, v, 'QUOTE-IMBALANCE', f"open {cn.count('“')} close {cn.count('”')}")

# ---------- CN-side string census (whole book) ----------
census_terms = ['回忆当时','禁寺','天房','清真寺','禁标处','副朝','小朝','这部经典','安拉','幽玄','归顺',
                '多神教徒','以物配主者','米卡伊勒','临在','自我','同胞','确信','埃及','利息','重利','利贷',
                '无家可归者','旅客','行路的人','撒旦','天课','施舍','真主','礼拜','火狱','地狱','乐园','天堂']
counts = {t: cn_text.count(t) for t in census_terms}

by_kind = Counter(f['kind'] for f in flags)
print('\nCN-side census (whole manuscript):')
for t, c in counts.items():
    print(f'  {t}: {c}')
print('\nPaired-check candidate flags by kind:')
for k, c in by_kind.most_common():
    print(f'  {k}: {c}')
print(f'TOTAL candidate flags: {len(flags)}')

json.dump({'counts': counts, 'parity_bad': parity_bad, 'total_cn_chars': total_cn_chars,
           'total_ar_chars': total_ar_chars, 'total_en_words': total_en_words,
           'flags': flags}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'\nflags written to {OUT}')
