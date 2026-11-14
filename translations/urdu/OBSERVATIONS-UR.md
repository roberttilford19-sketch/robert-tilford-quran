# OBSERVATIONS-UR — working notes for the Urdu manuscript

*Manuscript: `ayah-companion-manuscript-UR.md` — REVIEW DRAFT, not publication. Urdu rendering verse-for-verse from Robert Tilford's corrected English master; the Arabic is spliced from the master character-for-character. Built in 12 parallel slices from a single brief (`work/BRIEF-UR.md`); structure independently verified (below). Nothing here corrects meaning silently: every intended-reading is listed.*

## 1. Source-English errors rendered by intended reading (never propagated)

Total logged: **39 flags** — the canonical 26 (listed in the Italian run) plus 13 further instances of the same families found in other slices (mostly "Median" → مدین *Midian*: besides 22:44 also 7:85, 9:70, 11:84, 11:95, 20:40, 28:22, 28:23, 28:45, 29:36).

**Typos / wrong words (family):**
- 5:65 — "Scriputure" → آسمانی کتاب
- 39:67 — "in His righ" → right hand
- 23:110 — "made then" → made them
- 47:36 — "life of this word" → "life of this world"
- 11:42 — "On my son!" → "O my son!"
- 22:44 (+ 9 further refs) — "Median" rendered **مدین (Midian)**; *reviewer to confirm the Quranic referent, as in the Italian note*
- 3:7 — source "descent" rendered as discord/dissent (translator judgment; *flag for the reviewer: intended word is almost certainly "dissent"*)

**Broken grammar (family):** 4:77, 5:64, 5:80, 13:19, 33:15, 38:11, 41:29, 41:52, 57:6, 7:167.

**Unclosed or unmatched quotation marks (family):** 2:127, 2:215, 2:222 (extra closing quote), 6:78, 6:80, 6:162 (per brief), 7:16, 7:18, 7:67, 10:49, 60:4 (closed at 60:5). In Urdu the quote is closed where the sense closes it.

**Minor:** 7:173, 7:189 capitalization oddities; 56:96 missing final period; 29:14 "and He stayed" — rendered in third person about Noah (capital-H pronoun belongs to the English's grammar, not to a divine referent; matches the Italian run's resolution).

## 2. Terminology decisions for the reviewer

- **41:41 «یاد دہانی» vs 43:5 «نصیحت»** — "the Reminder" rendered two ways across slices (same weak spot as the Italian "il Richiamo"). Pick one and apply everywhere.
- **خدا (19×)** beside **اللہ (2,730×)**: the brief fixed اللہ for "God"; خدا survives mostly in idiomatic possessive-style phrases. Reviewer may wish to unify fully to اللہ or accept the idiom.
- **انکار کرنے والے (73×) / کافر (1×)**: brief default followed well.
- 33:40 spelled **محمد** correctly; the Italian "Maometto vs Muhammad" cross-slice inconsistency did **not** recur in Urdu.
- Brief-mandated vocabulary held manuscript-wide: اللہ، رب، رسول / نبی، کتاب / قرآن / آسمانی کتاب، آخرت، باغ / جنت، آگ / جہنم، نماز ادا کرنا / قائم کرنا، **زکاۃ with no percentage** (the Quran gives none), ایمان والے / انکار کرنے والے، ظالم، منافق، نشانیاں، قیامت کا دن۔ Names all in established Urdu spellings (موسیٰ، عیسیٰ، ابراہیم، مریم)۔

## 3. Literal renderings — known weak spots for a native reader

- **81:4** — "When the relationships are suspended" rendered literally: «جب رشتے معطل ہو جائیں۔» (same literalism flagged in the Italian run).
- **83:9, 83:20** — "A numerical book" rendered «ایک عددی کتاب۔» (literal; likely "a written register/record").
- Register variance across 12 translators is expected (fixed formulas, pronouns and connectives vary slightly); superlatives such as "the most Merciful" mirror the English rather than a single normalized form. A consistency pass is advisable.
- Independent letters (2:1 etc.) are in Urdu script as instructed; 26:1/27:1/28:1 use طٰسٓ مٓ type forms — reviewer to confirm preferred convention.

## 4. Structure and discipline

- Format identical to the Italian build: Urdu title block (نظرِ ثانی مسودہ / اشاعت کے لیے نہیں), فہرست table of contents, حصہ اول · ترجمہ, 114 sections with the Arabic surah name, an italic intro line, basmalah Arabic + italic fixed-formula line «اللہ کے نام سے، جو بڑا مہربان، نہایت رحم والا ہے۔» in the 112 surahs that carry the frame (surah 1 counts it as 1:1; surah 9 has none), translator's note inside 5:6 with its continuation after it, 15 prostration markers (11 مستحب, 4 واجب) printed after the verse's Arabic line, as in the Italian layout.
- Quran-alone discipline: no hadith/tafsir material imported, no traditional specifics added, no percentage for zakat.
- The audit is **structural** (counts, sequences, the Arabic character-for-character, markers, residue scan), as for the other drafts of this project: it is not a verse-by-verse philological proof. Final language quality requires a native Urdu reviewer.

## 5. Independent verification result (on the assembled file)

- (a) 114 surah headers, in order 1–114 ✓
- (b) 6,236 verse blocks; per-surah counts equal to the English master for all 114 surahs ✓
- (c) references continuous 1..k in every surah ✓
- (d) Arabic text: 6,462 ordered runs, byte-identical to the master (surah names, 112 basmalah frames, 6,236 verse lines) ✓
- (e) 0 [MISSING] markers ✓
- (f) 15 prostrations at the exact references (11 recommended, 4 obligatory); 5:6 translator's note and continuation present ✓
- (g) 0 verse/intro lines with English residue (Latin-letter scan) ✓

*File: `ayah-companion-manuscript-UR.md` (2,753,167 bytes; SHA-256 `83eb93d4f7f09ebf3334af6aaa070c249c209d9ed84b10d33119c9c3ea45cb1f`). Work files: `work/en/` (extracted English), `work/ur/` (Urdu slices), `work/meta.json` (Arabic/markers), `work/BRIEF-UR.md` (brief), `work/titles-ur.json` (Urdu surah titles), `work/flags.txt` (39 logged flags).*
