# SWEEP LANE B — Verse-Level Review, Surahs 12–28

**Scope:** Chinese Ayah Companion, staging anchor `robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md`, read against Robert's English Recital master (sole source) and the lane glossary `GLOSSARY-ZH.md`. Report only; no manuscript edited.
**Method:** (1) every Lane B flag in `census-flags.json` adjudicated in context (CN verse + EN verse read in full); (2) deterministic cross-probes (EN word vs CN word) for the six fault classes; (3) famous verses + first 10 verses of every surah read in full as a drift probe.
**Verdict key:** REAL = CN deviates from EN and/or the locked glossary · VARIATION = defensible translator choice · FALSE-POSITIVE = flag does not survive context.

---

## Headline patterns

1. **Divine-voice flattening is a chunk-level system in Surahs 23–28, not a scatter of slips.** Of 137 verses in 23–28 whose EN subject is "We", the CN preserves 我们 in only 31 (23%) and flattens to 我-only in **106 (77%)**. In Surahs 12–22 the same test gives 305 of 306 preserved (99.7%) — the sole exception is 18:103. The census caught only 11 of the 107 flattened verses because its patterns were verb-specific. Whoever/whatever translated the 23–28 chunks used 我 as the default divine voice.
2. **"Signs" （迹象） collapse into "revelations" （启示） — 14 verses.** Where EN distinguishes *signs* from *revelation/inspiration*, CN merges them into 启示， erasing Robert's word boundary (same class as Surah 2's 2:221).
3. **"The Book" without 这部 — 21 census flags, all REAL, plus 3 more found in probes (12:1, 26:2, 28:2).** The CN handles the *indefinite* correctly （一部经典 at 14:1, 21:10, 27:1 — positive controls), which makes the definite misses a habit, not a misunderstanding.
4. **Leftover editorial artifacts in the body text:** the prostration marker `*[叩头——建议的]*` survives at **8 verses** (13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26).
5. **Names are 100% clean in this lane.** Zero Ma Jian name forms in 12–28 (no 优素福 — Surah 12's body uses 约瑟 throughout; no 麦尔彦， 叶尔孤白， 易司哈格， 哈伦， 鲁特， 尤努斯， 麦西哈， 吉卜利勒， 阿丹…). The 2026-09-24 biblical-names unification held across all 17 surahs.
6. **Zakat: one breach only** — 24:37 （施舍 for "the zakat"). Correct at 23:4 （完纳天课） and 27:3 （完纳天课）.

---

## Part 1 — Census flags adjudicated (33 flags / 29 unique verses — ALL REAL)

### BOOK-NO-ZHEBU (21 flags, all REAL)
Glossary fixes 这部经典 for "the Book" (Robert's definite usage). In every flagged verse EN has definite "the Book" and CN has bare 经典.

| Verse | CN (verbatim) | EN (verbatim) |
|---|---|---|
| 13:1 | 这些是经典的迹象 | These are the verses of the Book |
| 13:36 | 我们赐给经典的人为降示给你的而欢喜 | Those We gave the Book rejoice in what was sent down to you |
| 13:43 | 还有通晓经典的人 | and whoever has knowledge of the Book |
| 15:1 | 这些是经典的节文；一部阐明一切的古兰经 | These are the signs of the Book — and a clear Quran |
| 16:64 | 我们降示给你经典 | We sent down the Book to you |
| 16:89 | 我们降示给你经典，作为对一切事物的解释 | We sent down the Book to you as an explanation of all things |
| 17:2 | 我们赐给摩西经典 | We gave Moses the Book |
| 17:4 | 我们在经典中传谕以色列的后裔 | We decreed for the children of Israel in the Book |
| 17:58 | 这是记录在经典中的 | That was written in the Book |
| 18:1 | 他把经典降示给他的仆人 | who sent down the Book to His servant |
| 19:16 | 你在经典中提及马利亚 | And mention Mary in the Book |
| 19:41 | 你在经典中提及亚伯拉罕 | And mention Abraham in the Book |
| 19:51 | 你在经典中提及摩西 | And mention Moses in the Book |
| 19:54 | 你在经典中提及以实玛利 | And mention Ishmael in the Book |
| 19:56 | 你在经典中提及以诺 | And mention Enoch in the Book |
| 23:49 | 我确已赐给摩西经典 (also WE-flag) | And We gave Moses the Book |
| 25:35 | 我赐给摩西经典 (also WE-flag) | We gave Moses the Book |
| 27:40 | 有经典知识的人说 | The one who had knowledge of the Book said |
| 28:43 | 赐给摩西经典 (also WE-flag) | And We gave Moses the Book |
| 28:52 | 在它之前我赐予经典的人信它 (also WE-flag) | Those to whom We gave the Book before it |
| 28:86 | 你未曾料到经典会传给你 | you did not hope that the Book would be cast to you |

Secondary notes: 13:1 CN renders EN "verses" as 迹象 (signs) — the signs/verses words swap both directions in this lane (see 27:1, 28:2 where EN "signs/verses" ↔ CN 经文/迹象）. 15:1 CN 一部阐明一切的古兰经 adds 一切 ("explains *everything*") not in EN "a clear Quran" — minor addition, low severity.

### WE-FLATTENED (11 census flags, all REAL)
EN divine "We" → CN singular 我. Full lane census in Part 2 §A — these 11 are a subset.

| Verse | CN | EN |
|---|---|---|
| 23:27 | 于是我启示他："在我的注视之下，奉我的启示建造方舟。当我的命令降临…" | Then We revealed to him, Make the ship under Our eyes, and by Our revelation. Then when Our command comes… |
| 23:33 | 我曾使他们在今世过着优渥的生活 | and whom We gave ease in the worldly life |
| 23:49 | 我确已赐给摩西经典 | And We gave Moses the Book |
| 25:35 | 我赐给摩西经典 | We gave Moses the Book |
| 25:48 | 我从天空降下纯净的水 | And We sent down purifying water from the sky |
| 26:59 | 我使以色列的后裔继承了它们 | and We gave it all to the Children of Israel as inheritance |
| 28:14 | 我赐给他智慧和知识。我这样报偿行善者 | We gave him judgment and knowledge. That is how We repay those who do good |
| 28:43 | 我在毁灭以前的世代之后，赐给摩西经典 | And We gave Moses the Book, after We destroyed the former generations |
| 28:52 | 在它之前我赐予经典的人信它 | Those to whom We gave the Book before it — they believe in it |
| 28:54 | 从我赐给他们的给养中施舍 | and they give from what We provided them |
| 28:76 | 我赐给他宝藏 | And We gave him of the treasures |

Note 28:54: 施舍 there renders EN "give" (not zakat) — correct use, not a breach.
Note 28:43 secondary: EN "insights for people" → CN 作为对人类的光明 ("a light for people") — "insights" （明证） swapped for "light". REAL, minor.

### ZAKAT-NO-TIANKE (1 flag, REAL)
- **24:37** — CN: 谨守礼拜和施舍 · EN: "keeping up the prayer, and **giving the zakat**". Glossary: zakat = 天课， never 施舍. REAL, high confidence. The lane's only zakat breach (cf. correct 完纳天课 at 23:4 and 27:3).

**Census score for Lane B: 33 flags → 33 REAL, 0 VARIATION, 0 FALSE-POSITIVE.**

---

## Part 2 — Beyond the census

### §A. Divine We→我 flattening: the full lane count (REAL, systematic)
Deterministic test (EN contains subject "We"; CN contains 我 but no 我们）, hand-verified on a sample (23:12, 24:1, 25:19, 26:15, 27:50, 28:44 — all REAL):

- **Surahs 12–22:** 306 EN-We verses → 305 preserved, **1 flattened: 18:103** (CN 你说："我告诉你们行为上损失最大的人吗？" · EN: Say, "Shall **We** tell you of the greatest losers in deeds?" — the quoted speaker itself shifts from God to the Prophet).
- **Surahs 23–28:** 137 EN-We verses → 31 preserved, **106 flattened.**

Flattened verse index, Surah 23 (31): 12, 13, 14, 17, 18, 19, 21, 23, 27, 30, 31, 32, 33, 41, 42, 44, 45, 49, 50, 55, 56, 62, 64, 71, 75, 76, 77, 90, 95, 96, 115.
Surah 24 (3): 1, 34, 46.
Surah 25 (18): 11, 19, 20, 23, 31, 32, 33, 35, 36, 37, 39, 45, 46, 48, 49, 50, 51, 56.
Surah 26 (21): 4, 7, 15, 52, 57, 59, 63, 64, 65, 66, 119, 120, 139, 170, 172, 173, 198, 200, 205, 208, 209.
Surah 27 (9): 4, 45, 50, 51, 53, 57, 58, 60, 86.
Surah 28 (24): 3, 5, 7, 10, 12, 13, 14, 35, 40, 41, 42, 43, 44, 45, 46, 51, 52, 54, 59, 61, 75, 76, 81, 83.

Exemplars (verbatim):
- 23:12 CN 我确已用泥土的精华创造了人 · EN "And **We** made man from an extract of clay."
- 24:1 CN 这是我降示的一章 · EN "A chapter — **We** sent it down, and made it binding…"
- 26:15 CN 我将与你们同在，倾听 · EN "**We** are with you, listening."
- 27:50 CN 他们谋划，我也谋划 · EN "They schemed a scheme, and **We** schemed a scheme."
- 28:44 CN 当我向摩西颁布命令时 · EN "when **We** decreed the matter to Moses."
Severity note: Robert's EN alternates We/He/I as the Arabic does (iltifat); flattening the We-verses to 我 homogenizes the divine voice across six surahs. Confidence: high (test is mechanical; sample hand-verified 6/6).

### §B. "Signs" → 启示 (revelations) — 14 verses (REAL)
CN uses 启示 (correctly) wherever EN says "inspired/revelation" — dozens of clean instances (12:15, 12:109, 16:68, 17:39, 26:52, 26:63, 28:7…). The drift is the noun for EN **"signs"**:
23:105 （我的启示 · "My signs"), 24:34 （阐明的启示 · "clarifying signs"), 24:46 (same), 24:58 (same formula), 24:59 （阐明他的启示 · "makes His signs clear"), 24:61 (same formula), 25:73 （他们主的启示 · "their Lord's signs"), 27:82 （我们的启示 · "Our signs"), 27:83 (same), 27:84 （我的启示 · "My signs"), 28:45 （宣读我的启示 · "reciting Our signs"), 28:47 （追随你的启示 · "follow Your signs"), 28:59 (same as 28:45), 28:87 （真主的启示 · "God's signs").
Related minor swaps in the same word-family: EN "signs" → 教训 "lessons" (12:7 对求知者确有许多教训 · "signs for those who ask"), EN "sign" → 奇迹 "miracle" (13:7 降下一个奇迹 · "Why was no sign sent down"), EN "reminder/remembrance" (dhikr) → 教诲 "teaching" (21:2 新的教诲， 21:10 你们的教诲， 26:5 新的教诲）, EN "signs" → 经文 (24:1 阐明的经文 · "clear signs"). All REAL, minor-to-moderate; the ayat word-field is unstable in both directions.
Borderline: EN "a sending down" (tanzil) → CN 的启示 at 20:4 and 26:192 — VARIATION (minor).

### §C. Leftover editorial artifacts — `*[叩头——建议的]*` ×8 (REAL, furniture)
13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26 — every sajda verse in the lane retains the bracketed prostration suggestion marker in the body text. Exemplar 19:58: …他们就哭泣着俯伏叩头。 *[叩头——建议的]* · EN: "they fell down in worship, weeping." Confidence: high. (False alarms excluded: 建议 as an ordinary verb at 12:26, 22:53, 26:35.)

### §D. Institutional loans — mixed verdicts
- **天房 for "the House" ×3 (REAL as pattern instances; term is Robert's open Decision 3):** 22:26 CN 我们为亚伯拉罕指明天房的地点 · EN "the place of **the House**"; 22:29 CN 环绕古老的天房 · EN "circle the **Ancient House**"; 22:33 CN 它们的归宿是古老的天房 · EN "their place is by the **Ancient House**."
- **禁寺 for EN "Sacred House" (REAL):** 14:37 CN 你的禁寺旁 · EN "by Your **Sacred House**".
- **禁寺 for EN plain "the mosque" (REAL, moderate):** 17:7 CN 要像第一次那样进入禁寺 · EN "to enter **the mosque** as they entered it the first time" — 禁寺 in Chinese Islamic usage denotes Mecca's sanctuary; the verse's mosque is Jerusalem's.
- **禁寺 authorized (FALSE-POSITIVE):** 17:1 and 22:25 — EN itself says "the **Sacred Mosque**" and glossary §四 fixes 禁寺 for al-Masjid al-Haram. Not drift.
- **清真寺 (FALSE-POSITIVE):** 22:40 CN 修道院、教堂、犹太会堂和清真寺 · EN "monasteries, and churches, and synagogues, and **mosques**" — generic plural, standard word.

### §E. 幽玄 for "the unseen" ×4 (pattern instances of Robert's open ruling item)
13:9 CN 他是幽玄和可见的知者 · EN "Knower of **the unseen** and the witnessed"; 16:77 CN 天地的幽玄属于真主 · EN "God's is **the unseen** of the heavens and the earth"; 18:26 CN 诸天与大地的幽玄属于他 · EN "His is **the unseen**…"; 23:92 CN 他全知幽玄与昭明 · EN "Knower of **the unseen** and the seen." The glossary does not fix al-ghayb; logged as instances, disposition is Robert's (cf. 2:3).

### §F. 贵族 for EN "chiefs / council" ×6 (REAL, systematic minor)
23:33 （他族中的贵族们 · "the chiefs of his people"), 23:46 （法老和他的贵族们 · "Pharaoh and his chiefs"), 26:34 （周围的贵族们 · "the chiefs around him"), 27:38 （众贵族啊 · "O council"), 28:32 （法老和他的贵族们 · "Pharaoh and his chiefs"), 28:38 （众贵族啊 · "Chiefs"). 贵族 (hereditary aristocracy) adds a class gloss absent from Robert's "chiefs/council" — same item as Surah 2's 2:246.

### §G. "Those who set up partners" — mostly correct, 3 deviations (REAL)
Correct fixed form 以物配主（者） at 12:106, 12:108, 15:94, 16:35, 16:120, 23:59. Deviations from glossary （以物配主者）: 16:123 CN 他不是偶像崇拜者 · EN "He was not among those who set up partners"; 22:17 CN 多神教徒 · EN "those who ascribe partners"; 28:87 CN 永不做多神教徒 · EN "never be of those who join partners with Him" (28:87 also carries a §B signs→启示 drift — double-drift verse).

### §H. "Submitted / submit" → 穆斯林 (REAL ×2)
- 15:2 CN 不信道的人也许希望成为穆斯林 · EN "Those who disbelieved may well wish that they had **submitted**."
- 22:78 CN 他以前和在这部经典中称你们为穆斯林 · EN "He named you **the submitted ones** before, and in this…"
Robert renders muslimun descriptively; CN restores the proper religious name. (Same verse 22:78: CN 在宗教上没有给你们困难 · EN "laid no hardship on you **in the way of life**" — 宗教 "religion" for Robert's descriptive phrase, minor REAL; and CN 你们要为主道尽力奋斗 adds 道 "path" to EN "strive for God", minor.)

### §I. Single-verse meaning items (famous verses & probes)
- **27:10 (REAL, notable):** CN 当他看见它抖动，仿佛恶魔一般 · EN "he saw it moving as if it were a **snake**" — the staff's simile swapped from snake to *demon* (jann misread as jinn). Concrete image lost.
- **25:63 (REAL, glossary):** CN 至慈者的仆人们 · EN "The servants of **the Beneficent**" — 至慈 is fixed for *the Merciful*; the Beneficent (al-Rahman) is 至仁. Name-attribute swap at the famous Furqan verse.
- **18:4 (REAL):** CN 警告那些说"真主生了儿子"的人 · EN "those who said, 'God has **taken** a child'" — "took" （收养/取） rendered 生了 (begot). Contrast 25:2, where CN correctly has 他未曾收养儿子 for "took no son" — the pair proves inconsistency.
- **14:8 (REAL):** CN 即使你们和大地上所有的人一起忘恩负义 · EN "If you **disbelieve** — you and all who are on earth" — kufr rendered ingratitude (cf. Surah 2's 2:88). Two verses earlier (14:7) EN itself says "ungrateful" and CN 忘恩负义 is correct there — CN uses one word for both EN words.
- **17:26 (REAL):** CN 穷人和旅客 · EN "the needy, and **the traveler**" — 旅客 (passenger/tourist) for ibn al-sabil; the glossary-adjacent literal 行路的人 occurs 0 times in the whole book (cf. 2:177, 2:215).
- **17:23 (REAL, minor):** CN 不要对他们说一句厌烦的话 · EN 'do not say **"Ugh"** to them' — the quoted interjection converted to a description ("a word of annoyance"); the ra'ina-pattern in miniature.
- **12:3 (REAL, minor):** CN 向你叙述最准确的历史 · EN "the **fairest of stories**" — stories → "most accurate history".
- **15:4 (REAL, minor, dropped element):** CN 除非它有定期 · EN "without a fixed term, **written down for it**" — "written down" dropped.
- **19:5 (REAL, minor, added gloss):** CN 我怕我死后我的亲属（无后继） · EN "I fear those who will follow after me" — bracketed in-text gloss （无后继） added.
- **26:10 (REAL, minor, addition):** CN 去教化暴虐的民众 · EN "'Go to the wrongdoing people'" — 教化 ("go teach/civilize") added to a bare "go".
- **13:1 / 26:2 / 28:2 (REAL, Book):** CN 明白经典 / 阐明经典 for EN "the clear Book" — three definite-Book misses beyond the census list.
- **17:68–69 (VARIATION):** CN 难道你们确信他不会使陆地的一块塌陷… · EN "Do you **feel safe** that He will not swallow you…" — security recast as certainty; the rebuke lands either way. (All other 确信 hits in the lane are FALSE-POSITIVE: 13:2 EN "that you may be **certain**", 15:99 EN "until **the certainty** reaches you", 27:3 EN "they are **certain**", 27:14 EN "their souls were **certain**" — CN matches EN.)
- **13:31 临在 (FALSE-POSITIVE):** substring artifact （降临在…附近）; no 临在 term in the lane.
- **自我 (FALSE-POSITIVE family):** no ego-drift in 12–28; hits are 自我洁净者 "one who purifies himself" (20:76, correct) and cross-boundary substrings. The Surah 2 "kill your ego" failure mode does not occur in this lane.
- **同胞 (none):** no 同胞-for-"yourselves" instance found in 12–28.
- **回忆当时 (none):** zero occurrences in 12–28 (all 12 book-wide are in Surah 2).

### §J. Positive controls (CN follows Robert against tradition)
- **Names:** zero Ma Jian forms in 17 surahs (see Headline 5). Surah 12 uses 约瑟/雅各/亚伯拉罕/以撒 throughout; 19:7 约翰 for John; 28:76 可拉 for Qarun.
- **18:65–82 (Khidr pericope):** read in full — tracks EN closely; the servant is never named (glossary: Khidr unnamed in body ✓); 18:82 CN 他们的父亲是敬畏者 · EN "their father was righteous" — glossary-exact.
- **24:35 (Light Verse):** CN tracks EN image-for-image （壁龛/玻璃罩/橄榄树） with no tafsir expansion.
- **13:28, 21:107, 18:29, 12:4:** clean, close renderings.
- **17:70:** EN "We honored the children of Adam" → CN 我们确已尊贵亚当的子孙 — We preserved, in the surah block where We is otherwise intact.
- **Indefinite "a Book":** CN 一部经典 correct at 14:1, 21:10, 27:1 （这部 reserved by sense for the definite — the misses in Part 1 are therefore selective, not systematic ignorance).
- **Zakat:** 完纳天课 at 23:4 and 27:3.
- **Quote pairing:** multi-verse speeches (19:4–6; 18:78–82) open and close where the EN does; no boundary bleeds found in the probe set (contrast Surah 2's 2:38/39).

---

## Per-surah summary

- **12 (Joseph):** Names perfect; We intact. Minor: 12:1 Book; 12:3 stories→history; 12:7 signs→教训； 12:2 "Arabic recital"→阿拉伯文的古兰经 (variation). 以物配主者 correct (106, 108).
- **13:** Census 13:1/36/43 Book REAL. 13:7 sign→奇迹； 13:9 幽玄； artifact 13:15. 13:28 clean; 13:2 确信 false-positive.
- **14:** 14:8 disbelieve→忘恩负义 REAL; 14:37 禁寺 for Sacred House REAL; 14:1 indefinite Book correct (positive).
- **15:** 15:1 Book REAL; 15:2 submitted→穆斯林 REAL; 15:4 dropped "written down"; 15:99 确信 false-positive.
- **16:** 16:64/89 Book REAL; 16:123 偶像崇拜者 deviation; 16:77 幽玄； artifact 16:50. Mushrik forms otherwise correct.
- **17:** 17:2/4/58 Book REAL; 17:26 traveler→旅客 REAL; 17:23 "Ugh" glossed REAL minor; 17:7 mosque→禁寺 REAL; 17:1 禁寺 authorized; artifact 17:109; 17:70 positive control.
- **18:** 18:1 Book REAL; 18:4 took→begot REAL; 18:26 幽玄； 18:103 the lane's only We-flattening outside 23–28; Khidr pericope clean.
- **19:** 19:16/41/51/54/56 Book REAL (the "mention in the Book" formula ×5); 19:5 bracket gloss; artifact 19:58; 19:58 itself also the famous-verse read — content otherwise exact.
- **20:** Lightest surah in lane. 20:4 tanzil→启示 variation; 20:76 自我洁净者 correct. 20:114 （增加我知识） clean.
- **21:** 21:2/10 dhikr→教诲 minor pattern; 21:107 clean; 21:10 indefinite Book correct.
- **22:** 22:26/29/33 天房 ×3; 22:17 多神教徒； 22:78 穆斯林 + 宗教 items; 22:25 禁寺 authorized; 22:40 清真寺 false-positive; artifacts 22:18, 22:77.
- **23:** The flattening begins: 31 We-verses flattened incl. census 23:27/33/49; 23:105 signs→启示； 23:92 幽玄； 贵族 ×2 (33, 46); 23:4 zakat correct (positive, pre-flattening zone).
- **24:** 24:37 zakat breach (lane's only one); signs→启示 ×5 (34, 46, 58, 59, 61); 24:1 signs→经文； 24:35 Light Verse clean; We flattened ×3 (1, 34, 46).
- **25:** We flattened ×18 incl. census 25:35/48; 25:63 至慈者 for the Beneficent REAL; 25:73 signs→启示； 25:60 artifact; 25:2 收养 positive contrast to 18:4.
- **26:** We flattened ×21 incl. census 26:59; 26:2 Book; 26:5 dhikr→教诲； 26:10 教化 addition; 贵族 26:34.
- **27:** We flattened ×9; signs→启示 ×3 (82, 83, 84); 27:10 snake→恶魔 REAL; 27:26 artifact; 27:40 census Book REAL; 27:3 zakat + certainty both correct (positive).
- **28:** We flattened ×24 incl. census 28:14/43/52/54/76; 28:43 insights→光明； 28:87 double drift （启示 + 多神教徒）; 贵族 ×2 (32, 38); 28:2 Book.

---

## Totals

| Category | Count | Notes |
|---|---|---|
| Census flags adjudicated | 33 | **33 REAL** (21 Book, 11 We, 1 zakat); 29 unique verses |
| We→我 flattened verses beyond census | 96 | 106 total in 23–28 + 18:103; census caught 11 |
| Signs→启示 | 14 | + word-family minors （教训 ×1, 奇迹 ×1, 教诲 ×3, 经文 ×1) |
| Book misses beyond census | 3 | 12:1, 26:2, 28:2 |
| Editorial artifacts `*[叩头——建议的]*` | 8 | 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26 |
| Institutional loans (real instances) | 5 | 天房 ×3 (22), 禁寺 ×2 (14:37, 17:7); 3 further hits authorized/false-positive |
| 幽玄 instances | 4 | open ruling item |
| 贵族 for chiefs/council | 6 | systematic minor |
| Mushrik-form deviations | 3 | 16:123, 22:17, 28:87 (against 6+ correct) |
| 穆斯林 for EN descriptive "submitted" | 2 | 15:2, 22:78 |
| Single-verse meaning items | 8 | 27:10, 25:63, 18:4, 14:8, 17:26, 17:23, 12:3, 15:4 (+ minors 19:5, 26:10, 28:43, 22:78b) |
| VARIATION | 3 | 20:4, 26:192 （启示 for tanzil), 17:68–69 （确信 for feel-safe) |
| FALSE-POSITIVE families | 5 | 确信 ×4 verses, 禁寺 ×2, 清真寺 ×1, 临在 ×1, 自我 family |

**Pattern summary.** Lane B splits cleanly in two. Surahs 12–22 are the healthiest long stretch yet audited: names fully biblical, the divine We intact at 99.7%, zakat sound, and the faults are the familiar Surah 2 species at low density — bare 经典 for "the Book" (the single most persistent habit), 幽玄， two descriptive-rendering overrides （穆斯林）, a handful of one-verse meaning swaps (18:4, 14:8, 17:26), and the sajda artifact line. Surahs 23–28 are a different country: the divine voice flattens to 我 in three-quarters of We-verses, "signs" collapse into 启示， 贵族 becomes the default for "chiefs," and the Book/zakat breaches continue — evidence that the 23–28 chunks were produced under different (weaker) constraint discipline than 12–22, exactly the "different slice crews drift differently" mechanism documented in the Jefferson audit. No dropped verses, no added passages, and no meaning reversals of the negation/agent class were found anywhere in the lane's probe set; the damage is lexical and vocal, not structural.
