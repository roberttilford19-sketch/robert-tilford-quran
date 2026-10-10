# Observations — Indonesian DRAFT (Ayah Companion)

**Status: REVIEW DRAFT — structural verification only.** Native Indonesian review required before any community-facing use. This is NOT claimed as the first Indonesian Quran translation; the existing Indonesian tradition, including the official Kementerian Agama translations, is acknowledged on the title page.

## What was independently verified (separate pass on the assembled file)
- 114 surah headers, in order 1–114.
- 6,236 verse blocks; per-surah counts equal the English master for all 114 surahs; refs continuous 1..k in every surah.
- Arabic runs: 6,462 (6,236 verse lines + 112 basmalah frames + 114 surah-name lines), byte-identical to the master sequence.
- 0 `[MISSING]`; 0 U+FFFD replacement characters; 0 "%" signs (zakat carries no percentage anywhere).
- 15 prostration markers at the exact refs — recommended *[sujud — dianjurkan]*: 7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 38:24, 84:21; obligatory *[sujud — wajib]*: 32:15, 41:38, 53:62, 96:19.
- 5:6 translator's note present ("Sebagian bacaan melanjutkan usapan hingga ke kaki; bacaan yang dicetak di sini mengatakan cuci.").
- 0 English-residue verse lines (function-word scan of the assembled file and of all 114 slice files returned zero hits).
- "Allah" used throughout (2,841 occurrences); address to God is capitalized "Engkau" (233 occurrences).
- Extraction was re-verified against the master *before* translation (6,236 refs in exact master sequence; counts and continuity confirmed in `work/extraction-report.json`).

## Source-text flags
Translator `#FLAG` lines: **176** in `work/flags-id.txt` — all canonical intended-reading rulings applied, including 5:65 "Scriputure"→Kitab Suci, 39:67 "His righ"→right hand, 23:110 "made then"→them, 47:36 "this word"→this world, 11:42 vocative, "Median"→Madyan at all 10 refs, 3:7 "descent"→dissent/discord (flagged judgment call), the broken-grammar and unclosed-quote lists, 56:96 period supplied, 29:14 Noah subject, and the garbled "Bearer" tokens at 17:105/48:8 rendered "pembawa kabar gembira". Same-family extra finds were flagged in-slice (e.g. 13:11 stray punctuation, 38:11 "with be defeated", 69:32 broken chain-length grammar, 2:102 "Salomon/Solomon" unified as Sulaiman).

## Weak spots for a native Indonesian reviewer
- **"the Reminder" is not fully uniform:** the brief fixed one rendering ("Peringatan") everywhere; slices reported consistent use, but a reviewer should confirm no variant (e.g. "Pesan" at 36:11, flagged) crept in against the Quran-alone definition discipline.
- **Disbeliever terminology:** every slice independently chose "orang-orang yang tidak beriman" (never "orang-orang kafir") — consistent across the whole book, but a reviewer should confirm this is the intended register for all contexts, including set labels like 109:1.
- **Plural audience:** "kalian" won everywhere the brief allowed a choice ("kamu sekalian" unused); confirm uniformly, and confirm the "Engkau" (God) vs "kamu" (singular human) split reads naturally in prayer passages.
- **Name forms resting on translator judgment, not the brief:** Qarun (for "Quaroon"), Haman, Zulkifli (for Ezekiel at 21:85/38:48), Ilyasa vs Ilyas distinction preserved at 6:85/6:86 mirroring the source's two names, Idris/Ismail, Zulkarnain, Ya'juj/Ma'juj, Al-Masih, Firaun; idol names at 71:23 (Wadd, Souwa, Yaghoos, Yaooq, Nassr) kept in English spelling rather than inventing Indonesian forms. One ruling from a reviewer would settle all of these.
- **Literal renderings kept deliberately and flagged:** 81:4 ("relationships are suspended"), 83:9 and 83:20 ("A numerical book"), 86:13 ("a Decisive Word"), 56:52 ("Pohon Kepahitan" — Zaqqum not named because the English does not name it), 55:31 ("O prominent two"), 31:22 rendered "pegangan yang paling dapat dipercaya" (the firm handhold).
- **Zakat/sedekah boundary:** 98:5 "give alms" rendered "menunaikan zakat" and 73:20 "regular charity" rendered "sedekah wajib" — both flagged; the zakat-vs-generic-charity line deserves one reviewer ruling. No percentage appears anywhere, per the Quran-alone rule.
- **Muqatta'at and proper-name spellings** (Sijjin/Illiyyin, Saqar, Lauh yang Terpelihara, Malam Ketetapan) transliterated without added meaning, as in the English.
- **Sensitive legal/household passages** (e.g. 58:2–3 rendered descriptively) should get a tone and naturalness pass, as in every language of this project.
- Ordinary register variance across the 12 slice boundaries remains, as in the German/French/Hindi drafts.
