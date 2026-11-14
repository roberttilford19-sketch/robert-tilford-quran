# ESCAPEE REPAIR RECEIPT — Chinese Ayah Companion, Patch Set 1 (post-v4)

**Authority:** Robert Tilford's ruling, 2026-10-12 ~22:39 CDT — "Fix all three escapees now."
**Scope:** the complete sampling-to-index escapee set {2:93, 2:286, 2:285-sub-item}, each verified REAL against both masters in SAMPLING-RECONCILIATION.md (E-1, E-2, E-3). No other verse was touched.

## Method

v4 was first frozen byte-identical as `patched/ayah-companion-manuscript-ZH-PATCHED-v4.md` (sha256 `439bbac0…`, cmp-verified). Each repair was applied verse-block-scoped: the target clause was asserted to occur **exactly once inside its own verse block** (and, as it happened, exactly once in the whole file) before replacement; replacement was by span splicing — no re-serialization, nothing else in the file rewritten.

## Per-row outcomes — 3 of 3 applied, 0 failed, 0 forced

| Verse | EN warrant (Recital master) | Before (v4) | After (v5) |
|---|---|---|---|
| 2:93 | "And the calf was poured into their hearts, for their disbelief." | 牛犊的爱充满了他们的心 ("the LOVE of the calf filled their hearts") | **牛犊被灌进了他们的心** ("the calf was poured into their hearts") |
| 2:286 | "You are our Protector — so help us against the disbelieving people." | 你是我们的主**和**保护者 (added 主 "Lord") | **你是我们的保护者** (added 主和 removed; the verse's faithful 我们的主啊 vocatives untouched) |
| 2:285 | "We heard and we obeyed." | 我们听从，我们顺服 （听从 = heed/obey; "heard" lost) | **我们听到了，我们顺服** (applied on the live v4 text, which already carries the verse's P-02 row; only this clause changed) |

## Gates (full suite on v5 — ALL PASS)

- **Parity:** 6,236/6,236 verse markers, sequence identical to v4, header identical. Census parity check: NONE — all 114 surahs exact.
- **Arabic:** 639,899 = 639,899 (both counting measures, \u0600–\u06FF and wide ranges); the Arabic line inside each of the 3 changed blocks is byte-identical to v4.
- **Isolation audit:** v4→v5 differing blocks = exactly {2:93, 2:285, 2:286}; each equals its approved repair; no verse in any other state.
- **Do-not-touch:** 2:275, 5:60, 16:36, 39:17, 2:276, 2:3 all byte-identical to v4; carriers intact (2:276 利息； 2:3 幽玄）.
- **Census re-run** (path-adapted copy of census.py): total candidate flags **5, all USURY-LIXI** — the five Ruling-1 no-change controls (2:275, 2:276, 2:278, 3:130, 4:161). Every other flag class 0. CN chars (census definition) 222,717.

## Hash chain

anchor `2030fe97…` → v1 `368835ad…` → v2 `11b3a78a…` → v3 `cf1c317b…` → v4 `439bbac032f00449ba06109a56a8ee47f650cd8961b224cc5180a6377a3c9ca8` → **v5 `d8e1d3c3920cc44667a8596748652d8a460d9442d385fe9819e121e2b2a2ec7e`**

Working master: `patched/ayah-companion-manuscript-ZH-PATCHED.md` (now v5). Propagation (workspace / staging / GitHub / archive.org) still awaits the probe close and Robert's word, per PROBE-DECISION-RULES.md.

## Follow-ons completed in the same pass

- **Probe feed refreshed to v5:** in `probe-feed/GEMINI-FEED-A2-CN.txt`, PX-22's body (the 2:93 entry) now carries the repaired v5 text — the byte-diff against the pre-refresh feed is exactly that one line. A2 integrity re-verified: 39 entries, **zero** `\d+:\d+` matches, all 42 verse texts verbatim in v5 (38 direct; the merged 112:1–4 entry PX-19 verified per-segment, concatenated equality). Robert's ruling superseded the "live test" design: Gemini will audit the repaired text blind.
- **`probe-feed/PROBE-PACK-FILLED.md`:** Entry 26's POST-PATCH CN updated to the v5 text; the internal diff-leg bookkeeping note for 2:93 amended to record the repair (it previously flagged the verse as unrepaired).
- **`probe-feed/PROBE-KEY-SEALED.md`:** PX-22's status updated from "LIVE-TEST — untouched in v4" to the v5 repaired status, with the ruling noted. (Key remains sealed; never fed.)
- **Proof pack:** this receipt copied into `proof-pack/`; PROOF-PACK-MANIFEST.md updated (receipt row added, escapee OUTSTANDING item marked ADDED with the v5 hash, hash-chain table extended to v5, and the pack's PROBE-PACK-FILLED.md copy refreshed from the updated source with its row re-hashed — the pack copy previously predated the feed refresh).

Nothing else was edited: staging anchor (2030fe97…) untouched, no git action, no uploads.
