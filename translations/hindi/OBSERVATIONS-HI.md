# OBSERVATIONS-HI — working notes for the Hindi manuscript

*Manuscript: `ayah-companion-manuscript-HI.md` — REVIEW DRAFT (समीक्षा मसौदा), not publication. Hindi (Devanagari) rendering verse-for-verse from Robert Tilford's corrected English master; the Arabic is spliced from the master character-for-character. Built in 12 parallel translator slices from a single brief (`work/BRIEF-HI.md`); structure independently verified on the assembled file (below). Nothing here corrects meaning silently: every intended-reading is listed. Full translator flag log: `work/flags-hi.txt` (197 `#FLAG` lines across the slices).*

## 1. Source-English errors rendered by intended reading (never propagated)

Translator flags total **197** lines (187 unique verse references) — a heavier flag rate than the German build, mostly terminology and name-form notes from the Hindi translators rather than source errors. The canonical intended-reading list carried over from the Italian/Urdu/Portuguese/French/German ruling list was applied wherever the refs occur; no English typo was copied into Hindi.

**Typos / wrong words:**
- 5:65 — "Scriputure" → किताब (Scripture)
- 39:67 — "in His righ" → दाहिने हाथ (right hand)
- 23:110 — "you made then a target" → "them" as intended
- 47:36 — "life of this word" → इस संसार का जीवन (world)
- 11:42 — "On my son!" → vocative "ओ मेरे बेटे!"
- "Median" → **मदयन** (Midian) at 22:44 and also 7:85, 9:70, 11:84, 11:95, 20:40, 28:22, 28:23, 28:45, 29:36 (10 instances)
- 3:7 — source "descent" rendered as dissent/discord (मतभेद); judgment call, flagged for the reviewer.

**Broken grammar rendered by sense:** 4:77, 5:64, 5:80, 7:167, 13:19, 33:15, 38:11, 41:29, 41:52, 57:6; also 43:53 ("or they angels came") by sense.

**Unclosed or unmatched quotation marks closed where the sense closes:** 2:127, 2:215, 2:222, 3:42, 3:45, 3:55, 6:78, 6:80, 6:162, 7:16, 7:18, 7:67, 10:49, 60:4 (closed at 60:5); cross-verse quote spans preserved and closed where the sense ends (e.g. 7:16–19, 11:54–57).

**Minor:** 7:173, 7:189 capitalization oddities; 56:96 missing final period (supplied); 29:14 "and He stayed" rendered as Noah (नूह) remaining among his people.

**Garbled source token:** 17:105 and 48:8 — source lines carry "Bearer <redacted> good news"; rendered by intended sense (खुशखबरी देने वाला) and flagged. Same-family extra finds: 33:45 and 35:24 carry the same "bearer" garble and were rendered by intended sense; the 35:INTRO line carries the same garble family and was rendered by sense. The master file itself was not edited.

**Extra in-slice catches (not in the canonical list, rendered by sense and flagged):** 2:47 broken grammar ("and I that favored you"); 2:217 unclosed quotation closed at verse end; 3:159 broken wording ("It is by of grace from God"); 57:6 broken grammar ("what the hearts contains"); 23:33 unclosed dignitaries' speech closed where the sense closes; stray source quote marks dropped at 13:28 and 14:5; punctuation oddity ";," at 13:11 rendered by sense.

## 2. Terminology decisions for the native reviewer

- **God = अल्लाह throughout; Latin "Allah" count = 0** (verified in the assembled file and in every slice text; Devanagari only). Hindu deity names (ईश्वर/भगवान/परमेश्वर) were not substituted for the one God, per the brief. The generic "god/deity" (a false god) is देवता (e.g. 2:255 "कोई देवता नहीं" beside अल्लाह) — reviewer should confirm this contrast reads naturally.
- **"The Reminder" = याद-दिहानी, fixed by the brief and held across all slices** (29:45, 29:51, 37:3, 41:41, 43:5, 20:124, 21:105 …) — the Urdu two-renderings weak spot did not recur. Lowercase "remembrance" stays याद, kept distinct.
- **Divine epithets:** the brief fixed the Beneficent = अत्यंत दयालु and the Merciful = असीम कृपावान (basmalah: "अल्लाह के नाम से, जो अत्यंत दयालु, असीम कृपावान है।"), and the mapping was applied consistently wherever the pair occurs. A stand-alone "the Compassionate" was mapped to अत्यंत दयालु in the late slices (e.g. 78:37, 59–77 passim) and "Clement" to plain दयालु (59:10) — a native reviewer should confirm one Rahman/Rahim convention and normalize any residue. Other epithets (Living, Eternal, Mighty, Wise, Sovereign, Holy…) were rendered plainly (ज़िंदा, हमेशा रहने वाला, शक्तिशाली, बुद्धिमान …) and are a natural review target.
- **Address convention held:** God and singular addressees as तुम throughout; plural audience तुम सब / तुम लोग; आप does not occur (verified 0 in the 7–10 slice and uniform across reports). Divine "We" → हम, "He" → वह.
- **zakat/charity distinction held as briefed:** obligatory charity (zakat) → ज़कात; generic charity/alms → दान (9:5, 9:60, 98:5) — **no percentage anywhere** (verified 0 "%" signs in body and file), per the Quran-alone rule. 8:41's "the fifth" is spelled out पाँचवाँ हिस्सा (the English says "fifth"; no percentage sign, reviewer may check the fraction wording).
- **Fixed glossary otherwise held:** रब (Lord), रसूल / नबी, किताब / क़ुरआन, आसमान / ज़मीन, आख़िरत, जन्नत (worldly gardens बाग़ kept distinct), आग / जहन्नुम, नमाज़ अदा करना, रोज़ा, हज, शैतान, फ़रिश्ते, जिन्न, निशानियाँ (62:2 "revelations" as आयतें is a flagged exception), क़यामत का दिन / क़यामत, ज़ालिम, मुनाफ़िक़, बंदा (servant of God), नेक / नेकी (righteous), किताब वाले (People of the Book), तौरात / इंजील, पवित्र आत्मा (Holy Spirit — 16:102 and elsewhere; reviewer may prefer रूहुल-क़ुदुस).
- **People-name forms mostly follow the brief's fixed list** (इब्राहीम, मूसा, ईसा, मरयम, नूह, इमरान, मुहम्मद, यूसुफ़, याक़ूब, इसहाक़, इस्माईल, हारून, दाऊद, सुलैमान, लूत, हूद, सालिह, शुऐब, फ़िरऔन, क़ारून, हामान, जालूत, तालूत, लुक़मान, समूद, मदयन, सबा). Live splits needing one ruling:
  - **Enoch**: इनोक at 19:56 and 21:85 (following the English spellings) vs the Hindi-tradition इदरीस — flagged in-file both times.
  - **Ezekiel**: एज़ेकिएल at 21:85 (following the English) vs ज़ुल-किफ़्ल at 38:48 (traditional identification, flagged by that translator here rather than in-file).
  - **Elijah/Elias**: अलयसा at 6:86 vs इल्यास at 6:85, per Hindi tradition — flagged for confirmation.
  - सामरी (the Samarian, 20:85; alternative सामिरी); "Salomon" (2:102) normalized to सुलैमान; Yathrib यस्रिब, Zaid ज़ैद, Baal बाल, Gog/Magog याजूज-माजूज, Zul-Qarnain ज़ुल-क़रनैन, Ahmad अहमद (61:6), Ezra उज़ैर (9:30) — standard transliterations, flagged where uncertain.
  - The unnamed servant of 18:65 was kept **unnamed** as in the English (no "Khidr" added); "Fellow of the Fish" (68:48) kept as मछली वाला without inserting यूनुस's name.

## 3. Literal renderings — known weak spots for a native reader

- **81:4** — "When the relationships are suspended" rendered literally (संबंध स्थगित); the traditional she-camels sense was deliberately NOT substituted (translate-the-English rule). Flagged.
- **83:9, 83:20** — "A numerical book" → अंकित किताब; सिज्जीन / इल्लिय्यीन transliterated with the English source's own spelling variance (Elliyyeen/Elliyyoon) noted.
- **Kept-literal items for review:** 31:22 "the trustworthy handle" → हैंडल (flagged idiom); 18:86 the sun "setting in a murky spring" → कीचड़ वाले झरने में डूबता हुआ; 21:30 heavens/earth "one mass… tore them apart" → एक पिंड… अलग कर दिया; 11:40 the source's "the volcano erupted" (for the oven/tannūr image) translated as given (ज्वालामुखी फटा); 68:42 "the Shin" → पिंडली; 68:16 muzzle → थूथन; 70:16 scalps; 70:40 "Easts/Wests" plurals; 77:1–6 unnamed oath fragments with no referent added; 93:3 "forget" sense kept where the INTRO says "displeased" (flagged mismatch); 81:15 "galaxies" → आकाशगंगाएँ.
- **Muqatta'at (disconnected letters)** transliterated from the English names without added meaning (19:1 काफ़, हा, या, ऐन, साद; 20:1 त्वा, हा; 26:1 ता, सीन, मीम) — flagged.
- Register variance across the 12 translators is expected, and Hindi **gender/case agreement** was required verse-internally by the brief but needs a native pass across slice boundaries. Sensitive passages (4:34, 24:2–9, 24:31–33, 33:50–53, 65 legal rulings) were translated plainly and literally — a Hindi reviewer should check tone, legal naturalness, and agreement.

## 4. Structure and discipline

- Format identical to the German/French/Portuguese/Italian builds: Hindi title block (हिंदी पांडुलिपि — समीक्षा मसौदा (अंतिम संस्करण नहीं); not-a-first line acknowledging the existing Hindi translation tradition), अनुक्रमणिका (contents, established Devanagari surah names), भाग I · अनुवाद, 114 sections with the Arabic surah name untouched from the master, an italic intro line, basmalah Arabic + italic fixed-formula line "अल्लाह के नाम से, जो अत्यंत दयालु, असीम कृपावान है।" in the 112 surahs that carry the frame (surah 1 counts it as 1:1; surah 9 has none), the translator's note inside 5:6 with its continuation after it ("कुछ पाठ पोंछने को पैरों तक बढ़ाते हैं; यहाँ छपा पाठ धोने को कहता है।"), and 15 prostration markers (11 *[सजदा — अनुशंसित]*, 4 *[सजदा — अनिवार्य]*) after the verse's Arabic line.
- Quran-alone discipline: no hadith/tafsir material imported, no traditional specifics added, no percentage for zakat.
- The audit is **structural** (counts, sequences, the Arabic character-for-character, markers, residue scan), as for the other drafts of this project: it is not a verse-by-verse philological proof. Final language quality requires a native Hindi reviewer — in particular for the name splits in §2, the literal renderings in §3, and gender-agreement/register consistency across slices.

## 5. Independent verification result (on the assembled file)

- Extraction upstream of translation was itself re-verified against the master before any translator ran: 114 surahs, 6,236 verses in the master's exact reference sequence, 6,462 Arabic runs (6,236 verse lines + 112 basmalah frames + 114 surah-name lines), 15 markers (11 recommended + 4 obligatory), 1 translator note (5:6), per-surah continuity true.
- (a) 114 surah headers, in order 1–114 ✓
- (b) 6,236 verse blocks; per-surah counts equal to the English master for all 114 surahs ✓
- (c) references continuous 1..k in every surah ✓
- (d) Arabic text: 6,462 ordered runs, byte-identical to the master Part I (114 surah names, 112 basmalah frames, 6,236 verse lines) ✓
- (e) 0 [MISSING] markers ✓
- (f) 15 prostrations at the exact references (7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 38:24 recommended; 32:15, 41:38, 53:62, 96:19 obligatory); 5:6 translator's note and continuation present ✓
- (g) 0 verse lines with English residue on the distinctly-English function-word scan (assembled file and slice texts); Latin "Allah" = 0 in body, slices, and file; "%" signs = 0 ✓

*File: `ayah-companion-manuscript-HI.md` — 3,390,602 bytes, SHA-256 0af12b9096ba381d0b2579b2d61a8f679121345aaff0f91669484c2b920923b9. Work files: `work/en/` (extracted English), `work/hi/` (Hindi slices), `work/meta.json` (Arabic/markers), `work/BRIEF-HI.md` (brief), `work/titles-hi.json` (Hindi surah titles), `work/flags-hi.txt` (197 translator flags), `work/extraction-report.json`, `work/slices.json`, `work/assemble.py`, `work/verify.py`, `work/verification-hi.json` (independent verification). Status: REVIEW DRAFT — structural verification only; native Hindi review required before any use beyond review.*
