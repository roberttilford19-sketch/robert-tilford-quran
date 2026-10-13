# QUARANTINE CLEARANCE RECEIPT — Chinese Ayah Companion, Patch Set 1

- Follow-up to: `PATCH-APPLICATION-RECEIPT.md` (first application: 692 applied · 27 quarantined)
- Manifest: `/home/hatch/workspace/ayah-chinese/sweep-2026-10-12/APPLICATION-MANIFEST.md` — approved proposed texts unchanged; only the matching method changed (verse-block-scoped replacement)
- Source (still untouched): `/home/hatch/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md`
  sha256 `2030fe976bb48f253968a4d4f3cbafe9d269b4a79137695cb8eee719293fd57b`
- Frozen v1 record: `patched/ayah-companion-manuscript-ZH-PATCHED-v1.md` — sha256 `368835add93fec8552dc80458c9f91d12ccab7ca86a511923729a5a3bac22cee` · 2,135,954 bytes (byte-copy of the first application's output, frozen before this pass)
- Working file (edited in place): `patched/ayah-companion-manuscript-ZH-PATCHED.md`
  **v2 sha256 `11b3a78a86d0e26c5f22d61e2bcc9ea3bf0ae1bb56e21a76955c069ac7f0691c` · 2,135,551 bytes (Δ vs v1: −403)**

## Method

For each quarantined row, the verse's own block (its `**S:V**` marker to the next marker) was isolated; the block's CN segment (all paragraphs before the Arabic paragraph) was whitespace-normalized (line/paragraph breaks → single space, matching the manifest's normalization) and asserted **verbatim-equal** to the manifest's current-CN field inside that block; the segment was then replaced with the manifest's proposed text exactly. Nothing was forced: all 27 rows matched on assertion, so all 27 were applied.

Note on the furniture rows: the break before the sajda/qira'at marker is a paragraph break (`\n\n`) in some verses (5:6, 13:15, 16:50, 53:62) and a single line break (sometimes with trailing spaces) in the rest — the normalization above covers both, which is why the first application's whole-file verbatim search missed all 16.

## Per-row outcome — 27 / 27 APPLIED, 0 left quarantined

### P-07 furniture rows (16) — marker/note paragraph removed, verse text otherwise per manifest

| Verse | Classes | Outcome |
|---|---|---|
| 5:6 | P-07 | APPLIED — qira'at note `*[有些读法是抹到脚为止；这里印刷的读法是洗。]*` removed |
| 7:206 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 13:15 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 16:50 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 17:109 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 19:58 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 22:18 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 22:77 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 25:60 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 27:26 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 32:15 | P-04, P-07 | APPLIED — `*[叩头——必行的]*` removed + 启示→迹象 per row |
| 38:24 | P-03, P-07 | APPLIED — `*[叩头——建议的]*` removed + 我→我们 per row |
| 41:38 | P-07 | APPLIED — `*[叩头——必行的]*` removed |
| 53:62 | P-07 | APPLIED — `*[叩头——必行的]*` removed |
| 84:21 | P-07 | APPLIED — `*[叩头——建议的]*` removed |
| 96:19 | P-07 | APPLIED — `*[叩头——必行的]*` removed |

### Non-unique rows (11) — matched inside the verse's own block, that verse's own row applied

| Verse | Classes | Outcome |
|---|---|---|
| 26:2 | P-02, P-04 | APPLIED — 这些是阐明的这部经典的节文。 (28:2's identical twin left for its own row) |
| 28:2 | P-02, P-04 | APPLIED — 这些是阐明的这部经典的节文。 |
| 26:8 | P-05 | APPLIED — 信士→信道者 (this verse's block only) |
| 26:103 | P-05 | APPLIED — 信士→信道者 |
| 26:121 | P-05 | APPLIED — 信士→信道者 |
| 26:174 | P-05 | APPLIED — 信士→信道者 |
| 26:190 | P-05 | APPLIED — 信士→信道者 |
| 43:2 | P-02 | APPLIED — 以阐明的这部经典发誓。 (44:2's twin handled by its own row) |
| 44:2 | P-02 | APPLIED — 以阐明的这部经典发誓。 |
| 94:5 | P-10 | APPLIED — 与艰难同在的，确有容易。 (94:6's twin handled by its own row) |
| 94:6 | P-10 | APPLIED — 与艰难同在的，确有容易。 |

**Patch Set 1 is now fully applied: 719 / 719 patch rows · 5 preserve rows untouched · 0 quarantined.**

## Gate results (all gates from the first application, re-run on v2)

- (a) Verse-marker parity: source 6,236 · v2 6,236 · sequence identical to source: True · header (pre-2:1 text) identical: True → **PASS (6,236/6,236, in sequence)**
- (b) Arabic characters: source 639,899 · v2 639,899 (identical under both the census measure U+0600–06FF and the broad Arabic-blocks measure) → **PASS — Arabic untouched**
- Isolation audit (this pass): blocks differing v1→v2 = **exactly the 27 target blocks**, no other block changed → **PASS**
- Full-state audit: blocks differing source→v2 = **exactly the 719 patch-row verses**; every differing block's normalized CN equals its manifest proposed text verbatim (716 rows parsed directly + the 3 merged Ruling-3 rows 2:144, 2:158, 2:196 verified positionally — their note fields contain an embedded separator); the 5 preserve rows (4:51, 20:4, 26:192, 56:80, 69:43) are byte-identical to source; **no verse in any other state** → **PASS**
- (c) Do-not-touch spots: 2:275 byte-identical · 5:60 byte-identical · 16:36 byte-identical · 39:17 byte-identical · 2:276 block = v1 block with 利息 carrier byte-identical · 2:3 block = v1 block with 幽玄 carrier byte-identical → **PASS**
- (d) Census re-run on v2 (adapted copy of census.py, same logic): parity failures NONE · CN 222,638 chars (census definition; v1 was 222,742, Δ −104 from furniture removal net of the text repairs) · Arabic 639,899 · **total candidate flags: 5 — all USURY-LIXI, the ruled Ruling-1 controls** (ZAKAT-NO-TIANKE 0 · TYRANT-EMO 0 · BOOK-NO-ZHEBU 0 · WE-FLATTENED 0 · TALUT-SAUL 0 · THINK-QUEXIN 0 · FACE-LINZAI 0) → **PASS**

## Hash chain

- Source (staging anchor, untouched): `2030fe976bb48f253968a4d4f3cbafe9d269b4a79137695cb8eee719293fd57b` · 2,133,557 bytes
- v1 (692 applied, 27 quarantined): `368835add93fec8552dc80458c9f91d12ccab7ca86a511923729a5a3bac22cee` · 2,135,954 bytes — frozen copy kept as `ayah-companion-manuscript-ZH-PATCHED-v1.md`
- **v2 (719/719 applied): `11b3a78a86d0e26c5f22d61e2bcc9ea3bf0ae1bb56e21a76955c069ac7f0691c` · 2,135,551 bytes** — the patched master, at `patched/ayah-companion-manuscript-ZH-PATCHED.md`, ready for the propagation step (workspace / staging / GitHub / archive.org sync, three-way byte verification) on Robert's word.
