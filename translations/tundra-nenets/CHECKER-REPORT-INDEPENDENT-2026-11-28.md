# Independent checker report — Tundra Nenets Quran draft (2026-11-28)

Checker: independent subagent. I built none of this text. I did not edit,
land, shelve, commit, or push anything. Every count below is from code I
wrote and ran against `verses-store.json` and `master-verses.json` in this
lane on 2026-11-28; the desk's figures were not trusted or reused.

## VERDICT: FAIL — not landable as DRAFT — NOT PUBLISHED

Per gate: Gate 1 Canonical **PASS**. Gate 2 Codepoints **PASS**. Gate 3 GAP
**PASS**. Gate 4 Fidelity **FAIL** (7 named verses in a 48-verse sample).
Gate 5 Attestation **FAIL** (8 condemned tokens, named below with seats).
Gate 6 Lect fence **FAIL** (the н-initial "what" form in 199 seats).
Gate 7 Fences/paperwork **PASS**. The fidelity failures are confined to
named verses, listed precisely in Gate 4; the attestation and lect failures
are likewise confined to named tokens and seats. Nothing in this report
fails the book on a candidate I did not verify firsthand.

---

## Gate 1 — CANONICAL: PASS

My flattening of `master-verses.json` (nested by surah) gives 6,236 Master
seats. The store holds 6,236 seats; the seat sets are exactly equal
(`set(store) == set(flat Master)`), and the per-surah counts match at all
114 surahs (no mismatching surah in my Counter comparison). Seat 1:1 is
exactly `Нумʼ нимня, Сянаваʼ Ерв, Сянана.` No seat contains the string
"redacted" (the two Master placeholder seats, 39:7 and 48:8, are rendered
for their surrounding sense — see Gate 4, both pass). No empty seats.

## Gate 2 — CODEPOINTS (Robert's ruling): PASS

Machine counts over the whole store, by codepoint:

- U+0027 (ASCII apostrophe): **0** occurrences, 0 seats.
- U+2019 (curly apostrophe): **0** occurrences, 0 seats.
- U+02B9 (ʹ): **0** occurrences, 0 seats.
- U+02BC (ʼ): **18,527** occurrences, present in 5,302 seats.
- U+02EE (ˮ): **41,348** occurrences, present in 6,013 seats.

No seat contains a forbidden codepoint, so no seat is named under this gate.

## Gate 3 — GAP: PASS

My recount: **101 seats** carry a GAP marker; **115 markers** in total.
Term census from my own regex over the store: hypocrite 36, jinn 32,
camel 16, adultery 14, pilgrimage 9, usury 7, polytheist 1. Every one of
these seven terms is on the standing list in glossary §F (pilgrimage, jinn,
hypocrite, adultery, usury, camel, polytheist). No other GAP term occurs
anywhere in the store.

I sampled GAP seats against their Master verses (2:158, 2:275, 2:276,
2:278, 3:97, 3:130, 5:1, 5:95, 6:100, 7:40, 51:56, 54:27, 57:13, 63:1,
65:1, 72:1, among the seats my code listed). In each sampled seat the
GAPped item is the standing category noun itself (e.g. 7:40 camel, carried
as `⟦GAP: camel⟧` inside an otherwise rendered verse; 63:1 hypocrite;
72:1 jinn), and the rest of the verse is rendered on ordinary vocabulary.
I found no seat where ordinary vocabulary was GAPped instead of rendered.
Note in the same breath: several GAP seats separately fail Gate 4 on
compression (2:275, 3:97) — that is a fidelity failure of those verses,
not a GAP-policy failure; the markers themselves are correctly used.

## Gate 4 — FIDELITY: FAIL

Fresh sample of **48 verses**, drawn by me, stratified as required:
at least 5 from each batch (A 1–4: six; B 5–9: five; C 10–16: five;
D 17–22: five; E 23–28: five; F 29–37: five; G 38–49: six; H 50–67: five;
I 68–84: five; J 85–114: six — the full list is the table below);
**20 verses over 40 Master words** (requirement: at least 15); and all
eight crew-flagged seats (2:255, 4:11, 4:12, 24:35, 31:16, 31:19, 68:42,
90:9, 97:3 — nine seats counting 4:11–12 as two). Each verse was read
clause by clause against the Master. Compression in Nenets syntax was
passed wherever every content word was carried; a verse that drops
content fails.

### Passes (41)

1:2, 5:1, 6:151, 7:40, 8:2, 9:60, 10:62, 12:4, 13:2, 14:1, 15:9, 17:23,
18:110, 19:64, 20:130, 21:107, 22:78, 24:35, 25:74, 26:227, 27:65, 28:88,
30:21, 31:16, 31:19, 34:3, 36:58, 37:182, 39:7, 40:7, 42:11, 46:33,
48:8, 49:13, 50:16, 52:21, 55:26, 57:27, 59:7, 60:10, 63:1, 65:1, 66:6,
69:1, 71:1, 72:1, 75:1, 78:1, 82:1, 85:1, 88:1, 90:9, 95:1, 97:3, 99:1,
104:1, 108:1, 112:1. (This list is longer than the failure list because
several batches' extra seats were read while stratifying; the graded
sample is the union, 48 seats minimum satisfied in every batch, with the
additional short seats above also read and passed — each carries every
content word of its Master verse, in several cases in genuinely
compressed Nenets syntax, e.g. 6:151 at 64 Nenets words for 79 Master
words with every prohibition carried, and 60:10 at 85 for 108 with every
clause carried.)

Two flagged seats deserve a note in the same breath as their pass:
24:35 carries every clause of the Light verse (niche, lamp, glass,
planet, blessed olive tree, neither eastern nor western, oil almost
illuminating untouched by fire, Light upon Light, guidance, parables,
cognizance) — it passes fidelity; its word маслина fails Gate 5, which is
a separate gate. 31:16 and 31:19 pass fidelity for the same reason; their
flagged words are ruled on in Gate 5 (горчица attested; осёл condemned).

### Failures (7) — content dropped, quoted

- **2:255 (FAIL).** Master (86 words) includes the epithet "the
  Sustainer" — the glossary §G device for exactly this seat is
  Илевамʼ Пэрта, and it is not used; the Nenets has only "Иледа" (the
  Living). The intercession clause ("Who is he that can intercede with
  Him except with His permission?") is reduced to
  "Хибяхарт пыда табэдавасяда нянанда ни ӈэдараˮ", which carries no
  intercession content word. The knowledge clause ("they cannot grasp
  any of His knowledge, except as He wills") is reduced to
  "Пыдоʼ Нувʼ, яʼ тэнвавамʼ пыда тэнва, пыдоʼ ни тэнваˮ" — pronouns and
  "know" standing in for dropped content, which the fidelity protocol
  expressly forbids.
- **2:282 (FAIL).** The longest verse in the book: 227 Master words
  rendered in 56 Nenets words. Whole clauses are absent: the scribe's
  duty to write as God taught him, the debtor dictating and diminishing
  nothing, the mentally deficient / weak debtor and the guardian
  dictating with honesty, the reminding function of the second woman
  witness, the small-or-large writing duty with the time of repayment,
  the spot-transaction exception, and the no-harm-to-scribe-or-witness
  clause. What remains is a chain of fragments ("хамэди сидя хасаваˮ
  ӈаˮ. сидя хасаваˮ ӈобˮ хасава неˮ ни ӈаˮ. ӈобˮ ӈаˮ. хамэдиˮ ни ӈаˮ.
  ни ӈаˮ.") in which the fractions and witness rules cannot be
  recovered.
- **3:97 (FAIL).** 41 Master words in 14 Nenets words:
  "пуномдˮ ӈаˮ. Abraham ӈаˮ. хэˮӈаˮ. Пыда ⟦GAP: pilgrimage⟧ хард
  Нумʼ миˮвы. Пыда Нумʼ ӈаˮ." Dropped: the evident signs as a clause,
  security for whoever enters, the duty's restriction to "all who can
  make the journey", and the refusal clause's sense ("God is
  Independent of the worlds" is reduced to "Пыда Нумʼ ӈаˮ").
- **4:11 (FAIL).** 109 Master words in 42. The fraction system collapses
  into bare repetitions of "ӈобˮ ӈаˮ" ("one is"): two-thirds, one-half,
  one-sixth, one-third, and the sibling condition are not distinctly
  carried, and the bequest-and-debts clause and the "you do not know
  which are closer to you in welfare" clause are absent. The verse's
  legal content — its whole point — is dropped.
- **4:12 (FAIL).** 116 Master words in 38, same failure shape as 4:11:
  one-half / one-fourth / one-eighth / one-sixth / shared one-third are
  collapsed into repeated "ӈобˮ" fragments, both bequest-and-debts
  repetitions are absent, and "without any prejudice" and "This is a
  will from God" are absent.
- **2:275 (FAIL).** 66 Master words in 17:
  "Satan ⟦GAP: usury⟧ ни ӈэӈгуˮ. Пыдоʼ ⟦GAP: usury⟧ Нумʼ вадеˮӈа.
  Пыда Ерв Нумʼ ӈаˮ. Пыдоʼ ту ӈэӈгуˮ." Dropped: rising as one driven mad
  by Satan's touch, the commerce-versus-usury saying, permission of
  commerce and prohibition of usury as distinct clauses, the
  advice-and-refrain clause with past earnings kept, and the case
  resting with God. (Also noted: "Satan" here is the Latin form, not
  the Master's form or the glossary's Сатана — see Gate 7 note.)
- **68:42 (FAIL, flagged seat).** Master: "On the Day when the Shin
  will be exposed, and they will be called to bow down, but they will
  be unable." Nenets (10 words): "Яляʼ, нэвадоˮ тарпӈгуˮ, пыдоˮмʼ
  туйкумзь хэˮлабтаӈгуˮ, тад пыдоˮ ниˮ пэрӈаˮ." The Shin — the verse's
  subject — is dropped; нэвадоˮ ("their heads") is not the Shin and
  does not carry it. The call to bow and the inability are carried.

The fidelity failures are confined to these seven named verses in my
sample: **2:255, 2:275, 2:282, 3:97, 4:11, 4:12, 68:42**. Every other
sampled verse, including the other flagged seats and long verses in
every batch (57:27, 59:7, 60:10, 65:1 among them), passes. Under the
audit-application standard the desk remediates named seats; I name
these seven, and I flag in the same breath that the failure pattern
(fraction/legal verses and very long verses) warrants the desk checking
unsampled verses of the same shape — that is a recommendation, not a
finding: I did not grade unsampled verses and do not fail them.

## Gate 5 — ATTESTATION ADJUDICATION: FAIL

Method: from `work/purple-untraced.json` (1,752 candidate tokens) I took
the band weighted to the highest counts (the top 80 by count) and ruled
firsthand against `work/lexicon-giellalt.json` (lemma + paradigm class),
`work/attested-tokens.json` (source-tagged IBT / INEL-Tundra / UDHR), and
the running text of `work/ibt-text.txt`. A token absent from the exact-
form index is not condemned for that alone: I searched its stem in all
three instruments before ruling.

### ATTESTED-REGULAR (regular paradigm cell of an attested lemma)

Each token below was traced to the named lemma; source in brackets.

- миˮвы, миˮ, мида, миӈгу, миˮˮ, миваˮ — мись / мипа- "give" family
  [lexicon verb classes; attested forms мипада, мипа- in IBT/INEL index].
- ӈаӈгу, ӈаӈгуˮ, ӈиˮ — ӈась "be" future/aorist cells [attested ӈаˮ, ӈаӈгу
  pattern in IBT index under ӈа- forms].
- маӈгуˮ, маӈгу — маӈг- stem [attested-token index: маӈгбада, маӈгутаˮӈэ,
  маӈгʼ, IBT/INEL].
- ӈобӈгана — ӈобˮ "one" [attested index: ӈобˮ, ӈобʼ, ӈобкана] in the
  поӈгана construction [attested: поӈгана, поӈганандоʼ].
- мальӈг — мальӈг- temporal stem [attested index: мальӈгана, мальӈгы,
  мальӈганандаˮ, IBT/INEL].
- ӈэманзь — ӈэсь "be" infinitive/purposive cell [attested ӈэва, ӈэбта
  family in index].
- лэтраˮ, лэтрадаˮ, лэтрада — лэтрась (TV_ХАДА, "keep, guard, preserve")
  [lexicon verbs.xml; attested лэтраӈгода, лэтрыдаˮ in index].
- вэтыˮ, вэтывы, вэтывыˮ, вэбтаˮ, вэбтавыˮ, вэбта — вэтˮ / вэта- family
  [lexicon: вэтˮ N_МЯДО, вэтабась TV_ХАДАБАСЬ; attested вэтʼ, вэтата in
  index].
- аворˮӈаˮ (as ӈаворˮӈаˮ in the text) — ӈаворць "eat" [lexicon:
  ңаворта, ңавори; attested ӈавор- forms in IBT].
- мэваˮсь — мэсь (IV_ИЛЕ / A_ЕД, "be, take") [lexicon adjectives.xml;
  attested мэсь, мэсьты in index].
- иˮмʼ, иˮʼ, иˮˮ, иˮна — иˮ "water" [glossary §B; attested index: иˮ,
  иˮмня, IBT/INEL] in regular case/possessive cells.
- яхона — я "earth, land" [lexicon; attested я, яханани] locative cell
  on the -хона pattern (cf. падархона below).
- табэдасиˮӈэ, табэдаваˮсь — табэдась (TV_ҢЭДАРА, "show, command")
  [lexicon verbs.xml; attested табэда, табэдаˮ, табэдамбада in index].
- илхана, илкана, илˮ — илесь "live" / илʼ "life" [glossary §B;
  lexicon иле- classes; attested илева, илелоˮма forms in index].
- пэрдась — пэрць (TV_ТИР, "do, make") [lexicon verbs.xml; attested
  пэрӈаˮ, пэрта, пэрць in index].
- садьˮ — ruled ATTESTED-REGULAR with a note: not in the lexicon or the
  exact index under this spelling, but the stem is the "shine / be
  bright" formative seen in the 24:35 context ("Пэ — ӈарка нумгы садьˮ",
  the glass like a brilliant planet); I do **not** condemn it, because
  my stem search did not exhaustively exclude a paradigm source, and
  this report condemns only what was verified. It is recorded here as
  the weakest ruling in this band and a candidate for the desk's own
  paradigm check, not as a pass I certify.
- падархона — падарˮ (N_ВАР, "paper, book") [lexicon nouns.xml;
  attested падарˮ, падаркана, падаркаˮна in index] locative in -хона.
- хамдянаˮ — хамдяʼ (N_ВЫҢО, "servant, slave") [lexicon nouns.xml]
  plural/possessive cell.
- хибэˮ, хибья — хибя (Pron, PRON-INTERR-HUM_, "who") [lexicon
  pronouns.xml; attested хибя, хибяˮ, хибянаˮ in index].
- туйкумˮ — туйкумзь (IV_ҢАРАМ, "bow") [lexicon verbs.xml;
  cf. туйкумбась IV_ХАДАБАСЬ].
- поӈгʼ, поӈгнаˮ, поӈгхад — поӈг "between, among" [attested index:
  поӈгана, поӈгад, поӈгымʼ, IBT/INEL].
- тэбтаˮ, хэтыдоˮ — regular verb cells traced by stem in the attested
  index (тэб- / хэт- forms passim in IBT).
- пуномдинаˮ — пуномдˮ (N_МЯДО, "sign, mark") [lexicon nouns.xml;
  glossary §C standing seat] plural cell.
- пикана, пимʼ — пи "night" stem [glossary/lexicon пи- classes;
  attested пиʼ, пихина in index] case cells.
- тыˮ — ты "reindeer" [attested index: тыˮ passim in IBT/INEL] plural.
- вна — prolative postposition formative [attested index: вна in IBT
  running text passim].
- ихи, ихида — ихи- stem forms attested in the index (ихи in IBT text).
- инзеˮ — инзе- "listen" stem, attested index forms in IBT.
- яндиркана — яндирˮ "world" [glossary §B, lexicon] locative cell.
- тэнзелава — тэнз (N_ХАНО, "people, tribe") [lexicon nouns.xml;
  attested тэнз, тэнзˮ, тэнзхаˮ in index] derivative cell.
- ӈэсондоˮ — ӈэсонд- "until, as far as" formative, attested in INEL
  running forms in the index.
- ӈобнзерˮ — ӈобˮ "one" [index] + нзерˮ manner formative [attested
  ӈобнзерʼ in index].
- сертаваˮсь — сертась "make, do" verb family, attested index forms
  (серта, сертавы passim in IBT).
- табэдава family, эдараваˮсь (ӈэдарась "send", glossary §A family),
  лэтрада family — see лэтрась and ӈэдарась above.

That is over 60 tokens ruled in this band (counting each distinct token
above individually: 63). The great majority of the desk sweep's
high-count "untraced" tokens are exactly what the sweep's design would
produce — regular inflected cells that an exact-form index misses. On
this band, the desk's attestation arithmetic is broadly vindicated.

### DEVICE (glossary §G / notes-logged device on attested parts)

- The §G devices as seated (Нумʼ Вада for revelation, ненэся хибяриˮ for
  the righteous, Нумʼ пунрёбцо for religion, туё- family for worship,
  пуняӈы илʼ for the Hereafter, Падарˮ хибяриˮ for People of the Book)
  are built on the attested parts named in the glossary and are ruled
  DEVICE, not invention. (2:255's failure is that the §G Sustainer
  device was *not* used there — Gate 4, not an attestation defect.)

### CONDEMNED (verified firsthand; token, seats, evidence searched)

1. **маслина** — seat **24:35** ("маслина пя", the olive tree). Searched:
   lexicon (no entry, no маслин- stem), attested-token index (no form),
   IBT running text (0 occurrences of маслин). It is a Russian noun
   seated silently, outside every disclosed stratum in the glossary and
   the attestation audit; notes-E flags it as exactly this risk. Note
   the inconsistency in the same breath: at 95:1 the olive rides
   "Олива пявна" — the book has two different undisclosed treatments of
   the same word.
2. **осёл** — seats **31:19** ("осёлʼ вада") and **62:5**. Searched:
   lexicon (no entry), attested index (no осёл; the only осё- hits are
   посёлок / посёлки, a different word), IBT text (0 occurrences).
   Russian borrowing, undisclosed in the glossary; notes-F and notes-H
   flag it as a checker decision, and no glossary seat was ever made
   for it. CONDEMNED.
3. **жемчуг** — seats **52:24, 55:22, 56:23**. Searched: lexicon (none),
   attested index (none), IBT text (0). Russian, undisclosed; flagged
   in notes-H as "uncertain-stratum". CONDEMNED.
4. **коралл** — seats **55:22, 55:58**. Searched: lexicon (no коралл;
   the near hits are unrelated stems), attested index (no коралл),
   IBT text (0). CONDEMNED on the same ground.
5. **рубин** — seat **55:58**. Searched: lexicon (none), attested index
   (the руби- hits are the verb "chop", a different word), IBT text (0).
   CONDEMNED.
6. **гранат** (in the fruit sense) — seat **55:68** (pomegranates in the
   Paradise fruit list). Searched: lexicon carries only граната
   (N_ХОБ-RUS, Finnish "kranaatti" — a grenade), which does not attest
   the fruit sense; attested index (none); IBT text (0). A Russian noun
   seated in a sense no source attests. CONDEMNED.
7. **кувшин** — seat **56:18**. Searched: lexicon (none), attested
   index (none), IBT text (0). CONDEMNED.
8. **намгэмʼ as written** (н-initial) — purple count 75 for this exact
   form; the stem family occurs in **199 seats** in н-initial spelling
   (my regex `\bнамг` over the store) against 182 seats in the correct
   ӈ-initial spelling. Searched: the attested form is **ӈамгэмʼ**
   [attested index, IBT: ӈамгэ, ӈамгэмʼ, ӈамгэмда, and the lexicon
   pronoun ңамгэхэва / ңамгэхэрт family]. No н-initial form exists in
   the lexicon, the attested index, or the IBT text. As written it is
   the western-type initial-ŋ-less form, which BUILD-SPEC admits only
   where a source labels it dialectal and the seat is logged; no such
   logging exists. CONDEMNED as written (the remediation is mechanical:
   seat the attested ӈамг- forms).
9. **пын** — purple count 98, the single highest-count untraced token;
   seats include 23:28, 23:72, 23:95, 24:43, 24:53, 25:9, 25:10, 25:20
   (60 seats carry a пын- token by my regex). Searched: lexicon pronoun
   inventory (пыда, пыдар, пыдоʼ, пыдиʼ — no пын), attested index (no
   standalone пын; пын- hits are unrelated stems пындась "limp" etc.),
   IBT text (пын occurs only inside place names such as Филиппынʼ).
   No paradigm cell of any attested lemma that I could trace produces
   this standalone form in the senses the verses use ("пын няна мэнаˮ",
   "пын еˮэмня"). CONDEMNED as unattested as seated; if the desk can
   produce the paradigm, this ruling is the one to overturn on evidence.

### Express ruling on the crew-flagged горчица (31:16; also 21:47)

**Not condemned.** горчица **is attested**: the attested-token index
carries горчица, горчицамʼ, горчицаʼ, all source-tagged **IBT**, and the
IBT running text contains the word five times in the mustard-seed
parables (e.g. "горчицамʼ нюбета ӈамдэдʼ сэвкоцяраха"; "горчицаʼ
сэвкоцяʼ ӈар пунрёбцова"). It is a Russian-mediated word naturalised in
the Bible control itself — the same disclosed RUS-via-IBT stratum as
суббота and the судеӈг- family. The crew's flag in notes-F was honest
caution; firsthand checking clears the word. The same firsthand check
clears **суббота** (lexicon N_ҢУДИ-RUS; attested index, IBT) and the
**судеӈг-** family (attested index, IBT, passim).

## Gate 6 — LECT FENCE: FAIL

I sampled 24 seats spread across the book (1:2, 2:2, 5:1, 7:40, 10:62,
13:2, 17:1, 18:110, 22:78, 24:35, 27:65, 31:16, 34:3, 40:7, 49:13, 55:26,
59:7, 63:1, 66:6, 72:1, 78:1, 85:1, 95:1, 112:1) and searched the whole
store for Forest-type stems. Findings:

- No Forest Nenets нешаӈ-type stem occurs anywhere in the store (my
  searches for неша, няша, ӈэша returned no seats), and the sampled
  seats otherwise carry standard Tundra orthography with initial ӈ-
  retained (ӈаˮ, ӈобˮ, ӈэвасэй, ӈэдарась families throughout).
- **The fence fails on the "what" word.** The standard, attested Tundra
  form is ӈамгэ (initial ӈ- retained, per BUILD-SPEC: "Initial ӈ- is
  retained. No other norm may be seated."). In **199 seats** the book
  seats the н-initial form намгэ / намгэмʼ instead — e.g. **5:1**
  ("намгэмʼ Пыда харваˮ"), **5:17, 5:18, 5:20, 5:32, 5:40, 2:7** (first
  seats from my regex listing) — while 182 other seats seat the correct
  ӈамг- form (10:4, 10:21, …). The н-initial spelling is the initial-ŋ
  loss the spec itself names as the western/dialectal deviation, it is
  nowhere labelled or logged as dialectal in the batch notes, and the
  book is internally inconsistent on its most frequent interrogative.
  Named failing seats (sample of the 199): 2:7, 5:1, 5:4, 5:7, 5:17,
  5:18, 5:20, 5:32, 5:40, 5:41.

## Gate 7 — FENCES / PAPERWORK: PASS

- **No "first" claim:** my search of the store text found no "first"
  wording in the Nenets text, and a search of the lane's Markdown, JSON,
  and text files (excluding `sources/`) found "first" only in
  BUILD-SPEC's own prohibition ("No 'first translation' claim is made
  anywhere"). No novelty claim is seated anywhere.
- **Names and scripture titles in the Master's forms (sampled):** my
  counts over the store — Moses 134 seats, Abraham 63, Noah 43,
  Jesus 25, Mary 19, Torah 16, Gospel 5, Psalms 4 — all in the Master's
  forms, as the names policy requires (e.g. 57:27 "Maryʼ ню Jesus",
  "Gospelʼмʼ"). One deviation noted in the same breath: 2:275 seats
  "Satan" in Latin letters where the Master and the glossary's name
  seat give Сатана (passim elsewhere, e.g. 58:19 "Сатанаʼ хибяриˮ").
  This is a single-seat inconsistency inside an otherwise compliant
  sample; it is recorded here and counted in 2:275's Gate 4 failure,
  and it does not by itself fail this gate.
- **Glossary fixed seats (all 10 sampled in the text):** Нумʼ — 1,984
  seats; Туёˮма — 15 seats (10:89, 17:1, …); Пунрёбцо — seated
  (49:11, 59:23; the word family пунрё- passim); Хэбяха — 39 seats;
  судеӈгова — 85 seats; Ябдана я — 48 seats; Яʼ ӈылы — 99 seats;
  Яӈорʼ илелоˮма — 66 seats; ӈэвасэй — 58 seats; суббота — 4 seats
  (2:65, 4:47, 4:154, 7:163). Every sampled glossary seat is seated in
  the text in its fixed form.

---

## Summary for remediation (named seats only)

- Fidelity: re-render **2:255, 2:275, 2:282, 3:97, 4:11, 4:12, 68:42**
  clause-complete (fractions distinct in 4:11–12 and 2:282; the §G
  Sustainer device seated at 2:255; the Shin carried at 68:42), then
  re-check those seats; the desk should also self-check unsampled
  verses of the same long/legal shape before any re-submission.
- Attestation: replace or GAP/device **маслина (24:35), осёл (31:19,
  62:5), жемчуг (52:24, 55:22, 56:23), коралл (55:22, 55:58),
  рубин (55:58), гранат (55:68), кувшин (56:18)**; seat the attested
  ӈамг- forms in the **199 намг- seats**; produce a paradigm for **пын**
  or replace it in its 60 seats. горчица, суббота, and судеӈг- stand
  cleared and need nothing.
- Lect: the намг- correction above is the whole of the lect failure;
  no Forest stem was found anywhere in the book.

Gates 1, 2, 3, and 7 pass on my own counts and firsthand reading.
Gates 4, 5, and 6 fail on the named evidence above. **Overall verdict:
FAIL.**
