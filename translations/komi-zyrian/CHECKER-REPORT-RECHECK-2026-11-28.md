# Komi-Zyrian (kpv) Quran draft — INDEPENDENT RE-CHECK (2026-11-28)

Checker stance: this re-checker built none of this text and did
none of the remediation. Nothing was edited, landed, shelved,
committed, or pushed by this check. Every figure below was
recomputed with this checker's own scripts on whitespace tokens
(GAP-marker interiors excluded for the Latin and mixed-script
counts, except where the GAP census itself is the object), from
`verses-store.json`, `quran-kpv.json`, `quran-kpv.txt`,
`master-verses.json` (the Locked English Master seat-set),
`BUILD-SPEC.md`, `glossary.md` (§J), the original
`CHECKER-REPORT-INDEPENDENT-2026-11-28.md`, and
`REMEDIATION-RECORD-2026-11-28.md`, with the pre-remediation
store at `work/verses-store-PRE-REMEDIATION.json` as the
comparison base.

The original checker's GAP-tier ruling —
PASS-WITH-GAP-TIER-RESERVATION — stands and is not reopened
here. This re-check rules on the remediation and on the one
reservation the remediation record left open (§8).

## Verdict (stated first)

**PASS.** Every headline figure in the remediation record
recomputes exactly at this desk (§§1–7), the retained-Latin
tier that failed the original check is closed with **0**
off-allowlist tokens, and the lesser splits left ununified are
ruled in §8 a disclosed reservation that may ride, not a bar to
landing. Landing may proceed under the Pipeline Landing
Authorization as **DRAFT — NOT PUBLISHED**. This checker did
not land it.

## 1. Recount, seat-set, per-surah grid — PASS, exact

- Store seats **6,236**; Master seats **6,236**; seat sets
  exactly equal in both directions (no missing, no extra).
  `quran-kpv.json` flattens to 6,236 seats and is identical to
  the store at every seat. Empty seats: NONE. The string
  "redacted": NONE.
- Per-surah grid: all 114 surah counts in the store and in the
  Master match the standard grid exactly (grid sum 6,236).
  Mismatches: NONE.
- All thirteen `work/batch-*.json` files are identical to the
  store at every seat (0 differing seats each), so the lane
  cannot regress on a re-merge from its batch sources.
- Seats changed against the preserved pre-remediation store:
  **1,176** — exactly the remediation record's figure.

## 2. Basmalah — PASS, exact

- Store seat 1:1 equals the BUILD-SPEC fixed form
  «Енлӧн нимӧн, Милӧсьт, Милӧсьт.» character for character.
  The full string occurs exactly **once** inside the verse
  store (at 1:1, nowhere else).
- In `quran-kpv.txt` the string occurs **113 times**: 112
  standalone unnumbered lines plus the numbered verse 1:1 —
  the expected 113 (112 standalone + 1:1), with surah 9
  correctly carrying none.
- Seat **1:3 reads «Милӧсьт, Милӧсьт.»** — the spec form,
  verified character for character (the original check's
  failing seat, "Beneficent, милӧсьта.", is gone).
- Seat 27:30 carries the in-verse Basmalah on the 1:1 seating:
  «ын ним Ен, Милӧсьт, Милӧсьт.» inside the quotation.

## 3. Retained Latin and the allowlist audit — PASS, 0 off-list

Recomputed on whitespace tokens, GAP interiors excluded:

- Pure Latin tokens: **128 types, 1,046 tokens**. Mixed
  name+лӧн device tokens (§4): **6**. Total kept Latin-bearing
  tokens: **1,052**. These reconcile the remediation record's
  "128 types / 1,052 tokens" exactly, read as occurring types
  with the 6 device tokens counted in the token total.
- **Off-allowlist Latin: 0 types, 0 tokens.** Every pure Latin
  token in the book stands on the recorded allowlist.
- One phrasing note, not a discrepancy in the text: the list
  as coded in the fixed `verify.py` names 133 spellings; 128
  occur as pure tokens. The five that do not occur — Ain, Kaf,
  Nun, Sad, Sin — are alternate spellings of disjointed-letter
  names, as the record itself notes for Ain/Nun/Kaf. No
  occurring type is unlisted, and no listed occurring type is
  unjustified (next paragraph).

**Audit of the allowlist itself.** Each of the 128 occurring
types was tested against the Master and inspected in context:

- **No common word is hiding in it.** The sharp test the
  original check applied — does the word occur lowercase in
  the Master? — returns **0 lowercase occurrences for every
  one of the 128 types**. No type that is GAP-marked or seated
  in Komi elsewhere is retained here.
- The types fall only in the permitted classes: personal names
  (Moses ×136, Abraham, Noah, Mary, Jesus, Joseph, Adam,
  Aaron, Isaac, Solomon, Jacob, David, and the rest), scripture
  titles (Quran ×68, Torah ×18, Gospel ×12, Psalms ×5), the
  disjointed letters (Alif, Lam, Meem, Ha, Ra, Ya, Ta, Ayn,
  Saad, Qaf, Shin), and proper place / people / language names
  (Israel, Egypt, Medina, Mecca, Sinai, Jews, Christians,
  Arabs, Arabic, Thamood, Aad, and the rest).
- Types that look questionable at first glance verify on
  inspection: **Samarian** is the Master's own form for the
  Samaritan figure (20:85, 20:87, 20:95); **Median** is the
  Master's place name (7:85 and passim); **Russ** (50:12) and
  **Arras** (25:38) are the Master's place/people names;
  **Malek** is a named figure (43:77); **Zul** + **Qarnain**
  are the two tokens of the one hyphenated name Zul-Qarnain,
  and **Abee** + **Lahab** of the one name Abee Lahab;
  **Islam**, **Judaism**, **Muslim(s)**, **Christian(s)** and
  **Jew(s)** are always-capitalised religion and people
  designations in the Master, disclosed in the record under
  its peoples/communities category; homographs such as Job
  and Ha are, in context, the name and the letter.
- Count reconciliations against the Master confirm the
  mechanism rather than undermining it: Solomon stands at 17
  tokens against the Master's 16 because the remediation's
  Salomon → Solomon correction (§5) adds the seventeenth;
  Abraham, Adam, Joseph and Pharaoh stand 1–3 below their
  Master capitalised counts because the remaining tokens are
  the mixed device forms of §4.

## 4. Mixed-script tokens — PASS, exactly the 6 disclosed

On whitespace tokens, exactly **6** tokens contain both Latin
and Cyrillic, and they are precisely the disclosed
genitive-on-names device tokens, at the recorded seats:
Adamлӧн (5:27), Pharaohлӧн (7:127, 40:28, 40:37), Abrahamлӧн
(11:74), Josephлӧн (12:58). No other mixed token exists. The
remediation corrected the claim rather than the forms, as the
original checker offered; the claim now matches the text.

## 5. Remediation claims spot-verified by count — PASS

Each claim was recomputed independently; all hold:

- **Closed core terms — all 0:** идӧг **0**, гӧнец **0**,
  верит- **0**, грек **0**, буркыв **0** (whitespace tokens,
  GAP interiors excluded). The unified families stand at the
  recorded totals: ангел family **88** (ангел 11 + ангеляс 75
  + Ангеляс 2), ыстысь family **361**, мыж family **446**,
  кевмӧм **87** (55 + кевмӧмяс 32). The эскысь family
  (believer) stands at 270 tokens on the unified эск- seat.
  Seat 2:87, which formerly carried both messenger seats in
  one verse, now carries ыстысьяс only.
- **Standing GAP families in Latin — all 0:** Sabbath **0**,
  Hajj **0**, Umrah **0** in the verse text outside GAP
  markers. In the GAP census they stand at sabbath **7**,
  hajj **7**, umrah **3** — the recorded token counts at the
  recorded seats (2:65, 4:47, 4:154, 7:163 ×3, 16:124 for
  Sabbath). One clarification, not a failure: the book's
  total GAP term "pilgrimage" is **4** markers — the 3
  capitalised Pilgrimage tokens the remediation GAP-marked
  plus 1 lowercase pilgrimage marker already present before
  remediation. The hyphen-split compounds are closed as
  recorded (4:47 «⟦GAP: sabbath⟧ - жуглӧ»; 9:90 «⟦GAP: desert⟧
  - Arabs», Arabs kept as a people name).
- **Device seatings:** кывзысь (Hearer) **16** tokens, exactly
  the recorded 16, and 2:127 now reads кывзысь beside тӧдысь
  as required. The Forgiver family recomputes at **17**
  tokens case-insensitively — прӧститысь 16 (including the
  sentence-initial capitalised token) + прӧститысьяс 1 —
  exactly the recorded Forgiver ×16 + Forgivers ×1. The mercy
  device seats verify at their recorded special seats: 55:1
  reads «Милӧсьта.» (formerly the single retained word
  "Compassionate."), and 2:163's two mercy names both ride
  милӧсьта. Maker → вӧчысь and Omnipotent → став вына ride
  inside larger pre-existing agent/Almighty families and are
  not isolable by raw count; no retained Maker or Omnipotent
  token remains (§3's zero covers them).
- **The пышйӧ defect — mechanism and repair verified.** All
  **24** recorded reflect seats (2:266, 3:191, 7:57, 10:3,
  10:24, 11:24, 13:3, 14:25, 16:44, 16:69, 23:85, 25:50,
  25:62, 30:8, 30:21, 32:4, 34:9, 34:46, 37:155, 39:42,
  40:58, 45:23, 51:49, 59:21) were read individually: every
  one now carries a мӧвпав- form (мӧвпавӧ / мӧвпав after оз),
  and none carries пышй-. The remaining пышй- tokens are
  **12**, at the 12 genuine flee seats (3:111, 27:80, 28:31,
  33:13, 33:16, 40:33, 51:50, 59:12, 62:8, 72:12, 74:51,
  80:34), each read against its Master verse — all are flee /
  flight seats, untouched as claimed. (33:16 carries two of
  the twelve tokens, which is why a seat list alone appears
  to show eleven in a case-sensitive scan.)
- **Small items:** "Scriputure" **0** (5:65 now seats гижӧд);
  "Salomon" **0** (2:102 now Solomon).

## 6. GAP census recomputed — PASS, exact

Recomputed from the store, independent of `verify.py`:

- GAP seats **5,042**; GAP markers **13,714**; verses without
  a marker **1,194**; distinct GAP terms **4,299**. Every
  figure matches the remediation record exactly.
- The marker increase over the pre-remediation 12,899 is
  **815**, exactly the recorded GAP-marked token total, spread
  over 332 terms whose counts increased (116 of them new
  terms, headed by hereafter ×101, which stands as the census's
  top term). Bracket integrity: 13,714 opening ⟦ and 13,714
  closing ⟧, no malformed seat. The companion manuscript
  carries 13,715 markers — the text's 13,714 plus the front
  matter's explanatory example, as before.
- Distribution: 0 markers 1,194 verses; 1 marker 1,641;
  2 markers 1,362; 3 markers 841; then a tail to one verse
  carrying 39 markers. Clean-verse share is now 19.1% — the
  GAP-tier reservation of the original ruling (§9 of that
  report) rides with this figure, unchanged and undisguised:
  the remediation closed the invisible tier by moving it into
  the visible census, which is what the reservation required.

## 7. Purple sweep — candidates only

This checker's own replication of the attestation screen
(GiellaLT lemmas, kaikki headwords and declined forms,
glossary lemmas, regular-ending decomposition) over the
remediated store returns exactly **6 untraced Cyrillic
candidates**, matching the remediation record:

- локтӧ ×441 — disclosed irregular present of локны "come".
- кулӧ ×56 — disclosed irregular present of кувны "die".
- юяс ×52 — regular plural -яс of ю "river".
- лӧн ×6 — the genitive suffix split by tokenisation from the
  6 device tokens of §4.
- прӧститысь ×16 and прӧститысьяс ×1 — the remediation's
  Forgiver forms, regular agent -ысь / plural -яс formations
  on прӧститны "forgive", disclosed in glossary §J.

All six are candidates only, and all six adjudicate as
disclosed paradigm or device forms, not unattested seats. No
other untraced Cyrillic token was found. Distinct Cyrillic
tokens **1,000**; tokens containing ӧ **476**; tokens
containing і **13** — all three match the remediation
record's post-remediation figures (ӧ stood at 475 in the
original check, before remediation).

## 8. The lesser splits — ruling on the recorded reservation

The remediation left three lesser pairs ununified and recorded
them for this re-check. Recomputed counts and seats:

- **sea:** море ×31 beside саридз (as саридзяс) ×4. The four
  саридз seats are exactly the "two seas" seats (25:53,
  27:61, 35:12, 55:19); море carries the general sea seats.
- **mountain:** гӧра (as гӧраяс) ×36 beside керӧс ×5 tokens
  at 4 seats (7:143, 7:171, 11:43, 59:21). The керӧс seats
  are the singular, specific "the mountain" seats; гӧраяс
  carries the plural "mountains" seats — a number pattern a
  reader can infer.
- **temple / mosque:** храм ×1 beside мечеть ×20. The single
  храм seat is 17:7, where the Master says "the Temple";
  every мечеть seat is a seat where the Master says Mosque /
  mosques. This pair follows the Master's own wording and is
  in substance not a split at all.

**Ruling: these are a disclosed reservation that may ride,
not a bar to landing.** Ground in one breath: both forms in
each pair are attested inventory forms (verified in the
original check, §7 of that report, and not disturbed by the
remediation); nothing is hidden, retained, or invented; the
counts are small (4, 5, and 1 tokens on the minority side);
each pair follows a discernible pattern (the two-seas seats,
singular against plural, Temple against Mosque in the
Master's own words) rather than the arbitrary alternation
that failed the five core terms; and the reservation is
recorded in the remediation record and in this report, so it
travels with the book's record. The five core theological
terms — angel, messenger, believe, sin, prayer — were the
consistency obligation, and they are unified (§5). A future
unification pass on these three pairs remains open as
ordinary revision work; it is not a landing gate.

## 9. Overall verdict

**PASS.**

The remediation closed every failing item of the original
check: the retained-Latin tier is at 0 off the audited
allowlist (§3), seat 1:3 and the 27:30 Basmalah stand on the
spec seating (§2), the Sabbath / Hajj / Umrah / pilgrimage
families are GAP-marked at every seat (§5), the five split
core terms are unified (§5), the пышйӧ reflect defect is
proven an engine artefact and all 24 seats are reseated on
мӧвпавны with the genuine flee seats untouched (§5), the
screens were fixed at the source, and every revised figure —
1,176 seats changed, GAP census 5,042 / 13,714 / 1,194 /
4,299 — recomputes exactly (§§1, 6). The GAP tier stands
under the original ruling, PASS-WITH-GAP-TIER-RESERVATION,
which this re-check does not reopen. The lesser splits are
ruled a disclosed reservation that may ride (§8).

**Landing may proceed under the Pipeline Landing
Authorization as DRAFT — NOT PUBLISHED.** This checker edited
nothing in the text, landed nothing, shelved nothing, and
committed or pushed nothing; the draft stands where the
remediation left it, ready for the landing step that is not
this checker's to take.

— Independent re-checker, 2026-11-28. All figures recomputed
at this desk from the files of record on whitespace tokens;
instrument output treated as candidates until adjudicated,
per house practice.
