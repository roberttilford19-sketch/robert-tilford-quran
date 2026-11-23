# LANDING REPORT — Bislama (bis) Quran, 2026-11-23

**Authority.** Landed under Robert Tilford's Pipeline Landing
Authorization (2026-11-14), which covers Quran pipeline drafts that
complete build, count, canonical verify, independent checker, and
Purple sweep reconciled, together with his explicit build word of
2026-11-23 (build all six census-buildable lanes). The independent
checker passed with corrections before landing (see below), every
required correction was applied and re-verified, and no seat was
unsettled: GAP seats are 0. Shelf folder 214 — 213 directories stood
under translations/ before this landing, and translations/bislama/
takes the next number.

**What landed** (translations/bislama/):
- ayah-companion-manuscript-BIS.md — the manuscript, byte-identical
  to the lane's corrected manuscript in ~/workspace/ayah-bislama/
  (SHA-256 1550acba36a452e810c692b25bd5a439d7b1bc05632798c3335e6be286c4c33e,
  2,426,615 bytes).
- GLOSSARY-BIS.md — consolidated from all seventeen range flags
  files (NAMES USED and TERMS records preserved as written).
- FLAGS-AND-GAPS-DISCLOSURE-BIS-2026-11-23.md — GAP seats (0), the
  flags record, the carried seats (divine "We" as Mifala; the
  gaedens/jajmen/kingdom/spring residue), and the status, named in
  one place.
- CHECKER-REPORT-BIS-2026-11-23.md — the independent checker's report.
- MANIFEST.txt — status, counts, and machine-computed file hashes.
- This report.

**Counts (machine-computed at landing).** 6,236 of 6,236 verses
rendered; GAP seats 0; per-surah counts matching the master grid at
all 114 surahs; verse markers in exact master sequence; Arabic
per-verse byte-identical to the Locked English Master across all
6,236 verses (grid check); Basmalah 113 standalone Arabic lines
(112 openings + 1:1), none at Surah 9, with 112 locked Bislama
Basmalah lines; prostration notes 15/15 (11 recommended, 4
obligatory); surah headings 114; placeholder scan clean.

**Verification chain.** Build (17 worker ranges, Arabic copied
programmatically from the master) → desk count/canonical verify
(one defect caught and repaired at 13:15, Arabic restored, grid
re-verified) → Purple sweep, REPORT mode only
(PURPLE-SWEEP-BIS-REPORT-2026-11-23.md in the lane folder) →
independent checker PASS WITH CORRECTIONS (language sample 40:
(a) 28, (b) 12, (c) 0; attestation 86.71% strict / 92.48% with core
function words; spot fidelity 8 of 10 faithful, 2 defects corrected)
→ all seven required corrections applied verse-scoped and the full
battery re-run clean (CORRECTIONS-BIS-2026-11-23.md in the lane
folder).

**Pillars.** Bislama Spelling Dictionary (Moon et al., Government of
Vanuatu, 2007, GPL v2) via bislama.org — spellings and attestation
only; Crowley's A New Bislama Dictionary is the spelling reference
behind it and is print/borrow-only, not claimed as open. Control:
Baebol long Bislama (Bible Society of the South Pacific, 1997; rev.
2012), open text.

**Status.** DRAFT — NOT SPEAKER-REVIEWED. Machine-assisted draft by
non-speakers under Robert Tilford's direction, labelled as such in
the manuscript's own front matter. No outreach was made to any
speaker or community about this book. Firstness in the bounded form
only: the first complete Bislama Quran translation found — after
research.

Translated by Robert Tilford. © 2026 Robert Tilford.
Gift terms, as every folder on this shelf: free to read and free to
download, never sold; attribution requested.
