# Landing Report — North Frisian, Mooring (frr) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

The landed claim in the same breath as its status: the North
Frisian — Mooring (frr) draft has landed on the GitHub shelf
as DRAFT — NOT PUBLISHED, and what lands is a lexical
skeleton and GAP map, not a readable translation — see the
binding reservation carried in full below.

## What landed

- `ayah-companion-manuscript-FRR.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its
  front matter carries DRAFT — NOT PUBLISHED on its face,
  names its base and sources, and discloses the GAP census.
- `quran-frr.txt` and `quran-frr.json` — the built book
  exactly as passed by the independent checker.
- `glossary.md` — the attested vocabulary of record.
- `BUILD-REPORT.md` and `BUILD-SPEC.md` — the build report
  and the lane build spec of record (the build report stands
  in this folder under the undated name, on the sibling-lane
  pattern; its lane original is
  BUILD-REPORT-2026-11-28.md).
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — the fresh
  independent checker: PASS-WITH-GAP-TIER-RESERVATION, with
  the §9 GAP-tier ruling carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-FRR-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `ATTESTATION-AUDIT-2026-11-28.md` — the attestation audit
  of record.
- `LICENCES-RECORDED-2026-11-28.md` — the licence record
  (English Wiktionary via kaikki.org, CC BY-SA, under the
  Mooring dialect screen; LearnFrisian Mooring wordlist,
  CC BY-SA 4.0, Mooring column only; Bendsen 1860, public
  domain, as historical control by fact and citation only).
- `MANIFEST.txt` — SHA-256 of every file above and of this
  report.

All copies in this folder were verified byte-identical to
the lane originals in `~/workspace/ayah-north-frisian/` at
landing (the build report against its dated lane original).

## Gate record

All figures below were re-verified at landing by this
desk's own count from the lane files of record, not taken
from the checker report alone; every figure matched the
checker's exactly.

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set
   equality store == Locked English Master grid TRUE
   (6,236 seats in each, no seat in either set that is not
   in the other); per-surah counts match the standard grid
   at all 114 surahs, mismatches NONE; `quran-frr.json`
   holds the same 6,236 verses with ZERO mismatches
   against verses-store.json; empty seats NONE; seats
   containing "redacted" NONE.
2. Canonical verify — PASS: 1:1 equals exactly «Önj noome
   ⟦GAP: god⟧, ⟦GAP: beneficent⟧, ⟦GAP: merciful⟧.»;
   1:3 equals exactly «⟦GAP: beneficent⟧, ⟦GAP:
   merciful⟧.»; the fixed Basmalah form occurs 113 times
   in `quran-frr.txt` (112 unnumbered opening lines, every
   one byte-identical to the fixed form, plus numbered
   verse 1:1), with exactly one occurrence in each surah
   except surah 9, which carries NONE.
3. Independent checker — PASS-WITH-GAP-TIER-RESERVATION:
   a fresh independent pass that built none of this text
   recomputed every quantitative claim and reproduced each
   one exactly — counts, seat-set equality, the GAP
   census, the dictionary figure, the attestation
   inventories, and both screens. No failure was found, so
   no failure seat lists arise.
4. GAP census — CONFIRMED figure for figure by this desk's
   own recomputation from verses-store.json: 6,190
   GAP-bearing seats, 50,826 GAP markers, 5,551 distinct
   GAP terms, agreeing with gap-census.json exactly; top
   terms reproduce (god 2,786; for 1,744; who 1,724; those
   1,189; lord 972; so 746; on 686; people 679; by 414).
   Only 46 of 6,236 seats are GAP-free.
5. Dictionary — CONFIRMED by this desk's own inventory-
   trace test: work/dict_core.py holds 494 candidate
   entries; 429 verified, 65 unverified, and the
   unverified set is exactly the set logged in
   work/unverified-dict.json. The 65 are held as GAPs, not
   seated.
6. Purple sweep / screens — reconciled: seated tokens 0
   untraced — this desk's own token screen over every
   non-GAP token found 456 distinct lower-cased seated
   token types, every one tracing to the Mooring
   inventory, the attested-plural set, or the explicit
   names allowlist, so 0 untraced types and 0 tokens;
   mixed-script NONE — no non-Latin alphabetic character
   occurs in the built text.
7. Historical-control fence — VERIFIED by this desk's own
   count: the Bendsen 1860 forms godd, göd, senne, and
   gnahse are seated 0 times each, and none stands in the
   Mooring inventory. The three build bugs (gunge / "God",
   hat / "it", diling / "this") were verified fixed by the
   checker (§8 of the checker report).

## Reservation carried with the landing — binding

**The checker's binding reservation, in full (§9 of the
checker report).** The tier is extreme and is stated
plainly: 6,190 of 6,236 seats (99.26%) carry GAP markers;
50,826 markers in total; the Basmalah itself — the most
familiar line in the book — is GAP-bearing for god,
beneficent, and merciful; core theological vocabulary
(God, lord, heaven, angel, soul, spirit, mercy, sin) and
core function words (for, who, on, by) are GAPs
throughout; only 46 seats are GAP-free. This is materially
beyond the GAP mass of the sibling lanes.

What lands is a lexical skeleton and GAP map, not a
readable Mooring translation of the Quran, and it must
never be described — on the shelf, in a manifest, or in
any post — as a translation without the GAP tier carried
in the same breath (6,190 of 6,236 seats GAP-bearing; God
and the Basmalah mercy names among the GAPs). Landing is
authorised by the checker verdict only under the existing
label DRAFT — NOT PUBLISHED, with the manuscript's current
honest face unchanged. Any future reduction of the GAP
tier must come from attested modern Mooring sources (the
named print dictionaries, under fact-and-citation fair
use), re-verified — never from relaxing the dialect or
historical fences.

The checker's ground for landability, in order: (1) the
gate law's own remedy for an unattested seat is the
visible GAP marker, never an invented or borrowed form,
and every alternative that would reduce the GAP count is
expressly barred and was verified unused; (2) nothing is
hidden — the GAP census, the God/mercy GAPs, and the
Basmalah's GAP form are disclosed on the manuscript's
face, in the build report, in BUILD-SPEC, in the
glossary, and in the attestation audit; (3) every
mechanical and fence claim was recomputed by the checker
and held exactly, the seated 429-entry core is genuinely
attested Mooring, and the GAP map (5,551 terms, counted)
is itself a usable work product.

## Notes

- No PDF is included: the manuscript Markdown, the built
  text, and the built JSON are the landed forms, on the
  pattern of the Komi-Zyrian, Chuvash, Southern Sámi, and
  Võro landings.
- Novelty wording stands only in the bounded form: no
  North Frisian Quran was found in the searches of
  27 November 2026; not found is not proven non-existent.
  No "first" claim is made anywhere in the landed files.
