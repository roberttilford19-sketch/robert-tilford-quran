# CHECKER REPORT — Romansh (Rumantsch Grischun) Quran lane

Independent checker report, 2026-11-27. The checker did not build any of
this text. Graded against the Locked English Master
(`master-verses.json`, 6,236 verses), the attested sources
(`sources/entries_RG-DE.txt` — Pledari Grond RG→German, RG side first;
`sources/rg-paradigms.json` — 3,817 conjugated verbs;
`sources/rg-attested-inventory.json`; `sources/rmwiki-plain.txt`), the
BUILD-SPEC's two laws (Form Law, Fidelity Law), the glossary of record,
and the batch notes. Every claim below carries its evidence: seat
numbers, counts, or the source line relied on.

## Verdict in one breath

**DO NOT LAND.** The book's skeleton is sound — the canonical grid is
exact (Gate 1 PASS), the GAP census is clean (Gate 5 PASS), and the
fidelity of the running text is, verse by verse, remarkably high with
no pronoun-collapse anywhere in 136 verses read clause by clause
(Gate 2 PASS, qualified). But the Form Law — this lane's first law,
written after the Veps lane failed its checker — is breached at scale
in Batch A (Surah 2): of the 133 suspect distinct tokens in
`verify-report.json`, **120 types (211 tokens) are UNATTESTED** against
PG, the paradigm tables, and the inventory (Gate 3 FAIL), including
exactly the Veps failure signatures — sister-idiom borrowings
(Sursilvan *dschai/dschais*, *vos*, *nos*), foreign loans (Italian
*meraviglia*, *orgogli*; French *traits*; English *surplus*, *end*),
a synthetic future (*terrarai*, 2:34), and paradigm-defying verb forms
(*proclaman* for PAR *proclameschan*, *fand* for PAR *faschond*,
*prendond* for PAR *prendend*, *udeva* for PAR *udiva*). The sense
gate also fails on the wonder seats (Gate 4): *marvezza* — PG
"Steifheit, Starre" (stiffness, rigor) — is seated for "wonder" at
10:2, 13:5 and 12:31. Batch A's own notes claim these 131 exception
types are "regular inflections… none is a borrowing" — that claim is
false on the record (Gate 7 FAIL for Batch A). The defects are
concentrated: essentially all of them sit in Surah 2 (Batch A), built
before the desk steering recorded in notes-M; Batches B–P self-screen
clean and the sampled notes for B, I and M verify. The repair is
bounded and mechanical, but it is owed before landing.

---

## Gate 1 — CANONICAL: **PASS**

Re-derived independently of `verify.py`, by direct count from
`verses-store.json` (not from the batch files):

- Store seats: **6,236**. Master seats (flattened from
  `master-verses.json`): **6,236**. Seat sets are **identical**
  (set-equality check, no seat in either that is not in the other).
- Per-surah counts in the store match the standard grid at **all 114
  surahs** (grid used: 7, 286, 200, 176, 120, 165, 206, 75, 129, 109,
  123, 111, 43, 52, 99, 128, 111, 110, 98, 135, 112, 78, 118, 64, 77,
  227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53,
  89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24,
  13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31,
  50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11,
  8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6 —
  sum 6,236). Zero mismatches.
- This agrees with `verify-report.json` (`seat_set_equal: true`,
  `per_surah_ok: true`) by a different route, as required.

## Gate 2 — FIDELITY SPOT-CHECK: **PASS (qualified — one FAILED seat, nine WEAKENED seats, all named below)**

Sample, as commissioned:

- **(a)** Every verse of 60+ Master words in Surahs 2, 4, 5, 9, 24, 33,
  49, 60, 65: **103 verses** (2:25, 2:26, 2:61, 2:85, 2:102, 2:136,
  2:143, 2:144, 2:145, 2:150, 2:164, 2:177, 2:178, 2:185, 2:187, 2:196,
  2:213, 2:217, 2:221, 2:228, 2:229, 2:231, 2:233, 2:235, 2:237, 2:246,
  2:247, 2:249, 2:253, 2:255, 2:258, 2:259, 2:260, 2:264, 2:275, 2:282,
  2:286; 4:6, 4:11, 4:12, 4:19, 4:23, 4:24, 4:25, 4:34, 4:43, 4:46,
  4:77, 4:78, 4:90, 4:91, 4:92, 4:94, 4:102, 4:127, 4:141, 4:153,
  4:157, 4:171, 4:176; 5:2, 5:3, 5:5, 5:12, 5:17, 5:18, 5:32, 5:41,
  5:44, 5:45, 5:48, 5:54, 5:64, 5:89, 5:95, 5:106, 5:110, 5:116; 9:24,
  9:40, 9:74, 9:94, 9:111, 9:120; 24:31, 24:33, 24:35, 24:43, 24:55,
  24:58, 24:61, 24:62; 33:35, 33:37, 33:50, 33:51, 33:53; 49:11; 60:1,
  60:4, 60:10; 65:1, 65:6).
- **(b)** Random sample of 30 further verses, drawn with Python
  `random.sample` over the sorted seat list, **seed 20261127**:
  3:10, 54:9, 18:4, 20:129, 44:19, 8:46, 10:4, 19:75, 27:66, 16:43,
  18:56, 5:40, 9:90, 37:18, 2:273, 9:107, 96:1, 12:76, 3:42, 53:3,
  92:16, 68:49, 38:46, 8:75, 83:28, 82:17, 2:222, 3:155, 34:52, 41:16.
- **(c)** The named seats 2:282, 2:34, 4:12, 5:3, 9:74, 24:31, 33:53,
  58:22, 73:20 (six of these already fall in (a); 2:34, 58:22 and
  73:20 are additional).

**Total distinct verses read clause by clause: 136.**

**Tally: 126 CARRIED · 9 WEAKENED · 1 FAILED.**

**Pronoun-collapse check (the named failure signature):** no verse in
the sample replaces content words with pronouns. Romansh token count
vs Master word count was computed for every sampled verse; the lowest
ratio in the whole sample is above 0.55, and in the long-verse belt
the Romansh is typically at or above the Master's length (e.g. 2:282:
227 Master words → 246 Romansh tokens; 5:110: 130 → 150; 24:31:
113 → 137). This agrees with `verify-report.json`
(`fidelity_collapse_candidates: []`). The Veps collapse signature is
absent from this lane.

Every non-CARRIED seat, in full:

- **2:34 — FAILED (form and mood).** Master: "And We said to the
  angels, 'Bow down to Adam.' They bowed down, except for Satan. He
  refused, was arrogant, and was one of the disbelievers." Romansh:
  "«As terrarai davant Adam.» Els èn sa terrads, auter che Satan…"
  The Master's **imperative** is rendered by *terrarai*, a
  synthetic-future-shaped form that exists in no paradigm: PAR
  *terrar* gives Imperativ pl. "terrai!" and a periphrastic future
  only (BUILD-SPEC: "prophetic future takes the periphrastic future —
  the only future the PG conjugator carries"). The command's mood is
  lost and the form is unattested. All other content is carried.
  Repair at Gate 3 / repair list.
- **2:259 — WEAKENED.** All clauses carried (the hundred years, the
  unspoiled food and drink, the donkey, the bones clothed with flesh),
  but "We will make you a **wonder** for mankind" is seated as "ina
  **meraviglia**" — an unattested Italian loan of the wrong wonder
  family (see Gates 3–4). One content word fails in form and family.
- **5:2 — WEAKENED (three losses).** "Do not **violate** God's
  sacraments" → "Na faschai betg **donn** a las chaussas sontgas"
  (do not *harm*); "let not the hatred of people… incite you to
  **aggression**" → "na vus mainia betg a **far donn**" (aggression
  flattened to harm, the same word doing both jobs); "cooperate with
  one another in virtuous conduct and **conscience**" → "gidai in
  l'auter en il bun agir e en **la tema da Dieu**" (conscience
  replaced by fear of God — an interpretive substitution, not the
  Master's word). The rest of this 90-word verse is carried.
- **5:45 — WEAKENED.** "it will serve as **atonement** for him" →
  "quai vegn a servir ad el sco **perdun**" (forgiveness). Atonement
  and forgiveness are different seats; the Master distinguishes them.
- **5:89 — WEAKENED.** Same substitution, twice in one verse: "The
  **atonement** for it is by feeding ten needy people…" and "That is
  the **atonement** for breaking your oaths" → both seated as
  "**perdun**". (Also 5:95, "he may **atone** by feeding the needy" →
  "el po **perdunar** cun dar da mangiar".) A systematic
  atonement→forgiveness flattening in Batch C's Surah 5 seats.
- **24:31 — WEAKENED (one phrase).** The long modesty catalogue is
  carried in full, relation by relation; but "children who are not yet
  aware of the **nakedness of women**" → "uffants che n'èn anc betg
  conscients dals **cors zuppads** da las dunnas" (the *hidden bodies*
  of women). Nakedness is replaced by hiddenness.
- **33:53 — WEAKENED (one word).** All clauses carried; "ask them
  from behind a **screen**" → "dumandai ellas da davos ina **paraid**"
  (a *wall*). Screen→wall is a concrete-object substitution.
- **37:18 (random sample) — WEAKENED.** "and you will be totally
  **subdued**" → "vus vegnis a vegnir **fatgs pitschens**" (made
  small). Subdual replaced by diminishment.
- **27:66 (random sample) — WEAKENED.** "In fact, they are **blind**
  to it" → "els **na vesan betg** ella" (they do not see it).
  Blindness flattened to not-seeing.
- **68:49 (random sample) — WEAKENED.** "he would have been thrown
  into the wilderness, **fully despised**" → "fiss el stà bittà en la
  terra deserta, **plain da vargugna**" (full of shame). Despised (by
  others) replaced by ashamed (in himself).
- **38:46 (random sample) — WEAKENED.** "We **distinguished** them
  with a distinct quality: the remembrance of the **Home**" → "Nus
  avain **elegì** els cun ina qualitad speziala: la regurdientscha da
  la **Chasa**" (chosen; the House). Both content words shifted.

Named-seat results inside the tally: 2:282 CARRIED (every clause of
the 227-word debt verse present, including the two-women testimony
clause and the spot-transaction exception); 4:12 CARRIED (all
fractions — halves, fourths, eighths, sixths, thirds — in order);
5:3 CARRIED (the full prohibited list, the rescue exception, the
drawing of lots); 9:74 CARRIED; 24:31 WEAKENED (above); 33:53
WEAKENED (above); 58:22 CARRIED (independently re-read against
notes-M's self-audit map — the map and the text agree); 73:20
CARRIED (night fractions, the three classes of readers, the generous
loan, all present).

## Gate 3 — TOKEN ADJUDICATION: **FAIL**

Method: every one of the 133 distinct suspect tokens in
`verify-report.json` was checked against (i) the PG RG-side headwords
in `entries_RG-DE.txt`, (ii) every form in the 3,817 paradigm tables
in `rg-paradigms.json`, (iii) the 161,521-form inventory, and (iv)
rmwiki running text (corroboration only, per the attestation audit —
a form attested only there cannot seat). Verdicts: **ATTESTED** (named
source), **REGULAR** (paradigm-conform derivation of an attested
lemma — lemma and pattern named), **UNATTESTED** (repair owed).

**Tally: 3 ATTESTED · 6 ATTESTED\* (the word is attested; the token is
a batch-N guillemet artifact — Gate 6) · 4 REGULAR · 120 UNATTESTED
(211 tokens).**

Named attention, as commissioned:

- **terrarai (2:34)** — UNATTESTED. Not a synthetic future the lane
  may use: the conjugator carries no synthetic future for any verb,
  and BUILD-SPEC mandates the periphrastic future. It is also the
  wrong mood — the Master at 2:34 is an imperative ("Bow down"), and
  PAR *terrar* Imperativ pl. is "terrai!". See Gate 2.
- **udeva (2:75)** — UNATTESTED. PAR *udir* Imperfect is *udiva,
  udivas…*; the udev- stem exists nowhere. Notes-M steering (§3 of
  the desk steering there) holds the udiva line for exactly this
  reason.
- **fand (2:196, 2:233, 2:279)** — UNATTESTED. PAR *far* Gerundium
  is *faschond*. An Italian-shaped gerund coinage.
- **prendond (2:233)** — UNATTESTED. PAR *prender* Gerundium is
  *prendend*.
- **meraviglia (2:259)** — UNATTESTED. Italian loan; no PG/PAR seat;
  wrong wonder family (repair: *smirvegl* family, Gate 4).
- **vussezs (9 tokens, Surah 2)** — UNATTESTED. Coined compound
  reflexive; the attested form is two words, *vus sezs*, which the
  book itself uses elsewhere (e.g. 4:43's batch, "Vus sezs eras").
- **rescat (2:48, 2:123, 2:184) and rescattais (2:85)** — UNATTESTED.
  No PG headword, no paradigm lemma. Notes-M §3 record the desk's own
  later verdict: "*rescat* is a named batch A zero-presence failure
  and was never seated" in Batch M (57:15 re-rendered instead).
- **spander (2:30, 2:84)** — UNATTESTED. No PG/PAR lemma; the
  'shed/spill' verb is a sister-idiom/Italian shape.
- **politeist / politeists (2:96, 2:105)** — UNATTESTED. PG has
  *politecnic, politecnicum* only; the word is a Germanic coinage.
- **nuncretta (2:88, 2:93, 2:108)** — UNATTESTED. Abstract noun
  coined on *cretta*; no PG headword.
- **cumplir (5 tokens) and family** (*cumplen* 2:177, *cumplanì*
  2:187) — UNATTESTED. The PG lemma is **accumplir** ("erfüllen,
  vollenden"); *cumplir* is a clipped coinage. The book itself seats
  *ademplir* for the same Master word elsewhere (4:12).
- **end (2:235)** — UNATTESTED. Lone token in "tegn end el per
  vussezs"; PG carries *end* only inside "happy end" and "tasta END".
  No Romansh seat.
- **vos (30 tokens) / nos (6 tokens in the report's count; 26 and 14
  seats respectively store-wide, all in Surah 2)** — UNATTESTED.
  These are the Sursilvan possessives. PG's RG possessives are
  **voss, vossa** ("voss, vossa — euer") and **noss, nossa**. Batch A
  mixes them with the correct forms in a single verse (2:128: "nos
  descendents" beside "noss rits"). A silent sister-idiom borrowing —
  the exact act BUILD-SPEC's Form Law names and bars.

The pattern behind the 120: Batch A repeatedly formed verbs on the
infinitive/present stem where the conjugator's table for that lemma
gives a different stem — *proclaman* (PAR *proclameschan*),
*navigan* (PAR *navigheschan*), *revelan* (PAR *reveleschan*),
*engianan/engiana* (PAR *engionan/engiona*), *reconcilia* (PAR
*reconciliescha*), *divorzia* (PAR *divorziescha*), *svia* (PAR
*sviescha*), *stgamian/stgamia* (PAR *stgomian/stgomia*),
*suondass/suondassan* (PAR *suandass/suandassan*), *cumbatessas/
cumbatessan* (PAR *cumbattess-*), *tramessess* (PAR *tramettess*),
*smaledì* (PAR *smaladì*), *victorià* (PAR *victorisà*), *savavas*
(PAR *savevas*), *volvai* (PAR *vulvai*), *baivai* (PAR *bavai*),
*chapais* (PAR *chapis*), *servais* (PAR *servis*), *tschernai*
(PAR *tscherni*), *resolveschan* (PAR *resolvan*), *terran* (PAR
*terreschan*), *stont* (PAR *stond*), *annunziend/divorziend*
(gerunds in the wrong class ending) — and coined nouns, agents and
adjectives with no lemma behind them (*aggressiun, aggressurs,
gidader, putgader(s), smalediders, imposturs, idolater(s)/idolatra(s)/
idolatric, disubedientscha, disubedì/disubedin, nunintenziunads,
nunengraziaivel(s), scissiun, redempziun, deterrenza, conducta,
baivra, traits, regrets, orgogli, surplus, fasibel, lisch, digns,
malfats, rits, chalcongs, sontgifitgain, glischnis, itgescha,
entaupar* family, *assignar* family, *exhortà, dedicà, directà,
desavuà, infligì, guastà, dannà/dannada, disturscheva, smarrids,
schanuglian/schanugliai, cundanna, spander, rescat* family,
*cumplir* family, *dschai/dschais, turpeggia, vieuais, offerì,
murì, pejor, giavischus, donnus, disonest, onoraivla/onoraivelmain,
onestitad, abundaivel, sumeglianza, tschaguolas*).

**Name candidates (159 in `verify-report.json`):** sanity-checked.
Every genuine proper name is carried in the Master's form (Abraham,
Noah, Mary, Lot, Joseph, Solomon, Ishmael, Zechariah, Jonah, Goliath,
Luqman, Elijah, Elisha, Ezekiel, Muhammad, Ahmad, Ezra, Harut, Marut,
Quraish, Thamood, Aad, Hud, Saleh, Shuaib, Sinai, Sheba, Babylon,
Egypt, Medina, Kaabah, Safa, Marwa, Arafat, Badr, Sirius, Tariq,
Saqar, Sijjeen, Elliyyeen/Elliyyoon, Tasneem, Zanjabeel, Salsabeel,
the disjointed-letter names Alif/Lam/Meem/Kaf/Ha/Ya/Ayn/Saad/Qaf/Ra/
Seen, Samarian — Master's own form at 20:85/20:95 — and Sabeans at
2:62). The remaining candidates are capitalised sentence-initial
common words and divine epithets (Daveras "truly", Perdunant,
Sapient, Crist, Creadur, Trumbeta, Lotus…), not names. Three
lowercase failures hide among the capitals, all already counted in
the 120: **Nos** (capitalised *nos*, 12 tokens), **Murì**, **Dschai**,
and **Sontgifitgai** (the *sontgifitgain* family). One further flag:
**Vae** (14 tokens, e.g. 36:30, 36:52, 77:15) renders the Master's
"Alas/Woe" with a Latin interjection that is neither a carried Master
name nor a glossary seat — a minor unlogged loan, repair owed.

### Full token adjudication table (133 types)

| Token | Tokens | Seats (first 8) | Verdict | Ground |
|---|---|---|---|---|
| vos | 30 | 2:105, 2:108, 2:139, 2:178, 2:195, 2:196, 2:198, 2:200 | UNATTESTED | Sursilvan possessive; PG possessive is voss/vossa ('voss, vossa — euer'). Repair: voss. |
| vussezs | 9 | 2:110, 2:187, 2:195, 2:223, 2:235, 2:281, 2:284, 2:44 | UNATTESTED | Coined compound reflexive; attested form is two words vus sezs (used elsewhere in the book). |
| retribuziun | 7 | 2:166, 2:178, 2:179, 2:191, 2:194, 2:196, 2:211 | UNATTESTED | No PG headword retribu*, no paradigm lemma retribuir; -ziun coinage. |
| nos | 6 | 2:128, 2:139, 2:170, 2:246, 2:285, 2:286 | UNATTESTED | Sursilvan possessive; PG possessive is noss/nossa. Repair: noss. |
| cumplir | 5 | 2:150, 2:185, 2:233, 2:283, 2:40 | UNATTESTED | No such lemma in PG/PAR; PG lemma is accumplir ('erfüllen'). Clipped coinage; cf. cumplir-family cumpler/cumplen/cumplanì/cumplenida seats. |
| dschai | 4 | 2:104, 2:154, 2:58 | UNATTESTED | Sursilvan spelling of dir imperative; PAR dir Imperativ is 'schai!'. Sister-idiom borrowing, barred by BUILD-SPEC. |
| aggressiun | 4 | 2:178, 2:190, 2:194, 2:231 | UNATTESTED | No PG aggress* headword; the inventory form used in later batches is agressiun (single g). |
| nuncretta | 3 | 2:108, 2:88, 2:93 | UNATTESTED | Coined abstract noun from cretta; no PG headword. |
| suondass | 3 | 2:120, 2:145 | UNATTESTED | suandar Cundiziunal stem is suand- (PAR: suandass); suond- is the present stem. |
| rescat | 3 | 2:123, 2:184, 2:48 | UNATTESTED | No PG/PAR lemma; named a batch-A zero-presence failure in notes-M §3 (57:15) and never seated there. |
| rits | 3 | 2:128, 2:158, 2:200 | UNATTESTED | No PG headword rit (only ritmus); plural coinage for 'rites'. |
| fand | 3 | 2:196, 2:233, 2:279 | UNATTESTED | far Gerundium is faschond (PAR); fand is an Italian-shaped gerund coinage. |
| conducta | 3 | 2:197, 2:44, 2:59 | UNATTESTED | As abstract noun 'conduct' no PG seat; PG conduct = conduit/pipe (Ablaufleitung etc.) — form and sense both fail. |
| entaupar | 3 | 2:223, 2:249, 2:46 | UNATTESTED | No PG headword, no paradigm lemma, not in infinitives; Sursilvan-shaped meeting verb. |
| › | 3 | 67:9, 71:20, 72:15 | ATTESTED* | Not a word: closing single-guillemet artifact of batch N (see Gate 6). |
| politeists | 2 | 2:105, 2:96 | UNATTESTED | No PG politeist* (only politecnic/politecnicum); Germanic plural coinage. |
| gidader | 2 | 2:107, 2:120 | UNATTESTED | Agent coinage; PG agent for gidar is gidanter/gidantra. |
| vairaivels | 2 | 2:111, 2:23 | UNATTESTED | No PG vairaivel headword; adjective coinage on vair. |
| schanuglian | 2 | 2:125, 2:43 | UNATTESTED | Verb schanugliar is no paradigm lemma (PG has noun schanugl, knee, in compounds only). |
| dschais | 2 | 2:140, 2:80 | UNATTESTED | Sursilvan spelling; PAR dir Preschent 2pl is schais. |
| volvai | 2 | 2:144, 2:150 | UNATTESTED | volver Imperativ pl is vulvai (PAR); volv- stem wrong. |
| savavas | 2 | 2:151, 2:239 | UNATTESTED | savair Imperfect 2pl is savevas (PAR). |
| voluntariamain | 2 | 2:158, 2:184 | ATTESTED | PG phrase headword: 'manchentar aposta/voluntariamain — schwänzen'. |
| sumeglianza | 2 | 2:17, 2:264 | UNATTESTED | -anza coinage; the book's own inventory form elsewhere is sumeglientscha. |
| stgamian | 2 | 2:174, 2:175 | UNATTESTED | stgamiar Preschent 3pl is stgomian (PAR). |
| baivai | 2 | 2:187, 2:60 | UNATTESTED | baiver Imperativ pl is bavai (PAR). |
| fasibel | 2 | 2:196 | UNATTESTED | No PG/PAR seat; coinage for 'feasible'. |
| divorzia | 2 | 2:230 | UNATTESTED | divorziar Preschent 3sg is divorziescha (PAR, -esch class). |
| amicabelmain | 2 | 2:231 | REGULAR | -main adverb on PG-attested amicabel ('freundlich'); -main pattern attested (voluntariamain, gistamain). |
| victorià | 2 | 2:249, 2:251 | UNATTESTED | victorisar Particip Perfect is victorisà (PAR); clipped pp. |
| svia | 2 | 2:26 | UNATTESTED | sviar Preschent 3sg is sviescha (PAR). |
| malfats | 2 | 2:271, 2:81 | UNATTESTED | Plural coinage; attested noun malfatg has plural malfatgs (used in the same verse, 2:81). |
| cundanna | 2 | 2:276, 2:286 | UNATTESTED | cundannar is no paradigm lemma and no PG headword. |
| putgader | 2 | 2:276, 2:283 | UNATTESTED | Agent coinage on putgà; no PG seat. Later batches render descriptively ('quels che fan putgads'). |
| spander | 2 | 2:30, 2:84 | UNATTESTED | No PG/PAR lemma; Italian/Sursilvan-shaped 'shed/spill'. |
| chapais | 2 | 2:44, 2:76 | UNATTESTED | chapir Preschent 2pl is chapis (PAR). |
| at | 2 | 86:1, 86:2 | ATTESTED | Component of the Master's carried name at-Tariq (86:1–2), per the Names policy; tokeniser split on the hyphen. |
| stgamia | 1 | 2:108 | UNATTESTED | stgamiar Preschent/Conjunctiv stem is stgomi- (PAR: stgomia). |
| vieuais | 1 | 2:115 | UNATTESTED | 2pl coinage on the vieut pp stem; volver Preschent 2pl is vulvais (PAR). |
| terran | 1 | 2:125 | UNATTESTED | terrar Preschent 3pl is terreschan (PAR). |
| assignar | 1 | 2:126 | UNATTESTED | No PG headword, no paradigm lemma (family: assignai, assignads). |
| engiana | 1 | 2:130 | UNATTESTED | engianar Preschent 3sg is engiona (PAR). |
| exhortà | 1 | 2:132 | UNATTESTED | exhortar is no paradigm lemma and no PG headword. |
| murì | 1 | 2:132 | UNATTESTED | As seated (2:132 imperative context) not a paradigm form: murir Imperativ pl is 'muri!', Particip Perfect is mort. |
| idolatric | 1 | 2:135 | UNATTESTED | Adjective coinage; PG has only the noun idolatria. |
| scissiun | 1 | 2:137 | UNATTESTED | No PG headword. |
| chalcongs | 1 | 2:143 | UNATTESTED | No PG headword (Italian calcagno shape); 'heels' coinage at 2:143. |
| suondassan | 1 | 2:145 | UNATTESTED | suandar Cundiziunal 3pl is suandassan (PAR). |
| smarrids | 1 | 2:15 | UNATTESTED | smarrir is no paradigm lemma; no PG smarr* headword. |
| nunengraziaivels | 1 | 2:152 | UNATTESTED | Coined nun- compound adjective (family: nunengraziaivel). |
| smalediders | 1 | 2:159 | UNATTESTED | Agent-plural coinage on smaladir; no PG seat. |
| proclaman | 1 | 2:160 | UNATTESTED | proclamar Preschent 3pl is proclameschan (PAR, -esch class). |
| navigan | 1 | 2:164 | UNATTESTED | navigar Preschent 3pl is navigheschan (PAR). |
| desavuà | 1 | 2:167 | UNATTESTED | desavuar is no paradigm lemma; no PG headword. |
| regrets | 1 | 2:167 | UNATTESTED | French/English loan plural; no PG seat. |
| servais | 1 | 2:172 | UNATTESTED | servir Preschent 2pl is servis (PAR). |
| dedicà | 1 | 2:173 | UNATTESTED | dedicar is no paradigm lemma; PG has only dedicaziun. |
| cumplen | 1 | 2:177 | UNATTESTED | cumplir family — see cumplir. |
| reconcilia | 1 | 2:182 | UNATTESTED | reconciliar Preschent 3sg is reconciliescha (PAR, -esch class). |
| dretgamain | 1 | 2:186 | REGULAR | -main adverb on PG-attested dretg; pattern as voluntariamain/gistamain. |
| cumplanì | 1 | 2:187 | UNATTESTED | cumplir family — see cumplir (2:187 'complete the fast'). |
| offerì | 1 | 2:188 | UNATTESTED | offrir Particip Perfect is offrì/offert (PAR); single-f spelling is not the paradigm form. |
| aggressurs | 1 | 2:190 | UNATTESTED | Agent plural coinage; no PG aggress* headword. |
| retaliai | 1 | 2:194 | UNATTESTED | retaliar is no paradigm lemma; English-shaped loan verb. |
| redempziun | 1 | 2:196 | UNATTESTED | No PG headword. |
| orgogli | 1 | 2:206 | UNATTESTED | Italian loan (orgoglio); RG seats are superbia/loschezia. |
| glischnis | 1 | 2:209 | UNATTESTED | Verb glischnar coined at 2:209 ('if you slip'); no PG/PAR seat. |
| stont | 1 | 2:217 | UNATTESTED | star Gerundium is stond (PAR). |
| intossicants | 1 | 2:219 | UNATTESTED | Plural adjective coinage; no PG seat. |
| surplus | 1 | 2:219 | UNATTESTED | English/French loan; PG word is surpli ('surpli d'expensas'). |
| assignai | 1 | 2:22 | UNATTESTED | assignar family — see assignar. |
| disonest | 1 | 2:220 | UNATTESTED | No PG headword (PG: onest, onestadad). |
| idolatras | 1 | 2:221 | UNATTESTED | Agent coinage on idolatria (family: idolatra, idolater, idolaters — German/English shapes). |
| idolatra | 1 | 2:221 | UNATTESTED | See idolatras. |
| idolaters | 1 | 2:221 | UNATTESTED | See idolatras (English plural shape). |
| idolater | 1 | 2:221 | UNATTESTED | See idolatras. |
| donnus | 1 | 2:222 | UNATTESTED | -us adjective coinage on donn at 2:222 ('harmful'). |
| directà | 1 | 2:222 | UNATTESTED | directar is no paradigm lemma; no PG seat. |
| nunintenziunads | 1 | 2:225 | UNATTESTED | Coined nun- compound participle. |
| resolveschan | 1 | 2:227 | UNATTESTED | resolver Preschent 3pl is resolvan (PAR). |
| onoraivla | 1 | 2:229 | UNATTESTED | Italianate shape; PG adjective is onuraivel (family: onoraivelmain). |
| dannada | 1 | 2:233 | UNATTESTED | dannar is no paradigm lemma; no PG headword (family: dannà). |
| dannà | 1 | 2:233 | UNATTESTED | See dannada. |
| prendond | 1 | 2:233 | UNATTESTED | prender Gerundium is prendend (PAR); -ond coinage. Notes-M steering names prendond-type coinages as a batch-A failure. |
| onoraivelmain | 1 | 2:234 | UNATTESTED | Stem onoraivel itself unattested — see onoraivla. |
| annunziend | 1 | 2:235 | UNATTESTED | annunziar Gerundium is annunziond (-ar class); -end is the wrong class ending. |
| end | 1 | 2:235 | UNATTESTED | Lone token at 2:235 ('tegn end el'); PG carries 'end' only in 'happy end / tasta END'. No RG seat. |
| entaupai | 1 | 2:235 | UNATTESTED | entaupar family — see entaupar. |
| divorziend | 1 | 2:236 | UNATTESTED | divorziar Gerundium is divorziond (PAR). |
| cumbatessas | 1 | 2:246 | UNATTESTED | cumbatter Cundiziunal stem is cumbattess- (PAR, double t). |
| cumbatessan | 1 | 2:246 | UNATTESTED | See cumbatessas. |
| digns | 1 | 2:247 | UNATTESTED | No PG headword dign (only dignitad); plural coinage. |
| retegniss | 1 | 2:251 | REGULAR | retegnair Cundiziunal stem retegniss- per its paradigm table (PAR lemma retegnair). |
| baivra | 1 | 2:259 | UNATTESTED | Noun coinage on baiver; no PG headword. Later batches seat the noun baiver (e.g. 10:4). |
| guastà | 1 | 2:259 | UNATTESTED | guastar is no paradigm lemma; no PG headword. |
| meraviglia | 1 | 2:259 | UNATTESTED | Italian loan (maraviglia); no PG/PAR seat, and the wrong wonder family — repair on smirvegl (see Gate 4). |
| turpeggia | 1 | 2:26 | UNATTESTED | Double-g spelling; the inventory form seated elsewhere is turpegia (33:53). |
| itgescha | 1 | 2:261 | UNATTESTED | Nonsense coinage at 2:261 ('Dieu multipel itgescha' for 'God multiplies'); no source seat. Sense broken at this word. |
| lisch | 1 | 2:264 | UNATTESTED | 'Smooth' at 2:264; PG lisch- seats are lischerna (lizard). No 'smooth' seat. |
| tschernai | 1 | 2:267 | UNATTESTED | tscherner Imperativ pl is 'tscherni!' (PAR). |
| gidants | 1 | 2:270 | UNATTESTED | Participle-plural coinage on gidar; PG agent is gidanter/gidantra. |
| traits | 1 | 2:273 | UNATTESTED | French loan ('features', 2:273); no PG seat. |
| nunengraziaivel | 1 | 2:276 | UNATTESTED | See nunengraziaivels. |
| onestitad | 1 | 2:282 | UNATTESTED | Variant coinage; PG noun is onestadad. |
| sontgifitgain | 1 | 2:30 | UNATTESTED | Coined compound verb (sontg + fitgar shape) at 2:30; no PG/PAR seat. Family: sontgifitgai, sontgifitgar seats. |
| terrarai | 1 | 2:34 | UNATTESTED | Synthetic-future shape at 2:34. PAR terrar: Imperativ pl 'terrai!', future periphrastic only (BUILD-SPEC). See Gate 2. |
| schanugliai | 1 | 2:43 | UNATTESTED | Imperative of the unattested verb schanugliar — see schanuglian. |
| infligì | 1 | 2:49 | UNATTESTED | infliger is no paradigm lemma; no PG headword. |
| abundaivel | 1 | 2:58 | UNATTESTED | -aivel coinage on abundanza/abundant; not in inventory. |
| umilmain | 1 | 2:58 | REGULAR | -main adverb on attested umil; pattern as voluntariamain/gistamain. |
| disubedientscha | 1 | 2:60 | UNATTESTED | Coined abstract noun; notes-M §3 themselves record 'disubedientscha not attested'. |
| tschaguolas | 1 | 2:61 | UNATTESTED | PG simplex tschagula is glossed 'Ente' (duck) / 'tschagula dubla' — the onion sense is not PG-carried for the simplex; rmwiki occurrence is corroboration only, which the attestation audit bars as sole authority. Sense hazard at 2:61 ('onions'). |
| pejor | 1 | 2:61 | UNATTESTED | Latin/Italian comparative loan; PG superlative seat is 'il pir'. |
| disubedì | 1 | 2:61 | UNATTESTED | Coined verb disubedir, pp (family: disubedin). |
| sabeans | 1 | 2:62 | ATTESTED | Master's carried name form (2:62 'the Sabeans'), per the Names policy. |
| deterrenza | 1 | 2:66 | UNATTESTED | Abstract coinage at 2:66; no PG seat. |
| udeva | 1 | 2:75 | UNATTESTED | udir Imperfect stem is udiv- (PAR: udiva); udeva is the wrong stem. Notes-M steering holds the udiva line. |
| disturscheva | 1 | 2:75 | UNATTESTED | disturscher is no paradigm lemma; no PG headword. |
| revelan | 1 | 2:77 | UNATTESTED | revelar Preschent 3pl is reveleschan (PAR, -esch class). |
| rescattais | 1 | 2:85 | UNATTESTED | Verb form of the unattested rescat family at 2:85 ('you ransom them'). |
| assignads | 1 | 2:85 | UNATTESTED | assignar family — see assignar. |
| imposturs | 1 | 2:87 | UNATTESTED | Noun coinage; PG impost- seats are impostar/imposta (different words). |
| smaledì | 1 | 2:88 | UNATTESTED | smaladir Particip Perfect is smaladì (PAR); vowel coinage. |
| engianan | 1 | 2:9 | UNATTESTED | engianar Preschent 3pl is engionan (PAR). |
| tramessess | 1 | 2:90 | UNATTESTED | trametter Cundiziunal stem is tramettess- (PAR). |
| disubedin | 1 | 2:93 | UNATTESTED | See disubedì. |
| giavischus | 1 | 2:96 | UNATTESTED | -us adjective coinage on PG giavisch (noun). |
| putgaders | 1 | 2:99 | UNATTESTED | See putgader. |
| ‹Dieu | 1 | 67:9 | ATTESTED* | Word Dieu attested (PG/HUN); the ‹ is batch N's single-guillemet artifact (Gate 6). |
| ‹sche | 1 | 68:28 | ATTESTED* | Word sche attested (glossary §E); artifact as above. |
| mo› | 1 | 68:28 | ATTESTED* | Word mo attested (PG 'mo — allein'; glossary §E); artifact as above. |
| ‹Dumandai | 1 | 71:10 | ATTESTED* | Dumandai is a dumandar paradigm form (PAR); artifact as above. |
| ‹Nus | 1 | 72:1 | ATTESTED* | Word Nus attested (glossary §E); artifact as above. |
## Gate 4 — SENSE ADJUDICATION: **FAIL**

Form is not sense; three seats carry an attested form with the wrong
meaning, and they are the *marvezza* shape exactly.

**(a) The wonder seats.** PG, `entries_RG-DE.txt`, s.v. *marvezza*:
"marvezza — Steifheit"; "marvezza — Starre"; "marvezza da fraid —
Kältestarre"; "marvezza da cadaver / da mort — Leichenstarre". The
word means stiffness/rigor. It is seated for "wonder" at:

- **10:2** — "È quai ina **marvezza** per il pievel…" (Master: "Is it
  a **wonder** to the people…"). Defect confirmed.
- **13:5** — "la vaira **marvezza** è lur dir" (Master: "the real
  **wonder** is their saying"). Defect confirmed — and the same verse
  opens with the correct verb ("Sche ti ta **smirveglias**"), so the
  verse contradicts itself.
- **12:31** — "èn els stads plain **marvezza** dad el" (Master: "they
  **marveled** at him"). A third seat, found by the checker's own
  grep; not in the commissioned pair but the same defect.

**Repair (all three): the *smirvegl* family** — PG "smirvegl —
Erstaunen, Verwunderung"; "sa smirvegliar — staunen, sich wundern" —
which the book itself seats correctly at 34:15 ("era ina smirvegl"),
37:12, 38:4, 43:48, 45:5, 50:2, 53:55, 53:59, 11:73 and throughout
the Surah 55 refrain.

Every other wonder/marvel seat in the book was grepped and read
(*smirvegl*, *surpraisa*, *miracul* families):

- *smirvegl* family: correct at every seat read (list above).
- *surpraisa* (7:63, 7:69 for "wonder/surprised"; 5:100, 9:55, 9:85
  for "impress"): attested and sense-adjacent — surprise for wonder
  is a weakening, not a failure; the "impress" seats are
  sense-carried. No repair required; noted.
- *miracul* seated for the Master's "**wonders**" at **17:12** ("two
  wonders" → "dus miraculs"), **31:31** and **40:13** ("His wonders"
  → "Ses miraculs"): a systematic sense shift — wonders are not
  necessarily miracles — WEAKENED, repair owed (seat *smirvegls* or
  *segns* per context). Where the Master says "miracle(s)" *miracul*
  is correct (10:20, 13:7, 13:27, 29:50, 54:2, 6:109, 7:103, 79:20…).
- *meraviglia* at 2:259: form and family both fail (Gates 2–3).

**(b) Batch M's flagged seats** (notes-M §5, graded against the
shipped text):

- **54:9 *rebattì*** — "ed el è vegnì rebattì" for "and he was
  rebuked". The pp traces to the *rebatter* paradigm/inventory, as
  the notes claim; no PG headword under that spelling was found by
  the checker either. Sense "rebuffed/driven back" fits the seat.
  **CARRIED, with the flag the notes themselves raise** — form
  attested by paradigm, gloss unverified. No repair required.
- **54:31 *Bragim*** — "in singul Bragim" for "a single Scream". PG
  *bragim* = "Geheul(e), Weinen" (howling, weeping). A great cry,
  not a scream. **WEAKENED**, disclosed in the notes; the
  approximation is logged and no closer attested form was found by
  the checker. Accepted as a logged approximation; no repair
  required beyond the log, which exists.
- **53:23 *olma* for "ego"** — "quai che l'olma desiderescha" for
  "what the ego desires". *olma* is PG "Seele" (soul). **WEAKENED**
  sense shift (ego→soul), disclosed in notes-M §3 with its reason.
  Accepted as logged; the Master's psychological term is not carried.
- **55:17 *Orients/Occidents*** — "Segner dals dus Orients e Segner
  dals dus Occidents" for "Lord of the two Easts and Lord of the two
  Wests". Both stems are inventory forms; the plural formation is
  regular; the east/west sense is the ordinary one. **CARRIED**
  (the notes' "gloss not separately verified" flag is honest and the
  sense is not in real doubt).
- **57:26 *lingia*** — "ed avain mess en lur lingia il dun d'esser
  profet" for "established in their line Prophethood". *lingia* is
  an inventory form; the lineage sense is the ordinary Romansh one.
  **CARRIED**, gloss-unverified flag noted as in the notes.

**(c) Twenty further whole verses read for wrong-sense inventory
forms** (checker's choice, from the Gate 2 random sample): 3:10,
18:4, 20:129, 44:19, 8:46, 10:4, 19:75, 16:43, 18:56, 5:40, 9:90,
9:107, 96:1, 12:76, 3:42, 53:3, 92:16, 8:75, 83:28, 34:52. **No
wrong-sense inventory form of the *marvezza* shape was found in any
of the twenty** — a clean bill for this sample, earned: e.g. 10:4
*baiver* as noun ("ina baiver d'aua buglienta") is the attested
verbal noun doing honest work; 9:107's *lieu da spia* for "outpost"
is a descriptive approximation, not a false friend. The weakenings
at 27:66, 37:18, 38:46, 68:49 found in Gate 2 are sense *flattenings*
of attested words, not false-friend seats, and are counted there.

One further false-friend hazard found by the checker, counted in
Gate 3: **conducta** (2:44, 2:59, 2:197, "mala conducta" for
misconduct) — PG *conduct* is a conduit/pipe; the abstract
'conduct' sense is not PG-carried. And **tschaguolas** (2:61,
"onions") — PG simplex *tschagula* is glossed "Ente" (duck); the
onion sense is not PG-carried for the simplex.

## Gate 5 — GAP CENSUS: **PASS**

Recounted independently from the store: **32 markers, all
⟦GAP: jinn⟧, no other GAP term exists** (regex census over all
6,236 verses; agrees with `verify-report.json`: `gap_total: 32`,
`gap_census: {jinn: 32}`). Seat list as in the verify report
(6:100, 6:112, 6:128, 6:130, 7:38, 7:179, 11:119, 15:27, 17:88,
18:50, 27:17, 27:39, 32:13, 34:12, 34:14, 34:41, 37:158 ×2, 41:25,
41:29, 46:18, 46:29, 51:56, 55:15, 55:33, 55:39, 55:56, 55:74, 72:1,
72:5, 72:6, 114:6). Five of these seats (6:100, 27:17, 27:39, 34:12,
34:14) are where the Master says "sprites" for the same beings; the
GAP is seated there too, which is the honest treatment.

*demuni* check: *demuni/demunis* occurs at exactly two seats —
**27:10** (Master: "as though it were a **demon**") and **38:37**
(Master: "And the **demons**—every builder and diver"). **At no seat
where the Master has jinn (or sprites) is *demuni* seated.** The
fence holds.

## Gate 6 — FENCES AND FIXED FORMS: **FAIL (quote normalisation only; every other fence PASS)**

- **Basmalah: PASS.** 1:1 in the store is exactly "En num da Dieu,
  il Buntadaivel, il Misericordaivel." — character-for-character the
  fixed form in BUILD-SPEC.
- **Segner / signur / patrun split: PASS.** 864 seats carry *Segner*;
  the checker tested every one against the Master — **zero** *Segner*
  seats where the Master lacks "Lord/God". Human seats verified by
  sample: 12:39 "differents **signurs**" (diverse lords), 12:41/12:42/
  12:50 "**patrun**" (the master in Joseph's story), 51:39 "signurs
  da guerra" (warlords), 2:286 both seats in one verse ("nos Segner e
  Patrun" for "our Lord and Master" — split by sense, as notes-A
  log; the *nos* form itself is a Gate 3 repair).
- **Rule A (almosna, no rate): PASS.** 24 *almosna* seats; none
  attaches a rate, percentage or fraction. (The two regex hits for
  number-words near *almosna* are 22:41 "l'almosna regulara" —
  *regular* alms, the Master's own sense — and 51:19 "ina part per
  quel che dumandava almosna", the Master's own "a share" wording.
  Neither is a rate.)
- **No "first/emprem" claim: PASS.** Zero occurrences of *emprem*,
  *emprema* or "first" as a claim in the store. In the pack texts,
  every "first" occurrence is either Bible-history fact in
  BIBLE-CONTROL-VERIFICATION-2026-11-27.md (the first Romansh Bible
  translations — cited historical fact about other books, not a claim
  for this one) or a quotation of Master verse content in the batch
  notes ("the first time", "the first day"). No first-ever claim for
  this translation anywhere.
- **Disjointed letters: PASS.** 2:1, 3:1 "Alif, Lam, Meem."; 19:1
  "Kaf, Ha, Ya, Ayn, Saad."; 36:1 "Ya, Seen."; 42:1 "Ha, Meem.";
  42:2 "Ayn, Seen, Qaf." — each identical to the Master.
- **Quote style: FAIL — normalisation owed.** The book's house style
  is the guillemet «» (Batches A, B, C, F, G, H, I, J, K, L, M, O, P).
  Census by batch file, counted by the checker:
  - **Batch D: 367 curly quotes (“ ”)**, 0 guillemets → normalise
    367 characters to «».
  - **Batch E: 528 straight quotes (")**, 0 guillemets → normalise
    528 characters to «».
  - **Batch N: 4 single guillemets (‹ ›)** at 67:9, 68:28, 71:10,
    72:1 (the source of the ATTESTED\* tokens in Gate 3) → normalise
    to «».
  Total normalisation owed: **899 quote characters across 3 batches.**
  (Store-wide census for reference: « 1,392, » 1,392, " 528, ” 184,
  “ 183, ‹ 4, › 4.)

## Gate 7 — NOTES AUDIT: **FAIL for Batch A; PASS for Batches B, I, M**

Three batches sample-verified against the shipped JSON, plus M in
full at Gate 2/4:

- **Batch A (notes-A.md): FAIL.** The clause maps exist (the file is
  thorough; its 2:282 and 2:34 maps match the shipped text — the
  2:34 map itself prints "«As terrarai davant Adam»"). But the notes'
  form self-audit is false on the record. It claims the 131 exception
  types are "each a regular inflection or derivation of an attested
  lemma on the patterns of reference/key-paradigms.md… none is a
  borrowing from German, Italian, French or a sister idiom". Gate 3
  shows the contrary, type by type: *dschai/dschais* are the
  Sursilvan spellings (PAR: *schai/schais*); *vos/nos* are the
  Sursilvan possessives (PG: *voss/noss*); *meraviglia* and *orgogli*
  are Italian; *traits* is French; *surplus* and *end* are
  English/French loans; *proclaman, navigan, revelan, engianan* are
  not the paradigm forms of their lemmas (PAR gives the -esch
  presents). The exceptions list itself is honestly printed — every
  suspect type is there to be found — but the verdict the notes pass
  on it does not hold.
- **Batch B (notes-B.md): PASS.** Clause maps exist (756 map lines);
  14 of 15 sampled Romansh fragments from the maps match the shipped
  store text verbatim (the one mismatch is punctuation-level).
- **Batch I (notes-I.md): PASS.** Clause maps exist; 15 of 15 sampled
  fragments match the shipped text. Its self-screen narrative (121
  first-round suspect types worked to clean in fix rounds) is
  consistent with the store: no Batch I token appears in the Purple
  suspect list.
- **Batch M (notes-M.md): PASS, and the strongest notes in the
  pack.** Its clause maps verify (58:22 and 57:27 fragments match
  the store character-for-character at the sampled phrases); its §5
  uncertainty flags (54:9, 54:31, 53:23, 55:17, 57:26) are exactly
  the seats an independent checker would flag, and its steering
  record correctly names Batch A's failures (*fand/prendond*-type
  coinages, *rescat*, synthetic futures, the *udiva* line) as things
  to avoid. Where M's notes and A's notes conflict, M is right.

---

## REPAIR LIST

Seat → current text → required fix → ground. Token-type repairs are
listed once per type with their seats; applying them touches 211
tokens, essentially all in Surah 2 (Batch A).

### R1. Unattested token types — 120 types, 211 tokens (Gate 3 table)
For every type marked UNATTESTED in the Gate 3 table: replace with
the paradigm form named in its ground (e.g. *proclaman* →
*proclameschan*, PAR proclamar; *fand* → *faschond*, PAR far;
*prendond* → *prendend*, PAR prender; *udeva* → *udiva*, PAR udir;
*suondass* → *suandass*, PAR suandar), or, where the lemma itself is
unattested (*cumplir, rescat, spander, entaupar, assignar, exhortà,
dedicà, directà, desavuà, infligì, guastà, dannà* families and the
coined nouns/agents/adjectives), re-render the clause on attested
forms or GAP-mark, per BUILD-SPEC. Highest-frequency items:

- All Surah 2 seats → *vos* → **voss** (26 seats) → ground: PG
  "voss, vossa — euer".
- All Surah 2 seats → *nos* → **noss** (14 seats) → ground: PG
  possessive noss/nossa.
- 2:110, 2:187, 2:195, 2:223, 2:235, 2:281, 2:284, 2:44 (+1) →
  *vussezs* → **vus sezs** → ground: attested two-word reflexive,
  used elsewhere in the book.
- 2:34 → *terrarai* → **terrai** (imperative) → ground: PAR terrar
  Imperativ pl. "terrai!"; Master's mood is imperative.
- 2:48, 2:123, 2:184 *rescat* and 2:85 *rescattais* → re-render on
  attested forms (the Batch M 57:15 road: *pajament per vossa
  liberaziun*) → ground: no PG/PAR seat for rescat.
- 2:259 → *meraviglia* → **smirvegl** family → ground: Gates 3–4.

### R2. Wrong-sense seats — 6 seats
- 10:2 → "ina marvezza" → **ina smirvegl** → ground: PG marvezza =
  Steifheit/Starre; PG smirvegl = Erstaunen/Verwunderung.
- 13:5 → "la vaira marvezza" → **il vair smirvegl** → same ground.
- 12:31 → "plain marvezza dad el" → re-render on *sa smirvegliar*
  → same ground.
- 17:12, 31:31, 40:13 → *miraculs* for the Master's "wonders" →
  **smirvegls** (or *segns* by context) → ground: Gate 4(a).

### R3. Fidelity weakenings — 8 seats (Gate 2)
- 5:2 → restore "aggression" and "conscience" as distinct seats
  (not *far donn* / *tema da Dieu* twice over).
- 5:45, 5:89 (×2), 5:95 → *perdun/perdunar* for the Master's
  "atonement/atone" → seat an atonement word distinct from
  forgiveness, or log the flattening in the notes as a disclosed
  loss (currently unlogged).
- 24:31 → "cors zuppads" → restore "nakedness".
- 33:53 → "paraid" (wall) → restore "screen".
- 37:18 → "fatgs pitschens" → restore "subdued".
- 27:66 → "na vesan betg" → restore "blind".
- 68:49 → "plain da vargugna" → restore "despised".
- 38:46 → "elegì / Chasa" → restore "distinguished / the Home".

### R4. Quote normalisation — 3 batches, 899 characters (Gate 6)
- Batch D: 367 curly “ ” → « ».
- Batch E: 528 straight " → « ».
- Batch N: 4 single ‹ › → « » (67:9, 68:28, 71:10, 72:1).

### R5. Minor
- *Vae* (14 tokens, e.g. 36:30, 36:52, 77:15) → replace the Latin
  interjection with an attested Romansh rendering of the Master's
  "Alas/Woe", or log it in the glossary as a disclosed device; it is
  currently neither.

**Repair count: 120 token types (211 tokens) + 6 wrong-sense seats +
8 fidelity seats + 3 batch quote jobs (899 characters) + 1 minor
item (Vae, 14 tokens) = 135 repair line items.** Several R3 seats
overlap R1 types (e.g. 2:259 sits in both); no item is double-counted
in the 135.

---

## Closing recommendation: **DO NOT LAND**

The lane was built against the Veps record, and in the ways that
killed Veps's long verses it has succeeded: the checker found no
fidelity collapse in 136 verses read clause by clause, no pronoun
substitution, a clean GAP census, an exact canonical grid, and
honest, verifiable notes in the later batches. What it did not
escape is the Veps lane's other signature — unattested and borrowed
forms — seated wholesale in Batch A before the desk steering
tightened, and then certified by Batch A's own notes under a claim
("none is a borrowing") that the sources contradict. The Form Law is
the lane's first law; a book carrying 120 unattested types, three
*marvezza* seats that say "stiffness" where the Master says
"wonder", and 899 unnormalised quote characters has not earned a
PASS, and this checker will not soften that.

The path back is short and mechanical: Batch A (Surah 2) re-screened
and repaired type by type against the paradigm tables — the same fix
rounds Batches I and M already ran on themselves — the six
wrong-sense seats re-seated, the eight fidelity weakenings restored
or logged, and the three quote batches normalised. On the evidence
of Batches B–P, the lane's own process can do every one of those
repairs. Land it after they are done and re-checked, not before.
