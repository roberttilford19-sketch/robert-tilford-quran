# Lule Sámi (smj) Quran lane — INDEPENDENT CHECKER REPORT

Checker: independent checker agent (built none of the text).
Date: 2026-11-27. Store checked: `verses-store.json` (6,236 seats) against
`master-verses.json` (6,236 seats), BUILD-SPEC.md, glossary.md,
ATTESTATION-AUDIT-2026-11-27.md, batch notes A–L, and
`work/verify-candidates.json`. All counts below were recomputed by script
from the store itself, not copied from the builders' notes.

## VERDICT: FAIL

Grounds, in brief: (1) the fixed orthography is breached at scale —
892 forbidden characters seated in 630 of 6,236 verses; (2) Northern
Sámi (sme) lexemes and spellings are seated as Lule Sámi, against the
spec's explicit "NEVER seat a Northern Sámi form"; (3) batch I's GAP
census is not honest as claimed — a large share of its 544 GAP markers
mark seats that the book's own attested devices carry elsewhere;
(4) the clause sample found dropped/distorted clauses at 9:117, 17:52
and 11:88. What passes is listed at the end; the failures are
correctable, but they are a rework of whole batches, not a correction
list, so this cannot be PASS WITH CORRECTIONS.

---

## 1. Clause-by-clause sample (72 verses, 6 per batch, all 12 batches)

Sample seats (deterministic spread — batch positions 1, ~104, ~208,
~312, ~416, last): A: 1:1, 2:97, 2:201, 3:19, 3:123, 4:27 ·
B: 4:28, 4:131, 5:59, 6:43, 6:147, 7:86 · C: 7:87, 7:190, 9:13, 9:117,
10:92, 11:87 · D: 11:88, 12:68, 14:18, 15:70, 16:75, 17:51 ·
E: 17:52, 18:44, 19:38, 20:44, 21:13, 22:5 · F: 22:6, 23:31, 24:17,
25:57, 26:84, 26:188 · G: 26:189, 27:65, 28:76, 30:23, 33:3, 34:34 ·
H: 34:35, 36:39, 37:60, 37:164, 38:86, 40:27 · I: 40:28, 41:46, 43:43,
44:58, 47:31, 51:5 · J: 51:6, 52:49, 54:42, 56:13, 57:21, 64:1 ·
K: 64:2, 68:33, 70:33, 74:17, 76:25, 79:8 · L: 79:9, 81:24, 85:19,
90:9, 98:6, 114:6.

69 of 72 carry every clause — by Lule Sámi text, a disclosed device,
or a GAP marker. The renderings are close paraphrases, often good
(e.g. 4:131, 7:86, 12:68, 22:5's long creation sequence, 57:21, 98:6,
where "the Polytheists" is carried descriptively as "ædnag Jubmel
jáhkkij", many-god believers). The shortest-ratio seats in the whole
book (1:4 "Duobmobiejve Hærrá"; 26:195; 70:3) were also checked and
carry their clauses in compressed form; they are not drops.
39:7 and 48:8 (the Master's literal "<redacted>" seats) are rendered
for their surrounding sense and the string "redacted" appears nowhere.

### Dropped / distorted clauses — failures by seat

- **9:117** — "those who **followed him** in the hour of difficulty"
  is rendered "sijáv, gu **jáhkin** su lossat ájgge" — *believed* him.
  The following clause is dropped and replaced by a different verb;
  the book's own verb for "follow" (tjuovvu-) is used elsewhere.
- **17:52** — "you will respond **with His praise**" is rendered
  "dij vástedibme **Su dakkamujn ja ármmujn**" — with His *deeds and
  mercy*. The praise clause is not carried.
- **11:88** — "**My success** lies only with God" is rendered "Mu
  **vuojnŋa** la dušše Jubmela lut" — my *rest/spirit* is only with
  God. The success clause is not carried (and the seat also seats
  Northern dušše, §2).

### Weakened renderings — corrections required, not counted as drops

- **3:123** — "God had given you **victory** at Badr" → "vaddám dijij
  **buorrev** Badr" (gave you *goodness*). Victory seat thinned.
- **2:201** — "the **torment** of the Fire" → "dållå **duobmos**"
  (the Fire's *judgement*, the duobmo device). Torment seat thinned.
- **22:5** — "**Resurrection**" → "**Árbbedime**", a formation on the
  árbb- stem family (inheritance/honour; cf. notes-B's unsure
  "árbbedijdda girddo", gate of honour). It is logged in notes-E as a
  descriptive rendering, so it is a disclosed device — but the stem
  does not mean resurrection, the seat is GAP-marked or carried by
  bajás-iellem / Duobmobiejvve devices everywhere else (resurrection
  GAP ×15 book-wide), and a reader meets an inheritance-word where
  the Master says Resurrection. Same formation at 4:139. Both seats
  must be re-rendered by GAP or by the book's standing devices.

## 2. Orthography — FAIL (1983 standard, Norwegian variant)

The spec fixes Æ (not Swedish Ä), ŋ (not ń), and Lule Sámi forms only.
Recomputed character census of the whole store:

| Character | Occurrences | Seats affected | Finding |
|---|---|---|---|
| ä (Swedish) | 474 | 397 | Swedish-variant spelling seated, e.g. läh, guäddi, seämma, jáhkkebähpet |
| Ä | 2 | 2 | 20:39 (Ädno), 30:42 (Äjlan) |
| š (Northern) | 286 | 157+ | dušše ×120, ráŋggáštus family, arabijlaš, dárbbaš- |
| đ (Northern) | 100 | 68 | gieđa family, viektevuođa, duohtavuođa, Boađe |
| č (Northern) | 26 | 26 | čáppis, čiehk(k)a-, čoahkke- families |
| Č | 3 | 3 | 32:6, 34:3, 62:9 |
| ž (Northern) | 1 | 1 | gáržes, 6:125 |
| ŋ / ń / ŧ | ŋ used throughout; ń = 0; ŧ = 0 | — | this part of the spec is kept |

Total: **892 forbidden characters in 630 seats (10.1% of the book).**
Per batch, only batch A is clean; B ä47/š70/đ30, C ä129, D š83,
E ä73, G ä52, I š48/đ25, J š58, K ä31, L ä56, H ä19/š23, F đ2.
This is not typo scatter: whole inflectional systems are seated in the
wrong variant (the -bähpet 2pl verb endings with ä passim; dušše
"only" ×120 where the attested Lule form duola appears at e.g. 25:57).

Northern Sámi lexemes/spellings seated as Lule Sámi (spec: NEVER):
**gieđa** "hand" for Lule **giehta** (giehta is in GiellaLT and
Wiktionary; gieđa traces to neither, §5); **dušše** for duola;
**čáppis** "beautiful" (no č- word can be Lule Sámi in this norm);
**ráŋggáštus** (Northern spelling, ×21+) beside the book's own correct
**ráŋástus** (×22) — the two spellings of "punishment" alternate
across batches, e.g. Northern form at 34:35.

## 3. GAP honesty — MIXED; batch I fails the honesty test as stated

Book-wide census (recomputed): **813 GAP markers in 546 seats, 408
distinct GAP terms.** Batches A–H and J–L together carry 269 markers;
their GAPs are mostly genuine concrete terms (heifer, cucumber,
garlic, lentil, onion, ape, donkey at 2:61/2:65/2:259) plus the three
standing GAP terms (pilgrimage ×19, Sabbath ×7, jinn ×37), and angel
is GAP-marked consistently book-wide (×35 incl. "angels"). No verse
anywhere is left as English or near-English: a scripted scan found
zero verses of English text outside GAP markers, and zero verses in
batch I with ≥3 English function words outside markers. The text
around the markers is Lule Sámi throughout. That part is honest.

**Batch I (40:28–51:5) does not hold.** It carries **544 markers in
322 of its 520 seats, with 316 distinct GAP terms** — two-thirds of
the whole book's GAP mass in one-twelfth of the book. Notes-I states
these seats have "no attested form in the seated glossary". That is
not true for a large share of them; the book itself carries the same
seats elsewhere on attested stems or logged devices:

- punishment ×18 — carried elsewhere as ráŋástus (and suhtto devices);
- Messenger/messengers ×27 — carried elsewhere as báhkobuktije, the
  logged "word-bringer" device (×33 book-wide);
- Hell ×10 — carried elsewhere as helvit (GiellaLT stem, ×16);
- Paradise ×5, Garden/Gardens ×~12 — carried elsewhere as paradijssa
  (GiellaLT stem, ×21);
- pray/prayers/worship ×~23 — carried elsewhere by the logged
  hållat-Jubmelin prayer device;
- Resurrection ×5 — GAP in A, but carried by bajás-iellem and
  Duobmobiejvve devices in D/E;
- rain (42:28) — arve "rain" is attested and used elsewhere in the
  book (arvev tokens in the store);
- servants ×16 — bálvvalij "servant" forms are seated elsewhere,
  including inside batch I's own range outside GAP markers.

So batch I's GAPs are disclosed, and no clause is silently dropped
because of them — but they are not "genuinely unattested terms".
They are an undisclosed change of method mid-book: one batch
GAP-marking common seats the other eleven batches render. The GAP
census as published (813) therefore overstates the language's gaps
and understates batch I's inconsistency, and notes-I's attestation
claim for the batch must be corrected. Genuinely unattested GAP
terms in I do exist in number (tower, yokes/chains, thunderbolt,
skins, horizons, and the like) — the failure is the mixture, not the
existence.

## 4. Basmalah — PASS

1:1 in the store is exactly:
**"Jubmela namán, dat Vájmodis, dat Ármmogis."** — character-for-character
equal to the BUILD-SPEC form. Both mercy seats rest on the attested
stems vájmmo and ármmo (§5).

## 5. Attestation spot-check — core 30/30 traced; extended probes fail

Thirty distinct content tokens taken from the text (the glossary core)
were traced against the GiellaLT stem inventory
(`sources/giellalt-stems.json`, stems cleaned of lexc codes), the
Wiktionary lexicon (`sources/lexicon-wikt.json`), the glossary, the
attestation audit, and the batch notes:

jubmel, almme, ednam, girjje, vájmmo, ármmo, biejvve, månno, násste,
várre, jávrre, idja, iellem, álmmuk, ulmusj, nissun, mánná, bieggá,
buorre, bahá, ballo, doajvvo, ráffe, soahte, gieresvuohta, bálges,
báhko, suddo, duobmár, gånågis — **30 of 30 traced (100%)**, every one
to GiellaLT, most also to Wiktionary with the right gloss (e.g.
ednam "earth, world; land", låhkåt-type verbs in the wider check:
diehtet, javllat, boahtet, vaddet, bårråt, tjállet all trace to both
inventories; värro traces to Wiktionary "sacrifice; tax";
paradijssa and helvit trace to GiellaLT and the batch notes).

Extended probes beyond the thirty, aimed at the §2 seats, do **not**
trace: **gieđa** (no GiellaLT/Wikt entry; giehta traces), **čáppis**
(no entry; no č- stem exists in the inventory), **dušše** (no smj stem
entry — attested Lule duola/duolak is in the inventory), and
**Árbbedime** (traces only to a batch-note mention, on the árbb-
inheritance stem family). The core lexicon is honestly attested; the
Northern intrusions are not.

Note on `verify-candidates.json`: it lists 7,083 "unknown" distinct
tokens. That instrument output is a candidate list, not a verdict —
its crude ending-stripping fails on ordinary inflected Lule Sámi and
even on function words (la, sij, jus, gå) that are plainly genuine.
I did not count it against the build; the tracing above used the
cleaned stem inventory directly.

## 6. What passes

- Seat grid: 6,236 of 6,236, per-surah counts all correct, no empty
  seats, batch files A–L sum to the store.
- Basmalah exact (§4). "redacted" nowhere; 39:7 and 48:8 handled per spec.
- No English or near-English verse anywhere; no invented form found
  for the three standing GAP terms (pilgrimage, Sabbath, jinn are
  GAP-marked every time).
- Core vocabulary attestation: 30/30 (§5).
- 69 of 72 sampled verses carry every clause (§1).

## Required before this lane can be re-checked

1. Purge all 892 forbidden characters (630 seats): ä/Ä → æ/Æ in the
   Norwegian variant; every č/š/ž/đ form replaced by its Lule Sámi
   form (giehta, duola, ráŋástus, etc.) or GAP-marked where no Lule
   form is attested.
2. Re-render batch I's non-genuine GAP seats (punishment, messenger,
   hell, paradise/garden, prayer/worship, rain, servants, and the
   rest that the book's devices already carry), and correct notes-I's
   attestation claim; publish a GAP census split by genuine vs.
   device-available seats.
3. Fix the dropped/distorted clauses at 9:117, 17:52, 11:88, and the
   weakened seats at 3:123, 2:201, 22:5, 4:139.

**Final verdict: FAIL** — on orthography at scale (892 forbidden
characters, 630 seats), Northern Sámi forms seated against the spec's
explicit ban, batch I's GAP census not being genuinely-unattested as
claimed (544 markers, 316 terms, dozens of them device-available),
and dropped clauses at 9:117, 17:52 and 11:88. The skeleton of the
build — grid, Basmalah, core attested lexicon, clause coverage in
69/72 sampled verses — is sound and is recorded above in the same
breath as the verdict.
