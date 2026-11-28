# Landing Report — Meadow Mari (mhr) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-MHR.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Meadow Mari, олык
  марий, ISO 639-3 mhr — the Yoshkar-Ola-based literary
  standard, in Cyrillic with ҥ, ӧ, ӱ, fenced distinct from
  Hill Mari; GiellaLT giella-mhr, LGPL v3, and the Meadow Mari
  lexicon of English Wiktionary, CC BY-SA, as attestation
  sources, with the Vienna Mari–English Dictionary, the Corpus
  of Literary Mari, the Yoshkar-Ola dictionary, and the modern
  Meadow Mari New Testament as controls by fact and citation
  only), discloses the Basmalah's single mercy stem, the GAP
  policy, and the flagged seats, and states that no claim is
  made that this is the first Meadow Mari Quran translation.
- `quran-mhr.txt` and `quran-mhr.json` — the built book exactly
  as passed by the re-check. Recount at landing, from the lane
  files of record: all 6,236 store verse texts stand verbatim
  in both the built text and the companion manuscript
  (0 missing from either).
- `glossary.md` — the attested vocabulary of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — first independent
  checker: FAIL.
- `REMEDIATION-RECORD-2026-11-28.md` — every repair, seat by seat.
- `CHECKER-REPORT-RECHECK-2026-11-28.md` — fresh independent
  re-check of the remediated text: PASS, with the held
  uncertainty carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-MHR-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `ATTESTATION-AUDIT-2026-11-28.md` — seat-by-seat attestation
  audit.
- `LICENCES-RECORDED-2026-11-28.md` and `BUILD-SPEC.md` — the
  licence record and the lane build spec of record.
- `MANIFEST.txt` — SHA-256 of every file above.

## Gate record

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set exactly
   equal to the Locked English Master (no seat in either
   direction); per-surah grid exact at all 114 surahs;
   `quran-mhr.json` flattened is text-identical to the verse
   store at every seat (0 differences); no empty seats; the
   string "redacted" appears in no seat and in neither
   assembled file. First verse 1:1 «Юмын лӱмеш, Серлагыш,
   Серлагыш.»; last verse 114:6 «⟦GAP: jinn⟧ кокла гыч да
   еҥ-влак кокла гыч.”»
2. Canonical verify — PASS: 1:1 equals the fixed Basmalah form
   exactly; the full Basmalah string occurs exactly 114 times
   in `quran-mhr.txt` and exactly 114 times in
   `ayah-companion-manuscript-MHR.md` (112 unnumbered openings
   + 1:1 + the in-verse quotation at 27:30 — the only two
   store seats containing the string are 1:1 and 27:30, both
   correct); the embedded duplicate opening lines at 7:1, 8:1,
   and 10:1 found by the first checker are gone.
3. Independent checker — FAIL (the Basmalah duplicates; five
   mixed-script corrupted tokens at 39:21, 39:30, 42:12,
   42:34, 43:83; the н-for-ҥ victory-stem class; unattested
   seatings including the нуждалык / нужда forms and the
   Мукш coinage at 17:1; the four-way mosque split; the
   Surah 48 victory seats and the 48:27 hair seat), then
   remediation of every verified finding, then a fresh
   independent re-check: PASS — every defect class repaired
   and verified seat by seat, and no new defect found. The
   re-check also ruled on the recorded нужналык nuance: the
   remediation's reseats are upheld on the inventory evidence
   (the Giella inventory holds нужналык glossed "poverty" and
   holds neither нуждалык nor нужда in any form; the
   replacement forms are themselves attested, so the text as
   rebuilt is attested under either reading).
4. Purple sweep — reconciled: 7,509 distinct Cyrillic tokens,
   122,571 Cyrillic tokens in all, 1,413 untraced candidate
   types (13,326 occurrences) — candidates only under house
   law; none of the repaired defect forms appears in the
   candidate list, and every replacement form traces.
5. GAP census (post-remediation, recomputed by the re-checker
   and verified at landing in the verse store): 298 GAP seats,
   339 GAP markers; 5,938 verses rendered in full. By term:
   scripture ×107, hell ×97, jinn ×32, covenant ×24, mosque
   ×20, pilgrimage ×16, usury ×8, Sabbath ×7, Umrah ×3, debt
   ×3, dowry ×2, fly ×2, and ×1 each for manna, cucumbers,
   garlic, lentils, onions, witchcraft, swine, gambling, Ark,
   donkey, palms, vines, martyrs, synagogue, olive, hail,
   palm, and hoopoe. (The manuscript file counts one further
   ⟦GAP: …⟧, the explanatory example in its front matter.)
6. Mosque unified to GAP — PASS: the Master names a mosque in
   exactly 19 seats; every one now carries ⟦GAP: mosque⟧,
   for 20 markers in all (17:1 carries two); мечеть occurs in
   no seat.
7. Hill Mari bar — PASS: no token or character ӓ, ӹ, Ӓ, or Ӹ
   in the verse store or in `quran-mhr.txt`; in the assembled
   manuscript ӓ and ӹ occur only inside the English
   front-matter paragraph that names the Hill Mari alphabet
   in order to fence it off — mentioned, never seated.

## Held uncertainty carried with the landing

**The ашындыр- allomorph.** ашындыр- occurs 22 times in 20
seats, unchanged by the remediation. The harvested inventory
holds only ашындараш. Whether the allomorph is a regular Mari
vowel alternation cannot be settled from the harvested
inventories; it remains a question for a Mari proofreader,
disclosed in the flags-and-gaps disclosure's open-seat record.
The original checker held it as a proofreader uncertainty, not
a failure, and the re-check holds it the same way; it does not
block the PASS and it is not hidden.

The re-check's recorded minor items also stand as recorded and
do not block the verdict: the Latin "Quran" (54 occurrences by
token count) beside Cyrillicised Коран, and the
early-hyphenated / later-fused name suffixes (≈49 fused tokens,
surahs 38–54).

## Notes

- No PDF is included: the manuscript Markdown, the built text,
  and the built JSON are the landed forms, on the pattern of
  the Erzya and Udmurt landings.
