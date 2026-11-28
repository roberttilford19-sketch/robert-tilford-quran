# Independent Re-Check Report — Erzya (myv) Quran Translation (post-remediation)

Checker: independent re-checker (built none of this text, did none
of the remediation; no edits made to the translation; nothing
landed). Date: 2026-11-27. Files checked: `verses-store.json`,
`master-verses.json`, `BUILD-SPEC.md`, `glossary.md`,
`sources/myv-lemmas.json`, `CHECKER-REPORT-MYV-2026-11-27.md`,
`REMEDIATION-LOG-MYV-2026-11-27.md`. Every figure below was
recomputed by this checker's own scripts (codepoint-level where
script is in question), not copied from the remediation log.

## OVERALL VERDICT: FAIL

Every claim in the remediation log is verified true on
recomputation — знярдо is gone, 7:166 is GAP-marked, 48:29 is
repaired, the English article is gone, the GAP census matches to
the marker, the canonical structure is exact, all five clause
repairs are seated as logged, and all four disclosure entries
exist and cover what the first checker required. The book
nevertheless FAILS the re-check's Item 1 as the task states it —
"any Cyrillic-Latin mixed token book-wide (0)" — because a
codepoint sweep found **13 script-mixed tokens in 12 seats**
(homoglyph Latin letters inside Erzya words) that neither the
first checker nor the remediation found: the first checker
reported the remaining Latin fragments as tokenisation artefacts
with 48:29 the one real exception, and that negative result does
not survive a codepoint check. The failure is narrow, mechanical
and repairable seat by seat; it is not a fidelity failure. Per
item:

| # | Item | Verdict |
|---|-------|---------|
| 1 | Forbidden / mixed / leakage counts | **FAIL** (знярдо 0 PASS; обезьяна 0 PASS; "the" 0 PASS; вешnez 0 PASS; any mixed token: 13 found, FAIL) |
| 2 | Canonical + GAP census | **PASS** |
| 3 | Repaired seats read against Master | **PASS** (all 12 seats; traces verified) |
| 4 | Fresh 24-verse clause sample | **PASS** (no dropped or distorted clause) |
| 5 | Disclosure entries in remediation log | **PASS** |

## Item 1 — Counts recomputed: FAIL on the mixed-token sub-criterion

- **знярдо / Знярдо: 0** occurrences book-wide (was 318 in 293
  seats). PASS. The replacement зярдо is an inventory lemma in
  `sources/myv-lemmas.json`; знярдо is not.
- **обезьяна (any form): 0** (was 1, at 7:166). PASS.
- **Standalone English "the": 0** book-wide, case-insensitive
  word-boundary count (was 8 in 5 seats). PASS.
- **вешnez: 0**; 48:29 now reads вешнезь. PASS on the named token.
- **Any Cyrillic-Latin mixed token book-wide: FAIL — 13 tokens
  in 12 seats.** Method: every whitespace token was stripped of
  surrounding punctuation and tested codepoint by codepoint for
  containing both U+0400–U+04FF and A–Z/a–z in a single
  hyphenless chunk. Hyphenated name forms (Latin personal name +
  Cyrillic case suffix across a hyphen, e.g. Adam-онь; 1,600
  tokens) are the names policy at work and are NOT counted, and
  the GAP-suffix token at 5:60 (⟦GAP: ape⟧кс — the Latin is the
  GAP term itself) is likewise excluded and noted separately.
  The 13 counted tokens, each verified by Unicode character
  names (Latin letter shown in the token):

  - 10:13 пин**get** (Latin g, e, t)
  - 17:107 Кемед**e** (final Latin e)
  - 18:29 к**emez**э ×2 (Latin e, m, e, z)
  - 18:69 мерьмас**o** (final Latin o)
  - 24:6 вало**c**ь (Latin c)
  - 24:58 ш**kat** (Latin k, a, t)
  - 46:24 пизем**e** (final Latin e)
  - 46:32 мен**e** (final Latin e)
  - 47:29 мел**e**ст (Latin e)
  - 47:38 серьгед**e**зь (Latin e)
  - 52:38 кустем**a** (final Latin a)
  - 53:57 мен**e**виксэсь (Latin e)

  These are homoglyph corruptions of the same class as the
  repaired вешnezь — visually invisible in ordinary reading,
  which is why a visual/tokenisation sweep missed them and a
  codepoint sweep does not. Until these 13 tokens are normalised
  to pure Cyrillic, the book does not meet the zero-mixed-token
  criterion the re-check was instructed to apply.

## Item 2 — Canonical re-verification and GAP census: PASS

- Store seats **6,236**; Master seats **6,236** (flattened from
  the nested Master); seat sets exactly equal — no missing, no
  extra seat.
- Per-surah counts match the Master at every surah, and match
  the standard canonical grid for all 114 surahs independently
  (grid sum 6,236; zero mismatches).
- 1:1 is exactly the fixed Basmalah "Пазонь лемсэ, Седеймариця,
  Седеймариця."
- The string "redacted" occurs **0** times; empty seats: **none**.
- GAP census recomputed: **70 markers in 56 seats** — jinn 30,
  pilgrimage 19, usury 8, Sabbath 7, apes 2, ape 1, cucumber 1,
  lentils 1, hoopoe 1. This matches the remediation log's claim
  exactly (the +1 marker / +1 seat against the first check is
  7:166, Item 3).

## Item 3 — Repaired seats read against the Master: PASS

All 12 seats were read in full against their Master verses.
Every clause of each Master verse is carried, and the specific
repairs are seated exactly as the remediation log records:

- **7:166** — "Be despicable apes" now reads "Уледе берянь
  ⟦GAP: apes⟧!", mirroring 2:65; the rest of the verse (rebellion
  against the commands, "We said to them") is carried.
  обезьянакс is gone.
- **48:29** — opening is now the clean "Muhammad — Пазонь
  кучовкс." (duplicated Пазонь removed); вешнезь stands for
  "seeking"; stern/compassionate, kneeling/prostrating, marks on
  faces, Torah/Gospel descriptions, the plant simile and the
  promise of forgiveness and great reward are all carried.
- **7:157, 9:111, 17:55, 21:105, 22:17** — the article "the" is
  dropped in all 8 former seats; the titles (Torah, Gospel,
  Quran, Psalms, Sabeans, Zoroastrians) stand under the names
  policy and every other clause of each verse is intact.
- **27:19** — аваргадсь (weeping verb) is gone; "He smiled and
  laughed at her words" rides on пейдсь alone, and пейдемс is
  the glossary §E seat for "laugh" and an inventory lemma. The
  prayer that follows is carried clause-complete.
- **5:110** — "obvious sorcery" now reads "неявикс тамаша
  теема", the book's logged тамаша device in the shape used at
  its other sorcery seats; "the leprous" now reads "проказасо
  сэредицятнень". **Trace run by this checker:** проказа IS a
  lemma in `sources/myv-lemmas.json` (exact match) — attested,
  seated legitimately, and disclosed in the log as
  Russian-shaped (Item 5). All other clauses (crib and maturity,
  Scripture and wisdom, the clay bird, the blind, the dead,
  Israel's children restrained) are carried.
- **65:4** — "if you have any doubts" now reads "бути тынь
  кавтолдатадо" — no longer disbelief. **Trace:** кавтолдомс IS
  an inventory lemma; кавтолдатадо is its regular 2pl present
  (spec paradigm 2pl -тадо/-тядо) and is the identical form the
  book already seats at 2:23 (verified in the store). The
  three-month term, the not-yet-menstruated clause, the pregnant
  clause and the God-fearing close are all carried. The
  menopause clause remains the builders' paraphrase ("од шкадо
  мейле шкас"), as the remediation log states it was not in its
  repair list; the clause is present, not dropped.
- **31:25** — "Praise be to God" now reads "Шнамо Пазонтень",
  the book's own praise form from 1:2 (шнамо/шнамс both traced
  to the inventory; шнамс is the "praise" seat). Сюкпря is gone
  from this seat.
- **22:5** — "it vibrates, and swells" now reads "сон чикорды,
  ды боции, ды касы" — swells stands as its own clause.
  **Trace:** боциямс IS an inventory lemma; боции is its
  regular 3sg present on the spec's printed paradigm (3sg
  -ы/-и), exactly as the log states. The full creation sequence,
  womb, infancy, strength, death, old age and the rain/plant
  close are carried.

## Item 4 — Fresh clause-fidelity spot sample: PASS

Sample: 24 verses chosen by this checker, spread across the
book and weighted to long verses, with **zero overlap** with
the first checker's 52-verse sample: 2:255, 3:154, 4:34, 6:59,
8:41, 9:40, 11:41, 12:87, 14:32, 16:90, 19:71, 24:31, 26:88,
30:21, 35:29, 38:26, 40:60, 49:13, 55:17, 57:20, 62:9, 67:15,
76:8, 90:13. Erzya/Master word ratios run 0.60–1.23, consistent
with Erzya's lack of articles; the low ratios are the shortest
verses (90:13, 3 Erzya words for "The freeing of a slave" —
clause-complete; 55:17 likewise complete).

Each verse was read clause by clause against the Master. **No
dropped clause and no distorted clause was found in the 24.**
The longest seats are carried in full: 2:255 (throne verse —
slumber/sleep, heavens and earth, intercession by permission,
before/behind, knowledge, Throne, preservation, Most High/Great
all present), 3:154 (security, slumber, self-concern, the
exchange of speeches, homes/death-beds, testing and purifying,
hearts), 24:31 (the full believing-women list, every kin
category present in order), 57:20 (play/distraction/glitter/
boasting/rivalry, the rain-and-wither simile, Hereafter agony
and forgiveness), 9:40 (cave, second of two, tranquility,
unseen forces, lowest/highest word). Two compressions are noted
for the record, neither a drop: 6:59 renders "clear record" as
виде сёрмадома ("true record" — the record clause stands,
"clear" weakened to "true"); 40:60 compresses "too proud to
worship Me" into a pride-marked worship clause (the pride and
the worship are both present; the forcible entry into Hell is
carried).

## Item 5 — Disclosure entries in the remediation log: PASS

All required entries exist in `REMEDIATION-LOG-MYV-2026-11-27.md`
(§"Disclosures", D1–D4, plus the проказа note at Repair 5),
each marked DISCLOSED, not regularised, and the seats stand as
built (verified in the store):

- **D1, мерсь:** entry present; this checker's recount confirms
  мерсь ×161 against ёвтась ×310, with the spec's hedge quoted.
- **D2, loans:** entries present for искушения (recount ×3),
  средства (recount ×6 occurrences in 5 seats — the log states
  both figures and the counting difference against the first
  checker's ×5) and чеснок (recount ×1, at 2:61); **проказа**
  is disclosed at its Repair 5 seat entry and again in D2 as an
  inventory-attested Russian-shaped lemma seated by the
  remediation.
- **D3, capitalisation:** entry present, covering divine
  pronouns and epithet participles (Минь, Сон, Содыця, Простиця,
  Мон/Тон in direct speech) beyond the spec's letter.
- **D4, Latin "O":** entry present; this checker's recount
  confirms standalone Latin "O" ×40, with the inconsistent
  Erzya vocative practice (Эй, / Cyrillic О elsewhere) named.

## Summary

The remediation is, on every one of its own claims, exactly
what it says it is — verified here by independent recomputation,
seat reads and inventory traces (проказа, боциямс→боции,
кавтолдомс→кавтолдатадо all traced to `sources/myv-lemmas.json`
or the spec paradigm by this checker). The book's canonical
structure (6,236 = 6,236, grid-exact, Basmalah fixed, no
"redacted", no empty seat), its GAP census (70 markers, 56
seats, term-for-term as claimed) and its clause fidelity (12
repaired seats + a fresh 24-verse sample, no dropped clause)
all PASS. The single bar to an overall PASS is the 13
homoglyph script-mixed tokens listed under Item 1 (10:13,
17:107, 18:29 ×2, 18:69, 24:6, 24:58, 46:24, 46:32, 47:29,
47:38, 52:38, 53:57): normalising those 13 tokens to pure
Cyrillic — a mechanical fix touching 12 seats, no retranslation
— would clear the only failing criterion. The re-checker made
no edits to the translation and landed nothing.
