# Landing Report — Võro (vro) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-VRO.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names its
  base and sources (GiellaLT lang-vro and kaikki/Wiktionary as
  attestation inventories; the Võro Institute dictionary and the
  1686 *Wastne Testament* as controls by fact and citation
  only), discloses the GAP census, the plain-style devices, the
  single-stem mercy seating, and the absence of a modern Võro
  Bible.
- `quran-vro.txt` and `quran-vro.json` — the built book exactly
  as passed by the independent checker.
- `glossary.md` — the attested vocabulary of record.
- `BUILD-REPORT.md` and `BUILD-SPEC.md` — the build report and
  the lane build spec of record (the build report stands in
  this folder under the undated name, on the sibling-lane
  pattern; its lane original is BUILD-REPORT-2026-11-28.md).
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — the fresh
  independent checker: PASS-WITH-GAP-TIER-RESERVATION, with the
  minor notes and the §11 GAP-tier ruling carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-VRO-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `LICENCES-RECORDED-2026-11-28.md` — the licence record
  (GiellaLT lang-vro, LGPL v3; kaikki/Wiktionary, CC BY-SA;
  the Võro Institute dictionary and the 1686 *Wastne
  Testament* as controls by fact and citation only).
- `MANIFEST.txt` — SHA-256 of every file above.

All copies in this folder were verified byte-identical to the
lane originals in `~/workspace/ayah-voro/` at landing.

## Gate record

All figures below were re-verified at landing by this desk's
own count from the lane files of record, not taken from the
checker report alone; every figure matched the checker's
exactly.

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set
   equality store == Locked English Master grid TRUE (6,236
   seats in each, no seat in either set that is not in the
   other); per-surah counts match the standard grid at all
   114 surahs, mismatches NONE; `quran-vro.json` holds the
   same 6,236 verses with ZERO mismatches against
   verses-store.json; empty seats NONE; seats containing
   "redacted" NONE.
2. Canonical verify — PASS: 1:1 == «Jumala nimeh, Arm, Arm.»
   character for character; 1:3 == «Arm, Arm.» exactly, both
   mercy names seated on the single attested stem arm, as
   disclosed on the manuscript face; the Basmalah string
   occurs 113 times in the built text `quran-vro.txt` (112
   unnumbered surah openings plus verse 1:1), and surah 9
   carries NONE.
3. Independent checker — PASS-WITH-GAP-TIER-RESERVATION: a
   fresh independent pass that built none of this text
   recomputed every quantitative claim in the build report
   and reproduced each one exactly — counts, seat-set
   equality, the GAP census, the dictionary figure, the
   attestation inventories, and both screens. No failure was
   found, so no failure seat lists arise.
4. Dictionary and the 27 unverified concepts — CONFIRMED by
   this desk's own count: work/dict_core.py holds 531
   entries; work/unverified-dict.json lists exactly 27, every
   one a dictionary key; 531 − 27 = 504 verified entries
   seated. The 27 concepts (camel, close, curse, darkness,
   desert, eighty, follow, forgive, forgiveness, moment,
   mosque, pray, resurrection, rise, safe, servant, seventy,
   sorrow, swear, temple, thank, throne, turn, until, wall,
   week, worship) stand as GAPs where the Master uses them,
   and NONE of their Võro candidate forms is seated anywhere:
   this desk's token scan of all non-GAP text, including the
   regular plural -q variant of each form, found zero seats.
5. GAP census — CONFIRMED figure for figure by this desk's
   own recomputation from verses-store.json: 6,009
   GAP-bearing seats, 29,698 GAP markers, 5,300 distinct GAP
   terms, agreeing with gap-census.json exactly; top terms
   reproduce in the checker's order (except 269, whoever 232,
   made 218, away 218, most 188, sent 172, given 172,
   believers 159, everything 150, until 149, like 148,
   merciful 145). Only 227 seats are fully seated.
6. Purple sweep / screens — reconciled: retained Latin 0
   candidates — this desk's own token screen over every
   non-GAP token found 114 untraced types, every one of them
   on the explicit 133-type allowlist of names, titles, and
   disjointed letters, so 0 candidate types and 0 tokens
   stand outside the allowlist and the Võro inventories;
   mixed script NONE — every alphabetic character in the
   built text is Latin script and Cyrillic characters number
   zero. The attestation fences held: the checker's own
   independently written screen returned ZERO untraced
   tokens, so no Seto form seats without Võro attestation
   (R1) and no 1686-only form is seated (R2).
7. The two build bugs — BOTH TESTED FIXED by the checker and
   confirmed at landing: ü-bearing forms survive intact
   throughout the seated text — this desk counted 44 distinct
   ü-bearing token types and 3,371 occurrences (süä, hüvä,
   ütlemä, üts, kümme, püha, and the rest), exactly the
   checker's figures; and the English word "sin" seats as
   patt in all its seats, never silently carried as the
   disjointed letter "Sin".

## Reservation carried with the landing

**The GAP-tier reservation — stated plainly, in the
checker's own terms (§11 of the checker report).** This book
is landed under PASS-WITH-GAP-TIER-RESERVATION. 6,009 of
6,236 seats (96.36%) carry at least one GAP marker; 29,698
markers in total, an average of 4.94 markers per GAP-bearing
seat and 4.76 per verse overall. Only 227 seats are fully
seated. Core theological vocabulary stands in the GAP mass:
worship 115, forgiveness 70, forgive 52, resurrection 78,
pray (verb) 42, mosque 18, throne 28, temple 1, camel 11. As
with the sibling lanes, a draft at this tier is a
seat-complete, honestly-gapped skeleton: every verse is
present, no word is invented, and the gaps are visible — but
the majority of the text's content words are not yet Võro,
and the draft must not be described, shelved, or read as a
substantially complete Võro translation. It is a verified
first-pass draft whose GAP tier is its defining fact. The
book is DRAFT — NOT PUBLISHED.

## The checker's minor notes

These ride with the landing exactly as the checker recorded
them; none gated the verdict, and none was repaired at
landing — they are recorded for correction at the next edit.

1. The kaikki counting label (§5): the claimed 7,543
   "forms" reproduces EXACTLY as the count of distinct
   normalised (lower-cased, combining marks stripped,
   apostrophe→q) strings in kaikki headwords ∪ forms. Raw
   counts differ by definition: 9,653 form entries in total,
   7,265 distinct raw form strings. The figure is therefore
   sound but its label is loose: 7,543 is the normalised
   distinct inventory contributed by kaikki including
   headwords, not a raw form count. (The companion inventory
   figures are exact as stated: GiellaLT lemmas 20,632,
   corpus word forms 81,133, kaikki 614 lines / 606 distinct
   headwords — all confirmed by this desk's own count where
   applicable.)
2. The BUILD-SPEC "säda" line (§9): BUILD-SPEC lists the
   number 100 as "säda" while the glossary, the dictionary,
   and the built text itself use "sada" — the checker
   recorded 10 seats of sada and 0 seats of säda; this desk
   counted 10 occurrences of the token sada across 7 seats
   and zero occurrences of säda anywhere. Both are inventory
   forms; the spec line should be corrected to match the
   seated text at the next edit.
3. The §8 "Seen" observation, not a failure: the Master's
   spelling "Seen" at 36:1 is GAP-held (⟦GAP: seen⟧) because
   the allowlist carries "Sin", not "Seen" — a held-open
   gap, honestly marked, where a carried letter-name might
   have been expected.

## Notes

- No PDF is included: the manuscript Markdown, the built
  text, and the built JSON are the landed forms, on the
  pattern of the Komi-Zyrian, Chuvash, and Southern Sámi
  landings.
- Novelty wording stands only in the brief's bounded form:
  the first complete Võro Qur'an translation found — after
  research (27 November 2026), with "not found is not proven
  non-existent" carried in the same passage. No "first ever"
  claim is made anywhere in the landed files.
