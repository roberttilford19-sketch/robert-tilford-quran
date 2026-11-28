# Meadow Mari (mhr) Quran draft — REMEDIATION RECORD (2026-11-28)

Remediation crew: a crew that built none of this text. Source of
findings: CHECKER-REPORT-INDEPENDENT-2026-11-28.md (verdict FAIL),
applied in full under the audit-application standard, most serious
first, together with the two desk rulings carried in the task
(mosque unified to GAP book-wide; Umrah GAP-marked). Every figure
below was recomputed mechanically from the rebuilt files by
verify-remediation-2026-11-28.py and the build's verify.py.

**Status after this record: DRAFT — NOT PUBLISHED. Nothing was
landed, shelved, committed, or pushed. Landing waits on a fresh
independent re-check PASS, which has not been run.**

Method: remediate-2026-11-28.py applied asserted seat-by-seat
replacements (each old string required to occur exactly the
expected number of times in its seat, else abort) to
verses-store.json and to the work/batch-*.json sources, so the
lane cannot regress on a re-merge. The book files were then
rebuilt with build.py and assemble.py. 72 seat-edits were applied
to the store (plus the 32-token шеҥгеч class counted within them
by seat), distributed across batches A, B, C, E, F, G, H, I, J.

## 1. Basmalah duplicated in print at 7:1, 8:1, 10:1 — REPAIRED

The embedded unnumbered opening line was stripped from the head
of each seat:
- 7:1 — now "Alif, Lam, Meem, Saad."
- 8:1 — now begins "Нуно тый деч налме пай нерген йодыт. …"
- 10:1 — now begins "Alif, Lam, Ra. …"
Recomputed: the full Basmalah string occurs exactly **114** times
in ayah-companion-manuscript-MHR.md and in quran-mhr.txt (112
unnumbered openings + 1:1 + the in-verse quotation at 27:30).
Surah 9 carries none. 1:1 still equals the fixed form exactly.

## 2. Five mixed-script corrupted tokens — REPAIRED

Respelt in pure Cyrillic on their attested stems, by codepoint:
- 39:21 — ужat (Latin a, t) → ужат
- 39:30 — колat (Latin a, t) → колат
- 42:12 — шарa (Latin a) → шара
- 42:34 — пытарen (Latin e, n) → пытарен
- 43:83 — модaш (Latin a) → модаш
Recomputed: verify.py's retained-Latin candidates are now only
al ×2 (al-Lat / al-Uzza, 53:19 — adjudicated legitimate by the
checker) and the Master-form group names Sabean, Sabian, Bedouin.
The a ×2 and en ×1 corruption fragments no longer exist.

## 3. н-for-ҥ class, 36 tokens — REPAIRED

- 4:141 — сенгаш → сеҥаш
- 5:23 — сенгаш → сеҥаш
- 5:56 — сенгыше → сеҥыше
- 6:61 — Сенгыше → Сеҥыше
- шенгеч → шеҥгеч, 32 tokens in the checker's 31 seats (17:47,
  17:63, 17:110, 18:6, 18:28, 18:47, 18:64, 18:66, 18:70, 18:79,
  18:85, 18:89, 18:92, 19:5, 19:43, 19:59, 19:64, 20:16, 20:47,
  20:78, 20:84, 20:90, 20:93, 20:108, 20:110, 20:123, 20:134,
  26:215, 33:15, 37:90, 38:55), applied book-wide by string with
  the total asserted at exactly 32.
Recomputed: no token сенгаш, сенгыше, Сенгыше, or шенгеч remains
anywhere in the store; шеҥгеч now stands at 241 tokens (203
previously correct + 32 repaired + paradigm occurrences counted
by string, as the checker counted).

## 4. Unattested seatings — REPAIRED seat by seat

The нужналык family was reseated onto attested forms (the
book's own batch-K precedent: batch K rejected the Russian-shaped
stem and reseated onto нимодымо):
- 2:61 — нужналык → нимодымылык (Giella: "poverty")
- 2:268 — нужналыкым → нимодымылыкым
- 3:112 — нужналык → нимодымылык
- 9:28 — нужналык → нимодымылык
- 9:60 — нужналык-влаклан → нимодымо-влаклан (нимодымо, Giella:
  "destitute person, poor person, pauper"); and the seat's third
  family token, нужда (жд spelling, in "нужда корно еҥлан",
  the traveller in need), respelt onto the attested stem:
  нужна корно еҥлан (нужна, Giella adjective: "poor").
  The seat's first token, нужна-влаклан ("the poor"), already
  rides the attested stem нужна and was left as seated.
- 9:120 — йӱаш нуждалыкым → йӱаш тӱнымашым (тӱнымаш, Giella:
  "want, need, necessity"); the batch-C "approximation" device
  is retired — the seat now carries "thirst" as a drinking-need
  on an attested noun, the rest of the verse untouched.
Recorded nuance, for the re-checker: the жн spelling нужналык
does stand in the Giella inventory as harvested in
sources/mhr-lemmas.json (gloss "poverty"), while the жд spellings
нуждалык (9:120) and нужда (9:60) stand in no inventory. The
reseats above were applied to all six seats as directed, so no
form of the family remains at any of the six seats under either
reading of the checker's §7(c).
- 17:1 — Мукш (coinage for "Farthest") retired by the GAP
  device under the mosque ruling (§5 below): the seat now reads
  "Шнуй ⟦GAP: mosque⟧ гыч, ⟦GAP: mosque⟧ деке". Мукш occurs
  nowhere in the rebuilt book.

## 5. Mosque — DESK RULING APPLIED book-wide

Ruling: unify all mosque seats to the GAP treatment the book's
face already discloses. The 19 Master mosque seats now all carry
⟦GAP: mosque⟧ — 20 markers in all (17:1 carries two, for the
Sacred Mosque and the Farthest Mosque):
- Already GAP, unchanged: 2:144, 2:149, 2:150, 2:191, 2:196,
  2:217 (6 markers).
- From храм / Шнуй Храм: 5:2 (Шнуй Храм гыч → Шнуй ⟦GAP:
  mosque⟧ гыч), 8:34 (деч), 9:7 (воктене), 9:19 (Шнуй Храмым →
  Шнуй ⟦GAP: mosque⟧-ым), 9:28 (дек), 9:107 (храм шогалтат →
  ⟦GAP: mosque⟧ шогалтат), 9:108 (Храм, кудо → ⟦GAP: mosque⟧,
  кудо), 48:25 (деч), 48:27 (Шнуй Храмшке → Шнуй ⟦GAP:
  mosque⟧-шке).
- From храм at 17:1 (×2): see §4.
- From кумалме вер: 2:187 (кумалме вер-влакыште → ⟦GAP:
  mosque⟧-влакыште).
- From Шнуй Пӧрт: 22:25 (Шнуй Пӧрт гыч → Шнуй ⟦GAP: mosque⟧ гыч).
- From мечеть: 22:40 (мечеть-влак → ⟦GAP: mosque⟧-влак, in the
  verse where synagogue is already GAP-marked).
Not mosque seats, correctly untouched: 8:35 (храм for the
Master's "the House") and 17:7 (храмшке for "the Temple") — храм
remains the book's attested temple loan at those seats, and
7:29 / 7:31 (кумалме вер for "place of worship", non-mosque
seats) are likewise untouched. The manuscript's front matter now
names the mosque among the standing gap terms.
Revised GAP census (recomputed exactly, §8 below): mosque ×20.

## 6. Surah 48 victory device — REPAIRED

сеҥымаш stands in the inventory (Giella: "victory, defeat, win")
and was already seated at 20+ other seats; the batch-J ground
("no victory lemma found") rested on the Russian spelling сенг-.
The five кугу полыш ("great help") seats were reseated onto the
сеҥымаш family, following the book's own forms at 57:10 and
61:13 ("лишыл сеҥымаш"):
- 48:1 — пале кугу полышым → пале кугу сеҥымашым
- 48:5 — кугу полыш уло → кугу сеҥымаш уло
- 48:18 — лишыл кугу полышым → лишыл кугу сеҥымашым
- 48:24 — кугу полышым → кугу сеҥымашым
- 48:27 — лишыл кугу полышым → лишыл кугу сеҥымашым
Recomputed: кугу полыш occurs nowhere in the rebuilt book;
surah 48 now carries сеҥымаш ×5.
Hair fix at 48:27: "йол пӱчкыме кӱчыкын" (legs cut short) →
"ӱп пӱчкыме кӱчыкын" — ӱп is the attested hair word, seated in
that sense at 30:54 ("ош ӱпым", white hair).

## 7. Umrah — DESK RULING APPLIED

Ruling: GAP-mark Umrah at 2:158 and 2:196, consistent with the
book's pilgrimage GAP practice. Recorded here as the ruling
applied:
- 2:158 — ышта Umrah → ышта ⟦GAP: Umrah⟧ (1 marker).
- 2:196 — да Umrah Юмылан → да ⟦GAP: Umrah⟧ Юмылан; and the
  seat's second, Cyrillicised mention (умра, which stands in no
  inventory) GAP-marked for consistency within the seat:
  кӧ ⟦GAP: Umrah⟧ гыч кая (2 markers).
⟦GAP: Umrah⟧ ×3 in all; no Latin "Umrah" and no "умра" remain
outside the markers.

## Minor items — disposition

- ашындыр- allomorph (22 occurrences, 20 seats): LEFT
  UNTOUCHED, as directed — held as an uncertainty for a Mari
  proofreader, recorded here and in the revised disclosure;
  not treated as a failure.
- Коран / Quran spelling variation (Latin "Quran" ×54,
  Cyrillicised Коран ×14) and name-suffix hyphenation (early
  batches hyphenated, later fused): LEFT AS RECORDED MINOR
  ITEMS. No mechanical fix was applied: the variation is
  disclosed in the checker report, touches no attestation or
  fidelity seat, and a book-wide respelling by string would
  risk seats this crew cannot re-verify by reading. Recorded
  here so the re-checker sees the disposition was deliberate.

## 8. Machine verification of the rebuilt book (recomputed)

- Seats: verses-store.json 6,236; master-verses.json 6,236;
  seat sets exactly equal. quran-mhr.json flattened: 6,236
  seats, text identical to the store at every seat.
- Per-surah grid against the standard grid: no mismatches,
  all 114 surahs. Empty seats: none. "redacted": none.
- Basmalah in the assembled manuscript: exactly 114.
- GAP census, recomputed exactly from the store: **298 GAP
  seats, 339 GAP markers, 5,938 verses rendered in full.**
  By term: scripture ×107, hell ×97, jinn ×32, covenant ×24,
  mosque ×20, pilgrimage ×16, usury ×8, Sabbath ×7, Umrah ×3,
  debt ×3, dowry ×2, fly ×2, and ×1 each: manna, cucumbers,
  garlic, lentils, onions, witchcraft, swine, gambling, Ark,
  donkey, palms, vines, martyrs, synagogue, olive, hail, palm,
  hoopoe. The disclosure's revised seat list is the machine
  list from this same count. Delta from the pre-check census:
  +10 GAP seats (2:187, 8:34, 9:7, 9:28, 9:107, 9:108, 17:1,
  22:25, 48:25, 48:27), +17 markers (mosque +14, Umrah +3).
- Hill Mari bar: no token or character ӓ / ӹ / Ӓ / Ӹ anywhere.
- Purple sweep (verify.py rerun): 7,509 distinct Cyrillic
  tokens (was 7,522), 1,413 untraced candidate types (was
  1,421); none of the repaired defect forms (шенгеч, сенгаш,
  сенгыше, нужналык, нужда, Мукш, мечеть, the five corruptions)
  appears in the candidate list, and every replacement form
  (шеҥгеч, сеҥымаш, нимодымо, нимодымылык, тӱнымаш) traces.

## Files changed

verses-store.json; quran-mhr.txt; quran-mhr.json;
ayah-companion-manuscript-MHR.md (rebuilt); work/batch-A.json,
batch-B.json, batch-C.json, batch-E.json, batch-F.json,
batch-G.json, batch-H.json, batch-I.json, batch-J.json (same
seat edits at source); assemble.py (front matter now names the
mosque and the Umrah among the standing gap terms);
FLAGS-AND-GAPS-DISCLOSURE-MHR-2026-11-28.md (revised census,
seat list, and open-seat record). Scripts:
remediate-2026-11-28.py, verify-remediation-2026-11-28.py.

## Stop line

The remediation stops here, before landing, as directed: the
book is NOT landed, shelved, committed, or pushed. It stands
DRAFT — NOT PUBLISHED, awaiting a fresh independent re-check.
