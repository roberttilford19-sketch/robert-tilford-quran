# Landing Report — Veps (vep) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-VEP.md` — the book: 6,236 verses on the standard
  grid; 5,678 fully rendered; 558 verses carrying 768 visible ⟦GAP: …⟧ markers.
  Front matter names the base honestly (modern literary Veps, Latin script,
  Central-based, Kodima/Zaitseva norm, with the candidate brief's §2 dissent
  carried on the face), states the fact-and-citation-only use of the Veps New
  Testament and Psalms, discloses the checker/source overlap, and carries the
  line: no claim is made that this is the first Quran translation into Veps.
- `GLOSSARY-VEP.md` — the attested vocabulary of record, §§A–K.
- `FLAGS-AND-GAPS-DISCLOSURE-2026-11-27.md` — census, flagged constructions,
  judgment seats, checker history, referred items.
- `REMEDIATION-LOG-2026-11-28.md` — the remediation record with dated addenda.
- `CHECKER-REPORT-2026-11-27.md` — the first checker's FAIL of the first build.
- `CHECKER-REPORT-REMEDIATION-2026-11-28.md` — first remediation checker pass.
- `CHECKER-REPORT-DELTA4-2026-11-28.md` — the final pass: every gate PASS.
- `MANIFEST.txt` — SHA-256 of every file above.

## Gate record

1. Canonical verify — PASS: 6,236 = 6,236 seats, per-surah mismatches none,
   U+02B9 apostrophes only, 1:1 = seated basmalah, angel seats 86.
2. GAP census reconciled — PASS: frozen 495/692/323 → landed 558/768/330,
   every movement traced (see remediation log).
3. Fences — PASS: no "first" claim anywhere; Uz' Zavet wording only as the
   recorded short citation phrases in the audit documents, none in the text.
4. Fidelity — PASS: fresh 46-verse sample weighted to long verses, zero
   failures; the 18 originally failed verses re-rendered and re-checked.
5. Token adjudication — PASS at the fourth checker round: the 22 SUSPECT
   families and every residue class found by successive checkers (capitalized
   Päiči/Jokčč-/Kärsi/Hüvästa/Maista, free päi, sanug participles, palʹm-,
   voitt-, bare selʹgenz-, Joka, Silloin, Päinvastoin, Olles, Sama, Vird, Saan)
   stand at zero on a case-insensitive full-book sweep, independently replicated
   with a sentence-initial hunt over 882 forms.

## Remediation totals

2,266 of 6,236 verses changed against the frozen first build; 1,556 fully
re-rendered from the Locked English Master. Disciples seated as openikad at
3:52, 5:111, 5:112 on the checker's three-source verification. Stems replaced
with attested forms: the kelʹta, tirpta, selʹged, mujada, jogahine, mir/kožmuz,
vägest-, päzu-, kitta families and the -nug → -nuded participle norm (151 tokens
in the final sweep alone). Seats GAPped where no attested replacement exists:
blessed (5), inheritance (89:19), and the fidelity-surfaced terms (tar, ants,
spider, bee, hoopoe, breastfeeding, bush, bricks, pens, armor, statues, palm).

## Notes

- No PDF is included: no PDF engine (pandoc/typst/LaTeX) is installed on the
  desk machine at landing time. The manuscript Markdown is the landed form.
- No concordance was built for this lane; none was among its gates.
- Referred ungraded items (küž- variant; epäil-, valehtelij-, ihmeh-, hänelle,
  judalai- families) stand on the record for a future adjudication.
