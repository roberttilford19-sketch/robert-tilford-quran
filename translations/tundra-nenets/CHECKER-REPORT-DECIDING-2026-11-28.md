# Deciding RE-CHECK (round 2) — Tundra Nenets Quran draft (2026-11-28)

Checker: deciding re-check subagent. I built none of this text and none
of either remediation. I did not edit the text, land, shelve, commit, or
push anything. Every count below is from code I wrote and ran in this
session against `verses-store.json` and `master-verses.json`; the
remediation log's claims were treated as claims to verify, not as
evidence. The re-check report on file
(`CHECKER-REPORT-RECHECK-2026-11-28.md`) ends mid-Gate-5, as the
remediation log itself notes; where its later gates are missing I
relied only on my own firsthand work, and I say so where it matters.

## VERDICT: FAIL — not landable as DRAFT — NOT PUBLISHED

Per gate: Gate 1 Canonical + codepoints **PASS**. Gate 2 Compression,
book-wide **PASS** (zero at the deciding bound; the ≥8-word count is
reported for the record). Gate 3 Batch A fidelity, the deciding gate
**PASS** (46 of 46 sampled verses, clause by clause). Gate 4 Gold/silver
**PASS**. Gate 5 GAP recount **PASS**. Gate 6 Attestation band **FAIL**
(one condemned token, тэӈгы, 34 seats, named with the evidence
searched). Gate 7 Regression spot-check, batches B–J **PASS** (12 of
12). Gate 8 Fences **FAIL** (Мария at 11 seats and Евангелие at 7 seats
are not the Master's forms; the no-"first" fence and the glossary
sample pass).

The round-2 remediation genuinely closed the fragmentary class: the
ratio criterion is zero book-wide at Master ≥ 12 words, and every
mandatory Batch A seat I was directed to read now carries its Master
verse in full. The book fails on two findings neither earlier checker
caught, both verified firsthand below. Nothing in this report fails
the book on a candidate I did not verify firsthand.

---

## Gate 1 — CANONICAL + CODEPOINTS: PASS

My flattening of `master-verses.json` gives 6,236 Master seats. The
store holds 6,236 seats; the seat sets are exactly equal, and my
per-surah Counter comparison matches at all 114 surahs (no mismatching
surah). Seat 1:1 is exactly `Нумʼ нимня, Сянаваʼ Ерв, Сянана.` No seat
contains "redacted"; no seat is empty. Machine codepoint counts over
the whole store:

- U+0027 (ASCII apostrophe): **0**. U+2019: **0**. U+02B9 (ʹ): **0**.
- U+02BC (ʼ): **21,350**. U+02EE (ˮ): **48,643**.

These match the round-2 pipeline figures, verified independently.

## Gate 2 — COMPRESSION, BOOK-WIDE: PASS

My own recomputation (Nenets words < 40% of Master words):

- At Master ≥ 12 words: **0 verses**. The deciding criterion is met;
  the re-checker's 224-verse class is closed by count.
- At Master ≥ 8 words, for the record: **7 verses** — 37:73 (9 Master
  words, 3 Nenets), 53:49 (11, 4), 55:6 (8, 3), 56:4 (8, 3), 56:52
  (8, 3), 83:29 (11, 4), 100:10 (8, 3). These are all short verses
  outside the deciding bound and outside Batch A; I record the count
  as instructed and do not fail the gate on it.

## Gate 3 — BATCH A FIDELITY (the deciding gate): PASS

Sample: **46 verses** drawn from the round-2 re-rendered class as
listed in `REMEDIATION-2026-11-28.md` Round 2 (the 224-seat r2 list,
the six additional Satan seats, 2:83, and the 17 re-rendered short
verses), including expressly every seat my task named. Each was read
against the Master clause by clause: every content word carried by a
form, a glossary device, or a GAP; no dropped clause, no reversal, no
pronoun standing in place of dropped content. **All 46 pass.**

The expressly named seats:

- **2:83 PASS.** Covenant with the Children of Israel; worship of
  none but God (ӈопой + negation); good to parents, relatives,
  orphans and the needy as distinct objects; speaking nicely to
  people (сава вадиˮмʼ); regular prayer; alms; and the closing
  movement — "Then you turned away, except for a few of you,
  recanting" — now carried in full. 48 Nenets words for 47 Master.
- **2:166 PASS.** The followed disowning the followers, seeing the
  retribution, ties severed — all three clauses carried in 14 words.
- **2:280 PASS.** Hardship, deferment until ease, remission as
  charity as the better course, and "if you only knew" — all carried.
- **3:104 PASS.** The community calling to virtue, advocating
  righteousness, deterring from evil, and "these are the successful"
  — the verse that stood as one word now reads in full.
- **3:194 PASS.** "What You have promised us through Your
  messengers" (ңэдарабэйˮтаˮвна … ватосавэй хэтаˮвыдаˮмʼ), no
  disgrace on the Day of Resurrection, and "You never break a
  promise" as a carried clause.
- **The seven Satan seats — all PASS.** 2:34 (the angels addressed,
  the bowing, Satan's refusal, arrogance, disbeliever status);
  2:168 (lawful and good eating, Satan's footsteps, the open enemy);
  2:208 (wholehearted submission, Satan's footsteps, the outright
  enemy); 2:268 (Satan's promises of poverty and immorality against
  God's promise of forgiveness and grace; the two epithets);
  3:155 (the day the two armies clashed, Satan causing the
  backsliding on account of some of what they earned, God's
  forgiveness, Forgiving/Prudent); 3:175 (Satan frightening his
  partisans, "do not fear them, but fear Me", the believer
  condition); 4:120 (promises, raised expectations, and delusions —
  Satan promising nothing but delusions).
- **83:31 PASS.** Going back to their families, going back exulting
  (ябдасавэй) — both movements carried.

Six of the 17 re-rendered short verses (Master < 12 words), as
required: **2:12 PASS** (troublemakers; not aware), **3:2 PASS** (no
god but He; the Living; the Eternal — all restored), **3:5 PASS**
(nothing hidden from God, on earth or in the heaven), **3:76 PASS**
(fulfilling commitments, maintaining piety, God loves the pious),
**4:99 PASS** (God may pardon them; Pardoning and Forgiving as
distinct epithets), **4:138 PASS** (the informing verb restored; the
hypocrites riding their standing GAP; the painful punishment).

The remaining 27 sampled r2 seats, each read clause by clause, all
**PASS**: 2:8, 2:27, 2:40, 2:59, 2:82, 2:104, 2:127, 2:152, 2:176,
2:201, 2:225, 2:250, 3:16, 3:31, 3:59, 3:85, 3:125, 3:133, 3:157,
3:200, 4:8, 4:28, 4:61, 4:85, 4:112, 4:145, 4:161. Two semantic
loosenesses are recorded in the same breath without failing their
verses, in the re-checker's own precedent at 4:104: at 2:268 the
epithet "Embracing" rides Ӈарка ("Great"), and at 3:5 "hidden" rides
the лэтра- stem — in both seats the clause is present, addressed to
the right parties, and no content word is dropped.

## Gate 4 — GOLD/SILVER: PASS

My whole-store searches: **золот- 0 occurrences, серебр- 0
occurrences** anywhere in the book. The GAP seats stand exactly as
ruled: **⟦GAP: gold⟧ at 3:14, 3:75 and 3:91; ⟦GAP: silver⟧ at 3:14**.
Seat 3:14 reads as a whole verse: the catalogue (women, children,
heaped ⟦GAP: gold⟧ and ⟦GAP: silver⟧ with their accusative suffixes
riding after the markers, branded horses, livestock, fields), the
conveniences of the worldly life, and the finest resort with God are
all carried. At 3:75 the heap-of-gold / single-coin contrast stands;
at 3:91 the earth full of gold offered as ransom stands.

## Gate 5 — GAP RECOUNT: PASS

My recount: **119 seats, 146 markers**. Term census by my own regex:
hypocrite 36, jinn 32, pilgrimage 18, camel 16, adultery 15, usury 8,
donkey 3, gold 3, pearl 3, coral 2, cucumber 1, garlic 1, lentils 1,
onion 1, swine 1, silver 1, polytheist 1, ruby 1, pomegranate 1,
pitcher 1. Every term is one of the disclosed set: the standing list
(pilgrimage, jinn, hypocrite, adultery, usury, camel, polytheist)
plus donkey, pearl, coral, ruby, pomegranate, pitcher, cucumber,
garlic, lentils, onion, swine, gold, silver. No other GAP term occurs
anywhere in the store. The figures match the round-2 pipeline census,
verified independently.

## Gate 6 — ATTESTATION BAND: FAIL

Method: from `work/purple-untraced.json` (2,178 candidates, as
regenerated) I took the band weighted to the highest counts,
**excluding every token either earlier checker already ruled
ATTESTED-REGULAR or DEVICE** (the first checker's Gate 5 list, the
remediation-confirmed пынʼ/пынмʼ oblique cells, and the cleared
горчица / суббота / судеӈг- families), and ruled 45 further tokens
firsthand against `work/lexicon-giellalt.json` (lemma + paradigm
class), `work/attested-tokens.json`, and the running text of
`work/ibt-text.txt`. A token absent from the exact-form index was not
condemned for that alone: its stem was searched in all three
instruments before ruling.

### Express ruling on ёнарˮ "thousand" at 3:125

**ATTESTED-REGULAR.** The GiellaLT lexicon carries ёнарˮ as an exact
lemma (N, contlex N_ТАРЕ, English "thousand"); the attested-token
index carries ёнарˮ itself with its paradigm neighbours (ёнареˮ,
ёнарʼ, ёнармʼ, ёнартоʼ); the IBT running text contains the string 27
times. The remediation's claim is verified firsthand. The seat at
3:125 ("самляӈг ёнарˮ Нувʼ юне ядэланасавэй", five thousand angels)
is sound.

### ATTESTED-REGULAR (lemma + source named; regular paradigm cells)

- ӈэбтаӈодˮ (30) — ӈась "be": the ӈэбта conditional stem is attested
  passim in the IBT text (78 substring occurrences) and the index
  (ӈэбта, ӈэбтаˮ, ӈэбтавʼ); regular suffixed cell.
- ниӈ (27) — the ни- negative stem family; index carries ниӈа, ниӈоˮ.
- серраˮмʼ (24), серˮраˮмʼ (9), сердоˮмʼ (17) — серˮ (lexicon
  N_ВАР, English "thing"); possessive cells; the index carries серˮ,
  серˮӈэ, серˮмана.
- пумʼ (17) — пумна (lexicon, postposition, POSTP_PROS); oblique cell,
  cf. index пумнанда, пумнанаˮ.
- миˮяˮ (16), миˮваˮ (14), миˮӈгу (14), миˮда (11), миˮбтаˮ (10),
  миˮӈгуваˮ (10) — the мись / мипа- "give" family (lexicon verb
  classes; index миˮӈа, миˮӈада, миˮӈаˮ for the ӈгу cells). Further
  cells of the family the first checker ruled; each traced by stem
  here.
- тэнвавасиˮ (16), тэнвавыˮ (13), тэнвавамʼ (10) — the тэнва- "know"
  stem: the lexicon's cognate lemma is теневась (TV_ЛАХАНА, Finnish
  "tietää"), and the stem's participles are logged in the batch
  notes (тэнвада "All-Knowing"). The book's э-spelling of this stem
  is consistent throughout and is recorded here as a spelling
  variant of a traced lemma, not an invention.
- пинараяˮ (13) — пинась (lexicon IV_НАМДА, "pelätä") / пинаркась
  (IV_ИЛЕ); index пина, пинаˮ, пинаяˮ.
- ервдоˮхад (12), ерватоˮ (9) — ерв (lexicon N_ХАНО, "lord, master");
  index ерв, ерванʼ, ервада, ерваваˮ; IBT ерв 265 substring
  occurrences.
- тоӈгу (12), тоӈгуˮ (10) — тось (lexicon IV_ТУ, Finnish "tulla",
  "come/enter"); the ӈгу future cell on the same pattern the first
  checker ruled for ӈась → ӈаӈгу.
- валыторӈадмʼ (12) — валыторць (lexicon IV_ТИР, "vannoa, luvata",
  "swear, promise"); regular cell.
- лэтра (11), лэтраˮӈаˮ (15), лэтраӈаˮ (10) — лэтрась (lexicon
  TV_ХАДА, "keep, guard"); further cells of the ruled family, stems
  verified in the index (лэтраˮма, лэтраванʼ).
- сяливысиˮӈэ (11) — сялилць (lexicon TV_ТИР, "sääliä", "pity");
  index сялилˮма, сялилӈа, сялилць.
- няˮмадась (11) — the няˮма- family (lexicon няˮмарась IV_ЛАХАНА
  and neighbours); index няˮмадаˮ, няˮма, няˮмава.
- ядоˮ (11) — ядэрць "walk" (glossary §A; index ядэрӈаˮ, ядэрць,
  ядэрта); IBT ядэ- 218 substring occurrences.
- еˮэваˮ (11) — еˮэй (lexicon N_ЕД, "share, property"); index еˮэй,
  еˮэйӈэ, еˮэмня.
- тэнзебтевы (11) — тэнз (lexicon N_ХАНО, "people, tribe"); index
  тэнз, тэнзˮ, тэнзхат; derivative cell on attested parts.
- хэӈгуˮ (10) — index хэӈг- family (хэӈгада, хэӈгӈэ, хэӈгудмʼ);
  IBT хэӈг- 162 substring occurrences.
- ӈэˮмамʼ (10) — index ӈэˮма- family (ӈэˮмамдоʼ, ӈэˮмяʼ, ӈэˮмяхана).
- мирдоˮмʼ (10) — мирдапась / мирдатась (lexicon, "myydä", "sell");
  index мирда- forms passim.
- хаӈгва (10) — index хаӈг- family (хаӈгу, хаӈгуˮ, хаӈгˮ, хаӈгуртаˮ);
  IBT substring 162.
- мэӈаˮ (10) — the мэсь family; index мэӈахаʼ, мэӈамта carry the
  мэӈа- stem.
- таӈгабцяда (10) — таӈгабцо (glossary §C standing seat, "peace");
  index таӈгабцо, таӈгабцор, таӈгабцохона.
- няӈэ (10) — IBT running text, 89 substring occurrences; index
  няӈэнда, няӈэӈэ, няӈэхана.
- ӈэсонггана (10) — the ӈэсонд- "until" formative; index ӈэсоӈгана,
  ӈэсондʼ, ӈэсовы (spelling variant of the ruled ӈэсондоˮ family).
- ӈэвамзь (10) — the ӈэва- family of ӈэвасэй (glossary §E); index
  ӈэвамʼ, ӈэвамдоʼ, ӈэвахана.
- судеӈгдаˮ (10) — судеңгось (lexicon IV_СЯНАКУ, "tuomita"); the
  судеӈг- family as cleared in round 1, IBT-attested.
- хэˮмамʼ (9) — хэˮмя (lexicon N_ҢОДИ); index хэˮмя, хэˮмямʼ,
  хэˮмяхад.

### DEVICE / artifact (not lexemes, not condemned)

- тухана (10) — compositional locative on attested parts: ту "fire"
  (glossary §B) + the -хана locative seated passim. Ruled DEVICE.
- обʼ (12), ˮнʼ (24), тяремʼ (11) — purple-tokenizer fragments, not
  words: under word tokenization they have zero standalone seats
  (обʼ arises inside ӈобʼ, ˮнʼ inside possessive/dative suffixes,
  тяремʼ inside таремʼ, itself attested — index таремʼ, IBT 915
  substring occurrences). Recorded so the next checker sees them
  knowingly.

### CONDEMNED (verified firsthand; token, seats, evidence searched)

1. **тэӈгы** — purple count **54**, the third-highest token in the
   regenerated candidate list; **34 standalone seats**, all in Batch
   C (Surahs 10–16): 10:13, 10:60, 10:74, 11:17, 11:24, 11:84, 11:97,
   11:110, 11:118, 12:21, 12:32, 12:38, 12:40, 12:68, 13:1, 13:6,
   13:14, 13:26, 13:32, 13:42, 14:9, 14:11, 14:17, 14:22, 15:81,
   16:4, 16:9, 16:26, 16:38, 16:61, 16:63, 16:75, 16:93, 16:113.
   It is seated as a contrastive connective ("but / yet / the
   others") — e.g. 10:13 "…тэӈгы пыдоʼ пунрёсь нивыˮ харваˮ", 14:22
   "…мивын, тэӈгы сиддоʼ вэва сертавын". Evidence searched: the
   GiellaLT lexicon carries **no тэӈг- lemma and no тэӈг- stem**
   (I read the full тэ- inventory of the harvested lexicon; the
   nearest entries are тэңга "ham", with a different second letter,
   and the тэва-/тэв- families); the attested-token index carries
   **no тэӈг- form** — its only тэӈг hits are мантэӈгудˮ, мантэӈгуˮ,
   мантэӈгун, мантэӈгухуʼ, cells of a different verb; the IBT running
   text contains **тэӈгы 0 times**, and тэӈг- only inside those same
   мантэӈг- forms (7 substring occurrences). It is not in the
   glossary, and no batch note logs it as a device. Unlike пын in
   round 1 — where a full pronoun paradigm stood in the lexicon
   waiting to overturn the ruling — no paradigm, lemma, or attested
   form for this token exists in any of the three instruments.
   CONDEMNED as unattested as seated. If the desk can produce a
   Tundra-labelled attestation for тэӈгы from a named source, this
   ruling is the one to overturn on that evidence; on the record
   before me it does not stand.

That is 45 tokens ruled in this band (43 attested-regular or device,
1 artifact group counted as three fragment tokens, 1 condemned). The
band otherwise vindicates the desk's attestation arithmetic, exactly
as both earlier bands did: the great majority of the highest-count
"untraced" candidates are regular inflected cells an exact-form
index misses. The failure is confined to the one named token and its
34 named seats.

## Gate 7 — REGRESSION SPOT-CHECK (batches B–J): PASS

Twelve fresh fidelity verses, none sampled by either earlier checker
(their reports list their samples; I checked mine against both
lists), five of them over 40 Master words, read clause by clause:
**5:48** (99 Master words — the Book revealed with truth,
confirming and superseding, judging by what God revealed, desires
not followed, a law and a method for each, the single-nation
counterfactual, the test, competing in righteousness, the return,
the informing — all carried), **22:5** (121 — doubt about the
Resurrection, dust, drop, clot, lump of flesh developed and
undeveloped, the wombs and the designated term, infants, full
strength, passing away, the vilest age, knowing after having known,
the earth still then vibrating, swelling, growing lovely pairs —
all carried), **9:111** (63 — the purchase, lives and properties
for Paradise, fighting, killing and being killed, the promise in
the Torah, the Gospel and the Quran, rejoicing in the exchange,
the supreme triumph — all carried; the Gospel's name-form is ruled
on in Gate 8, not here), **14:22** (78 — Satan's speech when the
issue is settled, both promises, no authority except the call and
the answer, blame yourselves, no mutual aid, the rejection of the
past association, the painful torment — all carried; the тэӈгы
token in this verse is ruled on in Gate 6, not here), **61:14**
(55 — supporters of God, Jesus son of Mary's question, the
disciples' answer, the two groups of the Children of Israel, the
support against the foe, becoming dominant — all carried; the
disciples ride хамдяˮ "servants", a looseness recorded without
failing the verse), **6:102, 19:35, 25:63, 33:72, 41:49, 76:23,
98:7** — all pass, every clause carried. **12 of 12 pass.** Outside
Batch A the book's fidelity remains sound, as both earlier checkers
found.

## Gate 8 — FENCES: FAIL

- **No "first" claim: PASS.** My search of the store text found no
  "first" wording anywhere in the Nenets text.
- **Glossary fixed seats standing (sample of 5, plus the round-1
  sample re-run): PASS.** Нумʼ — 1,988 seats; судеӈгова — 86 seats;
  Ябдана я — 52 seats; Яʼ ӈылы — 99 seats; Яӈорʼ илелоˮма — 78
  seats; and ӈэвасэй (59), Хэбяха (44), Туёˮма (24), суббота (seated
  in its inflected forms at 2:65, 4:47, 4:154, 7:163) all stand in
  their fixed forms.
- **Names in the Master's forms (sample): FAIL.** Moses (134 seats),
  Abraham (63), Noah (43), Jesus (25), Torah (16), Psalms (4) and
  Quran (9) all ride in the Master's forms, as the names policy
  requires. But two Master's forms are displaced by Russian forms at
  named seats, inconsistently with the book's own practice
  elsewhere:
  - **Мария for Mary — 11 seats:** 5:17, 5:46, 5:72, 5:75, 5:78,
    5:110, 5:112, 5:114, 5:116, 9:31, 43:57 (e.g. 5:46 "Jesusмʼ,
    Марияʼ нюмʼ"), against Mary in the Master's form at 19 other
    seats.
  - **Евангелие for the Gospel — 7 seats:** 5:46, 5:47, 5:66, 5:68,
    5:110, 7:157, 9:111 (e.g. 5:47 "Евангелиеʼ хибяриˮ"), against
    Gospel in the Master's form at 5 other seats (3:3, 3:48, 3:65,
    48:29, 57:27).
  Мария and Евангелие are the IBT control's forms, which explains
  their origin; the BUILD-SPEC names policy nevertheless seats the
  Master's forms unaltered, the glossary makes no seat for these
  forms, and no batch note discloses them. The first checker counted
  the Master's forms and passed this fence without searching for
  the Russian ones; firsthand searching finds them. FAIL on the 18
  named seats (5:46 and 5:110 carry both).

---

## Summary for remediation (named seats only)

- Attestation: produce a Tundra-labelled attestation for **тэӈгы**
  from a named source, or replace it in its **34 seats** (10:13,
  10:60, 10:74, 11:17, 11:24, 11:84, 11:97, 11:110, 11:118, 12:21,
  12:32, 12:38, 12:40, 12:68, 13:1, 13:6, 13:14, 13:26, 13:32,
  13:42, 14:9, 14:11, 14:17, 14:22, 15:81, 16:4, 16:9, 16:26, 16:38,
  16:61, 16:63, 16:75, 16:93, 16:113) with an attested connective,
  then re-check those seats.
- Names: seat the Master's forms **Mary** and **Gospel** at the 18
  named seats in Gate 8, or disclose a glossary seat for the IBT
  forms by the desk's ruling — the present undisclosed inconsistency
  is the failure, and it is the desk's call which way to close it.
- Everything else stands: Gates 1–5 and 7 pass on my own counts and
  firsthand reading, including the deciding Batch A gate — the
  round-2 re-renders are clause-complete in all 46 verses I read,
  gold and silver ride their ruled GAPs, and the GAP census is
  exactly the disclosed set.

**Overall verdict: FAIL — not landable as DRAFT — NOT PUBLISHED,**
on Gate 6 (тэӈгы, 34 seats) and Gate 8 (Мария / Евангелие, 18 seats)
only. Both failures are confined to named tokens and named seats;
no other gate fails.
