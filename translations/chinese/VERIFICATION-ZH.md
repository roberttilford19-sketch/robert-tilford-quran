# Verification Report — Chinese Manuscript (Ayah Companion)

**Date:** 2026-09-24
**File:** `ayah-companion-manuscript-ZH.md`
**Method:** programmatic checks against the corrected English manuscript and the Spanish manuscript (format template + Arabic source).

## Structural checks — all passed

| Check | Result |
|---|---|
| Surah headers (`## N.`) | 114/114, sequential 1–114 |
| Verse references (`**s:v**`) | 6,236/6,236 |
| Per-surah verse counts | all 114 match expected counts, zero mismatches |
| Sequential numbering within surahs | 1..N, no gaps or duplicates |
| Global verse order | strictly ordered 1:1 → 114:6 |
| Arabic lines preserved | 6,348 non-header Arabic lines, byte-identical to the Spanish manuscript |
| Basmalah | 115 بِسْمِ lines = 1:1 verse + 112 surah-header blocks + 2 legitimate in-verse occurrences (11:41, 27:30); Surah 9 has no basmalah block |
| Latin characters in Chinese verse lines | none |
| Format | mirrors the Spanish template (headers, italic intros, basmalah blocks, `---` separators, prostration markers) |

## Notes on verification artifacts (not manuscript issues)

- 114 "arabic line diffs" vs. the Spanish file are the surah **header** lines, which legitimately differ (Chinese `麦加 · 7节` vs. Spanish `Mequí · 7 versículos`); all verse Arabic lines are byte-identical.
- 3 "missing Arabic line" flags (5:6, 84:21, 96:19) are checker artifacts: 5:6's translation spans multiple lines including the source's own variant-reading note, and 84:21/96:19 carry prostration markers (`*［叩头——建议的］*`, `*［叩头——必行的］*`) between the Chinese line and the Arabic line. The Arabic is present in all three.
- The `<redacted>` text reported by two workers in English 11:2/12:96/33:45/35:24 is a **display-pipeline rendering quirk**, verified at byte level: the English file reads "bearer of good news" cleanly. The Chinese renders it correctly (报喜者/报喜讯者).

## Chunk provenance

Translated by 10 worker agents in parallel ranges (1–4, 5–9, 10–16, 17–22, 23–28, 29–37, 38–47, 48–58, 59–77, 78–114), each with per-surah count confirmation. Two ranges (10–16, 48–58) required re-dispatch after first attempts produced no files; all re-dispatches delivered complete, verified chunks.

**Surahs 5–9 collision (resolved):** the original worker delivered late, after a re-dispatch was already running, and both wrote to the same three paths multiple times with conflicting name conventions (biblical-style vs Ma Jian-style). Sequence: original's biblical-style files → re-dispatch's Ma Jian-style chunk → final biblical-style chunk. The re-dispatch verified the final on-disk set (695/695, sequential, Arabic intact, basmalah correct) and confirmed no further writes. The canonical 5–9 uses biblical-style names (大卫, 所罗门, 以撒, 雅各, 约伯, 约拿, 罗得, 撒迦利亚, 以实玛利, 舒艾卜, 萨利赫; 哈伦, 胡德 kept), documented in the rewritten `chunks/glossary-notes-005-009.md`. The coordinator applied 4 consistency fixes to the final chunk (6:20, 6:89, 6:114, 7:196: English "the Book" → 这部经典 per mandate). The intermediate Ma Jian-style draft survives only in `work-005-009/zh.txt` (not merged).

**Surahs 10–16 collision (resolved):** the original worker's files landed late; the re-dispatch wrote a complete internally consistent set. The re-dispatch's set is canonical (665/665 + glossary + flags); superseded files preserved under `chunks/superseded/`.
