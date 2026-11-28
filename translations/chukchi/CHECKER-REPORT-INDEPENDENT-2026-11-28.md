# Chukchi (ckt) Quran lane — INDEPENDENT CHECKER REPORT (2026-11-28)

Checker: independent checker (did none of the build). Method: governing
documents read in full (BUILD-SPEC.md, PREBUILD-VERIFICATIONS.md,
ATTESTATION-AUDIT-2026-11-28.md, LICENCES-RECORDED-2026-11-28.md);
verify.py re-run firsthand; GAP census and codepoint counts recomputed
in the checker's own scripts; seat grounds verified firsthand against
the files in `sources/`; refusal list, norm fence, names allowlist and
fidelity checked seat by seat and verse by verse as specified. No build
file was edited. No git command was run.

## VERDICT: FAIL

Ground in one breath: the build is honest about its gaps (the GAP
markers are real, counted correctly, and the refusal list holds
perfectly), but it carries three correctness defects that a gap-tier
reservation cannot absorb — a FALSE seat (`even` → the Even-people
ethnonym ӄаарамкын, rendered 89 times), a letterform breach of ruling 2
(U+04A3 ң in the built text, 26 occurrences, in seats whose correct
U+04C8 ӈ twin exists in the same dictionary), and a names-policy breach
(1,889 English tokens retained in the text, including God-epithets the
BUILD-SPEC expressly forbids on the allowlist) — and its thinness is
beyond the sibling reservation: 6,209 of 6,236 verses (99.57%) carry
GAP markers, 66,690 markers in all (2.84× the Chuvash lane's 23,456),
5,691 distinct English terms are gapped against a 454-key dictionary
(439 usable keys; 15 are `/translations` junk keys that can never match
a Master word), and of the 27 fully seated verses about 22 are
disjointed-letter lists retained in Latin, not translations. Exact
remediation is named in §G.

---

## A. verify.py — re-run firsthand, line by line

Command: `python3 ~/workspace/ayah-chukchi/verify.py` — exit code 0.
All 21 checks PASS, exactly as the build claimed:

| # | Check | Result |
|---|---|---|
| 1 | seat-set equality (store vs Master) — store 6236, master 6236 | PASS |
| 2 | Master total 6236 | PASS |
| 3 | per-surah grid (114 surahs) — mismatches: [] | PASS |
| 4 | seat-set equality (json vs Master) | PASS |
| 5 | json text == store text | PASS |
| 6 | 1:1 Basmalah exact | PASS |
| 7 | 1:3 exact | PASS |
| 8 | 112 unnumbered Basmalah lines — found 112 | PASS |
| 9 | no empty verses | PASS |
| 10 | no 'redacted' string | PASS |
| 11 | no Latin placeholder text | PASS |
| 12 | GAP census reconciles — seats 6209, markers 66690, distinct 5691 | PASS |
| 13 | codepoint zero: U+052F hook-tail el — count 0 | PASS |
| 14 | codepoint zero: U+0027 ascii apostrophe — count 0 | PASS |
| 15 | codepoint zero: U+2019 right single quote — count 0 | PASS |
| 16 | codepoint present: ԓ U+0513 — 1825 | PASS |
| 17 | codepoint present: ӄ U+04C4 — 4306 | PASS |
| 18 | codepoint present: ӈ U+04C8 — 6758 | PASS |
| 19 | codepoint present: ʼ U+02BC — 838 | PASS |
| 20 | token attestation screen (0 untraced) — untraced: {} total 0 | PASS |
| 21 | retained-Latin screen (allowlist only) — off-allowlist: {} | PASS |

Final line: `GAP census: 6209 seats; 66690 markers; 5691 distinct terms`
/ `VERDICT: PASS`.

**Checker's independent recomputation (own script, from
verses-store.json):** GAP verses **6,209**; markers **66,690**; distinct
GAP terms **5,691**; fully seated verses **27** — all three figures
match the census file and verify.py exactly. Content-slot analysis
(checker's own): of 128,918 content slots, GAP markers are 66,690
(**51.7%**), seated Cyrillic tokens 60,339 (46.8%), retained Latin
tokens 1,889 (1.5%). 1,348 verses are ≥60% GAP by slots.

**Limits of verify.py the checker found:** (i) it does not test U+04A3
(ң) or U+2018 — both occur in the built text (see §D); (ii) its
attestation inventory hard-codes two additions (`inv.add("гымнин")`,
`inv.add("та")`) — та is the disclosed case device, but гымнин's ground
(fieldasr DATA.md) is not among the files in `sources/` and cannot be
verified from the lane folder; (iii) its retained-Latin screen is only
as strong as the allowlist, which is over-broad (§E) — the screen
passes trivially.

## B. Attestation adjudication — stratified sample of 64 seats

Sample composition: the 1 curated seat (god), all 3
`initial-digraph-converted` seats, all 18 `internal-digraph` seats, the
audit's curated religious seats, pronoun/function seats, and a spread
of en-pair, en-gloss and ru-gloss seats — 64 seats in total. Each ground
was checked firsthand in `sources/wikt-ckt-entries.json`,
`sources/wikt-en-ckt-pairs.json`, `sources/ruwikt-ckt-entries.json` /
`ruwikt-clean.json`, and `sources/ruwikt-examples.json` (IBT sentences).

**Tally: VERIFIED 56 / WEAK 7 / FALSE 1.**

### VERIFIED (56) — cited form present in the cited source with the cited gloss

god → Тэнантомгыӈэн (curated; the form stands in the IBT Luke 1:19
sentence quoted in ruwikt-examples.json: «Гым – Гавриилегым, чымче
ваԓьэгым Тэнантомгыӈына»); spirit → эӈэӈ (en entry, glosses
['spirit','God']); lord/master → этын (ru этын, gloss хозяин);
servant → выёльын (ru, gloss слуга); doubt → матэватгыргын (ru, gloss
сомнение); custom → вагыргын (ru, gloss обычай — seated for 'custom'
only, correctly NOT for 'life'); name → нынны (ru, gloss имя);
death → вайнʼыгыргын (ru headword вайн'ыгыргын, gloss смерть);
enmity → аʼкʼалтывагыргын (ru а'к'алтывагыргын, gloss вражда);
hatred → эʼкʼу лынʼгыргын (ru phrase, gloss ненависть);
gift → ӄэвийыръын (ru к'эвийыръын, gloss подарок; initial кʼ→ӄ per the
disclosed conversion rule); room → ӄэлгикʼэл (ru headword
к'элгик'эл, gloss комната — initial conversion + internal glottal,
both per rule); granddaughter → ӈавытлывэ (ru н'авытлывэ, gloss
внучка); always → амкʼынъычо (ru амк'ынъычо, gloss всегда);
beautiful → гытинʼыльын (ru, красивый); fog → йынʼапылмын (ru, туман);
tail → налгынʼойнʼын (ru, хвост); red → нычелгыкʼэн (ru headword
нычелгык’эн with U+2019, gloss красный — normalised to U+02BC per
rule); answer → очынʼатгыргын (ru, ответ); mushroom → пъонʼпъонʼ (ru,
гриб); fly → ринʼзмъетык (ru, летать); smile → рэмыннунʼык (ru,
улыбаться); laughter → таннʼыткогыргын (ru, смех); laugh →
тэннʼыткук (ru, смеяться); cold → чьэченʼкин (ru, холодный);
evening → вулкʼытвин (en pair 'evening'; also ru вечер);
scarlet → нычеллякʼэн (en pair 'scarlet'); thigh → аймалкʼыл (en pair
'thigh' — one of three paired forms, first-listed seated);
bear → кэйӈын (en 'brown bear'; ru медведь (бурый)); fish → ыннээн
(ru рыба); water → мимыԓ (en 'water, liquid'); moon → йъиԓгын (en
'moon, month'); child → нэнэны (en 'child'; ru ребёнок);
dog → ыттʼын (en 'dog'); heart → линлиӈ (en 'heart'; ru сердце);
fire → йынйын (ru огонь); earth → нутэнут (ru земля);
sea → аӈӄы (en 'sea'; ru море); river → вээм (ru река);
tree → уттуут (en 'tree'; ru дерево); star → аӈатԓыӈын (en 'star');
night → ныкирит (ru ночь); woman → ӈэвысӄэт (en pair
'woman/translations'); field → ергыер (ru ергыер, gloss поле — note:
the audit's neighbour list prints ергын, the dictionary's ергыер is
the attested headword; the audit line, not the seat, is the slip);
love → ыʼԓгу ԓыӈык (en entry, gloss 'to love'); address → нымытван
(en entry gloss 'address'; ru адрес); catch/take/receive/seize →
эймитык (en entry glosses exactly ['take','receive','catch','kill
reindeer (to eat)','seize'] — all four seats rest on the one attested
polyseme, disclosed here as verified); friend → тумгытум (en 'friend,
comrade, fellow, companion'); people/nation → варат (ru народ; en
pair 'nation'); chukchi → ԓыгъоравэтԓьан (en entry 'Chukchi, Chukchi
people'; en pair 'Chukchi'); alphabet → алфавит (en entry gloss
'alphabet' — a Russian loanword standing in the Chukchi entry itself;
form and gloss check, register noted in §D); we/us → мури (IBT Luke
5:5 sentence in ruwikt-examples.json uses мури as 'we' — verified
from the running text, the ru stub notwithstanding).

### WEAK (7) — form present, but the ground or the seat is compromised

| Seat | Problem |
|---|---|
| even → ӄаарамкын — **counted FALSE, see below** | — |
| horse → мури | The ru entry itself is garbled: headword мури is tagged POS 'pron' yet glossed лошадь, конь. The audit distrusts this same stub for the pronoun seats, yet the build seats it for 'horse'. Form+gloss are literally in the source, so not FALSE — but the seat rests on a source the build itself records as unreliable, and it makes 'horse' and 'we/us' homographs throughout the book. |
| holiday → праздник | The en pair list for 'holiday' offers three forms — праздник, эӈэӈыткун, крычмын. The build seated праздник, the plain Russian word, over two attested non-Russian alternatives, with no ground recorded for the choice. (Mitigation: the seat never fires — 'holiday' occurs 0 times in the built book.) |
| plant → тыңэчьын | The ru headword is spelled with **ң (U+04A3)**, not the ruling-2 letter ӈ (U+04C8), and the build seated that shape for the key 'plant' while its own twin key 'plant/translations' carries the correct тыӈэчьын. The built text uses the U+04A3 form 11 times and the correct form 0 times. See §D. |
| sun → Тиркытир | En pair cites the capitalised proper-name entry 'Sun'. The seat keeps the capital everywhere, so a common noun is capitalised mid-verse throughout (e.g. 7:54 «ынкъам Тиркытир ынкъам йъиԓгын»), against BUILD-SPEC's capitalisation rule (verse-initial and proper names only). The IBT Luke 23:44 sentence in the sources writes тиркытир lower-case. |
| my/mine → гымнин | Ground cites a fieldasr DATA.md lesson title («Гымнин нынны») that is **not in `sources/`** and cannot be verified firsthand from the lane folder; verify.py hard-codes the form into its inventory. Plausible and disclosed in the audit, but the ground is not checkable in-lane. |
| her/him/his/its/me → ытлён / гым | Ground is 'pronoun paradigm, case by context (spec)' — no per-seat checkable form; the flattening of all third-person cases to ытлён is a disclosed device, but as grounds these cite no form. (The base forms themselves are attested; the case assignments are not.) |

### FALSE (1)

| Seat | Finding |
|---|---|
| **even → ӄаарамкын** | The ground is `en.wikt translation pair 'Even'` — capital-E **Even**, the Even (Lamut) people, an ethnonym. The Master word seated is the adverb 'even'. The pair file confirms the entry is `{'en': 'Even', 'ckt': 'ӄаарамкын'}`. This is a homonym trap: the ethnonym is rendered wherever the Master says 'even' — **89 occurrences** in the built text (Master 'even' ×103). E.g. 24:35 «…illuminate, **ӄаарамкын** if no fire has touched it» and 2:44 «forget yourselves, **ӄаарамкын** though you read the Scripture» — a reader meets the Even-people word where the text means 'even'. A wrong word printed 89 times is not a gap; it is a mistranslation, and it is the single FALSE ground in the sample. |

No other sampled ground was fabricated: every other cited form was
found in its cited source. The dictionary's mechanical verification
largely did what it claimed — the failures are semantic (homonym,
garbled stub, variant choice), not invented forms.

**Dictionary-shape notes:** 454 keys include 15 `/translations` junk
keys (and/translations, bear/translations, …) that can never match a
Master token, so the usable dictionary is 439 keys / 402 distinct
seated forms. work/unverified-dict.json holds exactly one dropped seat
(polaris) — the drop mechanism worked.

## C. Refusal-list audit — PASS, complete

Checked every ruling-5 term plus the extended list (mercy, merciful,
beneficent, fasting, alms, pilgrimage, revelation, covenant, temple,
mosque, priest, law, judgment, paradise, hell) against
work/eng2ckt.json keys: **none is seated — zero exceptions.** No
near-key leakage either (no believ-, creat-, heaven-, sign-, truth-,
life-, book-, king-, pray-, merc-, soul-, sin- or law- keys of any
spelling). вагыргын seats 'custom' only; 'life' is GAP (129 markers),
exactly as the audit's refusal records. The agricultural list (sow,
sowing, seed, reap, reaping, harvest, garden, fruit, bread, sower) is
**entirely unseated**, and no agricultural near-key exists. The GAP
census confirms the refusal in the text itself: believe ×412 (+
believers 159, believed 100, disbelieve 133…), book ×121, truth ×181,
reward ×120, worship ×115, scripture ×115, signs ×112, hell ×93,
soul ×79, mercy ×140, merciful ×144 — all GAP, none silently seated.
This is the build's strongest suit.

## D. Norm fence — MIXED: dialect fence holds; letterform fence breached

- **Fenced sources:** no seat's ground cites Dunn, Chuklang, Salminen,
  Weinstein or GiellaLT; every ground traces to en/ru Wiktionary or the
  IBT sentences quoted inside ru.wiktionary. No Telqep, southern or
  Koryak form was found seated ('koryak' → танӈытан seats the *word*
  'Koryak' as an ethnonym gloss, which is a lexeme, not a Koryak form).
  PASS.
- **Men's/women's practice:** the letter ц occurs **0 times** in the
  seat dictionary and **0 times** in the built text (checker's own
  count, both cases). No ц-variant is seated. PASS.
- **Codepoint integrity (checker's own counts on the built text):**
  U+052F = **0**, U+0027 = **0**, U+2019 = **0** — ruling 2's three
  named zeros all hold. ԓ (U+0513) 1,825; ӄ (U+04C4) 4,306; ӈ (U+04C8)
  6,758; ʼ (U+02BC) 838.
- **BREACH — U+04A3 (ң): 26 occurrences in the built text**, from five
  seats whose ru.wiktionary headwords are spelled with ң instead of
  the ruling-2 letter ӈ: plant тыңэчьын (×11), rope танңыңэлгын (×7),
  winter льэлең (×1), rainbow йыңэттэтқымчучьын (×0 in text), hunter
  гынниңңыттыльын (×0 in text). Ruling 2 fixed Ӈ/ӈ as the modern single
  letters with "no silent normalisation between shapes"; ң is a
  different letter (the Kazakh/Kyrgyz-style eng), unattested as a
  Chukchi seat letter anywhere in the governing documents, and
  verify.py never tests for it. The sources' spelling was carried
  through silently — precisely what ruling 2 forbade. The correct twin
  тыӈэчьын already exists in the same dictionary under
  'plant/translations', proving the fix was available in-lane.
- **Minor:** one U+2018 (left single quote) inside a GAP marker at
  12:9 — ⟦GAP: father‘s⟧ — a Master possessive carried into the marker
  unnormalised. Cosmetic, inside a marker, but it is a fourth
  apostrophe shape in a book verified free of apostrophe variants.
- **Russian loanword seats:** праздник (holiday, never fires),
  интернет, округ, алфавит stand in the en.wiktionary Chukchi entries
  themselves, so they are attested-in-source; they are recorded here
  as register observations, not fence breaches — except that the
  build's own ru-side stoplist excluded exactly this class of Russian
  entries, and no equivalent screen was applied to the en-pair side.

## E. Names allowlist audit — FAIL against the BUILD-SPEC names policy

Sampled 25+ allowlist types against master-verses.json occurrences,
then audited the whole list and the retained-Latin tokens in the built
text (checker's own count: **244 distinct Latin types retained, 1,889
tokens**).

- Genuine names verified in the Master and correctly carried: Aaron,
  Abraham, Adam, Ahmad, Azar, David, Elijah, Elisha, Enoch, Ezekiel,
  Ezra, Gabriel, Goliath, Hud, Isaac, Ishmael, Jacob, Jesus, Job, John,
  Jonah, Joseph, Mary, Moses, Noah, Pharaoh, Saleh, Saul, Shuaib,
  Solomon, Zechariah, Luqman, Imran, Zaid — these are unobjectionable.
- **But roughly half the 248 types are not names at all.** The list
  carries God-epithets and common nouns/adjectives that BUILD-SPEC
  expressly bars from it ("Capitalised Master epithets are NOT names
  and never ride the allowlist… epithet phrases GAP or seat word by
  word like everything else"): Accepter, Acceptor, Avenger, Beholder,
  Benevolent, Bounteous, Conqueror, Crusher, Designer, Forgiver,
  Forgivers, Giver, Hearer, Knower, Observer, Omnipotent, Omnipresent,
  Omniscient, Originator, Pardoning, Perceiver, Praiseworthy, Producer,
  Provider, Redeemer, Relenting, Responsive, Reviver, Sender, Sovereign,
  Tempter, Vengeful, Victor, Wisest — and common nouns: Board, Books,
  Chamber, Chambers, Cataclysm, Catastrophe, Condemnation, Deluge,
  Easts, Wests, Elevations, Everybo
...[truncated 3075 chars]