# North Frisian — Mooring (frr) Quran draft — build report (2026-11-28)

**Status: BUILD COMPLETE — STOPPED BEFORE LANDING, as ordered.**
Nothing was shelved, committed, or pushed. The draft stands in
~/workspace/ayah-north-frisian/ only, labelled DRAFT — NOT
PUBLISHED, and awaits a fresh independent checker who did not
build it.

## Lane authority
Opened in order under Robert Tilford's ruling of 2026-11-27,
21:16 CST (queue … Võro, North Frisian (Mooring)): Võro's build
is complete, so this lane opened in order with no fresh ruling
needed. The dialect built is Mooring (Bökingharde), Robert's own
specification in that ruling — not another North Frisian
dialect. Saterland Frisian was not touched; West Frisian
(frisian, PARKED as DRAFT — NOT PUBLISHED) was not touched.

## Counts (machine-verified, verify.py final run)
- Verses built: **6,236 / 6,236** — seat-set equality with the
  Locked English Master grid: true; per-surah mismatches: NONE;
  empty seats: NONE.
- Basmalah: 1:1 = "Önj noome ⟦GAP: god⟧, ⟦GAP: beneficent⟧,
  ⟦GAP: merciful⟧." (exact); 1:3 = "⟦GAP: beneficent⟧,
  ⟦GAP: merciful⟧." (exact); Basmalah lines in built text: 113
  (112 unnumbered openings + verse 1:1); surah 9 carries none.
- GAP census: **6,190 seats** carry GAP markers; **50,826
  markers**; **5,551 distinct GAP terms**. Census file:
  gap-census.json; disclosure:
  FLAGS-AND-GAPS-DISCLOSURE-FRR-2026-11-28.md.
- Dictionary size: **429 verified English–Mooring entries**
  seated (work/dict_core.py, screened by work/build_engine.py);
  65 candidate entries unverified and held as GAPs (listed in
  the disclosure). Attestation inventories: 3,685 Mooring forms
  (463 Mooring-sense kaikki entries, 113 untagged pan-dialect
  entries, 268 attested plurals, 178 LearnFrisian Mooring pairs);
  968 other-dialect-only entries excluded.
- Screens, run from the start as ordered: whitespace-token
  retained-Latin screen with explicit allowlist — **0 candidate
  types, 0 tokens**; mixed-script (non-Latin) screen — **NONE**;
  "redacted" string — NONE. Two bugs were found and fixed during
  the build and are part of the record (attestation audit): a
  stem device that seated "God" as gunge ("to go"), and a
  harvest rule that wrongly excluded the headword hat ("it").

## The headline honesty item, in the same breath
God, lord, heaven, angel, soul, spirit, mercy and sin have **no
modern Mooring seat in the held inventories** and stand as GAPs
throughout — including in the Basmalah. Bendsen (1860) attests
God in Mooring as Godd / Göd, but in 1860 spelling; under the
Historical Control Bar (the Võro lane's R2 applied alike) those
spellings corroborate historically and were not seated as
modern forms. Several everyday function words (for, who, on,
by) are likewise unattested for Mooring in the held record and
stand as GAPs. These are gaps of the held record, not claims
that Mooring lacks the words; the modern print Mooring
dictionaries (in copyright, none held) are the independent
checker's road to closing them.

## Sources
English Wiktionary via kaikki.org (CC BY-SA) under the Mooring
dialect screen; LearnFrisian Mooring wordlist (CC BY-SA 4.0,
Mooring column only); Bendsen (1860, public domain) as
historical control by fact and citation only. Full record:
LICENCES-RECORDED-2026-11-28.md;
ATTESTATION-AUDIT-2026-11-28.md. No person or institution
contacted.

## Files
- ayah-companion-manuscript-FRR.md — the draft with its honest
  face (DRAFT — NOT PUBLISHED, base, GAP census, devices).
- quran-frr.txt / quran-frr.json — built text (6,236 verses).
- verses-store.json — seat store; master-verses.json — Master grid.
- BUILD-SPEC.md, glossary.md, build.py, verify.py, assemble.py,
  work/build_engine.py, work/dict_core.py,
  work/unverified-dict.json, work/verify-candidates.json,
  work/basmalah.json.
- sources/ — kaikki-frr.jsonl, mooring-forms.json,
  mooring-plurals.json, eng2frr-mooring.json,
  learnfrisian-mooring.json, bendsen1860_djvu.txt, harvest.py.

## Novelty wording
No "first" claim anywhere, in any form. The brief's bounded
finding stands: no North Frisian Quran was found in the
searches of 27 November 2026; not found is not proven
non-existent.

## Next step (not taken)
A fresh independent checker pass, then Robert's word before any
landing. This build does not land, shelve, commit, or push.
