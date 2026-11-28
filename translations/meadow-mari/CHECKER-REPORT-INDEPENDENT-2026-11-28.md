# Meadow Mari (mhr) Quran draft — INDEPENDENT CHECKER REPORT (2026-11-28)

Checker: a fresh crew that built none of this text. Nothing was edited,
landed, shelved, committed, or pushed by this check. Every figure below
was recomputed mechanically by the checker's own scripts from
verses-store.json, quran-mhr.json, quran-mhr.txt,
ayah-companion-manuscript-MHR.md, master-verses.json, and
sources/mhr-lemmas.json — the build's verify.py was run once only to
confirm the build's own numbers replicate, and they do.

## VERDICT: FAIL

The book's skeleton is sound — seat grid, GAP census, Hill Mari bar,
core-term consistency, and the clause-fidelity sample all pass, and the
Purple untraced mass adjudicates as regular paradigm forms, not
silently seated unattested words. The FAIL rests on a small, exactly
listed set of text defects that a canonical book cannot carry:
a duplicated Basmalah printed inside three verse seats, five
mixed-script corrupted tokens, a systematic н-for-ҥ misspelling class
(36 tokens) whose forms stand in no inventory, two unattested
Russian-shaped seatings, and a mosque policy applied four different
ways while the book's face discloses only one of them. Every defect
is repairable seat by seat; the seat lists are given in full so the
repair crew need not re-derive them.

## 1. Seat count, seat-set equality, per-surah grid — PASS

- verses-store.json: 6,236 seats. master-verses.json flattened:
  6,236 seats. Sets exactly equal (no seat in either direction).
- quran-mhr.json flattened: 6,236 seats, text identical to
  verses-store.json at every seat (0 differences).
- Per-surah counts against the standard grid (7, 286, 200, … 6):
  no mismatch in store or Master, all 114 surahs.
- Empty seats: none. The build's 6,236/6,236 claim is verified.

## 2. The Basmalah — FAIL (3 seats)

- 1:1 equals the fixed form exactly: "Юмын лӱмеш, Серлагыш, Серлагыш."
  1:3 is "Серлагыш, Серлагыш." as specified.
- BUT the unnumbered opening line is also embedded inside the verse-1
  seat text of three surahs, and the assembled book prints it twice in
  succession (opening line, then again as the head of verse 1):
  - 7:1 — seat reads "Юмын лӱмеш, Серлагыш, Серлагыш.\nAlif, Lam, Meem, Saad."
  - 8:1 — seat begins "Юмын лӱмеш, Серлагыш, Серлагыш.\nНуно тый деч …"
  - 10:1 — seat begins "Юмын лӱмеш, Серлагыш, Серлагыш.\nAlif, Lam, Ra. …"
- Counted: the full Basmalah string occurs 117 times in the manuscript;
  the correct count is 114 (112 unnumbered openings + 1:1 + the
  in-verse quotation at 27:30, which is correct and matches the
  Master's own quotation). Surah 9 correctly carries none.
- BUILD-SPEC seats the Basmalah as an unnumbered opening line, never
  as part of a numbered verse. Batch C's notes disclose seating it
  "at the head of 7:1, 8:1, 10:1" — the assembly then added the
  opening line a second time. The book-level disclosure does not
  mention it. Repair: strip the embedded first line from seats
  7:1, 8:1, 10:1 in the store and rebuild the book files.

## 3. GAP census — PASS as counted; the mosque application FAILS (see §8)

Recomputed seat by seat from the store:
- GAP seats: 288. GAP markers: 322. Verses rendered in full: 5,948.
  All three figures match the disclosure exactly.
- By term, recomputed = disclosed, every term: scripture ×107,
  hell ×97, jinn ×32, covenant ×24, pilgrimage ×16, usury ×8,
  Sabbath ×7, mosque ×6, debt ×3, dowry ×2, fly ×2, and ×1 each:
  manna, cucumbers, garlic, lentils, onions, witchcraft, swine,
  gambling, Ark, donkey, palms, vines, martyrs, synagogue, olive,
  hail, palm, hoopoe.
- The disclosure's 288-seat list is set-equal to the store's GAP
  seats (0 in either direction). The census is honest as a count
  of the markers present.

## 4. Hill Mari bar — PASS

No token in the store, and no character in quran-mhr.txt, contains
ӓ, ӹ, Ӓ, or Ӹ. The bar holds absolutely, as the build reported.

## 5. "Redacted" placeholder seats — PASS

The string "redacted" appears nowhere in the Mari text (store or
.txt). Both Master seats carrying the literal placeholder were
rendered for their surrounding sense, per BUILD-SPEC:
- 39:7 — the bearer clause is restructured ("One holds his own
  burden; he cannot bear another's burden"); the negation's scope
  shifts but the sense is carried. Acceptable under the spec's
  surrounding-sense rule.
- 48:8 — "witness, bearer of good news, warner" all carried.

## 6. Purple sweep — figures replicate; adjudication: PASS with two defect classes carved out (§7)

- The checker's independent tokenisation reproduces the build's
  screen exactly: 7,522 distinct Cyrillic tokens, 1,421 untraced
  candidate types (13,363 occurrences of 122,599 Cyrillic tokens).
  work/verify-candidates.json matches a fresh verify.py run.
- Adjudication of the 1,421, by the checker's own stronger tracers
  plus family-by-family inspection of every large family and a
  539-type small-count tail: the mass is regular paradigm forms on
  attested stems, exactly as the disclosure claims. The largest
  families are: the bare suffix fragments влак / ын / ым / лан /
  ште left by hyphenated name plurals and inflections (≈3,300
  occurrences); the BUILD-SPEC pronoun paradigm (нунын ×1,544,
  нуным ×724, тудылан ×324, and the мемнан/тендан/туды- chains);
  the suppletive and stem-changing verb paradigms (улаш: улыт
  ×633, улыда, улына; пуаш: пуа/пуэн/пуэна/пуат…; каяш:
  кая/каят/каен/каеныт…; ужаш, ӱжаш, муаш, лияш, шуаш families);
  case forms with regular final-vowel drop (мланде → мландым
  ×100, мландын, мландыште; волгыдо, еҥ, Юмо chains); possessive
  chains (-ж, -жлан, -шкыже…) and -влак/-маш/-рак/-дыме
  derivations on attested stems throughout the tail.
- No silently seated unattested content word was found in the
  untraced mass beyond the two classes in §7, which the screen
  itself had surfaced as candidates and the build left unresolved.

## 7. Defect classes inside the candidate mass — FAIL

(a) Mixed-script corrupted tokens (Latin codepoints inside Cyrillic
words) — 5 tokens, 5 seats, mechanically proven by codepoint:
- 39:21 — ужat (Latin a, t) for ужат
- 39:30 — колat (Latin a, t) for колат
- 42:12 — шарa (Latin a) for шара
- 42:34 — пытарen (Latin e, n) for пытарен
- 43:83 — модaш (Latin a) for модаш
These are the build's own unresolved "a ×2, en ×1" Latin candidates;
they are not words in any language, they are typographical
corruptions, and they stand in the printed text.

(b) н-for-ҥ misspellings — forms absent from the harvested inventory
(51,333 lemmas as loaded by the checker), i.e. unattested as seated:
- сенгаш — 4:141, 5:23; сенгыше — 5:56; Сенгыше — 6:61 (4 tokens,
  4 seats). The attested forms are сеҥаш / сеҥыше (both in the
  inventory).
- шенгеч — 32 occurrences in 31 seats: 17:47, 17:63, 17:110, 18:6,
  18:28, 18:47, 18:64, 18:66, 18:70, 18:79, 18:85, 18:89, 18:92,
  19:5, 19:43, 19:59, 19:64, 20:16, 20:47, 20:78, 20:84, 20:90,
  20:93, 20:108, 20:110, 20:123, 20:134, 26:215, 33:15, 37:90,
  38:55. The attested postposition is шеҥгеч (seated correctly
  203 times in 183 other seats).
ҥ is a distinct letter of the Meadow Mari alphabet, not a stylistic
variant of н; a book whose face claims an attested lexical base
cannot carry 36 tokens in spellings no inventory holds.

(c) Unattested Russian-shaped seatings:
- нужналык ×5 — 2:61, 2:268, 3:112, 9:28, 9:60; and нуждалык ×1 —
  9:120. Neither нужда, нужналык, nor нуждалык stands in the
  inventory. Batch C's notes log the 9:120 seat as an
  "approximation" device; batch K's sweep in fact rejected нужда
  as not in the inventory and reseated its own seats — the two
  batches applied opposite rules to the same word, and the
  book-level disclosure names neither.
- Мукш — 17:1 ("Мукш храм" for the Farthest Mosque). Мукш stands
  in no inventory; it is a coinage. Batch E's notes disclose the
  Шнуй/Мукш distinction as a device, but a disclosed coinage is
  still a coinage: the GAP policy's whole point is that an
  unattested form does not seat.

(d) Held as an uncertainty, not a failure: the ашындыр- allomorph
(22 occurrences, 20 seats, all in surah 2–3: 2:49, 2:50, 2:51,
2:53, 2:54, 2:55, 2:58, 2:60, 2:61, 2:63, 2:67, 2:72, 2:152,
2:198, 2:200, 2:203, 2:231, 2:239, 3:41, 3:103). The inventory
holds only ашындараш; the book elsewhere seats ашындар- forms
96 times. Whether ашындыр- is a regular Mari vowel alternation
cannot be settled from the harvested inventories; a Mari
proofreader should rule on it before landing. It is disclosed
nowhere in the build's papers.

## 8. The mosque seats — FAIL (policy applied four ways; disclosure states one)

The Master names a mosque in 19 seats. Recomputed treatment:
- GAP-marked (batch A only): 2:144, 2:149, 2:150, 2:191, 2:196,
  2:217 — the disclosure's ×6.
- храм / Шнуй Храм (temple loan): 5:2, 8:34, 9:7, 9:19, 9:28,
  9:107, 9:108, 17:1 (×2 in the verse), 48:25, 48:27.
- кумалме вер (prayer-place device): 2:187.
- Шнуй Пӧрт (prayer-house device): 22:25.
- мечеть (the Russian loan, which does stand in the inventory):
  22:40 — in the very verse where synagogue is GAP-marked.
Batch A's stated ground for GAPping was that храм is temple/church
and юмынпӧрт the Mari prayer house, so neither may silently seat
"Sacred Mosque". Batches B, C, and E then seated храм for the same
"Sacred Mosque" phrase (5:2, 8:34, 48:27…), batch C seated кумалме
вер at 7:29/7:31 (non-Sacred seats), and batch F seated мечеть.
Each choice is defensible alone; together they are four policies
for one term, and the book's face and the disclosure present
mosque only as a GAP term. A reader meets ⟦GAP: mosque⟧ in surah 2
and Шнуй Храм for the identical phrase from surah 5 onward, with
no word of explanation. This needs one ruling applied book-wide
and disclosed — it is a consistency failure, not an attestation
failure (храм and мечеть are both inventory loans).

## 9. Core-term consistency — PASS

All counts recomputed against the Master's seats:
- God: the Master names God in 1,853 seats; every one carries a
  Юмо form. No exceptions.
- Prophet: 75 Master prophet seats; every one carries пиямбар
  (79 occurrences book-wide). пророк is never seated — the
  audit's standing seat held uniformly.
- Mercy: 273 Master merc* seats; all carry the серлаг- stem —
  the noun Серлагыш in the divine-name seats (including both
  Basmalah names at every occurrence) and the attested verb
  серлагаш forms at verb seats (7:23 серлагет, 17:8 / 17:54
  серлага). The single-stem seating is uniform and disclosed.
- Fasting: the true fasting seats (2:183, 2:184, 2:185, 2:187,
  2:196, 4:92, 5:89, 5:95, 19:26, 33:35, 58:4) all ride the
  пӱтӧ family (пӱтӧ / пӱтым / пӱтым кучаш). 2:184 and 2:185 were
  read in full: the fast is carried in both. (Seats where the
  Master's "fast" means "hold fast" — 3:103, 4:146, 7:145 —
  correctly do not ride пӱтӧ.)
- Sin: сулык is the uniform sin seat; every Master seat whose
  "sin" is the noun/verb of wrongdoing carries it (the apparent
  exceptions in a naive regex census are the Master's "single /
  sincere / since" false positives, verified by reading).

## 10. Clause-fidelity sample — PASS, with the surah-48 device and one lexical error carved out

44 verses were read in full against the Master, spread across the
book and weighted to the seats the builders themselves flagged:
1:5, 1:6, 1:7, 2:57, 2:61, 2:144, 2:184, 2:185, 2:282 (227 Master
words — every clause carried, debt GAP ×3 as disclosed), 4:34
(the admonish / abandon / strike sequence in the Master's own
order, unsoftened), 5:110 (130 words, all clauses), 12:88, 17:1,
22:40, 24:35, 30:3, 33:35 (the full paired list, fasting seat
included), 39:7, 48:1, 48:8, 48:25, 48:27, 48:29 (93 words, all
clauses), 55:33, 57:10, 60:10, 72:1, 73:20 (132 words, all
clauses), 74:31 (101 words, both scripture GAPs, all other
clauses), 91:8, 91:13, 91:14, 96:2, 96:19, 98:6, 98:8, 110:1,
114:6, and the corruption seats in context (39:21, 39:30, 42:12,
42:34, 43:83). No dropped clause was found anywhere in the
sample. Named readings:

- Batch A mosque GAP (2:144): the verse is otherwise
  clause-complete around the marker. The GAP itself is honestly
  applied — its fault is only that later batches did not follow
  it (§8).
- Surah 91 devices (91:8 "inspired" → ончыктыш "showed"; 91:13
  she-camel → ава тӱе; 91:14 "hamstrung" → индырышт): each is
  exactly the disclosed approximation its batch notes claim,
  clause carried, specific sense narrowed. Acceptable as
  disclosed devices.
- Surah 96 devices (96:2 "clot" → вӱр курал; 96:19 kneel →
  кумалаш bow): as disclosed; acceptable.
- Surah 48 victory device — FAIL on its ground, and one error:
  batch J's notes state no victory lemma was found ("сенгаш /
  сенгымаш checked, absent"). The check was run on the Russian
  spelling. Under the Mari spelling the lemma stands in the
  inventory (сеҥаш, сеҥымаш both present), and the rest of the
  book seats it freely (8:10, 9:25, 9:89, 10:64, 30:3, 33:71,
  37:60, 45:30, 57:10 — the seat batch K itself corrected to
  сеҥымаш — 61:13, 110:1…). Surah 48 alone rides кугу полыш
  ("great help") at 48:1, 48:5, 48:18, 48:24, 48:27. The device
  is disclosed, but its disclosed ground is false, and it leaves
  the Quran's most victory-dense surah inconsistent with the
  book's own standing seat. Separately, 48:27 renders "or hair
  cut short" as "йол пӱчкыме кӱчыкын" — йол is leg/foot; the hair
  word is ӱп. As seated, the verse speaks of legs cut short.
  That is a lexical error, disclosed nowhere.
- 48:25, which batch J calls its weakest, most compressed seat,
  reads clause-complete on a fresh read (barring, offering,
  unknown faithful men and women, unintentional-crime clause
  riding шонадыме сулык, dispersal counterfactual, punishment).
  The batch's self-flag overstates the damage; no failure taken.

## 11. Rulings on the disclosed open items

- Vienna Mari–English Dictionary licence variant: the licence
  record states plainly that the exact Creative Commons variant
  was not named in the pages retrieved and was not re-verified,
  and that the build's attestation base is the GiellaLT (LGPL v3,
  licence file read in full) and Wiktionary/kaikki (CC BY-SA)
  inventories harvested at the desk. The checker's inventory work
  confirms the seated vocabulary traces to those two inventories,
  not to any Vienna wording. The non-reliance claim holds.
  PASS — the open seat is honestly carried and may stand as
  recorded; no landing should upgrade the wording about the
  Vienna dictionary beyond "Creative Commons, attribution" until
  the variant is verified.
- Retained-Latin candidates: resolved seat by seat. al-Lat /
  al-Uzza (53:19) are Master-form divine names — legitimate.
  Sabean (2:62), Sabian (5:69), Bedouin (33:20) are the Master's
  group names seated as stems under the Mari plural -влак, the
  same names-policy paradigm as the 372 hyphenated name forms
  (116 distinct) — legitimate. The remaining fragments (a ×2,
  en ×1) are not retentions at all: they are the §7(a)
  corruptions. One further retention the build did not list:
  Umrah in Latin script at 2:158 and 2:196 — a rite name, neither
  a personal name nor a scripture title; it should be ruled on
  (Cyrillicised, device-rendered, or GAP-companioned) rather
  than left silent. Minor.
- Approximation seats (general): with the sole exceptions of the
  surah-48 victory device (§10) and the mosque split (§8), every
  disclosed approximation the checker sampled is what its notes
  claim — a clause carried on attested forms with a narrowed
  specific sense, logged in the batch notes. The approximation
  mechanism itself is honest.
- Minor inconsistencies recorded without failing weight: the
  title "Quran" stands in Latin 54 times but is Cyrillicised
  Коран 14 times (46:29, 47:24, 50:1, 50:45, 54:17, 54:22,
  54:32, 54:40, 55:2, 56:77, 59:21, 72:1, 73:4, 73:20); name
  suffixes are hyphenated in the early batches (Moses-лан) and
  fused in the later ones (Mosesым, Torahште — ≈40 tokens,
  surahs 38–54); batch B's long-verse fidelity list is batch A's
  list copied verbatim (it lists surah 2–3 verses for a surah
  4–6 batch) — the verses themselves sample clean, but that
  batch's fidelity record does not evidence its own check;
  5:110's "obvious sorcery" rides чын йомак ("true tale") on
  batch B's self-flagged йомак device, the weakest sense-carry
  the checker met.

## 12. What must happen before this book can land

1. Strip the embedded Basmalah line from seats 7:1, 8:1, 10:1;
   rebuild store-derived files; re-verify the 114-count.
2. Repair the five corrupted tokens (§7a) by codepoint.
3. Reseat сенг- → сеҥ- (4 seats) and шенгеч → шеҥгеч (31 seats).
4. Reseat or GAP нужналык/нуждалык (6 seats) and Мукш (17:1)
   under the GAP policy.
5. One ruling for mosque, applied to all 19 seats and disclosed
   on the book's face alongside the GAP terms.
6. Reseat surah 48's victory seats on сеҥымаш (48:1, 48:5, 48:18,
   48:24, 48:27) and correct йол → the hair word at 48:27; or
   bring the device to Robert as a decision point with the true
   inventory ground stated.
7. A Mari proofreader's ruling on the ашындыр- allomorph (20 seats).

Until those repairs are made and re-checked, the book stands
DRAFT — NOT PUBLISHED, and this checker does not pass it.
