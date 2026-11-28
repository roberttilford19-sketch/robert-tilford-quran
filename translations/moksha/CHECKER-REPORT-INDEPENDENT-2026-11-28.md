# Independent Checker Report — Moksha (mdf) Quran Draft

Checker: a fresh agent who built none of this text. Date: 2026-11-28.
Scope: `quran-mdf.txt`, `quran-mdf.json`, `verses-store.json`,
`ayah-companion-manuscript-MDF.md`, checked against
`master-verses.json` (the lane copy of the Locked English Master),
`BUILD-SPEC.md`, `glossary.md`, `ATTESTATION-AUDIT-2026-11-27.md`,
`LICENCES-RECORDED-2026-11-27.md`, and the build's own
`FLAGS-AND-GAPS-DISCLOSURE-MDF-2026-11-27.md`. Every figure below
was recomputed with the checker's own scripts; the build crew's
`verify.py` was re-run only as a cross-check and reproduced its
reported figures exactly. Nothing was edited, landed, shelved,
committed, or pushed by this check.

## VERDICT: FAIL

The book's skeleton is sound — counts, seat-set, Basmalah, GAP
census, and the Erzya bar all pass exactly as reported. The FAIL
rests on the attestation gate the build set for itself: four
unattested or expressly barred function-word families are seated
at scale (што/штоба 623 tokens, эли 127, иля/иляда 117, мельга 48
word tokens), on 21 mixed-script tokens in which Latin
transliteration tails are fused to Cyrillic stems, on one garbled
legal clause with a literal ellipsis left in the finished text
(4:23), and on one number error in the fidelity sample (29:14).
Every failing item is bounded and remediable; none requires a
rebuild. Reservations that do not by themselves fail the book —
кда (865 tokens, spec-authorised but inventory-unattested), the
сынь pronoun variant (265 tokens), the disclosed
prophet/messenger collapse, the 74:30 teen formation, the 4:56
кедь skin seat, Latin manna/Bedouin retention, and one unclosed
guillemet — are stated in the summary at §10 and detailed in §9.

## 1. Recount, seat-set, empty seats, redactions — PASS

- Store seats 6,236; master seats 6,236; seat sets exactly equal
  (no missing, no extra). `quran-mdf.json` flattened equals
  `verses-store.json` seat for seat (6,236/6,236, texts identical).
- Per-surah grid clean at all 114 surahs against the standard
  grid (sum 6,236); the numbered verse lines in `quran-mdf.txt`
  also match the grid at all 114 surahs, and txt verse texts match
  the store at every seat except nine trailing-space differences
  (see §9.7).
- Empty seats: NONE. No seat shorter than three characters.
- The string "redacted" (any case) appears in no seat. All seven
  master placeholder seats (39:7, 48:8, 33:45, 35:24, 11:2, 12:96,
  17:105) are rendered for their surrounding sense; spot-read,
  each carries the "bearer of good news / warner" sense in Moksha
  with no placeholder residue.

## 2. Basmalah — PASS

- 1:1 equals the fixed form exactly:
  «Шкаень лемса, Милостивай, Милостивай.» — the only store seat
  equal to it; 1:3 is «Милостивай, Милостивай.» as specified.
- In `quran-mdf.txt`: exactly 112 standalone Basmalah lines —
  one at the head of every surah except surah 1 (where it is
  verse 1, numbered, not standalone) and surah 9 (none, verified:
  surah 9 opens directly at verse 1). No surah carries two.
- 27:30 carries the Basmalah inside the verse, matching the
  Master's Solomon-letter seat. Correct, not a double seating.

## 3. GAP census and GAP practice — PASS, with one exception (§8.5)

- Recomputed: 57 GAP seats, 67 markers — jinn 31, pilgrimage 16,
  usury 8, Sabbath 7, apes 2, gnat 1, cucumber 1, fig 1. The seat
  list matches the disclosure's list seat for seat. All markers
  are well-formed (⟦/⟧ balanced at 67/67; no malformed "GAP"
  strings). The manuscript's 68th marker is the front matter's
  own explanation of the format, not a verse seat.
- No silent seating of standing terms: every master seat
  containing "jinn" (26 seats), "usury" (6), "Sabbath" (5),
  "gnat" (1), "cucumber" (1), "fig" (1), or "pilgrimage/hajj" (7)
  carries a GAP marker. Marker counts above the master's word
  counts (e.g. jinn 31 markers over 26 word-seats) come from
  verses naming jinn twice or in construct phrases — checked,
  not over-marking. Pilgrimage markers sit in Hajj-context seats
  (2:158, 2:196–197, 5:95–96, 22:27…) where the rite, not the
  word, is the seat.
- The one exception is 7:166 (apes), detailed at §8.5.

## 4. Erzya bar, seat by seat — PASS

Whole-token recount over all Cyrillic tokens, case-insensitive:
паз 0, чи 0, кедь 0, теште 0, кинига 0, казне 0, пежеть 0,
шайтян 0, пророк 0, баславамс 0, седеймариця 0. Substring scans
find no шайтян/шайтан, пророк, пежеть, or паз stem anywhere in
the book. The Moksha seats stand in their place throughout:
кядь family (60+ distinct forms), тяште family, бславамс family
(35+ forms), ши 130 whole tokens against чи 0. Two
stem-collisions required seat-by-seat settlement:

- **казнефт at 34:35 and 37:59 — PASS.** Not the barred Erzya
  noun казне (0 whole tokens; казне never seats). It is the
  regular -фт participle on казня "punishment", which is in the
  build's own inventory and is the glossary's flagged loan seat
  (казня family: 141 whole tokens plus full paradigm). The batch
  H note states the same ground. Settled: pass.
- **кедьсна / кедьса at 4:56 — recorded reservation, not a
  failure.** The only кедь- tokens in the book (2 tokens, one
  seat). The seat's sense is "skins" (the Master's 4:56 is the
  roasted-skins verse), and кедь in the sense "skin, hide" is in
  the build's mdf inventory — a genuine Moksha word that
  coincides in form with the Erzya word for "hand". The barred
  sense (hand) is nowhere seated; hand is кядь throughout. The
  seat is defensible, but the disclosure's claim of "zero
  Erzya-bar seats" is true only on the whole-token reading, and
  the build's screen would not have caught an inflected barred
  form. The desk should note 4:56 on the record so the seat is a
  decision, not an accident.

## 5. Script and orthography — FAIL (see §8.4 and §8.6)

The book is Cyrillic in the Russian 33-letter norm as specified,
with no Latin-script passages and no Arabic script. Two
contamination classes fail it:

- **Mixed-script tokens: 13 distinct, 21 occurrences** — Cyrillic
  stems with Latin transliteration tails fused on, no hyphen:
  Азороze ×5 (3:51, 40:28, 42:10, 43:64, 43:88), азороze ×5
  (7:29, 7:33, 7:143, 7:151, 7:155), кучфоze (43:46), пилесna
  (7:179), сундукc (20:39), пингonte (26:155), алянoke (28:23),
  тевnte (28:55), отвечade (28:65), Шкайноke and Шкайnte (29:46),
  идолnte (30:40), videста (54:49 — the Moksha word виде itself
  spelled in Latin letters). These are the substance behind the
  disclosure's "13 retained-Latin candidates": they are not
  retained names, they are possessive/derivational endings
  (-зе, -на, -с, -онте, -оке, -нте, -аде, -ке, -ста) typed in
  Latin. Every one converts mechanically to its Cyrillic shape.
- **кең at 47:25** — the word кең "wide" carries ң (U+04A3),
  a letter of the Kazakh/Kyrgyz alphabets that is not in the
  Moksha 33-letter norm. One token, one seat; mechanical fix
  (кенг/кенде shape per the inventory's spelling).

Legitimate Latin, settled pass: personal names and scripture
titles in the Master's forms per the names policy (149 distinct
Latin tokens, 1,127 occurrences — Moses 136, Pharaoh 74,
Abraham 69, Quran 68, and the disjointed-letter names), including
hyphenated master forms al-Lat, al-Uzza (53:19) and at-Tariq
(86:1–2). Two retentions are reservations, not passes (§9.5):
manna standing in Latin at 2:57, 7:160, 20:80, and Bedouin-тнень
at 33:20 — common nouns, not names, left untranslated while the
book translates their neighbours.

## 6. Core-term consistency — PASS, with the disclosed collapse reserved

Recomputed stem censuses: Шкай family ~3,009 tokens; Азор family
~1,150 (Lord); ангел 86 (angel); вайме 143 (spirit/soul — one
attested lemma carries both, disclosed in the audit); Ине Вайме
4 (Holy Spirit, all seats); озкс 65 against молитва 9 (both
glossary-seated prayer words; озкс dominant, no third form);
рай 33 (Paradise); ад family 40 (Hell); Судонь ши 16 exact
phrases, 19 судонь tokens in all cases (Judgment Day); виде ки
149 (straight path); берянь вайме 30 (devil); сатана 51;
озкс куд 8 (temple); книга 255; грех 186; пост 14.
Шкаень кучф stands 203 times and the кучф family 386 times, and
every master seat naming a prophet (75 seats) or a messenger
(318 seats) carries the кучф device — no seat drops the figure
or substitutes another word. The prophet/messenger distinction
itself is not carried: one device serves both, exactly as the
glossary and attestation audit disclose. That is a recorded
reservation (§9.3), not an inconsistency: the book does openly
and uniformly what its front matter says it does.

## 7. Clause-fidelity sample — 56 verses; two failures

Sample: a 30-verse number battery (2:196, 2:243, 2:259, 2:261,
4:11, 4:12, 5:89, 5:95, 8:65, 9:36, 11:7, 12:4, 12:43, 12:47,
18:22, 18:25, 21:47, 29:14, 34:46, 37:147, 39:6, 41:30, 46:15,
56:7, 70:4, 71:28, 74:30, 97:3, 9:122), long legal and long
verses read clause by clause (2:282 — the longest verse in the
book, tail verified clause-complete; 2:229, 2:233, 4:176, 5:6,
6:151, 9:60, 17:23, 24:2, 24:4, 24:31, 33:49, 65:1, 65:4), and
short controls (1:5, 2:188, 2:255, 3:18, 3:26, 14:34, 22:78,
31:14, 36:58, 40:60, 49:13, 55:26, 59:7, 99:7, 112:1, 114:1).
Word ratios on long verses run 0.80–1.15, the expected band for
an agglutinative target; no collapsed or pronoun-substituted
verse was found in the sample. Numbers verify at 28 of 30
battery seats, including the hard ones: 4:11–12 fractions
(two-thirds кафта колмоце пялькст, half, fourth нилеце), 5:89
ten/three, 9:36 twelve (кемгафтува)/four, 18:25 three hundred
(колма сят) adding nine, 37:147 a hundred thousand (сяда
тёжяненьди), 70:4 fifty thousand (вете кеменонь тёжянь),
46:15 thirty (колмогемонь) and forty (нильгемонь), 8:65
twenty/two hundred/a hundred/a thousand, 74:30 see §9.4.
The two failures are 4:23 and 29:14 (§8.3, §8.7).

## 8. FAILING FINDINGS — remediation list, most serious first

### 8.1 што / штоба — unattested conjunctions at scale (623 tokens)
Recomputed case-insensitively: што 348 tokens in 302 seats,
штоба 275 tokens in 219 seats (the crew's ~348/~275 figures are
exact). Neither form is a lemma in the build's own inventory
(`sources/mdf-lemmas.json`), neither is a Giella stem, and
neither appears in the kaikki harvest as a Moksha lemma.
BUILD-SPEC is explicit: "Every function word MUST be checked
against sources/mdf-lemmas.json before seating; an unchecked
function word does not seat." These two seat in roughly one
verse in ten, in the load-bearing "that / so that" positions.
Remediation: replace with attested devices seat by seat (кода,
сянь инкса-type phrasing, or the -ма nominalisations the spec
uses elsewhere); the replacement is systematic but not a blind
find-and-replace, because што covers both complementiser and
relative senses.

### 8.2 эли — expressly unseated by the spec, seated 127 times
Recomputed: эли 127 tokens in 109 seats (crew's ~127 exact).
эли is not in the inventory; али is, and BUILD-SPEC seats "or"
as али and states "эли is NOT seated". Remediation is mechanical
(эли → али), with a capitalisation pass at sentence heads.

### 8.3 4:23 — garbled clause and a literal ellipsis in the text
The Master's clause "the wives of your genetic sons" is rendered
«тинь виде цёраньк аляснон авалангс... и аватне:» — "your true
sons' fathers' wives... and the wives:" — which reverses the
kinship, trails into a literal "..." (the only ellipsis in the
book), and leaves a stray fragment («и аватне:») hanging before
the next clause. Batch B's own note flags this as its weakest
seat and recommends desk review; the review never landed. The
rest of 4:23's long kinship list is carried in full.
Remediation: re-render the one clause (the "genetic sons" sense
on attested stems, e.g. the шачф "born" phrasing the verse
already uses for stepdaughters), delete the ellipsis and the
stray fragment.

### 8.4 Mixed-script tokens — 13 distinct, 21 occurrences
Listed seat by seat at §5. A reader meets «Азороze» for "my
Lord" in five separate theophany speeches. Remediation is
mechanical: write the endings in Cyrillic (Азорозе, пилесна,
сундукс, видеста, and so on).

### 8.5 7:166 — apes silently seated against the book's own GAP practice
At 2:65 and 5:60 "apes" takes ⟦GAP: apes⟧; at 7:166 the same
word is silently rendered маймункс. маймун is not in the build's
inventory (checked: no lemma). Either ground attests it or the
seat takes the same GAP marker as its two sister seats; the
present state is the one silent-seating breach of the GAP law
found in the book. One seat.

### 8.6 47:25 — non-Moksha letter ң
кең, one token (§5). Mechanical fix.

### 8.7 29:14 — number error: fifty rendered as ninety
Master: Noah stayed "a thousand years minus fifty years."
Mdf: «тёжянь кизот вейхксагемонь кизода башка» — вейхксагемонь
is nine-tens, ninety (вейхкса 9 + гемонь tens; fifty is
ведьгемонь, which the book itself uses correctly at 70:4 in
expanded form). One seat; mechanical fix once seen.

### 8.8 иля / иляда — the spec-barred prohibitive, 117 tokens
Recomputed: иля 92 tokens, иляда 25 tokens, in surahs 2 (36),
3 (19), 11, 12, 14, 15, 16 — wider than batch D alone. BUILD-SPEC
states "иля + imperative is Erzya-shaped and NOT seated" and
prescribes аф + 2pl present for command negation; иля is not in
the inventory. Batch D's notes disclose the deviation honestly
and state it "converts mechanically if barred" — it is barred,
by the spec's own words. Remediation: the mechanical conversion
the batch itself describes.

### 8.9 мельга — unattested follow-postposition, 48 word tokens
Recomputed: мельга 48 whole tokens (74 substring occurrences
including мельганза-type forms, 67 seats). The companion item
settles the other half: **мельге IS attested** — it stands in
the Giella stem XML as a postposition lemma (`<l pos="Po">мельге
</l>`) and in `mdf-lemmas.json`; batch H's note is correct, and
мельге seats (79 whole tokens) PASS. мельга as a bare form is
not a lemma in either source. Follow-seat census over the
Master's 158 "follow" seats: 77 ride мельг- forms, 49 ride the
spec's молемс … кинц эзга path device, 32 ride other attested
restructures (spot-read, legitimate). Remediation: regularise
the мельга seats onto the мельге paradigm or the spec device,
seat by seat.

## 9. Open items settled as PASS or recorded reservation

1. **канд- forms (7:106, 9:92, 10:24) — PASS.** The batches
   feared кандомс was unseated; it is in fact a Giella verb
   lemma (`<l pos="V" val="TV">кандомс</l>`) and in
   `mdf-lemmas.json`. The spec's "NOT seated" caution is
   superseded by the inventory evidence. The канд- family
   (298 substring tokens: кандть, кандомс, канды, кандозь…)
   is regular paradigm on an attested stem.
2. **казнефт (34:35, 37:59) — PASS.** See §4.
3. **Prophet/messenger collapse — recorded reservation.**
   Disclosed in the glossary and audit; uniform in practice
   (§6). A reader cannot tell a prophet seat from a messenger
   seat in Moksha. The desk accepted this device at build time;
   it is recorded here so the landing decision is made with it
   in view.
4. **74:30 "Nineteen" — recorded reservation.** Rendered
   «вейхкса кемонь» ("nine ten"), where the book's own teen
   pattern at 12:4 is unit-fused onto ten (кемфкие, eleven).
   The reversed order reads ambiguously beside вейхксагемонь
   (ninety) at 29:14. One seat; a native or dictionary check
   should settle the teen formation before landing.
5. **manna (2:57, 7:160, 20:80) and Bedouin-тнень (33:20) —
   recorded reservation.** Common nouns left in Latin while the
   book translates elsewhere; manna is the Master's own word
   carried over, Bedouin is a Latin stem with a Moksha plural
   suffix hyphenated on. Minor; regularise or disclose.
6. **кда — recorded reservation (the largest single reservation
   in the book).** Recomputed: 865 whole tokens in 415+ seats
   (crew's ~865 exact). кда is not in the inventory. Unlike
   што/эли/иля, кда was seated by BUILD-SPEC's own
   relative-clause note ("else кда/кие phrasing, logged"), so
   the batches followed their orders; the gap is between the
   spec and the inventory, not between the builders and the
   spec. It cannot be passed silently: before landing, the desk
   needs either corroboration of кда from a fuller Moksha
   source than the harvested inventory, or a ruling accepting
   it as a seated function word on the record. If it were
   barred, the remediation would be the largest in the book —
   that is why it is a reservation for a ruling, not a finding
   against the builders.
7. **Minor typographic reservations.** (a) One net unclosed
   guillemet: 21:56 opens a « that is never closed (21:66 opens
   a second, 21:67 closes one; book totals « 232 / » 231), and
   the « » quote system used by some batches sits alongside the
   “ ” system used elsewhere — the Master's own curly quotes
   are themselves unbalanced (1,848/1,817), so the “ ” imbalance
   (1,615/1,612) is largely inherited and is not counted against
   the build. (b) Nine store seats carry a trailing space (92:5,
   92:6, 92:8, 92:9, 101:6, 101:8, 102:5, 110:1, 110:2) — the
   only txt/store differences in the book; cosmetic. (c) сынь
   "they" stands 265 times against the spec's pronoun table
   form синь (4,819) — a variant the decomposition screen
   cannot trace; regularise or record. (d) ингели (136 tokens)
   beside the spec's инголе — same class, minor.

## 10. Purple untraced adjudication

The build's screen figures reproduce exactly under re-run:
9,923 distinct Cyrillic tokens, 4,955 untraced candidates
(21,104 occurrences; 2,770 of the distinct candidates are
hapax). Adjudication of the candidate list, by the checker's own
tokenisation (which agrees with the screen on every top item):

- **Paradigm tail — not defects.** The largest single family is
  the азомс "say" paradigm the short-stem decomposition cannot
  resolve: азсь 492, азьк 338, азыхть 318, азсть 273, азы 91,
  азсы 85, азтада 72, азыихть 71 (≈1,740 occurrences on an
  attested stem). The same holds for definite/possessive chains
  (менельхнень 146, тевснон 86, кемихнень 64, лангозост 63),
  compounds (мезевок 155, фкявок 62), шиня 159 (ши paradigm),
  dative variants (тинди 194 beside тиньди 118), and the
  нь/нди fragments (143/105) split off hyphenated name suffixes.
  This is the expected tail of an agglutinative language against
  a lemma list, and it matches the disclosure's own description.
- **Genuine unattested residue — exactly the items settled
  above, no hidden mass.** кда 865 (reservation, §9.6), што 348
  and штоба 275 (§8.1), эли 127 (§8.2), сынь 265 (§9.7c),
  маймункс 1 (§8.5). иля does not appear in the candidate list
  because the screen's glossary harvest traces it — the bar on
  иля is the spec's, not the screen's, and §8.8 rests on the
  spec and the inventory, not on Purple.
- No other high-frequency untraced token survives inspection as
  a candidate invention. The candidate list is adjudicated:
  Purple raises no finding beyond §§8–9.

## Summary for the landing decision

Do not land in the present state. The remediation is bounded:
four function-word regularisations (што/штоба by device,
эли → али, иля/иляда → аф + 2pl, мельга → мельге paradigm),
21 mixed-script tokens and one stray letter respelled in
Cyrillic, one clause re-rendered (4:23), one number corrected
(29:14), one GAP marker restored (7:166) — plus three rulings
or records for the desk: кда (§9.6), the 74:30 teen form
(§9.4), and the 4:56 кедь skin seat (§4). Everything else the
crew reported — 6,236/6,236 verses, exact seat-set equality,
a clean 114-surah grid, the Basmalah exactly as fixed with
surah 9 bare and surah 1 carrying it as verse 1, the GAP census
of 57 seats / 67 markers with no silent seating of any standing
term except 7:166, and zero whole-token Erzya-bar seats — is
verified as stated, with the crew's approximate figures
(~348/~275/~127/~865) confirmed exact on a case-insensitive
recount.
