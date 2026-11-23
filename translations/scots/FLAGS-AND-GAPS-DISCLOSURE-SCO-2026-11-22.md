# FLAGS AND GAPS DISCLOSURE — Scots (sco) Quran

Written for the landing of 2026-11-22. Everything in this book that
rests on a declared ruling, a judgment call, or a known anomaly is
named here, in the open, in one place. Nothing in the manuscript is
passed off as something it is not. The full working record stands in
the lane folder ~/workspace/ayah-scots/ (work/flags-sco-full.md —
16 items; BUILD-REPORT-SCO-2026-11-22.md;
CHECKER-REPORT-SCO-2026-11-22.md).

## The standing count

6,236 of 6,236 verses rendered. GAP seats: 0. No seat was left
unrendered and no English was faked into a seat: the declared rule
system produced a Scots rendering for all 6,236 verses. The figure
is a drafting count, reconciled mechanically by an independent
checker (PASS, 2026-11-22: per-surah counts matching at all 114
surahs; seat set sequence-identical to the master grid; Arabic runs
6,462 of 6,462; prostration markers 15 of 15 at the master's seats;
0 [MISSING]; 0 "%"). This book is not speaker-reviewed: it was
machine-assisted by non-speakers under Robert Tilford's direction,
and no native or critic review is awaited, invited, or chased
(Robert's ruling, 2026-11-18).

## The declared norm

Modern literary Scots, disciplined by Dictionaries of the Scots
Language (DSL) spellings and usage, on a broad Lowland literary
base; no apologetic apostrophes (write *o*, never *o'*); sustained
Scots grammar (negation *no/dinna/didna/canna*; pronouns
*ye/thay/thaim/yer*; relative *wha/that*). Pillars: DSL Online
(fact only — spellings and attestation, never the dictionary's
wording or arrangement) and Nisbet's Scots New Testament (c. 1520)
as historical control only; the norm is modern, not 1520 Scots.
No first-translation claim is made beyond the bounded form:
first complete Scots Quran translation found — after research.

## Declared rulings, carried consistently across the whole build

- **Lord → Laird** — 972 occurrences in the Scots verse text
  (checker-recomputed, exact).
- **Master → Maister** — 19 occurrences, matching the master's
  any-case "master" count; no "Master" remains in Scots verse text.
- **Rahman → the Mercifu; Rahim → the Compassionate** — 0 mismatches
  at the checker: every master "Beneficent" seat carries *Mercifu*
  and every "Merciful" seat carries *Compassionate*. Mercifu 22 =
  Beneficent 20 + the 2 disclosed judgment seats below;
  Compassionate 151 = Merciful 140 + 11 seats where the master
  itself already reads "Compassionate" for Rahman.
- **God addressed as Ye** throughout.
- **Basmalah:** "In the name o Allah, the Mercifu, the
  Compassionate." — 115 occurrences in the manuscript = 112
  standalone openings (byte-identical form) + 1:1 (the verse itself)
  + 27:30 (embedded, in Solomon's letter) + 1 front-matter
  quotation. Surah 9 has no Basmalah, in Scots or Arabic.

## Judgment calls disclosed (from the lane flags file, 16 items)

1. **Benevolent → Mercifu** at 2:163 and 13:30 ("the Benevolent
   One"): the master's "Benevolent" stands for Rahman at these
   seats, so the declared Rahman rendering was applied. 2 seats.
2. **"The Merciful" → "the Compassionate" everywhere**, per the
   declared Rahim ruling — including seats where the Arabic epithet
   is Rahman but the master itself prints "Merciful". The master's
   wording governs the lane; the tension is disclosed.
3. **27:30** — the Basmalah inside Solomon's letter is rendered in
   the declared Basmalah form with *Allah*, where the master reads
   "In the Name of God, …".
4. **"Gracious" kept as "Gracious"** (3 seats: 2:243, 3:152,
   22:65): not part of the Rahman/Rahim pair in the master, and a
   shared Scots word.
5. **Path → gate** (from the sample's *straucht gate*) extended to
   every "path/paths" seat, including "God's path" formulas.
   111 seats of *gate*.
6. **Weak past in -it**: *creatit, guidit, blessit, usit, unitit,
   passit* etc., applied only where the English stem ends
   t/d/s/x/sh/ch. Protected words ("indeed, deed, seed, sacred,
   wicked, naked, beloved") were fixed after a first pass produced
   *indit/dit/sit*; those three defects were caught, the rule set
   fixed, and the build re-run — final slices contain 0 of them.
7. **Gerund/participle in -in**: *enterin, feedin, believin,
   forgivin*. Nouns like *king, morning, during, offspring*
   protected.
8. **also → an aw** placed before the modified word; Scots often
   places *an aw* after. Placement disclosed.
9. **are not → are na** (two words) rather than a fused form.
10. **these → thir** as determiner and pronoun; **those → thaim**
    as demonstrative, following the sample's "thaim that".
11. **earth → yird** at every seat (378), including the "heivens an
    yird" formula. *Yird* is DSL-attested for earth/soil; it is the
    build's boldest recurring choice.
12. **woman → wumman, women → weemin** (98 seats of *weemin*).
13. **servant → servand, children → bairns, book → beuk, whoever →
    whaever, whatever → whitivir, whenever → whanever** — modern
    literary Scots forms, applied consistently.
14. **wrongdoers → wrangdaeers**; **falsehood → fausheid**.

## English-leak disclosure (honest residue, carried instead of GAPs)

- **158 verses word-for-word identical to the English master** —
  all short/shared-vocabulary seats: 98 of ≤5 words, 54 of 6–9
  words, only 6 of ≥10 words, the longest 18 words at 42:19
  (disconnected-letter openings, short formulae, and seats whose
  every content word is common to Scots and English, e.g. 55:1
  "The Compassionate."). Seat list in
  `work/verification-sco-full.json` in the lane folder; the checker
  reproduced the count and the seat set exactly.
- **47 near-identical verses** (≥90% same words, same length), all
  short, likewise listed by seat; the checker sampled 8 and found
  each differing by one or two Scots tokens.

## Checker anomalies, carried on the record (none verdict-changing)

1. **Possessive "Lord's" unconverted at 35:39 and 53:55** — the
   Laird rule missed the possessive form. Laird total 972
   reconciles against the master's any-case "lord" total of 974
   (969 capital "Lord" in verse text).
2. **59:22** renders two distinct master epithets ("the
   Compassionate, the Merciful") as **"the Compassionate, the
   Compassionate"** — a duplication produced mechanically by the
   declared rule; a wording blemish, not a meaning change.
3. **5:65 — master-side item, not a Scots defect.** The Locked
   English Master itself reads "Scriputure" ("Had the People of
   the Scriputure believed and been righteous…"). The Scots carries
   it faithfully as "Scriputure" under the source lock; the lane
   does not edit the master. The other 106 "Scripture" seats are
   clean. Flagged for the master side.

## Checker verdict

**PASS** (independent checker, read-only against the draft,
2026-11-22). Counts exact on every canonical measure, and the
40-verse language sample graded: **(a) real Scots rendering 32,
(b) Scots frame with English content standing in 7, (c) effectively
English with substitutions 1** — category (a) dominant at 80%.
Corpus-wide Scots saturation agrees (*thaim* 3,136, *ye* 4,130,
*tae* 3,155, *wha* 1,807, *frae* 1,116, *hae* 1,104, *dinna* 524,
by the checker's slice counts). Zakat carries no percentage
anywhere in the book: "%" count is 0 in verse text, slices, and
the whole manuscript.
