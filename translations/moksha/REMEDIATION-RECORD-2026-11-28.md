# Remediation Record — Moksha (mdf) Quran Draft, 2026-11-28

Status: DRAFT — NOT PUBLISHED. **Not landed, not shelved, not
committed, not pushed.** This remediation was applied under the
audit-application standard (desk-verified findings are applied
most-serious-first) to the draft exactly as the independent
checker found it; the previous remediation crew was interrupted
before making any edits, and its report confirms none were made.
The remediator built none of the original text. Landing waits on
a fresh independent re-check PASS, which a later crew will run.

Source of findings: `CHECKER-REPORT-INDEPENDENT-2026-11-28.md`
(verdict FAIL, §§8–9). Method: `work/remediate-2026-11-28.py`
against `verses-store.json`; the pre-remediation store is
preserved at `work/verses-store-PRE-REMEDIATION-2026-11-28.json`,
and the per-seat change ledger (1,067 entries from the scripted
pass, plus the §9.7(d) pass below) is at
`work/remediation-ledger-2026-11-28.json`. Outputs were rebuilt
with the lane's own `build.py` and `assemble.py`. All figures
below were mechanically recomputed on the finished store, not
estimated; every before-figure equals the checker's own recount.

Seats changed in total: **1,111 of 6,236**; 5,125 seats are
byte-identical to the checked draft.

## §8.1 што / штоба — unattested conjunctions (623 tokens) — DONE

Before: што 348 tokens / 302 seats; штоба 275 tokens / 252 seats.
After: **0 / 0**.

Reseating devices — the build's own Batch D road (work/notes-D.md),
which removed што/штоба from all 556 of its verses before shipping
on exactly this attestation ground, adopted book-wide:

- **што (complementiser "that")** — deleted; the complement clause
  rides asyndetic juxtaposition after its governing verb, Batch D's
  logged device. Punctuation was preserved seat by seat (", што "
  → ", "; "што, " parentheticals → ","; sentence-initial "Што "
  deleted with the following word capitalised). Sample-verified
  after conversion at 4:3, 4:127, 6:151, 8:25, 18:104, 22:40,
  22:65, 24:53, 34:14, 36:60 — every sampled clause reads complete
  with no content word lost.
- **штоба (purpose "so that")** — reseated onto **сянь инкса**,
  Batch D's logged purpose device (сянь + инкса, both lemmas in
  `sources/mdf-lemmas.json`; the purpose phrase itself is
  dictionary-attested: Ščankina 2011, via the kaikki harvest,
  glosses сянкса "that's why, with that purpose" and lists the
  phrase сянкса штоба). Сянь инкса tokens: 101 → 376 (+275, exactly
  the штоба count). Two seats (5:35, 37:61) now carry инкса …
  сянь инкса in sequence, mirroring the dictionary phrase's own
  stacking; recorded here so the re-checker sees them as a
  decision, not an accident.

## §8.2 эли → али — DONE

Before: эли 127 tokens / 109 seats. After: **0**. Mechanical
reseat onto али, the form BUILD-SPEC seats for "or" and a Giella
CC lemma (`<l pos="CC">али</l>`, fin "tai/vai"); capitalisation
preserved (Эли → Али). Али tokens: 360 → 487 (+127).

## §8.3 4:23 — garbled clause and literal ellipsis — DONE

The clause «тинь виде цёраньк аляснон авалангс... и аватне:»
("your true sons' fathers' wives... and the wives:" — kinship
reversed, ellipsis in the finished text) is replaced by
«И тинь шачф цёраньк аватне,» — "and the wives of your born
(genetic) sons" — on the verse's own attested stems: шачф "born"
(a lemma in the inventory, and the very form this verse already
uses for the stepdaughters, «шачфт аватнень эзда»), цёра "son",
ава "wife/woman", in the verse's own possessor-first order
(compare «брадоньк стиренза», «аваньк тядяснон» in the same
verse). The ellipsis and the stray fragment are gone; the book
now contains no "..." anywhere. The rest of 4:23 is untouched
and carries the Master's full kinship list.

## §8.4 Mixed-script tokens — DONE

All 13 distinct fused tokens (21 occurrences, 20 seats) respelled
in pure Cyrillic: Азороze→Азорозе (×5), азороze→азорозе (×5),
кучфоze→кучфозе, пилесna→пилесна, сундукc→сундукс,
пингonte→пингонте, алянoke→аляноке, тевnte→тевнте,
отвечade→отвечаде, Шкайноke→Шкайноке, Шкайnte→Шкайнте,
идолnte→идолнте, videста→видеста. Residual fused tokens: **0**.
(The hyphenated name forms of the names policy — Moses-нди and
its like — are untouched; they are the book's standing practice,
not this defect class.)

## §8.5 7:166 — apes GAP — DONE

«берянь маймункс» → «берянь ⟦GAP: apes⟧», consistent with the
sister seats 2:65 and 5:60. маймун tokens: 1 → 0. GAP census is
now **58 seats / 68 markers** (jinn 31, pilgrimage 16, usury 8,
Sabbath 7, apes 3, gnat 1, cucumber 1, fig 1); the manuscript's
front matter was recomputed by `assemble.py` and carries the new
census.

## §8.6 47:25 — non-Moksha letter ң (U+04A3) — DONE

«кең васта» → «келе васта». Ground, stated plainly because it
departs from the checker's parenthetical guess: кенде is a
Giella noun lemma but its gloss is a felt saddle-blanket
(fin "satulan alla oleva huopapeite"), not "wide", and кенг is
not in the inventory at all — neither could seat. The seated
form келе is the book's own attested "wide/vast" adjective
(`mdf-lemmas.json` lemma; the book's own seats at 29:56
«Монь модазе келги», 39:10 «Шкаень модац келе»). U+04A3 tokens
book-wide: 1 → **0**; a full scan finds no Cyrillic letter
outside the 33-letter norm anywhere in the book.

## §8.7 29:14 — number error — DONE

«тёжянь кизот вейхксагемонь кизода башка» ("a thousand years,
ninety years apart") → «тёжянь кизот **ведьгемонь** кизода
башка» ("a thousand years minus fifty years"), ведьгемонь being
the attested fifty (a lemma in `mdf-lemmas.json` and a Giella
Num stem; the book's own expanded form at 70:4 is the same
number). One seat.

## §8.8 иля / иляда — spec-barred prohibitive (117 tokens) — DONE

Before: иля 92 + иляда 25 = 117 tokens / 95 seats. After: **0**.
Conversion is the one Batch D's own notes prescribe and
BUILD-SPEC orders: **аф + 2pl present as command**. The book's
аф count rose 4,661 → 4,778 (+117, exactly one аф per removed
иля token). The verb after each иля was reseated to its 2pl
present form under three recorded grounds:

- **[A] book-attested 2pl form** — the replacement form already
  stands in this book's own text in a 2pl seat: тиихтяда (4:3
  «аф тиихтяда»), сявода (4:89 «аф сявода»), ярхцада (4:29
  «Аф ярхцада»), шавода (4:29), сувада (12:67, the same verse's
  second clause), пеледа (4:3), улетяда (2:150), азтада,
  арьсетяда, нолдада, кирдеда, кадтада, васедьтада, веляфтада,
  корхтада, вештада, моледа (6:153), максода, кандатада,
  авардеда, учеда, путтада, путнеда, ётатада, сярядтада,
  малаттада.
- **[R] regular formation** — stem + -тада/-тяда on the attested
  stem, the spec's own paradigm endings, where the book happens
  not to seat that verb's 2pl elsewhere: кяшнетяда,
  сювордатада, ёмафтада, ёрятада, кемокстатада, юкстатада,
  кочкатада, сюдтада, венемтада, вишкфтада, синдяда,
  виздефтетяда, ванатада, полафтада.
- **[K] form already plural present** — particle swap only:
  кулоттяда, араттяда, тиетяда (2pl present already), and the
  third-person frames арьсихть, азыхть, сявыхть, азый, where
  аф + the seated present form carries the prohibition without
  re-personing the clause (2:282's «аф азый аф сёрмадомс» reads
  "shall not refuse to write", the Master's sense).

Three two-word seats were converted as units: «иля война тие»
→ «аф война тиихтяда» (2:191), «иля алу пут» → «аф алу путтада»
(3:194), «иля вишкине тие» → «аф вишкине тиихтяда» (2:282).
Note for the re-checker: the spec's uniform 2pl frame is applied
even where the Master addresses one person (e.g. 15:88,
«Аф венемтада тонь сельме-от…») — that is the spec's prescribed
conversion, applied uniformly so the re-check can judge the rule
itself, not a mixture.

## §8.9 мельга → мельге paradigm — DONE

Before: мельга-family а-forms 74 substring occurrences / 67
seats (мельга 48, мельганза 11, мельгат 10, мельгаст 5).
After: **0**. Reseat onto the мельге paradigm — мельге is a
Giella postposition lemma (`<l pos="Po">мельге</l>`) and an
`mdf-lemmas.json` lemma, as the checker settled: мельга→мельге
(48; мельге tokens 79 → 127), мельганза→мельгенза (11),
мельгат→мельгет (10), мельгаст→мельгест (5; мельгест tokens
3 → 8). Forms already on the е-stem (мельгели, мельгест,
мельгенк, мельгянт, мельгон) were left as they stood.

## §9.6 кда — CORROBORATED AND RECORDED (desk ruling executed)

кда (865 tokens) **stands**, on named attested evidence found in
the lane's own held sources: the 2016 Moksha New Testament
frequency list held in the GiellaLT giella-mdf repository at
`sources/giella/devtools/testdata/bibleFreq2016.txt` — the
frequency count of the very control text BUILD-SPEC names —
records **кда 332 occurrences and Кда 239 (571 in all)**, in the
company of the book's other attested function words (кода 739,
мес 735, мзярда 435, али 267 in the same list). кда is therefore
an attested Moksha conjunction in the modern literary control
text; its absence from the harvested headword list
(`mdf-lemmas.json` holds only the phrase «кда ули нужа») is a
harvest gap, not an attestation gap. This paragraph is the
record the desk ruling required; кда may not be re-flagged as
"unattested and unrecorded" from this date.

## §9.7 / §9.4 reservations — DONE

- **(c) сынь → синь**: 265 tokens / 207 seats → **0** сынь;
  синь 4,819 → 5,084 (+265). синь is the spec pronoun-table form
  and an inventory lemma.
- **(d) ингели → инголе**: 136 tokens / 127 seats → **0**
  ингели. Ground: инголе is the Giella postposition lemma
  (`<l pos="Po">инголе</l>`) and the 2016 NT frequency list's
  form (инголе 214 + Инголе 1; ингели 0 in the same list);
  ингели is in neither source. Applied as the same §9.7 class
  as сынь.
- **(a) unclosed guillemet**: 21:56 now closes its « at the
  verse end («…мон тянь свидетельян.»); book totals balance
  « 232 / » 232. 21:57 keeps its own opening mark, as in the
  Master, where the speech is seated verse by verse.
- **(b) trailing spaces**: the nine seats (92:5, 92:6, 92:8,
  92:9, 101:6, 101:8, 102:5, 110:1, 110:2) stripped; txt/store
  differences are now **0 at all 6,236 seats**.
- **§9.4 74:30 teen formation**: «вейхкса кемонь» ("nine ten",
  ambiguous beside "ninety") → **кевейхксые**, the Giella Num
  stem for nineteen and an `mdf-lemmas.json` lemma, in the
  inventory's own teen series (кефкие 11, кемгафтува 12,
  кемголмува 13, кемнилие 14, кеветие 15, кемготува 16,
  кемгафксува 18, кевейхксые 19). One seat.

## Reservations carried forward, untouched by this remediation

Recorded so the re-check and the landing decision see them:
the prophet/messenger collapse (§9.3, disclosed device);
4:56 кедь "skins" (§4, defensible Moksha seat coinciding in
form with the barred Erzya word); manna in Latin at 2:57,
7:160, 20:80 and Bedouin-тнень at 33:20 (§9.5 — the lane's
`verify.py` now reports exactly these, plus the vocative "O"
and the al- of al-Lat/al-Uzza, as its only retained-Latin
candidates); the “ ” quote imbalance inherited from the Master
itself (§9.7a). None of these was in the remediation's charge;
none was silently altered.

## Mechanical verification of the remediated book

Recomputed on the finished store and rebuilt outputs
(`build.py`, `assemble.py`, `verify.py` all re-run):

- Store seats 6,236 = master seats 6,236; seat sets exactly
  equal; per-surah grid clean at all 114 surahs.
- `quran-mdf.json` flattened equals `verses-store.json` seat
  for seat (6,236/6,236, texts identical); `quran-mdf.txt`
  carries 6,236 numbered verse lines matching the store at
  every seat, 0 mismatches.
- 1:1 equals the fixed Basmalah exactly; txt carries 114
  Basmalah occurrences (112 standalone lines + 1:1 numbered +
  27:30 inline), as the checker verified for the pre-remediation
  book.
- GAP seats 58, markers 68, all well-formed; no empty seats;
  the string "redacted" appears in no seat.
- Erzya-bar whole-token screen: NONE (verify.py).
- Every §8 target count is 0 (table above); no double spaces,
  no space-before-punctuation, no verse opens lowercase, no
  Cyrillic letter outside the 33-letter norm.
- Purple-style screen (verify.py): distinct Cyrillic tokens
  9,901; untraced candidates 4,940 (was 4,955) — the removed
  mass is exactly the remediated families; the largest remaining
  candidate is кда (865), now corroborated and recorded above,
  followed by the азомс paradigm tail the checker adjudicated
  as not defects (§10).

## Stop line

This remediation **stops before landing**, as ordered: nothing
was landed, shelved, committed, or pushed, and the GitHub shelf
was not touched. The work/batch-*.json files stand unedited as
the build's historical record; the remediated text lives in
`verses-store.json` and its rebuilt outputs. The next step is a
fresh independent re-check by an agent who built none of this
text and none of this remediation.
