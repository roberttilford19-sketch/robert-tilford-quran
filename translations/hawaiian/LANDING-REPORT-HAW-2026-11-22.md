# LANDING REPORT — Hawaiian (haw) Quran, 2026-11-22

**Authority.** Landed under Robert Tilford's Pipeline Landing
Authorization (2026-11-14), which covers Quran pipeline drafts that
complete build, count, canonical verify, independent checker, and
Purple sweep reconciled, together with his explicit build release
of this lane on 2026-11-22. The independent check passed before
landing (see the verification chain below), its prescribed
normalization pass and one-seat repair were completed and
re-verified before landing, and no seat was unsettled: GAP seats
are 0. Shelf folder 211 — 210 directories stood under
translations/ before this landing, and translations/hawaiian/
takes the next number.

**What landed** (translations/hawaiian/):
- ayah-companion-manuscript-HAW.md — the manuscript, byte-identical
  to the lane's normalized manuscript in ~/workspace/ayah-hawaiian/
  (SHA-256
  c7680617396312265d00ccf1e977c1211827f2be5335744938f7b1ac8e2b06b9,
  2,439,069 bytes, verified after copy and again live, below).
- Ayah_Companion_Tilford_Hawaiian_Manuscript.pdf — the reading
  edition, built by a new lane builder written for this landing
  (~/workspace/ayah-hawaiian/work/build_pdf_full.py), following the
  Ojibwe pattern (FPDF, Noto Serif + Noto Naskh Arabic,
  arabic_reshaper / bidi) at 6×9 in: title page, one status page
  carrying the honest status, acknowledgements page, contents,
  then all 114 surahs parsed from the assembled manuscript itself,
  so the PDF carries exactly the landed text: 738 pages; final
  surah present — the text layer carries 114:6, "Mai waena mai o
  ka jinn a mai waena mai o nā kānaka."; Arabic runs survive text
  extraction (635,461 Arabic-script characters counted in the
  extracted text; 0 replacement characters and 0 missing-glyph
  characters found in the extracted text; the ʻokina U+02BB
  survives extraction at 51,835 occurrences and the macron vowels
  survive, ā at 28,003).
- GLOSSARY-HAW.md — the lane glossary, unchanged.
- FLAGS-AND-GAPS-DISCLOSURE-HAW-2026-11-22.md — GAP seats, the
  flags record under both counting conventions, range_08 drafted
  new, the backup-file resolution, the restored 13:15 prostration
  note, the name normalization with its two intro-line exceptions,
  the 10:62 repair, the minor disclosed deviations, the 23:6 vs
  24:31 inconsistency, and the Purple caveat, named in one place.
- MANIFEST.txt — status, counts, and machine-computed file hashes.
- This report.

**Counts (machine-computed at landing).** 6,236 of 6,236 verses
rendered; GAP seats 0; per-surah counts matching the master grid
at all 114 surahs; Arabic per-verse byte-identical to the Master
across all 6,236 verses; Basmalah 113 standalone Arabic lines
(112 openings + 1:1), none at Surah 9; prostration notes 15/15
seat- and kind-exact; flagged verse references approximately
2,700 across 17 flags files (builder 2,709; checker 2,725 by
entry-leading references and 3,001 counting all references — a
counting-convention difference, disclosed in the disclosure file).

**Verification chain of record.** Build report
(BUILD-REPORT-HAW-2026-11-22.md, lane folder): counts reconciled
by count; range_08 (Surahs 21–24, 372 seats) drafted new, the
lane's only missing material; the backup-file correction recorded
(the set-aside backup duplicates range_15's span, not range_14's);
Purple sweep REPORT-only reconciled
(PURPLE-SWEEP-HAW-REPORT-2026-11-22.md — the shipped
purple_measure.py is hard-wired to 19 slice-structured lanes and
cannot measure this range-structured lane, so Purple's G7/G8
measures were applied directly in report mode; its one real
finding, the dropped prostration note at 13:15, was restored at
source and re-verified, notes now 15/15). Independent checker
(did not build the draft) PASS, 2026-11-22
(CHECKER-REPORT-HAW-2026-11-22.md): every count recomputed
mechanically and exact; Arabic byte-identical 6,236/6,236; the
backup resolution verified seat by seat (manuscript follows
range_15 at all 336 seats where range_15 and the backup differ,
the backup in 0); 40-verse fidelity sample graded 35 sound, 4
sound-with-disclosed-weakness, 1 partial (10:62), 0 meaning
breaks, 0 inventions; G7's 5,033 candidate hits reproduced
exactly as the Hawaiian words he and no. Correction chain: the
checker's prescribed normalization pass and one-seat repair were
applied to the assembled manuscript only
(CORRECTION-HAW-NAMES-2026-11-22.md: 83 name occurrences unified
across 19 names to one spelling per name in verse bodies,
including two spellings found by the pass beyond the checker's
table — Thamud's fifth at 85:18 and Aad's fourth at 69:4/69:6;
the two intro-line exceptions, Surah 7 "Adamu" and Surah 28
"ʻAigupita", left as they stand; the 10:62 opener repaired from
"He ʻoiaʻiʻo ʻole" to "He ʻoiaʻiʻo") and re-verified mechanically
in full: counts unchanged, Arabic diff still 0, exactly one
spelling per name in every verse body. The landed manuscript is
the normalized manuscript.

**Commits.** The landing commit is
fbac6acb7c48e5fc31c3b25a2dde88a67332f546 ("Hawaiian Quran landed —
full draft of the Locked English Master, checker PASS, name
normalization applied (2026-11-22)"), pushed to origin. This
report lands in the commit that carries it, completing the
landing series. Note on the branch: this repository's branch of
record is main (origin/HEAD → origin/main); the landing was
pushed to main.

**Live verification.** After the push, the manuscript was fetched
back from GitHub raw
(https://raw.githubusercontent.com/roberttilford19-sketch/robert-tilford-quran/main/translations/hawaiian/ayah-companion-manuscript-HAW.md)
and its SHA-256 is
c7680617396312265d00ccf1e977c1211827f2be5335744938f7b1ac8e2b06b9 —
identical to the local normalized copy, at the same 2,439,069
bytes. The remote folder listing (git ls-tree origin/main) shows
the pack files on the shelf.

**Status language.** This text is a machine-assisted draft by
non-speakers under Robert Tilford's direction. It is NOT
speaker-reviewed; no native or critic review is awaited, invited,
or chased (Robert's ruling, 2026-11-18). No outreach was made to
any speaker or community about this book. The only firstness
claim is the bounded form: first complete Hawaiian Quran
translation found — after research.

**Gift terms**, as every folder on this shelf: free to read and
free to download, never sold; attribution requested.
