# Veps lane — FOURTH DELTA CHECKER REPORT (DELTA-4) ON THE TOKEN-ADJUDICATION GATE (2026-11-28)

Fourth delta pass by an agent that did not do the remediation or any
repair. Scope, per commission: verify the seats repaired after
Delta-3 (Addendum 4 of the remediation log), replicate the wider
sentence-initial hunt INDEPENDENTLY and in full — not merely
re-check the named seats — extend the same suspicion to capitalised
forms after internal punctuation, repeat the full case-insensitive
SUSPECT sweep, and re-confirm the mechanical gates. No verse text
was edited; the only file written is this report. Sources:
verses-store.json (current), master-verses.json,
work/remediation/verses-store-PRE-REMEDIATION.json (frozen store),
REMEDIATION-LOG-2026-11-28.md Addendum 4 (treated as a list to
test), CHECKER-REPORT-REMEDIATION / -DELTA / -DELTA2 /
-DELTA3-2026-11-28.md, glossary.md §§A–K, sources/lexicon-wikt.json
(Wiktionary lexicon), sources/wikt-pages.json (raw Wiktionary
pages), sources/dict-rus-vep/inc/*.xml (GiellaLT dict-rus-vep),
sources/lang-vep/src/fst/freq.txt (GiellaLT frequency list),
sources/corpus-vep (GiellaLT Veps Wikipedia corpus). One source
note, stated in the same breath: sources/kaikki-vep.json as it
stands in the lane is a 162-byte 404 HTML stub, so it contributes
no attestation either way in this pass; every check below rests on
the remaining harvested sources, which are the ones that carried
every prior pass's findings. All sweeps are this checker's own
scripts over the full 6,236-seat store.

## Verdict

**Gate 5: PASS** — the nine Addendum-4 seats are repaired exactly
as claimed, with the Master's sense preserved at every seat; the
full commissioned SUSPECT sweep is clean for the third pass
running; and this checker's independent replication of the wider
hunt — 882 capitalised sentence-initial forms, the 207 that never
occur lowercase screened one by one against every harvested
source, plus an extension screen of all 1,410 capitalised
non-initial forms — finds **no** sentence-initial or
capitalisation-shielded form that is both unattested in the
harvested sources and Finnish/Karelian-shaped. The failure mode
that produced the Päiči, selʹgenz, Joka and Sama/Vird/Saan residues
across four passes does not recur in the current store.
Mechanical gates: **CONFIRMED** (verify.py clean; GAP census 558
seats / 768 markers / 330 raw terms, palm exactly 15; verses
changed vs frozen 2,266 — all exactly as claimed in Addendum 4 as
corrected).

---

## 1. The nine repaired seats — CONFIRMED, all PASS

Each seat read against its Master verse; the frozen-store form in
brackets.

- **2:233** "…Se-žo velg om ⟦GAP: heir⟧ päle. Ku hö molembad
  tahtoba ⟦GAP: weaning⟧, ühtel melel i **ühtes pagiždes**, hö ei
  tege värad." Master: "The same duty is upon the heir. If the
  couple desire weaning, by mutual consent and consultation, they
  commit no error." [Sama; "küzu s"] **Se-žo** renders "the same"
  on the book's seated demonstrative paradigm; the split token
  "küzu s" is gone and the consultation phrase now stands as the
  fused attested-shaped form **ühtes pagiždes** ("in one
  discussion"). Both repairs as claimed; sense preserved in full.
  PASS.
- **13:17** "**Josmuz** kandoi nouzijad vahtad." Master: "The
  current carries swelling froth." [Vird, in a collapsed frozen
  rendering] **Josmuz** is attested outright in the harvested
  dictionary: dict-rus-vep N_rusvep.xml gives josmuz as the Veps
  equivalent in the течение ("current") entry — the dict's own
  word for exactly this sense, as Delta-3 predicted. PASS.
- **11:72** "**San**-ik minä lapsen, konz minä olen vanh naine…"
  Master: "Shall I give birth, when I am an old woman…" [Saan]
  **San** is the attested 1sg of sada (lexicon lemma sada, "to
  get, to receive, to obtain"; frequency list san ×23, verified
  by this checker's own grep). PASS.
- **74:49** "**Mikš** hö pörduba muštospäi?" — "Why are they
  turning away from the Reminder?" [Miks] **Mikš** is the lexicon
  lemma itself (frequency Mikš ×132 + mikš ×123). PASS.
- **95:7** "**Mikš** sinä vie küžud uskon?" — "So why do you still
  reject the religion?" [Miks] Same ruling. PASS.
- **98:3** "**Niš** oma kalʹhid kirjutuzid." — "In them are
  valuable writings." [Nis] **Niš** now matches the book's own
  seated form (niš in 18 lowercase seats). PASS.
- **52:33** "Vai hö sanudas: «Hän sädi sen»? **Ei, hö vaiše ei
  uskkoi**." Master: "Or do they say, 'He made it up'? Rather,
  they do not believe." [Eisa] The fused token is gone; the verse
  is restructured exactly as Addendum 4 claims, the adversative
  carried by the construction, sense preserved. PASS.
- **7:4** "**Kuverzʹ** lidnad mö murenzim?" — "How many a town
  have We destroyed?" [Kuverz] **Kuverzʹ** is the lexicon lemma
  ("how much, how many"), the dropped ʹ restored. PASS.
- **14:22** "…**Minei** ei olnuded ni üht valdad teiden päle,
  vaiše miše minä kucin teid, i tö vasttižid **minei**." Master:
  "I had no authority over you, except that I called you, and you
  answered me." [Minele] **Minei** is the book's usual allative
  (×91 book seats before this repair; frequency ×619) — the
  Delta-3 form note is normalised to the seated form. PASS.

Addendum 4's repair claim is verified in all nine particulars,
including the 2:233 split-token repair it disclosed alongside the
named seats.

## 2. The wider hunt, replicated independently — PASS, no residue

Method (this checker's own, built from scratch, deliberately
wider than the Delta-3 net): every sentence-initial token in the
book was extracted — verse-initial and after sentence punctuation
(. ! ? ;) — giving **882 distinct capitalised forms over 10,960
occurrences**. (Delta-3 reported 880 forms / 10,566 occurrences /
208 never-lowercase forms; the small differences are
extraction-boundary differences, and the wider net is the
conservative direction for a hunt whose whole history is forms
escaping narrower nets.) Of the 882 forms, **207 never occur
lowercase anywhere in the book** (one of them is the GAP-marker
head, an artefact, excluded from screening; 206 substantive
forms). Each of the 206 was screened one by one against the
Wiktionary lexicon, the frequency list, the dict XML equivalents,
the raw Wiktionary pages, and the corpus, with an exact-form
attestation pass followed by a stem-and-paradigm pass for every
form with no exact hit.

**Extension beyond sentence-initial seats, as commissioned:**
every capitalised token in a non-initial position was also
extracted — **1,410 distinct forms, 16,275 occurrences, of which
599 never occur lowercase** — covering the capitalisation behind
internal punctuation (— « " :) as well as the book's mid-sentence
capitalisation generally. The 599 were screened on the same
standard. Four internal forms were spot-read in their verses
before clearing: **Ent** at 20:51 (the native conjunction,
capitalised only because it follows the opening « of direct
speech), **Adahe** at 14:29 (illative of the book's ada "hell"
stem, "Adahe — hö palabad siš" for "Into Hell — they will burn
in it"), **Verhaz** at 41:44 (regular form of lexicon-attested
veraz, "foreign"), and **Todez** at 69:1 and passim (a nominal
derivative on the attested tozi / tod- "truth" stem, used as the
title "The Truth"; no Finnish profile — the Finnish cognate shape
would be totuus). The voit- forms in the internal list (Voitab,
Voitai, Voitajale, Voitandan) are the book's own voit- paradigm,
which occurs lowercase in 60+ seats and was ruled seatable by
Delta-3 §2; they are not the SUSPECT voitt- family (§3, zero).

How legitimate forms were separated from suspects, as commissioned:

- **Master proper names and their Veps-inflected forms** — names
  carried in the Master's forms per glossary §I policy, checked
  against the Master text: Moses / Mosesan, Pharaoh / Pharaohan /
  Pharaohale / Pharaohannoks / Pharaohin, Faraon / Faraonan /
  Faraonale / Faraonaspäi, Abraham / Abrahamin, Noah / Noahin /
  Noan, Joseph / Josephas, Aaron, Lot / Lotan, Jesus / Jesusan,
  Imranin, Thamood / Thamoodan, Aad, Muhammad, Messiah, Solomon,
  Safa, Saban, Ramadan, Egyptian, Quaroon, Quraish, Romanad, and
  the transliterated letter-names Alif, Lam, Meem, Ra, Seen, Ya,
  Saad, Ayn, Qaf, Noon. The internal-position screen adds the same
  names in their remaining case forms (Abrahamale, Adaman,
  Isaacale, Ishmaelile, Jacoban, Johnan, Jonah, Saleh, Shuaib,
  Zechariah, Luqman, Mary / Maryn, Gog / Magog, Harut / Marut,
  and the rest) and the Master's retained English terms under the
  names policy (Quran and its case forms, Torah, Gospel, Psalms,
  Christians, Jews, Arabs, Islam, West, Criterion, and similar) —
  none of these is a Veps-form question at all.
- **Jumal- forms** — Jumalal and Jumalale (frequency-attested
  outright), Jumalannoks (frequency-attested), Jumalannost,
  Jumalaspäi, Jumalavaraidajile: case forms of the seated lemma
  Jumal (glossary §A), capitalised book-wide by the book's God
  convention, stems attested. The internal screen adds the same
  paradigm's remaining cases (Jumalaha, Jumalalpäi, Jumalanke,
  Jumalas, Jumalannole) and the capitalised God-epithet compounds
  on attested stems (Kaiktedai, KaikenTedai, Kaikvoii, Kuldei /
  Kuundelii on the -i agent pattern, Ižandan- case forms of the
  §A lemma ižand).
- **Seated devices of glossary §§A–K** — Armahtajan / Armahtajale
  (§H armahtai), Sananvedä- compounds (§H), Selʹgeduz (selʹged
  family), the endustai-family and kirjutai/sudii-pattern
  derivations ruled seatable by prior passes (Hüvütettud,
  Läbipäzui, Vägevzoita, Čudoičet, Kirjutajiden, Opendatjad),
  and the Libutamižen device family in internal positions.
- **Ordinary inflected forms of attested stems** — imperative
  plurals in -kat/-gat (Alekat, Keragat, Riktkat, Palagat,
  Sabaskat, Vasttakat, Tulbat), jussives in -kaha (Kackaha,
  Kuckaha, Loikaha — the paradigm Delta-3 seated beside
  frequency-attested sanugaha), the -g singular imperative
  paradigm the book sanctions in sanug (Torag, of glossary
  torata), converbs in -des/-ten (Kändes, Lebaides, Eksudes,
  Ümbärdes, Ottades, Magaten, Paštaden, Sulaten, Jäteden,
  Erigoten), case forms of seated nouns and pronouns (Neced /
  Nec / Neces on glossary §F nece; Hänennost on hän; Čas / Časan
  on dict-attested čas; Jogi, Naku, Sei, Muite, Arvod, Valičend,
  Bohat, Jodes, Sanumata, Znamoitud — frequency- or dict-attested
  outright), regular compounds and derivations on attested stems
  (Pahantegijile, Värantegijile, Uskijanost / Uskomatomile /
  Uskijoidennost / Uskujale on usk-, Grähkategijan / Grähkhišpäi
  on grähk, Andaksandmindaha, Edelembai on edel, Otimmek /
  Pidämek — 1pl forms carrying the -k interrogative clitic,
  Jogaükselle — cleared by Delta-2 §5, Ecmata / Ectba — cleared
  by Delta-2 §5 on ectä, Stökl — cleared by Delta-2 §5, Dumajab /
  Dumajeden — the dumaj- family Delta-2 cleared as
  frequency-attested, Nacei — dict-attested (наверно(е) → nacein
  family), Kidžha — one capitalised form of the book's kidž-
  family, which occurs lowercase book-wide, so the stem is not a
  never-lowercase hiding place of the adjudicated kind, Adahe,
  Verhaz, Todez, Ent — read in their verses and cleared in the
  extension paragraph above), and the two repaired seats
  themselves in their new forms (**Josmuz** — dict-attested
  outright; **San** — frequency-attested ×23).

What remains after that separation is nothing that meets the
FAIL standard: no never-lowercase sentence-initial form, and no
capitalised form in any position, is both unattested in the
harvested sources and Finnish/Karelian-shaped. The only
never-lowercase forms with no attestation of any kind are the
referred families of §5, which the commission places outside
this gate. **PASS.**

## 3. Full SUSPECT sweep repeated (case-insensitive, book-wide)

Zero is the pass mark. Counts are substring tokens unless marked
(word). Every commissioned family stands at zero:

päiči 0 · tyo (substring and word) / tyospäi 0 · rauh 0 ·
hülgä- 0 · kield- / kielt- 0 · selʹkt- 0 · mörinä 0 ·
kärzind- / kärsi- / kärs- (any) 0 · ilma (substring and free
word) 0 · maistta / maista / maits- 0 · jokčč- 0 · hüväst- 0 ·
perindon 0 · välleng- 0 · kogokoi 0 · heikendel- 0 · kiälta 0 ·
**voitt- 0** · **palʹm- 0** · **free standalone päi (word) 0** ·
**selʹgenz bare stem (selʹgenz(?!o)) 0** (all 21 selʹgenz tokens
are selʹgenzoit- forms, as Delta-2's census established). The
delta-round forms are likewise all zero on re-sweep: joka (word)
0, silloin 0, päinvastoin 0, olles 0, **sama (word) 0, vird (word)
0, saan (word) 0**, sinanvedä- 0.

Two standing substring notes, recorded so they are not raised
again unexplained: **veka** returns one substring hit, the
previously ruled **Vekat** at 40:46 — the regular imperative
plural of vedäda, not the SUSPECT word veka (word count 0);
**estai** returns 3 hits, all the previously ruled, dict-rooted
vägestai family at 4:75, 5:56, 6:61.

**Singular -nug participles.** Full -nug- census repeated (27
distinct -nug- forms): the only token ending in bare -nug is
**sanug ×114** (95 Sanug + 19 sanug), every seat doing "Say:" /
"tell" imperative work, with its sanctioned paradigm sanugat,
sanugaha, sanugoi. All other -nug- tokens are -nugoi plurals on
attested stems. No singular -nug participle stands outside the
sanctioned set. PASS.

**PASS — the commissioned sweep is clean in full, for the third
consecutive delta pass.**

## 4. Form notes

None. The five Delta-3 form notes (Miks ×2, Nis, Eisa, Kuverz,
Minele) are all normalised in the seats verified at §1, and this
pass's wider and internal screens found no new spelling variant
of an attested form standing in a capitalised seat. The küž-
sentence-initial instance (Küžujale, 70:25) belongs to the
referred families of §5, not to this section, exactly as
Delta-2 and Delta-3 recorded it.

## 5. Referred families (examined, reported separately, NOT graded)

Per the commission's scope note, the families prior checkers
referred without grading remain outside this gate: the küž-
ž-variant (sentence-initial instance **Küžujale** at 70:25,
×22 book-wide, of attested küzuda) and the never-adjudicated
**epäil-** (sentence-initial **Epäiluseta** at 11:22,
**Epäilʹdäta** at 40:43), **ihmeh-** (**Ihmehtot** at 7:63 and
7:69; internal Ihmehtod at 11:73), **valehtelij-**
(**Valehtelija** at 96:16), **judalai-** (**Judalaized** at 9:30,
**Judalaižile** at 6:146) and **hänelle** families. This checker
confirms their instances so the record is complete; none of them
is a form of a commissioned SUSPECT family, and none has been
allowed to carry this verdict either way. They await the desk's
separate adjudication, exactly as referred.

## 6. Mechanical gates — CONFIRMED

verify.py re-run by this checker on the current store:

- store seats: **6,236**; master seats: **6,236**; seat-set
  equal: **True**
- per-surah mismatches: **NONE**
- non-U+02B9 apostrophes: **NONE (0)**
- GAP seats (verify.py): **558**
- angel seats: **86**
- 1:1 == basmalah: **True** — "Jumalan nimel, Armahtajan,
  Armahtajan."

(verify.py's untraced-candidate list is, by its own header, a
candidate list for the checker, not a verdict; it is not a gate
and is not graded here.)

Checker's own mechanical GAP recount (regex ⟦GAP: …⟧ over the
store): **558 seats / 768 markers / 330 distinct raw terms** —
Addendum 4's claimed 558 / 768 / 330 reproduced exactly. The term
**palm: exactly 15 markers**, as claimed (palm-containing markers
total 18, the standing note). Case-folded distinct terms: 329,
the standing Sabbath/sabbath raw-counting note.

Verses changed vs the frozen pre-remediation store, checker's
recount: **2,266 of 6,236** — exactly Addendum 4's corrected
figure (the nine-seat repair adds seven net changed verses to
Delta-3's 2,259: two of the nine seats, 13:17's re-render among
them, already differed from the frozen text — the arithmetic
reconciles seat by seat against the frozen store). Also
confirmed: Cyrillic characters none; "sspäi" none.

---

## Summary for the record

| Check | Verdict |
|---|---|
| 1. Nine repaired seats (2:233, 13:17, 11:72, 74:49, 95:7, 98:3, 52:33, 7:4, 14:22) vs Master | PASS — forms as claimed (Se-žo + ühtes pagiždes, Josmuz, San, Mikš ×2, Niš, restructured 52:33, Kuverzʹ, Minei), sense preserved at all nine |
| 2. Independent replication of the wider sentence-initial hunt (882 forms; 207 never-lowercase screened one by one) + internal-capitalisation extension (1,410 forms; 599 never-lowercase) | PASS — no unattested Finnish/Karelian-shaped form in any capitalised position |
| 3. Full SUSPECT sweep + bare selʹgenz + voitt- + palʹm- + free päi + singular -nug census + all delta-round forms | PASS — every commissioned family at zero, third consecutive pass |
| 4. Mechanical gates + GAP census | CONFIRMED — verify.py clean; 558 / 768 / 330 and palm 15 reproduced exactly; 2,266 verses changed vs frozen, as claimed |

**Gate 5 verdict: PASS.** The nine-seat Delta-3 repair is verified
complete and accurate in every particular Addendum 4 claimed —
its forms, its census and its corrected changed-verse count all
reproduce exactly — the commissioned SUSPECT sweep is clean
book-wide for the third consecutive pass, and the decisive test
this commission set, a full independent replication of the
sentence-initial hunt extended to capitalised forms in every
position, finds no further residue of the adjudicated failure
mode. The token-adjudication gate therefore passes on the book
as it stands. The §5 referred families (küž- and the
never-adjudicated epäil-, valehtelij-, ihmeh-, hänelle, judalai-
families) remain a separate adjudication that this pass names
but does not grade, exactly as the commission scoped it; the
gate's PASS does not speak to them either way.
