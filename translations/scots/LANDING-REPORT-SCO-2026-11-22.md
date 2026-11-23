# LANDING REPORT — Scots (sco) Quran, 2026-11-22

**Authority.** Landed under Robert Tilford's Pipeline Landing
Authorization (2026-11-14), which covers Quran pipeline drafts that
complete build, count, canonical verify, independent checker, and
Purple sweep reconciled, together with his explicit build release
of this lane on 2026-11-22. The independent check passed before
landing (see the verification chain below), and no seat was
unsettled: GAP seats are 0. Shelf folder 209 — 208 directories
stood under translations/ before this landing, and
translations/scots/ takes the next number.

**What landed** (translations/scots/):
- ayah-companion-manuscript-SCO.md — the manuscript, byte-identical
  to the lane's governing built text in ~/workspace/ayah-scots/
  (SHA-256
  5126aebcfcfd1a68496e8af20b3d2736ff109f1037e9a17f73ab6a23fa076d00,
  verified after copy and again live, below).
- Ayah_Companion_Tilford_Scots_Manuscript.pdf — the reading
  edition, built by the lane's own pattern extended from the sample
  builder (FPDF, Noto Serif + Noto Naskh Arabic, arabic_reshaper /
  bidi) at 6×9 in: title page, one status page carrying the honest
  status, acknowledgements page, contents, then all 114 surahs from
  work/meta.json and the work/sco/ slices: 691 pages; final surah
  present — the text layer carries 114:6, "Frae amang jinn an amang
  fowk."; Arabic runs survive text extraction (no missing-glyph
  boxes, no replacement characters found in the extracted text).
- GLOSSARY-SCO.md — the lane glossary, unchanged.
- FLAGS-AND-GAPS-DISCLOSURE-SCO-2026-11-22.md — the declared norm,
  every declared ruling and judgment call, the identical-verse
  residue, and the checker anomalies, named in one place.
- MANIFEST.txt — status, counts, and machine-computed file hashes.
- This report.

**Counts (machine-computed at landing).** 6,236 of 6,236 verses
rendered; GAP seats 0; per-surah counts matching the master grid at
all 114 surahs; Arabic runs 6,462 of 6,462; prostration markers 15
of 15 at the master's seats; Basmalah 112 standalone + 1:1, none at
Surah 9; 0 [MISSING]; 0 "%" anywhere in the manuscript.

**Verification chain of record.** Build report
(BUILD-REPORT-SCO-2026-11-22.md, lane folder): counts reconciled by
count, English-leak scan disclosed (158 word-for-word identical
short verses, longest 18 words at 42:19; 47 near-identical), Purple
sweep REPORT-only reconciled (Basmalah 115 = 112 standalone + 1:1 +
27:30 + 1 front-matter quotation; G7 function-word figure 33,634
read as shared Scots/English vocabulary, not collapse).
Independent checker (did not build the draft) PASS, 2026-11-22
(CHECKER-REPORT-SCO-2026-11-22.md): every count recomputed
mechanically and exact; 40-verse language sample graded (a) 32,
(b) 7, (c) 1 — (a)-dominant; identical-verse claim reproduced
exactly. Checker anomalies carried in the disclosure: possessive
"Lord's" unconverted at 35:39 and 53:55; 59:22 "the Compassionate,
the Compassionate" for two distinct master epithets; the
master-side typo "Scriputure" at 5:65 carried faithfully under the
source lock — a Locked English Master item, not a Scots defect.

**Commits.** The landing commit is
06cbac2d5d714d4aa7c50659f6433cbd75684058 ("Scots Quran landed —
full draft of the Locked English Master, declared Modern literary
Scots norm, checker PASS (2026-11-22)"), pushed to origin. This
report lands in the commit that carries it, completing the landing
series. Note on the branch: this repository's branch of record is
main (origin/HEAD → origin/main); the landing was pushed to main.

**Live verification.** After the push, the manuscript was fetched
back from GitHub raw
(https://raw.githubusercontent.com/roberttilford19-sketch/robert-tilford-quran/main/translations/scots/ayah-companion-manuscript-SCO.md;
the same path under master also resolves) and its SHA-256 is
5126aebcfcfd1a68496e8af20b3d2736ff109f1037e9a17f73ab6a23fa076d00 —
identical to the local copy, at the same 2,213,312 bytes. The
remote folder listing (git ls-tree origin/main) shows the pack
files on the shelf.

**Status language.** This text was machine-assisted by
non-speakers of Scots under Robert Tilford's direction. It is NOT
speaker-reviewed; no native or critic review is awaited, invited,
or chased (Robert's ruling, 2026-11-18). Declared norm: Modern
literary Scots, DSL-disciplined. No first-translation claim beyond
the bounded form: first complete Scots Quran translation found —
after research.

**Gift terms**, as every folder on this shelf: free to read and
free to download, never sold; attribution requested.
