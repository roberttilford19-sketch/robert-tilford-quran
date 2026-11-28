# Landing Report — Southern Sámi (sma) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-SMA.md` — the book in companion manuscript form: 6,236 verses on the standard grid. Its front matter carries DRAFT — NOT PUBLISHED on its face, states the machine-rendered first-pass nature, the GAP census, and the Sámi fence, and makes no "first translation" claim of any kind.
- `quran-sma.txt` and `quran-sma.json` — the built book exactly as passed by the independent checker.
- `glossary.md` — the attested vocabulary of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — the fresh independent checker report: PASS-WITH-GAP-TIER-RESERVATION.
- `FLAGS-AND-GAPS-DISCLOSURE-SMA-2026-11-28.md` — census, flagged constructions, and disclosures.
- `LICENCES-RECORDED-2026-11-28.md` and `BUILD-SPEC.md` — the licence record and the lane build spec of record.
- `BUILD-REPORT.md` — the build report of record.
- `MANIFEST.txt` — SHA-256 of every file above.

All copies in this folder were verified byte-identical to the lane originals in `~/workspace/ayah-southern-sami/` at landing.

## Gate record

All figures below were re-verified at landing by this desk's own count from the lane files, not taken from the checker report alone; every figure matched exactly.

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set equality store == master == quran-sma.json TRUE on all pairs, and quran-sma.json texts identical to verses-store.json texts at every seat; per-surah grid exact; no empty seats; no 'redacted' seats.
2. Canonical verify — PASS: 1:1 == «Nomme Jupmele, Åårmegs, Åårmegs.»; 1:3 == «Åårmegs, Åårmegs.» exactly; quran-sma.txt carries exactly 112 unnumbered Basmalah lines (every surah except 1 and 9 carries one; surah 9 carries none).
3. Independent checker — PASS-WITH-GAP-TIER-RESERVATION (fresh independent checker, 2026-11-28, who built none of this text): every mechanical claim recomputed exactly, the Sámi fence holds, and the labelling is honest.
4. Dictionary and attestation — CONFIRMED: work/eng2sma.json carries 4,308 English seat keys; the attestation inventory carries 57,160 forms (GiellaLT lang-sma lexc stems 55,600 plus the 2022 dictionary's 6,808, less the 5,248 forms present in both); every eng2sma value traces to the inventory; the one dropped unverified seat (revelation → volverimmie) is absent from the dictionary and the draft.
5. GAP census — CONFIRMED figure for figure: 5,762 seats carrying GAP markers, 24,673 GAP markers total, 3,509 distinct GAP terms; largest terms of 3,502, lord 972, by 414; the stored gap census is identical to the recomputed counter; no malformed markers.
6. Purple sweep / screens — reconciled: retained English 0 candidates against the 135-type names allowlist; mixed script NONE, and no non-Latin-script letters at all in the draft; exactly 2 disclosed untraced candidates, neither a failure of any stated claim — `jupmele?'“satne` at 5:116 (a punctuation fusion of two attested words) and `kraevies-åejjie-goelkh` at 73:17 (a hyphenated compound whose two-part form åejjie-goelkh stands in the inventory as a whole).
7. The Sámi fence — CONFIRMED: every seated token traces to the Southern Sámi attestation inventory (GiellaLT lang-sma plus the 2022 dictionary) or the names allowlist, so no Northern Sámi (sme), Lule Sámi (smj), or Skolt Sámi (sms) form is seated; no token carries the distinctive sme/smj diacritics (á, č, đ, ŋ, š, ŧ, ž); the distinctive sme form Ipmil is absent — God is seated Jupmele throughout. The token hearra (seating "priests") stands in GiellaLT lang-sma's own nouns.lexc as a Southern Sámi noun and is recorded in the checker report so a later reader does not mistake it for Northern Sámi hearrá.

## Reservation carried with the landing

**The GAP-tier reservation — stated plainly.** This book is landed under the checker's ruling PASS-WITH-GAP-TIER-RESERVATION. 5,762 of 6,236 seats are GAP-bearing — 92.4% — with 24,673 GAP markers and 3,509 distinct unseated terms, and the unseated set includes the genitive relation itself (of, 3,502 markers) and the core theological vocabulary: lord, angel, prophet, scripture, reward, and revelation carry no attested seat at all and ride GAP markers throughout, as do worship and righteous. This is a complete seat-for-seat first-pass skeleton, not a readable finished translation, and it must not be represented as one. The gaps are held open honestly: every marker is visible inline and the census is printed on the book's face, no gap was filled by invention, and none was filled by borrowing from Northern Sámi, Lule Sámi, Skolt Sámi, or any neighbouring language. Closing the reservation would require attested seats for the core terms from sources not harvested here, which is a build decision for Robert, not a checker repair. The book is DRAFT — NOT PUBLISHED.

## Notes

- No PDF is included: the manuscript Markdown, the built text, and the built JSON are the landed forms, on the pattern of the Komi-Zyrian and Chuvash landings.
