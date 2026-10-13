#!/usr/bin/env python3
"""
we-census.py — Divine-We clause census v2 (P-03 master enumeration + regression checklist)

Pairs EVERY verse of the Recital EN master against the Chinese staging manuscript
and classifies the divine first-person voice at CLAUSE level.

EN classification
-----------------
Robert's orthography is the primary signal: the divine pronoun is CAPITALIZED
even mid-clause ("and what We provided them", "they return to Us"); human
we/our/us is lowercase and excluded outright.
Capitalized We/Our/Us is a divine CANDIDATE unless speaker analysis says human:
  * inside a quote attributed to creatures (they said / the angels said /
    a prophet said / "for their saying:")            -> HUMAN
  * vocative prayer "Our Lord, ..." (creature prayer) -> HUMAN
  * after "Say:" (the Prophet is told what to say; the voice inside is the
    believers' confession / human prayer)             -> HUMAN (reviewed)
Tier 1 = capitalized token mid-clause. Tier 2 = clause-initial (verse start,
after a conjunction, or at a quote opening) — divine narrative vs. human
prayer both occur, so Tier 2 rows were all read in hand review.

CN judging (clause level)
--------------------------
CN verse is split into clauses on ，；：、。！？ The verse's EN divine clauses
(in order) are assigned contiguous zones of the CN clause list (monotonic
alignment). A clause is PRESERVED if 我们 governs its zone: present in the
zone, or carried over from the subject of the preceding CN sentence with no
intervening bare 我. Otherwise FLATTENED (bare 我 subject, dropped object,
or zero pronoun with no carry-over).
Verse verdict: PRESERVED (all), FLATTENED (none), MIXED (some of each).

Hand review: every FLATTENED clause, every remaining Tier-2 clause, every
both-pronouns verse, and a sample of PRESERVED rows were read in context;
corrections live in OVERRIDES ((surah, verse, clause_no) -> 'HUMAN' |
'PRESERVED' | 'FLATTENED'). The script is otherwise deterministic.

Outputs: WE-CENSUS.md next to this script.
"""
import re, json
from collections import Counter

EN_PATH = '/home/hatch/workspace/original-recital/files/original-recital-FULL.txt'
CN_PATH = '/home/hatch/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md'
OUT_MD  = '/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/WE-CENSUS.md'
OUT_JSON = '/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/WE-CENSUS-rows.json'

# ---------------------------------------------------------------- hand review
# (surah, verse, clause_no): 'HUMAN' | 'PRESERVED' | 'FLATTENED'
# Every candidate row was read in context during the 2026-10-12 hand review
# (all 358 script-FLATTENED rows, all MIXED-verse rows, all both-pronoun-verse
# PRESERVED rows, all Tier-2 quote rows, all Tier-2 no-divine-verb rows, all
# Tier-1 quote rows, the unknown-quote residue, and two attribution-pattern
# sweeps). Rationale classes are noted per group; see WE-CENSUS.md header.
OVERRIDES = {
    # --- PRESERVED: pairing misses — the CN verse does carry 我们 for this
    # clause, but outside the ±1-clause anchor window / sentence pattern.
    (2, 254, 0): 'PRESERVED', (5, 19, 0): 'PRESERVED', (7, 103, 0): 'PRESERVED',
    (10, 61, 0): 'PRESERVED', (10, 74, 0): 'PRESERVED', (10, 75, 0): 'PRESERVED',
    (14, 1, 0): 'PRESERVED', (16, 97, 0): 'PRESERVED', (18, 29, 0): 'PRESERVED',
    (20, 21, 0): 'PRESERVED', (20, 85, 0): 'PRESERVED',
    # --- PRESERVED by cross-verse carry-over: CN verse opens with a zero
    # pronoun continuing the 我们 subject of the immediately preceding verse
    # (51:35 我们把…撤了出来 / 56:60 我们已…注定了死亡) — voice stays plural.
    (51, 36, 0): 'PRESERVED', (56, 61, 0): 'PRESERVED',
    # --- FLATTENED: anchor window borrowed a 我们 belonging to another
    # clause/speaker; this clause's own CN is 我 / zero / third person.
    (2, 57, 1): 'FLATTENED',    # quoted command = 吃我赐给你们 (next segment's 他们没有亏待我们 bled in)
    (25, 21, 0): 'FLATTENED',   # "meet Us" → 与我相会
    (27, 83, 0): 'FLATTENED',   # "We gather" → 我…集合 (window caught 我们的启示)
    (41, 15, 0): 'FLATTENED',   # "Our signs" → 我的启示 (window caught the 'Ad quote 谁比我们更有力)
    (61, 14, 1): 'FLATTENED',   # "We strengthened those who believed" → 我援助了 (window caught disciples' 我们)
    # --- HUMAN: creature speech — quoted or dictated words of humans, angels,
    # jinn, or other creatures; ordinary plurals, excluded from the census.
    # Believers' dictated confessions / prescribed words (Say:-class):
    (2, 136, 0): 'HUMAN', (2, 136, 1): 'HUMAN', (2, 285, 0): 'HUMAN',
    (3, 84, 0): 'HUMAN', (3, 84, 1): 'HUMAN', (9, 52, 0): 'HUMAN',
    (29, 46, 0): 'HUMAN', (34, 26, 0): 'HUMAN', (42, 15, 0): 'HUMAN',
    (67, 29, 0): 'HUMAN',
    # Creature prayers / "Our Lord" vocatives:
    (2, 201, 0): 'HUMAN', (3, 16, 0): 'HUMAN', (4, 75, 0): 'HUMAN',
    (6, 128, 0): 'HUMAN', (7, 53, 0): 'HUMAN', (10, 88, 0): 'HUMAN',
    (14, 44, 0): 'HUMAN', (18, 10, 0): 'HUMAN', (23, 109, 0): 'HUMAN',
    (25, 65, 0): 'HUMAN', (25, 74, 0): 'HUMAN', (28, 63, 0): 'HUMAN',
    (46, 13, 0): 'HUMAN', (50, 27, 0): 'HUMAN', (59, 10, 0): 'HUMAN',
    # Quoted creature speech (narration, dialogue, judgment-day pleas):
    (2, 156, 0): 'HUMAN', (3, 7, 0): 'HUMAN', (3, 52, 0): 'HUMAN',
    (4, 150, 0): 'HUMAN', (5, 7, 0): 'HUMAN', (5, 22, 0): 'HUMAN',
    (7, 76, 0): 'HUMAN', (7, 127, 0): 'HUMAN', (7, 173, 0): 'HUMAN',
    (8, 21, 0): 'HUMAN', (12, 8, 0): 'HUMAN', (12, 73, 0): 'HUMAN',
    (12, 79, 0): 'HUMAN', (12, 91, 0): 'HUMAN', (12, 97, 0): 'HUMAN',
    (14, 11, 1): 'HUMAN', (15, 53, 0): 'HUMAN', (15, 55, 0): 'HUMAN',
    (15, 58, 0): 'HUMAN', (16, 28, 0): 'HUMAN', (17, 90, 0): 'HUMAN',
    (18, 21, 1): 'HUMAN', (18, 88, 0): 'HUMAN', (20, 47, 0): 'HUMAN',
    (20, 47, 1): 'HUMAN', (20, 70, 0): 'HUMAN', (21, 14, 0): 'HUMAN',
    (21, 46, 0): 'HUMAN', (21, 53, 0): 'HUMAN', (21, 97, 0): 'HUMAN',
    (23, 83, 0): 'HUMAN', (23, 113, 0): 'HUMAN', (24, 16, 0): 'HUMAN',
    (24, 47, 0): 'HUMAN', (24, 51, 0): 'HUMAN', (26, 47, 0): 'HUMAN',
    (26, 61, 0): 'HUMAN', (26, 71, 0): 'HUMAN', (27, 27, 0): 'HUMAN',
    (27, 33, 0): 'HUMAN', (27, 41, 0): 'HUMAN', (27, 42, 0): 'HUMAN',
    (27, 47, 0): 'HUMAN', (27, 49, 0): 'HUMAN', (27, 68, 0): 'HUMAN',
    (28, 63, 1): 'HUMAN', (28, 63, 2): 'HUMAN', (29, 10, 0): 'HUMAN',
    (29, 31, 0): 'HUMAN', (32, 12, 1): 'HUMAN', (32, 12, 2): 'HUMAN',
    (33, 13, 0): 'HUMAN', (35, 37, 1): 'HUMAN', (37, 30, 0): 'HUMAN',
    (37, 32, 0): 'HUMAN', (38, 7, 0): 'HUMAN', (40, 11, 1): 'HUMAN',
    (40, 43, 0): 'HUMAN', (41, 31, 0): 'HUMAN', (45, 32, 0): 'HUMAN',
    (45, 32, 1): 'HUMAN', (46, 31, 0): 'HUMAN', (48, 11, 0): 'HUMAN',
    (49, 14, 0): 'HUMAN', (49, 14, 1): 'HUMAN', (60, 4, 1): 'HUMAN',
    (61, 14, 0): 'HUMAN', (68, 31, 0): 'HUMAN', (72, 1, 0): 'HUMAN',
    (72, 2, 0): 'HUMAN', (74, 43, 0): 'HUMAN', (76, 9, 0): 'HUMAN',
    (76, 9, 1): 'HUMAN', (76, 10, 0): 'HUMAN',
    # Split artifact: the clause span holds only the townspeople's lowercase
    # "we" quote; the verse's divine clause is c1 ("a provision from Us").
    (28, 57, 0): 'HUMAN',
}

# ------------------------------------------------------------------- parsing
def parse_en(path):
    en, cur = {}, None
    for line in open(path, encoding='utf-8'):
        m = re.fullmatch(r'(\d+):(\d+)\s*', line.strip())
        if m:
            cur = (int(m.group(1)), int(m.group(2)))
        elif cur and line.startswith('EN:'):
            en[cur] = line[3:].strip(); cur = None
    return en

def parse_cn(path):
    text = open(path, encoding='utf-8').read()
    cn = {}
    for m in re.finditer(r'\*\*(\d+):(\d+)\*\*\s*(.*?)(?=\n\*\*\d+:\d+\*\*|\Z)', text, re.S):
        zh = []
        for ln in m.group(3).split('\n'):
            if re.search(r'[\u0600-\u06FF]', ln):
                break
            if ln.strip():
                zh.append(ln.strip())
        cn[(int(m.group(1)), int(m.group(2)))] = ''.join(zh)
    return cn

# ------------------------------------------------------------- EN clause work
CONJ = {'and', 'then', 'so', 'but', 'for', 'yet'}
CREATURE_SUBJ = re.compile(
    r"\b(they|the angels|the devils|the people|the men|the women|pharaoh|"
    r"the jews|the christians|the disbelievers|the believers|the hypocrites|"
    r"the wrongdoers|the guilty|the companions|his people|her|she|mary|"
    r"the children of israel|the magicians|the chiefs|his brothers|his sons|"
    r"the prisoners|the hosts|iblis|satan)\b", re.I)
SPEECH_VERB = re.compile(r"\b(said|says|say|saying|cried|cry|called|call|answered|replied|asked|exclaimed|declared|confess\w*)\b", re.I)
DIVINE_ATTR = re.compile(r"\b(your Lord|God|the Lord|We|He)\s+(said|says)\b")

def en_clauses(text):
    parts = re.split(r'(?<=[.?!;])\s+|\s+—\s+', text)
    out = []
    for p in parts:
        subs = re.split(r',\s+(?=(?:and\s+|but\s+|then\s+)?We\b)|(?<=:)\s+(?=")', p)
        out.extend(s.strip() for s in subs if s.strip())
    return out

def quote_spans(text):
    spans, inq, start = [], False, None
    for i, ch in enumerate(text):
        if ch == '"':
            if not inq:
                start, inq = i, True
            else:
                spans.append((start, i)); inq = False
    return spans

def clause_offset(clauses, idx):
    off = 0
    for c in clauses[:idx]:
        off += len(c) + 1
    return off

def token_speaker(text, spans, tok_start, clause):
    """Classify speaker of a capitalized pronoun at tok_start."""
    in_q = any(a <= tok_start <= b for a, b in spans)
    if not in_q:
        return 'divine'
    qstart = max(a for a, b in spans if a <= tok_start <= b)
    pre = text[max(0, qstart - 90):qstart]
    if DIVINE_ATTR.search(pre) and 'We said' in pre or re.search(r"(your Lord|God|the Lord)\s+said", pre):
        return 'divine'
    if re.search(r"\bSay:\s*$", pre.strip()) or pre.rstrip().endswith('Say:'):
        return 'human'      # believers' confession dictated after "Say:"
    if SPEECH_VERB.search(pre) and CREATURE_SUBJ.search(pre):
        return 'human'
    if SPEECH_VERB.search(pre):
        return 'unknown-quote'
    return 'unknown-quote'

def is_prayer_vocative(clause, tok):
    return tok == 'Our' and re.match(r'"?\s*Our (Lord|God)\b', clause) is not None

def divine_candidates(text):
    """Return list of dicts per EN clause containing candidate divine pronouns."""
    clauses = en_clauses(text)
    spans = quote_spans(text)
    out = []
    base = 0
    for ci, cl in enumerate(clauses):
        found = text.find(cl, base)
        if found >= 0:
            base = found
        toks = []
        for m in re.finditer(r"\b(We|Our|Us)\b", cl):
            tok_start = text.find(cl, base) + m.start() if text.find(cl, base) >= 0 else base + m.start()
            speaker = token_speaker(text, spans, tok_start, cl)
            # colon-introduced speech: "... their saying: We ..." — the We
            # clause after the colon is the quoted speech of the sayer.
            colon = cl.rfind(':', 0, m.start())
            if colon > 0 and re.search(r"\b(saying|said|say|says)\b", cl[:colon], re.I):
                pre_colon = cl[:colon]
                if CREATURE_SUBJ.search(pre_colon) or re.search(r"\btheir\b", pre_colon, re.I):
                    speaker = 'human'
                elif re.search(r"\b(We|God|your Lord|the Lord)\b[^:]*$", pre_colon):
                    speaker = 'divine'
            # tier: token is clause-initial if only conjunctions/quotes precede
            before = cl[:m.start()]
            lead = re.sub(r'["\s]', '', before).lower()
            tier = 2 if lead in ('', 'and', 'then', 'so', 'but', 'for', 'andthen', 'soand') else 1
            if is_prayer_vocative(cl, m.group(1)):
                speaker = 'human'
            toks.append({'token': m.group(1), 'tier': tier, 'speaker': speaker})
        if toks:
            first_off = None
            for m in re.finditer(r"\b(We|Our|Us)\b", cl):
                if any(t['token'] == m.group(1) for t in toks):
                    first_off = base + m.start(); break
            out.append({'clause_no': len(out), 'text': cl, 'tokens': toks,
                        'clause_index': ci, 'n_clauses': len(clauses),
                        'frac': (first_off / len(text)) if first_off is not None and text else 0.5})
        base += len(cl) + 1
    return out

# ------------------------------------------------------------- CN clause work
def cn_clause_list(zh):
    clauses, sidx = [], -1
    for part in re.split(r'(?<=[。！？])', zh):
        if not part.strip():
            continue
        sidx += 1
        for c in re.split(r'(?<=[，；：、])', part):
            if c.strip():
                clauses.append({'sent': sidx, 'text': c})
    return clauses

BARE_I = re.compile(r'(?<!们)我(?!们)')

def judge_zone(zone, clauses, zstart):
    """zone: list of CN clause dicts for this EN clause. Return verdict."""
    ztext = ''.join(c['text'] for c in zone)
    if '我们' in ztext:
        return 'PRESERVED'
    # carry-over: nearest earlier clause (any previous zone / earlier in this
    # sentence stream) whose subject is 我们, with no bare 我 after it
    prior = clauses[:zstart]
    last_we, last_i = -1, -1
    for i, c in enumerate(prior):
        if '我们' in c['text']:
            last_we = i
        if BARE_I.search(c['text']):
            last_i = i
    if last_we > last_i and last_we >= 0:
        return 'PRESERVED'
    return 'FLATTENED'

# ---------------------------------------------------------------------- main
def build_rows(en, cn):
    rows, verse_verdict = [], {}
    for ref in sorted(en):
        s, v = ref
        cand = divine_candidates(en[ref])
        # keep only divine / unknown-quote speakers (humans excluded here,
        # unknown-quote resolved in review via overrides default: divine)
        cand = [c for c in cand if any(t['speaker'] != 'human' for t in c['tokens'])]
        if not cand:
            continue
        clauses_cn = cn_clause_list(cn.get(ref, ''))
        T = len(clauses_cn)
        verdicts = []
        for rank, c in enumerate(cand):
            if T:
                ctr = min(T - 1, int(c.get('frac', 0.5) * T))
                zstart = max(0, ctr - 1)
                zone = clauses_cn[zstart:ctr + 2]
            else:
                zstart, zone = 0, []
            verdict = judge_zone(zone, clauses_cn, zstart)
            tier = min(t['tier'] for t in c['tokens'])
            ov = OVERRIDES.get((s, v, c['clause_no']))
            if ov == 'HUMAN':
                continue
            if ov in ('PRESERVED', 'FLATTENED'):
                verdict = ov
            rows.append({'surah': s, 'verse': v, 'clause_no': c['clause_no'],
                         'tier': tier, 'en_clause': c['text'],
                         'cn_clause': ''.join(z['text'] for z in zone),
                         'verdict': verdict, 'cn_verse': cn.get(ref, '')})
            verdicts.append(verdict)
        if not verdicts:
            continue
        verse_verdict[ref] = ('PRESERVED' if all(x == 'PRESERVED' for x in verdicts)
                              else 'FLATTENED' if all(x == 'FLATTENED' for x in verdicts)
                              else 'MIXED')
    return rows, verse_verdict

def _cell(t, cap=400):
    t = t.replace('|', '\\|').replace('\n', ' ').strip()
    return t if len(t) <= cap else t[:cap] + ' …'

def write_md(rows, vv):
    from collections import defaultdict
    by_s = defaultdict(list)
    for r in rows:
        by_s[r['surah']].append(r)
    vv_by_s = defaultdict(Counter)
    for (s, v), x in vv.items():
        vv_by_s[s][x] += 1
    rc = Counter(r['verdict'] for r in rows)
    repair = sorted(ref for ref, x in vv.items() if x != 'PRESERVED')
    L = []
    L.append('# WE-CENSUS — Divine-We Clause Census (Patch Class P-03 master enumeration)')
    L.append('')
    L.append('Generated 2026-10-12 by `we-census.py` (this folder) from:')
    L.append('- EN master: `~/workspace/original-recital/files/original-recital-FULL.txt`')
    L.append('- CN staging: `~/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md`')
    L.append('- Machine rows (same data as the tables below): `WE-CENSUS-rows.json` (this folder)')
    L.append('')
    L.append('## Method')
    L.append('')
    L.append('Every EN verse was scanned for first-person-plural divine voice at CLAUSE level.')
    L.append("Robert's EN capitalizes the divine pronoun even mid-clause (\"what We provided them\") —")
    L.append('that is Tier 1, unambiguous. A capitalized We/Our/Us at a clause head is Tier 2 (usually')
    L.append('divine narration, occasionally a creature\'s sentence-initial word). Lowercase we/our/us is')
    L.append('never Robert\'s divine voice and was excluded. Each EN clause was anchored into the CN')
    L.append('verse by its character fraction; the CN clause window (±1 clause) was judged: 我们')
    L.append('governing the clause = PRESERVED; 我, zero pronoun with singular carry-over, a dropped')
    L.append('pronoun, or a third-person substitution = FLATTENED. A verse with both = MIXED.')
    L.append('Creature speech (quoted or dictated words of humans, angels, jinn — including "Our Lord"')
    L.append('prayers and Say:-dictated confessions) was classified HUMAN and excluded.')
    L.append('The script cast a wide net; EVERY candidate row was then hand-read in context')
    L.append('(all script-FLATTENED rows, all MIXED verses, all both-pronoun verses, all Tier-2')
    L.append('quote/verb queues, the Tier-1 quote queue, the unknown-quote residue, and two')
    L.append('attribution-pattern sweeps). Corrections live in the script\'s OVERRIDES table with')
    L.append('rationale comments — this file is fully reproducible by re-running the script.')
    L.append('')
    L.append('## Book totals')
    L.append('')
    L.append(f'- Verses containing divine We: **{len(vv)}** — PRESERVED {sum(1 for x in vv.values() if x=="PRESERVED")} · '
             f'FLATTENED {sum(1 for x in vv.values() if x=="FLATTENED")} · MIXED {sum(1 for x in vv.values() if x=="MIXED")}')
    L.append(f'- Clauses: **{len(rows)}** — PRESERVED {rc["PRESERVED"]} · FLATTENED {rc["FLATTENED"]}')
    L.append('')
    L.append('## Verses needing P-03 repair (verse verdict FLATTENED or MIXED)')
    L.append('')
    L.append(', '.join(f'{s}:{v}' + (' (MIXED)' if vv[(s, v)] == 'MIXED' else '') for s, v in repair))
    L.append('')
    L.append('## Borderline calls (read before patching)')
    L.append('')
    L.append('- **51:36 / 56:61 — judged PRESERVED by cross-verse carry-over.** The CN clause has a zero')
    L.append('  pronoun, but it continues the 我们 subject of the immediately preceding verse')
    L.append('  (51:35 我们把…撤了出来； 56:60 我们已…注定了死亡）, so the voice stays plural. Not repair items.')
    L.append('- **30:28 — flattening by third-person substitution:** "what We provided you" is rendered')
    L.append('  真主赐予你们 (God as third person). Counted FLATTENED.')
    L.append('- **8:59 — "outran Us": the divine object pronoun is dropped in CN.** Counted FLATTENED.')
    L.append('- **Zero-pronoun continuations after a 我 clause** (e.g. 77:17, 77:21, 80:26, 95:5) stay')
    L.append('  FLATTENED: the carried subject is the singular 我.')
    L.append('- **29:31** was excluded as HUMAN (the angels\' "We will destroy"); its narration possessive')
    L.append('  "Our messengers" is nonetheless preserved in CN （我们的使者） — no repair needed there.')
    L.append('- **15:66** "We decreed for him that command" is read as divine narration resuming after')
    L.append('  the angels\' speech (CN 我们告诉他我们的判决， PRESERVED) — flagged here as the one')
    L.append('  genuinely arguable speaker call in the census.')
    L.append('')
    L.append('## Per-surah totals')
    L.append('')
    L.append('| Surah | Verses w/ divine We | V-PRESERVED | V-FLATTENED | V-MIXED | Clauses | C-PRESERVED | C-FLATTENED |')
    L.append('|---|---|---|---|---|---|---|---|')
    for s in sorted(by_s):
        cc = Counter(r['verdict'] for r in by_s[s])
        vc = vv_by_s[s]
        L.append(f'| {s} | {sum(vc.values())} | {vc["PRESERVED"]} | {vc["FLATTENED"]} | {vc["MIXED"]} '
                 f'| {len(by_s[s])} | {cc["PRESERVED"]} | {cc["FLATTENED"]} |')
    L.append('')
    L.append('## Clause table')
    L.append('')
    L.append('CN clause = the anchor window the verdict was judged on (the matched CN clause ±1).')
    L.append('After Patch Set 1 is applied, re-run the script: every row below must read PRESERVED.')
    for s in sorted(by_s):
        L.append('')
        L.append(f'### Surah {s}')
        L.append('')
        L.append('| Verse | # | EN clause | CN clause | Verdict |')
        L.append('|---|---|---|---|---|')
        for r in sorted(by_s[s], key=lambda x: (x['verse'], x['clause_no'])):
            L.append(f"| {s}:{r['verse']} ({vv[(s, r['verse'])]}) | {r['clause_no']} | "
                     f"{_cell(r['en_clause'])} | {_cell(r['cn_clause'])} | {r['verdict']} |")
    L.append('')
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L) + '\n')

def main():
    en, cn = parse_en(EN_PATH), parse_cn(CN_PATH)
    rows, vv = build_rows(en, cn)
    write_md(rows, vv)
    json.dump({'rows': rows, 'verse_verdict': {f'{k[0]}:{k[1]}': x for k, x in vv.items()}},
              open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c, vvc = Counter(r['verdict'] for r in rows), Counter(vv.values())
    print(f'clause rows: {len(rows)}  {dict(c)}')
    print(f'verses with divine We: {len(vv)}  {dict(vvc)}')
    print(f'tier-2 rows: {sum(1 for r in rows if r["tier"] == 2)}')

if __name__ == '__main__':
    main()
