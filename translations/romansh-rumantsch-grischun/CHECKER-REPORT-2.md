# CHECKER REPORT 2 — Romansh (Rumantsch Grischun) Quran lane, RE-CHECK after repairs

Independent re-check, 2026-11-27. This checker did not build or repair
any of this text. The first checker's report (`CHECKER-REPORT.md`,
verdict DO NOT LAND, 135 repair items) is the checklist; the repaired
text in `verses-store.json` (6,236 verses) and the repaired batch
files `work/batch-*.json` are the evidence, graded against the Locked
English Master (`master-verses.json`), PG
(`sources/entries_RG-DE.txt`), the paradigm tables
(`sources/rg-paradigms.json`, 3,817 verbs), the attested inventory
(`sources/rg-attested-inventory.json`), rmwiki running text
(corroboration only), the BUILD-SPEC's Form Law and Fidelity Law,
and the two repair logs (`work/notes-A-repair.md` — 209 change
entries counted by this checker; `work/notes-repair-2.md`).

Every screen below was re-run by this checker over the whole store,
not copied from `verify-report.json`. The fresh `verify-report.json`
was read and agrees with this checker's own runs where they overlap.

## Verdict in one breath

**DO NOT LAND.** The repair crews did the large work, and this
report says so plainly: all 120 UNATTESTED types of the first report
are gone (211 tokens), all 6 wrong-sense seats are re-seated, all 8
fidelity items are restored, Vae is gone book-wide, the quote
normalisation is done, and the canonical gate and every fence still
pass with no regression found in the verses read whole. Three
defects remain, and the Form Law — this lane's first law — admits no
exceptions for size. (1) **Colpa** (2:60) and **Colpai** (2:73), the
imperatives for the Master's "Strike", are UNATTESTED: no PG
headword, no paradigm lemma, no inventory form — and an attested
road exists (PAR *batter*, Imperativ "batta!" / "battai!"). (2)
**Laudabel** (2:267, and also 31:12, 34:6, 35:15 — four seats, not
one) is UNATTESTED: PG's attested adjective is **ludaivel**
("anerkennenswert, lobenswert, löblich, rühmlich"); *laudabel* is in
no source and is an Italian/Latin-shaped coinage of exactly the kind
the first report condemned. (3) At **13:16** the Batch E mechanical
quote alternation produced a visibly reversed nested quote pair
(a speech opening printed » and its closing printed «). The repair
crew itself flagged items (1) and (2) in `notes-A-repair.md` and
left them "as shipped"; flagging is not repairing. The remaining
work is three small, mechanical jobs. Land after they are done and
spot-re-checked, not before.

---

## R1 — The 120 UNATTESTED types (Batch A): **REPAIRED, with two capitalised exceptions carried to §6 below**

### Whole-store token screen, re-run by this checker

This checker re-ran the `verify.py` token screen independently over
all 6,236 verses of the repaired store (GAP markers removed, tokens
split on spaces/punctuation/apostrophes, lowercase tokens checked
against the attested inventory). Result: **exactly 7 suspect types
remain** — identical to the fresh `verify-report.json`
(`suspect_distinct: 7`). Zero of the first report's 120 UNATTESTED
types survive. A whole-word search for the first report's signature
failures confirms the screen: *vussezs, terrarai, meraviglia, rescat,
fand, prendond, udeva, proclaman, navigan, revelan, engianan,
dschai, dschais, cumplir, spander, politeist(s), nuncretta, orgogli,
surplus, traits, aggressiun, deterrenza, conducta, entaupar,
smarrids* — **0 occurrences each, book-wide**. Standalone tokens
*vos* and *nos*: **0 occurrences book-wide** (the substring "vos"
survives only inside the attested *voss/vossa/vossas*).

### The 7 remaining suspect types — adjudicated one by one

| Type | Seats | This checker's verdict | Ground |
|---|---|---|---|
| voluntariamain | 2:158, 2:184 | **ATTESTED — confirmed** | PG phrase headword, `entries_RG-DE.txt`: "manchentar aposta/voluntariamain — schwänzen". |
| amicabelmain | 2:231 ×2 | **REGULAR — confirmed** | PG headword *amicabel* ("freundlich, freundschaftlich, gütlich…"); -main adverb on the attested pattern of *voluntariamain*. |
| dretgamain | 2:186 | **REGULAR — confirmed** | -main adverb on PG-attested *dretg*; same pattern. |
| retegniss | 2:251 | **REGULAR — confirmed** | Cundiziunal stem of PAR lemma *retegnair*, per its paradigm table. |
| umilmain | 2:58 | **REGULAR — confirmed** | -main adverb on attested *umil*; same pattern. |
| sabeans | 2:62 | **ATTESTED — confirmed** | The Master's carried name form ("the Sabeans"), per the Names policy. |
| at | 86:1, 86:2 | **ATTESTED — confirmed** | Tokeniser split of the Master's carried name *at-Tariq*, per the Names policy. |

The first checker's adjudication of all seven is **confirmed, none
overturned**.

### Spot-verification of repaired seats (30 seats read against the Master and the sources)

All 30 **PASS** — the replacement at each seat is the paradigm/PG
form named in the first report's ground, and the clause around it is
intact:

- **2:34 — PASS, imperative restored.** Shipped "«As terrarai davant
  Adam»" now reads "«As **terrai** davant Adam.»" — PAR *terrar*
  Imperativ pl. "terrai!"; the Master's imperative mood is restored
  and the synthetic future is gone.
- **2:259 — PASS.** *meraviglia* gone; "Nus vegnin a far ti in
  **smirvegl** per l'umanitad" (PG *smirvegl* = Erstaunen,
  Verwunderung); the unattested noun *baivra* is replaced by the
  book's own *baiver*, and *guastà* by "n'è betg ì a perder". Every
  clause of the long verse is present (hundred years, unspoiled food
  and drink, donkey, bones clothed with flesh).
- **2:61 — PASS** (the GAP added here is graded at §6a). *pejor* →
  *il pir*; *disubedì* → "na han betg obedì"; *tschaguolas* removed.
- **2:235 — PASS.** *end* gone (the clause now reads "u tegnai el
  per vus sezs"); *annunziend* replaced by the *annunziar* gerund
  seated as "annunziond voss engagement"; *entaupai* gone
  ("na scuntrai betg ellas en secret").
- **2:128 — PASS, vos/nos gone.** The verse now reads "**Noss**
  Segner, e fa nus suttamess a Ti, e da **noss** descendents ina
  communitad suttamessa a Ti. E mussa a nus **noss rituals**…" —
  both Sursilvan possessives replaced by PG *noss*, and *rits* by
  attested *rituals*. The first report's mixed-verse defect
  ("nos descendents" beside "noss rits") no longer exists.
- **2:75 — PASS, udiva seated.** "…ina part dad els **udiva** il Pled
  da Dieu, e lura al **sturscheva** cun deliberaziun…" — PAR *udir*
  Imperfect *udiva*; *udeva* and *disturscheva* both gone
  (*sturscheva* = PAR *storscher* Imperfect).
- **2:196 — PASS, gerund seated.** "…faschond diesch en tut" —
  *faschond* is PAR *far* Gerundium; *fand* gone. The *rescat* seat
  is re-rendered "in pajament per la liberaziun" (the Batch M road).
- **2:233 — PASS, gerunds seated.** "…els na commettan betg errur
  **faschond** quai. Vus na commettais betg errur **prendend**
  mammas da tezzar…" — *prendend* is PAR *prender* Gerundium;
  *prendond* and *dannà/dannada* gone.
- **2:9 — PASS, engionan seated.** "mo els **engionan** nagin auter
  che sasezs" — PAR *engianar* Preschent 3pl *engionan*;
  *engianan* gone.
- **2:160 — PASS, proclameschan seated.** "…e **proclameschan**" —
  PAR *proclamar* Preschent 3pl, -esch class; *proclaman* gone.
- **2:261 — PASS.** The nonsense coinage *itgescha* is gone; the
  verse now reads "Dieu **multiplitgescha** per tgi ch'El vul" —
  the multiplication clause is carried on an attested form and the
  sense is restored.
- Further seats read and passed, each with the named replacement in
  place and no collateral damage: 2:14 (*scuntran* for *entaupan*),
  2:15 (*sperdids*), 2:17 (*sumeglientscha*), 2:22 (*mettai* for
  *assignai*), 2:26 (*sviescha*, *turpegia*), 2:30 (*sponder*,
  *declerain Ti sontg*), 2:40 (*accumpli/accumplir*, *cumplir* gone),
  2:44 (*bun agir*, *vus sezs*, *chapis*), 2:48 (*pajament per sia
  liberaziun*), 2:58 (*en abundanza*, *schai*), 2:66 (descriptive
  *exempel che fa temair* for *deterrenza*, logged in the repair
  notes), 2:84 (*sponder*), 2:85 (*pajais per lur liberaziun*),
  2:88 (*smaladì*, *mancanza da cardientscha*), 2:96 (descriptive
  "quels che aduran blers dieus" for *politeists*), 2:104 (*schai*),
  2:107 (*gidanter*), 2:125 (*Tegnì Mia Chasa sontga*; *schanugls*
  noun for the kneel clause), 2:137 (*dispita* for *scissiun*,
  weakening logged), 2:143 (*chaltgogns*), 2:164 (*navigheschan*),
  2:167 (*desditg*; *s'enriclian* clause for *regrets*), 2:184
  (*pajament per la liberaziun*), 2:187 (*bavai*), 2:197 (*mal agir*
  for *conducta*), 2:206 (*superbia* for *orgogli*), 2:219 (*surpli*;
  *bavrondas cun alcohol*, logged), 2:221 (descriptive idol clauses),
  2:227 (*resolvan*-class seated as "resolvan da divorziar" — read
  in the store as "sche els resolvan da divorziar"), 2:230
  (*divorziescha*), 2:236 (*divorziond*), 2:246 (*cumbattessas/
  cumbattessan* with double-t stem), 2:251 (*victorisà*-class and
  *retegniss* standing as adjudicated), 2:264 (*plat* for *lisch*,
  logged), 2:273 (*fatscha* for *traits*, logged), 2:282, 2:283
  (*accumplir* family), 2:286 (*condemna*-class re-rendered;
  *cundanna* gone).

No replacement seated by the Batch A repair was found that is
itself unattested or wrong-sense. The descriptive re-renders where
no attested form exists (*dispita* for schism at 2:137, *plat* for
smooth at 2:264, the deterrent clause at 2:66) are logged in
`notes-A-repair.md` with their nuance loss stated, which is the
BUILD-SPEC treatment. **R1 is repaired — subject only to the three
capitalised forms the repair log itself left standing, graded at
§6b, which are R1-shaped defects and are counted there.**

---

## R2 — The 6 wrong-sense seats: **REPAIRED (all 6)**

Book-wide census by this checker: ***marvezza* — 0 tokens** in the
whole store.

- **10:2 — CARRIED.** "È quai ina **smirvegl** per il pievel…" —
  PG *smirvegl* = "Erstaunen, Verwunderung" for the Master's
  "a wonder". Correct family, correct sense.
- **13:5 — CARRIED.** "Sche ti ta smirveglias — il vair **smirvegl**
  è lur dir…" — noun and the verse's own verb now agree; the
  self-contradiction the first checker found is gone.
- **12:31 — CARRIED.** "…èn els **sa smirvegliads** dad el" —
  re-rendered on *sa smirvegliar* (PAR pp m.pl. *smirvegliads*);
  "they marveled at him" is carried.
- **17:12 — CARRIED.** All three seats in the verse repaired, not
  only the commissioned one: "dus **smirvegls**… il **smirvegl** da
  la notg… il **smirvegl** dal di" for the Master's "two wonders /
  the wonder of the night / the wonder of the day". *miracul* no
  longer stands for "wonder" here.
- **31:31 — CARRIED.** "per vus mussar da Ses **smirvegls**" for
  "His wonders"; the verse's *segns* seat for "signs" stands, so the
  Master's two seats stay distinct.
- **40:13 — CARRIED.** "I è El che mussa a vus Ses **smirvegls**"
  for "He shows you His wonders".

Where the Master says "miracle(s)", *miracul* stands untouched.
**R2 is repaired in full.**

---

## R3 — The 8 fidelity items: **REPAIRED (all 8 CARRIED)**

- **5:2 — CARRIED.** Both seats restored distinctly. Aggression:
  "na vus mainia betg a **l'agressiun**" — PG headword *agressiun* =
  "Aggression, Angriff" (single-g; the double-g *aggressiun* of
  Batch A remains unattested and absent). Conscience: "gidai in
  l'auter en il bun agir ed en **la conscienza**" — PG headword
  *conscienza* = "Gewissen" ("sin onur e conscienza — auf Ehre und
  Gewissen"; "avair buna conscienza — ein reines Gewissen haben").
  The verse's first seat (*far donn* for "violate/harm") and the
  aggression seat no longer share one word, and *tema da Dieu* no
  longer stands for "conscience".
- **5:45 — CARRIED.** "quai vegn a servir ad el sco **expiaziun**"
  — PG *expiaziun* = "Abbüssung, Sühne". Atonement is now a seat
  distinct from *perdun* (forgiveness).
- **5:89 (both seats) — CARRIED.** "**L'expiaziun** per quai è: da
  dar da mangiar a diesch umans basegnus…" and "Quai è
  **l'expiaziun** per la rumper da voss saraments…" — both
  atonement seats restored on *expiaziun*.
- **5:95 — CARRIED.** "U el po **expiar** cun dar da mangiar als
  basegnus" — PAR lemma *expiar* ("abbüssen"). The verse's later
  forgiveness seat ("Dieu perduna quai ch'è passà" — the Master's
  own "God forgives what is past") correctly stands as *perduna*;
  atone and forgive are distinct in the verse, as in the Master.
- **24:31 — CARRIED.** "uffants che n'èn anc betg conscients da la
  **nivadad** da las dunnas" — PG *nivadad* = "Nacktheit, Blösse".
  Nakedness restored; *cors zuppads* gone.
- **33:53 — CARRIED.** "dumandai ellas da davos ina **tenda**" —
  PG *tenda* carries the curtain sense ("tenda da tribuna —
  Bühnenvorhang"; "tenda — Vorhang"). Screen restored; *paraid*
  (wall) gone from this seat.
- **37:18 — CARRIED.** "e vus vegnis a vegnir **umiliads**" —
  PAR *umiliar* = "demütigen, erniedrigen" (to humble/subdue),
  pp m.pl. *umiliads*. Subdual restored; *fatgs pitschens* gone.
- **27:66 — CARRIED.** "els èn **tschorvs** ad ella" — PG
  *tschorv* = "blind" ("tschorv(a) — Blinde(r)"; "vegnir tschorv —
  blind werden"). Blindness restored; the flattened "na vesan betg"
  is gone.
- **68:49 — CARRIED.** "fiss el stà bittà en la terra deserta,
  **spretschà**" — PG *spretschar* = "verachten" (to despise), PAR
  pp *spretschà*; the same word the book seats for "despised" at
  7:18. Despised-by-others restored in place of ashamed-in-himself.
- **38:46 — CARRIED (both words).** "Nus avain **distinguì** els
  cun ina qualitad speziala: la regurdientscha dal **Dachasa**" —
  PG *distinguer* = "auszeichnen, unterscheiden", PAR pp
  *distinguì*; PG *dachasa* = "Heim, Heimat, Zuhause", seated
  capitalised as the Master capitalises "the Home". Distinguished
  and the Home both restored; *elegì* and generic *Chasa* gone from
  this seat.

No descriptive fallback was needed at any R3 seat — every restored
word has the PG/PAR ground named above, each verified by this
checker in the source files. **R3 is repaired in full; no item is
STILL WEAKENED.**

---

## R4 — Quote normalisation: **REPAIRED, with one visibly broken verse (13:16)**

Census re-run by this checker over the whole store and over the
batch files:

- **No “ ” ‹ › characters anywhere** in the store or in any batch
  file A–P (0 of each). Batch D: « 183, » 184, curly 0 (the
  one-character imbalance is the Master's own cross-verse speech
  spanning at 7:16–7:19, preserved character-wise, as logged).
  Batch N: « 72, » 73, single guillemets 0; the four converted seats
  are 67:9, 68:28, 71:10, 72:1, as named.
- **Batch E: « 270, » 258, and zero straight " characters in any
  value** — confirmed on the parsed values, as the work order
  required.
- The 12 odd-count verses in Batch E were logged in
  `notes-repair-2.md` (11:54, 11:57, 11:85, 11:86, 12:8, 12:26,
  12:27, 12:38, 12:40, 13:16, 13:28, 14:36). This checker read
  three of them whole, against the Master:
  - **11:54 — NOT BROKEN.** "«Nus schain mo ch'ina part da noss
    dieus t'ha prendì cun il mal.» El ha ditg: «Jau clom Dieu sco
    perditga… che jau sun senza culpa da quai che vus associais."
    The final speech is unclosed because the Master's speech itself
    continues into 11:55 — faithful spanning, exactly as in Batch D.
  - **12:26 — NOT BROKEN.** Same shape: the witness's speech opens
    with « and runs unclosed into 12:27, as the Master's does.
  - **13:16 — VISIBLY BROKEN.** The verse's quote sequence is
    « » « » « » « » « (nine characters). The last speech — the
    nested "Say, 'God is the Creator of all things…'" — is printed
    **"Di: »Dieu è il Creatur da tuttas chaussas, ed El è l'In,
    quel che Venscha tut.«"**: its opening mark is a closing »
    and its closing mark is an opening «, a reversed pair produced
    by the mechanical per-verse alternation when it met the
    Master's nested quotation. A reader meets two quote marks
    pointing the wrong way in a single verse. **Repair owed at
    this one seat:** seat the nested pair as « … » in the house
    style (or the Master's nesting resolved as the surrounding
    verses resolve it), by hand, not by alternation.

The other eleven logged odd-count verses follow the 11:54 / 12:26
spanning pattern and are not broken. **R4 is repaired except for
13:16.**

---

## R5 — Vae: **REPAIRED**

Census re-run by this checker: ***Vae* — 0 tokens book-wide.**
***Guai* is seated at all 14 named seats**: 36:30, 36:52 (Batch J)
and 77:15, 77:19, 77:24, 77:28, 77:34, 77:37, 77:40, 77:45, 77:47,
77:49, 83:1, 83:10 (Batch O). (The store carries further *Guai*
tokens at seats that were never *Vae* — e.g. 104:1, 107:4, 20:61,
21:14 — which are pre-existing seatings, not part of this item.)
Ground verified in PG by this checker: **"guai! — wehe!"** (also
"guai! — siehe!") — an attested Romansh woe interjection, not a
glossary device and not a loan seated on faith.

Sense graded at three seats:

- **36:30** — "Guai als serviturs." for "Alas for the servants."
  **CARRIED** — woe pronounced over a class, as in the Master.
- **36:52** — "«Guai a nus! Tgi ans ha resuscità da noss lieu da
  ruaus?»" for "Woe to us! Who resurrected us…?" **CARRIED.**
- **77:15** — "Guai sin quel Di a quels che din manzegnas." for
  "Woe on that Day to the liars." **CARRIED** — and the refrain
  seats (77:19–77:49) read identically in shape.

**R5 is repaired in full.**

---

## §6 — NEW ITEMS

### 6a. The onion GAP at 2:61: **census confirmed; the GAP treatment graded ACCEPTABLE but conservative — and the first report's ground for it does not fully hold**

Census re-run by this checker: **33 GAP markers book-wide — 32
⟦GAP: jinn⟧ + 1 ⟦GAP: onion⟧ at 2:61** — agreeing with the fresh
`verify-report.json` (`gap_total: 33`, `gap_census: {jinn: 32,
onion: 1}`). The rest of the 2:61 vegetable list (ervas, cucumeras,
agl, lentiglias) stands on attested forms, as shipped.

On the decision itself, this checker must correct the record it was
handed. The first report stated that PG's simplex *tschagula* "is
glossed 'Ente' (duck)" and that "the onion sense is not PG-carried
for the simplex". That is incomplete on the source this checker
read: `entries_RG-DE.txt` carries, under the simplex headword
*tschagula*, not only "Ente" but also **"tschagula — Zwiebel,
Gemeine Zwiebel, Küchen-Zwiebel"**, "tschagula — Zwiebelknolle",
"tschagula da sem — Steckzwiebel", "sosa da tschagulas —
Zwiebelsauce", "schuppa da tschagulas — Zwiebelsuppe", and further
onion compounds. The onion sense **is** PG-carried for the simplex.
GAP-marking was therefore not the only honest treatment: *tschagulas*
could have been seated on a PG gloss, and the GAP is a disclosed
fidelity loss that the sources did not force.

Grading, plainly: a visible GAP marker is never a Form Law breach —
it is the BUILD-SPEC's own honest device, it is logged in
`notes-A-repair.md` with its reason stated, and a reader is told
exactly what is missing. **The onion GAP is ACCEPTABLE as shipped
and is not, by itself, a bar to landing.** But the desk should know
the seat can be carried: if the three repairs in the verdict are
made, seating *tschagulas* on the PG "Zwiebel" glosses in the same
pass would close this seat at no risk. What may not stand is the
first report's sentence that the onion sense "is not PG-carried" —
on the full PG entry, it is.

### 6b. The three capitalised forms left as shipped: **REPAIR OWED on all three**

The Batch A repair log flags these as "not in the checker's repair
list… left exactly as shipped, disclosed here for the checker's
eye". Disclosure is noted and credited. Adjudication, against PG,
PAR and the inventory, by this checker:

- **Colpa (2:60)** — "«Colpa il crap cun tes fist.»" for the
  Master's "Strike the rock with your staff." **UNATTESTED —
  repair owed.** No PG headword *colpar/culpar* in the strike sense
  (PG's *culp-* family is *inculpar/disculpar/exculpar* — accuse /
  excuse; its *colp-* family is *colportar* — to peddle); no PAR
  lemma; *colpa* is not in the attested inventory. The word's only
  appearance in rmwiki is as a noun ("la colpa" = the fault, in a
  non-RG idiom passage) — corroboration only, which the attestation
  audit bars as a seat, and a noun is not an imperative in any case.
  An attested road exists and is short: **PAR *batter*** ("batter —
  anschlagen, schlagen") gives Imperativ sg. **"batta!"** — 2:60 is
  a singular command to Moses: seat *Batta*.
- **Colpai (2:73)** — "«Colpai el cun ina part dad ella.»" for
  "Strike him with part of it." **UNATTESTED — repair owed.** Same
  ground as Colpa; PAR *batter* Imperativ pl. is **"battai!"** —
  seat *Battai*.
- **Laudabel (2:267)** — "Dieu è Suffizient e Laudabel" for
  "Sufficient and Praiseworthy", and the same epithet at **31:12,
  34:6, 35:15** (four seats book-wide, counted by this checker).
  **UNATTESTED — repair owed.** *laudabel* is in no source: no PG
  headword, no inventory form, zero occurrences in rmwiki. PG's
  attested adjective is ***ludaivel*** — "ludaivel —
  anerkennenswert"; "(fitg) ludaivel — hochlöblich"; "ludaivel —
  lobenswert, löblich, rühmlich, wohllöblich" — built on the
  glossary's own *ludar* (to praise; PG *laud* = praise). *Laudabel*
  is the Latin/Italian shape (*laudabilis / lodevole* family)
  seated silently — the exact act the Form Law names and bars, in
  the exact batch the first report condemned for it. Seat
  *Ludaivel* at all four seats.

These three types escaped both Purple screens for one reason only:
they are capitalised, so the screen files them as name candidates.
They are not names. *Colpa/Colpai* are sentence-initial imperatives
inside quoted speech, and *Laudabel* is a capitalised divine
epithet of the same class as *Perdunant* and *Sapient* — except
that those trace to attested stems and this one does not. The Form
Law covers every word form seated, capitalised or not. **§6b is
the principal remaining defect in the book: 3 types, 6 tokens.**

---

## §7 — REGRESSION SWEEP: **PASS (no regression found)**

- **Canonical gate, re-derived by this checker from the store:**
  6,236 seats; seat set identical to the Master's flattened seat
  set; per-surah counts match the standard grid at all 114 surahs.
  Agrees with `verify-report.json` (`seat_set_equal: true`,
  `per_surah_ok: true`) by an independent route.
- **Basmalah:** 1:1 is exactly "En num da Dieu, il Buntadaivel, il
  Misericordaivel." — character-for-character the fixed form. PASS.
- **Segner split:** 864 *Segner* seats; this checker tested every
  one against the Master and found **zero** *Segner* seats where
  the Master lacks "Lord/God". The 2:128 repair did not disturb the
  split ("Noss Segner" for "Our Lord"). PASS.
- **Rule A (almosna, no rate):** 24 *almosna* seats, the same seat
  list as the first report; none attaches a rate, percentage or
  fraction. PASS.
- **No firstness:** *emprem* — 0 occurrences book-wide. PASS.
- **GAP/fences from the first report:** the *demuni* fence is
  untouched by the repairs (no repair seat touches a jinn seat);
  GAP census is 33 as graded at §6a (32 jinn + 1 disclosed onion).
  PASS.
- **Apostrophes:** 0 bad apostrophes in the fresh verify report and
  on this checker's reading of the repaired seats (U+0027 only).
  PASS.
- **Clause coverage in repaired verses:** this checker read 10
  repaired verses whole against the Master — 2:34, 2:61, 2:85,
  2:196, 2:233, 2:259, 5:2, 5:89, 24:31, 33:53 — and found every
  Master clause carried in each, including the long legal verses
  2:196 (offering, head injury, the three-plus-seven fast, the
  Sacred Mosque household exception) and 24:31 (the full relation
  catalogue). The repairs changed words, not coverage; no verse was
  shortened, merged or thinned by either repair pass. The fresh
  verify report's fidelity screens agree
  (`fidelity_thin_candidates: []`,
  `fidelity_collapse_candidates: []`). PASS.

---

## Remaining defects — the complete list

1. **2:60 *Colpa* → *Batta*** (PAR *batter* Imperativ sg.) —
   UNATTESTED imperative. (§6b)
2. **2:73 *Colpai* → *Battai*** (PAR *batter* Imperativ pl.) —
   UNATTESTED imperative. (§6b)
3. ***Laudabel* → *Ludaivel*** at 2:267, 31:12, 34:6, 35:15 —
   UNATTESTED epithet; PG *ludaivel* is the attested form. (§6b)
4. **13:16 nested quote pair reversed** (» … « for « … ») —
   mechanical-alternation artifact. (§R4)

Not defects, recorded so they are not mistaken for any: the onion
GAP at 2:61 (disclosed, acceptable; seatable on PG's "Zwiebel"
glosses if the desk chooses, §6a); the logged descriptive
re-renders at 2:66, 2:137, 2:219, 2:264, 2:273 (nuance loss stated
in the repair notes, per BUILD-SPEC); the cross-verse quote
spanning in Batches D, E and N (the Master's own spanning,
preserved).

## Closing recommendation: **DO NOT LAND**

The first checker set 135 repair items. This re-check finds 131 of
them repaired and verified, the canonical gate and every fence
intact, and no regression anywhere in the repaired text. That is a
large, honest repair, and the crews' logs state their weakenings
where they made them. But the Form Law is this lane's first law,
written after the Veps failure, and it does not grade on a curve:
a book that still seats two unattested imperatives for the
Master's "Strike" and an unattested Latin-shaped epithet at four
seats — all three flagged by the repair crew itself and left as
shipped — has not finished its repair list, and one verse (13:16)
still shows a reader two quote marks pointing the wrong way.

The path back is now very short: *Batta* at 2:60, *Battai* at
2:73, *Ludaivel* at its four seats, and the nested pair at 13:16
set by hand — six tokens and one verse. (Seating *tschagulas* at
2:61 on PG's onion glosses may ride the same pass, at the desk's
choice; it is not required.) Do those, re-screen, and this lane
lands. Until they are done: **DO NOT LAND.**
