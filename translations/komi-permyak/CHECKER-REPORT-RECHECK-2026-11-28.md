# Komi-Permyak (koi) Quran draft — INDEPENDENT RE-CHECK (2026-11-28)

Re-checker stance: this re-checker built none of the text and did
none of the remediation. Every figure below was recomputed with
this re-checker's own scripts from the files of record
(verses-store.json, quran-koi.txt/.json,
ayah-companion-manuscript-KOI.md, master-verses.json,
CHECKER-REPORT-INDEPENDENT-2026-11-28.md,
REMEDIATION-RECORD-2026-11-28.md, BUILD-REPORT-KOI-2026-11-28.md,
ATTESTATION-AUDIT-2026-11-28.md,
FLAGS-AND-GAPS-DISCLOSURE-KOI-2026-11-28.md, BUILD-SPEC.md,
verify.py as tightened, work/dict_core_koi.py, glossary.md, and
the harvested inventories in sources/). Nothing was edited in
the text, landed, shelved, committed, or pushed by this check.

## Verdict (stated first)

**PASS — with the GAP-tier reservation of the first checker's
§9 ruling carried forward unchanged (see §6 below), and one
disclosed residual recorded in §2 that was not a §10
remediation item.**

Every item of the first checker's §10 remediation list is
verified complete at the seat level: the Zyrian plurals are
gone and their Permyak replacements stand at exactly the
checker's 313 listed seats (§1); seat 1:7 and all six other
"misguided" seats now seat вошны (§2); the alms reconciliation
is consistent across the audit addendum, BUILD-SPEC, and the
glossary (§3); the record was corrected by dated addendum
without rewriting the originals, and verify.py is tightened so
the fault class can no longer be absorbed (§4); and every
headline figure of the remediated book still holds to the
digit (§5).

## 1. The Zyrian plural fault — GONE; replacements exact (§7/§10.1)

Recomputed from the store with this re-checker's own tokeniser
(GAP interiors excluded):

- Tokens ending in **-яс: 0** in verses-store.json, 0 in
  quran-koi.txt, 0 in the manuscript. The old fault tokens
  эскісьяс and вӧчісьяс occur 0 times each in all three.
- **эскісььэз: 272 tokens in 250 seats. вӧчісььэз: 67 tokens
  in 66 seats.** This re-checker parsed the first checker's
  §7 seat lists out of CHECKER-REPORT-INDEPENDENT-2026-11-28.md
  (250 and 66 seats) and compared set-for-set: **both lists
  are exactly equal** to the seats now carrying the
  replacement forms — no seat added, no seat lost. Union:
  **313 seats**, exactly the checker's union. The three
  both-token seats are exactly **2:254, 17:82, 34:31**, each
  verified to carry both new forms.
- Source seat verified in work/dict_core_koi.py PHRASES:
  ("believers", "Эскісььэз"), ("disbelievers", "Оз
  эскісььэз"), ("wrongdoers", "Лёк вӧчісььэз") — the Permyak
  agent plural (stem-final сь doubled + -эз), the book's own
  shape in ыстісььэз and адззылісььэз.
- **Whole-text screen for any other Komi-Zyrian-only form:**
  every distinct Cyrillic token of the book (841) was compared
  against the Komi-Zyrian (kpv) GiellaLT/kaikki inventory held
  in the sibling lane (193,842 lemmas/forms) and against the
  koi inventories. The only tokens standing in the kpv
  inventory but not in a raw koi inventory are the same
  disclosed paradigm/derivation forms the first checker
  traced (шуӧ, ись, кольӧ, эскӧм, мучитӧм, прӧститӧм, вӧчӧм,
  восьтӧм, кув, дзеб, ов, plus the pronoun stem сы) — each a
  present stem, -ӧм device, or paradigm form traced to a koi
  infinitive or the proofread paradigm tests. No other
  candidate. The Zyrian lane's split seats (гӧнец, идӧг,
  кевмӧм, буркыв, грек, море, керӧс, мезӧс, милӧсьт, енэж,
  тӧлысь, ыстысь) occur 0 times each; войтыр 0 times (Permyak
  отир seated); эскысьяс / вӧчысьяс (Zyrian spellings) 0
  times. No koi paradigm-test form (15,533) ends in -сьяс.
  Core-term consistency holds as the first checker found it
  (ангел, ыстісь, мыж, келмӧм, кодзув only — кӧдзыв 0 —
  енӧж, ад).

## 2. Seat 1:7 and the вошны family (§8/§10.3)

- 1:7 now reads: «Туй эна тэ кутӧ ⟦GAP: blessed⟧, оз эна
  паныт кинӧ ло ⟦GAP: anger⟧, **ни эна кин лоӧ вошӧ**.» The
  final clause seats **вошӧ**, the present of вошны — the
  glossary's own astray seat. The guide verb no longer stands
  at the "misguided" neighbourhood of this clause.
- The Master's exact token "misguided" occurs at exactly 7
  seats (recomputed from master-verses.json): 1:7, 16:25,
  18:104, 26:86, 27:41, 36:47, 56:51. **All seven now seat
  вошӧ** (verified seat by seat in the store). At 27:41 the
  нуӧтӧ that also appears in the seat belongs to the Master's
  separate "guided" clause of the same verse ("…or be among
  the misguided" is the вошӧ clause) — not a residue.
- Source seat verified: OVERRIDE in work/dict_core_koi.py now
  carries "misguided": ("вошны", "V"), with the remediation
  comment naming the mis- prefix-stripping fault it closes;
  the replicated dictionary (§5) seats it.
- **Sample of the seats remediation left as built and
  disclosed (REMEDIATION-RECORD §2) — recorded, not hidden:**
  the verb tokens "misguide" (6:125, 7:155, 16:37, 22:4) and
  "misguides" (7:186, 13:33, 18:17, 40:33) still seat the
  guide verb **нуӧтӧ**, indistinguishable in the text from
  "guide" at the same seats (e.g. 7:155 "You misguide
  whomever You will, and guide whomever You will" renders
  both verbs нуӧтӧ; 16:37 likewise). This is the same
  prefix-stripping route, one word-family over. It was NOT
  among the first checker's §10 required items — the checker
  confirmed only the "misguided" seats — and the remediation
  record disclosed it in the open and left it for this sample.
  It is recorded here as a known disclosed residual for any
  future dictionary pass; it does not contradict any §10
  item, and it is not a ground to fail a remediation whose
  required list it was never on. The noun "misguidance"
  (7:30, 14:18, 16:36) GAP-marks at all three seats —
  verified; no fault there.

## 3. Alms reconciliation (§3/§10.3) — CONSISTENT

The same reconciled rule stands in all three places, in the
same terms: **alms as a technical term (zakat) is a standing
GAP family; the generic alms/charity seat rides the attested
корӧм**, exactly as the generic scripture seat rides гижӧт.

- ATTESTATION-AUDIT addendum (2026-11-28): states the rule
  and the ground.
- BUILD-SPEC GAP policy: clarified in place, dated
  2026-11-28, same rule, same ground.
- glossary.md core section: an explicit entry "alms /
  charity (generic) — корӧм" with the ground stated and a
  cross-reference to the audit addendum.
- Ground verified at this desk: the giella-koi dictionary
  entry for корӧм carries the Russian glosses "милостыня,
  подаяние" (alms, almsgiving) among its senses
  (sources/koi-gloss-dict.json).
- Text verified: all 8 Master seats carrying the word "alms"
  (2:83, 2:110, 5:12, 9:5, 24:37, 41:7, 58:13, 98:5) seat
  корӧм — including 2:110 «сетӧ корӧм» and 5:12 «мед корӧм»
  as cited. No seat changed by this item, as the remediation
  record states; the discrepancy was in the family list, and
  the list is now reconciled everywhere it appears.

## 4. Record correction and the tightened screen (§6/§10.2)

- **Addenda correct; originals unrewritten.** In each of the
  three closed records the original removal sentence still
  stands verbatim in the body (verified by normalised-text
  match at this desk): the attestation audit's "caught by the
  attestation screen and removed before the final build"
  sentence — including its own residue instance "disbelievers
  — Оз эскісьяс" in the Faith section — the build report's
  "Two Zyrian forms caught in the first engine draft (войтыр
  and Zyrian plural shapes) were removed…" sentence and its
  original 1,317-entry figure, and the disclosure's repeated
  removal sentence. Each file then carries a dated
  **Addendum — 2026-11-28** naming the phrase-table residue
  (эскісьяс ×272, вӧчісьяс ×67, 313 seats), its repair, the
  1:7 item, and the alms reconciliation. House practice
  (dated addendum, never silent rewrite) is followed exactly.
- **verify.py tightened, verified in source:** the
  single-letter endings ("а", "я", "м", "д", "с", "н") are
  absent from its ENDINGS list, and traces() rejects any
  non-inventory token ending in -яс outright, with the
  remediation comment naming the letter-by-letter absorption
  it closes.
- **Demonstration recomputed at this desk:** this re-checker
  reconstructed the unrepaired text in memory (ьэз forms
  swapped back to яс) and ran its own implementation of the
  tightened tracing rules over it: the screen returns
  **exactly two untraced candidates — эскісьяс ×272 and
  вӧчісьяс ×67 — and no others.** On the repaired text the
  same screen returns 0 (see §5). The corrected screen can
  see the fault class, as §10.2 required.

## 5. Headline figures of the remediated book — ALL HOLD

Recomputed independently; every figure exact:

- **Verses 6,236 / 6,236.** Store seat-set exactly equal to
  the Master seat-set in both directions; per-surah grid
  exact against the standard grid, mismatches NONE; empty
  seats NONE; "redacted" NONE. quran-koi.json, flattened,
  equals the store seat for seat (6,236 seats).
- **Basmalah 113** in quran-koi.txt (and 113 in the
  manuscript): seat 1:1 equals «Енлӧн нимӧн, Милӧсьта,
  Милӧсьта.» character for character; **seat 1:3 equals
  «Милӧсьта, Милӧсьта.» exactly**.
- **GAP census unchanged: 5,444 GAP seats, 16,840 GAP
  markers, 4,728 distinct GAP terms, 792 verses without a
  marker.** Bracket integrity 16,840 ⟦ / 16,840 ⟧; the
  manuscript carries 16,841, the one extra being its
  front-matter explanatory example. Top terms recomputed
  identical (used ×149, things ×108, belongs ×73, should
  ×50, doubt ×48, fight ×43, blessed ×40, considered ×40,
  reached ×39, wronged ×39). No remediation item added or
  removed a marker — confirmed by the unchanged census.
- **Seated dictionary 1,318 entries.** This re-checker
  replicated the engine's dictionary construction in memory
  (FUNC + PRON + NUM + OVERRIDE, then the 712 gloss-matched
  seats of work/dict_koi.json expanded by its plural-key
  rule, each entry passed through the engine's verification
  rule against the koi inventories): RAW 1,318, seated
  **1,318**, **dropped as unverified 0** (work/unverified-
  dict.json is an empty object, as logged; unmatched curated
  keys 283, as logged). The +1 over the pre-remediation 1,317
  is the direct "misguided" seat of §2, present in the
  replicated dictionary as ("вошны", "V").
- **Inventories:** GiellaLT giella-koi lemmas 77,661;
  glossed dictionary lemmas 14,725; gt-norm paradigm forms
  15,533; English Wiktionary Komi-Permyak headwords 334 —
  all recounted exact.
- **Script purity:** retained Latin on whitespace tokens,
  GAP interiors excluded, against the explicit allowlist
  extracted from verify.py: allowlisted **129 types / 1,056
  tokens**; **non-allowlist retained Latin 0 types / 0
  tokens**; lowercase-initial Latin types NONE.
- **Mixed-script tokens: exactly the 6 disclosed** name +
  -лӧн genitive tokens — Adamлӧн (5:27), Pharaohлӧн (7:127,
  40:28, 40:37), Abrahamлӧн (11:74), Josephлӧн (12:58).
  Other mixed tokens: NONE.
- **Cyrillic attestation (this re-checker's own tightened
  screen, §4 rules): 841 distinct Cyrillic tokens, 0
  untraced.** Tokens containing ӧ: 369 types; containing і:
  35 types — counts unchanged from before remediation, the
  two -яс types replaced one-for-one by the two -ьэз types,
  which trace by the doubled-consonant plural rule to the
  seated stems эскісь and вӧчісь.
- **Stop state:** the manuscript's face still says DRAFT —
  NOT PUBLISHED (twice). There is no Komi-Permyak folder on
  the GitHub shelf under
  ~/workspace/robert-tilford-quran/translations/ (the only
  folder whose name contains "koi" is mountain-koiali, whose
  contents are a KPX manuscript — a different item, not this
  lane). Nothing in this check landed, shelved, committed,
  or pushed anything.

## 6. The GAP-tier ruling — STILL APPLIES

The first checker's §9 ruling was **PASS-WITH-GAP-TIER-
RESERVATION**, given on the tier's own figures. Those figures
are unchanged by the remediation — 5,444 of 6,236 seats
(87.3%) carrying 16,840 visible markers, 792 verses clean, a
clean share of 12.7%, the census disclosed on the book's
face, no marker added or removed (§5). The §7 breach that
the ruling expressly carved out of the GAP tier ("a fence
failure on seated core terms, not a GAP practice failure…
ruled on there, not here") is now repaired and verified in
§1. **The ruling therefore still applies to the remediated
text in its own terms: the GAP mass itself is landable as
DRAFT — NOT PUBLISHED now that the §10 remediation is done
and this re-check has passed it; no GAP-reduction pass is
required, and none should be substituted for the §10 repair.
Any future claim about the book must carry the census with
it, in the same breath.**

## 7. Failure seat lists

None. No head of this re-check failed, so there are no
failure seat lists to give. The one known residual — the
"misguide/misguides" verb seats 6:125, 7:155, 16:37, 22:4,
7:186, 13:33, 18:17, 40:33 seating нуӧтӧ, disclosed by the
remediation record itself as left as built — is listed in
full in §2 so it travels with this PASS, in the same breath.

— Independent re-checker, 2026-11-28. All figures recomputed
at this desk from the files of record with this re-checker's
own scripts; instrument output treated as candidates until
adjudicated, per house practice. This re-check edited no
text, landed nothing, shelved nothing, committed nothing,
and pushed nothing.
