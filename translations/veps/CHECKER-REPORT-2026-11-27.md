# Veps lane — INDEPENDENT CHECKER REPORT (2026-11-27)

Checker pass by an agent that did not build this text. No verse text was
edited. Sources read: BUILD-SPEC.md, glossary.md (§§A–J), ATTESTATION-AUDIT-
2026-11-27.md, LICENCES-RECORDED-2026-11-27.md, work/RECOVERY-TABLE.md,
work/verify-candidates.json, verses-store.json, master-verses.json, batch
notes work/notes-A..H + recovery/fix notes (skimmed in full, grepped for
adjudications), sources/lexicon-wikt.json, sources/rus2vep.json (GiellaLT
dict-rus-vep), GiellaLT lang-vep frequency list. verify.py re-run at the desk.

## Check 1 — CANONICAL: **PASS**

verify.py output (re-run 2026-11-27):

- store seats: 6,236; master seats: 6,236; equal: True
- per-surah mismatches: NONE (against the standard grid in verify.py)
- non-U+02B9 apostrophes: NONE (0 seats)
- 1:1 == basmalah: True — 1:1 = "Jumalan nimel, Armahtajan, Armahtajan."

All four sub-checks pass exactly as specified.

## Check 2 — FIDELITY SPOT-CHECK (64 verses): **FAIL**

Sample: 64 verses — the 20 mandated seats (2:282, 2:183, 2:255, 3:54, 9:3,
12:93, 19:26, 22:27, 24:53, 27:23, 36:60, 39:7, 48:8, 51:56, 69:13,
112:1–4, 114:6) plus 44 verses drawn one per remaining surah spread
(4:83, 5:20, 6:102, 7:167, 8:7, 10:10, 11:106, 13:2, 13:35, 14:7, 15:47,
16:15, 17:65, 18:28, 20:10, 21:12, 23:56, 25:54, 26:18, 28:31, 29:12,
30:36, 31:28, 32:2, 33:73, 34:8, 35:15, 37:162, 38:81, 40:75, 41:4, 42:37,
43:75, 44:26, 45:4, 46:15, 47:3, 49:18, 50:9, 52:19, 53:27, 54:10, 55:70,
56:16, 57:19).

Redaction seats (mandated ruling): the Master carries a literal
"<redacted>" placeholder inside 39:7 ("No bearer <redacted> burden…")
and 48:8 ("a bearer <redacted> good news"). The store contains the
string "redacted" in **zero** seats (grep-verified). 39:7 renders the
surrounding sense ("Ei ükskän heng, kudamb kandab jügedust, voi kanda
toižen jügedust") and 48:8 renders it fully ("Mö oigetim sinun toden
sanujaks, i hüvän sanan tojaks, i endustajaks"). Both seats PASS the
redaction test.

Verses that carry the Master's sense cleanly on attested forms, flagged
constructions, carried names, or visible GAPs include: 2:183, 2:255,
3:54 (meletada device, RECOVERY-TABLE), 9:3, 19:26, 22:27, 24:53 (oath
GAP, table-sanctioned), 48:8, 51:56 (jinn GAP per table; lemboi seat
correctly converted), 69:13 (trumpet GAP, table allows GAP where the
noun is unavoidable), 112:1–4, 114:6, 2:282 (sense carried in full;
minor form notes: kirjutajale uses the -ja agent beside the §J
kirjutai used elsewhere in the same verse, and the "prevent doubt"
clause rides on the SUSPECT kieldä- stem, Check 3), 4:83, 5:20, 6:102,
7:167, 20:10, 21:12, 40:75, 42:37, 46:15, 47:3, 49:18, 53:27, 54:10,
57:19.

Verses where sense is LOST, REPLACED, or the verse collapses into
truncated word-salad (18 of 64 — the failure is systematic, not
isolated):

- **27:23** — Master: a woman ruling over them, given of everything,
  with a magnificent throne. Store: "Minä naine minä hän antud minä
  hän ⟦GAP: throne⟧." Ruling, given-of-everything and magnificent are
  all gone; the sentence is not grammatical Veps prose.
- **36:60** — Master: the covenant with the Children of Adam not to
  serve the devil, their sworn enemy. Store: "Tegi minä ei toivotuz
  sinä, lapsʹed Adam, se sinä ei se hän." Devil and enemy seats absent;
  sense lost.
- **37:162** — Master: "Cannot seduce away from Him." Store: "Jumal
  sanub: nece om tozi." — a different sentence entirely; sense replaced.
- **28:31** — the staff/serpent/Moses narrative collapses to "Minä konz
  hän ku hän minä tegi ei Moses, tulda minä tehta ei varaita, sinä."
- **29:12** — "Ned ken sanuda ned ken uskta, te, minä mö taht grähkad.
  te hö grähkad. hö." — the carry-your-sins proposition is lost.
- **30:36** — "Konz mö antta hö ka konz mi käded hö." — taste of mercy,
  rejoicing, adversity and despair all lost.
- **31:28** — "Lodamine minä vaiše heng. Jumal minä." — creation/
  resurrection as a single soul and Hearing/Seeing lost.
- **33:73** — "Jumal ustavzoitta minä minä minä minä Jumal uskjad, minä
  Jumal armahtai." — hypocrite/idolater/believer men-and-women seats
  replaced by repeated "minä".
- **13:2** — second half garbled ("Hän kaik, i Hän kirjad, se sinä voib
  olda sinun Ižand"); manages-affairs, explains-signs, certainty of the
  meeting lost. Also rides on SUSPECT ilma ("without").
- **13:35** — truncated mid-verse; the sequel-of-the-disbelievers clause
  is mangled ("ka ei uskjad om Tuli" survives only as a fragment).
- **14:7** — broken grammar ("Minä tuleb antta sinä; ka ku sinä oma ei
  kitai"); thanks/increase survives only approximately.
- **15:47** — ill-feelings, hearts, brothers/sisters on couches facing
  one another reduced to "I Mö tuleb kaik - heiden südäimed—velʹlʹad
  i, päle üksʹ toine."
- **16:15** — "lest it shifts with you" and "roads, so that you may be
  guided" lost ("miše ei se sinä; i joged, i, muga…").
- **17:65** — opening seat lost: "varoin Minun, sinä om tobmuz päle
  heid" — "My devotees" is not rendered.
- **32:2** — fragment: "Ozutuz kirj, Ižand." — without-doubt and
  from-the-Lord seats reduced to a noun string.
- **34:8** — garbled; the Hereafter/torment/astray seats survive only
  in part ("mokita, minä").
- **35:15** — fragment: "Sinä ken gollič, Jumal; Jumal." — the poor/
  need-of-God contrast and Rich/Praiseworthy lost.
- **12:93** — partially carried (shirt, father's face, sight) but word
  order is broken and a stray full stop + closing quote sit mid-verse:
  "i se päle minun tat" mod, i hän tuleb hänen nägumine."

Pattern: the failures cluster in later-batch, longer, syntactically
complex verses, where content words are dropped and pronoun tokens
(minä/sinä/hän) are left standing in their place. This is a fidelity
failure of the seated text, independent of attestation: even where
every surviving token is attested, the verse does not carry the
Master's sense. **Check 2 FAILS.**

## Check 3 — TOKEN ADJUDICATION: **FAIL** (28 SUSPECT tokens)

Method: verify.py's screen leaves 3,633 untraced candidate tokens of
8,693 distinct tokens — the screen's stemmer is weak (it misses
ordinary inflection), so every candidate in the adjudication set was
re-tested by hand against the harvested inventory (Wiktionary lexicon,
dict-rus-vep equivalents, GiellaLT frequency list, glossary headwords
and §H/§J constructions), with up to three layers of regular ending
stripping, infinitive restoration, and compound splitting.

Set adjudicated: the 150 most frequent untraced tokens + 50 random
tail tokens (seeded sample). Rulings: 127 ATTESTED-REGULAR or FLAGGED
CONSTRUCTION (representative grounds: händai ×326 — partitive of hän,
BUILD-SPEC pronoun paradigm; sudindan ×89 — genitive of the §H Sudindan
päiv construction stem sudind; sananvedäjan/-jid/-jale — inflections of
§H sananvedäi; olizi/oliz/oliziot — conditional of olda, BUILD-SPEC
-iži-; vie — glossary §F; elʹgat — §J elgeta, dict-rus-vep понимать;
asjad — dict-rus-vep дело → azj, s-spelling noted; täuzin — W täuzʹ;
rinnal — D rind; nečes/nečen — nece oblique stem; čud- derivatives —
§J čud, W; ustavzoitandan — glossary ustavzoitta; joukho, avatud,
pagendsijad, živad, išttuzitte, jügedudeta, päivänlaskmoiden — regular
inflection/derivation/compounding on attested stems).

### SUSPECT table (no attestation found in any harvested source)

| Token | × | Seats (up to 5) | Seems to carry |
|---|---|---|---|
| päiči | 71 | 38:24, 38:65, 38:74, 38:83, 39:3 | "except, apart from" (cf. 51:56 "päiči radta" = except to worship) |
| tyo | 45 | 38:21, 38:22, 38:25, 38:40, 38:47 | postposition "to, towards" (39:7 "Ižandan tyo") |
| päi | 43 | 2:19, 2:258, 3:27, 3:46, 3:58 | free postposition "from" (114:6 "keskes päi") |
| rauh (incl. rauhun) | 13 | 10:10, 20:47, 25:63, 39:73, 43:89 | "peace" — Finnish rauha shape; dict-rus-vep мир → mailʹm / kožmuz, no rauh anywhere |
| hülgäba | 14 | 6:33, 6:39, 6:49, 6:89, 6:150 | "reject, deny" (3sg present) |
| hülgäiba | 21 | 6:5, 6:11, 6:31, 7:51, 7:64 | "reject, deny" (3pl past) — hülgä- stem untraced; Finnish hylätä shape |
| kieldäba | 14 | 2:39, 2:41, 2:91, 2:121, 2:161 | "deny, forbid" — dict запрещать → kelʹta; kield- stem untraced, Finnish kieltää shape |
| kieltiba | 16 | 6:140, 7:165, 21:77, 22:42, 23:26 | "deny, forbid" (past) — same kield-/kielt- family |
| kieldiba | 11 | 2:61, 2:89, 2:102, 2:167, 3:4 | "deny" (past) — same family |
| kieldud | 11 | 2:85, 2:196, 3:50, 4:23, 5:3 | "forbidden, denied" (participle) — same family; load-bearing at 5:3 (forbidden foods) |
| selʹktaks | 25 | 2:109, 2:118, 2:159, 2:187, 2:219 | "clear(ly), become clear" — selʹged "clear" is attested (W), the -kta- stem is not |
| tulnug | 21 | 38:21, 39:32, 39:71, 40:34, 40:35 | past participle of tulda "come" — -nug allomorph: zero -nug forms in the GiellaLT frequency list; norm participle is -nu/-nud |
| sanug | 19 | 52:31, 52:48, 56:49, 61:13, 62:6 | past participle of sanuda "say" — same -nug family |
| usknug | 14 | 39:71, 40:10, 40:12, 40:22, 40:30 | past participle of uskta "believe" — same -nug family |
| kosketanug | 3 | 38:41, 41:50, 50:38 | "touched" — kosk- stem attested (D трогать → koskta), -nug participle as above |
| vedänugoi | 1 | 59:6 | "dragged/brought" — vedäda attested, -nugoi participle as above |
| mörinän | 15 | 6:2, 6:60, 7:34, 7:142, 7:143 | "grumbling, murmuring" (gen.) — dict has mörmötada "mumble"; the noun mörinä is untraced, Finnish murina shape |
| kärzindanke | 15 | 6:34, 7:87, 7:128, 7:199, 8:46 | "with patience/endurance" — attested patience verb is tirpta (§J); kärz- untraced, Finnish kärsi- shape |
| ilma | 14 | 13:2, 16:7, 16:23, 16:25, 16:49 | "without" — dict воздух → ilʹm; ilma as a free "without" postposition is the Finnish form, untraced |
| maistta | 13 | 13:4, 16:94, 16:112, 17:75, 22:9 | "taste" — untraced; Finnish maistaa shape |
| jokččel | 11 | 7:38, 7:134, 8:56, 9:8, 9:124 | "each, every one" — untraced; Finnish jokainen shape |
| hüvästʹtud | 11 | 21:26, 21:50, 22:64, 23:14, 23:29 | "blessed" (participle) — hüvästʹta- stem untraced |
| perindon | 1 | 89:19 | "heritage, inheritance" (gen.) — untraced |
| veka | 2 | 40:8, 44:47 | "take/bring away" (imperative-like) — untraced |
| vällengand | 2 | 3:146 | "weakened" — välleta "loosen" attested; this form untraced |
| kogokoi | 1 | 75:3 | "gathered (people)" — untraced |
| heikendelkoi | 1 | 47:35 | "grow weak" — heikend- untraced, Finnish heikentää shape |
| estai | 1 | 50:25 | "hinderer, preventer" (agent) — est- stem untraced |

SUSPECT count: **28 tokens** (22 distinct stems/families). The pattern
is coherent and serious: a Finnish-shaped stratum (rauh, hülgä-,
kield-/kielt-, kärz-, maistta, jokččel, ilma, mörinä, heikend-) plus a
systematic -nug past-participle allomorph and three free postpositions
(päiči, tyo, päi) carry load in hundreds of seats — exactly the silent
borrowing BUILD-SPEC's GAP policy forbids ("NEVER borrow silently from
Finnish, Karelian, or Russian"). Because unattested forms carry load,
**Check 3 FAILS.**

## Check 4 — GAP CENSUS: **PASS** (with two noted judgment seats)

Machine census: 692 GAP markers in 495 seats; **323 distinct GAP
terms**. Every term tested against the RECOVERY-TABLE STAYS GAP list
and the batch/recovery/fix notes:

- The table's STAYS GAP categories cover the high-frequency terms:
  pilgrimage (12), fasting (14), throne (19), jinn (16), Jews (14),
  Christians (12), camel/she-camel/camels (13), cave (11), curse/cursed
  (16), divorce (8), usury (7), fruit (8), palm (7), adultery (6),
  Sabbath (6), intercession (3), quails (3, per the table's pöud
  correction), sorcery/sorcerer (9, per the velho adjudication), chain
  (3, per the ketju adjudication), silk (3), West (4), wombs (2),
  prisoners (2), shackles (2), martyrs (2), pen (2), pearls/coral/
  crystal/elephant/apes/locusts/manna/donkey/monasticism/Islam/
  Muslims/Judaism/pregnant/menstruation/menopause — all present and
  all on the list.
- The long tail of one-off terms (e.g. shocker 101:1–3, crusher 104:4–5,
  galaxies 81:15, garlic/lentils/onions 2:61, Bahirah/Saibah/Wasilah/
  Hami 5:103) is not on the STAYS GAP list by name, but GAP-marking any
  term with no attested form is the BUILD-SPEC default, and the seats
  are logged in the batch notes (spot-verified: proof/proofs seats
  logged line-by-line in notes-A; oath seats adjudicated in
  notes-A-recovery; measure noun seats adjudicated in
  notes-C-recovery, quoted below). No unlogged GAP term was found.
- Missed-seat test — two judgment seats, both disclosed in the notes
  rather than hidden, so neither breaks the check: (a) **measure**
  (noun, 7 seats: 12:60, 12:63, 12:88, 13:8, 15:19, 15:21, 17:35) —
  the table seats märita as a verb only; notes-C-recovery rules the
  pure noun seats have no attested noun form and stay GAP. A checker
  could argue a märita-derivative, but the logged ruling is defensible
  and visible. (b) **well** (6 seats: 12:50, 16:103, 17:47, 17:55,
  17:96, 18:104) — these are the adverb "know full well", not the noun
  kaiv (W, seated elsewhere); GAP is the honest seat for the adverb.
- **oath** (24 markers) is the largest GAP term not on the STAYS GAP
  list; it is covered by the table's DEVICE entry (antta sana, "where
  the legal-oath sense will not carry, leave GAP; log") and the seats
  are logged. Stands as a logged judgment.

**Check 4 PASSES**: no GAP term was found that the recovery table
seats and the text failed to seat, and no GAP term is unlogged.

## Check 5 — DISCIPLES QUESTION: **openikad MAY seat** (currently GAP — conservative, not an error)

The recovery table conditions the seat on checker verification. The
verification succeeds on three independent harvested sources:

- sources/lexicon-wikt.json contains the lemma **openik** (and
  üläopenik), beside opendai "teacher".
- GiellaLT dict-rus-vep: ученик → **openik** (-an, -oid) — XML entry at
  sources/dict-rus-vep/inc/N_rusvep.xml ("openik (-an, -oid)"), also in
  sources/rus2vep.json.
- GiellaLT lang-vep frequency list (running Veps text, NT-driven):
  openikad 276, openikoile 113, Openikad 94, openikoid 61, openik 60,
  and a full oblique paradigm.

Ruling: **openik is attested** (Wiktionary lexicon + dict-rus-vep +
corpus frequency). The three disciples seats — **3:52, 5:111, 5:112** —
**may seat openikad** under the recovery table's own condition. Their
present ⟦GAP: disciples⟧ markers (left standing by notes-A-recovery
pending this verification) are conservative and honest, not a defect;
seating them is now authorised by the table, not required by this
report.

## Check 6 — FENCES: **PASS**

- C7 ("first" claims): grep of BUILD-SPEC.md, glossary.md,
  ATTESTATION-AUDIT-2026-11-27.md and LICENCES-RECORDED-2026-11-27.md
  for "first" returns exactly one hit — glossary.md §J, "Seated from
  the full harvested inventory after the **first translation pass**" —
  a process description, not a claim that this is the first Veps
  Qur'an translation. No "first" claim about the translation exists in
  any pack-facing file.
- C3 (Uz' Zavet wording): the only Uz' Zavet wording quoted in the
  pack-facing files is the Lord's Prayer citation material recorded in
  the audit (Matvei 6:9–13): "Tulgha sinun valdkund", "tehkaha kaik
  sinun tahton mödhe", "pästa meiden velgad", "kodvusehe", "päzuta
  meid pahaspäi", the prayer title "Meiden Tat — loičend", and single
  forms cited as forms (taivhaline, velgad, päzuta). BUILD-SPEC cites
  tulgha/tehkaha only as jussive-form grammar examples. No Uz' Zavet
  wording beyond those short recorded citation phrases was found.

## Check 7 — ANGEL SEATS: **PASS**

- Machine count in the store (verify.py, regex \bangel): **86 verses**
  — matches the specified aggregate exactly.
- Disclosure: angel is disclosed as corpus-observed and
  dictionary-unattested in ATTESTATION-AUDIT-2026-11-27.md ("NOT
  dictionary-attested in the sources read. Observed in running Veps
  text… Seated as a corpus-attested loan with the observation
  disclosed") and in glossary §H ("corpus-observed loan… every seat
  logged in batch notes"), with the audit's mechanical fallback stated
  (every seat converts to GAP if corpus observation is judged
  insufficient).
- Seat logging: batch notes carry per-batch angel-seat lists (e.g.
  notes-A §"Angel seats (22 verses…)" listing seats individually;
  angel mentions across notes-A/B/C/D/E/F/G/H total 63 lines). The
  logged seats are the batches' own record and aggregate to the same
  population the machine counts at 86 verses.

## Verdict summary

| Check | Verdict |
|---|---|
| 1 Canonical | PASS |
| 2 Fidelity spot-check (64 verses) | **FAIL** — 18/64 sampled verses lose or replace the Master's sense |
| 3 Token adjudication (200 tokens) | **FAIL** — 28 SUSPECT tokens, incl. a Finnish-shaped stratum and the -nug participle family |
| 4 GAP census (323 terms) | PASS |
| 5 Disciples (openik) | MAY SEAT — openik attested (W + dict-rus-vep + freq list); 3:52, 5:111, 5:112 may take openikad |
| 6 Fences (C7/C3) | PASS |
| 7 Angel seats (86) | PASS |

Overall: the lane's canonical frame, GAP discipline, fences, angel
disclosure and disciples handling are sound. The seated text itself is
not yet sound: fidelity collapses in roughly a quarter of sampled
verses, and a stratum of unattested (largely Finnish-shaped) forms
carries load against the lane's own GAP policy. Both failures are in
the text, not in the paperwork.
