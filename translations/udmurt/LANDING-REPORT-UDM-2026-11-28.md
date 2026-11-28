# Landing Report — Udmurt (udm) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-UDM.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Udmurt, Cyrillic with
  the five extra letters Ӝ Ӟ Ӥ Ӧ Ӵ; GiellaLT lang-udm, LGPL v3,
  with its own untested-by-speakers caveat carried in the same
  breath; English Wiktionary, CC BY-SA, as attestation; the 2013
  complete Udmurt Bible as control by fact and citation only),
  discloses the single mercy stem in the Basmalah, the
  пайгамбар loan layer, and the GAP policy, and states that no
  first-translation claim is made.
- `quran-udm.txt` — the built book exactly as passed by the
  re-check, opening "QURAN — UDMURT DRAFT / DRAFT — NOT
  PUBLISHED" with its status note.
- `GLOSSARY-UDM.md` — the attested vocabulary of record,
  including the remediation disclosure of the compositional
  messenger seat ыстэм мурт.
- `CHECKER-REPORT-INDEPENDENT-2026-11-27.md` — first independent
  checker: FAIL, nine findings.
- `REMEDIATION-RECORD-2026-11-28.md` — every repair, seat by seat.
- `CHECKER-REPORT-RECHECK-2026-11-28.md` — fresh independent
  re-check of the remediated text: PASS, with three reservations
  (below).
- `ATTESTATION-AUDIT-2026-11-27.md` — seat-by-seat attestation
  audit, with its dated 2026-11-28 remediation addendum.
- `LICENCES-RECORDED-2026-11-27.md` and `BUILD-SPEC.md` — the
  licence record and the lane build spec of record.
- `MANIFEST.txt` — SHA-256 of every file above.

## Landing assembly note

The lane's companion manuscript file predated the 2026-11-28
remediation (it still carried the pre-remediation text and the
pre-remediation GAP census of 1,759 seats / 2,534 markers). The
shelf manuscript was therefore assembled at landing from the
remediated verse store — the files of record the re-checker
passed (`quran-udm.txt`, `quran-udm.json`, `verses-store.json`) —
preserving the companion front matter, with only its GAP census
figures updated to the verified post-remediation census. No
translation wording was edited in the assembly, and the lane's
own files were not altered.

## Gate record

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set equality
   with the Locked English Master exact; per-surah grid exact at
   all 114 surahs; no empty seats; the string "redacted" nowhere.
   Recount at landing, from the landed files themselves: 6,236
   numbered verse markers in both `quran-udm.txt` and
   `ayah-companion-manuscript-UDM.md`; first verse 1:1
   «Инмарлэн нимыныз, Гажась, Гажась.»; last verse 114:6
   «⟦GAP: jinn⟧ пӧлысь но калык пӧлысь.»
2. Canonical verify — PASS: 1:1 equals the fixed Basmalah;
   surah 9 carries no standalone Basmalah line; every other
   surah 2–114 carries exactly one.
3. Independent checker — FAIL (nine findings: four script
   contaminations; Russian-only letters ф х ц щ and silently
   seated Russian stems; the 18:25 number error; silent Russian
   seats in batches J and L; batch B GAP over-marking; the
   messenger seated three ways; Resurrection Day four ways and
   Holy Spirit three ways; the missing DRAFT — NOT PUBLISHED
   label; lesser fidelity deviations and Satan/devil name
   forms), then remediation of every verified finding, then a
   fresh independent re-check: PASS.
4. Purple sweep — reconciled: 5,364 untraced candidate types
   (29,225 occurrences), candidates only under house law; none
   of the first checker's flagged Russian forms appears in the
   regenerated list, independently confirmed by the re-checker's
   book-wide scans (zero ф/х/ц/щ tokens; zero occurrences of
   every flagged stem).
5. GAP census (post-remediation, recomputed by the re-checker
   and verified at landing in the verse body): 1,732 GAP-bearing
   seats, 2,430 GAP markers; 4,504 verses rendered in full. (The
   manuscript file counts one further ⟦GAP: …⟧, the explanatory
   example in its front matter.)

## The re-checker's three reservations, carried with the landing

These ride with the landing, as the re-check states them; none
blocks the PASS, and none is hidden.

1. **Residual GAP markers outside batch B.** 38 GAP markers for
   garden, wisdom, witness, and wise remain at seats outside
   batch B where сад, визь, and адӟись are seated elsewhere in
   the book (garden 14 markers; wisdom 18 markers at 17 seats;
   witness 5; wise 1 at 2:32). The re-checker rules them a
   recorded reservation, not a failure — a GAP marker invents
   nothing, borrows nothing silently, and misstates nothing —
   and recommends, without requiring, that the desk unify them
   onto сад, визь, and адӟись in a future consistency pass
   before any publication decision.
2. **The кушт- forgiveness system.** The stem кушт- (куштыны,
   "to cast away, reject" — the book's ordinary verb for
   rejecting the revelations at 335 seats) also serves as a
   forgiveness seat at a run of seats the remediation did not
   touch, because the first report named it only at 11:41: the
   epithet Куштӥсь renders "Forgiving" at, among others, 7:153,
   7:167, 8:69, 8:70, 9:5, 9:27, 9:91, 9:102, 10:107, 57:28,
   58:12, and 60:7; the noun куштон renders "forgiveness" at
   8:4, 8:33, 8:74, 9:80, 9:113, 11:3, 11:11, 11:52, and 63:5;
   and at person-object seats it reads as casting the person
   away rather than forgiving them, most plainly 7:151, where
   "forgive me and my brother" reads «монэ но мынам братме
   кушты». The re-checker grades it a lesser fidelity deviation
   at a larger scale than the single seat the first report
   sampled, and recommends a seat-by-seat review of the кушт-
   forgiveness seats against the book's own гажаса мозмыт- seat
   in a future pass.
3. **An unverified figure in the remediation record.** The
   record's figure of 322 ыстэм мурт occurrences could not be
   reproduced: the re-checker's own counts are 308 occurrences
   of the phrase ыстэм мурт in any capitalisation, including its
   case-inflected continuations, and 395 occurrences of the
   ыстэм stem in all its forms. The functional claim underneath
   the figure — one unified messenger seat at all 318 master
   messenger verses, zero GAP-messenger markers, zero
   пайгамбар-for-messenger — is verified in full, so the
   discrepancy is a defect in the record's arithmetic, not in
   the book; the number 322 itself stands unverified.

## Notes

- No PDF is included: the manuscript Markdown and the built
  text are the landed forms, on the pattern of the Erzya and
  Lule Sámi landings of 2026-11-27.
