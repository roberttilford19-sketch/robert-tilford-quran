# LANDING REPORT — Upper Sorbian (hsb) Quran

Landed 2026-11-27 under the Pipeline Landing Authorization, on the
authority of Robert Tilford's ruling of 2026-11-27 (21:16 CST)
adopting the desk recommendations in CANDIDATE-BRIEF-UPPER-SORBIAN
wholesale, under the brief's conditions. Status of the book:
DRAFT — NOT PUBLISHED.

## What landed

translations/upper-sorbian/ on the robert-tilford-quran shelf:
- ayah-companion-manuscript-HSB.md — the book: 6,236 verses,
  6,137 fully rendered, 99 seats carrying 117 visible ⟦GAP: …⟧
  markers. MD5 3cfca93bcf7b36358a000b66da6f87a4.
- GLOSSARY-HSB.md — the seat table every form traces to.
- FLAGS-AND-GAPS-DISCLOSURE-2026-11-27.md — every gap,
  construction, descriptive device, and the full checker history.
- CAPTION-UPPER-SORBIAN-2026-11-27.md — a draft post for Robert's
  hand. DRAFT — NOT POSTED; posting is his alone.
- MANIFEST.txt — the shelf record with file hashes.

No PDF stands in this folder: no PDF toolchain was present in the
build environment at landing. The manuscript is the book of record;
a PDF is owed when the house's PDF road is next run, and this
report names that debt rather than hiding it. No Google Drive copy
was made: Drive stacking stands stopped under Robert's ruling
(resume only on his fresh word).

## The gates, and how each closed

- Licences (brief condition 1): recorded before reliance in
  LICENCES-RECORDED-2026-11-27.md — Soblex database in-copyright,
  fact/citation only; its GPL v3 spellchecker inventory for
  spelling/attestation-pointing; HOTKO not a build base (no open
  licence); Wiktionaries and hsb Wikipedia CC BY-SA as
  fact/citation and frequency pointing; PD dictionaries and PD
  Bibles as the control.
- Modern-Bible boundary (condition 2): public-domain Bibles
  (1728–1905) alone as control; the 2006 Catholic Bible in
  copyright, not consulted, no contact made (condition 4 likewise:
  silent build-and-gift on public sources).
- Attestation audit (condition 3): ATTESTATION-AUDIT-2026-11-27.md
  — core terms seated with sources named; usury, jinn, hypocrite,
  adultery held as standing GAPs; zakāh and pilgrimage on
  disclosed descriptive devices.
- Translation: twelve batches from the Locked English Master
  (MD5 ecc5b8e2848e5044186b7ad82bed9f4e) under BUILD-SPEC.md,
  including its mandatory fidelity protocol (element inventory,
  clause-by-clause rendering, no pronoun substitution, length
  sanity, surah self-check).
- Machine count: 6,236 verses; canonical verify PASS at every
  pass; Purple sweep reconciled (verify.py: canonical PASS,
  artefact scan PASS, character audit 0 after remediation,
  SUSPECT candidates adjudicated by family at each checker pass).
- Independent checker: three passes by checkers that built
  nothing. Pass 1 FAIL (token adjudication); remediation round 1
  (268 seats, checker-prescribed). Pass 2 FAIL (token
  adjudication, second residue found by a fuller census);
  remediation round 2 (80 seats). Pass 3 (CHECKER-REPORT-3.md):
  ALL SEVEN CHECKS PASS — canonical; fidelity (0 content losses
  in 140 verses read, including every repaired seat); token
  adjudication (full codepoint census clean but for Q/V in the
  Master's carried names); GAP census (117 markers, 99 seats,
  reconciled); constructions; fences (no "first" wording; Bóh
  stands, zero "Allah"); grammar. Verdict: LAND.
- Novelty wording (condition 6): none anywhere in the book or
  this pack. No "first" claim is made.

## Landing verification (desk, at landing)

Manuscript verse markers counted in the built text: 6,236; first
1:1 ("W mjenje Boha, Miłosćiweho, Smilneho."), last 114:6.
Front-matter counts computed from the store at assembly agree
with the third checker's census. The commit and push for this
folder, with explicit-path staging, are recorded in the lane
build log (UPPER-SORBIAN-BUILD-LOG-2026-11-27.md in the
endangered-language goal's hidden_files) together with the
origin verification.

Translated by Robert Tilford. © 2026 Robert Tilford.
Gift terms, as every folder on this shelf: free to read and free
to download, never sold; attribution requested.
