# BUILD RECORD — Pfälzisch Quran, 2026-11-23

**The book:** *De Quran óf Pälzisch* — the Quran in Pfälzisch (Palatine), the ancestral tongue of Victoria/Herzog and Catherine, Ellis County, Kansas. It is **not** Volga German and is never so labelled — not in the text, not in the front matter (which states the distinction in so many words), and not in the shelf record. Status: **DRAFT — NOT PUBLISHED.** The dedication page stands as a marked empty place; Robert ruled no dedication for this lane.

**Authority:** Robert's ruling A, main chat, 2026-11-23 01:58 CST — "Open the Pfälzisch lane now on the pins as they stand." Source record: `GATE-PINS-PF-2026-11-23.md`; sources note: `SOURCES-NOTE-PF-2026-11-23.md`.

## Sources as used

- **Base:** the Locked English Master (`~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md`, post-"Scriputure"-correction state, 3,270,474 bytes at build time), parsed to 114 surahs / 6,236 verses with per-surah counts reconciled against the master's own name lines, zero mismatches.
- **Control:** Dieter Zimmer, *Es Neie Teschdament — Es lewenniche Wort (ELW)*, text status May 2021 — a complete Westpfälzisch New Testament, held at `sources/Neues_Testament_westpfaelzisch_2021_05.pdf` (881 pages; the publisher's own file, taken from the Internet Archive Wayback Machine snapshot after the live evpfalz.de path began returning the site's 404 page). NT-only and West Palatine in centre; both limits are named in the book's front matter and in the shelf record. © Dieter Zimmer, all rights reserved — used as a control only: read for forms and terminology, never reproduced. Its text was extracted to a 13,266-form attestation lexicon.
- **Dictionary:** the *Pfälzisches Wörterbuch* at the Trierer Wörterbuchnetz (woerterbuchnetz.de) — complete across the alphabet behind a one-lemma-at-a-time interface, no bulk file. The road taken: the build's terminology was seated in the control's attested vocabulary first; dictionary-interface spot checks settled the seats the brief named in advance (Häll/Höll — in the event settled by the control itself, Häll 34× against Höll 0×). The interface road and its limit are disclosed in the front matter. No bulk dictionary data was taken, and none is claimed.

## Build

Seventeen chunk workers translated the 114 surahs from the brief (`work/BRIEF-PF.md` — locked terminology seated in the control's own words, attested forms only, gaps bracketed and flagged, never invented), reporting verse counts summing to exactly 6,236. Assembly by script (`work/assemble.py`); Arabic reinserted programmatically from the master parse, never retyped. A pre-corrections copy stands at `work/QURAN-PFALZISCH-PRE-CORRECTIONS.md`.

## Gates, in order

1. **Count and canonical verify** (`work/verify.py`) — verse sequence identical to the master, 6,236/6,236; per-surah 114/114; Arabic 6,348 lines sequence byte-identical; Basmalah uniform (112 italic head lines + 1:1 + 27:30 = 114 locked-line occurrences); sajda apparatus 15/15 at the master's seats; no zakat percentage. **ALL PASS**, before and after corrections.
2. **Desk conform rounds** — 4,212 replacements seating the text in the governing combined-2021 orthography (CORRECTIONS-PF §A).
3. **Independent checker** (did not build the text) — **PASS WITH CORRECTIONS**: language sample 19 (a) / 19 (b) / 2 (c) of 40; fidelity clean of imported doctrine in 10 verses; 24 required corrections, every prescribed form grep-verified in the control. Report: `CHECKER-REPORT-PF-2026-11-23.md`. All 24 applied (2,003 replacements; CORRECTIONS-PF §B–C), battery re-run clean.
4. **Attestation** — 83.63% of the book's tokens against the control's lexicon, stated as a floor (the lexicon's tokenisation splits some of the control's own words; see FLAGS-PF.md).
5. **GAP seats** — 311 stand open, every one graded a true gap by the checker or a disclosed device; no word was invented anywhere in the book.

## Final manuscript

`QURAN-PFALZISCH-2026-11-23.md` — 2,291,240 bytes, SHA-256 `6b3a57a7c44235476ff04a772ac58e445eeb49c104ee57f71bc94d8228ff00cb`.

## Shelving

Shelved under the Pipeline Landing Authorization (2026-11-14) on the GitHub Quran shelf at `translations/pfalzisch/`, with the lane's records. Nothing posted, sent, or published; the book's status travels as DRAFT — NOT PUBLISHED.
