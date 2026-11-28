# Meadow Mari (mhr) Quran draft — INDEPENDENT RE-CHECK REPORT (2026-11-28)

Checker: a fresh crew that built none of this text and did none of the
remediation. Nothing was edited, landed, shelved, committed, or pushed
by this re-check. Every figure below was recomputed mechanically by the
re-checker's own scripts from verses-store.json, quran-mhr.json,
quran-mhr.txt, ayah-companion-manuscript-MHR.md, master-verses.json,
sources/mhr-lemmas.json, and sources/giella-lemmas-full.json — the
remediation record's figures were treated as claims to test, never as
evidence. This re-check answers CHECKER-REPORT-INDEPENDENT-2026-11-28.md
(verdict FAIL) as remediated in REMEDIATION-RECORD-2026-11-28.md.

## VERDICT: PASS

Every defect class that failed the book in the independent check is
repaired in the rebuilt text, verified seat by seat below, and no new
defect was found in the re-check's own screens. The two items the
original checker held open without failing weight — the ашындыр-
allomorph (a proofreader question, §9) and the recorded minor
inconsistencies (§10) — stand exactly as recorded and do not block
this verdict, as the original checker itself framed them. The book
stands DRAFT — NOT PUBLISHED. Landing may proceed under the Pipeline
Landing Authorization as DRAFT — NOT PUBLISHED. This checker does not
land it.

## 1. Seat count, seat-set equality, per-surah grid — PASS

- verses-store.json: 6,236 seats. master-verses.json flattened:
  6,236 seats. Sets exactly equal (no seat in either direction).
- quran-mhr.json flattened: 6,236 seats, text identical to
  verses-store.json at every seat (0 differences).
- Per-surah counts against the standard grid (7, 286, 200, … 6):
  no mismatch, all 114 surahs.
- Empty seats: none. "redacted" appears in no seat, and in neither
  assembled file. The rebuilt 6,236/6,236 claim is verified.

## 2. The Basmalah duplicates (original §2) — REPAIRED, PASS

- 1:1 equals the fixed form exactly: "Юмын лӱмеш, Серлагыш,
  Серлагыш." 1:3 is "Серлагыш, Серлагыш." as specified.
- The embedded opening line is gone from all three seats, read
  directly: 7:1 is now "Alif, Lam, Meem, Saad."; 8:1 begins
  "Нуно тый деч налме пай нерген йодыт. …"; 10:1 begins
  "Alif, Lam, Ra. …".
- The full Basmalah string occurs exactly 114 times in
  ayah-companion-manuscript-MHR.md and exactly 114 times in
  quran-mhr.txt (112 unnumbered openings + 1:1 + the in-verse
  quotation at 27:30 — the only two seats containing the string in
  the store are 1:1 and 27:30, both correct). The remediation's
  114-count is verified, not copied.

## 3. Mixed-script corrupted tokens (original §7a) — REPAIRED, PASS

- All five seats now carry the pure-Cyrillic respelling, verified
  in place: 39:21 ужат, 39:30 колат, 42:12 шара, 42:34 пытарен,
  43:83 модаш. Each replacement form traces to the inventory under
  the re-checker's own Purple replication (§8).
- Independent corruption screen: no token in the store begins with
  a Cyrillic letter and contains a Latin letter — the corruption
  pattern is extinct. The only mixed tokens remaining are the
  fused name-suffix forms of surahs 38–54 (Davidым, Mosesлан,
  Quranште, Torahште…), where a Master-form Latin name stem takes
  a Cyrillic suffix; these are the previously recorded minor
  hyphenation/fusion inconsistency (§10), not corruptions — no
  Cyrillic stem carries Latin letters anywhere in the book.

## 4. The н-for-ҥ class (original §7b) — REPAIRED, PASS

- сенгаш, сенгыше, Сенгыше, and шенгеч occur in no seat of the
  rebuilt store (0 occurrences of each, searched book-wide).
- шеҥгеч stands at 241 string occurrences book-wide (235 lower-case
  шеҥгеч + 6 capitalised Шеҥгеч), exactly the remediation's figure,
  recomputed by string count as the original checker counted.
- The reseated victory stems stand in the text: сеҥаш and сеҥыше
  forms present at the four named seats (4:141, 5:23, 5:56, 6:61
  read in the store), and both lemmas stand in the harvested
  inventory.

## 5. Unattested seatings and the нужналык nuance (original §7c) — REPAIRED, PASS, with the nuance ruled on

- No form of the family remains at any of the six seats: нужналык,
  нуждалык, and нужда occur nowhere in the rebuilt store.
- The six seats read as the remediation records: 2:61 нимодымылык,
  2:268 нимодымылыкым, 3:112 нимодымылык, 9:28 нимодымылык,
  9:60 нимодымо-влаклан with нужна корно еҥлан, 9:120 йӱаш
  тӱнымашым — each read directly in the store by this checker.
  нимодымылык, нимодымо, нужна, and тӱнымаш all stand in the
  harvested inventory and all trace in the Purple replication.
- RULING ON THE RECORDED NUANCE: the remediation's nuance is
  CORRECT on the re-checker's own inventory search.
  sources/giella-lemmas-full.json (50,921 entries) holds нужналык
  as a noun glossed "poverty; scarcity, insufficiency, poverty,
  want" (and бедность), and holds нужна as an adjective; it holds
  neither нуждалык nor нужда in any form, and neither жд spelling
  stands in sources/mhr-lemmas.json either, while нужналык does
  stand in that list. The original checker's §7(c) therefore
  overstated one limb: the five жн seats (2:61, 2:268, 3:112,
  9:28, 9:60) were seated on a form the Giella inventory does
  hold, glossed "poverty"; only the жд spellings — нуждалык at
  9:120 and нужда at 9:60 — stood in no inventory. The reseats
  were nonetheless applied to all six seats as directed, the
  replacement forms are themselves attested (нимодымылык is
  likewise glossed "poverty" in the same Giella inventory), and
  no seat is worse for the change. The correction to the original
  report's reasoning is recorded here; it does not reopen any
  seat, because the text as rebuilt is attested under either
  reading.
- Мукш (17:1) — REPAIRED: the coinage occurs nowhere in the
  rebuilt book. 17:1 now reads "Шнуй ⟦GAP: mosque⟧ гыч,
  ⟦GAP: mosque⟧ деке" (see §6).

## 6. Mosque unified to GAP (original §8) — REPAIRED, PASS

- The Master names a mosque in exactly 19 seats (recomputed from
  master-verses.json): 2:144, 2:149, 2:150, 2:187, 2:191, 2:196,
  2:217, 5:2, 8:34, 9:7, 9:19, 9:28, 9:107, 9:108, 17:1, 22:25,
  22:40, 48:25, 48:27. Every one of the 19 now carries
  ⟦GAP: mosque⟧ — verified seat by seat — for 20 markers in all
  (17:1 carries two). The book-wide GAP-mosque count is 20.
- The four-way split is extinct: мечеть occurs in no seat; храм /
  Храм survives only at the two non-mosque seats the remediation
  named, 8:35 (the Master's "the House") and 17:7 ("the Temple"),
  both correctly untouched; the кумалме вер seats that remain
  (7:29, 7:31 and others) are non-mosque "place of worship" seats,
  not Master mosque seats. One policy now governs the term, and
  the disclosure and the manuscript front matter name mosque
  among the standing gap terms, as the remediation records.

## 7. Surah 48 victory seats and the hair seat (original §10) — REPAIRED, PASS

- кугу полыш occurs nowhere in the rebuilt book (0 occurrences).
- Surah 48 carries сеҥымаш exactly 5 times, at the five named
  seats, each read directly: 48:1 "пале кугу сеҥымашым", 48:5
  "кугу сеҥымаш уло", 48:18 "лишыл кугу сеҥымашым", 48:24
  "кугу сеҥымашым", 48:27 "лишыл кугу сеҥымашым". сеҥымаш stands
  in the inventory and traces in the Purple replication; surah 48
  is now consistent with the book's standing seat (20 сеҥымаш
  tokens book-wide by token count).
- 48:27 hair: the seat now reads "але ӱп пӱчкыме кӱчыкын" — ӱп,
  the attested hair word, stands in the inventory; йол occurs
  nowhere in the verse. The "legs cut short" error is gone.

## 8. GAP census, Hill Mari bar, Purple sweep — PASS, figures replicated independently

- GAP census, recomputed seat by seat from the store: 298 GAP
  seats, 339 GAP markers, 5,938 verses rendered in full — exactly
  the remediation's revised figures. By term, recomputed =
  disclosed, every term: scripture ×107, hell ×97, jinn ×32,
  covenant ×24, mosque ×20, pilgrimage ×16, usury ×8, Sabbath
  ×7, Umrah ×3, debt ×3, dowry ×2, fly ×2, and ×1 each: manna,
  cucumbers, garlic, lentils, onions, witchcraft, swine, gambling,
  Ark, donkey, palms, vines, martyrs, synagogue, olive, hail,
  palm, hoopoe.
- The disclosure's revised 298-seat list is set-equal to the
  store's GAP seats (0 in either direction, recomputed).
- Umrah (desk ruling in the remediation): ⟦GAP: Umrah⟧ ×3 —
  2:158 ×1, 2:196 ×2 — verified in place. No Latin "Umrah" and
  no Cyrillic "умра" remains anywhere outside the markers.
- Hill Mari bar: no token or character ӓ, ӹ, Ӓ, or Ӹ in the store
  or in quran-mhr.txt. In the assembled manuscript the two
  characters ӓ and ӹ occur only inside the English front-matter
  paragraph that names the Hill Mari alphabet in order to fence
  it off — they are mentioned, never seated; the bar holds in
  the text exactly as in the original check.
- Purple sweep, replicated by the re-checker's own implementation
  of the screen (inventory + glossary lemmas, regular-ending
  stem-stripping): 7,509 distinct Cyrillic tokens, 122,571
  Cyrillic tokens in all, 1,413 untraced candidate types
  (13,326 occurrences) — exactly the remediation's revised
  figures (was 7,522 / 1,421 at the original check). None of the
  repaired defect forms (шенгеч, сенгаш, сенгыше, нужналык,
  нуждалык, нужда, Мукш, мечеть, or any of the five corruptions)
  appears in the candidate list, and every replacement form
  (шеҥгеч, сеҥымаш, нимодымо, нимодымылык, тӱнымаш, ужат, колат,
  шара, пытарен, модаш) traces. The untraced mass is the same
  regular-paradigm mass the original checker adjudicated as
  paradigm forms, diminished by exactly the repaired classes.

## 9. The ашындыр- allomorph — HELD, as recorded, no failing weight

Recomputed: ашындыр- occurs 22 times in 20 seats, unchanged by
the remediation, exactly as both prior papers record. The
inventory holds only ашындараш. Whether the allomorph is a
regular Mari vowel alternation cannot be settled from the
harvested inventories; it remains a question for a Mari
proofreader, disclosed in the revised disclosure's open-seat
record. The original checker held it as an uncertainty, not a
failure, and this re-check holds it the same way.

## 10. Core terms and minor items — PASS / stand as recorded

- God: the Master names God in 1,836 seats by this checker's
  \bGod\b census (the original checker's 1,853 counted a wider
  pattern); every one carries a Юмо form — 0 exceptions.
- Prophet: all 75 Master prophet seats carry the пиямбар family
  (the capitalised title Пиямбар at the "O Prophet!" seats
  included, read at 5:81, 33:1, 33:6, 49:2). пророк is never
  seated (0 occurrences).
- Mercy: every Master merc* seat whose sense is divine mercy
  carries the серлаг- stem; the only seats without it are the
  Master's merchandise/commerce false positives (2:275, 12:19,
  12:65, 12:88, 24:37), verified by reading — the same
  adjudication the original checker made for its false positives.
- Minor items left as recorded by the remediation's deliberate
  disposition — the Latin "Quran" (54 occurrences by token count)
  beside Cyrillicised Коран, and the early-hyphenated /
  later-fused name suffixes (≈49 fused tokens, surahs 38–54) —
  touch no attestation, fidelity, or consistency seat and were
  recorded as minor by the original checker itself. They stand
  disclosed and do not block this verdict.

## Stop line

This re-check edited nothing in the text under review, and landed,
shelved, committed, and pushed nothing. The verdict is PASS: the
remediated Meadow Mari Quran draft may proceed to landing under
the Pipeline Landing Authorization, as DRAFT — NOT PUBLISHED.
