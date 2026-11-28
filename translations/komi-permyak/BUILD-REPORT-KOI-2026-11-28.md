# Komi-Permyak (koi) Quran draft — BUILD REPORT (2026-11-28)

**Result: complete first-pass draft built and STOPPED before
landing. Nothing landed, shelved, committed, or pushed. The
draft awaits a fresh independent checker.**

Status: DRAFT — NOT PUBLISHED.
Work folder: ~/workspace/ayah-komi-permyak/
Authorisation: Robert Tilford's open-in-order queue ruling
2026-11-27 21:16 CST (… Komi-Zyrian, Komi-Permyak, Chuvash …).
Gate conditions: CANDIDATE-BRIEF-KOMI-PERMYAK.md (goal
hidden_files). Model lane: ~/workspace/ayah-komi-zyrian/,
including its independent checker's lessons, applied from the
start: (1) carried names ride an EXPLICIT allowlist only,
never derived from Master capitalisation; (2) retained-Latin
and mixed-script screens run on WHITESPACE tokens, not a
Cyrillic-only regex; (3) core terms ride ONE seat each;
(4) standing GAP families (Sabbath, pilgrimage, Hajj, Umrah)
are GAP-marked at every seat, never retained in English;
(5) seat 1:3 takes the spec's Basmalah mercy-names form
exactly.

## Relaunch note
The previous crew stopped at execution timeout during source
harvest. Its sources/kaikki-koi.jsonl (162 bytes) was the
kaikki.org 404 page: kaikki has NO Komi-Permyak per-language
download (its dictionary index lists Komi-Zyrian only). The
bogus file was deleted and the harvest redone cleanly:
GiellaLT lang-koi (already on disk; licence read, LGPL v3)
plus English Wiktionary Komi-Permyak entries through the
MediaWiki API.

## Counts (recomputed by verify.py, 2026-11-28)
- Verses: **6,236 / 6,236** — store seats == Master seats,
  per-surah grid exact against the standard grid, no empty
  seats, "redacted" nowhere.
- GAP census: **5,444 GAP seats** (87.3% of verses),
  **16,840 GAP markers**, **4,728 distinct GAP terms**,
  **792 verses rendered without a marker**. (Manuscript
  marker count 16,841 = the text's 16,840 + the front-matter
  explanatory example.)
- Basmalah: fixed form "Енлӧн нимӧн, Милӧсьта, Милӧсьта." —
  **113** occurrences in quran-koi.txt (112 unnumbered +
  numbered 1:1; surah 9 none). Seat 1:3 = "Милӧсьта,
  Милӧсьта." exactly, per spec. 27:30's in-verse Basmalah
  rendered on the same seats.
- Number battery (spot-checked by hand against the Master):
  18:25 nine ӧкмыс ✓ · 7:142 thirty + ten = forty ✓ ·
  12:4 eleven дасӧтік ✓ · 38:23 ninety-nine and one ✓ ·
  17:101 nine ✓ · 69:7 seven and eight ✓ · 2:234 four and
  ten ✓ · 23:17 seven ✓ · 11:13 ten ✓.

## Dictionary and sources
- Seated dictionary: **1,317 entries**; dropped as unverified
  at build time: **0**.
- Inventories: GiellaLT giella-koi stem files **77,661
  lemmas**; giella-koi dictionary XML **14,725 glossed
  lemmas** (Russian glosses); gt-norm paradigm test files
  **15,533 forms** (proofread by Larisa Ponomareva,
  2019-10-22); English Wiktionary Komi-Permyak **334
  headwords** with English glosses.
- Dictionary build: manual core (work/dict_core_koi.py) +
  712 gloss-matched seats (work/dict_koi.json, built by
  work/build_dict.py from work/dict_rus.py / dict_rus2.py);
  283 curated keys unmatched, logged at work/unmatched.json.
- Sources and licences: LICENCES-RECORDED-2026-11-28.md.
  Bible control: complete New Testament only (Бур Юӧр 2019,
  Institute for Bible Translation, Finland), fact and
  citation only, never a spelling authority; no complete
  Bible in Komi-Permyak was found.

## Verification screens (verify.py; candidates for the
## independent checker, not a verdict)
- Cyrillic attestation: 841 distinct tokens, **0 untraced
  candidates** — every token traces to a koi inventory lemma,
  a glossary lemma, or a disclosed regular derivation
  (including the Permyak doubled-consonant plural). Two
  Zyrian forms caught in the first engine draft (войтыр and
  Zyrian plural shapes) were removed and the build re-run
  before these figures were taken.
- Retained Latin (whitespace tokens, GAP interiors excluded,
  explicit allowlist): allowlisted 129 types / 1,056 tokens
  (names, titles, disjointed letters); **non-allowlist
  retained Latin: 0 types, 0 tokens** — no silent English
  tier.
- Mixed-script tokens: 6, all the disclosed name + -лӧн
  genitive device (5:27, 7:127, 11:74, 12:58, 40:28, 40:37);
  other mixed tokens: NONE.

## Files
- verses-store.json — the seat store {S:V}.
- quran-koi.txt / quran-koi.json — built text (build.py).
- ayah-companion-manuscript-KOI.md — the assembled book with
  honest front matter (assemble.py; merge.py re-runs both).
- BUILD-SPEC.md · LICENCES-RECORDED-2026-11-28.md ·
  ATTESTATION-AUDIT-2026-11-28.md ·
  FLAGS-AND-GAPS-DISCLOSURE-KOI-2026-11-28.md · glossary.md
- work/build_engine.py, work/build_dict.py, work/harvest.py,
  work/make_glossary.py, work/dict_core_koi.py,
  work/dict_rus.py, work/dict_rus2.py, work/dict_koi.json,
  work/unmatched.json, work/unverified-dict.json (empty),
  work/verify-candidates.json.
- sources/: giella-koi-lemmas.json, koi-gloss-dict.json,
  yaml-forms.json, wikt-koi-parsed.json, eng2koi-wikt.json,
  lang-koi-main/, lang-koi.zip.

## Open items for the independent checker (named, not hidden)
1. Sample the 712 gloss-matched seats for homonym traps of
   the kind removed by hand during the build (панлавны,
   веськӧтлыны, тор); known candidates are listed in the
   disclosure (peace → му, pay → мед, understand → артавны,
   the 1:7 final clause).
2. Rule on the flagged thin/device seats, singly: милӧсьта
   (mercy), ен for Lord, веськыт (righteous), казьмӧтны
   (warn), мезмӧтны (save), келмӧм (prayer), видз (fasting),
   дон (reward), гижӧт (scripture), пас/кодзув/саридз/мыж/
   джинн (glossless lemmas).
3. The GAP tier is heavy (87.3% of verses carry a marker;
   clean share 12.7%, against Komi-Zyrian's 21.9%): the
   markers are honest and disclosed on the book's face, and
   no house rule sets a GAP ceiling, but the checker should
   rule on the tier as the Komi-Zyrian checker did.
4. Clause-fidelity sample and the checker's own recount, as
   in the sibling lanes.

**STOP state: the draft is complete and verified by the
build's own screens; it has NOT been independently checked,
and it is NOT landed, shelved, committed, or pushed.**

---

## Addendum — 2026-11-28 (remediation pass; this addendum corrects the record above, which is not rewritten)

The independent checker report of 2026-11-28 (verdict FAIL, §7) established that this report's sentence — "Two Zyrian forms caught in the first engine draft (войтыр and Zyrian plural shapes) were removed and the build re-run before these figures were taken" — did not hold for the phrase table: эскісьяс (272 tokens, 250 seats) and вӧчісьяс (67 tokens, 66 seats), 339 tokens in 313 seats, stood in the text with the Zyrian plural suffix -яс. Remediation was applied the same day under the standing gate law (full record: REMEDIATION-RECORD-2026-11-28.md):

- work/dict_core_koi.py PHRASES now seats эскісььэз / Оз эскісььэз / Лёк вӧчісььэз (Permyak agent plural: stem-final сь doubled + -эз, cf. ыстісььэз, адззылісььэз), and the whole book was rebuilt from the engine (store, quran-koi.txt, quran-koi.json, manuscript).
- Seat 1:7's final clause is re-seated: "misguided" now rides the glossary's astray seat вошны (present вошӧ) by a direct OVERRIDE entry, instead of falling through the engine's mis- prefix stripping to the guide verb нуӧтӧ. The same direct seat corrects the other six seats carrying the token "misguided" (16:25, 18:104, 26:86, 27:41, 36:47, 56:51). Final clause at 1:7 now reads "ни эна кин лоӧ вошӧ".
- verify.py is tightened: the single-letter endings ("а", "я", "м", "д", "с", "н") are removed from its ending-stripping decomposition and a token ending in -яс is rejected outright as the Zyrian plural. On the unrepaired text the tightened screen returns exactly эскісьяс ×272 and вӧчісьяс ×67 as untraced candidates — the fault class can no longer be absorbed letter by letter. On the repaired text it returns 0 untraced candidates.
- New figures after remediation (recomputed by the tightened verify.py and independently in the remediation record): verses 6,236/6,236, seat-set equal, per-surah grid exact; GAP seats 5,444, GAP markers 16,840, distinct GAP terms 4,728, verses without a marker 792 (all unchanged); Basmalah 113 occurrences in quran-koi.txt, 1:1 and 1:3 exact; distinct Cyrillic tokens 841, untraced 0, tokens containing ӧ 369 types, containing і 35 types (all unchanged in count — the two -яс types are replaced by the two -ьэз types); retained Latin non-allowlist 0 types / 0 tokens, allowlisted 129 types / 1,056 tokens; mixed-script tokens exactly the 6 disclosed name + -лӧн tokens; -яс plural tokens 0. Seated dictionary is now 1,318 entries (was 1,317; +1 for the direct "misguided" seat), dropped as unverified 0.
- The alms standing-family discrepancy (checker §3) is reconciled in the attestation audit's addendum of the same date: the technical zakat term remains a standing GAP family; the generic seat rides the attested корӧм, as the generic scripture seat rides гижӧт.

**STOP state unchanged: nothing landed, shelved, committed, or pushed. The remediated draft awaits a fresh independent re-check PASS.**
