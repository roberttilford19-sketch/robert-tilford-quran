# P-03 SUPPLEMENT APPLICATION RECEIPT — Chinese Ayah Companion, Patch Set 1

**Applied:** 2026-10-12 (America/Chicago) · **Authority:** Robert approved all 48 rows of `P03-SUPPLEMENT.md`.
**Method:** verse-block-scoped replacement on the working master. Each row's Current CN was asserted verbatim (exactly one occurrence) inside its own verse block before replacement; no row was forced. v3 was frozen and byte-verified before editing.

## Hash chain

| Stage | sha256 | Bytes |
|---|---|---|
| Staging anchor (untouched) | `2030fe97…` | — |
| v1 (719-row application, 692 applied) | `368835ad…` | 2,135,954 |
| v2 (quarantine clearance, 719/719) | `11b3a78a…` | 2,135,551 |
| v3 (particle supplement + 84:15 harmonization) | `cf1c317bdb95b3e750d87cbb8b7b6805b84bb7cd5058242010880a0c8207b84e` | 2,135,602 |
| **v4 (this pass)** | **`439bbac032f00449ba06109a56a8ee47f650cd8961b224cc5180a6377a3c9ca8`** | **2,135,794** |

Frozen copies kept beside the working file: `ayah-companion-manuscript-ZH-PATCHED-v1.md`, `-v2.md`, `-v3.md` (v3 byte-verified `cf1c317b…` before this pass).

## Outcome

**48 of 48 rows applied · 0 assertion failures · 0 forced.**

- Mode A （我→我们 at the flattened divine clauses) — 41 rows: 18:103, 44:30, 44:32, 46:26, 59:21, 64:10, 64:12, 65:8, 66:12, 67:5, 68:16, 68:17, 68:35, 68:39, 68:44, 69:11, 69:44, 69:45, 69:49, 70:7, 70:39, 70:40, 70:41, 71:1, 72:16, 73:5, 73:15, 74:16, 75:3, 75:4, 75:18, 76:2, 76:3, 76:4, 76:28, 77:16, 77:18, 77:20, 77:25, 77:38, 77:44.
- Mode B (dropped divine object restored as 于我们） — 2 rows: 8:59, 29:39.
- Mode C (zero-pronoun divine subject restored) — 4 rows: 77:17, 77:21, 80:26, 95:5.
- Mode D (third-person substitution reversed inside the provided-clause only) — 1 row: 30:28 （真主赐予你们 → 我们赐予你们； the 他 narration frame untouched, per the row's specification).

The two combined rows landed as single combined finals: **70:40** 不——我以东西方的主发誓，我们确是全能的 (oath-singular 我以…发誓 untouched per its guard) and **75:4** 的确，我们确能重造他的指尖 (particle repair from v3 + pronoun repair here). Guards honored throughout: 68:44's 留给我 (EN "leave Me") and all creature speech, Say:-confessions, prayers, and royal human We remain singular/untouched — verified present and unchanged in the isolation audit (only the 48 target blocks differ).

## Gates — full suite on v4, ALL PASS

- **Parity:** 6,236/6,236 verse markers; marker sequence identical v3→v4; header byte-identical. census.py parity check independently reports "NONE — all 114 surahs exact".
- **Arabic:** 639,899 chars (U+0600–06FF) in v3 = 639,899 in v4; per-block Arabic segments identical across all 6,236 blocks — Arabic untouched.
- **Isolation audit:** v3→v4 differing blocks = exactly the 48 target verses; each differing block equals its v3 block with exactly its supplement proposed text substituted (verified verbatim, block by block). No verse in any other state.
- **Do-not-touch:** 2:275, 5:60, 16:36, 39:17 byte-identical v3→v4; 2:276 byte-identical and still carries 利息； 2:3 byte-identical and still carries 幽玄.
- **census.py re-run (path-adapted copy, original untouched):** total candidate flags **5, all USURY-LIXI** — the ruled Ruling-1 controls, exactly as expected. CN han/punct chars 222,719; Arabic 639,899.

## We-census regression (path-adapted copy of we-census.py; original script and its WE-CENSUS outputs untouched)

Same script, same baked-in hand-review overrides, three texts:

| Text | Verses w/ divine We | PRESERVED | MIXED | FLATTENED | Repair set (script) |
|---|---|---|---|---|---|
| Staging (original census, hand-reviewed) | 1,165 | 870 | 4 | 291 | **295** |
| Frozen v3 (script re-run, baseline) | 1,165 | 1,109 | 2 | 54 | 56 |
| **v4 (script re-run)** | 1,165 | **1,157** | **1** | **7** | **8** |

Clause level, v3→v4: FLATTENED clauses 62 → 8 (PRESERVED 1,421 → 1,475). **All 48 supplement targets read PRESERVED in v4** — the script repair set shrank by exactly 48. Combined genuine P-03 population (census 295 + manifest-only 28:57) is now fully applied: 248 manifest rows + 48 supplement rows.

**Residue: 8 script-flagged verses, 0 genuine — every one disproved by direct quotation of the v4 text.** Script flags are candidates, not verdicts (the standing caveat); the residue decomposes into two known instrument artifacts:

1. **Frozen hand-review overrides (5)** — the script's OVERRIDES table stamps FLATTENED verdicts recorded at census construction (staging era) over verses the manifest's P-03 rows have since repaired; the stamp replaces the judged verdict unconditionally, so the script cannot self-clear them. 2:57 (MIXED; override at clause 1) reads 吃我们赐给你们…他们没有亏待我们 — plural throughout. 25:21 reads 与我们相会 (the exact locus the override named). 27:83 reads 我们从每个民族集合…否认我们迹象. 41:15 reads 否认我们的迹象 (the 'Ad quote 谁比我们更有力 is creature speech, correctly untouched). 61:14 reads 我们援助了信道者 (clause-1 locus).
2. **Anchor-window misses (3)** — 23:31, 23:42, 43:23 were census-FLATTENED verses repaired by manifest P-03 rows; the script's clause anchor sits on the fronted time-phrase and misses the subject. V4 reads: 23:31 我们兴起了另一代人 · 23:42 我们兴起了其他世代 · 43:23 我们没有向任何城镇派遣警告者 — all plural, all repaired.

No P-03 residue requiring a further repair row was found.

## Files

- Working master (v4): `patched/ayah-companion-manuscript-ZH-PATCHED.md` — sha256 `439bbac0…` (above).
- Nothing else was edited: the staging anchor, workspace manuscript, GLOSSARY-ZH, all sweep reports, census scripts and their original outputs are untouched. Propagation (workspace / staging / GitHub / archive.org) remains a separate step on Robert's word.
