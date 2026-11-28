# Lule Sámi (smj) Quran lane — INDEPENDENT RE-CHECK after remediation

Checker: fresh independent re-checker agent (built none of the text,
remediated none of it; a previous checker dispatch produced nothing,
so this is the deciding check). Date: 2026-11-27.
Store checked: `verses-store.json` against `master-verses.json`,
BUILD-SPEC.md, CHECKER-REPORT-INDEPENDENT-2026-11-27.md (the FAIL),
REMEDIATION-RECORD-2026-11-27.md and work/remediation-log.json.
Every figure below was recomputed by my own scripts from the store
itself; no figure was copied from the remediation crew's log. Where
the crew's log and my recomputation can be compared, they agree
exactly (forbidden 892 → 0; GAP book 813/546/408 → 638/469/377;
batch I 544/322/316 → 369/245/284; 175 markers re-seated in batch I).

## VERDICT: PASS

All five checks pass in full. The grounds are stated check by check
below, in the same breath as the verdict, with the two tracing
caveats that do not rise to failures disclosed at §2.

---

## 1. Forbidden-character census — PASS (zero)

Recomputed over all 6,236 seats, character by character:

| Character | Before (first checker) | Now (recomputed) |
|---|---|---|
| ä | 474 | **0** |
| Ä | 2 | **0** |
| š | 286 | **0** |
| đ | 100 | **0** |
| č | 26 | **0** |
| Č | 3 | **0** |
| ž | 1 | **0** |

**Total: 0 forbidden characters in 0 seats** (was 892 in 630 seats).
Also zero: ń, ŧ, Š, Đ, Ž. The Norwegian variant (Æ æ, ŋ) holds
throughout. The remediation record's claim of 892 → 0 is verified,
not taken on trust.

## 2. Northern lexemes and replacement tracing — PASS

None of the named Northern lexemes remain, in any inflected form:
substring searches for gieđ-, dušš-, čápp-, ráŋggášt- (case-insensitive,
whole store) all return **zero**. Specifically gieđa, dušše, čáppis
and ráŋggáštus are gone.

Replacement forms, spot-traced against `sources/giellalt-stems.json`
(stems cleaned of lexc codes: leading `#»` and trailing class digits
stripped), `sources/lexicon-wikt.json`, and the book's own usage
outside batch I (seats counted by script):

| Replacement | Occurrences / seats | Trace |
|---|---|---|
| duola | 155 occ, 145 seats (121 outside I) | GiellaLT stems duolak/duolag exact; the book's own form at e.g. 25:57 |
| giehta | 75 occ, 67 seats (60 outside I) | GiellaLT exact; Wiktionary exact, gloss "hand; arm" |
| ráŋástus | 79 occ, 78 seats (44 outside I) | The book's own established punishment form outside batch I. Caveat, in the same breath: no standalone GiellaLT stem ráŋást- exists in the cleaned inventory (the only GiellaLT hit is the compound ráŋggáštusláhka, which itself carries the Northern spelling); the trace rests on the book's own established usage, which is the basis the first checker itself named for this form |
| tjáppis | 10 occ, 10 seats (all outside I) | GiellaLT stem tjápp- exact (tjáppag, tjáppedit family) |
| tjiehka | 10 occ, 10 seats (all outside I) | GiellaLT exact |
| tjoahkke | 17 occ, 17 seats (all outside I) | GiellaLT exact |
| gártjes | 1 occ, 1 seat (6:125, outside I) | GiellaLT exact |
| ådås | 17 occ, 16 seats (15 outside I) | GiellaLT exact; Wiktionary exact, gloss "new; something new; news" |
| helvit | 35 occ, 35 seats (23 outside I) | GiellaLT exact |
| paradijssa | 41 occ, 41 seats (24 outside I) | GiellaLT exact |
| báhkobuktije | 50 occ, 48 seats (24 outside I) | Book's logged "word-bringer" device; compound of báhko (GiellaLT exact) + bukta- stem (GiellaLT bukta/buktal exact) |
| dievnara | 17 occ, 16 seats | GiellaLT stem dievnár exact; book's servant form at 2:186 (dievnara) and 2:90 (dievnarij) outside batch I |
| hålla Jubmelin | 11 occ, 11 seats (3 outside I) | Book's logged prayer device at 2:3/2:43; hålla stem GiellaLT exact, Jubmel exact |
| bajás-iellem | 7 occ, 7 seats | Book's resurrection device (seated at 22:5, batch E, outside I); components trace: bajás- compounds and iellem exact in GiellaLT, iellem exact in Wiktionary ("life") |
| vuojtto | 21 occ, 20 seats (18 outside I) | GiellaLT exact |
| gudne | 117 occ, 107 seats (90 outside I) | GiellaLT gudne- stems (gudnedibme, gudnekråvnnå, gudneássje family) and the book's own honour/praise usage throughout. Caveat, in the same breath: Wiktionary's gudna is a homograph glossed "ash"; the gudne trace rests on the GiellaLT gudne- stems and the book's usage, not on Wiktionary |

**No replacement form is untraceable** to the inventory or to the
book's own established devices. Every form the remediation seated
was already the book's form somewhere outside the seats it repaired,
or is an exact GiellaLT/Wiktionary stem.

## 3. GAP census — PASS

Recomputed census:

| Scope | Markers | Seats | Distinct terms |
|---|---|---|---|
| Book-wide, before | 813 | 546 | 408 |
| **Book-wide, now** | **638** | **469** | **377** |
| Batch I (40:28–51:5, 520 seats; key set verified exactly the Master's 40:28–51:5 range), before | 544 | 322 | 316 |
| **Batch I, now** | **369** | **245** | **284** |

The checker's named device-available terms no longer sit as GAP
markers in batch I — verified term by term, including substring
searches so no inflected or compound marker escapes: punishment,
Messenger/messengers (all cases), Hell, Paradise, Garden/Gardens,
pray/prayers, worship/worshipers, servants, Resurrection and rain
all return **zero** GAP markers in batch I (the only "rain" substring
hit is the genuine term "grain" at 50:9). They are re-seated on
ráŋástus, báhkobuktije, helvit, paradijssa, hålla Jubmelin/hållama,
dievnastit/dievnastiddje, dievnara, bajás-iellem and arve, as §2
traces. The crew's claimed reseat count (175) reconciles exactly
with the census movement (544 − 369 = 175).

Judgment on the remaining batch I GAPs: they are genuine gaps or
standing terms. The standing terms among them — jinn ×4 and angels
×7 in batch I — are GAP book-wide by spec policy (book-wide:
jinn ×37, angel ×26 + angels ×9, pilgrimage ×19, Sabbath ×7; jinn is
GAP-marked at every Master occurrence in the book). The remainder
are concrete terms with no standing device in the book (tower,
yokes/chains, thunderbolt, skins, horizons, sheath, jugular vein,
brocade, and the like — the same class the first checker recorded as
genuine). A small number (service, fruit, play, example) are rendered
contextually at individual seats elsewhere in the book, but none has
a standing device of the kind the first checker named, and
GAP-marking them is the spec's own honest fallback: the seat is
visibly marked, never silently dropped and never filled with an
invented form. notes-I.md carries the dated correction the first
checker required, appended with the original text unaltered; I read
it in place.

## 4. Clause checks — PASS

### The seven repaired seats, against the Master

- **9:117 — PASS.** "gu tjuovvun suv lossat ájgge" — *followed him*
  in the hour of difficulty (tjuovvu-, the book's own follow verb,
  2:143). Redeemed / Emigrants / Supporters / hearts almost swerved /
  pardoned / Kind, Compassionate all carried.
- **17:52 — PASS.** "dij vástedibme Su gudnijn" — you will respond
  *with His praise*. Day / calls / stayed only a little all carried.
- **11:88 — PASS.** "Mu vuojtto la duola Jubmela lut" — *My success*
  is only with God (vuojtto, GiellaLT exact; Northern dušše gone).
  Every other clause of the long verse carried.
- **3:123 — PASS.** "vaddám dijij vuojttov Badr" — gave you
  *victory* at Badr. Weak / fear God / thankful carried.
- **2:201 — PASS.** "suojede mijáv dållå ráŋástusas" — protect us
  from the *torment of the Fire* (elative of ráŋástus). Goodness in
  this world and the Hereafter carried.
- **22:5 — PASS.** "epán bajás-iellem birra" — in doubt about the
  *Resurrection*, on the book's standing device. The full creation
  sequence (dust, drop, clot, lump of flesh partly developed and
  partly undeveloped, clarify, wombs, designated term, infants, full
  strength, pass away, vilest age, not know after having known,
  earth still, water sent down, vibrates and swells, lovely pairs)
  is carried clause by clause.
- **4:139 — PASS.** "Åtsi sij gudnev sijás? Buok gudne gullá
  Jubmelij." — Do they seek *glory* in them? All *glory* belongs to
  God. Ally with disbelievers instead of believers carried.

Observation, not a failure: the Árbbed- family remains at other
seats (5:116, 6:100 "Glory be to Him"; family/inherit/honour seats
elsewhere). The first checker named only 22:5 and 4:139 for repair,
and the remediation record disclosed in the open that it left the
unflagged seats untouched. That is the checker's own scope, kept.

### Fresh clause sample — 36 verses, 3 per batch, all 12 batches

Seats (first, middle and last seat of each batch):
A: 1:1, 2:254, 4:27 · B: 4:28, 5:112, 7:86 · C: 7:87, 9:66, 11:87 ·
D: 11:88, 15:19, 17:51 · E: 17:52, 19:91, 22:5 · F: 22:6, 25:6,
26:188 · G: 26:189, 29:41, 34:34 · H: 34:35, 37:113, 40:27 ·
I: 40:28, 44:7, 51:5 · J: 51:6, 55:40, 64:1 · K: 64:2, 72:14, 79:8 ·
L: 79:9, 88:12, 114:6.

**Result: 36 of 36 carry every clause** of the Master — by Lule Sámi
text, by a disclosed device (e.g. intercession by the prayer device
at 2:254; praise by gudne at 64:1), or by a GAP marker (extravagant
at 40:28; jinn at 114:6). No dropped or distorted clause was found.
Noted in particular: 34:35, the seat the first checker cited for the
Northern punishment spelling, now seats ráŋástuvá; 9:66 now seats
"stráffep" for "We will punish" with no forbidden character; the
shortest seats (51:5, 51:6, 79:9, 88:12) carry their clauses in
compressed form and are not drops.

## 5. Canonical checks — PASS

- Seat count: **6,236**; seat-set equality with the Master: **exact**
  (no missing, no extra).
- Per-surah counts: all 114 match the standard grid; zero mismatches.
- Batch files A–L sum to 6,236 and match the store seat for seat
  (zero mismatches).
- 1:1 is exactly the fixed Basmalah:
  **"Jubmela namán, dat Vájmodis, dat Ármmogis."** —
  character-for-character equal to the BUILD-SPEC form.
- The string "redacted" appears **nowhere** (39:7 and 48:8 rendered
  for their surrounding sense, per spec).
- Empty seats: **none**.
- No verse left as English outside GAP markers: a scripted scan for
  English function words outside GAP markers found no English verse;
  the only repeated hits are the Lule Sámi particles go/gå (7:169,
  10:59), in verses that are Lule Sámi throughout. GAP markers
  themselves carry English terms by design, as the spec prescribes.

---

**Final verdict: PASS** — forbidden characters recomputed at zero in
6,236 seats; no Northern lexeme remains in any inflected form and
every replacement traces to the GiellaLT/Wiktionary inventory or the
book's own established devices (§2 caveats stated in the same
breath); batch I's device-available GAPs are re-seated (census
638/469 book-wide, 369/245 in batch I, both recomputed) and its
remaining GAPs are genuine or standing; the seven named clause seats
are repaired and a fresh 36-verse sample across all 12 batches
carries every clause; and the canonical grid, Basmalah, "redacted"
and no-English checks all pass. The lane is fit to land on this
record, subject to Robert's own hand on the landing, which is his
and not this checker's.
