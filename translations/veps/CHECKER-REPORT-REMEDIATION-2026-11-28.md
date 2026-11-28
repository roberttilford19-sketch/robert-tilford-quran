# Veps lane — INDEPENDENT CHECKER REPORT ON THE REMEDIATION (2026-11-28)

Checker pass by an agent that did not do the remediation. No verse text
was edited. The remediation desk's claims in REMEDIATION-LOG-2026-11-28.md
were treated as a list to test, not as facts. Sources: verses-store.json
(remediated), work/remediation/verses-store-PRE-REMEDIATION.json (frozen
pre-remediation store), master-verses.json, BUILD-SPEC.md, glossary.md
§§A–K, work/RECOVERY-TABLE.md, sources/lexicon-wikt.json,
sources/rus2vep.json + sources/dict-rus-vep/inc/*.xml (GiellaLT
dict-rus-vep), sources/lang-vep/src/fst/freq.txt (GiellaLT frequency
list). verify.py re-run at the desk; all censuses below were also
recounted mechanically by the checker's own scripts.

## Verdict table

| Gate | Verdict | Strongest single piece of evidence |
|---|---|---|
| 1 Canonical verify | **PASS** | verify.py re-run: store 6,236 = master 6,236, seat-set equal True, per-surah mismatches NONE, non-U+02B9 apostrophes NONE (0), 1:1 == basmalah True, angel seats 86 |
| 2 GAP census reconciled | **PASS** | Checker's own mechanical recount: frozen 495 seats / 692 markers / 323 raw terms → remediated 551 / 760 / 330 raw terms, exactly the log's figures; every claimed term removal, addition and absorbed-seat count reproduced digit-for-digit (see Gate 2) |
| 3 Fences (first-claim / Uz' Zavet) | **PASS** | The manuscript's own front matter carries the disclaimer "No claim is made that this is the first Quran translation into Veps"; the only "first" in any pack file is the glossary's process phrase "first translation pass"; Uz' Zavet wording appears only as the recorded Lord's Prayer citation phrases in ATTESTATION-AUDIT-2026-11-27.md (4 hits), none in the manuscript text |
| 4 Fidelity spot-check (fresh sample) | **PASS** | Fresh 46-verse sample, long-verse-weighted, 20 of them from surahs 12–19 / 27–37 and none of those 20 in the original failed 18: **zero** verses lose or replace the Master's sense (the original pass failed 18 of 64 on the same test) |
| 5 Token adjudication sweep | **FAIL** | The log's headline claim "Zero SUSPECT tokens remain book-wide" is refuted mechanically: **Päiči survives in 9 seats** (38:74, 38:83, 43:27, 44:42, 60:4, 70:22, 70:30, 72:23, 72:27), with further residuals in the jokčč-, kärz-/kärsi-, maist- and free-päi families and an unattested palʹm seat at 36:34 — the token pass systematically missed sentence-initial capitalised forms |

Overall: the remediation genuinely repaired the fidelity failure and
the GAP bookkeeping is exact, but its token claim overstates the
result. Gate 5 fails on a bounded, enumerable residue (roughly two
dozen seats), not on a stratum: the Finnish-shaped families that
carried load in hundreds of seats in the first build now survive only
in the missed capitalised seats named in Gate 5.

---

## Gate 1 — CANONICAL VERIFY: **PASS**

verify.py re-run by the checker, 2026-11-28:

- store seats: **6,236**; master seats: **6,236**; seat-set equal: **True**
- per-surah mismatches vs the standard grid: **NONE**
- non-U+02B9 apostrophes: **NONE (0 seats)** — the log's claim that
  three ASCII apostrophes in surah 27 were found and fixed is
  consistent with this zero result
- 1:1 == basmalah: **True** — 1:1 = "Jumalan nimel, Armahtajan, Armahtajan."
- angel census (regex \bangel): **86 seats** — matches the specified
  aggregate and the log's "unchanged" claim
- checker's own additions: Cyrillic characters in the store: **none**;
  "sspäi": **none**. One correction to the log's §5: its claim "Bare
  'keske': none" does not hold — the free form **keske** stands in
  17:53 ("heiden keske"), 18:93 ("kahden seinän keske") and 34:54
  ("heiden i sen keske"). keske is not the glossary's seated
  postposition (keskes, §F); it reads as an illative-type form of the
  keskes stem. It is a form note, not a canonical failure, and it is
  ruled on again in Gate 5.
- Changed-verse count, checker's recount against the frozen store:
  **2,214 of 6,236** — exactly the log's §1 figure.

## Gate 2 — GAP CENSUS RECONCILED: **PASS**

Checker's mechanical census (regex ⟦GAP: …⟧ over the store; terms
counted raw, as the desk counts them):

| | seats | markers | distinct terms |
|---|---|---|---|
| Frozen build (checker's recount) | 495 | 692 | 323 raw (322 case-folded) |
| Remediated (checker's recount) | **551** | **760** | **330 raw (329 case-folded)** |
| Log's claim | 551 | 760 | 330 |

The figures reconcile exactly. Counting note, stated in the same
breath: the 323/330 figures hold only under raw counting, because
"Sabbath" and "sabbath" are counted as two terms in both stores; a
case-folded census gives 322 → 329. The reconciliation itself is
unaffected.

Term movements — every one tested and **confirmed**:

- Removed: disciples 3→0 (seated openikad, Gate 5), ancestor 6→0,
  lion 1→0 (lev seated at 74:51: "Pageden levaspäi?"), horse 1→0
  (19:52 re-rendered to the Mount: "mägen oiktal bokalpäi" — the
  wrong GAP is gone and the verse now carries the Master's sense).
  The checker's set-difference also shows mouth and weight removed —
  both are claimed by the log under "absorbed" seats (below), so the
  two lists agree in substance.
- Added, with the log's exact counts: tar 3, blessed 5, ants 2,
  ant 1, spider 2, bee 1, hoopoe 1, breastfeeding 1, bush 1,
  bricks 1, pens 1, armor 1, statues 1 — **all reproduced exactly**.
- Absorbed judgment seats, all reproduced exactly: well 6→2,
  measure 7→4, mouth 1→0 (13:14 now renders "suhun" — su "mouth" is
  lexicon-attested), weight 1→0 (18:105 renders jügedus),
  generation 4→3, descendants 5→4, cave 11→9, provisions 5→4.
- Standing-term growth, all reproduced exactly: oath 24→37,
  curse 7→17, jinn 16→27, semen 1→6, dust 1→7, fruit 8→12.
- perindon seat: 89:19 now carries ⟦GAP: inheritance⟧, as claimed
  (inheritance total 1→2, consistent with the re-renders surfacing
  a second seat).
- Assembly check: quran-vep.txt carries 760 markers; the manuscript
  carries 761 string matches, the extra one being the front matter's
  own sentence describing the markers ("760 visible ⟦GAP: …⟧
  markers"), so the manuscript's stated "5,685 fully rendered +
  551 GAP seats = 6,236" arithmetic is consistent with the store.

## Gate 3 — FENCES: **PASS**

(a) "First" claims. Searched: ayah-companion-manuscript-VEP.md,
quran-vep.txt, glossary.md, BUILD-SPEC.md,
ATTESTATION-AUDIT-2026-11-27.md, REMEDIATION-LOG-2026-11-28.md.
Hits: (i) manuscript front matter — "no_first_claim: No claim is
made that this is the first Quran translation into Veps. No such
claim is made for any part of this book." (a disclaimer, the
opposite of a claim); (ii) glossary.md §J — "Seated from the full
harvested inventory after the **first translation pass**" (process
description, acceptable under the task's own rule). No claim to be
the first Veps Quran exists anywhere in the pack.

(b) Uz' Zavet wording. The NT (Pabivus 2006) is named in BUILD-SPEC,
the audit, the licences file and the manuscript front matter as
fact-and-citation only. The recorded citation phrases (Lord's Prayer
material: "Tulgha sinun valdkund", "tehkaha kaik … tahton mödhe",
"pästa meiden velgad", "kodvusehe", "päzuta meid pahaspäi", the
title "Meiden Tat — loičend", single forms taivhaline / velgad /
päzuta) occur only in ATTESTATION-AUDIT-2026-11-27.md (4 phrase
hits). The manuscript text itself contains **zero** of those phrases,
and no other NT wording beyond short citation phrases was found in
any pack-facing file. One non-hit recorded for completeness:
manuscript 53:19 "al-Uzzan" is the Qur'anic name al-Uzza, not Uz'
Zavet wording.

## Gate 4 — FIDELITY SPOT-CHECK: **PASS**

Method and threshold, stated plainly: a fresh sample of **46 verses**
was drawn by the checker (longest Master verses per range, to weight
towards the long verses that collapsed in the first build): 20 from
surahs 12–19 and 27–37, **none of them among the original failed 18**,
22 spread across the rest of the book as the longest verse of their
surahs, plus 4 re-checks of original failures (27:23, 36:60, 33:73,
13:2). The gate passes only if no sampled verse drops content words,
substitutes pronoun tokens for dropped content, or intrudes foreign
sense — the original failure mode. Minor descriptive approximations
that carry the content (of the kind the recovery table itself
sanctions) are noted, not failed. Result: **46 PASS, 0 FAIL.**

Fresh target-range verses (20), all PASS: 33:53 (full household /
screen / never-marry sense carried clause by clause), 33:50 (wives,
dowries, four classes of kinswomen, emigration, self-offering woman,
exclusivity, "to spare you difficulty" all present; note: "those
your right-hands possess" rides on radnikad "servants" — content
present, wording approximate), 18:19, 33:37, 13:31, 13:16, 14:22,
12:100 (note: "throne" rides on the disclosed "valdan päle"
descriptive, audit-sanctioned in the first report), 18:22, 34:33,
33:51, 33:35 (the ten paired classes all present, fasting honestly
GAP-marked twice), 27:40, 18:21, 13:33, 18:82, 28:15, 18:17,
14:9, 13:17.

Spread verses (22), all PASS: 2:282 (checked in full including the
tail: witnesses-on-contract, no-harm-to-scribe-or-witness, "God
teaches you" all present), 73:20, 5:110 (crib / leprous / sorcery
honestly GAP-marked, everything else carried), 24:61 (the full
eleven-house list plus keys and friends, greeting clause present),
22:5 (note: "wombs" rides on koht "belly" descriptive — content
present), 4:102, 3:154, 60:10, 74:31, 58:22, 48:29 (note: scripture
titles carried in the Master's forms "the Torah / the Gospel" per
the names policy; 5:110 prints them without "the" — a consistency
note, not a sense loss), 7:143, 10:24, 9:74, 6:93, 46:15 (weaning
carried as "erigoičend söndaspäi"), 57:27, 8:72, 59:2, 42:15,
47:4, 66:8.

Re-checked original failures (4), all now PASS: 27:23 ("Minä löuzin
naižen, kudamb ohjab heid, i hänele om anttud kaikes, i hänele om
surʹ ⟦GAP: throne⟧" — ruling, given-of-everything, magnificent all
restored), 36:60 (covenant, devil as lemboi, sworn enemy as
"selʹged vihankandai" all restored), 33:73 (hypocrite / idolater /
believer men-and-women all seated; "valehtelijoid" for hypocrites is
approximate but content-bearing), 13:2 (pillars, sun and moon
regulated, manages-affairs, explains-signs, certainty of the meeting
all restored; ilma gone, bare construction used).

One false alarm the checker records so it is not raised again:
"erased" in the Veps text (24 seats) is the Veps indefinite pronoun
"some" (e.g. 37:113 "erased oma oigedad" = "some are righteous";
69:44 "erased sanad" = "some statements"), not an English redaction
artifact. It is not an intrusion.

## Gate 5 — TOKEN ADJUDICATION SWEEP: **FAIL**

### 5a. The 22 original SUSPECT families — book-wide recount

Gone entirely (checker-verified zero in the remediated store):
tyo (45→0), rauh (34→0), hülgä- (49→0), kield-/kielt- (147→0),
selʹkt- (64→0), mörinä (17→0), ilma (14→0), hüvästʹt- (12→0),
perindon (1→0), veka (2→0), välleng- (4→0), kogokoi (1→0),
heikendel- (1→0), estai (1→0), and the batch-C kiälta (8→0).
Singular -nug participles: the family collapses from 75 distinct
forms / 217 tokens to plural -nugoi forms plus sanug (ruled at 5c).

**Still standing — the log's "zero SUSPECT tokens remain" claim is
refuted at these seats:**

- **päiči — 9 seats:** 38:74, 38:83, 43:27, 44:42, 60:4, 70:22,
  70:30, 72:23, 72:27 — all sentence-initial "Päiči …" = "Except …",
  the exact SUSPECT seat-type the log claims was converted to vaiše.
  FAIL at these 9 seats.
- **jokčč- — 8 seats:** Jokččel (kerdal) at 7:38, 7:134, 9:8, 9:124,
  10:12, 10:47 ("every time") and Jokččine / Jokččes at 7:160,
  9:122. The log claims jokčč- → joga/jogahine book-wide; the
  capitalised and kerdal-collocation seats were missed. FAIL.
- **kärz-/kärsi- — 3 seats:** 64:17 ("Jumal om Kitai i **Kärzii**",
  the Forbearing epithet), 73:10 and 76:24 (imperative "**Kärsi**"
  = "be patient"). The tirpta replacement was not applied here.
  FAIL at these 3 seats.
- **maist- — 1 seat:** 44:49 "**Maista!**" (imperative, "Taste!") —
  the mujada/magu replacement was not applied. FAIL.
- **free päi — 9 seats:** 12:24, 12:33, 12:34, 15:34, 19:16, 33:10,
  34:51, 34:52, 34:53 — free päi in "hänehe päi poiš", "täs päi",
  "alhas päi" type constructions. Weaker than the päiči residue
  (several are directional-particle uses beside poiš), but the log
  claims the free form was converted to bound -späi book-wide, and
  it was not. FAIL as a claim; the seats themselves are a form
  defect, not a sense defect.

Pattern, stated for the desk: every residue family survives in
sentence-initial or capitalised form. The token pass evidently
matched lowercase forms only. The residue is bounded (≈29 seats
across five families) and mechanically enumerable — but "zero
remain" is false, and Gate 5 grades the claim as made.

### 5b. Claimed replacements — spot-verified against the sources

- **kelʹta paradigm: VERIFIED.** GiellaLT dict-rus-vep XML,
  V_rusvep.xml: запрещать → "kelʹ|ta (-dab, -zi)", with the worked
  example "kelʹta pipkutand" (which also attests the -nd noun, 5c).
  The form-for-form replacement of kield-/hülgä- seats is seated in
  the store (kelʹdaba, kelʹziba, kelʹta infinitive uses passim).
- **tirpta: VERIFIED.** Wiktionary lemma (glossary §J) and
  dict-rus-vep терпеть → "tirp|ta (-ab, -i)".
- **selʹged family: VERIFIED.** selʹged and selʹgenzoitta are both
  lemmas in sources/lexicon-wikt.json.
- **mujada (for maistta): VERIFIED** as a lemma in
  lexicon-wikt.json; 6:141 → **magu: VERIFIED** (lexicon lemma;
  dict вкус → magu).
- **jogahine: VERIFIED** by corpus — GiellaLT frequency list carries
  jogahine (the lexicon file does not); joga-family replacement is
  seated passim.
- **mir / kožmuz (for rauh): VERIFIED.** dict-rus-vep мир →
  "1) mailʹm 2) (согласие) kožmuz"; mir is a lexicon lemma and the
  glossary (§C) records it as "world, peace (W)".
- **openik at 3:52 / 5:111 / 5:112: VERIFIED and seated.** All three
  seats now read openikad / openikoid; attestation stands on the
  three sources the first checker verified (Wiktionary lemma,
  dict ученик → openik, frequency paradigm openikad 276 etc.).
- **lev at 74:51: VERIFIED and seated** ("Pageden levaspäi?"; lev is
  a lexicon-wikt lemma — W-grade, as the recovery table records).

### 5c. The remediation's disclosed open items — ruled one by one

- kelʹtai — claimed in the log and glossary §K, but the checker
  finds **zero seats** in the store. Not a defect; the disclosure
  overstates what was used. No ruling needed.
- **kelʹtand — SEATABLE.** Stronger than "flagged": the dict's own
  example sentence attests the form ("kelʹta pipkutand"). 6 seats.
- **tirptai / tirptand / tirptajad — SEATABLE** (flagged
  constructions on tirpta, attested; regular -i agent and -nd
  deverbal patterns, kirjutai/sudii precedent). 2 + 11 seats.
- **heitai (50:25, also 33:18) — SEATABLE.** heitta is a lexicon
  lemma ("to prevent, to stop" among its glosses — exactly the
  50:25 "Preventer of good" sense); -i agent regular.
- **selʹgenzoituz (25:33 and the selʹgenzoitus- seats) — SEATABLE.**
  selʹgenzoitta is itself a harvested lexicon lemma, so the -uz
  noun is a regular derivation on an attested stem, not a coinage.
- **libutamine / Libutamižen Päiv — SEATABLE** (flagged; -mine noun
  on the book-attested libuta- stem, uniform across 20+ seats).
- **voittand (28:37, 28:82) — FAIL.** The voitt- stem itself is
  untraced in every harvested source the checker searched:
  lexicon-wikt has no voitta, dict-rus-vep gives победа → vägestuz
  and победитель → vägestai, and no voitt- form appears in the
  dict XML or kaikki file. The family is not confined to the two
  disclosed seats — voitt- forms stand in **24 seats** (12:23,
  12:43, 14:21, 16:116, 28:35, 28:67, 30:3, 30:38 …). A flagged
  construction must sit on an attested stem; this one, on the
  sources harvested, does not. (If a source outside the harvested
  set attests voitta, the desk should cite it into the glossary;
  on the record as it stands the ruling is FAIL.)
- **eläbetai (30:50) — SEATABLE, borderline, as flagged.** Single
  seat ("Kolnuziden Eläbetai", the Reviver of the dead); eläda is
  attested and the causative-agent derivation is regular, but the
  eläbet- causative stem itself is not a harvested lemma. It stands
  only under the flagged-construction disclosure, which the log
  and §K do carry.
- **muštelend (the Reminder) — SEATABLE** as flagged. muštelta is a
  lexicon lemma (glossed "to honour" in the harvested line — the
  desk's "remember/remind" use is a semantic stretch the checker
  notes; the -nd noun formation is regular and the device is
  disclosed and uniform, 12 seats).
- **pidämižen (31:22) — SEATABLE** judgment seat: "the most
  trustworthy handle" rendered as "kaikiš varman pidämižen" (the
  surest grasping) on attested pidäda; sense carried descriptively.
- **Kitketud judgment seats (22:24, 22:64, 23:14, 25:1, 25:10,
  25:61; adjectival 34:18; land at 21:71/81) — SEATABLE as a
  disclosed judgment, with the shift named:** kitta is a lexicon
  lemma ("to thank, to compliment, to praise"), so Kitketud
  "Praiseworthy" is attested-stemmed; rendering the Master's
  "blessed" by the book's Praiseworthy epithet changes the word,
  not the referent, and the log discloses every seat. The four
  seats the desk instead GAP-marked (21:50, 23:29, 24:35, 24:61 —
  checker-verified present as ⟦GAP: blessed⟧) are the honest
  alternative and both treatments are defensible; neither is a
  failure.
- **Absorbed well / measure / mouth / weight seats — SEATABLE.**
  The absorbed seats render on attested forms (13:14 suhun on su
  "mouth", lexicon-attested; 18:105 jügedus for weight), and the
  seats the desk could not carry remain honestly GAP-marked
  (well 2, measure 4). This matches the first checker's own note
  that both were disclosed judgment seats.
- **vinmarjoidenke (36:34) — SEATABLE.** vinmarj is corpus-attested:
  the GiellaLT frequency list carries vinmarjad (×6); vin and marj
  are both attested stems, so the comitative compound is regular.
  **But the same verse FAILS on its other half:** "saduid
  **palʹmidenke**" seats palʹm-, which the checker finds in no
  harvested source (no lexicon lemma, dict пальма → no entry,
  no frequency form), and palm-tree stands on the RECOVERY-TABLE
  STAYS GAP list. 36:34 should carry ⟦GAP: palm-trees⟧ (or the
  standing GAP term) beside the vinmarj seat. FAIL at 36:34.
- **kelastades (69:44) — SEATABLE.** kelastada is attested where
  the remediation's own lookup should have found it: dict-rus-vep
  V_rusvep.xml, лгать → "kelast|ada (-ab, -i)". The gerund form is
  regular. (The verse's "erased sanad" is the Veps pronoun, Gate 4.)
- **Kaclei (25:20) — SEATABLE** as flagged: kacelta is attested
  (lexicon "to watch, to observe"; dict наблюдать → kacelta) and
  -i agent is the book's regular construction. "aiven Kaclei" =
  "ever Watchful" carries the Master's "always Observing".
- **Non-frequency -nugoi forms on attested stems — SEATABLE.** The
  plural -nugoi allomorph itself is frequency-attested (olnugoi 37,
  usknugoi 39, sanugoi 38, tednugoi 15 in the GiellaLT list), so
  extending it to other attested stems (käskenugoi at 57:27,
  kacelnugoi at 57:27, usknugoi at 59:2, etc.) is regular inflection
  of an attested pattern, not invention. The log's normalisation
  note (uskonugoi → usknugoi) is consistent with the store.
- **sanug — split ruling.** sanug stands ×116, overwhelmingly as
  the sentence-initial "Sanug:" = "Say:" imperative of the
  re-renders. The -g- extended stem is paradigm-adjacent in the
  harvested corpus (frequency list: sanugaha jussive, sanugat,
  sanugoi), and the use is uniform; the checker seats it as a
  flagged form rather than failing 100+ otherwise-sound verses.
  **But at 12:80** ("teiden tat om **sanug** teidpäi toivotusen" —
  "your father has taken a promise from you") **and 18:76**
  ("Sinä olet **sanug** minunpäi andaksandandan") sanug is doing
  singular past-participle work — the original SUSPECT -nug
  participle, unconverted. FAIL at 12:80 and 18:76.
- **keske (17:53, 18:93, 34:54) — GAP-grade form note, not failed:**
  an unlisted form beside the seated keskes; the desk should either
  cite it or normalise it. It carries no sense risk.

### Gate 5 verdict reasoning

The remediation's central token work is real and verified: fifteen
of the twenty-two SUSPECT families are gone entirely, every claimed
replacement the checker spot-tested is genuinely attested, the
disciples and lion seats are correctly seated, and most disclosed
constructions seat. The gate nevertheless **FAILS**, on the desk's
own stated standard — "Zero SUSPECT tokens remain book-wide (final
residue scan)" — which the mechanical recount refutes at named
seats: Päiči ×9, Jokčč ×8, Kärsi/Kärzii ×3, Maista ×1, free päi ×9,
sanug-as-participle ×2, palʹm at 36:34, and the untraced voitt-
family (24 seats, of which voittand at 28:37 / 28:82 was the
disclosed item). Each failure is named above with its seats, so the
residue can be cleared by a bounded seat list without another
book-wide pass.

---

## Summary for the record

| Gate | Verdict |
|---|---|
| 1 Canonical verify | PASS |
| 2 GAP census reconciled | PASS |
| 3 Fences | PASS |
| 4 Fidelity spot-check (46 fresh verses) | PASS — 0 failures |
| 5 Token adjudication sweep | **FAIL** — bounded residue, every seat named in Gate 5 |

The first build's two failures are not equal after remediation.
Fidelity — the failure that touched the reader — is repaired on
every verse the checker sampled, including all four re-checked
original failures. The token failure is reduced from a load-bearing
stratum to a capitalisation-shaped residue plus two stem questions
(palʹm, voitt-), but the remediation log claims zero residue, and
zero is not what the store contains. The desk should not repeat the
"zero SUSPECT tokens" claim until the Gate 5 seat list is cleared
and re-scanned with a case-insensitive screen.
