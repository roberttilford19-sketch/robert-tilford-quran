# Landing Report — Erzya (myv) Quran

**Landed: 2026-11-27, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-MYV.md` — the book: 6,236 verses on the
  standard grid; 6,180 fully rendered; 56 verses carrying 70 visible
  ⟦GAP: …⟧ markers (jinn 30, pilgrimage 19, usury 8, Sabbath 7,
  apes 2, ape 1, cucumber 1, lentils 1, hoopoe 1). Front matter names
  the base honestly (modern literary Erzya, Cyrillic unmodified,
  Central-based; GiellaLT giella-myv LGPL v3 and Wiktionary/CC BY-SA
  as attestation sources; the 2006 New Testament and modern
  dictionaries as controls by fact and citation only), discloses the
  Basmalah's single mercy stem, the GAP policy, and carries the line:
  no claim is made that this is the first Erzya Quran translation.
- `GLOSSARY-MYV.md` — the attested vocabulary of record.
- `FLAGS-AND-GAPS-DISCLOSURE-MYV-2026-11-27.md` — census, flagged
  constructions, disclosures D1–D4, checker history.
- `REMEDIATION-LOG-MYV-2026-11-27.md` — every repair seat by seat.
- `CHECKER-REPORT-MYV-2026-11-27.md` — first independent checker: FAIL.
- `CHECKER-REPORT-RECHECK-MYV-2026-11-27.md` — re-check: remediation
  verified, one new homoglyph finding, FAIL.
- `CHECKER-REPORT-DELTA-MYV-2026-11-27.md` — final delta check: PASS.
- `MANIFEST.txt` — SHA-256 of every file above.

## Gate record

1. Machine count — PASS: 6,236 = 6,236 seats, seat-set equality with
   the Locked English Master (MD5 ecc5b8e2848e5044186b7ad82bed9f4e),
   per-surah grid clean at all 114.
2. Canonical verify — PASS: 1:1 equals the fixed Basmalah; the string
   "redacted" appears nowhere; no empty seats.
3. Purple sweep — reconciled: 8,164 distinct Cyrillic tokens, 3,047
   untraced candidates — an instrument candidate list dominated by
   regular inflected forms; two independent checkers spot-traced the
   top-30 tokens (30/30) and a random 30 candidates (28/30 regular,
   2 flagged minor formal irregularities) directly against the
   harvested inventory, and did not count the list against the build.
4. Independent checker — FAIL, then remediation, then re-check FAIL
   on a single new codepoint finding, then homoglyph repair, then
   final delta PASS. Repairs: знярдо (a form the build spec forbade
   by name) replaced by attested зярдо at all 318 occurrences;
   7:166 GAPped to match 2:65/5:60; 48:29 script corruption and
   garbled opening repaired; retained English "the" dropped at 8
   occurrences in 5 seats; clause repairs at 27:19, 5:110, 65:4,
   31:25, 22:5; 13 Cyrillic–Latin homoglyph tokens in 12 seats
   normalised to pure Cyrillic, codepoint sweep clean.
5. Fidelity — PASS: 52-verse first-checker sample plus a fresh
   24-verse re-check sample, weighted to long verses, no systematic
   dropping; the longest verse (2:282, 227 Master words) carried
   clause-complete.

## Notes

- This lane was a continuation: batches A–I (4,510 verses) stood
  complete from the first build crew, which timed out before
  finishing; batches J–M (1,726 verses) were built in this run.
- No PDF is included: the manuscript Markdown is the landed form,
  on the pattern of the Veps landing of the same night.
- Disclosures D1–D4 (мерсь usage, four inventory-attested loans,
  divine-epithet capitalisation, Latin vocative "O") stand in the
  flags disclosure and the remediation log.
