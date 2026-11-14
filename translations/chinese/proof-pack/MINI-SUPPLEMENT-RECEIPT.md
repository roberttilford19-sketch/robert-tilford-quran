# MINI-SUPPLEMENT RECEIPT — Probe PX-13 Repair (one row)
Applied 2026-10-13 ~00:01 CDT, on Robert Tilford's explicit approval (widget tap, 2026-10-13 ~00:01 CDT: "Approve the one-row repair — 向我求情").

## Provenance
- The Gemini probe's PX-13 entry (verse 23:27) was desk-verified by Awen during Step-2 preparation and found to contain a **verified divergent — a repair overshoot introduced by Patch Set 1's own P-03 row**. Pre-patch, 23:27 ran entirely in the divine singular （我启示 / 我的注视 / 我的启示）; the P-03 repair pluralized the verse's pronouns to match the EN's We/Our — correctly for four pronouns, but it swept the verse's final divine pronoun plural as well, where both the EN and the Arabic keep a deliberate singular. The probe caught what the patch phase introduced, before publication.
- Per PROBE-DECISION-RULES (1 verified divergent → mini-supplement path), Robert approved the single-row repair; targeted re-probe of PX-13 follows.

## The repair
- Verse: **23:27**
- OLD span: 不要为不义者向我们求情
- NEW span: 不要为不义者向我求情
- OLD span occurred exactly once in the master (verified pre-application).
- The verse's other divine pronouns stand unchanged, correctly matching the EN: 我们启示 (We revealed) / 我们的注视 (Our eyes) / 我们的启示 (Our revelation) / 我们的命令 (Our command).

## Warrants
- EN (Original Recital master): "And do not speak to **Me** about the wrongdoers." — singular *Me*.
- Arabic: وَلَا تُخَاطِبْنِي — *tukhāṭibnī*, "do not address **Me**" — singular suffix.

## Hashes
- v5 (before): `d8e1d3c3920cc44667a8596748652d8a460d9442d385fe9819e121e2b2a2ec7e`
- v6 (after): `50116db0f1a735917c1a91c0cf927006fd83784386610e8a1e3bf9a1216c2382`
- Live file: `patched/ayah-companion-manuscript-ZH-PATCHED.md`; frozen copy: `patched/ayah-companion-manuscript-ZH-PATCHED-v6.md` (identical hash). The staging anchor was not touched.

## Gate suite on v6 — ALL PASS
- (a) Verse parity: 6,236 / 6,236 verse markers, sequence identical to v5.
- (b) Arabic character total: 639,899 — identical to v5.
- (c) Isolation diff v5→v6: ONLY the 23:27 block differs; within it, the sole change is the deletion of 们 in 我们 → 我 at the repaired span. Preamble identical.
- (d) Do-not-touch verses byte-identical to v5: 2:275 ✓ · 5:60 ✓ · 16:36 ✓ · 39:17 ✓.

## State after this receipt
- Running repair total: 779 approved rows (Patch Set 1 + supplements + escapees) + 1 ruled harmonization (84:15) + this 1 mini-supplement row.
- Propagation remains gated on the probe closing under PROBE-DECISION-RULES; PX-13 targeted re-probe pending.
