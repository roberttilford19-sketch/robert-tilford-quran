# Komi-Permyak (koi) Quran draft — INDEPENDENT CHECKER REPORT (2026-11-28)

Checker stance: this checker built none of the text under review.
Every figure below was recomputed at this desk with this checker's
own scripts (in /tmp, not the build's verify.py) from the files of
record: verses-store.json, quran-koi.json, quran-koi.txt,
ayah-companion-manuscript-KOI.md, master-verses.json,
BUILD-SPEC.md, glossary.md, ATTESTATION-AUDIT-2026-11-28.md,
FLAGS-AND-GAPS-DISCLOSURE-KOI-2026-11-28.md,
LICENCES-RECORDED-2026-11-28.md, BUILD-REPORT-KOI-2026-11-28.md,
and the harvested inventories in sources/. Nothing was edited,
landed, shelved, committed, or pushed by this check.

## Verdict (stated first; ground and consequence in §§7, 9, 10)

**FAIL — with the GAP-tier ruling given separately in §9 as
PASS-WITH-GAP-TIER-RESERVATION.** Almost every headline figure
the build reports is verified to the digit (§§1–6, 8): 6,236
verses, the GAP census, the Basmalah, zero non-allowlist Latin,
exactly the 6 disclosed mixed-script tokens, 841 Cyrillic
tokens with 0 untraced, and войтыр truly absent. The FAIL
rests on §7: the Zyrian plural shapes the build says it caught
and removed in fact stand in the text — эскісьяс ×272 and
вӧчісьяс ×67, 339 tokens in 313 seats (full seat list in §7) —
the Zyrian plural suffix -яс seated on three core terms,
against BUILD-SPEC's own Permyak plural rule. Bounded and
remediable by the §10 repair pass; no rebuild required.


## 1. Recount, seat-set, per-surah grid — PASS, exact

- Store seats 6,236; Master seats 6,236; seat sets exactly equal
  in both directions. `quran-koi.json`, flattened, holds 6,236
  seats identical to the store, seat for seat.
- Per-surah grid: all 114 surah counts match the standard grid
  exactly (7, 286, 200, 176, 120, 165, 206, 75, … 6; sum 6,236).
  Mismatches: NONE.
- Empty seats: NONE. The string "redacted": NONE in the store,
  in `quran-koi.txt`, or in the manuscript. The two Master seats
  carrying a literal "<redacted>" placeholder are rendered for
  their surrounding sense (39:7; 48:8 — verified in §8).

## 2. Basmalah — PASS, exact

Fixed form «Енлӧн нимӧн, Милӧсьта, Милӧсьта.»

- Store seat 1:1 equals the fixed form character for character;
  the full string occurs exactly once inside the store (at 1:1).
- In `quran-koi.txt`: **113** occurrences — counted surah by
  surah at this desk: exactly one in every surah section except
  surah 9 (zero, correctly); surah 1's single occurrence is the
  numbered verse 1:1, the other 112 are unnumbered opening
  lines. Anomalies: NONE. The manuscript likewise counts 113.
- Seat 1:3 equals «Милӧсьта, Милӧсьта.» exactly, per spec — the
  seat the Komi-Zyrian draft failed; this draft passes it.
- 27:30: the in-verse Basmalah is rendered on the same seats
  word by word in lower case, as the Master's sentence position
  requires («…‘ ын ним ен, милӧсьта, милӧсьта.»). Verified as
  disclosed; not the fixed capitalised form, and not claimed
  to be.

## 3. GAP census — PASS, exact to the digit

Recomputed from the store, independent of `verify.py`:

- GAP seats **5,444** (87.3% of verses); GAP markers **16,840**;
  distinct GAP terms **4,728**; verses without a marker **792**.
  Every figure in the build report and disclosure is verified
  exactly, including the top terms (used ×149, things ×108,
  belongs ×73, should ×50, doubt ×48, fight ×43, blessed ×40,
  considered ×40, reached ×39, wronged ×39).
- Distribution: 0 markers 792 verses; 1 marker 1,515; 2 markers
  1,352; 3 markers 915; 4 markers 591; 5 markers 407; 6 markers
  221; 7 markers 151; then a tail to one verse (2:282) carrying
  40 markers. Bracket integrity: 16,840 opening ⟦ and 16,840
  closing ⟧, no malformed seat.
- The manuscript's count is 16,841 — exactly one more, the
  front-matter explanatory example. Not a discrepancy.
- Standing GAP families verified GAP-marked at every seat, in
  lower-case marker form: Sabbath (2:65, 4:154, 7:163, 16:124 —
  «⟦GAP: sabbath⟧»), Hajj (2:189, 2:196, 2:197), Umrah (2:158,
  2:196), pilgrimage (2:158, 3:97, 9:3, 22:27), usury, wisdom
  (31 GAP seats), justice (29), permission (25), doubt (58).
  One minor inconsistency, recorded not failed: "alms" is
  named a standing GAP family in the attestation audit, yet
  the generic seat rides the attested корӧм (2:110; мед корӧм
  at 5:12), as the generic scripture seat rides гижӧт under
  the spec's own exception. The audit's family list and the
  glossary should be reconciled at remediation.

## 4. Script purity — retained Latin and mixed script — PASS, exact

This checker's own whitespace-token census (GAP interiors
excluded), the method the Komi-Zyrian checker's §4 prescribed:

- Pure Latin tokens: **129 types / 1,056 tokens, every one on
  the explicit allowlist** (personal names, scripture titles,
  disjointed letters, place/people/language proper names).
  Non-allowlist retained Latin: **0 types, 0 tokens**.
  Lowercase-initial Latin types: NONE. There is no silent
  English tier in this draft — the fault that failed the
  Komi-Zyrian lane is genuinely absent here, and the build's
  screen this time measures what it claims (its allowlist is
  explicit in `verify.py`, not derived from Master
  capitalisation; this checker extracted and tested against
  that same list independently, and also confirmed no Latin
  type outside it occurs at all).
- Mixed-script tokens: **exactly 6**, all the disclosed
  name + -лӧн genitive device — Adamлӧн (5:27), Pharaohлӧн
  (7:127, 40:28, 40:37), Abrahamлӧн (11:74), Josephлӧн
  (12:58). Other mixed tokens: NONE.

## 5. Dictionary and inventories — PASS, exact

- Seated dictionary **1,317 entries**: replicated at this desk
  from the engine's own construction without running it —
  core (FUNC 109 + PRON 45 + NUM 29 + OVERRIDE 376, with
  overlaps) plus the 712 gloss-matched seats of
  `work/dict_koi.json`, expanded by the engine's plural-key
  rule, totals exactly 1,317 RAW entries; `work/unverified-
  dict.json` is an empty object, so **dropped as unverified:
  0**, as claimed. Unmatched curated keys: 283, as logged.
- Inventories, recounted from `sources/`: GiellaLT giella-koi
  lemmas **77,661**; glossed dictionary lemmas 14,725;
  gt-norm paradigm forms **15,533**; English Wiktionary
  Komi-Permyak headwords **334**. All verified exactly.

## 6. Cyrillic attestation screen — PASS on attestation, with the §7 exception

This checker's own screen (koi inventories + glossary lemmas +
disclosed regular derivations: doubled-consonant plural,
case endings, present -ӧ, -ӧм nouns, -ісь agents):

- Distinct Cyrillic tokens **841** — verified. Tokens
  containing ӧ: 369 types; containing і: 35 types — both as
  reported. The Permyak letters are genuinely used.
- Untraced tokens: **0**, with one qualification that is the
  subject of §7: two tokens — эскісьяс (×272) and вӧчісьяс
  (×67) — trace only if a plural decomposition in **-яс** is
  admitted. Every other token of the 841 traces on Permyak
  inventories and Permyak derivations alone. `verify.py`'s
  "0 untraced" is therefore literally reproduced, but its
  ending-stripping decomposition is permissive enough to
  absorb the -яс ending letter by letter, so its screen
  cannot see the §7 fault — the same construction lesson as
  the Zyrian lane's screens, in a milder form.

## 7. The koi/kpv attestation fence — FAIL (one bounded fault)

The build claims (BUILD-REPORT; ATTESTATION-AUDIT): two Zyrian
forms caught in the first engine draft — войтыр and "the
Zyrian plural shapes" — "were removed and the build re-run
before these figures were taken."

- **войтыр: truly absent.** 0 occurrences in the store; the
  Permyak seat отир is seated instead (e.g. 7:163, 9:3). The
  only вой- tokens are вой "night" (×95) and война "war" (×3,
  a flagged attested loan). PASS on this item.
- **The Zyrian irregular-plural table: truly replaced.** The
  engine's IRREG_PLURAL now seats Permyak shapes (морттэз,
  аннез, кагаэз, коккез, пиннез, гӧтыррез, ёрттэз), verified
  in the engine source and in the text. PASS on this item.
- **But Zyrian plural shapes are NOT absent from the text.**
  Two tokens carry the Zyrian plural suffix **-яс**:
  эскісьяс "believers/disbelievers" (272 tokens, 250 seats)
  and вӧчісьяс "doers/wrongdoers" (67 tokens, 66 seats) —
  **339 tokens in 313 seats** in all (full seat list below).
  Ground, in the same breath: the Komi-Permyak plural marker
  is /ez/ (эз/ез) with stem-final consonant doubling — stated
  in BUILD-SPEC's own grammar ("plural: stem-final consonant
  doubled + -эз"), in the book's front matter, and in the
  standard grammar of Permyak; -яс is the Komi-Zyrian nominal
  plural (cf. the Zyrian lane, where эскысьяс is its regular
  agent plural). No form in the harvested koi paradigm files
  (15,533 forms) ends in -сьяс, and no koi inventory attests
  either token. Their provenance is visible in the lane's own
  files: `work/dict_core_koi.py` PHRASES (lines 261–263) seats
  ("believers", "Эскісьяс"), ("disbelievers", "Оз эскісьяс"),
  ("wrongdoers", "Лёк вӧчісьяс") — the model lane's phrase
  table copied across with і substituted (the Zyrian engine
  seats the identical phrases with Эскысьяс / Вӧчысьяс). This
  is the same copying route by which войтыр entered the first
  draft; the removal caught the irregular table and missed
  the phrase table.
- The fault is internally inconsistent as well as cross-fence:
  the book itself pluralises the same agent class in Permyak
  elsewhere — ыстісььэз "messengers" (3:184), адззылісььэз
  "witnesses" (2:282) — so one reader-facing rule does not
  hold across the book's core terms.
- No other Zyrian-only form was found seated as Permyak.
  Screen run at this desk: every Cyrillic token was compared
  against the kpv GiellaLT lemma inventory (193,665 lemmas);
  the only tokens standing in the kpv inventory but not in
  any koi inventory are disclosed paradigm/derivation forms
  (шуӧ, ись, кольӧ, эскӧм, мучитӧм, прӧститӧм, вӧчӧм, восьтӧм,
  кув, дзеб, ов — present stems, the split elative token, and
  -ӧм devices, each traced to a koi infinitive). The Zyrian
  lane's split seats (гӧнец, идӧг, кевмӧм, буркыв, грек, море,
  керӧс, мезӧс, милӧсьт, енэж, тӧлысь, ыстысь) occur 0 times
  each in this text. Core-term consistency otherwise holds:
  angel ангел only, messenger ыстісь only, sin мыж only,
  prayer келмӧм / pray кеймыны, star кодзув only (the matched
  dictionary's кӧдзыв never reaches the text), heaven енӧж
  only, hell ад only — the Zyrian lane's §8.1 splits are
  absent here.

### Full seat list for the §7 failure (313 seats)

Seats carrying эскісьяс (250): 2:8, 2:19, 2:24, 2:34, 2:89,
2:90, 2:91, 2:93, 2:97, 2:104, 2:105, 2:109, 2:191, 2:223,
2:248, 2:254, 2:278, 2:285, 3:28, 3:49, 3:68, 3:72, 3:91,
3:100, 3:110, 3:121, 3:122, 3:124, 3:131, 3:139, 3:141,
3:152, 3:160, 3:164, 3:166, 3:175, 3:179, 3:196, 4:18, 4:37,
4:51, 4:84, 4:95, 4:101, 4:102, 4:103, 4:115, 4:139, 4:140,
4:141, 4:144, 4:146, 4:151, 4:162, 5:11, 5:23, 5:43, 5:44,
5:54, 5:57, 5:82, 5:88, 5:112, 6:122, 6:130, 7:2, 7:50, 7:72,
7:75, 7:85, 7:101, 7:143, 8:1, 8:2, 8:4, 8:5, 8:7, 8:14,
8:17, 8:18, 8:19, 8:30, 8:59, 8:62, 8:64, 8:65, 8:74, 9:2,
9:13, 9:16, 9:26, 9:32, 9:49, 9:55, 9:61, 9:62, 9:68, 9:72,
9:73, 9:79, 9:85, 9:105, 9:107, 9:111, 9:112, 9:120, 9:122,
9:123, 9:125, 9:128, 10:2, 10:57, 10:87, 10:99, 10:103,
10:104, 11:42, 11:53, 11:86, 11:120, 12:103, 13:14, 13:31,
13:32, 13:35, 14:2, 14:41, 15:77, 15:88, 16:27, 17:8, 17:9,
17:82, 18:2, 18:80, 18:100, 19:83, 21:30, 23:1, 23:117, 24:2,
24:3, 24:17, 24:19, 24:31, 24:47, 24:51, 24:62, 25:26, 25:52,
26:3, 26:8, 26:51, 26:67, 26:103, 26:114, 26:118, 26:121,
26:139, 26:158, 26:174, 26:190, 26:215, 27:2, 27:77, 28:47,
28:86, 29:44, 29:47, 29:54, 30:4, 30:8, 30:47, 33:1, 33:6,
33:8, 33:11, 33:22, 33:23, 33:25, 33:37, 33:43, 33:47,
33:50, 33:59, 33:64, 33:73, 34:20, 34:31, 35:39, 37:29,
38:4, 39:71, 40:14, 40:25, 40:50, 40:74, 40:85, 41:7, 42:26,
44:12, 45:3, 47:10, 47:11, 47:34, 48:4, 48:5, 48:12, 48:13,
48:18, 48:20, 48:26, 48:29, 49:9, 49:10, 49:15, 50:2, 51:35,
51:55, 52:42, 54:8, 54:43, 57:8, 57:20, 58:4, 58:5, 58:10,
59:2, 60:10, 60:11, 61:8, 61:13, 63:8, 64:2, 64:13, 66:4,
66:9, 67:20, 67:28, 69:50, 70:2, 71:26, 71:27, 74:10, 74:31,
83:34, 83:36, 85:7, 85:10, 109:1.

Seats carrying вӧчісьяс (66): 2:35, 2:59, 2:124, 2:145, 2:165,
2:246, 2:254, 2:270, 3:128, 3:192, 5:72, 5:107, 6:21, 6:93,
6:129, 6:135, 7:5, 7:41, 7:44, 8:25, 9:23, 9:47, 10:39,
10:106, 11:18, 11:31, 11:83, 11:94, 11:116, 14:13, 14:22,
14:42, 15:78, 17:47, 17:82, 17:99, 18:50, 19:38, 19:72,
21:3, 21:29, 21:59, 21:64, 21:87, 21:97, 22:53, 25:37,
28:37, 28:59, 29:14, 29:31, 30:29, 34:31, 35:40, 39:51,
40:52, 42:8, 43:65, 45:19, 49:11, 59:17, 60:9, 62:7, 71:24,
71:28, 76:31. (Union of the two lists: 313 seats; three seats
— 2:254, 17:82, 34:31 — carry both tokens.)

## 8. Flagged thin/device seats, clause fidelity, book face

- Flagged seats rule as disclosed, singly: милӧсьта (mercy —
  inventory lemma, family gloss-attested by милуйтны; the
  single-stem Basmalah seating is disclosed on the book's
  face and is accepted as a disclosed thin seat); ен for Lord
  (disclosed device; "Lord of the worlds" Муэзлӧн Ен verified
  at 1:2); веськыт / веськытлун (straight/just device,
  disclosed); казьмӧтны (remind seated for warn, disclosed);
  мезмӧтны (free/release seated for save, disclosed); келмӧм
  (prayer, Usol.-dialect gloss flag stands); видз (fasting,
  "пост" gloss attested, meadow homonym flagged); дон (reward,
  "price" — thin, flagged); гижӧт (scripture generic, "writing,
  letter" — flagged); пас, кодзув, саридз, мыж, джинн (lemmas
  attested, own glosses not carried — flagged thin, as
  disclosed). All stand as honest disclosed seats; none is a
  fail ground. The attested-loan list is likewise seated only
  as flagged.
- Disclosed candidates adjudicated: "peace" rides му —
  ACCEPTED: the seat's own gloss is «земля; мир», and Russian
  мир carries "peace" as well as "world"; 36:58 («Му — шуӧ ись
  медся милӧсьта ен») and 19:62 are therefore gloss-supported,
  not traps. "Understand" rides артавны at the sampled seats
  (2:44, 2:73) — a gloss-matched drift (consider/count-out),
  disclosed; recorded as a candidate for a future dictionary
  pass, not a fail ground. "Pay" rides мед — disclosed
  candidate, likewise recorded. Seat 1:7's final clause seats
  the guide verb нуӧтӧ at the "misguided" neighbourhood
  («ни эна кин лоӧ нуӧтӧ»), where the glossary's own astray
  seat is вошны — a real semantic mismatch at one clause,
  disclosed in the disclosure as a candidate; it is recorded
  here as CONFIRMED and listed for remediation (§10), but as
  a single disclosed clause it does not carry the verdict.
- Clause-fidelity sample (1:5–7, 2:255, 5:3, 19:62, 24:35,
  27:30, 30:21, 36:58, 39:7, 48:8, 55:1, 99:1, 112:1–4, plus
  the number battery): within the disclosed plain style,
  clauses are carried by a Permyak seat, a disclosed device,
  or a GAP marker, with no dropped clause found apart from
  the 1:7 item above; negations ride оз throughout; 55:1 is
  «Милӧсьта.» whole (the seat the Zyrian draft left in
  English); 2:163 renders both mercy names in Permyak.
- Number battery — PASS in full: 18:25 nine (ӧкмыс, with
  куим дасдас "three hundred"); 7:142 thirty + ten = forty
  (куимдас, дас, нёльдас); 12:4 eleven (дасӧтік); 38:23
  ninety-nine and one (ӧкмысдас ӧкмыс, ӧтік); 17:101 nine;
  69:7 seven and eight; 2:234 four and ten; 23:17 seven;
  11:13 ten.
- Book face and licences — PASS: the manuscript carries
  DRAFT — NOT PUBLISHED (twice, plus the front-matter status
  line), the first-pass build tier stated plainly, the GAP
  census on its face in the figures verified in §3 (792 /
  5,444 / 16,840), the single-stem Basmalah and the Lord
  device disclosed, the New Testament-only Bible control
  stated with no complete-Bible claim, and an explicit "No
  first claim" paragraph — no first-translation claim appears
  anywhere in the manuscript, the build report, or the
  disclosure. Licences verify as recorded: the lang-koi
  LICENSE file on disk is LGPL v3, as recorded; Wiktionary
  CC BY-SA; the Bible control and the 1985 dictionary
  tradition cited by fact only. Nothing for this lane stands
  on the GitHub shelf (no koi folder under
  robert-tilford-quran/translations/), as the build's STOP
  state claims.

## 9. SPECIAL RULING — the GAP tier

**Ruling: PASS-WITH-GAP-TIER-RESERVATION.**

Ground, in the same breath as the figures: the GAP tier —
5,444 of 6,236 seats (87.3%) carrying 16,840 visible markers,
792 verses clean, a clean share of **12.7%** against
Komi-Zyrian's 21.9% (1,366 clean) — breaks no house rule. No
house rule sets a GAP ceiling; the GAP law requires that a
seat with no attested form be held open visibly, that no form
be invented or silently borrowed, and that the census be
disclosed on the book's face. On the tier's own ground the
first and third hold exactly (§§3, 8: the markers are really
there, counted to the digit, and the census stands on the
face). The second — no silent borrowing — holds for the GAP
tier itself; its one breach in the book is the §7 -яс plural,
which is a fence failure on seated core terms, not a GAP
practice failure, and it is ruled on there, not here. The
comparison with Komi-Zyrian measures degree, produced by a
disclosed difference of kind: a first-pass engine render over
a 1,317-entry verified dictionary for a language whose open
attested base is thinner, its build tier stated plainly on
its face. A heavier honest GAP tier is not a dishonest book.

Consequences, spelled out as the Zyrian checker spelled them:

- **PASS on the GAP tier** (not given) would have meant the
  tier needs no reservation on the record. Withheld: at 12.7%
  clean this is the GAP-heaviest draft the desk has produced,
  and any future claim about the book must carry the census
  with it, in the same breath.
- **FAIL on the GAP tier** (not given) would have meant a
  GAP-reduction pass must precede any landing. Withheld: no
  ceiling exists in house law, and the tier's honesty is
  verified, not merely claimed.
- **PASS-WITH-GAP-TIER-RESERVATION** (given) means: the GAP
  mass itself is landable as DRAFT — NOT PUBLISHED once the
  §10 remediation is done and re-checked; no GAP-reduction
  pass is required, and none should be substituted for the
  §10 repair.

## 10. Verdict and remediation

**Overall verdict: FAIL** — on §7 alone: the Zyrian plural
shapes the build reports as caught and removed in fact stand
in the text as эскісьяс (×272) and вӧчісьяс (×67), 339 tokens
in 313 seats, on three of the book's core terms (believers,
disbelievers, wrongdoers), contradicting BUILD-SPEC's own
plural rule, the front matter's plural statement, and the
attestation audit's removal claim. Every other head of claim
passes, several exactly: §§1–5 (recount, grid, Basmalah
including 1:3, GAP census, retained Latin 0, mixed script
exactly the 6 disclosed, dictionary 1,317 / 0 dropped,
inventories 77,661 / 15,533 / 334), §6 (841 Cyrillic tokens,
0 untraced on Permyak derivations), §8 (flagged seats as
disclosed, number battery, honest labelling), and the GAP
tier under §9's reservation. As in the Zyrian lane, the fail
is bounded and remediable; it is not a rebuild.

Remediation required before a re-check, in order:

1. **Re-seat the two -яс plurals in Permyak shape** at all
   313 seats of §7's list — the book's own Permyak agent
   plural (cf. ыстісььэз, адззылісььэз): эскісьяс →
   эскісььэз, вӧчісььэз likewise for вӧчісьяс — in the
   PHRASES table of `work/dict_core_koi.py`, then re-run the
   build so store, text, JSON, and manuscript move together.
2. **Correct the record in the same pass:** the attestation
   audit's and build report's "Zyrian plural shapes removed"
   sentence must be amended (dated addendum, per house
   practice) to name the phrase-table residue and its repair;
   and `verify.py`'s attestation decomposition should be
   tightened so a -яс ending cannot be absorbed letter by
   letter — the corrected screen must return the two tokens
   as candidates on the unrepaired text.
3. Small items in the same pass: seat 1:7's final clause
   re-seated (вошны family or GAP), and the audit's standing
   GAP-family list reconciled with the seated generic alms
   seat корӧм (§3).

Nothing in this list requires Robert's ruling or a
GAP-reduction pass: every item is a repair under the standing
gate law. After remediation the lane needs a fresh independent
re-check PASS before landing, exactly as its disclosure
already states. This checker edited no text, landed nothing,
shelved nothing, committed nothing, and pushed nothing; the
draft stands where the build left it.

— Independent checker, 2026-11-28. All figures recomputed at
this desk from the files of record with this checker's own
scripts; instrument output treated as candidates until
adjudicated, per house practice.
