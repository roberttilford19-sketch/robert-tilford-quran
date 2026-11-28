# Independent Re-check Report — Moksha (mdf) Quran Draft (Remediated)

Checker: a fresh agent who built none of this text and did none of
the remediation. Date: 2026-11-28.
Scope: `quran-mdf.txt`, `quran-mdf.json`, `verses-store.json`,
checked against `master-verses.json` (the lane copy of the Locked
English Master), `BUILD-SPEC.md`, `glossary.md`,
`CHECKER-REPORT-INDEPENDENT-2026-11-28.md` (original FAIL), and
`REMEDIATION-RECORD-2026-11-28.md`.
Method: every figure below was recomputed with this checker's own
scripts; the lane's `verify.py` was re-run only as a cross-check
and reproduced its reported figures exactly. Nothing was edited,
landed, shelved, committed, or pushed by this check.

## VERDICT: PASS

Every finding that failed the book in the original independent
check (§§8.1–8.9) is verified closed by this checker's own
recount, the desk-ruling item the original check reserved (кда,
§9.6) is corroborated from the lane's own held source, and the
§9.7/§9.4 reservations the remediation also addressed are verified
closed. The skeleton — counts, seat-set, grid, Basmalah, GAP
census, Erzya bar — passes exactly. Landing may proceed under the
Pipeline Landing Authorization as DRAFT — NOT PUBLISHED. This
checker does not land it.

Reservations carried forward unchanged, none of them a bar to
landing (all were recorded as reservations, not findings, in the
original check and were expressly outside the remediation's
charge): the disclosed prophet/messenger collapse (§9.3 of the
original report); the 4:56 кедь "skins" seat (§4 below); manna in
Latin at 2:57, 7:160, 20:80 and Bedouin-тнень at 33:20 (§9.5);
the “ ” quote imbalance inherited from the Master itself (§9.7a).

## 1. Recount, seat-set, grid — PASS

- Store seats 6,236; master seats 6,236; seat sets exactly equal
  (no missing, no extra). `quran-mdf.json` flattened equals
  `verses-store.json` seat for seat (6,236/6,236, texts
  identical).
- Per-surah grid clean at all 114 surahs against the standard
  grid (sum 6,236). `quran-mdf.txt` carries 6,236 numbered verse
  lines matching the store at every seat — 0 mismatches (the
  original check's nine trailing-space differences are gone; no
  seat carries a trailing space, no double spaces anywhere, no
  verse opens lowercase).
- Empty seats: NONE. No seat shorter than three characters. The
  string "redacted" appears in no seat. No "..." anywhere in the
  book.

## 2. Basmalah — PASS

- 1:1 equals the fixed form exactly: «Шкаень лемса, Милостивай,
  Милостивай.» — the only store seat equal to it; 1:3 is
  «Милостивай, Милостивай.» as specified.
- In `quran-mdf.txt`: exactly 112 standalone Basmalah lines, and
  114 occurrences of the fixed form in all (112 standalone + 1:1
  numbered + 27:30 inline in Solomon's letter, verified present
  in the store seat).

## 3. GAP census — PASS

- Recomputed: 58 GAP seats, 68 markers — jinn 31, pilgrimage 16,
  usury 8, Sabbath 7, apes 3, gnat 1, cucumber 1, fig 1. Exactly
  the remediation record's census (was 57/67; the +1 seat/+1
  marker is 7:166, §6). Markers well-formed: ⟦/⟧ balanced 68/68,
  no malformed GAP strings.
- No silent seating of standing terms: every master seat
  containing "jinn" (26), "usury" (6), "Sabbath" (5), "gnat" (1),
  or "fig" (1), and every pilgrimage/hajj seat (7), carries its
  GAP marker in the Moksha seat.

## 4. Erzya bar — PASS

Whole-token recount, case-insensitive: паз 0, чи 0, кедь 0,
теште 0, кинига 0, казне 0, пежеть 0, шайтян 0, пророк 0,
баславамс 0, седеймариця 0. Substring scans find no шайтян,
шайтан, пророк, or пежеть anywhere. казнефт stands at 34:35 and
37:59 — the -фт participle on казня "punishment", settled PASS
in the original check and unchanged.
The 4:56 seat stands as the original check recorded it: кедьсна /
кедьса, "skins", a genuine Moksha word coinciding in form with
the barred Erzya word for "hand"; the barred sense is nowhere
seated. (The only other кедь substrings in the book, at 23:40 and
25:40, are inside пяшкедьф(т) "filled" — not this word.) Recorded
reservation, carried forward; not a failure.

## 5. Script purity — PASS

- Mixed-script tokens (Cyrillic + Latin letters fused in one
  token): 0 occurrences, 0 distinct (was 13 distinct / 21
  occurrences). All thirteen remediated shapes are pure Cyrillic.
- U+04A3 (ң): 0 occurrences book-wide (was 1, at 47:25; that seat
  now reads «келе васта», verified in place). A full character
  scan finds no Cyrillic letter outside the 33-letter Russian
  norm anywhere in the book.
- Guillemets balance: « 232 / » 232 (was 232/231; 21:56 now
  closes its « at the verse end, verified in the seat text).
- Retained Latin is the names-policy Latin only; the lane
  screen's retained-Latin candidates are exactly the recorded
  reservations: manna ×3, Bedouin ×1, the vocative "O", and the
  al- of al-Lat/al-Uzza.

## 6. Remediation spot-verification — every claim verified by count

Each figure below is this checker's own recount on the finished
store, set against the original checker's before-figure:

- §8.1 што 348 → **0** tokens; штоба 275 → **0** tokens. The
  purpose reseat is exact: сянь инкса substring occurrences 376
  (= 101 pre-existing + 275, the штоба count). Sample seat 4:3
  reads complete asyndetically with no content word lost.
- §8.2 эли 127 → **0**; али 360 → **487** (+127, exact).
- §8.3 4:23: the garbled clause, the literal ellipsis, and the
  stray fragment are gone. The seat now carries «И тинь шачф
  цёраньк аватне,» ("and the wives of your born sons") on the
  verse's own шачф device, and the full kinship list stands.
- §8.4 mixed-script: 21 → **0** (see §5).
- §8.5 7:166 now reads «берянь ⟦GAP: apes⟧», consistent with
  2:65 and 5:60 (both verified carrying the marker). маймун
  tokens: 1 → **0**.
- §8.6 U+04A3: 1 → **0** (see §5).
- §8.7 29:14 now reads «тёжянь кизот ведьгемонь кизода башка»
  — ведьгемонь (fifty) present, 1 token; вейхксагемонь (ninety)
  0 tokens book-wide. The book's own fifty-thousand at 70:4
  («вете кеменонь тёжянь») is the same number in expanded form.
- §8.8 иля 92 → **0**; иляда 25 → **0**. The conversion count is
  exact: аф 4,661 → **4,778** (+117, one per removed token).
  Sample seat 4:3 carries the prescribed аф + 2pl frame
  («аф тиихтяда», «аф уледа»).
- §8.9 мельга family: мельга whole tokens 48 → **0**; substring
  мельга 74 → **0** (мельганза, мельгат, мельгаст all 0). The
  мельге paradigm stands in its place: мельге 79 → **127**,
  мельгенза 11, мельгет 10, мельгест 8 — the remediation's
  figures reproduced exactly.
- §9.6 кда: 865 whole tokens (unchanged, as the ruling directs).
  Corroboration verified directly in the lane's own held source,
  `sources/giella/devtools/testdata/bibleFreq2016.txt` (the 2016
  Moksha New Testament frequency list): кда 332 + Кда 239 = **571
  occurrences**, in the company of кода 739 and али 267 in the
  same list. кда is attested in the control text; the desk
  ruling stands on evidence this checker has seen. In the same
  list инголе stands at 214 and ингели at 0 — corroborating the
  §9.7(d) reseat from the same source.
- §9.7(c) сынь 265 → **0**; синь 4,819 → **5,084** (+265, exact).
- §9.7(d) ингели 136 → **0**; инголе whole tokens 387.
- §9.7(a) guillemet balanced (see §5); §9.7(b) trailing spaces
  9 → **0** (txt/store mismatches 0 at all 6,236 seats, §1).
- §9.4 74:30 now reads «кевейхксые» (nineteen, the inventory's
  teen-series form), 1 token; the ambiguous «вейхкса кемонь» is
  gone.

## 7. Purple sweep — candidates only

The lane screen (`verify.py`, re-run as cross-check) reports
9,901 distinct Cyrillic tokens and 4,940 untraced candidates
(was 9,923 / 4,955) — the removed mass is exactly the remediated
families, as the remediation record states. Candidates are
candidates, not findings: the largest is кда (865), now
corroborated and recorded (§6); the next mass is the азомс
paradigm tail (азсь 492, азьк 338, азыхть 318, азсть 273, азы
91, азсы 85) and the definite/possessive chains the original
check adjudicated as the expected agglutinative tail, not
defects. No new high-frequency untraced token survives
inspection as a candidate invention. Purple raises no finding
beyond what §§1–6 settle.

## 8. Fidelity spot checks — PASS

Number seats re-read against the Master: 29:14 thousand-minus-
fifty (corrected, §6); 70:4 fifty thousand in expanded form;
46:15 колмогемонь (thirty) present; 9:36 кемгафтува (twelve)
present; 18:25 колма сят (three hundred) present; 37:147 сяда
тёжяненьди (a hundred thousand) present; 12:4 кемфкие (eleven)
present — the book's teen pattern that §9.4's fix now matches at
74:30. Core-term stems stand as the original check counted them
(азор family ~1,150 substring occurrences; книга 255; the Шкаень
кучф prophet/messenger device uniform — the disclosed collapse
remains a recorded reservation, §9.3 of the original report, not
an inconsistency).

## Summary for the landing decision

The remediation is verified complete and exact: every §8 count
is 0, every reseat count reconciles to the token (али +127,
аф +117, сянь инкса +275, синь +265, мельге +48), 4:23 is
repaired, 29:14 reads fifty, 7:166 carries its GAP marker, the
script is pure, and кда stands corroborated at 571 occurrences
in the 2016 Moksha New Testament frequency list held in the
lane's own sources. The book stands at 6,236 of 6,236 verses,
seat-set exactly equal to the Locked English Master, grid clean
at all 114 surahs, Basmalah exactly as fixed, GAP census 58
seats / 68 markers, zero whole-token Erzya-bar seats.

**PASS. Landing may proceed under the Pipeline Landing
Authorization as DRAFT — NOT PUBLISHED.** This checker has not
landed, shelved, committed, or pushed anything.
