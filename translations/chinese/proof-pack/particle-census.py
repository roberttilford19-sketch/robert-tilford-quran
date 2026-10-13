#!/usr/bin/env python3
"""
particle-census.py — deterministic pairing census for corrective particles
(kalla / balaa) in Robert Tilford's Recital EN master vs the Chinese staging text.

Three nets, unioned:
  NET-EN : EN verse contains a corrective surface token:
           "Yes —", "No —", "But no —", "Then no —", "No indeed —",
           "No indeed.", "Yes indeed —", "Yes, by ..." (dialogue balaa).
  NET-K  : Arabic contains kalla (كَلَّا) — distinguished from kullaa (كُلًّا,
           "all/each") by the vowel on the kaf (fatha vs damma) BEFORE
           diacritic stripping.
  NET-B  : Arabic contains balaa (بَلَىٰ) after normalization.

For every candidate occurrence the script records the EN surface, its
position (opening / mid-verse), an EN snippet, the full Chinese verse text
(han script only), the CN opening, and every CN corrective-marker string
found (不 / 绝不 / 不然 / 的确 / 真的 / 诚然 / 是的 / 当然 / 并非 / 绝非 /
不会 / 不可) with its character offset — the raw material for hand-checking.

Outputs (this folder): particle-candidates.json + particle-review.txt
Read-only: never writes to either manuscript.
"""
import re, json
from collections import Counter

EN_PATH = '/home/hatch/workspace/original-recital/files/original-recital-FULL.txt'
CN_PATH = '/home/hatch/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md'
OUT_JSON = '/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/particle-candidates.json'
OUT_TXT = '/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/particle-review.txt'

# ---------------- parse EN master + Arabic ----------------
en_verses, ar_verses = {}, {}
cur = None
for line in open(EN_PATH, encoding='utf-8'):
    line = line.rstrip('\n')
    m = re.fullmatch(r'(\d+):(\d+)', line.strip())
    if m:
        cur = (int(m.group(1)), int(m.group(2)))
    elif cur and line.startswith('EN:'):
        en_verses[cur] = line[3:].strip()
    elif cur and line.startswith('AR:'):
        ar_verses[cur] = line[3:].strip()

# ---------------- parse CN staging (han only) ----------------
cn_text = open(CN_PATH, encoding='utf-8').read()
cn_verses = {}
for m in re.finditer(r'\*\*(\d+):(\d+)\*\*\s*(.*?)(?=\n\*\*\d+:\d+\*\*|\Z)', cn_text, re.S):
    s, v, body = int(m.group(1)), int(m.group(2)), m.group(3)
    han = ''.join(re.findall(r'[\u4e00-\u9fff，。；：？！、""''（）《》·—…\d]', body))
    cn_verses[(s, v)] = han

# ---------------- Arabic nets ----------------
def norm_ar(s):
    s = re.sub(r'[\u064B-\u065F\u0670\u0640]', '', s)
    return (s.replace('ٱ', 'ا').replace('أ', 'ا').replace('إ', 'ا')
             .replace('آ', 'ا').replace('ى', 'ي'))

def _strip_marks(s):
    return re.sub(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]', '', s)

def has_kalla(raw):
    """Kalla is a STANDALONE word. Token-test on the raw line: a token whose
    mark-stripped form is exactly كلا counts — unless its kaf carries a damma,
    which makes it kullaa ('all/each'). Substring look-alikes inside longer
    words (akala 'they ate', ta'kuluuna 'you eat') never qualify."""
    for tok in raw.split():
        bare = _strip_marks(tok).replace('ٱ', 'ا').replace('أ', 'ا').replace('إ', 'ا')
        if bare == 'كلا':
            vowels = [c for c in tok if c in '\u064E\u064F\u0650']
            if vowels and vowels[0] == '\u064F':
                continue  # kullaa
            return True
    return False

def has_balaa(raw):
    # norm_ar maps alef-maksura (ى) to ya (ي), so balaa surfaces as بلي
    return re.search(r'(^|\s)بلي(\s|$)', norm_ar(raw)) is not None

# ---------------- EN token net ----------------
TOKEN_RE = re.compile(
    r'(?P<surface>Yes indeed\s*—|No indeed\s*—|No indeed\.|'
    r'Yes\s*—|No\s*—|But no\s*—|Then no\s*—|So no\s*—|Yes,\s*by)')

CN_MARKERS = ['绝不会', '绝不', '不然', '的确', '真的', '诚然', '是的',
              '当然', '并非', '绝非', '不会', '不可', '不']

records = []
for (s, v) in sorted(en_verses):
    ent = en_verses[(s, v)]
    ar = ar_verses.get((s, v), '')
    nets = set()
    if has_kalla(ar):
        nets.add('KALLA')
    if has_balaa(ar):
        nets.add('BALAA')
    toks = list(TOKEN_RE.finditer(ent))
    if toks:
        nets.add('EN-TOKEN')
    if not nets:
        continue
    cn = cn_verses.get((s, v), '')
    markers = []
    for mk in CN_MARKERS:
        for mm in re.finditer(re.escape(mk), cn):
            markers.append({'marker': mk, 'offset': mm.start()})
    markers.sort(key=lambda d: d['offset'])
    if toks:
        for t in toks:
            pos = 'opening' if t.start() <= 15 else 'mid'
            records.append({
                'surah': s, 'verse': v, 'nets': sorted(nets),
                'kind': 'EN-TOKEN', 'surface': t.group(0).strip(),
                'position': pos,
                'en_snippet': ent[max(0, t.start() - 55): t.end() + 65].strip(),
                'en_full': ent, 'cn_full': cn, 'cn_opening': cn[:16],
                'cn_markers': markers,
            })
    else:
        # Arabic-net-only candidate (EN carries no dash token at the particle)
        records.append({
            'surah': s, 'verse': v, 'nets': sorted(nets),
            'kind': 'AR-ONLY', 'surface': '(no EN dash token)',
            'position': 'n/a',
            'en_snippet': ent[:130], 'en_full': ent,
            'cn_full': cn, 'cn_opening': cn[:16], 'cn_markers': markers,
        })

by_kind = Counter(r['kind'] for r in records)
by_net = Counter(n for r in records for n in r['nets'])
verses = {(r['surah'], r['verse']) for r in records}
print(f'candidate occurrences: {len(records)} across {len(verses)} verses')
print('by kind:', dict(by_kind))
print('by net (verse may carry several):', dict(by_net))

json.dump({'records': records}, open(OUT_JSON, 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
with open(OUT_TXT, 'w', encoding='utf-8') as f:
    for r in records:
        f.write(f"== {r['surah']}:{r['verse']} [{','.join(r['nets'])}] "
                f"{r['surface']} ({r['position']})\n")
        f.write(f"EN: {r['en_snippet']}\n")
        f.write(f"CN: {r['cn_full']}\n")
        f.write(f"CN markers: {[(m['marker'], m['offset']) for m in r['cn_markers']]}\n\n")
print('wrote', OUT_JSON, 'and', OUT_TXT)
