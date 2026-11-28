# Komi-Permyak (koi) Quran draft — flags-and-gaps disclosure (2026-11-28)

All figures recomputed from verses-store.json by verify.py at
this desk on 2026-11-28. The draft stands STOPPED before
landing: nothing shelved, committed, or pushed. It awaits a
fresh independent checker.

## Headline counts
- Verses: **6,236 of 6,236** (store seats == Master seats,
  per-surah grid exact, no empty seats, "redacted" nowhere).
- Verses rendered without a GAP marker: **792**.
- GAP seats: **5,444** (87.3% of verses). GAP markers:
  **16,840**. Distinct GAP terms: **4,728**.
- Marker distribution: 0 markers 792 verses; 1 marker 1,515;
  2 markers 1,352; 3 markers 915; 4 markers 591; 5 markers
  407; 6 markers 221; 7 markers 151; then a tail to one verse
  carrying 40 markers. Bracket integrity: 16,840 opening ⟦ and
  16,840 closing ⟧. The manuscript's count is 16,841 — the
  extra marker is the explanatory example in the front matter.
- Seated dictionary: **1,317 entries** (engine count; manual
  core + 712 gloss-matched seats). Dropped as unverified at
  build time: **0**.
- Inventories: GiellaLT giella-koi 77,661 lemmas (14,725 with
  glosses); gt-norm paradigm forms 15,533; Wiktionary
  Komi-Permyak 334 headwords.

## Basmalah
Fixed form **Енлӧн нимӧн, Милӧсьта, Милӧсьта.** — 113
occurrences in quran-koi.txt (112 unnumbered opening lines +
numbered 1:1; surah 9 carries none, correctly). Seat 1:1
equals the fixed form exactly; seat 1:3 equals the spec form
**Милӧсьта, Милӧсьта.** exactly. The in-verse Basmalah at
27:30 is rendered on the same seats word by word.

## Script purity (screens built to the Komi-Zyrian checker's
§4 specification, from the start)
- Retained Latin, measured on WHITESPACE tokens with GAP
  interiors excluded, against the explicit names allowlist
  (BUILD-SPEC names policy): allowlisted **129 types / 1,056
  tokens** (personal names, scripture titles, disjointed
  letters, place/people/language proper names). Non-allowlist
  retained Latin: **0 types, 0 tokens**. There is no silent
  English tier in this draft: every unseated Master word,
  capitalised or not, carries the GAP marker.
- Mixed-script tokens: **6**, all the disclosed genitive-on-
  names device (Adamлӧн 5:27; Pharaohлӧн 7:127, 40:28, 40:37;
  Abrahamлӧн 11:74; Josephлӧн 12:58). Other mixed tokens:
  NONE.
- Cyrillic attestation screen (verify.py): distinct Cyrillic
  tokens 841; untraced candidates **0** — every Cyrillic token
  traces to a koi inventory lemma, a glossary lemma, or a
  disclosed regular derivation of one. Tokens containing ӧ:
  369 types; containing і: 35 types.
- The Komi-Zyrian fence on the Cyrillic side: the screen's
  inventories are koi-only. Two Zyrian forms caught in the
  first engine draft (войтыр; Zyrian plural shapes) were
  removed and the build re-run; see the attestation audit.

## Top GAP terms (markers)
used ×149 · things ×108 · belongs ×73 · should ×50 · doubt
×48 · fight ×43 · blessed ×40 · considered ×40 · reached ×39
· wronged ×39 · losers ×37 · associate ×35 · community ×34 ·
inspired ×34 · miserable ×33 · marvels ×33 · terrible ×32 ·
wisdom ×32 · glory ×30 · patient ×30 · justice ×30 ·
blessings ×29 · permission ×29 · presence ×29 · admit ×29 ·
bounty ×28 · authority ×28 · lot ×28 · perform ×27 · avail
×27 · delivered ×27 · benefit ×27 · greater ×27 · goodness
×27 · verses ×27 · fruits ×26 · sincere ×26 · provision ×26
· present ×26 · proofs ×26. Standing GAP families held open
at every seat: Sabbath, Hajj, Umrah, pilgrimage (technical),
usury (technical), alms (technical), wisdom, justice,
permission, doubt.

## Flagged seats and known candidates for the checker
- **милӧсьта** (mercy family, incl. the Basmalah and 55:1):
  inventory lemma, own gloss not carried in the XML subset;
  family gloss-attested by милуйтны "миловать, любить".
- **ен** for "Lord": disclosed device (no господь seat
  attested); "Lord of the worlds" rides the phrase Муэзлӧн Ен
  (муэзлӧн is the attested plural genitive [Y]).
- **веськыт** for "righteous" and **веськытлун** for
  "righteousness": the straight/just seat; no праведный gloss
  attested in the koi sources.
- **казьмӧтны / казьмӧтісь** for "warn / warner": "remind"
  seated for "warn", disclosed.
- **мезмӧтны** for "save": "free, release" seated for "save",
  disclosed.
- **келмӧм** for "prayer": gloss marked Usol. dialect.
- **видз** for "fasting": homonym with "meadow".
- **дон** for "reward": gloss "price".
- **гижӧт** for "scripture" (generic): gloss "writing,
  letter".
- **пас** (sign), **кодзув** (star), **саридз** (sea),
  **мыж** (sin), **джинн** (jinn): inventory lemmas whose own
  glosses are not carried in the XML subset.
- Attested loans seated and flagged: ангел, пророк, рай, ад,
  храм, трон, жертва, идол, джинн, мечеть, религия, слуга,
  враг, факт, семья, дело, средство, война.
- Devices: ыстісь (messenger), эскісь (believer), эскӧм
  (faith), прӧститӧм (forgiveness), пикӧтӧм (punishment),
  восьтӧм (revelation), мӧд олӧм (hereafter), став вына
  (almighty), керӧм (deed), вӧчӧм (creation), мучитӧм
  (torment), оз эскӧм (disbelief), мунны бӧрын (follow),
  кӧ оз (unless), медым оз (lest), оз кужӧ (cannot).
- Auxiliary devices: will/shall/would → лоӧ; can/could →
  кужӧ; may → позьӧ; have/has/had → кутны; let → позьны;
  "at" seats empty; "out" and "by" dropped as plain-style
  particles (engine DROP set, disclosed in the glossary).
- **Candidates recorded for the checker's adjudication** (not
  asserted as errors): "peace" rides му (the земля/мир
  homonym — the same seat as earth/world); "pay" rides мед
  (a verb seat matched on the платить gloss); 36:58 therefore
  reads with му at the "Peace" seat; 1:7's final clause seats
  the guide verb at the "astray" neighbourhood by the
  engine's inflection matching; "understand" rides артавны
  (gloss-matched; its first gloss family is
  consider/count-out). Each is a gloss-matched seat under the
  disclosed method, listed here so the checker can rule on
  them singly.
- The checker pool for this language overlaps the resources'
  own makers (brief §6); that overlap is disclosed on the
  book's face, per the brief's condition 5.

## What this disclosure does not claim
No independent check has been run on this draft. verify.py's
figures are the build's own mechanical screen, stated as
candidates for the fresh independent checker, who must
recompute them. Nothing here is landed, shelved, committed,
or pushed, and the book's face says DRAFT — NOT PUBLISHED.

---

## Addendum — 2026-11-28 (remediation pass; this addendum corrects the record above, which is not rewritten)

- The sentence above — "Two Zyrian forms caught in the first engine draft (войтыр; Zyrian plural shapes) were removed and the build re-run" — is corrected by the addenda to the attestation audit and the build report of the same date: the Zyrian plurals эскісьяс (×272) and вӧчісьяс (×67) in fact stood in the text (checker §7, 313 seats) and have now been re-seated in Permyak shape as эскісььэз and вӧчісььэз by an engine rebuild; -яс plural tokens are now 0, and the tightened verify.py returns 0 untraced candidates (841 distinct Cyrillic tokens; ӧ 369 types; і 35 types — counts unchanged).
- Seat 1:7's final clause, listed above as a candidate, was CONFIRMED by the checker as a real mismatch and is now re-seated on вошны (вошӧ): "ни эна кин лоӧ вошӧ".
- Standing GAP families: the list above is reconciled for alms — alms as a technical term (zakat) remains GAP-marked as a family; the generic alms/charity seat rides the attested корӧм (gloss includes "милостыня, подаяние"), the same generic-seat exception the list already carried for scripture/гижӧт. See the attestation audit's addendum of 2026-11-28.
- GAP census after remediation is unchanged: 5,444 GAP seats, 16,840 markers, 4,728 distinct terms, 792 verses without a marker. Seated dictionary is now 1,318 entries (+1, the direct "misguided" seat). Full record: REMEDIATION-RECORD-2026-11-28.md. The draft remains STOPPED before landing, awaiting a fresh independent re-check.
