# Independent Checker Report — Chavacano (Zamboangueño) Quran Lane

**Date:** 2026-11-23
**Checker:** Independent checker (did not build this text; graded cold)
**Built text:** `ayah-companion-manuscript-CBK.md`
**Master:** `ayah-companion-manuscript.md`, Part I only (lines 188–26512)
**Lexicon:** De Castro 2019 (`decastro-lexicon.txt`, 2,578 entries)
**Control:** Chavacano NT only, 1981 (`chavacano-NT-ebible-plain.txt`)
**Flags reviewed:** all 16 files in `work/flags-*.md`

## VERDICT: PASS WITH CORRECTIONS

The book is structurally complete and is, in the sample, genuinely Chavacano in grammar. It does not land as-is: eight required corrections are listed at the end, two of them false held-open gaps where an attested form exists, and three of them cross-chunk inconsistencies the flags themselves expose. None of the corrections requires retranslation of a surah; all are local.

---

## 1. Structural checks

| Check | Master | Built text | Result |
|---|---|---|---|
| Verse markers | 6,236 | 6,236 | PASS |
| Verse sequence (S:V order) | — | identical to master, element by element | PASS |
| Per-surah counts | 114 surahs | identical for every surah; no diffs | PASS |
| Arabic lines | 6,462 Arabic-bearing lines (incl. 114 surah-name lines) | 6,462; sequence identical line-for-line to master Part I | PASS |
| Basmalah, uniform string "Na nombre de Dios, el Benevolente, el Misericordioso." | 112 italic headings + 1:1 (+ 27:30 internal, capitalised differently in English) | 114 occurrences of the exact string: 112 italic headings + 1:1 + 27:30 internal | PASS |
| Basmalah placement | Surah 9 has none | Surah 9 has none (its summary even notes "sin un basmala") | PASS |
| Sajda (prostration) notes | 15 | 15, at the same verses, with the same recommended/obligatory split (11 recommended, 4 obligatory), rendered `*[postracion — recomendado]*` / `*[postracion — obligatorio]*` | PASS |

Sajda note verses, both files: 7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 32:15 (obligatory), 38:24, 41:38 (obligatory), 53:62 (obligatory), 84:21, 96:19 (obligatory). The Arabic sajda symbol ۩ also appears on 15 lines in both files.

**One structural anomaly (correction C5 below):** after 41:38, the built text inserts a duplicate of Surah 41's italic summary line — `*Detallado: el maga señal ya explica, y un pueblo que ya habla que el di amon maga corazon tiene cubrida.*` — between the verse and its Arabic line, ahead of the (correctly present) sajda note. The line already stands in its proper place under the Surah 41 heading. Line-type counts otherwise match the master (114 headings, 114 Arabic-name lines, 6,236 verses); one verse in each file (5:6) wraps onto a continuation line, in both, so that is inherited, not a defect.

## 2. Language sample — 40 verses

**Method:** deterministic spread — verses at indices 0, 156, 312, … (every ~156th of 6,236), i.e. 1:1, 2:150, 3:20, 3:176, 4:132, 5:112, 6:147, 7:138, 9:13, 10:40, 11:87, 13:9, 15:70, 16:127, 18:44, 19:89, 21:12, 22:56, 24:16, 26:31, 26:187, 28:23, 30:22, 33:54, 36:38, 37:111, 38:84, 40:77, 43:41, 46:12, 51:3, 53:50, 56:11, 59:20, 68:31, 72:10, 76:22, 80:11, 85:16, 93:2. Graded against Zamboangueño markers (maga plural, el article, ya/ta/ay aspect, con/na marking, control pronouns came/kita/vosotros/sila) and the lexicon/control.

**Counts: (a) 24 — (b) 16 — (c) 0.**

### (a) Real Chavacano — 24 verses

- **2:150** — "Y donde quiera ustedes esta, volve di inyo maga cara para ese. Para el maga gente nuay ningun argumento contra ustedes — sino sila quien ta hace mal entre ila. Poreso no teme con ila, pero teme con Mi, para ay completa Yo di Mio maga bendicion sobre ustedes, y para ay queda ustedes guiao." Full marker set: maga, di inyo, nuay, con marking, ay future.
- **11:87** — "Ya habla sila, 'Oh Shuaib, ¿el di tuyo oracion ta manda ba contigo que kame ay abandona cosa di amon maga padre ya adora, o hace con di amon riqueza cosa kame quiere?'" Exclusive-we kame/diamon used correctly against the addressees.
- **28:23** — "Hende came puede saca agua hasta el maga pastor ay sale, y el di amon tata un hombre bien viejo." hende negation, came, ay, di amon — control grammar throughout.

Also (a): 4:132, 5:112, 10:40, 15:70, 19:89, 21:12, 22:56, 24:16, 26:31, 26:187, 30:22, 33:54, 38:84, 46:12, 51:3, 53:50, 56:11, 59:20, 68:31, 76:22, 93:2.

Note on 51:3 ("Y aquellos que ta move suavemente"): "move" looks like an English insertion but is not — De Castro lists `move (verb) = to move` and the NT control uses "move" (e.g. "puede kita move"). It grades (a).

### (b) Chavacano frame with coinage, uncertain or Spanish-substituted lexis — 16 verses

- **3:20** — "Si ya entrega sila, entonces guia o sila" — the frame is Chavacano (ya aspect, sila, di vos deber amo lang comunica), but "guia o sila" is a garbled form where "guiao sila" (they are guided) is meant; see also fidelity, §3.
- **9:13** — "Ay tu no pelea un gente quien ya viola di ila maga juramento, y ya planea para exilio el Mensajero, y ya principia maga hostilidad contra tu? Hace tu miedo con ila?" Chavacano frame, but the question construction is broken and "maga hostilidad" is a Spanish abstract plural substituted into it.
- **36:38** — "Y el sol ta corre para su destino. Asi el diseño del Todo Poderoso, el Todo-Sabiente." ta corre is right; "Todo-Sabiente" is a coined calque of "the All-Knowing" (no such compound attested) and "diseño" is a straight Spanish substitution.

Also (b): 1:1 (prescribed Basmalah formula; na frame, lexis wholly Spanish), 3:176 ("el otro vida" substituted for the Hereafter, inconsistently with the [Aqui Despues] gap used elsewhere), 6:147 ("Poseedor de misericordia infinito" — Spanish "Poseedor" where "Dueño" is used elsewhere), 7:138 (singular "Tu amo… un ignorante gente" addressed to a people), 13:9 (epithet string, no aspect marking), 16:127, 18:44 (garbled "Ese porque el autoridad parte de Dios"), 37:111, 40:77, 43:41 ("vengansa"), 72:10 ("malo intendido"), 80:11, 85:16.

### (c) Effectively not Chavacano — 0 verses

None of the 40 is plain Spanish or plain English. The nearest approaches, 13:9 and 85:16, still carry Chavacano structure (el + epithet order; "Hacedor de cosa Ele quiere" word order) and are graded (b), not (c). No verse in the sample lacks the maga/el/aspect/con-na system entirely.

## 3. Fidelity sample — 12 verses against the master English

Verses: 2:150, 2:282, 3:20, 4:11, 5:112, 7:138, 11:87, 22:56, 24:2, 28:23, 40:77, 65:1 (ten drawn from/near the §2 spread, plus the long debt verse 2:282 and the inheritance verse 4:11 as stress tests).

**ERRORS found: 2.**

- **2:282 (ERROR, minor)** — Master closes: "And fear God. God teaches you. God is aware of everything." Built text: "Y teme con Dios. **Si** Dios ta enseña con ustedes. **Si** Dios sabe todo." A spurious "Si" (if) is prefixed to both final statements, turning two assertions into conditionals. The rest of this very long verse is faithful, including the two-men / one-man-and-two-women witness rule.
- **3:20 (ERROR)** — Master: "If they have surrendered, then they are guided." Built text: "Si ya entrega sila, entonces guia o sila" — the predicate is garbled ("guia o sila" for "guiao sila"); the meaning is obscured, though recoverable from context.

No other meaning drift in the twelve. 4:11's fractions (two-thirds, one-half, one-sixth, one-third) are all correct; 24:2's hundred lashes and witness group are correct; 65:1's divorce conditions are correct; 5:112's "fiesta" for the feast from heaven is a loose but not meaning-changing rendering.

## 4. Attestation — percentage of verse-text tokens attested

**Method (stated in full, since the figure depends on it):** verse lines only (`**S:V**` lines in the built text). Tokens = lowercase alphabetic sequences (accents retained). Bracketed gap segments excluded in the headline run. Vocabulary = De Castro headwords (the word before the part-of-speech parenthesis, split into words: 2,618 distinct tokens) ∪ all distinct tokens of the NT control plain text (3,718 distinct), union 4,845. A token counts as attested if it appears in that union. No stemming or inflection-folding.

**Result: 154,321 of 166,053 tokens attested = 92.93%.** With bracketed gap tokens left in, 92.81% (154,342 / 166,302).

**The desk's figure of 92.78% is CONFIRMED** within tokenisation tolerance (±0.15 points; the small spread is punctuation/apostrophe handling). The checker does not correct it.

Caveat that rides with the figure: the unattested residue (11,732 instances, 2,336 distinct) is not mostly exotic coinage — its top items are ordinary Spanish-derived forms and inflections the two sources happen not to list in that exact shape (inyo ×520, nosotros ×160, misericordia ×154, disuyu ×147, misericordioso ×134, sabio ×116, baja ×115, trae ×103, rechaza ×89), plus proper names kept per the brief (Moses ×88, Quran ×68, Pharaoh ×40). The 92.78% is a strict-form match rate, not a measure of how much of the text a Zamboangueño reader would recognise.

## 5. Gap honesty

**Count: 227 bracketed segments in verse text, 136 distinct** (262 bracketed segments in the whole file, the rest in surah titles and summaries). The flags files disclose the same population verse by verse.

Checked every distinct gap against De Castro headwords and the NT token set. The great majority are genuinely unattested in both sources — e.g. [jinn] ×23, [Hajj] ×8, [usury] ×5, [retaliation] ×4, [ganado], [orphan], [mostaza], [balanza]-family [scales], [rope] (no cuerda/soga/cordel in either source) all check out as unattested. Phrase gaps built from attested words ([Aqui Despues], [santidad de peregrino], [con guirnalda]) are conservative — the compound/concept is unattested even though its words are — and are disclosed as calques/phrases in the flags. That is honest holding-open.

**Two gaps are false — the word is attested (corrections C1–C2):**

- **12:41 [crucifica]** — De Castro: `crucifica (verb) = to crucify`, `crucificao (adjective) = crucified`; the NT control uses crucifica/crucificao dozens of times. The flags file for this chunk claims "verb form not attested in De Castro / NT control." That claim is wrong.
- **6:146 [tripa]** — De Castro: `tripa (noun) = intestine`. The flags claim no attested form. Wrong. (The companion gap in the same verse, [garra] claws, is genuinely unattested and stands.)

## 6. Flags files — disclosed uncertainties that bear on landing

The 16 flags files are thorough, but they disclose — and in places contradict each other on — four things that should be settled before landing:

1. **Orphan (blocking inconsistency).** flags-005-006 renders orphan as unbracketed "huerfano," claiming the NT control attests the concept; flags-092-114 brackets [orphan] at 93:6, 93:9, 107:2, stating "huerfano unattested in both." The checker's own search sides with the second file: "huerfano" appears in neither De Castro headwords nor the NT plain text. Yet unbracketed "huerfano" stands in some 17 verses (2:83, 2:177, 2:215, 2:220, 4:2, 4:3, 4:6, 4:8, 4:10, 4:36, 4:127, 6:152, 8:41, 17:34, 18:82, 59:7, 76:8, 89:17, 90:15 — 20 occurrences in the file). One treatment must be chosen and disclosed.
2. **Sacred Mosque (blocking inconsistency).** flags-001-002 records that "mezquita" is not attested in either source and adopts the paraphrase "Sagrado Lugar de Oracion"; flags-019-022 then uses unbracketed "Sagrado Mezquita" (22:25), and "mezquita" occurs 14 times in the book. The two chunks applied opposite rules to the same term.
3. **Unbracketed Spanish-derived choices.** flags-019-022 discloses a run of Spanish-derived forms used *without* brackets and *without* attestation in either named source: datiles (19:25), codorniz (20:80), becerro (20:88), pozo (22:45), mosca (22:73), monasterio/sinagoga (22:40), peregrinacion (22:27), and "semilla de mostaza" at 21:47 — while the same word is bracketed at 31:16 ("grano de [mostaza]"). These may be defensible Chavacano usage, but as the text stands they breach the build's own stated discipline ("no attested form → brackets") and are applied inconsistently. They need either bracketing, a disclosed front-matter exception, or replacement.
4. **Sajda-note record does not match the book.** Different flags files describe the prostration notes as "kept unchanged" in English (flags-092-114, on 96:19), "preserved unchanged" (flags-015-018, on 16:50/17:109), rendered "*[inclinacion — recomendado]*" (flags-010-014, on 13:15), and rendered "*[postracion — recomendado]*" (flags-026-028, on 27:26). The built text is in fact uniform — all 15 as postracion notes (§1) — so the book is right and the flags record is unreliable on this point. The record should be corrected so a later reader is not misled.

Nothing in the flags discloses an invented word presented as attested, a missing surah, or a known mistranslation left standing. The front matter of the built text is honest about its sources, including that the control is a New Testament only.

## Required corrections (by verse reference)

- **C1 — 12:41:** remove the false gap [crucifica]; use the attested form (De Castro crucifica/crucificao; NT control passim). Correct the flags claim.
- **C2 — 6:146:** remove the false gap [tripa]; De Castro attests tripa = intestine. Correct the flags claim. ([garra] in the same verse stands.)
- **C3 — orphan, throughout:** unify the treatment of "huerfano" / [orphan] (unbracketed at 2:83, 2:177, 2:215, 2:220, 4:2, 4:3, 4:6, 4:8, 4:10, 4:36, 4:127, 6:152, 8:41, 17:34, 18:82, 59:7, 76:8, 89:17, 90:15; bracketed at 93:6, 93:9, 107:2) and disclose the chosen basis, since the form is unattested in both named sources.
- **C4 — Sacred Mosque, throughout:** unify "Sagrado Lugar de Oracion" (Surah 2 and elsewhere) vs "Sagrado Mezquita" (22:25 and elsewhere; 14 occurrences of mezquita). One rule, disclosed.
- **C5 — 41:38:** delete the duplicated Surah 41 summary line inserted between the verse and its Arabic line.
- **C6 — 2:282:** delete the two spurious "Si" prefixes in the closing sentences ("Si Dios ta enseña con ustedes. Si Dios sabe todo." → statements, as in the master).
- **C7 — 3:20:** repair "entonces guia o sila" → the guided predicate (e.g. "entonces guiao sila").
- **C8 — mostaza and the flags-019-022 Spanish-derived set:** reconcile 21:47 (unbracketed "semilla de mostaza") with 31:16 (bracketed [mostaza]), and bring datiles (19:25), codorniz (20:80), becerro (20:88), pozo (22:45), mosca (22:73), monasterio/sinagoga (22:40) and peregrinacion (22:27) under one disclosed rule.

## Headline numbers

- Verses: 6,236 / 6,236, sequence and per-surah counts exact; Arabic lines 6,462 / 6,462 identical in sequence.
- Basmalah: 114 exact uniform occurrences; absent from Surah 9, as in the master. Sajda notes: 15 / 15.
- Language sample (40 verses): (a) real Chavacano 24, (b) frame with coinage/Spanish-substituted lexis 16, (c) not Chavacano 0.
- Fidelity sample (12 verses): 2 errors — 2:282 (minor) and 3:20.
- Attestation: 92.93% by the checker's stated method (92.81% with gap tokens in) — the desk's 92.78% confirmed.
- Held-open gaps: 227 in verse text (136 distinct); 2 false gaps (12:41, 6:146); the rest verified genuinely unattested or honestly disclosed calques/phrases.
