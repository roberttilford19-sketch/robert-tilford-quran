# Chuvash (chv) Quran draft — INDEPENDENT CHECKER REPORT
Date: 2026-11-28 · Checker: fresh independent pass (built none of this text) · Status of draft under check: DRAFT — NOT PUBLISHED

Verdict: **PASS** — every quantitative claim recomputed independently reproduces exactly; three non-gating wording notes are recorded in §§7–8. Full reasoning below.

Method: every figure recomputed by the checker's own scripts from the primary files (verses-store.json, master-verses.json, quran-chv.json, quran-chv.txt, work/eng2chv.json, work/gap-census.json, work/names-allowlist.json, work/unverified-dict.json, sources/kaikki-chv.jsonl, sources/apertium-chv.lexc, sources/attestation-inventory.json). The build's verify.py was read for reference only; no build number is trusted.

Files under check: BUILD-REPORT.md, BUILD-SPEC.md, verses-store.json, master-verses.json, quran-chv.json, quran-chv.txt, ayah-companion-manuscript-CHV.md, glossary.md, FLAGS-AND-GAPS-DISCLOSURE-CHV-2026-11-28.md, LICENCES-RECORDED-2026-11-28.md, verify.py, work/build.py, work/gap-census.json, work/unverified-dict.json, work/names-allowlist.json.

---
## 1. Verse counts, seat-set equality, grid — PASS (exact)

Recomputed from verses-store.json, master-verses.json, and quran-chv.json against the standard 114-surah grid (sum 6,236):

- verses-store.json: **6,236 seats**. master-verses.json: **6,236 seats**. quran-chv.json: **6,236 seats**.
- Seat-set equality store == master: **TRUE**. Store == quran-chv.json on keys **and** on every value: identical, 0 differing seats.
- Per-surah grid mismatches (store and master, independently): **NONE**. Verse numbering within every surah is contiguous 1..N with no missing or extra seat.
- Empty seats: **NONE**. Non-string seats: none. Seats containing "redacted" (any case): **NONE** — and the string "redacted" occurs 0 times in verses-store.json, quran-chv.txt, the manuscript, and master-verses.json.
- Master provenance: the Locked English Master at ~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md has MD5 **ecc5b8e2848e5044186b7ad82bed9f4e**, exactly as claimed. Re-deriving the master verse set from that file with the checker's own extraction gives 6,236 seats, identical to master-verses.json (0 value differences).
- Derived files are faithful: quran-chv.txt carries 6,236 seat-prefixed lines and every store verse text appears in it; the manuscript carries 6,236 seat-prefixed lines and every store verse text appears in it. No verse is missing from either rendering.

## 2. Basmalah spec — PASS (exact)

- 1:1 == «Турӑ ятпа, Аван, Аванлӑх.» — **TRUE**, character for character.
- 1:3 == «Аван, Аванлӑх.» (spec form, the two names without the frame) — **TRUE**.
- quran-chv.txt: **112 lines** consisting solely of the Basmalah (the unnumbered opening lines). Per-surah parse of the .txt: every surah except 9 contains the Basmalah exactly once; surah 9 contains it 0 times; surah 1 contains it once, as verse 1:1 (seat-prefixed), with no unnumbered duplicate. Total lines containing the Basmalah in the .txt: 113 (112 unnumbered + 1:1).
- Manuscript: 112 lines consisting solely of the Basmalah, plus 1:1 as a seat line, plus one front-matter quotation of the seated form — 114 containing lines, fully accounted for.
- Mercy seating: 1:1 and 1:3 seat Beneficent as Аван and Merciful as Аванлӑх, and the substitution (аван "good" / аванлӑх "kindness", kaikki-attested, because no attested mercy noun was found in the harvested inventories) is disclosed in BUILD-SPEC.md, in glossary.md, in FLAGS-AND-GAPS-DISCLOSURE-CHV-2026-11-28.md, and on the manuscript's own face. **Disclosed as claimed.**

## 3. Dictionary and attestation inventory — PASS (exact)

Recomputed with NFC normalisation and lower-casing, replicating the harvesting rules independently:

- kaikki-chv.jsonl: 1,249 entries; **1,003 distinct headwords**; **2,047 distinct declined forms**. Both figures exactly as claimed.
- Apertium apertium-chv lexc harvest: **75,337 stem/form tokens**, exactly as claimed. (Line-initial stems alone give 56,367; the claimed figure is the full-text harvest the build used, and it reproduces exactly.)
- Union inventory: **77,249 forms**, exactly as claimed. The saved sources/attestation-inventory.json is identical, as a set and in sorted order, to the checker's recomputed union — no drift between the recorded inventory and the sources.
- Seat dictionary (work/eng2chv.json): **2,223 English seat keys**, exactly as claimed. Re-simulating the gloss-inversion stage alone reproduces **2,088 keys**, exactly as claimed; the remaining 135 keys are curated-core / suffix-device additions (45 further curated entries overwrite kaikki-derived values for keys already present). 2,088 + 135 = 2,223. ✓
- Dropped-seat log verified: work/unverified-dict.json records from/than → ран and under/below → айӗн as dropped. Neither ран nor айӗн is in the attestation inventory (confirmed), neither appears anywhere in the seated text (confirmed, 0 seats), from/than seat instead as рен (the disclosed -рен suffix device), and under/below surface honestly as GAP markers (under ×16, below ×1). The disclosure in FLAGS matches the data.

## 4. GAP census — PASS (exact)

Recomputed from verses-store.json with the checker's own marker extraction:

- Seats carrying at least one GAP marker: **5,842 of 6,236**. Total markers: **23,456**. Distinct GAP terms: **4,384**. All three figures exactly as claimed.
- Top terms reproduce exactly: down 214, away 211, punishment 207, sent 172, out 164, at 149, revelations 135, reward 120, knowledge 111, while 107, follow 106, deeds 104, up 102, hereafter 101, servants 100, guided 99, wise 99, whomever 98, call 95, women 95.
- work/gap-census.json agrees with the recomputation in full: its gap_seats list equals the recomputed seat list (5,842) and its gap_counter equals the recomputed counter on every one of the 4,384 terms (0 mismatches). All GAP terms are plain lower-case English (letters, spaces, hyphens, apostrophes only) — no smuggled seated text inside markers.

## 5. Screens — PASS (exact, with two footnotes)

- Cyrillic token attestation: **651 distinct Cyrillic tokens** in the seated text (GAP interiors excluded), **0 untraced** under the build's stated tracing rules (attestation inventory, dictionary seats, -сем plural stripping). Exactly as claimed. The build's own work/verify-candidates.json (unknown 0, latin 0, mixed 0, gaps 5,842) agrees with this independent recomputation.
  - Footnote A: the 0 depends on exactly one form that is not itself in the inventory — **ятпа** (1 occurrence, in 1:1), the regular instrumental of ят "name" (ят is a kaikki headword and is in the inventory). verify.py hard-codes ятпа plus seven other allowances (турӑ, шуйттан, аван, аванлӑх, ра, рен, ӑн); the checker confirms only ятпа actually needs the allowance — the other seven trace through the inventory or dictionary on their own. The derivation is disclosed in BUILD-SPEC.md ("ятпа is the regular instrumental of ят"). This is a disclosed device, not a hidden borrowing, but a reader of the headline figure should know the screen's allowance list is what carries it.
  - Footnote B: 85 of the 651 tokens trace only through the inventory (mostly -сем plurals whose stems are attested), and 2 tokens (пурнӑҫа, тӑру) trace only through dictionary phrase seats (пурнӑҫа кӗрт; лару-тӑру), both kaikki-derived. No token traces to nothing.
- Retained Latin: **134 types / 1,064 tokens**, all on the allowlist; **0 non-allowlist types, 0 non-allowlist tokens**. Exactly as claimed.
  - Footnote: work/names-allowlist.json holds 135 types. Two of them, Zul and Qarnain, never occur as separate tokens, because the text seats the hyphenated form **Zul-Qarnain** (3 tokens, at 18:83, 18:86, 18:94), which verify.py adds to the allow set. The claimed "134 types against the 135-type allowlist" is accurate with that mechanism understood.
- Mixed-script: **NONE**. No whitespace token mixes Latin and Cyrillic. Confirmed independently.
- Character set: outside GAP markers the text uses only the Chuvash Cyrillic alphabet (including Ӑӑ, Ӗӗ, Ҫҫ, Ӳӳ), Latin capitals/lowercase for allowlisted names, and ordinary punctuation. No letter outside those sets occurs.

## 6. Oghuric bar — PASS (on the evidence available to a mechanical check)

The claim is a negative — no Tatar, Turkish, or other Common Turkic form seated as Chuvash — and a mechanical checker can test it only by traceability, which is the test the house law prescribes:

- Every one of the 651 distinct Cyrillic tokens in the seated text traces to the Chuvash attestation inventories (kaikki Chuvash entries or Apertium apertium-chv) or to a kaikki-derived dictionary seat, with the single disclosed exception of ятпа above (a regular Chuvash instrumental derivation from an attested Chuvash headword, not a foreign form).
- No Tatar-specific Cyrillic letters (ә, ө, җ, ң, һ) occur anywhere in the text.
- The build's seat sources are kaikki + Apertium-chv only; the licences record confirms the Turku corpus, the Hugging Face datasets, and the Skvortsov/Ashmarin dictionaries were not used for seats, and no Tatar or Turkish source file exists in the lane's sources/ folder.
- On that evidence, no Common Turkic form is seated. A full philological diff against a Tatar dictionary is beyond a mechanical check and is not claimed here; the traceability evidence is complete and clean.

## 7. "First" wording, Saifutdinov acknowledgement, labelling

- **No priority claim exists anywhere in the build — PASS on substance.** A targeted search for "first translation / first complete / first Quran / first rendering" phrasing across all lane documents and the .txt returns nothing. The manuscript's face states the opposite: a partial Chuvash rendering by Ruslan Saifutdinov already exists, "this draft is a second, independent rendering", and "No claim of being first is made anywhere in this draft."
- **Caveat (wording, not substance):** the absolute sentences in BUILD-REPORT.md ("NO 'first' wording appears anywhere in this build"; "no 'first' wording anywhere") are literally overstated. The word "first" does occur in non-claim uses: the build-tier descriptor "first-pass" (manuscript title and front matter, BUILD-REPORT, BUILD-SPEC, FLAGS), "the first task list for any later repair pass" (FLAGS), and the dictionary seat "first — пӗрремӗш" (glossary.md, a translation seat for the Master's word "first", which itself seats as пӗрремӗш in the text — quran-chv.txt contains no Latin "first" at all). None of these asserts priority over Saifutdinov or anyone else. Remediation, if Robert wants the absolute wording to stand literally, is a one-line softening in BUILD-REPORT (e.g. "no first-ever claim"); it does not gate the draft.
- **Saifutdinov acknowledgement — PASS.** The tafsir (2006 commission of the Spiritual Administration of Muslims of the Chuvash Republic; juzʾ 30 volume, Cheboksary: Novoe Vremya, 2020) is acknowledged on the manuscript's own face, in BUILD-REPORT.md, in BUILD-SPEC.md, in LICENCES-RECORDED-2026-11-28.md, and in glossary.md (Турӑ note). The licences record correctly treats it as in copyright, fact/citation only, wording never reproduced — consistent with the token-traceability result in §5, since no token is untraced to a Chuvash inventory.
- **DRAFT — NOT PUBLISHED labelling — PASS on the reader-facing face, with a note.** The exact label stands on the manuscript's face (line 3, directly under the title) and twice in BUILD-REPORT.md. The exact string does not appear in BUILD-SPEC.md, FLAGS-AND-GAPS-DISCLOSURE-CHV-2026-11-28.md, LICENCES-RECORDED-2026-11-28.md, or glossary.md (those files state the stop-before-landing position in other words), and the raw data files quran-chv.txt and quran-chv.json carry no front matter or label at all. The book a reader meets is labelled; the claim "labelling throughout" holds for the manuscript and build report, not literally for every file in the lane.
- **Not landed — confirmed.** No chv/chuvash folder exists on the GitHub shelf tree at ~/workspace/robert-tilford-quran/translations/ (229 folders listed, none matching). Nothing in this check landed, shelved, committed, or pushed anything; the checker edited no text under check.

## 8. Minor discrepancy noted (does not affect any headline claim)

BUILD-SPEC.md states: "The two Master seats carrying a literal '<redacted>' placeholder are rendered for their surrounding sense." In fact **no seat** in the Locked English Master (the whole source manuscript, not only Part I) and none in master-verses.json contains the string "redacted" — the count is 0 everywhere. build.py's replace of "<redacted>" is therefore a no-op on this lane; the sentence reads as sibling-lane boilerplate carried into this spec. The substantive claim it supports — no 'redacted' seats in the draft — is true (§1). Remediation, if wanted, is deleting or correcting that one spec sentence; it does not gate the draft.

## VERDICT: PASS

Every quantitative claim in the build report was recomputed independently and reproduces **exactly**: 6,236/6,236 verses with seat-set equality true, per-surah grid mismatches none, empty seats none, 'redacted' seats none; dictionary 2,223 seat keys (2,088 kaikki gloss-inverted + 135 curated/device additions), kaikki 1,003 headwords / 2,047 forms, Apertium apertium-chv 75,337 tokens, union inventory 77,249 forms (saved inventory identical to recomputation); Basmalah spec met in full (1:1 is the Basmalah verse, 112 unnumbered lines, 1:3 in spec form, аван / аванлӑх mercy seating disclosed on the book's face); GAP census 5,842 seats / 23,456 markers / 4,384 distinct terms, agreeing with work/gap-census.json term for term; screens 651 distinct Cyrillic tokens with 0 untraced, retained Latin 134 types / 1,064 tokens with 0 non-allowlist against the 135-type allowlist, mixed-script none; Oghuric bar upheld on complete token traceability; no first-ever claim anywhere, with the Saifutdinov tafsir acknowledged on the book's face; DRAFT — NOT PUBLISHED on the manuscript's face; Master MD5 ecc5b8e2848e5044186b7ad82bed9f4e verified; nothing landed or shelved.

No seat list is attached for any failure, because there is no failure to list: the failure sets (grid mismatches, empty seats, redacted seats, untraced tokens, non-allowlist Latin types, mixed-script tokens, counter mismatches) are all empty, and each was computed, not assumed.

Three non-gating wording items are recorded for the record, with their remediations named in place: (1) BUILD-REPORT's absolute "no 'first' wording anywhere" is literally overstated given the "first-pass" tier descriptor and one ordinal use — soften the sentence if the absolute form is to stand (§7); (2) BUILD-SPEC's '<redacted>' sentence describes a condition that does not occur in this lane's Master — delete or correct it (§8); (3) the attestation screen's 0-untraced figure rests on the disclosed ятпа allowance in verify.py — already disclosed in BUILD-SPEC, noted here so the headline figure is never quoted without it (§5, Footnote A). None of these requires re-seating any verse, and none blocks the draft from proceeding to whatever step Robert rules next. This checker makes no landing recommendation and has taken no landing action.
