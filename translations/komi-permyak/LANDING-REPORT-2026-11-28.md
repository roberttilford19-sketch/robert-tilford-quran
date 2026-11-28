# Landing Report — Komi-Permyak (koi) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-KOI.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Komi-Permyak, перем
  коми кыв, ISO 639-3 koi — the Kudymkar-based literary
  standard, in Cyrillic, the Russian alphabet plus і and ӧ,
  fenced distinct from Komi-Zyrian (kpv); GiellaLT giella-koi,
  LGPL v3, and the Komi-Permyak lexicon of English Wiktionary,
  CC BY-SA, as attestation sources, with the Batalova &
  Krivoshchekova-Gantman dictionary tradition (1985) and the
  modern Komi-Permyak New Testament (Бур Юӧр 2019, Institute
  for Bible Translation, Finland) as controls by fact and
  citation only — a complete New Testament only, with no
  complete-Bible claim), discloses the build tier, the GAP
  census, and the flagged seats, and states that no claim is
  made that this is the first Komi-Permyak Quran translation.
- `quran-koi.txt` and `quran-koi.json` — the built book exactly
  as passed by the independent re-check. Recount at landing,
  from the lane files of record, verified by this landing
  desk's own count: the verse store, the Master seat-set, and
  the flattened built JSON each hold 6,236 seats, identical at
  every seat.
- `glossary.md` — the attested vocabulary of record.
- `BUILD-REPORT-KOI-2026-11-28.md` and `BUILD-SPEC.md` — the
  build report (with its dated remediation addendum) and the
  lane build spec of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — first
  independent checker: FAIL.
- `REMEDIATION-RECORD-2026-11-28.md` — every repair, seat by
  seat.
- `CHECKER-REPORT-RECHECK-2026-11-28.md` — fresh independent
  re-check of the remediated text: PASS, with the GAP-tier
  reservation and the one disclosed residual carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-KOI-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `ATTESTATION-AUDIT-2026-11-28.md` — seat-by-seat attestation
  audit (with its dated remediation addendum).
- `LICENCES-RECORDED-2026-11-28.md` — the licence record.
- `MANIFEST.txt` — SHA-256 of every file above.

All copies in this folder were verified byte-identical to the
lane originals in `~/workspace/ayah-komi-permyak/` at landing.

## Gate record

1. Machine count — PASS, verified at landing by this desk's
   own count: 6,236 of 6,236 verses; seat-set exactly equal to
   the Locked English Master (no missing, no extra); per-surah
   grid exact at all 114 surahs (grid sum 6,236);
   `quran-koi.json` flattens to 6,236 seats and is identical to
   the verse store at every seat; no empty seats; the string
   "redacted" appears in no seat. Master provenance: the Locked
   English Master MD5 ecc5b8e2848e5044186b7ad82bed9f4e, as
   recorded in the lane's licence record. First verse 1:1
   «Енлӧн нимӧн, Милӧсьта, Милӧсьта.»
2. Canonical verify — PASS: 1:1 equals the BUILD-SPEC fixed
   Basmalah form «Енлӧн нимӧн, Милӧсьта, Милӧсьта.» character
   for character; in `quran-koi.txt` the Basmalah occurs
   exactly 113 times (112 unnumbered opening lines plus the
   numbered verse 1:1, with surah 9 correctly carrying none);
   seat 1:3 reads «Милӧсьта, Милӧсьта.» — the spec form,
   verified character for character at landing.
3. Independent checker — FAIL, then remediation in full, then
   a fresh independent re-check: PASS. The full chain:
   - First checker FAIL (CHECKER-REPORT-INDEPENDENT-2026-11-28)
     on §7 alone: the Zyrian plural shapes the build reported
     as caught and removed in fact stood in the text —
     эскісьяс ×272 and вӧчісьяс ×67, 339 tokens in 313 seats,
     carrying the Komi-Zyrian plural suffix -яс on three core
     terms (believers, disbelievers, wrongdoers), against
     BUILD-SPEC's own Permyak plural rule; with two small
     items confirmed in the same report: seat 1:7's final
     clause seating the guide verb нуӧтӧ at the "misguided"
     neighbourhood, and the alms standing-family list
     unreconciled with the seated generic seat корӧм. Every
     other head passed, several exactly (recount, grid,
     Basmalah including 1:3, GAP census, retained Latin 0,
     mixed script exactly the 6 disclosed, dictionary, and
     the GAP tier under §9's reservation below).
   - Remediation (REMEDIATION-RECORD-2026-11-28), applied
     under the standing gate law in the checker's §10 order,
     every fix made in the engine's source and the whole book
     rebuilt from it: the PHRASES table now seats the Permyak
     agent plurals эскісььэз / Оз эскісььэз / Лёк вӧчісььэз
     (stem-final сь doubled + -эз) at exactly the checker's
     313 listed seats; a direct OVERRIDE seat "misguided" →
     вошны corrects 1:7 and all six other "misguided" seats
     (16:25, 18:104, 26:86, 27:41, 36:47, 56:51); the alms
     rule is reconciled across the attestation audit addendum,
     BUILD-SPEC, and the glossary; the closed records were
     corrected by dated addendum, never silently rewritten;
     and verify.py was tightened so a -яс ending can no longer
     be absorbed letter by letter.
   - Fresh independent re-check PASS
     (CHECKER-REPORT-RECHECK-2026-11-28): every §10 item
     verified complete at the seat level — -яс plural tokens
     0 in the store, the built text, and the manuscript; the
     replacement forms at exactly the checker's 313 seats
     (эскісььэз 272 tokens in 250 seats, вӧчісььэз 67 tokens
     in 66 seats, the three both-token seats 2:254, 17:82,
     34:31); all seven "misguided" seats seating вошӧ; the
     alms reconciliation consistent in all three places; the
     tightened screen returning exactly the two fault tokens
     on a reconstructed unrepaired text and 0 on the repaired
     text — and every headline figure of the remediated book
     holding to the digit.
4. Purple sweep — reconciled, candidates only under house law:
   the re-checker's own whole-text screen returns 841 distinct
   Cyrillic tokens with 0 untraced on the tightened rules
   (tokens containing ӧ: 369 types; containing і: 35 types),
   and its comparison against the Komi-Zyrian inventory found
   no other Zyrian-only form seated — the only tokens standing
   in the kpv inventory but not in a raw koi inventory are the
   disclosed paradigm/derivation forms traced by both
   checkers. Verified at landing by this desk's own count:
   retained Latin on whitespace tokens, GAP interiors
   excluded, against the explicit allowlist in verify.py —
   allowlisted 129 types / 1,056 tokens; non-allowlist
   retained Latin 0 types / 0 tokens; mixed-script tokens
   exactly the 6 disclosed name + -лӧн genitive tokens
   (Adamлӧн 5:27; Pharaohлӧн 7:127, 40:28, 40:37; Abrahamлӧн
   11:74; Josephлӧн 12:58); other mixed tokens NONE.
5. GAP census — recomputed by both checkers and verified at
   landing by this desk's own count: 5,444 GAP seats, 16,840
   GAP markers, 4,728 distinct GAP terms, 792 verses without a
   marker; bracket integrity 16,840 opening ⟦ and 16,840
   closing ⟧. (The companion manuscript carries 16,841
   markers — the text's 16,840 plus the front matter's
   explanatory example.) Top terms: used ×149, things ×108,
   belongs ×73, should ×50, doubt ×48, fight ×43, blessed ×40,
   considered ×40, reached ×39, wronged ×39. Seated
   dictionary 1,318 entries (replicated at landing by this
   desk: RAW 1,318, seated 1,318, dropped as unverified 0;
   the +1 over the pre-remediation 1,317 is the direct
   "misguided" seat), against inventories of 77,661 GiellaLT
   giella-koi lemmas, 14,725 glossed dictionary lemmas, 15,533
   gt-norm paradigm forms, and 334 English Wiktionary
   Komi-Permyak headwords.

## Reservation carried with the landing

**The GAP-tier reservation — stated plainly.** This book is
landed under the first checker's ruling
PASS-WITH-GAP-TIER-RESERVATION, carried forward unchanged by
the re-check. 5,444 of the 6,236 seats are GAP-bearing
(87.3%), carrying 16,840 visible markers, and only 792 verses
are rendered without a marker (12.7% clean-verse share — the
GAP-heaviest draft the desk has produced, as the checker
recorded). It is a first-pass engine build over a 1,318-entry
verified dictionary for a language whose open attested base
is thin: every Master content word with no verified
Komi-Permyak seat carries the visible marker ⟦GAP: <english
term>⟧ rather than an invented or silently borrowed form, and
the census is disclosed on the book's own face. No house rule
sets a GAP ceiling, and the tier's honesty is verified, not
merely claimed; no GAP-reduction pass was required before
landing, and a future GAP-reduction pass — enlarging the
seated dictionary — remains open as ordinary revision work.
Any future claim about this book must carry the census with
it, in the same breath. The book is DRAFT — NOT PUBLISHED.

## Disclosed non-blocking residual carried with the landing

The re-check records, in the same breath as its PASS, one
known residual that was not among the first checker's §10
required items and does not contradict any §10 item: the verb
tokens "misguide" (6:125, 7:155, 16:37, 22:4) and "misguides"
(7:186, 13:33, 18:17, 40:33) — 8 seats in all — still seat the
guide verb нуӧтӧ, indistinguishable in the text from "guide"
at the same seats, by the same mis- prefix-stripping route
that the remediation closed for "misguided". The remediation
record disclosed it in the open and left it as built for the
re-checker to sample; the re-checker listed it in full as a
known disclosed residual for any future dictionary pass. The
noun "misguidance" (7:30, 14:18, 16:36) GAP-marks at all
three seats — no fault there.

## Notes

- No PDF is included: the manuscript Markdown, the built text,
  and the built JSON are the landed forms, on the pattern of
  the Komi-Zyrian and Chuvash landings.
