# Independent Checker Report — Bislama Quran Lane

**Date:** 2026-11-23 · **Checker:** independent check pass (checker did not build this text)
**Manuscript:** `~/workspace/ayah-bislama/ayah-companion-manuscript-BIS.md` (6,236 verses parsed, sequential, no gaps found)
**Master:** `~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md` (6,236 verses parsed)
**Brief:** `~/workspace/ayah-bislama/WORKER-BRIEF.md` · **Flags:** `work/flags_01.md` … `flags_17.md`
**Lexicon sources:** `sources/dict-bi-en.txt` (Government of Vanuatu Bislama Spelling Dictionary, Moon et al. 2007) + `sources/bislama.txt`; control register: Baebol long Bislama.

## VERDICT: PASS WITH CORRECTIONS

The text is genuinely Bislama in frame and grammar throughout the sample — this is not English in Bislama spelling. It does not pass clean, because every one of the six flagged defects stands in the text, two of them are wider than the flags admitted, and the spot check found two further meaning shifts. All required corrections are listed in §5 with exact current wording and exact replacements using only attested words and the brief's locked terms. No correction requires re-translation of a verse.

---

## 1. Language sample — 40 verses, every ~150th verse

Method: verses taken at positions 1, 151, 301, … in file order (40 of the 42 systematic points), graded (a) real Bislama, (b) Bislama frame with coinage/uncertain lexis, (c) effectively not Bislama.

**Counts: (a) 28 · (b) 12 · (c) 0**

Graded (a): 1:1, 2:144, 3:158, 4:108, 6:112, 7:97, 8:41, 9:116, 11:28, 12:55, 16:50, 17:72, 21:68, 23:28, 26:69*, 26:219, 30:42, 33:68, 36:46, 37:113, 38:81, 40:68, 45:28, 50:21, 53:17, 67:10, 78:29, 83:3. (*26:69 is clean Bislama but carries the Ibrahim name-form defect, §3v.)
These verses use the grammar naturally — predicate marker *i*, *blong/long/wetem*, *bambae*, *oli*, *nao*, short clauses — e.g. 12:55: "Hem i talem se, 'Yu putum mi mi lukaotem ol haos blong putum kakae blong graon ia; mi mi tru mo mi gat save.'" That is real Bislama, not a calque.

Graded (b) — Bislama frame, coinage or uncertain lexis (12): 3:8 (*gaedem*), 5:82 (*lav*), 14:51 (*jajmen*, *peim*), 19:1 (transliterated muqatta'at letters — by design, but not ordinary lexis), 20:53 (*usum*, *plant*), 24:60 (*aotsaed*; one very long sentence against the brief's short-sentence standard), 28:49 (*gaedens*, *lidim*), 43:26 (Ebraham name-form split), 55:50 (*spring*), 57:26 (Ebraham; *sin*), 70:26 (*jajmen*), 74:56 (coined divine epithets).

Worst (b) examples, verbatim (there are no (c) examples to cite):

- **74:56** — "Be bambae oli no tingbaot, be spos God i wantem nomo. Hem i Ples we Stret Fasin i Kam Long Hem, mo Ples we Fogiv i Kam Long Hem." (Master: "He is the Source of Righteousness, and the Source of Forgiveness." The capitalised paraphrase-epithets are coined and read as place-names.)
- **55:50** — "Long tufala i gat tu spring wota we i stap ron." (English *spring* carried over untranslated.)
- **28:49** — "…we i lidim man i go long gaedens moa gud winim tufala…" (*gaedens* is a coinage for "guidance"; the dictionary-attested noun is not used anywhere in the book — *gaedens* occurs 33 times.)

## 2. Attestation

Method: lexicon built from the first-column headwords of `dict-bi-en.txt` (6,636 unique lowercased headwords; `bislama.txt` is the same list and adds nothing). Verse text only (the `**N:M**` Bislama lines, 196,543 tokens) was tokenised on letters; a token counts as attested if its lowercase form is a headword.

- **Strict dictionary attestation: 86.71%** of verse-text tokens.
- The supplied dictionary text omits, as headwords, core Bislama function words that the Baebol control uses constantly (*we* relative, *se*, *ya*, *o*, *spos*, *sore*, *moa*). Adding only those declared function words plus the brief's locked loans (*zakat*, *jinn* — neither is a dictionary headword): **92.48%**.
- The largest remaining "unattested" types are not coinages but core words missing from the supplied extract (*man* 4,134 tokens, *go* 987, *rod* 373, *woman* 258, *god* 204, *trutok* 162, *glad* 142) — an extract limitation, stated here so the 86.71% figure is not read as a language failure.
- The genuine coinage/loan residue is small and identifiable: *gaedens* (33), *jajmen* (63 across sample+counts), *spendem* (40), *wonem* (68), *gaedem* (59), *obei/obeim* (130), *bilifim* (39), *promesem* (44), *sendemdaon* (33), *kingdom* (27), *spring* (23), *lav*, *lid/lidim*. Most are regular transitive *-em* formations on attested stems, which is productive Bislama morphology; *gaedens*, *jajmen*, *kingdom*, *spring* are the true outliers.

## 3. Known flagged defects — verification

(i) **4:34 "smol" — STANDS.** Bislama: "…nao yufala i kilim olgeta smol." Master: "then strike them." Arabic وَاضْرِبُوهُنَّ carries no qualifier. *smol* ("lightly") is an added softening, exactly as flags_02.md:89 honestly records. Correction 1.

(ii) **4:76 "Devel" — STANDS, and is wider than flagged.** The flag (flags_02.md:64) admits one use; the text has capitalised *Devel* three times: **4:76 ×2** ("ol fren blong Devel. Tru, plan blong Devel i wik") and **4:83 ×1** ("bambae yufala i folem Devel"), both for Satan singular, where the brief locks **Setan** (used 68 times elsewhere). A third capitalised use, 23:70 ("Devel i stap long hem?"), renders the master's "He is possessed" (Arabic *jinnah*) and is a generic use — it may stand. Lowercase *devel* for generic devils (shayāṭīn) occurs in 26 verses; *devel* is dictionary-attested, so that is a consistency question for a house ruling, not a locked-term breach. Correction 2 covers 4:76 and 4:83 only.

(iii) **4:162 zakat paraphrased — STANDS.** Bislama: "mo ol man we oli givim samting long ol puaman" for the master's "the givers of charity" (Arabic مُؤْتِي الزَّكَاةَ). The brief locks the bare term **zakat**, used correctly 27 times elsewhere (2:43, 2:110, 4:77, 5:12, 9:5 …). flags_02.md:131 records the inconsistency honestly. Correction 3.

(iv) **Christ/Messiah split — STANDS.** *Kraes* occurs only at **5:17** (2 occurrences: "God i Kraes, pikinini blong Meri" / "spolem Kraes pikinini blong Meri"); *Mesaea* occurs at 3:45, 4:157, 4:171, 4:172, 5:72, 5:75, 9:30, 9:31. Both render the same Arabic al-Masīḥ; the master's English alternates "the Christ"/"the Messiah" and the workers followed it inconsistently (flags_03.md:19). Correction 4 settles on *Mesaea* (one verse to change, not eight).

(v) **Abraham split — STANDS.** *Ebraham*: 44 occurrences in 38 verses, surahs 2, 3, 4, 6, 9, 11, 12, 42, 43, 57, 60. *Ibrahim*: 26 occurrences in 26 verses — 14:35, 15:51, 16:120, 16:123, 19:41, 19:46, 19:47, 19:58, 21:51, 21:60, 21:62, 21:69, 22:26, 22:43, 22:78, 26:69, 29:16, 29:31, 33:7, 37:83, 37:104, 37:109, 38:45, 51:24, 53:37, 87:19. *Abraham* (the Baebol spelling) occurs 0 times — neither worker form is the Baebol form, a point Robert may wish to rule on; the correction below settles on the majority form *Ebraham* for internal consistency. Correction 5.

(vi) **Divine "We" as "Mifala" — CONFIRMED as described; house-level choice, not an error.** Capitalised *Mifala* for the divine We occurs in 1,157 verses, sentence-initial and mid-sentence, throughout all ranges. Bislama forces a choice the Arabic and English do not: *mifala* is exclusive (excludes the person addressed), *yumi* is inclusive. Rendering God's "We" as *Mifala* excludes the Prophet and the reader from the divine party, which is theologically the safer reading and is applied consistently; the same form correctly serves human exclusive "we" (e.g. 1:5, worshippers addressing God). This checker records it as a deliberate house choice requiring Robert's ruling on the record, not a correction. One orthographic note: mid-sentence divine *mifala* is lowercased (e.g. 4:162 "bambae mifala i givim wan bigfala pei") while sentence-initial uses are capitalised — normal sentence case, no action needed.

## 4. Spot fidelity — 10 verses at random (seed 20261123)

Compared against the master English and the Arabic line carried under each verse.

- **5:59** — Faithful. "Yufala i agens long mifala nomo from mifala i bilif long God…" matches the master clause for clause.
- **9:76** — **Meaning shift.** Master's "of His bounty" (Arabic مِنْ فَضْلِهِ) is rendered "aot long gladhat blong Hem" — *gladhat* ("glad heart") turns bounty/grace into an emotion. The same rendering recurs at 8:29, 9:28, 9:59, 9:74, 9:75. Correction 6.
- **10:57** — Faithful in substance; "guidance" rendered *lid* (an English loan spelling) and "mercy" as *sore* (the locked Baebol word). Acceptable; *lid* noted under §2 residue.
- **26:160** — Faithful. "Ol man blong Lot oli no bilifim ol man blong karem tok."
- **38:76** — Faithful, exact: "Yu mekem mi long faea, mo Yu mekem hem long klei."
- **44:5** — Follows the master ("We have been sending messages" → "Mifala i bin sendem ol tok"); the Arabic (إِنَّا كُنَّا مُرْسِلِينَ) speaks of sending messengers, so the narrowing to "messages" is inherited from the master, not introduced by the Bislama. No Bislama-side correction.
- **48:9** — Faithful to the master, including its ambiguity ("yufala i helpem Hem" — support Him).
- **51:42** — Faithful; "olsem ol bun we i roten" for "like decayed ruins" (Arabic كَالرَّمِيمِ, crumbled remains) is a fair plain rendering.
- **69:43** — **Minor loss.** "Lord of the Worlds" (Arabic رَبِّ الْعَالَمِينَ) rendered "Masta blong evri man long wol" — *worlds* narrowed to *every man in the world*. The same phrase occurs at 3:33, 14:8, 68:52, 70:14, 81:27, while 1:2 uses the correct "Masta blong olgeta wol". Correction 7.
- **104:5** — Faithful; al-Ḥuṭamah rendered descriptively as "Ples we i Krase Evri Samting", consistent with the brief's descriptive-phrase rule.

Net: 8 of 10 faithful; 2 with a shift or loss (9:76, 69:43), both correctable by phrase substitution. No additions found in the spot check beyond the already-flagged 4:34.

## 5. Required corrections (exact)

All replacements use dictionary-attested words or the brief's locked terms only.

1. **4:34** — Current: "nao yufala i kilim olgeta smol." → Replace with: "nao yufala i kilim olgeta." (Deletes the added softener *smol*, absent from master and Arabic.)
2. **4:76** — Current: "Olsem yufala i faet agens long ol fren blong Devel. Tru, plan blong Devel i wik." → Replace with: "Olsem yufala i faet agens long ol fren blong Setan. Tru, plan blong Setan i wik."
   **4:83** — Current: "bambae yufala i folem Devel, be smol namba nomo i no folem." → Replace with: "bambae yufala i folem Setan, be smol namba nomo i no folem."
3. **4:162** — Current: "mo ol man we oli givim samting long ol puaman" → Replace with: "mo ol man we oli givim zakat" (locked bare term).
4. **5:17** — Current: "God i Kraes, pikinini blong Meri" → "God i Mesaea, pikinini blong Meri"; and "spolem Kraes pikinini blong Meri" → "spolem Mesaea, pikinini blong Meri". (*Mesaea* then stands at every al-Masīḥ verse.)
5. **Abraham, 26 verses** (14:35, 15:51, 16:120, 16:123, 19:41, 19:46, 19:47, 19:58, 21:51, 21:60, 21:62, 21:69, 22:26, 22:43, 22:78, 26:69, 29:16, 29:31, 33:7, 37:83, 37:104, 37:109, 38:45, 51:24, 53:37, 87:19) — Current: "Ibrahim" → Replace with: "Ebraham" in every occurrence, so one form stands book-wide. (If Robert prefers the Baebol spelling *Abraham*, that is a one-line ruling and a mechanical change the other way; what cannot stand is the split.)
6. **9:76** (and the same phrase at 8:29, 9:28, 9:59, 9:74, 9:75) — Current: "aot long gladhat blong Hem" → Replace with: "aot long ol gud samting we Hem i givim" — at 9:76 the full clause becomes: "Be taem Hem i givim long olgeta aot long ol gud samting we Hem i givim, oli kam stingy wetem hem, mo oli tanem i go aot, oli no laekem." (At 8:29, "God i gat bigfala gladhat blong givim" → "God i gat plante gud samting blong givim.")
7. **69:43** (and 3:33, 14:8, 68:52, 70:14, 81:27) — Current: "Masta blong evri man long wol" → Replace with: "Masta blong olgeta wol" (the book's own 1:2 rendering). At 69:43 the verse becomes: "Hem i wan tok we God i sendem i kamdaon, Masta blong olgeta wol."

**Not corrections — recorded for Robert's ruling:** (a) divine *Mifala* (§3vi) — house choice, consistently applied; (b) lowercase generic *devel* for shayāṭīn in 26 verses — dictionary-attested, but a one-form ruling (*Setan* / *ol man blong Setan*) would tighten consistency; (c) the §2 coinage residue (*gaedens*, *jajmen*, *kingdom*, *spring*) — intelligible in context, flagged here rather than corrected, because no attested single-word replacement exists and the brief's own rule permits descriptive renderings; a speaker review, when one is offered, is the right gate for these.

**Counts reconciled:** 6,236 Bislama verses = 6,236 master verses; sample 40 = 28 (a) + 12 (b) + 0 (c); attestation 86.71% strict / 92.48% with declared function words and locked loans, on 196,543 verse-text tokens.
