# OBSERVATIONS-ALS — working notes for the Alemannic manuscript

*Manuscript: `ayah-companion-manuscript-ALS.md` — REVISION DRAFT / ÜBERARBEITUNGS-ENTWURF, not a final edition and not native-reviewed. Alemannic rendering verse-for-verse from Robert Tilford's corrected English master; Arabic spliced from `work/meta.json` verse-for-verse at assembly. PDF: `Ayah_Companion_Tilford_Alemannic_Manuscript.pdf` (497 pages). Nothing was published, uploaded, emailed, archived, or posted.*

## 1. Dialect choice and house rules

- Target is a readable pan-Alemannic written compromise (Alemannisch, ISO gsw umbrella): not Swiss-only, not Swabian-only, not Alsatian-only. Alemannic has no standardized orthography, so this compromise is an explicit draft device, stated as such in the front matter; regional speakers will not all hear it as their home dialect.
- Recurring forms are `i/du/er-sie-es/mir/ir/sie`, `de/d/s` articles, `isch/het/cha`, `wil/wenn`, `vo/zue/bi/mit/für`, with light consistent spelling. The draft aims at Robert's stated target: plain, clear, humble everyday words and short sentences where the English permits, with a dignified register.
- `Allah` is kept as `Allah` (2,694 occurrences in slice verse text; 2,818 Latin-script `Allah` in the assembled file including front matter, contents/intros, and repeated Basmalah lines). `Lord` is generally `Herr` (1,033 occurrences); owner/protector/master senses are flagged in the per-range flag files where the choice matters.
- Quran-alone discipline held: no hadith/tafsir material imported, no traditional specifics added, and zakat/obligatory charity receives no percentage. Verified: 0 `%` in slices, assembled verse first-lines, and the whole manuscript.
- Surah titles are in `work/titles-als.json`, newly made in the pan-Alemannic compromise from the English title list in `work/meta.json`. The front matter makes no first-ever claim: it states only that no complete Alemannic Quran translation was found after research, which is not proof of being first. It also states the draft is held locally, asserts no ownership overreach, and follows Robert Tilford's free-giving stance if he later chooses to release it.

## 2. Production note

- The Alemannic slices were translated from `work/en/surah_001.txt` ... `surah_114.txt` only, in 13 surah ranges. Extraction had already verified 114 surahs / 6,236 verses in the corrected English master's exact reference sequence, 6,462 Arabic runs, 112 basmalah frames, and 15 markers.
- Slice audit (independent recount at assembly): 114/114 files, 114 INTRO lines, 6,236 verse lines, refs identical to English in order for every surah, no tab-format failures, no empty verse texts, ` ¶ ` parity with English (1 occurrence — the 5:6 split), 0 `[MISSING]`.
- Small self-fixes were made inside ranges before delivery and are documented in that range's flag file (e.g., surah 25 verses 63–65 re-split into separate lines in range 6; a typo at 79:18 fixed in range 12; "ergriffe" at 6:44 fixed in range 2).

## 3. Terminology and consistency flags for a native Alemannic reviewer

Full per-range flags are preserved in `work/flags/flags-r01.txt` ... `flags-r13.txt`, concatenated as `work/flags-als.txt` (500 lines). The main consistency decisions a reviewer should make once, project-wide, are:

- **Quran/Koran split**: verse text has `Quran` 34x and `Koran` 34x — an exactly even split. Ranges differ internally (e.g., range 9 uses `Koran` consistently, ranges 1/7/11 use `Quran`). Choose one house spelling.
- **Moses split**: `Mose` 136x and `Moses` 23x. Other name forms vary by slice (Quraisch, Abee Lahab, Thamud/Thamood, Dschinn spellings). A single name policy is needed.
- **Generic "god" versus Allah**: `Gott` occurs 125x, mostly in fixed formulas ("kei Gott usser Allah") and a few deliberate retentions (43:84 "Gott im Himmel … Gott uf de Erd"; 37:4 "Eu Gott" flagged in range 8). This is a proper-name/common-noun split, not English leakage (standalone English `God` = 0), but the convention should be confirmed by a native reviewer.
- **Divine epithets**: outside the fixed Basmalah pair (`em Wohltätige, em Barmherzige`), the Compassionate/Beneficent/Merciful field is not fully unified: `Wohltät*` 65x, `Barmherz*` 210x, `Erbarm*` 52x. Superlative coinages appear in several ranges. Pick one Rahman/Rahim handling and normalize.
- **Charity/zakat vocabulary**: `Wohltätigkeit*` 37x, `Almos*` 10x, plus `Gab`/`Spende`/`fälligi Stür` variants (notably 9:29 "due tax" rendered plainly with no traditional term imported). Keep one term for "obligatory charity" while preserving Robert's rule: no percentage because the Quran gives none.
- **Jinn/spirits**: `Dschinn` 24x, but English "sprites/imp" sometimes became `Geischter/Kobold/Geischt/Dämone` (27:17/39, 34:12–14, 38:37, 41:25/29). Review should distinguish jinn from generic spirits as the English does.
- **Pronouns/register/negation**: this is the largest visible seam. Ranges vary among `nid/nöd/nit` for "not", `ir/euch/öi` for "you (pl.)", `mir/wir` spellings, and plural verb endings. The pan-dialect device makes some seaming unavoidable, but a native reviewer should normalize the worst clashes.
- **Prostration verb**: range 8 improvised `nidderproschterne` (32:15); the assembly label is `Niderwerfig`. A reviewer should confirm a natural verb for the act itself.
- **Repeated literal images**: "stabilizers" over the earth kept literal (41:10 family), "numerical book" (83:9/20), 81:4 follows the English master's "relationships are suspended", 68:42 the Shin remains literal, 37:49 "guarded pearls", palm-fiber/thorn phrasing in surah 111, and Tilford's coined epithets ("De Schocker" 101:1, "de Zerquetscher" 104:4, "Bluetklumpe" 96:2) were kept from his wording and flagged.

## 4. Source-English problems handled by intended reading, not copied

- 47:36 — English "life of this word" rendered as world (`Welt`), following the Bavarian precedent; flagged in range 10 as a likely source typo.
- 39:67 — English "His righ" read as "right".
- Broken quotation and sentence flow was preserved where the English itself splits across verses or lacks a closing quote. Strong or sensitive source wording was not softened by commentary (4:34, 4:89/91, inheritance fractions at 4:11/12/176, 58:2–4, 65 divorce terms, 66:12). These need native legal/tone review precisely because the draft stayed close.

## 5. Assembly details

- Front matter is labeled in Alemannic and English as a revision draft in progress inviting later peer/native review; no final/locked claim, no first-ever claim, and an explicit local-only / no-ownership-overreach statement per Robert's restraints.
- Basmalah frame wording at assembly: `Im Name vo Allah, em Wohltätige, em Barmherzige.` Surah 9 carries no basmalah frame; surah 1's basmalah is verse 1:1. Solomon's letter (27:30) uses the same Basmalah form.
- 5:6 retains the source ` ¶ ` split in the slice. In the manuscript and PDF, the first part is followed by the translator's note — `Mängi Lesarte setze s Wüsche bis zu de Füess wyter; di do druckti Lesart seit wäsche.` — then the continuation, as in the other Ayah Companion builds.
- Prostration labels read `Niderwerfig — empfohle` (recommended) and `Niderwerfig — verpflichtend` (obligatory), placed after the verse Arabic.

## 6. Independent verification result

Verification file: `work/verification-als.json`.

- 114 surah headers in order 1–114: true.
- 6,236 assembled verse blocks; per-surah counts match `meta.json` and the corrected English master for all 114 surahs: true.
- Reference continuity 1..k inside every surah: true.
- Slice audit: 114/114 files, 114 INTRO lines, 6,236 verse lines, refs identical to English in order, no missing/extra refs, no tab-format failures, no empty verse texts, ` ¶ ` parity (1 = 1, the 5:6 split), 0 `[MISSING]`.
- Arabic: 6,462 ordered runs in the Alemannic manuscript; identical to both the corrected English master segment and the expected `meta.json` sequence (114 surah names + 112 basmalah frames + 6,236 verse Arabic lines): true.
- Markers: 15/15 at 7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 38:24, 84:21 (recommended) and 32:15, 41:38, 53:62, 96:19 (obligatory): match.
- 5:6 note present: true.
- Percent sign: 0 in slices, verse first-lines, and entire manuscript.
- Distinctly-English function-word scan: 20 hits in assembled verse first-lines and 20 across slice texts — all 20 are the single token `to` in surahs 11–16 (e.g., "Unrecht to hend"), which is the Alemannic infinitive/perfect verb form from `tue`, not English leakage. No other strict-list English word appears. This scan does not judge German/Alemannic cognates or retained proper names.
- PDF check: 497 pages; extracted text has exactly 6,236 unique verse-reference tokens, the 5:6 note present, and Arabic text present throughout (311,358 Arabic characters extracted). The PDF is a reading build of the same verified manuscript, not a separate edition.

## 7. File record

- `ayah-companion-manuscript-ALS.md` — 2,256,574 bytes — SHA-256 `4bf3493333d2cbda20bf474191605e68e5a05fd2202555af74628dff25a9c905`
- `Ayah_Companion_Tilford_Alemannic_Manuscript.pdf` — 1,835,265 bytes — SHA-256 (see MANIFEST.txt)
- `work/titles-als.json` — SHA-256 (see MANIFEST.txt)
- `work/verification-als.json` — SHA-256 (see MANIFEST.txt)
- `work/flags-als.txt` — concatenated per-range flags (500 lines) — SHA-256 (see MANIFEST.txt)

Status remains: **REVISION DRAFT — structural verification only; native Alemannic review required before any use beyond review. Local only; nothing published, uploaded, emailed, archived, or posted.**
