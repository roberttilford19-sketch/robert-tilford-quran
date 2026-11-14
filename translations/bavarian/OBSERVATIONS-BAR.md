# OBSERVATIONS-BAR — working notes for the Bavarian manuscript

*Manuscript: `ayah-companion-manuscript-BAR.md` — REVISION DRAFT / ÜBERARBEITUNGS-ENTWURF, not a final edition and not native-reviewed. Bavarian rendering verse-for-verse from Robert Tilford's corrected English master; Arabic spliced from `work/meta.json` verse-for-verse at assembly. PDF: `Ayah_Companion_Tilford_Bavarian_Manuscript.pdf` (503 pages). Nothing was published, uploaded, emailed, or posted.*

## 1. Dialect choice and house rules

- Target is broad Central Bavarian (Mittelbairisch / Boarisch) in a readable written form: not a narrow village phonetic spelling and not standard German with dialect words sprinkled in. Recurring forms are `i/du/ea/mia/es`, `da/d/s`, `ned`, `a`, `ham/hod`, `is/war/werd`, `ko/wui`, `wann/wei`, `vo/zua/fia/bei/mit`.
- The language aims at Robert's stated target: plain, clear, humble everyday words and short sentences where the English permits it, while preserving legal, oath, quotation, and sentence structures that are themselves dense in the source.
- `Allah` is kept as `Allah` for English God as referent (2,462 occurrences in slice verse text; 2,850 Latin-script `Allah` in the assembled file including front matter, contents/intros, and the repeated Basmalah lines). `Lord` is generally `Herr`; master/owner/protector senses sometimes became `Besitzer`, `Beschützer`, or `Schutzherr` and are flagged where the choice matters.
- Quran-alone discipline held: no hadith/tafsir material imported, no traditional specifics added, and zakat/obligatory charity receives no percentage. Verified: 0 `%` in slices, assembled verse first-lines, and the whole manuscript.
- Surah titles are in `work/titles-bar.json`, newly made in Bavarian from the English title list in `work/meta.json`. The front matter makes no first-ever claim: it states only that no complete Bavarian Quran translation was found after research, which is not proof of being first.

## 2. Production and rate-limit note

- The Bavarian slices were translated from `work/en/surah_001.txt` ... `surah_114.txt` only. Extraction had already verified 114 surahs / 6,236 verses in the corrected English master's exact reference sequence, 6,462 Arabic runs, 112 basmalah frames, and 15 markers.
- Three first-pass ranges failed on a provider 429 rate limit before writing files: surahs 4-6, 7-9, and 67-74. They were refilled in six smaller blocks (surah 4; 5-6; 7; 8-9; 67-70; 71-74). Final audit found every range present; no quarantined or substituted text was used.

## 3. Terminology and consistency flags for a native Bavarian reviewer

Full per-verse flags are preserved in `work/flags-bar.txt`. The main consistency decisions a reviewer should make once, project-wide, are:

- **Quran/Koran split**: verse text has `Quran` 43x and `Koran` 25x. Choose one house spelling.
- **Moses split**: `Mose` 47x and `Moses` 89x. Other people-name forms also vary by slice (e.g. Henoch/Ezechiel/Ismael at 21:85; English-form Moses/Abraham noted at 87:19; Qarun normalized while Abee Lahab, Erum, idol names at 71:23, and at-Tariq were retained). A single name policy is needed.
- **Generic "god" versus Allah**: `Gott` occurs 94x, mostly in fixed formulas such as "koa Gott außer Eam" and at 114:3 "Am Gott da Menschheit." This is a proper-name/common-noun split, not English leakage (standalone English `God` = 0), but a Bavarian Muslim reviewer may prefer a different convention.
- **Divine epithets**: outside the fixed Basmalah pair (`am Wohltätigen, am Barmherzigen`), the Compassionate/Beneficent/Merciful field is not fully unified: `Wohltät*` 54x, `Barmherz*` 201x, `Erbarm*` 1x. Pick one Rahman/Rahim handling and normalize.
- **Charity/zakat vocabulary**: `Almos*` 15x, `Wohltätigkeit` 23x, `Pflichtabgabe/Pflichtabgab` 2x. Keep one term for the English "obligatory charity" while preserving Robert's rule: no percentage because the Quran gives none. At 8:41 the "fifth" remains a fraction of spoils, not a zakat rate.
- **Remembrance vocabulary**: `Erinnerung` 45x beside `Gedenken` 15x; devotional register should be settled.
- **Jinn/spirits**: `Dschinn` 27x, but English "sprites" sometimes became descriptive `Geister/Geisterwesen` (notably 6:100, 27:17/39, 34:12). Review should distinguish jinn from generic spirits as the English does.
- **Pronouns/register**: slices vary among `es/ihr`, `eng/eich/enka`, `mia/wia`, and plural address. This is the largest visible register seam and should be normalized only by a native reviewer, not during structural audit.
- **Repeated literal images**: "stabilizers" over the earth became `Stabilisatoren` (31:10, 41:10, 21:31 family) 4x; "numerical book" is `Buch mit Zahlen` (83:9/20); 81:4 follows the English master's "relationships are suspended"; 68:42 the Shin remains literal; 37:49 keeps "guarded pearls"; 111-family palm-fiber/thorn phrasing needs idiom check.

## 4. Source-English problems handled by intended reading, not copied

- 39:67 — English "His righ" read as "right": `in Seina Rechten`.
- 47:36 — English "life of this word" rendered as world: `S Lebn vo dera Welt`.
- 3:7 — English "seeking descent" was rendered literally as `auf da Suche nach Abstieg`. This remains a high-priority reviewer decision; the current draft preserves the odd source wording rather than importing an interpretation.
- Broken quotation and sentence flow was preserved where the English itself splits across verses or lacks a closing quote, including 2:127-129, 2:215, 2:222, 11:54-55, 12:5-6, 43:13-14, 44:43-44, 6:145, and 25:22. Punctuation-only smoothing was flagged at 13:11 (`;,`).
- Strong or sensitive source wording was not softened by commentary: 4:34, 4:89/91, 4:92, inheritance fractions at 4:11/12/176, 58:2-3 zihar, 60:10, 65:1/4, 66:12, 56:35-37. These need native legal/tone review precisely because the draft stayed close.

## 5. Assembly details

- Front matter is labeled in Bavarian and English as a revision draft awaiting native Bavarian review; no final/locked claim is made.
- Basmalah frame wording at assembly: `Im Nama vo Allah, am Wohltätigen, am Barmherzigen.` Surah 9 carries no basmalah frame; surah 1's basmalah is verse 1:1.
- 5:6 retains the source ` ¶ ` split in the slice. In the manuscript and PDF, the first part is followed by the Bavarian translator's note — `Manche Lesartn setzn s Wischn bis zu de Fiaß fort; de do druckte Lesart sogt woschn.` — then the continuation, as in the other Ayah Companion builds.
- Prostration labels read `Niadwerfung — empfohlen` (recommended) and `Niadwerfung — verpflichtend` (obligatory), placed after the verse Arabic.

## 6. Independent verification result

Verification file: `work/verification-bar.json`.

- 114 surah headers in order 1-114: true.
- 6,236 assembled verse blocks; per-surah counts match `meta.json` and the corrected English master for all 114 surahs: true.
- Reference continuity 1..k inside every surah: true.
- Slice audit: 114/114 files, 114 INTRO lines, 6,236 verse lines, no missing refs, no extra refs, no tab-format failures, no empty verse texts, ` ¶ ` parity with English slices, 0 `[MISSING]`.
- Arabic: 6,462 ordered runs in the Bavarian manuscript; identical to both the corrected English master segment and the expected `meta.json` sequence (114 surah names + 112 basmalah frames + 6,236 verse Arabic lines): true.
- Markers: 15/15 at 7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 38:24, 84:21 (recommended) and 32:15, 41:38, 53:62, 96:19 (obligatory): match.
- 5:6 note present: true.
- Percent sign: 0 in slices, verse first-lines, and entire manuscript.
- Distinctly-English function-word scan: 0 hits in assembled verse first-lines and 0 hits across slice texts. This scan does not judge German/Bavarian cognates or retained proper names.
- PDF check: 503 pages; extracted text has exactly 6,236 unique verse-reference tokens, the 5:6 note present, and Arabic text present throughout. The PDF is a reading build of the same verified manuscript, not a separate edition.

## 7. File record

- `ayah-companion-manuscript-BAR.md` — 2,257,142 bytes — SHA-256 `22139e3988424078b0c15fb333a17139ae0c75a35fc25c141bb78ae8da715c98`
- `Ayah_Companion_Tilford_Bavarian_Manuscript.pdf` — 1,859,904 bytes — SHA-256 `41fa0516579ee6c098d1505e9c634f73dc75b54832e99b791f93347fcb3c917f`
- `work/titles-bar.json` — 2,636 bytes — SHA-256 `325635b7d7da3a4e5c79463440ddcb725690ac0bd408b80f4ca336e4179ab971`
- `work/verification-bar.json` — 4,854 bytes — SHA-256 `d758f186b747809c3e3cdc659d7068e8a52aa5cf1465ba4b023b3483abe3ccfb`
- `work/flags-bar.txt` — 10,942 bytes — SHA-256 `49e0f3c47ac28a71ebdf4e3f7981627b6004cbb3502278b1d8af3792520378ce`

Status remains: **REVISION DRAFT — structural verification only; native Bavarian review required before any use beyond review.**
