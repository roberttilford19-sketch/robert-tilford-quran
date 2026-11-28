# Komi-Zyrian (kpv) Quran draft — INDEPENDENT CHECKER REPORT (2026-11-28)

Checker stance: this checker built none of the text under review.
Every figure below was recomputed at the desk with this checker's
own scripts from the files of record: `verses-store.json`,
`quran-kpv.json`, `quran-kpv.txt`,
`ayah-companion-manuscript-KPV.md`, `master-verses.json` (the
Locked English Master seat-set), `BUILD-SPEC.md`, `glossary.md`,
`ATTESTATION-AUDIT-2026-11-28.md`,
`FLAGS-AND-GAPS-DISCLOSURE-KPV-2026-11-28.md`,
`LICENCES-RECORDED-2026-11-28.md`, and the harvested inventories
in `sources/`. Nothing was edited, landed, shelved, committed, or
pushed by this check. Sibling standards applied: the landed
Erzya, Udmurt, Moksha, and Meadow Mari lanes and their checker
reports, recomputed from their own stores at this desk (Udmurt
1,732 GAP seats / 2,430 markers / 4,504 clean verses; Meadow Mari
298 / 339 / 5,938; Moksha 58 / 68 / 6,178; Erzya 56 / 70 / 6,180).

## Verdict (stated first; ground and consequence in §10)

**FAIL — with the GAP-tier ruling given separately in §9 as
PASS-WITH-GAP-TIER-RESERVATION.** The book's skeleton is exact:
every mechanical headline figure the build reports is verified
to the digit (§§1–3). The FAIL rests on §4: the built text
silently retains English in at least 484 proven tokens (219
types, 438 seats) — and, on the wider count, roughly a thousand
further capitalised epithet and term retentions including
*Hereafter* ×101 — where the build's own disclosure claims
retained-Latin candidates other than Master names number **0**.
A book whose face claims zero silent English retention while
carrying this mass of it does not pass, however exact its
counts are. Every failing item is bounded and remediable by a
retention-to-GAP/seat repair pass; none requires a rebuild.

## 1. Recount, seat-set, per-surah grid — PASS, exact

- Store seats 6,236; Master seats 6,236; `quran-kpv.json` seats
  6,236. Seat sets exactly equal in both directions (no seat in
  either set missing from the other). Store texts and
  `quran-kpv.json` texts are identical, seat for seat.
- Per-surah grid: every one of the 114 surah counts in both the
  store and the Master matches the standard grid exactly
  (7, 286, 200, 176, 120, 165, 206, 75, … 6; grid sum 6,236).
  Mismatches: NONE.
- Empty seats: NONE. The string "redacted": NONE in the store,
  in `quran-kpv.txt`, or in the manuscript. The build's
  6,236/6,236 claim is verified in full.

## 2. Basmalah — PASS (the build's "113" is correct, and here is the ground)

The seated form is fixed by BUILD-SPEC as
**Енлӧн нимӧн, Милӧсьт, Милӧсьт.** This checker's own counts:

- Store seat 1:1 equals the fixed form, character for character.
  The full Basmalah string occurs exactly **once** inside the
  verse store — at 1:1 and nowhere else. There is no duplicated
  Basmalah embedded in any verse seat (the defect that failed
  Meadow Mari's §2, where the string occurred 117 times in the
  manuscript, is absent here).
- In `quran-kpv.txt`: the string occurs **113 times** — 112
  standalone unnumbered lines plus the numbered verse 1:1.
  Counted surah by surah: exactly one standalone line in every
  surah except surah 1 (zero standalone; its Basmalah is verse
  1:1) and surah 9 (zero, correctly). Anomalies: NONE.
- In the companion manuscript
  `ayah-companion-manuscript-KPV.md`: identically 113 — 112
  standalone lines with the same per-surah distribution, plus
  numbered 1:1.

Ruling on the build's figure: **113 in `quran-kpv.txt` is
correct and matches the sibling pattern exactly** (Udmurt
re-check: 112 standalone lines, surah 9 zero, plus 1:1; Moksha:
112 standalone lines). The count is not an error and not a
duplication. One related seat is reserved, not failed, here and
failed under §4/§8: at 27:30 the Master's in-verse Basmalah
("In the Name of God, the Beneficent, the Merciful") is rendered
only in part — "ын ним Ен, Beneficent, милӧсьта" — with the first
mercy name retained in English (see §4).

## 3. GAP census — figures PASS, exact to the digit

Recomputed from the store, independent of `verify.py`:

- GAP seats: **4,870**. GAP markers: **12,899**. Verses rendered
  without a marker: **1,366**. Distinct GAP terms: **4,183**.
  Every figure in the disclosure is verified exactly, including
  the top terms (painful ×66, wronged ×39, destroyed ×34,
  disbelief ×29, bounty ×28, beyond ×27, sincere ×26,
  provision ×26, ancients ×26, settled ×25).
- Marker distribution per verse: 0 markers 1,366 verses;
  1 marker 1,645; 2 markers 1,330; 3 markers 808; 4 markers 437;
  5 markers 238; 6 markers 159; 7 markers 106; then a long tail
  to one verse carrying 39 markers. Mean 2.65 markers per
  GAP-bearing verse; 78.1% of all verses carry at least one
  marker. Bracket integrity: 12,899 opening ⟦ and 12,899
  closing ⟧, no malformed seat.
- The manuscript's marker count is 12,900 — exactly one more
  than the text's 12,899; the extra marker is the explanatory
  example "⟦GAP: …⟧" in the front matter, not a verse marker.
  Not a discrepancy.
- GAP practice in the narrow sense — gaps held open, visibly
  marked, terms logged — is honest as far as the markers go.
  The exception is §4: a second, invisible tier of unrendered
  vocabulary exists beside the GAP tier, retained in English
  with no marker at all. The GAP-tier ruling itself is §9.

## 4. Script purity and retained Latin — FAIL (the build's "0" does not hold)

The disclosure claims: mixed-script tokens NONE; retained-Latin
candidates other than Master names **0**. This checker's own
census (GAP-marker interiors excluded throughout):

- Distinct Cyrillic tokens (lowercased): **1,000** — verified,
  as reported. Tokens containing ӧ: **475** — verified. Tokens
  containing і: **13** — verified. Occurrences: ӧ/Ӧ 67,045
  characters; і/І 8,259 characters. The Komi letters are
  genuinely and heavily used, not normalised away.
- Mixed-script tokens: not NONE. Exactly **6** tokens join a
  Latin Master name directly to the Cyrillic genitive suffix
  with no separator: Adamлӧн (5:27), Pharaohлӧн (7:127, 40:28,
  40:37), Abrahamлӧн (11:74), Josephлӧн (12:58). These are the
  disclosed genitive-on-names device (glossary: "Adamлӧн") at
  work, so they are recorded as a disclosed device, not a
  corruption — but the disclosure's flat "NONE" is inaccurate
  on its own terms, and the sibling practice (Erzya) writes
  such forms across a hyphen. Minor; correct the claim or the
  forms at remediation.
- Retained Latin overall: **470 distinct types, 1,945 tokens**
  in the verse text. Genuine carried names, scripture titles,
  and the disjointed letters account for much of this and are
  legitimate under the names policy (Moses ×136, Pharaoh ×74,
  Abraham ×69, Quran ×68, Israel ×43, Noah ×43, Mary ×34,
  Joseph ×27, Thamood ×26, Adam ×25, Jesus ×25, Aad ×24,
  Aaron ×20, Torah ×18, Isaac ×17, Solomon ×16, Jacob ×16,
  David ×16, Ishmael ×12, Gospel ×12, Messiah ×9, Psalms ×5,
  Muhammad ×4, the letters Alif/Lam/Meem/Ha/Ra, and the like).
  The failure is the remainder, in two proven classes:

  **Class A/B — proven non-name retention: 219 types, 484
  tokens, 438 seats.** A retained type belongs to this class
  if its lowercase form occurs lowercase in the Master, or —
  the sharper test — the same word is GAP-marked in lowercase
  elsewhere in this same book. A word cannot be an unseatable
  GAP in one seat and a carried "name" in the next. Examples,
  each verified at its seats: Capable ×15 (3:26: "тэ лоӧ
  Capable став торяс" — while "sovereignty" in the same verse
  is GAP-marked twice and "Owner Sovereignty" is retained
  whole), Blaze ×15 (4:10), Compassionate ×11 (55:1, the whole
  verse, is the single English word "Compassionate."),
  Mount ×10, Clement ×10, Knowledgeable ×9, Ark ×9 (2:248),
  Bliss ×9, Desert ×9 (9:90: "Desert - Arabs" split and
  retained), Trumpet ×9, Sublime ×8, Cognizant ×8,
  Guardian ×7, Monotheist ×6, Appreciative ×6, Sufficient ×6,
  Presence ×6, Supreme ×6, Invisible ×6, Exalted ×6,
  Criterion ×5 (2:53), Repentance ×5, Thereupon ×5, Blast ×5.

  **Class C — capitalised-only epithets and terms: at least
  300 further tokens.** These never occur lowercase in the
  Master because the Master always capitalises them; the
  build's screen therefore classified every one as a "name."
  They are not personal names or scripture titles under
  BUILD-SPEC's own names policy. The largest: **Hereafter
  ×101** — a core theological term retained in English in 101
  seats, never translated, never GAP-marked (2:4 and passim);
  Beneficent ×19; Hearer ×16; Forgiver ×16; Praiseworthy ×11;
  Expert ×9; Omniscient ×8; Observant ×8; Reality ×7;
  Omnipotent ×7; Independent ×6; Inferno ×6; Eden ×6;
  Majestic ×6; Maker ×5; Originator ×5; Giver ×5;
  Pardoning ×5; Glorious ×5; Forbearing ×4; Benevolent ×2
  (2:163: "Benevolent, Compassionate." — the verse's two divine
  names both retained); Owner ×2. The glossary itself supplies
  devices for this family (кывзысь "the Listener", тӧдысь "the
  Knower", став вына "the Almighty", дзик ӧти "the Absolute"),
  which makes the retention an inconsistency as well as a
  silence: at 2:127 "Hearer" is retained in English in the same
  breath as тӧдысь renders "the Knower."

  **Seat 1:3 fails the spec outright.** BUILD-SPEC fixes 1:3 as
  the Basmalah's two mercy names without the frame:
  "Милӧсьт, Милӧсьт." The store reads **"Beneficent,
  милӧсьта."** — the first mercy name retained in English in
  the book's third verse, against the spec's explicit seating
  and against 1:1's own practice.

  Why the build's screen missed all of this: `verify.py`
  constructs its name whitelist as every capitalised word-form
  occurring anywhere in the Master — sentence-initial common
  words included — so any capitalised English word the engine
  retained was whitelisted by construction. The screen's "0"
  is an artefact of that definition, not a measurement. Under
  the spec's actual names policy (personal names and scripture
  titles, carried unaltered), the retention mass above is
  silently seated English: not Komi, not a disclosed device,
  not a GAP. That is the one fault the house GAP law exists to
  prevent, and it is why this check fails despite §§1–3.

  Two smaller retentions ride here: "Scriputure" ×1 — the
  Master's own misspelling, carried unaltered into the Komi
  text; and "Salomon" ×1 beside Solomon ×16.

## 5. Batch census against the batch files — PASS, exact

Each `work/batch-<X>.json` was recounted independently and
compared with the disclosure's per-batch census, and each batch
file was compared seat by seat with the store. All thirteen
batches match on both counts — A 415/1,434 · B 412/1,511 ·
C 463/1,499 · D 475/1,277 · E 362/944 · F 355/957 · G 389/878 ·
H 350/916 · I 428/1,025 · J 336/770 · K 398/981 · L 374/545 ·
M 113/162 (GAP seats / markers) — batch totals reconcile to the
book totals 4,870 / 12,899, and every batch text is identical
to its store seats. One internal inconsistency in the lane's
own paperwork, minor: the attestation audit says 25 dictionary
entries were dropped at verification; `work/unverified-dict.json`
holds **26** entries, which is the figure the disclosure uses.
The audit's "25" should be corrected to 26 in the record. The
disclosure's "1,314 seated dictionary entries" could not be
reconciled exactly from the dictionary files' mixed formats at
this desk (973 quoted keys in `dict_core.py` plus 272 in
`dict_nouns.py`, the verb file in another format) and is
recorded as a candidate figure, not verified and not disputed.

## 6. Purple sweep — candidates only; adjudicated PASS

The build's `verify.py` was re-run and reproduces its printed
result exactly (4 untraced candidates). This checker then ran a
fresh, independently written attestation screen over the same
inventories (GiellaLT lemmas, kaikki headwords, kaikki declined
forms, glossary lemmas, regular-ending decomposition). It
returns 12 candidates — the build's 4 plus 8 the build's screen
absorbs through its hand-added function-word list. All 12
adjudicate as disclosed paradigm or function forms, not
unattested seats:

- локтӧ ×441 — disclosed irregular present of локны "come";
  stem локны verified in the GiellaLT inventory at this desk.
- кулӧ ×56 — disclosed irregular present of кувны "die"; stem
  verified in GiellaLT.
- юяс ×52 — regular plural -яс of ю "river"; stem verified in
  GiellaLT and kaikki.
- лӧн ×6 — the genitive suffix split by tokenisation from
  carried names (see §4 on the 6 name+лӧн tokens).
- ысь ×1,125, кӧст ×140, тӧг ×67, сянь ×11 — glossary function
  words (elative/postposition seats), seated in glossary §C.
- нином ×136 — glossary pronoun seat ("nothing").
- эскысьяс ×92 — regular agent plural of эскыны "believe".
- синтом ×32 — regular privative -тӧм on син "eye" ("blind").
- терпитысь ×30 — regular agent -ысь on терпитны "endure".

No unattested Cyrillic seat was found anywhere in the book.
The Komi-Permyak fence holds on the Cyrillic side: every
Cyrillic token traces to a kpv inventory lemma, a glossary
lemma, or a disclosed regular derivation of one. The fence's
failure is not Permyak — it is the Latin side of §4, which a
Cyrillic-only screen cannot see by construction. (The same
construction flaw makes `verify.py`'s "mixed-script tokens:
NONE" vacuous: its token counter is built from a Cyrillic-only
regex, so no token it examines can contain Latin. This
checker's whitespace-token method found the 6 tokens of §4.)

## 7. Dictionary attestation spot-checks — PASS

110 seated lemmas sampled across the glossary's core, people,
faith, verb, and number families were looked up directly in
the harvested inventories at this desk (fact and citation
only). **All 110 were found** — in the GiellaLT lemma inventory,
in kaikki headwords, or in kaikki declined forms. The core
religious seats verify with their glosses: ен (GiellaLT,
Finnish "Jumala"), мезӧс ("Herra"), ним ("nimi"), милӧсьт
("armo" — mercy/grace; the single-stem Basmalah seating rests
on a genuinely attested mercy word), небӧг ("kirja"), енэж
("taivas"), рай ("paratiisi"), ад ("helvetti"), ангел
("enkeli"), пророк ("profeetta"), ыстыны ("lähettää"), кыв
("kieli"), югыд ("kirkas"), му, ва ("vesi"), би ("tuli"),
шонді ("aurinko"), тӧлысь ("kuu"), кодзув ("tähti"), морт
("ihminen"), ань, мам ("äiti"), сьӧлӧм ("sydän"), эскыны
("uskoa"), прӧща ("anteeksianto"), кӧсйысьӧм ("lupaus"),
вын ("voima"), жертва ("uhri"), свидетель ("todistaja"),
восьтыны ("avata"), дорйыны ("puolustaa"), гижӧд ("teksti" —
the flagged generic scripture seat is honestly flagged: the
lemma means "text/writing"), and the full number row
ӧти…сюрс. The two flagged thin seats verify exactly as
flagged: джинн stands in the GiellaLT inventory with **no
gloss carried** — as the audit discloses; радейтны stands with
the gloss "pitää huolta" (to take care of) — lemma-attested,
gloss-thin for "love", as flagged. Both halves of the split
seats of §8 also attest (идӧг, GiellaLT "enkeli"; гӧнец,
kaikki headword): the splits are consistency failures, not
attestation failures. Inventory sizes verify as recorded:
GiellaLT 193,665 lemmas; kaikki 1,006 parsed headwords;
29,484 declined forms.

## 8. Core-term consistency and clause fidelity

### 8.1 Core-term splits — FAIL (consistency, not attestation)

The glossary carries two dictionary chunks — the desk core
(§§C–F) and the crew-curated chunk (§§G–H) — and the engine
seated both, so five core terms ride two competing Komi seats
across the book, with no rule a reader can infer:

- **angel**: ангел ×11 tokens (10 seats) beside идӧг ×75
  (75 seats; e.g. 2:30, 2:34, 4:97 all идӧгяс). Glossary §A
  seats ангел; §G seats идӧг. The disclosure's flagged-loan
  list names ангел only.
- **messenger**: ыстысь ×226 tokens (205 seats) beside гӧнец
  ×121 (113 seats) — at 2:87 both seats occur in one verse.
  §A's disclosed device is ыстысь; §G's seat is гӧнец.
- **believe / believer**: эск- stems ×1,061 beside верит-
  stems ×169.
- **sin**: мыж- ×344 beside грек ×90.
- **prayer**: кевмӧм ×55 beside буркыв ×32.
- Lesser splits of the same kind: sea море ×31 / саридз ×4;
  mountain керӧс ×5 / гӧра ×36; temple-or-mosque seats ride
  мечеть ×20 while §A's temple seat храм occurs ×1 (the same
  mosque-application question Meadow Mari's checker carved
  out; here it is recorded as a reservation, since both forms
  are inventory loans and the Master's own wording varies).

This is the Udmurt check-5 disease in a milder form (there,
"messenger" rode three seats). It does not hide anything —
both forms are attested — but a landed draft's core terms must
ride one seat each, or a stated rule for the split.

### 8.2 Standing GAP families not held — FAIL (rides with §4)

The attestation audit names Sabbath and pilgrimage as standing
GAP families. In the built text neither is GAP-marked:
**Sabbath is retained in English at all seven tokens** (2:65,
4:47, 4:154, 7:163 ×3, 16:124), and **Hajj is retained ×7**
(2:189, 2:196, 2:197 ×3) with **Umrah ×3** beside it (2:196).
The Udmurt lane GAP-marked both families at every seat,
"Hajj" included. At 4:47 and 9:90 the retention splits a
compound across a hyphen ("Sabbath - жуглӧ" for
"Sabbath-breakers"; "Desert - Arabs"), which is the retention
device at its most visible. These seats belong to §4's repair:
seat an attested form, apply a disclosed device, or GAP-mark —
but do not retain.

### 8.3 Clause-fidelity sample — PASS, with the §4 seats carved out

Twenty verses sampled across the book's length (1:5–7, 2:255,
3:26, 4:97, 5:3, 7:142, 12:4, 18:25, 19:62, 24:35, 27:30,
30:21, 36:58, 39:7, 48:8, 99:1, 112:1–4, and the number
battery below) were read clause by clause against the Master.
Within the engine's disclosed plain style, clauses are carried
— by a Komi seat, a disclosed device, or a GAP marker — with
no dropped clause found in the sample and negations carried
by оз throughout. The two "<redacted>" seats are rendered for
their surrounding sense exactly as the spec directs (39:7,
48:8), and the string never appears.

- **Number battery — PASS in full.** Every tested number is
  right: three hundred years adding **nine** (ӧкмыс) at 18:25
  — the very seat the Udmurt draft failed with "six"; thirty
  nights completed with ten to forty at 7:142; eleven at 12:4;
  ninety-nine and one at 38:23; nine signs at 17:101; seven
  nights and eight days at 69:7; four months and ten days at
  2:234; seven pathways at 23:17; ten chapters at 11:13.
- Carved out of the pass, all of §4's class: 55:1, whose whole
  verse is the retained English word "Compassionate."; 2:163,
  both divine names retained; 2:255, "Sustainer" retained;
  38:23, "Entrust" retained inside the quotation; 31:27,
  "Majestic" retained — while the same word is rendered
  elsewhere and "cognizant" is GAP-marked at 24:35 yet
  retained as "Cognizant" at eight other seats. The sample's
  fidelity failures are the retention system's, not the
  clause system's.
- One lexical reservation from the sample, recorded as a
  candidate for remediation, not a fail ground: пышйӧ (the
  present of пышйыны, "flee") is correctly seated at fleeing
  seats (51:50, 62:8, 80:34) but is also seated where the
  Master says "reflect / ponder / take heed" (3:191, 30:21,
  51:49) — at 30:21 "people who reflect" reads "people who
  flee". One verb family, a handful of seats; a dictionary
  correction, not a structural fault.

### 8.4 Book face and licences — PASS by the sibling pattern

The companion manuscript carries its honest status on its
face: DRAFT — NOT PUBLISHED (twice), the build tier stated as
a first-pass draft, the GAP census stated in the front matter
with the same figures this check verified (1,366 / 4,870 /
12,899), the single-stem Basmalah disclosed, the unverified
2023 complete-Bible record disclosed with no complete-Bible
claim made, and no first-translation claim anywhere. The bare
`quran-kpv.txt` carries no front matter — which matches the
landed Erzya, Moksha, and Meadow Mari texts exactly (their
`.txt` files likewise open at surah 1); it is not held against
this lane. Licences verify as recorded: GiellaLT giella-kpv
LGPL v3, Wiktionary/kaikki CC BY-SA, the Bible controls and
the Lytkin tradition cited by fact only, the Locked English
Master as build base. One gap in the face's honesty is §4's:
the front matter's claim that every unrendered word carries
the GAP marker is not true of the retained-English tier, and
the face must be corrected with the text at remediation.

## 9. SPECIAL RULING — the GAP tier

**Ruling: PASS-WITH-GAP-TIER-RESERVATION.**

Ground, stated in one breath with the figures: the GAP tier
itself — 4,870 of 6,236 seats (78.1%) carrying 12,899 visible
markers, 1,366 verses clean — breaks no house rule. The house
GAP practice has never set a numerical ceiling: it requires
that a seat with no attested form be held open visibly, that
no form be invented or silently borrowed, and that the census
be disclosed on the book's face. On the GAP tier's own ground
all three hold here — the markers are really there (§3,
verified to the digit, batch by batch), the attestation
screen finds no invented Cyrillic form anywhere (§§6–7), and
the census stands on the book's face in the same figures this
check recomputed (§8.4). The comparison with Udmurt (1,732
GAP seats, 27.8% of verses) measures a difference of degree —
2.8× the seats, 5.3× the markers — produced by a disclosed
difference of kind: Udmurt was hand-built over a larger seated
dictionary; this draft is a first-pass engine render over a
1,314-entry verified dictionary, and its build tier is stated
plainly on its face. A heavier honest GAP tier is not a
dishonest book. **A GAP-reduction pass is therefore NOT
required before landing as DRAFT — NOT PUBLISHED.**

The reservation, which is a real condition and not a courtesy:
the reservation attaches to what the GAP census does not
cover. This book may land on the strength of its GAP honesty
only when the text contains no second, invisible tier of
unrendered vocabulary beside the GAP tier. At present it does
(§4, §8.2). The consequence of each ruling, spelled out:

- **PASS** (not given) would have meant: land as-is under the
  Pipeline Landing Authorization. Withheld, because §§4/8
  fail independently of the GAP tier.
- **FAIL on the GAP tier** (not given) would have meant: a
  GAP-reduction pass — enlarging the seated dictionary and
  re-rendering — must precede any landing, however honest the
  markers. Withheld, because no house rule sets a GAP ceiling
  and the tier's honesty is verified, not merely claimed.
- **PASS-WITH-GAP-TIER-RESERVATION** (given) means: the GAP
  mass itself is landable as DRAFT — NOT PUBLISHED once the
  §10 remediation is done and re-checked; no GAP-reduction
  pass is required, and none should be substituted for the
  §10 repair. The reservation must ride with the book's
  record: this is the GAP-heaviest draft the desk has
  produced, its clean-verse share (21.9%) is a third of
  Udmurt's (72.2%), and any future claim about the book must
  carry the census with it, in the same breath.

## 10. Verdict and remediation

**Overall verdict: FAIL** — on §4 (retained Latin: at least
484 proven non-name tokens in 438 seats, plus the
capitalised-only epithet tier headed by Hereafter ×101, plus
seat 1:3 against the spec's explicit seating), §8.1
(core-term splits), and §8.2 (Sabbath/Hajj/Umrah retained
against the audit's own GAP families) — with §§1, 2, 3, 5, 6,
7, and 8.4 passing, several of them exactly, and the GAP tier
ruled landable under §9's reservation.

Remediation required before a re-check, in order:

1. **Close the retention tier.** Every retained English word
   that is not a personal name, a scripture title, or a
   disjointed letter must be seated on an attested Komi form,
   rendered by a disclosed glossary device, or GAP-marked —
   seat by seat, Classes A/B/C of §4 and §8.2's families
   included. Seat 1:3 takes the spec's form "Милӧсьт,
   Милӧсьт." The Basmalah at 27:30 is completed on the same
   seating as 1:1.
2. **Fix the screen, not just the text.** `verify.py`'s name
   whitelist (every capitalised Master word) and its
   Cyrillic-only mixed-script test must be rebuilt so both
   purity figures measure what the disclosure claims they
   measure; the corrected figures ride in the revised
   disclosure, and the disclosure's "retained-Latin: 0" and
   "mixed-script: NONE" claims are not re-issued until a
   screen that can see Latin returns them.
3. **Unify the split core seats** of §8.1 (angel, messenger,
   believe, sin, prayer at minimum) to one seat each or a
   stated rule, and correct the front matter's
   every-unrendered-word-is-GAP-marked sentence to match the
   repaired text.
4. Small record corrections in the same pass: the audit's
   dropped-entries figure 25 → 26; "Scriputure" and "Salomon"
   resolved with the retention repair; the пышйӧ
   reflect-family seats (§8.3) re-seated.

Nothing in this list requires a rebuild, a GAP-reduction
pass, or Robert's ruling: every item is a repair under the
standing gate law, of the same kind the sibling lanes'
remediations executed. After remediation, the lane needs a
fresh independent re-check PASS before landing, exactly as
its disclosure already states. This checker edited nothing,
landed nothing, and pushed nothing; the draft stands where
the build left it.

— Independent checker, 2026-11-28. All figures recomputed at
this desk from the files of record; instrument output treated
as candidates until adjudicated, per house practice.
