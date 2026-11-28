# Independent Checker Report — Erzya (myv) Quran Translation

Checker: independent checker (built none of this text; no edits made).
Date: 2026-11-27. Files checked: `verses-store.json`,
`ayah-companion-manuscript-MYV.md`, `master-verses.json`,
`work/master-<A-M>.json`, `work/batch-<A-M>.json`, `BUILD-SPEC.md`,
`glossary.md`, `ATTESTATION-AUDIT-2026-11-27.md`,
`work/notes-<B-M>.md`, `work/verify-candidates.json`,
`sources/myv-lemmas.json` (39,661 lemmas). All figures below were
recomputed by the checker's own scripts, not copied from the sweep.

## OVERALL VERDICT: FAIL

The book is canonically exact and, in the clause sample, genuinely
clause-faithful — but it fails the attestation gate on one explicit,
book-scale BUILD-SPEC prohibition (знярдо, 318 occurrences), and it
carries three smaller honesty/orthography defects (an unattested
Russian loan seated where sister seats are GAP-marked, 7:166; retained
English "the" in five seats; one script-mixed token, 48:29). Every
failure is narrow and repairable; none requires retranslation. Per
check:

| # | Check | Verdict |
|---|-------|---------|
| 1 | Canonical | **PASS** |
| 2 | Clause fidelity (52-verse sample) | **PASS**, with isolated failures named below |
| 3 | GAP honesty | **FAIL** (one seat, 7:166; system otherwise exemplary) |
| 4 | Attestation | **FAIL** (знярдо; мерсь ruled a lesser deviation) |
| 5 | Orthography / script | **FAIL** (48:29 script-mixed token; "the" leakage counted under Check 3/5) |

## Check 1 — Canonical: PASS

Recomputed: store seats 6,236; Master seats 6,236; seat sets exactly
equal (store == Master, no missing, no extra). Every batch file
`batch-<A-M>.json` equals its store slice and its `master-<X>.json`
key set (13/13 batches, seat counts 493/461/519/556/454/449/537/501/
540/469/516/548/193 = 6,236). Per-surah counts match the Master at
every surah, and spot-verified against the standard canonical grid
for surahs 62–114: zero mismatches. 1:1 is exactly the fixed Basmalah
"Пазонь лемсэ, Седеймариця, Седеймариця."; 1:3 matches the spec's
frameless form. The string "redacted" occurs 0 times; the two Master
placeholder seats are rendered for sense (39:7 fully, including the
burden clause; 48:8 "witness … bearer of good news … warner" all
carried). Empty seats: none. The Purple figures are confirmed in
full. (The manuscript's GAP count of 70 vs the store's 69 is the
front-matter template "⟦GAP: …⟧" explaining the marker — not a
discrepancy; 40 randomly sampled store verses all appear verbatim in
the assembled manuscript.)

## Check 2 — Clause fidelity: PASS, isolated failures named

Sample: 52 verses, 4 per batch A–M (the two longest Master verses in
each batch plus two seeded-random verses over 25 Master words; seed
42). Seats: 2:282, 2:102, 2:111, 2:30, 5:110, 4:102, 5:38, 5:16,
7:143, 10:24, 8:32, 7:149, 13:31, 13:16, 16:14, 11:44, 18:19, 18:22,
20:134, 17:59, 22:5, 24:61, 24:35, 23:44, 27:40, 28:15, 27:19,
27:18, 33:50, 33:53, 31:25, 32:26, 42:15, 39:71, 40:28, 42:49,
48:29, 46:15, 46:7, 52:16, 73:20, 60:10, 58:7, 65:4, 74:31, 78:38,
85:10, 78:40, 98:8, 98:6, 98:5, 101:4. Each was compared clause by
clause against the Master.

No systematic dropping exists. The longest verse in the book, 2:282
(227 Master words), is carried clause-complete, as are 5:110, 4:102,
24:61, 33:53, 73:20 and 60:10. Book-wide, the Erzya/Master word ratio
is mean 0.841, median 0.833 (long verses: mean 0.830, minimum 0.423) —
consistent with Erzya's lack of articles, not with omission. The
magic/sorcery seats ride a descriptive device (тамаша family) that
is logged in notes-C, notes-F and notes-M; that disclosure was
verified, so those seats are devices, not silent losses.

Isolated failures and distortions, seat by seat:

- **27:19** — "He smiled and laughed at her words": Erzya "Сон пейдсь
  ды аваргадсь" adds аваргадсь, on авардемс "weep" — laughed is
  rendered with a weeping verb. Distortion.
- **5:110** — "obvious sorcery" → "виде берянь тев" (obvious evil
  deed) and "the leprous" → "сэредицятнень" (the sick, generic):
  both content words weakened beyond the logged тамаша device used
  elsewhere.
- **65:4** — "if you have any doubts" → "бути тынь ули а кемема"
  (if you have unbelief): doubt rendered as disbelief; the menopause
  clause is a vague paraphrase ("од шкадо мейле шкас").
- **31:25** — "Praise be to God" → "Сюкпря Пазонтень" (thanks to
  God): praise/thanks substitution.
- **22:5** — "it vibrates, and swells": "swells" is absorbed into
  касы (grows); no separate swelling clause.
- **48:29** — "Muhammad is the Messenger of God" → "Muhammad —
  Пазонь кучовкс Пазонь" (God's messenger of God): duplicated
  Пазонь, garbled opening clause (the script defect in this verse
  is under Check 5).

These are isolated; they do not form a pattern, and no sampled verse
drops a whole clause. PASS stands on this check, with the seats
above on the record.

## Check 3 — GAP honesty: FAIL (one seat)

Recomputed GAP figures, confirming Purple: 69 markers in 55 seats —
jinn 30, pilgrimage 19, usury 8, Sabbath 7, cucumber 1, lentils 1,
apes 1, ape 1, hoopoe 1. Consistency audit against every Master seat
carrying the term or its sense (jinn/sprites, Hajj/Umrah/pilgrim,
Sabbath, usury, apes): every term seat is GAP-marked, with one
exception —

- **7:166** — "Be despicable apes" is rendered "Арадо вечкевикстевтеме
  **обезьянакс**", seating Russian обезьяна, which is **not in
  `sources/myv-lemmas.json`** (neither обезьяна nor the stem) and is
  not in the glossary or the attestation audit. The same word is
  GAP-marked at 2:65 (⟦GAP: apes⟧) and 5:60 (⟦GAP: ape⟧). This is
  both an inconsistent GAP and a silent Russian borrowing, against
  BUILD-SPEC ("NEVER borrow silently from … Russian"). FAIL seat.

No verse is left substantially in English. Latin tokens (1,266 total)
are overwhelmingly the Master's proper names and titles, which the
names policy seats unaltered, plus the disjointed-letter verses
(2:1, 3:1, 7:1, 19:1, 20:1, etc.), which the spec also seats as in
the Master. One exception class:

- **Retained English article "the" — 8 occurrences in 5 seats**:
  7:157 ("the Torah", "the Gospel"), 9:111 ("the Torah", "the
  Gospel", "Quran" with "the"), 17:55 ("the Psalms"), 21:105
  ("the Psalms"), 22:17. The titles themselves are policy; the
  English article is not part of any title and is retained English
  inside Erzya sentences. Minor, but it is leakage and must be
  named. (The single "Bedouin" at 33:20 is the Master's ethnonym
  carried in a descriptive clause — "паксясо Bedouin марто", "in
  the desert with the Bedouin" — a name-policy carry, not leakage;
  it is disclosed here so the record is complete.)

Apart from 7:166 and the "the" seats, the GAP system is honest and
consistent: jinn is never silently replaced by идемевсь/шайтян,
pilgrimage markers cover the Hajj, Umrah and pilgrim-sanctity seats
(2:158, 2:189, 2:196, 2:197, 3:97, 5:1, 5:2, 5:95, 5:96, 9:3, 9:19,
22:27), and every GAP seat renders the rest of its verse in full.

## Check 4 — Attestation: FAIL

Method: the 30 most frequent Cyrillic tokens were traced against
`sources/myv-lemmas.json`, the glossary, and BUILD-SPEC paradigms;
30 untraced candidates were drawn at random (seed 20261127) from
`verify-candidates.json`'s 3,047-candidate list and traced the same
way. Recomputed token figures: 116,190 Cyrillic tokens, 8,217
distinct lower-cased forms (Purple's 8,164 differs only by
tokenisation of hyphenated forms — immaterial).

Top-30 result: 26 of 30 are exact inventory lemmas (ды, а, сынст,
сынь, сон, минь, сонзэ, тынк, тынь, марто, мезе, но, паз, эйстэ,
паро, бути, тонь, виде, тон, монь, секс, берянь, мон, те, туртов,
мейле). The remaining four are regular paradigm forms of attested
lemmas: конат (кона + plural -т), ули (3sg of улемс), пазонь
(genitive of паз, per the spec's own paradigm), пазось (definite
nominative of паз). Top-30 attestation: clean.

Random-30 untraced result: 28 of 30 decompose regularly on attested
stems — e.g. пурназь (participle, пурнамс), изнязь (изнямс),
кадызь/кадсызь (past, кадомс), кучизе (кучомс), пейдтадо (пейдемс),
полавтовольть (полавтомс), велявтовельть (велявтомс), вайгелензэ
(вайгель + possessive), бутияк (бути + clitic -як), сэтьмелгады
(сэтьме + inchoative; the infinitive сэтьмелгадомс is itself an
inventory lemma). Two are stem-traced but formally irregular:
таргемс at 14:26 and 15:66 (infinitive variant on attested таргамс,
used as a passive "be uprooted") and the ванькставт- family
("warner", book-wide; inventory carries the cognate causative
ванькскавтомс on ванькс, not this exact stem shape). Both are
flagged here as minor formal irregularities, not inventions ex
nihilo. The 3,047-candidate list is therefore what Purple said it
is: an instrument candidate list dominated by inflected forms, not
a verdict of unattestation.

The three seats the task named for specific ruling:

- **знярдо — FAIL, and it decides this check.** BUILD-SPEC states in
  plain words: "знярдо is NOT seated (use кода / сестэ "then" for
  "when")". Recomputed: знярдо occurs **318 times in 293 seats**,
  concentrated in batches E (74), I (66), K (63), L (55), J (48),
  F (2) and M (10); batches A–D, G, H use none. It is **not in the
  lemma inventory** (checked exact and lower-cased). The attested
  synonym зярдо is itself an inventory lemma and is used 576 times
  elsewhere in the same book — so an attested form existed, was
  known to the builders, and the forbidden form was seated anyway,
  in roughly one verse in twenty-one. Whatever знярдо's status in
  Erzya at large, the house rule for this book forbade it by name,
  and the book breaks that rule at scale. Batch notes do not
  disclose it (notes-E quotes one знярдо verse without comment; no
  other notes file mentions it). Attestation cannot PASS with this
  seat standing.
- **мерсь — deviation, not a failure of attestation.** Recomputed:
  мерсь 161 times; the spec's preferred ёвтась 310 times. BUILD-SPEC
  itself prints мерсь inside its past-tense paradigm ("3sg -сь
  (тейсь, содась, мерсь→…") and then hedges: "use мерсь only if
  sure; safer 3sg past of меремс is ёвтась", with ёвтась named the
  standing narrative form. мерсь is the paradigm-regular 3sg past
  of the attested lemma меремс; it is not an invented form. But the
  builders used the hedged form 161 times against the spec's stated
  preference, undisclosed in the batch notes. Ruled: a spec-
  preference deviation to be regularised or disclosed, not an
  attestation breach.
- **Retained Latin candidates** — "O" ×40 is the Master's vocative
  "O" before names (18:86, 18:94, 19:7, 19:12, 19:27, …), carried
  with the names under the names policy: acceptable, though an
  Erzya vocative exists in the book's own practice elsewhere
  ("Эй," at 2:61 and 2:275; Cyrillic "О" at 2:189-type seats) —
  the practice is inconsistent and should be disclosed. "Bedouin"
  ×1 at 33:20: name-policy carry, see Check 3. The remaining Latin
  fragments in the sweep (e, c, kat, emez, nez) are tokenisation
  artefacts of hyphenated names — with one real exception, the
  script-mixed token at 48:29 under Check 5.

Two further inventory-attested but undisclosed Russian-shaped loans
were found while tracing: искушения ×3 (2:49, 2:66, 2:102) and
средства ×5 (2:102, 58:4, 58:12, 65:6, 65:7), plus чеснок at 2:61.
All three stems stand in the Giella inventory, so they are not
inventions; but BUILD-SPEC seats Russian-shaped loans "only as
flagged in the audit", and none of the three is flagged in the
attestation audit or the glossary (the flagged list is рай, пост,
ангел, ханства, сатана). Disclosure defect, minor, named here.

## Check 5 — Orthography / script: FAIL (one seat)

Script inventory recomputed: apart from Latin (names, titles,
disjointed letters — policy) and the GAP markers, the text is
Cyrillic in the Russian 33-letter set; no non-standard letters
occur. No Moksha-specific markers were identified: the book uses
the Erzya forms the spec fixes (весе "all", эйкакш "child", паз,
менель, мода, ведь), and no Moksha-distinctive lexeme was found in
the samples or the top-frequency list — this is a negative result
from sampling and frequency inspection, not a full Moksha lexicon
diff, and it is stated as such.

- **48:29 — FAIL seat.** The token "вешnezь" mixes Cyrillic and
  Latin letters inside one word ("веш" + Latin "nez" + "ь") in
  "вешnezь чансть Паздо" ("seeking blessings from God"). A
  typesetting/script corruption in a seated verse.
- Capitalisation: sentence-initial and proper names per spec, with
  Паз and its forms capitalised. Two extensions beyond the spec's
  letter were observed and are disclosed, not failed: divine
  pronouns and epithets are capitalised mid-sentence throughout
  (Минь "We" of God ×1,386 mid-sentence, Сон ×831, participles such
  as Содыця and Простиця as divine titles), and Мон/Тон are
  capitalised in some direct-speech seats. The practice is
  consistent and reverential in intent, but the spec says
  "sentence-initial and proper names only, plus Паз and its
  pronouns where the Master capitalises" — the extension to
  epithet participles goes past that letter and should be either
  disclosed on the book's face or regularised.

## Summary of what must be repaired before this book can PASS

1. знярдо (318 occurrences, 293 seats, batches E, F, I, J, K, L, M):
   replace with the attested зярдо / кода / сестэ per BUILD-SPEC,
   or obtain a ruling that seats it with disclosure. As built, it
   breaks an explicit spec prohibition.
2. 7:166: обезьянакс → ⟦GAP: apes⟧, matching 2:65 and 5:60.
3. 48:29: вешnezь → вешнезь; also repair the duplicated Пазонь in
   the same verse's opening clause.
4. "the" before titles at 7:157, 9:111, 17:55, 21:105, 22:17
   (8 occurrences): drop the English article; the titles stand.
5. Disclose or regularise: мерсь (161) against the ёвтась
   preference; the loans искушения, средства, чеснок; the
   capitalisation of divine epithets; Latin "O" vs Erzya vocative
   practice.
6. Clause-level repairs from Check 2: 27:19 (аваргадсь), 5:110
   (sorcery, leprous), 65:4 (doubts), 31:25 (praise), 22:5
   (swells).

What stands proven in the book's favour, in the same breath: the
canonical structure is exact at every seat (6,236 = 6,236, Basmalah
fixed, no "redacted", no empty seat); the GAP system is consistent
at every term seat except 7:166; and a 52-verse clause sample
spread over all thirteen batches, weighted to the longest verses,
shows clause-complete rendering with no systematic dropping. The
FAIL is a gate verdict on the defects named above — chiefly
знярдо — not a judgement that the translation is broadly unfaithful.
The checker made no edits to the translation and landed nothing.
