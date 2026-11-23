# Chavacano (Zamboangueño) Quran lane — BUILD RECORD, 2026-11-23

Built on Robert's build word, main chat 2026-11-23 01:20 CST (all six census-buildable lanes, concurrently, standard pipeline).

## Sources (held in sources/)
- **De Castro 2019**, *Chavacano de Zamboanga: Idiomatic Expressions and Chavacano-English Dictionary* — Zamboangueño-specific MINI dictionary (~2,580 entries), all rights reserved, openly posted by the author; held as the author's dataset form (2,578 rows) and rendered lexicon. Primary lexical authority.
- **SEAlang Library Chavacano Dictionary** — Riego de Dios, *Composite Dictionary of Philippine Creole Spanish* (1987/1989, ~6,542 entries), free, search interface only; centre COTABATO, Zamboangueño comparative. Supplement only; De Castro and the control govern conflicts (census Addendum 2).
- **CONTROL — NEW TESTAMENT ONLY, named as such:** *El Nuevo Testamento na Chabacano* (1981, rev. 2008), open via eBible.org; held in full (HTML zip + plain text, 1,536,430 bytes). No Old Testament exists in Chavacano.
- **Orthography:** the control's Filipino/phonetic orthography.

## Build
From the Locked English Master (`ayah-audit/corrected/ayah-companion-manuscript.md`, Part I), 16 chunks translated in parallel, attested forms only, gaps held open in [brackets] and disclosed. Basmalah uniform: "Na nombre de Dios, el Benevolente, el Misericordioso." God = Dios, Lord = Señor.

## Gates
- **Count:** 6,236/6,236 verse markers, sequence identical to master; per-surah 114/114 exact.
- **Canonical verify:** all 6,462 Arabic-bearing lines byte-identical to the master, in sequence; Basmalah 114; sajda notes 15/15 (11 recommended, 4 obligatory), uniform "postracion" form (one missing note at 41:38 restored and spelling variants normalised at assembly).
- **Independent checker** (did not build it): **PASS WITH CORRECTIONS** — language sample of 40: (a) real Chavacano 24, (b) Chavacano frame with coinage/Spanish-substituted lexis 16, (c) not Chavacano 0; attestation confirmed (checker's method 92.93%; desk method 92.79% after corrections); fidelity sample 12 verses, 2 errors found. Report: CHECKER-REPORT-CBK-2026-11-23.md.
- **Corrections applied (all 8, diff-verified, battery re-run clean):** C1 12:41 [crucifica] unbracketed (attested; false gap); C2 6:146 [tripa] unbracketed (attested; false gap); C3 orphan unified as held-open [huerfano] at all 23 seats (unattested in both sources); C4 Sacred Mosque unified as "(Sagrado) Lugar de Oracion" (mezquita unattested); C5 duplicated Surah 41 summary line after 41:38 deleted; C6 2:282 two spurious "Si" removed; C7 3:20 "guia o sila" → "guiao sila"; C8 flags-019-022 disclosed Spanish-derived set bracketed as held-open, reconciled with 31:16.
- **Purple-style sweep vs the current master:** verse sequence, per-surah counts and Arabic reconciled exactly against the master as above; no zakat percentage; markers 15/15.
- **Held-open gaps disclosed:** 227 bracketed segments in verse text at checker count (136 distinct; chiefly [jinn] ×23, [Hajj], [Aqui Despues], [usury]), plus the C3/C8 unifications — every one logged in FLAGS-CBK.md (610 flag lines + desk corrections note). Attestation settles existence, not fluency — the caveat rides with the figure.

## Landed copy
`ayah-companion-manuscript-CBK.md` — 2,336,922 bytes, SHA-256 833e5321a2581146db32d3ac964f8d32228146dcda1411a0d38557e4626970eb (post-corrections).
