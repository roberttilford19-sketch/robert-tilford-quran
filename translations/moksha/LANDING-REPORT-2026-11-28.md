# Landing Report — Moksha (mdf) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-MDF.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Moksha, Cyrillic with
  spelling rules identical to those of Russian, the same
  33-letter alphabet and no additional letters, Central dialect
  group in its ä-retaining form; GiellaLT giella-mdf, LGPL v3,
  and the Moksha lexicon of English Wiktionary, CC BY-SA, as
  attestation sources; the 2016 complete Moksha New Testament
  and the modern dictionaries as controls by fact and citation
  only), discloses the Basmalah's single mercy stem, the GAP
  policy, the flagged seats, and states that no claim is made
  that this is the first Moksha Quran translation.
- `quran-mdf.txt` and `quran-mdf.json` — the built book exactly
  as passed by the re-check. Recount at landing, from the lane
  files of record: all 6,236 store verse texts stand verbatim in
  the companion manuscript (0 missing).
- `glossary.md` — the attested vocabulary of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — first independent
  checker: FAIL, findings §§8.1–8.9.
- `REMEDIATION-RECORD-2026-11-28.md` — every repair, seat by seat.
- `CHECKER-REPORT-RECHECK-2026-11-28.md` — fresh independent
  re-check of the remediated text: PASS, with the reservations
  carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-MDF-2026-11-27.md` — census,
  flagged constructions, and disclosures.
- `ATTESTATION-AUDIT-2026-11-27.md` — seat-by-seat attestation
  audit.
- `LICENCES-RECORDED-2026-11-27.md` and `BUILD-SPEC.md` — the
  licence record and the lane build spec of record.
- `MANIFEST.txt` — SHA-256 of every file above.

## Gate record

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set exactly
   equal to the Locked English Master (no missing, no extra);
   per-surah grid clean at all 114 surahs; `quran-mdf.json`
   flattened equals the verse store seat for seat (6,236/6,236,
   texts identical); `quran-mdf.txt` matches the store at every
   seat (0 mismatches); no empty seats; no seat shorter than
   three characters; the string "redacted" appears in no seat.
   First verse 1:1 «Шкаень лемса, Милостивай, Милостивай.»;
   last verse 114:6 «⟦GAP: jinn⟧ ёткста и ломантнень ёткста.”»
2. Canonical verify — PASS: 1:1 equals the fixed Basmalah form
   exactly, and is the only store seat equal to it; in
   `quran-mdf.txt`, exactly 112 standalone Basmalah lines and
   114 occurrences of the fixed form in all (112 standalone +
   1:1 numbered + 27:30 inline in Solomon's letter).
3. Independent checker — FAIL (findings §§8.1–8.9: the што /
   штоба and эли purpose-and-disjunction families, the garbled
   4:23 clause, 13 mixed-script token shapes in 21 occurrences,
   7:166 missing its GAP marker, the U+04A3 (ң) codepoint at
   47:25, the 29:14 thousand-minus-fifty number error, the
   иля / иляда negation family, and the мельга postposition
   family), then remediation of every verified finding, then a
   fresh independent re-check: PASS — every §8 count verified at
   zero by the re-checker's own recount, and every reseat count
   reconciled to the token (али +127, аф +117, сянь инкса +275,
   синь +265, мельге +48).
4. Purple sweep — reconciled: 9,901 distinct Cyrillic tokens
   and 4,940 untraced candidates, candidates only under house
   law; the largest candidate, кда (865 whole tokens), is
   corroborated directly in the lane's own held source, the
   2016 Moksha New Testament frequency list
   (`bibleFreq2016.txt`: кда 332 + Кда 239 = 571 occurrences),
   and no new high-frequency untraced token survives inspection
   as a candidate invention.
5. GAP census (post-remediation, recomputed by the re-checker):
   58 GAP seats, 68 markers — jinn 31, pilgrimage 16, usury 8,
   Sabbath 7, apes 3, gnat 1, cucumber 1, fig 1; markers
   well-formed, ⟦/⟧ balanced 68/68. (The manuscript file counts
   one further ⟦GAP: …⟧, the explanatory example in its front
   matter.) 6,178 verses are rendered in full.
6. Erzya bar — PASS: zero whole-token seats of every barred
   Erzya form (паз, чи, кедь, теште, кинига, казне, пежеть,
   шайтян, пророк, баславамс, седеймариця all 0), and no
   шайтян, шайтан, пророк, or пежеть substring anywhere.
7. Script purity — PASS: mixed-script tokens 0; U+04A3 (ң) 0
   book-wide; no Cyrillic letter outside the 33-letter Russian
   norm anywhere in the book; guillemets balanced « 232 / » 232.

## Reservations carried with the landing

These ride with the landing, as the re-check states them; none
blocks the PASS, and none is hidden.

1. **The prophet/messenger collapse (§9.3 of the original
   check).** The Шкаень кучф device ("God's sent one") serves
   uniformly for both prophet and messenger; the collapse is
   disclosed, not an inconsistency, and stands as a recorded
   reservation.
2. **The 4:56 кедь "skins" seat.** The seat stands as кедьсна /
   кедьса, "skins" — a genuine Moksha word coinciding in form
   with the barred Erzya word for "hand"; the barred sense is
   nowhere seated. (The only other кедь substrings in the book,
   at 23:40 and 25:40, are inside пяшкедьф(т) "filled".)
3. **Latin manna.** The word manna stands in Latin at 2:57,
   7:160, and 20:80, under the names-policy Latin retained in
   the book.
4. **Bedouin-тнень at 33:20 (§9.5).** The Bedouin seat stands
   in its recorded Latin-derived form with the Moksha definite
   plural ending, as the original check recorded it.
5. **Master-inherited curly-quote imbalance (§9.7a).** The
   “ ” curly-quote imbalance in the book is inherited from the
   Locked English Master itself; the guillemets, the book's own
   quotation marks, are balanced 232/232.

## Notes

- No PDF is included: the manuscript Markdown, the built text,
  and the built JSON are the landed forms, on the pattern of
  the Erzya and Udmurt landings.
