# LANDING REPORT — Ojibwe (Anishinaabemowin) (oj) Quran, 2026-11-22

**Authority.** Landed under Robert Tilford's Pipeline Landing
Authorization (2026-11-14), which covers Quran pipeline drafts that
complete build, count, canonical verify, independent checker, and
Purple sweep reconciled, together with his explicit build release
of this lane on 2026-11-22. The independent check passed before
landing (see the verification chain below), its one prescribed
correction was completed and re-verified before landing, and no
seat was unsettled: GAP seats are 0. Shelf folder 210 — 209
directories stood under translations/ before this landing, and
translations/ojibwe/ takes the next number.

**What landed** (translations/ojibwe/):
- ayah-companion-manuscript-OJ.md — the manuscript, byte-identical
  to the lane's corrected manuscript in ~/workspace/ayah-ojibwe/
  (SHA-256
  285ed1b3a9860e5c79d00de82d697ecbd13bb347e305aef73bac1abeb89442ad,
  2,359,833 bytes, verified after copy and again live, below).
- Ayah_Companion_Tilford_Ojibwe_Manuscript.pdf — the reading
  edition, built by a new lane builder written for this landing
  (~/workspace/ayah-ojibwe/work/build_pdf_full.py), following the
  Scots pattern (FPDF, Noto Serif + Noto Naskh Arabic,
  arabic_reshaper / bidi) at 6×9 in: title page, one status page
  carrying the honest status, acknowledgements page, contents,
  then all 114 surahs parsed from the assembled manuscript itself,
  so the PDF carries exactly the landed text: 782 pages; final
  surah present — the text layer carries 114:6, "Wenjiik Jinn,
  wenjiik anishinaabeg."; Arabic runs survive text extraction
  (635,514 Arabic-script characters counted in the extracted
  text; 0 replacement characters and 0 missing-glyph characters
  found in the extracted text).
- GLOSSARY-OJ.md — the lane glossary, unchanged.
- FLAGS-AND-GAPS-DISCLOSURE-OJ-2026-11-22.md — GAP seats, the
  flags record, the duplicate-seat resolutions, surah 4 and its
  PARTIAL seat, the checker sample PARTIALs, the carried
  variations, the name correction, and the variety and Purple
  caveats, named in one place.
- MANIFEST.txt — status, counts, and machine-computed file hashes.
- This report.

**Counts (machine-computed at landing).** 6,236 of 6,236 verses
rendered; GAP seats 0; per-surah counts matching the master grid
at all 114 surahs; Arabic per-verse character-identical to the
Master across all 6,236 verses (diff 0); Basmalah 113 standalone
Arabic lines (112 openings + 1:1) with 112 byte-identical Ojibwe
openings, none at Surah 9; flag entries 3,094 in 63 flags files
(the checker's corrected file count).

**Verification chain of record.** Build report
(BUILD-REPORT-OJ-2026-11-22.md, lane folder): counts reconciled
by count; duplicate-seat resolutions recorded; surah 4 drafted
new (176 verses, the lane's only missing material); Purple sweep
REPORT-only reconciled (PURPLE-SWEEP-OJ-2026-11-22.md — the
shipped purple_measure.py is hard-wired to 19 other lanes and
cannot measure this one, so Purple's measures were applied
directly). Independent checker (did not build the draft) PASS,
2026-11-22 (CHECKER-REPORT-OJ-2026-11-22.md): every count
recomputed mechanically and exact; duplicate resolutions verified
seat by seat with no blends; 45-verse fidelity sample graded
42 PASS, 3 PARTIAL (4:24, 7:54, 75:1), 0 failures. Correction
chain: the checker's one prescribed correction — English
proper-name spellings at 8 seats in surah 2 — was applied to the
assembled manuscript only (CORRECTION-OJ-NAMES-2026-11-22.md:
8 seats, 12 substitutions to the brief's locked forms) and
re-verified mechanically in full: counts unchanged, Arabic diff
still 0, and the post-correction scan found 0 English brief-list
names remaining.

**Commits.** The landing commit is
305f21c382b6de7046bc6c97ffafdcb3a5a6f1f4 ("Ojibwe Quran landed —
full draft of the Locked English Master, strict double-vowel
orthography, checker PASS (2026-11-22)"), pushed to origin. This
report lands in the commit that carries it, completing the
landing series. Note on the branch: this repository's branch of
record is main (origin/HEAD → origin/main); the landing was
pushed to main.

**Live verification.** After the push, the manuscript was fetched
back from GitHub raw
(https://raw.githubusercontent.com/roberttilford19-sketch/robert-tilford-quran/main/translations/ojibwe/ayah-companion-manuscript-OJ.md)
and its SHA-256 is
285ed1b3a9860e5c79d00de82d697ecbd13bb347e305aef73bac1abeb89442ad —
identical to the local corrected copy, at the same 2,359,833
bytes. The remote folder listing (git ls-tree origin/main) shows
the pack files on the shelf.

**Status language.** This text was machine-assisted by
non-speakers of Ojibwe under Robert Tilford's direction. It is
NOT speaker-reviewed; no native or critic review is awaited,
invited, or chased (Robert's ruling, 2026-11-18). The Quiet
Protocol for Indigenous North America stands: no outreach was
made to any speaker, tribe, or community about this book. No
first-translation claim beyond the bounded form: first complete
Ojibwe Quran translation found — after research.

**Gift terms**, as every folder on this shelf: free to read and
free to download, never sold; attribution requested.
