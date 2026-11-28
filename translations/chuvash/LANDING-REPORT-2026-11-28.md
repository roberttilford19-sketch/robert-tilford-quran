# Landing Report — Chuvash (chv) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-CHV.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Chuvash, ISO 639-3
  chv, in the modern Cyrillic standard — the Russian alphabet
  plus Ӑӑ, Ӗӗ, Ҫҫ, Ӳӳ), acknowledges the partial Chuvash Qur'an
  tafsir by Ruslan Saifutdinov (2006 commission of the Spiritual
  Administration of Muslims of the Chuvash Republic; juzʾ 30
  volume, Cheboksary: Novoe Vremya, 2020) and states that this
  draft is a second, independent rendering with no claim of
  being first made anywhere in it, discloses the GAP census on
  its face, and discloses the Basmalah mercy seating (аван
  "good" / аванлӑх "kindness", kaikki-attested, because no
  attested mercy noun was found in the harvested inventories).
- `quran-chv.txt` and `quran-chv.json` — the built book exactly
  as passed by the independent checker. Recount at landing, by
  this landing desk's own count from the lane files of record:
  6,236 seats in the verse store, the master set, and the built
  JSON, identical at every seat.
- `glossary.md` — the attested vocabulary of record.
- `BUILD-REPORT.md` and `BUILD-SPEC.md` — the build report and
  the lane build spec of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — the fresh
  independent checker: PASS, with the GAP-tier reservation and
  the three non-gating wording notes carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-CHV-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `LICENCES-RECORDED-2026-11-28.md` — the licence record
  (kaikki Chuvash, CC BY-SA, and Apertium apertium-chv as
  attestation sources; the complete Chuvash Bible, IBT 2009,
  and the Saifutdinov tafsir as fact and citation only, their
  licences unverified and recorded as such).
- `MANIFEST.txt` — SHA-256 of every file above.

All copies in this folder were verified byte-identical to the
lane originals in `~/workspace/ayah-chuvash/` at landing.

## Gate record

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set
   exactly equal to the Locked English Master (no missing, no
   extra); per-surah grid exact at all 114 surahs (grid sum
   6,236); `quran-chv.json` is identical to the verse store at
   every seat (0 differing seats); no empty seats; the string
   "redacted" appears in no seat. Master provenance: the Locked
   English Master MD5 ecc5b8e2848e5044186b7ad82bed9f4e, as
   verified by the checker. First verse 1:1 «Турӑ ятпа, Аван,
   Аванлӑх.»; last verse 114:6 «рен хушшинчи ⟦GAP: jinn⟧ тата
   хушшинчи халӑх.”»
2. Canonical verify — PASS: 1:1 equals the BUILD-SPEC fixed
   Basmalah form «Турӑ ятпа, Аван, Аванлӑх.» character for
   character; `quran-chv.txt` carries exactly 112 unnumbered
   Basmalah lines (every surah except 1 and 9; surah 9 carries
   none, and surah 1 carries it once, as the numbered verse
   1:1); seat 1:3 reads «Аван, Аванлӑх.» — the spec form, the
   two names without the frame, verified character for
   character.
3. Independent checker — PASS: a fresh independent pass that
   built none of this text recomputed every quantitative claim
   in the build report and reproduced each one exactly —
   counts, seat-set equality, dictionary and inventory figures
   (seat dictionary 2,223 English keys: 2,088 kaikki
   gloss-inverted + 135 curated/device additions; kaikki 1,003
   distinct headwords / 2,047 distinct declined forms; Apertium
   apertium-chv 75,337 stem/form tokens; union inventory 77,249
   forms, the saved inventory identical to the recomputation),
   the GAP census, and both screens. No seat list is attached
   for any failure, because there is no failure to list.
4. Purple sweep — reconciled, candidates only under house law:
   the checker's own recomputation of the attestation screen
   returns 651 distinct Cyrillic tokens with 0 untraced, in
   agreement with the build's verify-candidates record
   (unknown 0, latin 0, mixed 0, gaps 5,842); the retained-Latin
   screen returns 134 types / 1,064 tokens, all on the
   allowlist, with 0 non-allowlist types and 0 non-allowlist
   tokens against the 135-type allowlist in
   work/names-allowlist.json (two allowlist types, Zul and
   Qarnain, never occur as separate tokens because the text
   seats the hyphenated form Zul-Qarnain, 3 tokens); mixed-
   script tokens: none.
5. GAP census — recomputed by the checker and verified at
   landing by this desk's own count: 5,842 GAP seats, 23,456
   GAP markers, 4,384 distinct GAP terms, agreeing with
   work/gap-census.json term for term. Largest terms: down
   214, away 211, punishment 207, sent 172, out 164.
6. Oghuric bar — PASS on the evidence available to a mechanical
   check: every one of the 651 distinct Cyrillic tokens traces
   to the Chuvash attestation inventories (kaikki Chuvash
   entries or Apertium apertium-chv) or to a kaikki-derived
   dictionary seat, with the single disclosed exception of
   ятпа (see the wording notes below); no Tatar-specific
   Cyrillic letters occur anywhere in the text; no Tatar or
   Turkish source file exists in the lane's sources.

## Reservation carried with the landing

**The GAP-tier reservation — stated plainly.** This book is
landed under PASS-WITH-GAP-TIER-RESERVATION. 5,842 of the
6,236 seats are GAP-bearing (only 394 verses carry no GAP
marker). It is a first-pass engine build over a ~1,003-headword
kaikki inventory: every Master content word with no verified
Chuvash seat carries the visible marker ⟦GAP: <english term>⟧
rather than an invented or borrowed form, and the census is
disclosed on the book's own face. A future GAP-reduction pass —
enlarging the seated dictionary — remains open as ordinary
revision work. The book is DRAFT — NOT PUBLISHED.

## The checker's three non-gating wording notes

These ride with the landing exactly as the checker recorded
them; none requires re-seating any verse, and none gated the
PASS.

1. BUILD-REPORT's absolute sentences ("NO 'first' wording
   appears anywhere in this build"; "no 'first' wording
   anywhere") are literally overstated. The word "first" does
   occur in non-claim uses: the build-tier descriptor
   "first-pass", "the first task list for any later repair
   pass" in the flags disclosure, and the dictionary seat
   "first — пӗрремӗш" in the glossary (a translation seat for
   the Master's word "first"). None of these asserts priority
   over Saifutdinov or anyone else, and no priority claim
   exists anywhere in the build. Remediation, if Robert wants
   the absolute wording to stand literally, is a one-line
   softening in BUILD-REPORT (e.g. "no first-ever claim").
2. BUILD-SPEC states: "The two Master seats carrying a literal
   '<redacted>' placeholder are rendered for their surrounding
   sense." In fact no seat in the Locked English Master and
   none in master-verses.json contains the string "redacted" —
   the count is 0 everywhere, and build.py's replace of
   "<redacted>" is a no-op on this lane; the sentence reads as
   sibling-lane boilerplate carried into this spec. The
   substantive claim it supports — no 'redacted' seats in the
   draft — is true. Remediation, if wanted, is deleting or
   correcting that one spec sentence.
3. The attestation screen's 0-untraced figure rests on exactly
   one form that is not itself in the inventory — ятпа (1
   occurrence, in 1:1), the regular instrumental of ят "name"
   (ят is a kaikki headword and is in the inventory). verify.py
   hard-codes ятпа plus seven other allowances (турӑ, шуйттан,
   аван, аванлӑх, ра, рен, ӑн); the checker confirms only ятпа
   actually needs the allowance — the other seven trace through
   the inventory or dictionary on their own. The derivation is
   disclosed in BUILD-SPEC ("ятпа is the regular instrumental
   of ят"). This is a disclosed device, not a hidden borrowing,
   but the headline figure is never to be quoted without it.

The checker also noted, on labelling: the exact DRAFT — NOT
PUBLISHED label stands on the manuscript's face and in
BUILD-REPORT; the spec, flags, licences, and glossary files
state the stop-before-landing position in other words, and the
raw data files quran-chv.txt and quran-chv.json carry no front
matter or label at all. The book a reader meets is labelled.

## Notes

- No PDF is included: the manuscript Markdown, the built text,
  and the built JSON are the landed forms, on the pattern of
  the Komi-Zyrian and Meadow Mari landings.
