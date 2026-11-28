# Võro (vro) Quran draft — Independent Checker Report (2026-11-28)

Checker: fresh independent pass; checker built none of this text.
Scope: verify build claims with own scripts, recomputing every figure.
No text edited, nothing landed, shelved, committed, or pushed by this check.

Status: COMPLETE — verdict at §12 (end of file): PASS-WITH-GAP-TIER-RESERVATION.

## 1. Seat grid and counts — VERIFIED

Recomputed from verses-store.json against master-verses.json and the
standard 114-surah grid, with the checker's own script:

- Store seats: 6,236. Master seats: 6,236. Seat-set equality: TRUE
  (no seat in either set that is not in the other).
- Per-surah counts match the standard grid for all 114 surahs:
  mismatches NONE.
- Empty seats: NONE. Seats containing "redacted": NONE.
- quran-vro.json holds the same 6,236 verses with ZERO mismatches
  against verses-store.json; quran-vro.txt carries the same text.

## 2. Basmalah — VERIFIED

- 1:1 == «Jumala nimeh, Arm, Arm.» — exact, character for character.
- 1:3 == «Arm, Arm.» — exact.
- Both mercy names seat on the single attested stem arm, exactly as
  disclosed on the manuscript face, in the glossary, and in
  BUILD-SPEC. No second mercy stem is seated anywhere in 1:1 or 1:3.
- Basmalah string count in the built text (quran-vro.txt): 113 —
  112 unnumbered surah openings plus verse 1:1. Surah 9 carries
  NONE (verified by parsing all 114 surah sections). The manuscript
  file counts 114 occurrences only because its front-matter prose
  quotes the Basmalah once; the built text itself is 113.

## 3. GAP census — VERIFIED, figure for figure

Recomputed independently from verses-store.json:

- GAP-bearing seats: 6,009 — matches gap-census.json exactly.
- GAP markers total: 29,698 — matches exactly.
- Distinct GAP terms: 5,300 — matches exactly.
- Top terms reproduce in the same order and counts (except 269,
  whoever 232, made 218, away 218, most 188, sent 172, given 172,
  believers 159, everything 150, until 149, like 148, merciful 145).

## 4. Dictionary and the 27 unverified concepts — VERIFIED

- work/dict_core.py DICT holds 531 entries; work/unverified-dict.json
  lists exactly 27, every one of them a DICT key; 531 − 27 = 504
  verified entries seated. The claimed 504 reproduces exactly.
- The 27: camel, close, curse, darkness, desert, eighty, follow,
  forgive, forgiveness, moment, mosque, pray, resurrection, rise,
  safe, servant, seventy, sorrow, swear, temple, thank, throne,
  turn, until, wall, week, worship.
- NONE of their Võro candidate forms is seated anywhere: the
  checker's token scan of all non-GAP text (including the regular
  plural -q variant of each form, e.g. kaamelq) found zero seats
  for kaamel, mošee, palvetama, andistama, andistamine,
  ülesnousmine, kummardama, tempel, troon, sulane, kõrb, sein,
  nädal, hetk, and the rest.
- Each concept instead stands as a GAP where the Master uses it
  (counts of the exact GAP term: worship 115, turn 108, follow 106,
  until 149, resurrection 78, forgiveness 70, forgive 52, pray 42,
  throne 28, servant 28 — with further seats under plural/variant
  GAP terms such as servants 100). Two concepts, moment and week,
  occur nowhere in the Master at all (0 seats), so their GAP status
  is vacuous but not contradicted. The disclosed distinction also
  holds in the text: the noun palvõ (prayer) is seated while the
  verb pray is GAP-held throughout.

## 5. Attestation inventories — VERIFIED (one counting note)

- GiellaLT lang-vro lemmas (sources/giella-lemmas.json): 20,632 —
  exact, all distinct.
- Corpus word forms (sources/wordfreq-forms.json): 81,133 — exact,
  all distinct.
- kaikki/Wiktionary (sources/kaikki-vro.jsonl): 614 lines, 606
  distinct headwords — exact. The claimed 7,543 "forms" reproduces
  EXACTLY as the count of distinct normalised (builder's norm:
  lower-cased, combining marks stripped, apostrophe→q) strings in
  headwords ∪ forms. Raw counts differ by definition: 9,653 form
  entries in total, 7,265 distinct raw form strings. The figure is
  therefore sound but its label is loose: 7,543 is the normalised
  distinct inventory contributed by kaikki including headwords, not
  a raw form count. Recorded as a counting-definition note, not a
  failure.

## 6. Attestation fences (R1/R2) — VERIFIED as mechanically enforced

- The checker's own independently written token screen (inventories:
  GiellaLT lemmas + wordfreq forms + kaikki headwords/forms, under
  the same normalisation, plus the disclosed plural -q derivation
  and the three disclosed additions jumal/jumala/nimeh) over every
  non-GAP token in all 6,236 seats: ZERO untraced tokens. Every
  seated form traces to a held Võro inventory. The Estonian-gloss
  bridge (sources/est2vro-giella.json) is NOT part of the seating
  inventory in either the builder's or the checker's screen, so no
  Standard Estonian form can seat without independent Võro
  attestation — the fence is enforced by construction, and the
  zero result confirms it held.
- Seto fence (R1): no Seto inventory is held in the lane and no
  seating path exists outside the Võro inventories above; the zero
  untraced result is the mechanical evidence available. Limitation
  stated plainly: the checker holds no independent Seto wordlist,
  so a form attested in BOTH Seto and the Võro inventories would
  seat on its Võro attestation — which is what R1 requires.
- 1686 fence (R2): no Wastne Testament text or wordlist is held in
  the lane, and no seating path draws on it; every seated form
  traces to a modern Võro inventory (§6, first bullet). A form
  attested in both 1686 and the modern inventories seats on its
  modern attestation, which is what R2 permits. No evidence of any
  1686-only form seated was found.

## 7. Screens — VERIFIED

- Retained Latin: the checker's screen found 0 candidate types /
  0 tokens outside the explicit allowlist (133 names/titles/
  disjointed letters) and the Võro inventories — matching the
  build's 0 / 0.
- Mixed script: NONE. Every alphabetic character in the built text
  is Latin script (652,153 letters counted); zero Cyrillic tokens.
- "redacted": NONE (§1).

## 8. The two build bugs — BOTH TESTED FIXED

(a) Diaeresis-stripping normalisation: ü-bearing forms survive
intact throughout the seated text — 44 distinct ü-bearing token
types, 3,371 occurrences (süä, hüvä, ütlemä, üts, kümme, püha,
löüdmä, sükäv, and the rest), and the attestation screen in §6,
run WITHOUT stripping ü, still returns zero untraced tokens, so
no stripped-u ghost forms are seated either.

(b) Allowlist "Sin" capturing English "sin": tested directly.
The Master carries the English word "sin" in 31 seats and "sins"
in 49 seats; in the built text ALL 31 seat patt and ALL 49 seat
patt (plural pattq where plural), e.g. 2:173 "…tä ⟦GAP: commits⟧
ei patt." Zero seats carry a standalone "Sin" token, and zero
carry ⟦GAP: sin⟧. The English word is seated on the attested Võro
word for sin, never silently carried as the disjointed letter.
One adjacent observation, not a failure: the Master's spelling
"Seen" at 36:1 is GAP-held (⟦GAP: seen⟧) because the allowlist
carries "Sin", not "Seen" — a held-open gap, honestly marked,
where a carried letter-name might have been expected.

## 9. Honest labelling and novelty wording — VERIFIED

- The manuscript face carries DRAFT — NOT PUBLISHED at its head,
  names its base and sources, discloses the GAP census, the
  plain-style devices, the single-stem mercy seating, and the
  absence of a modern Võro Bible.
- No "first ever" claim appears anywhere; the only occurrences of
  the phrase are negations ("No 'first ever' claim is made").
- The novelty wording stands only in the brief's bounded form:
  "the first complete Võro Qur'an translation found — after
  research (27 November 2026)", with "not found is not proven
  non-existent" carried in the same passage.
- Minor documentation inconsistency, not a text failure:
  BUILD-SPEC lists the number 100 as "säda" while the glossary,
  the dictionary, and the built text itself use "sada" (10 seats,
  0 seats of säda). Both are inventory forms; the spec line should
  be corrected to match the seated text at the next edit.
- Note: quran-vro.txt and quran-vro.json are bare built-text files
  with no header; the DRAFT labelling lives on the manuscript face
  and the build report, which are the draft's presented form.

## 10. Not landed — VERIFIED

No vro/voro folder stands on the shelf under
~/workspace/robert-tilford-quran/translations/ (232 folders counted
this check, none Võro). The draft stands in ~/workspace/ayah-voro/
only, as the build report states.

## 11. Ruling on the GAP tier — RESERVATION (explicit)

6,009 of 6,236 seats (96.36%) carry at least one GAP marker;
29,698 markers in total, an average of 4.94 markers per GAP-bearing
seat and 4.76 per verse overall. Only 227 seats are fully seated.
Core theological vocabulary stands in the GAP mass: worship 115,
forgiveness 70, forgive 52, resurrection 78, pray (verb) 42,
mosque 18, throne 28, temple 1, camel 11. As with the sibling
lanes, a draft at this tier is a seat-complete, honestly-gapped
skeleton: every verse is present, no word is invented, and the
gaps are visible — but the majority of the text's content words
are not yet Võro, and the draft must not be described, shelved, or
read as a substantially complete Võro translation. It is a
verified first-pass draft whose GAP tier is its defining fact.
That reservation rides with the verdict below, in the same breath.

## VERDICT: PASS-WITH-GAP-TIER-RESERVATION

Every machine-checkable build claim was recomputed by the checker
and verified: 6,236/6,236 seats with seat-set equality true,
per-surah mismatches none, empty seats none, "redacted" none;
Basmalah 113 lines with surah 9 carrying none, 1:1 and 1:3 exact
on the single disclosed arm stem; GAP census 6,009 / 29,698 /
5,300 exact; dictionary 504 seated with the 27 unverified concepts
held as GAPs and none of their forms seated anywhere; attestation
inventories 20,632 / 81,133 / 606 exact and 7,543 reconciled under
its counting definition (§5); retained-Latin candidates 0 against
the allowlist, mixed-script none; both build bugs tested fixed
(ü-forms intact; English "sin" seated as patt in all 80 seats,
never as the letter "Sin"); R1/R2 fences mechanically enforced
with zero untraced tokens; labelling DRAFT — NOT PUBLISHED with
novelty wording only in the bounded brief form; nothing landed.
No failure was found, so no failure seat lists arise. The two
minor notes (§5 counting label, §9 säda/sada spec line, plus the
§8 "Seen" observation) are recorded for correction at the next
edit and do not disturb the verdict. The GAP-tier reservation in
§11 is part of this verdict: PASS on every claim as made, with
the draft's 96.36% GAP-bearing tier stated as its defining limit.
This check edited no text and landed, shelved, committed, and
pushed nothing; landing remains for Robert's word.
