# WE-CENSUS — Divine-We Clause Census (Patch Class P-03 master enumeration)

Generated 2026-10-12 by `we-census.py` (this folder) from:
- EN master: `~/workspace/original-recital/files/original-recital-FULL.txt`
- CN staging: `~/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md`
- Machine rows (same data as the tables below): `WE-CENSUS-rows.json` (this folder)

## Method

Every EN verse was scanned for first-person-plural divine voice at CLAUSE level.
Robert's EN capitalizes the divine pronoun even mid-clause ("what We provided them") —
that is Tier 1, unambiguous. A capitalized We/Our/Us at a clause head is Tier 2 (usually
divine narration, occasionally a creature's sentence-initial word). Lowercase we/our/us is
never Robert's divine voice and was excluded. Each EN clause was anchored into the CN
verse by its character fraction; the CN clause window (±1 clause) was judged: 我们
governing the clause = PRESERVED; 我, zero pronoun with singular carry-over, a dropped
pronoun, or a third-person substitution = FLATTENED. A verse with both = MIXED.
Creature speech (quoted or dictated words of humans, angels, jinn — including "Our Lord"
prayers and Say:-dictated confessions) was classified HUMAN and excluded.
The script cast a wide net; EVERY candidate row was then hand-read in context
(all script-FLATTENED rows, all MIXED verses, all both-pronoun verses, all Tier-2
quote/verb queues, the Tier-1 quote queue, the unknown-quote residue, and two
attribution-pattern sweeps). Corrections live in the script's OVERRIDES table with
rationale comments — this file is fully reproducible by re-running the script.

## Book totals

- Verses containing divine We: **1165** — PRESERVED 870 · FLATTENED 291 · MIXED 4
- Clauses: **1483** — PRESERVED 1135 · FLATTENED 348

## Verses needing P-03 repair (verse verdict FLATTENED or MIXED)

2:3, 2:23, 2:39, 2:57 (MIXED), 8:59, 18:103, 23:12, 23:13, 23:14, 23:17, 23:18, 23:19, 23:21, 23:23, 23:27, 23:30, 23:31, 23:32, 23:33, 23:41, 23:42, 23:44, 23:45, 23:49, 23:50, 23:55, 23:56, 23:62, 23:64, 23:65, 23:71, 23:75, 23:76, 23:77, 23:90, 23:95, 23:96, 23:115, 24:1, 24:34, 24:46, 25:11, 25:19, 25:20, 25:21, 25:23, 25:31, 25:32, 25:33, 25:35, 25:36, 25:37, 25:39, 25:45, 25:46, 25:48, 25:49, 25:50, 25:51, 25:56, 26:4, 26:7, 26:15, 26:52, 26:57, 26:59, 26:63, 26:64, 26:65, 26:66, 26:119, 26:120, 26:139, 26:170, 26:172, 26:173, 26:198, 26:200, 26:204, 26:205, 26:208, 26:209, 27:4, 27:13, 27:15, 27:45, 27:50, 27:51, 27:53, 27:57, 27:58, 27:60, 27:82 (MIXED), 27:83, 27:86, 28:3, 28:5, 28:7, 28:10, 28:12, 28:13, 28:14, 28:35, 28:36, 28:40, 28:41, 28:42, 28:43, 28:44, 28:45, 28:46, 28:48, 28:51, 28:52, 28:54, 28:58 (MIXED), 28:59, 28:61, 28:75, 28:76, 28:81, 28:83, 29:39, 30:28 (MIXED), 38:3, 38:17, 38:18, 38:20, 38:24, 38:25, 38:26, 38:27, 38:28, 38:29, 38:30, 38:34, 38:36, 38:39, 38:40, 38:41, 38:43, 38:44, 38:45, 38:46, 38:47, 38:54, 39:2, 39:27, 39:41, 40:23, 40:25, 40:51, 40:53, 40:70, 40:77, 40:78, 40:84, 40:85, 41:12, 41:15, 41:16, 41:17, 41:18, 41:25, 41:27, 41:28, 41:39, 41:40, 41:44, 41:45, 41:50, 41:51, 41:53, 42:7, 42:13, 42:20, 42:23, 42:35, 42:38, 42:48, 42:52, 43:3, 43:4, 43:6, 43:8, 43:11, 43:21, 43:23, 43:25, 43:32, 43:33, 43:36, 43:38, 43:41, 43:42, 43:45, 43:46, 43:47, 43:48, 43:50, 43:55, 43:56, 43:59, 43:60, 43:69, 43:76, 43:78, 43:79, 43:80, 44:3, 44:5, 44:15, 44:16, 44:17, 44:28, 44:30, 44:32, 44:33, 44:37, 44:38, 44:39, 44:54, 44:58, 45:6, 45:9, 45:16, 45:17, 45:18, 45:21, 45:25, 45:29, 45:34, 46:3, 46:7, 46:15, 46:16, 46:25, 46:26, 46:27, 46:29, 47:13, 47:30, 47:31, 59:21, 61:14, 63:10, 64:8, 64:10, 64:12, 65:8, 66:12, 67:5, 68:15, 68:16, 68:17, 68:35, 68:39, 68:44, 69:11, 69:44, 69:45, 69:49, 70:7, 70:39, 70:40, 70:41, 71:1, 72:16, 73:5, 73:12, 73:15, 73:16, 74:16, 74:31, 75:3, 75:4, 75:17, 75:18, 75:19, 76:2, 76:3, 76:4, 76:23, 76:28, 77:16, 77:17, 77:18, 77:20, 77:21, 77:23, 77:25, 77:38, 77:44, 80:26, 95:5

## Borderline calls (read before patching)

- **51:36 / 56:61 — judged PRESERVED by cross-verse carry-over.** The CN clause has a zero
  pronoun, but it continues the 我们 subject of the immediately preceding verse
  (51:35 我们把…撤了出来； 56:60 我们已…注定了死亡）, so the voice stays plural. Not repair items.
- **30:28 — flattening by third-person substitution:** "what We provided you" is rendered
  真主赐予你们 (God as third person). Counted FLATTENED.
- **8:59 — "outran Us": the divine object pronoun is dropped in CN.** Counted FLATTENED.
- **Zero-pronoun continuations after a 我 clause** (e.g. 77:17, 77:21, 80:26, 95:5) stay
  FLATTENED: the carried subject is the singular 我.
- **29:31** was excluded as HUMAN (the angels' "We will destroy"); its narration possessive
  "Our messengers" is nonetheless preserved in CN （我们的使者） — no repair needed there.
- **15:66** "We decreed for him that command" is read as divine narration resuming after
  the angels' speech (CN 我们告诉他我们的判决， PRESERVED) — flagged here as the one
  genuinely arguable speaker call in the census.

## Per-surah totals

| Surah | Verses w/ divine We | V-PRESERVED | V-FLATTENED | V-MIXED | Clauses | C-PRESERVED | C-FLATTENED |
|---|---|---|---|---|---|---|---|
| 2 | 45 | 41 | 3 | 1 | 58 | 54 | 4 |
| 3 | 13 | 13 | 0 | 0 | 17 | 17 | 0 |
| 4 | 33 | 33 | 0 | 0 | 43 | 43 | 0 |
| 5 | 21 | 21 | 0 | 0 | 26 | 26 | 0 |
| 6 | 53 | 53 | 0 | 0 | 75 | 75 | 0 |
| 7 | 69 | 69 | 0 | 0 | 96 | 96 | 0 |
| 8 | 6 | 5 | 1 | 0 | 6 | 5 | 1 |
| 9 | 4 | 4 | 0 | 0 | 6 | 6 | 0 |
| 10 | 26 | 26 | 0 | 0 | 41 | 41 | 0 |
| 11 | 30 | 30 | 0 | 0 | 42 | 42 | 0 |
| 12 | 20 | 20 | 0 | 0 | 28 | 28 | 0 |
| 13 | 8 | 8 | 0 | 0 | 9 | 9 | 0 |
| 14 | 9 | 9 | 0 | 0 | 10 | 10 | 0 |
| 15 | 30 | 30 | 0 | 0 | 34 | 34 | 0 |
| 16 | 21 | 21 | 0 | 0 | 26 | 26 | 0 |
| 17 | 47 | 47 | 0 | 0 | 69 | 69 | 0 |
| 18 | 36 | 35 | 1 | 0 | 41 | 40 | 1 |
| 19 | 29 | 29 | 0 | 0 | 34 | 34 | 0 |
| 20 | 36 | 36 | 0 | 0 | 42 | 42 | 0 |
| 21 | 52 | 52 | 0 | 0 | 82 | 82 | 0 |
| 22 | 16 | 16 | 0 | 0 | 22 | 22 | 0 |
| 23 | 35 | 3 | 32 | 0 | 41 | 3 | 38 |
| 24 | 3 | 0 | 3 | 0 | 3 | 0 | 3 |
| 25 | 19 | 0 | 19 | 0 | 23 | 0 | 23 |
| 26 | 25 | 3 | 22 | 0 | 27 | 3 | 24 |
| 27 | 15 | 2 | 12 | 1 | 18 | 4 | 14 |
| 28 | 29 | 2 | 26 | 1 | 40 | 3 | 37 |
| 29 | 22 | 21 | 1 | 0 | 30 | 29 | 1 |
| 30 | 9 | 8 | 0 | 1 | 12 | 11 | 1 |
| 31 | 7 | 7 | 0 | 0 | 10 | 10 | 0 |
| 32 | 10 | 10 | 0 | 0 | 13 | 13 | 0 |
| 33 | 8 | 8 | 0 | 0 | 11 | 11 | 0 |
| 34 | 19 | 19 | 0 | 0 | 26 | 26 | 0 |
| 35 | 8 | 8 | 0 | 0 | 9 | 9 | 0 |
| 36 | 26 | 26 | 0 | 0 | 38 | 38 | 0 |
| 37 | 41 | 41 | 0 | 0 | 42 | 42 | 0 |
| 38 | 24 | 2 | 22 | 0 | 27 | 2 | 25 |
| 39 | 5 | 2 | 3 | 0 | 6 | 3 | 3 |
| 40 | 13 | 4 | 9 | 0 | 15 | 4 | 11 |
| 41 | 21 | 6 | 15 | 0 | 23 | 7 | 16 |
| 42 | 8 | 0 | 8 | 0 | 11 | 0 | 11 |
| 43 | 29 | 1 | 28 | 0 | 36 | 1 | 35 |
| 44 | 14 | 0 | 14 | 0 | 17 | 0 | 17 |
| 45 | 9 | 0 | 9 | 0 | 10 | 0 | 10 |
| 46 | 8 | 0 | 8 | 0 | 9 | 0 | 9 |
| 47 | 3 | 0 | 3 | 0 | 5 | 0 | 5 |
| 48 | 4 | 4 | 0 | 0 | 4 | 4 | 0 |
| 49 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 50 | 15 | 15 | 0 | 0 | 20 | 20 | 0 |
| 51 | 9 | 9 | 0 | 0 | 10 | 10 | 0 |
| 52 | 4 | 4 | 0 | 0 | 5 | 5 | 0 |
| 53 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 54 | 21 | 21 | 0 | 0 | 23 | 23 | 0 |
| 55 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 56 | 13 | 13 | 0 | 0 | 16 | 16 | 0 |
| 57 | 6 | 6 | 0 | 0 | 10 | 10 | 0 |
| 58 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 59 | 1 | 0 | 1 | 0 | 2 | 0 | 2 |
| 61 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 63 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 64 | 3 | 0 | 3 | 0 | 3 | 0 | 3 |
| 65 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 66 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 67 | 1 | 0 | 1 | 0 | 2 | 0 | 2 |
| 68 | 6 | 0 | 6 | 0 | 6 | 0 | 6 |
| 69 | 4 | 0 | 4 | 0 | 4 | 0 | 4 |
| 70 | 4 | 0 | 4 | 0 | 4 | 0 | 4 |
| 71 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 72 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 73 | 4 | 0 | 4 | 0 | 5 | 0 | 5 |
| 74 | 2 | 0 | 2 | 0 | 3 | 0 | 3 |
| 75 | 5 | 0 | 5 | 0 | 5 | 0 | 5 |
| 76 | 5 | 0 | 5 | 0 | 8 | 0 | 8 |
| 77 | 9 | 0 | 9 | 0 | 9 | 0 | 9 |
| 78 | 5 | 5 | 0 | 0 | 5 | 5 | 0 |
| 80 | 2 | 1 | 1 | 0 | 2 | 1 | 1 |
| 83 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 87 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 88 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 90 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 92 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 94 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 95 | 2 | 1 | 1 | 0 | 2 | 1 | 1 |
| 96 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 97 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 108 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |

## Clause table

CN clause = the anchor window the verdict was judged on (the matched CN clause ±1).
After Patch Set 1 is applied, re-run the script: every row below must read PRESERVED.

### Surah 2

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 2:3 (FLATTENED) | 0 | Who believe in the unseen, keep up the prayer, and give from what We provided them. | 履行礼拜，并施舍我所赐给他们的。 | FLATTENED |
| 2:23 (FLATTENED) | 0 | And if you are in doubt about what We sent down upon Our servant, then bring a chapter like it, and call your witnesses besides God, if you are truthful. | 如果你们怀疑我降示给我的仆人的，就作出一章像这样的， | FLATTENED |
| 2:34 (PRESERVED) | 0 | And when We said to the angels, "Bow down to Adam," they bowed down | 当时我们对天使们说：“向亚当叩头。 | PRESERVED |
| 2:35 (PRESERVED) | 0 | And We said, "O Adam, dwell | 我们说：“亚当啊， | PRESERVED |
| 2:36 (PRESERVED) | 0 | And We said, "Go down | 使他们离开了原有的境况。我们说：“你们下去吧， | PRESERVED |
| 2:38 (PRESERVED) | 0 | We said, "Go down from it, all of you. | 我们说：“你们全体从其中下去。 | PRESERVED |
| 2:39 (FLATTENED) | 0 | And those who disbelieve and call Our signs lies | 至于不信道并否认我的迹象的人——他们是火狱的居民——他们将永居其中。” | FLATTENED |
| 2:49 (PRESERVED) | 0 | And when We saved you from Pharaoh's people, who laid on you the worst punishment | 回忆当时，我们拯救你们脱离法老的宗族。 | PRESERVED |
| 2:50 (PRESERVED) | 0 | And when We parted the sea for you, and saved you, and drowned Pharaoh's people, while you were watching. | 回忆当时，我们为你们分开大海， | PRESERVED |
| 2:51 (PRESERVED) | 0 | And when We appointed forty nights for Moses, then you took up the calf after him | 回忆当时，我们为摩西约定了四十夜。 | PRESERVED |
| 2:52 (PRESERVED) | 0 | Then We pardoned you after that, so that you might give thanks. | 然后我们在那之后宽恕了你们，以便你们感谢。 | PRESERVED |
| 2:53 (PRESERVED) | 0 | And when We gave Moses the Book and the Criterion, so that you might be guided. | 回忆当时，我们把经典和辨别真伪的标准赐给摩西， | PRESERVED |
| 2:56 (PRESERVED) | 0 | Then We raised you after your death, so that you might give thanks. | 然后我们在你们死后使你们复活，以便你们感恩。 | PRESERVED |
| 2:57 (MIXED) | 0 | And We shaded you with the clouds, and sent down upon you the manna and the quails: | 我们以云荫蔽你们，降下甘露和鹌鹑给你们： | PRESERVED |
| 2:57 (MIXED) | 1 | "Eat from the good things We provided you." They did not wrong Us, but they were wronging themselves. | 降下甘露和鹌鹑给你们：“吃我赐给你们的佳美食物。”他们没有亏待我们， | FLATTENED |
| 2:58 (PRESERVED) | 0 | And when We said, "Enter this town, and eat from it wherever you wish, plentifully, and enter the gate bowing down, and say, 'hitta' | 回忆当时，我们说： | PRESERVED |
| 2:58 (PRESERVED) | 1 | We will forgive you your sins | 但要谦卑地进城门，说‘宽恕’。我们将宽恕你们的罪， | PRESERVED |
| 2:58 (PRESERVED) | 2 | and We will increase those who do good." | 我们将宽恕你们的罪，并增加行善者的。” | PRESERVED |
| 2:59 (PRESERVED) | 0 | Then those who did wrong changed the word to other than what was said to them, so We sent down upon those who did wrong a scourge from the sky, because they kept disobeying. | 但他们中的不义者换用了别的言辞代替给他们的，于是我们因他们的恶行，从天上降下灾疫给不义者。 | PRESERVED |
| 2:60 (PRESERVED) | 0 | We said, "Strike the rock with your staff" | 回忆当时，摩西为他的宗族求水。我们说： | PRESERVED |
| 2:63 (PRESERVED) | 0 | And when We took your covenant, and raised the Mount above you: | 回忆当时，我们接受了你们的盟约， | PRESERVED |
| 2:63 (PRESERVED) | 1 | "Hold to what We gave you with strength, and remember what is in it, so that you may be righteous." | 并把山悬在你们上方：“坚定地持守我们赐给你们的，记住其中的， | PRESERVED |
| 2:65 (PRESERVED) | 0 | And you knew those among you who transgressed on the Sabbath, so We said to them, "Be apes, despised." | 我们对他们说：“你们变成卑贱的猿吧！” | PRESERVED |
| 2:66 (PRESERVED) | 0 | So We made it a warning for what was before it and what came after it, and a lesson for the righteous. | 于是我们以它作为对他们当代和后代的警戒，以及对敬畏者的教训。 | PRESERVED |
| 2:73 (PRESERVED) | 0 | So We said, "Strike him with part of her." Thus God brings the dead to life, and shows you His signs, so that you may use reason. | 我们说：“用它的一部分击打他。 | PRESERVED |
| 2:83 (PRESERVED) | 0 | And when We took the covenant of the Children of Israel: | 我们曾与以色列的后裔立约：“你们只崇拜真主； | PRESERVED |
| 2:84 (PRESERVED) | 0 | And when We took your covenant: | 我们曾与你们立约：“你们不得流你们同胞的血， | PRESERVED |
| 2:87 (PRESERVED) | 0 | And We gave Moses the Book, and sent messengers after him in succession. | 我们把经典赐给摩西，在他之后派遣了一系列使者。 | PRESERVED |
| 2:87 (PRESERVED) | 1 | And We gave Jesus, son of Mary, the clear proofs, and strengthened him with the Holy Spirit. | 我们把经典赐给摩西，在他之后派遣了一系列使者。我们把明证赐给马利亚之子耶稣， | PRESERVED |
| 2:93 (PRESERVED) | 0 | And when We took your covenant, and raised the Mount above you: | 我们曾与你们立约，并把山悬在你们上方： | PRESERVED |
| 2:93 (PRESERVED) | 1 | "Hold to what We gave you with strength, and listen." They said, "We heard and we disobeyed." And the calf was poured into their hearts, for their disbelief. | “坚定地持守我们赐给你们的，听从。”他们说： | PRESERVED |
| 2:99 (PRESERVED) | 0 | And We sent down to you clear signs | 我们已降示给你明确的迹象，只有犯罪者否认它们。 | PRESERVED |
| 2:106 (PRESERVED) | 0 | Whatever sign We abolish or cause to be forgotten | 我们不废除一节，也不使它被遗忘， | PRESERVED |
| 2:106 (PRESERVED) | 1 | We bring one better than it, or like it. | 我们不废除一节，也不使它被遗忘，除非我们带来更好的或类似的。 | PRESERVED |
| 2:118 (PRESERVED) | 0 | We made the signs clear for a people who are certain. | ”他们之前的人也是这样说的。他们的心相似。我们已为笃信的人阐明迹象。 | PRESERVED |
| 2:119 (PRESERVED) | 0 | We sent you with the truth, a bringer of glad news and a warner | 我们确已派遣你带着真理——报喜、警告。 | PRESERVED |
| 2:121 (PRESERVED) | 0 | Those to whom We gave the Book recite it as it should be recited | 我们赐给经典的人如应诵读般诵读它——这些人信它。至于否认它的人——这些人是亏损者。 | PRESERVED |
| 2:125 (PRESERVED) | 0 | And when We made the House a place of return for the people, and a safe haven | 我们使天房成为人们的归向和安宁之所。以亚伯拉罕的立足地为礼拜处。 | PRESERVED |
| 2:125 (PRESERVED) | 1 | "And take from the standing-place of Abraham a place of prayer." And We charged Abraham and Ishmael: | 我们嘱托亚伯拉罕和以实玛利：“为环游者、静修者、 | PRESERVED |
| 2:130 (PRESERVED) | 0 | And We chose him in this world | 谁会背弃亚伯拉罕的宗教？我们在今世选择了他，在后世他必在敬畏者之列。 | PRESERVED |
| 2:143 (PRESERVED) | 0 | And thus We made you a middle community, so that you may be witnesses over the people, and the messenger a witness over you. | 我们就这样使你们成为中正的共同体，以便你们为人类作证， | PRESERVED |
| 2:143 (PRESERVED) | 1 | And We made the qibla you were facing only so We may know who follows the messenger from who turns back on his heels. | 使者为你们作证。我们只设立你们曾遵循的礼拜方向，以便区分追随使者的人和转身后退的人。 | PRESERVED |
| 2:144 (PRESERVED) | 0 | We see the turning of your face toward the sky | 我们确已看见你的脸转向天空。我们必使你转向你满意的方向。 | PRESERVED |
| 2:144 (PRESERVED) | 1 | so We will turn you to a qibla that will please you. | 我们确已看见你的脸转向天空。我们必使你转向你满意的方向。所以把你的脸转向禁寺。 | PRESERVED |
| 2:146 (PRESERVED) | 0 | Those to whom We gave the Book know it as they know their sons. | 我们赐给经典的人认识它，如同认识自己的儿女。 | PRESERVED |
| 2:151 (PRESERVED) | 0 | Just as We sent among you a messenger from you, reciting to you Our signs, and purifying you, and teaching you the Book and the wisdom, and teaching you what you did not know. | 正如我们派遣给你们一位你们自己的使者，向你们诵读我们的迹象， | PRESERVED |
| 2:155 (PRESERVED) | 0 | And We will surely try you with something of fear and hunger, and loss of wealth and lives and fruits. | 我们必以恐惧、饥饿、 | PRESERVED |
| 2:159 (PRESERVED) | 0 | Those who hide what We sent down of the clear proofs and the guidance, after We made it clear for the people in the Book | 那些隐瞒我们降示的明证和引导的人，在我们已在经典中向人类阐明之后——这些人——真主诅咒他们， | PRESERVED |
| 2:172 (PRESERVED) | 0 | O you who believe, eat from the good things We provided you, and give thanks to God, if it is Him you worship. | 信道的人们啊！吃我们赐给你们的佳美食物，感谢真主， | PRESERVED |
| 2:211 (PRESERVED) | 0 | Ask the Children of Israel how many a clear sign We gave them. | 你问以色列的后裔，我们给了他们多少明证。 | PRESERVED |
| 2:252 (PRESERVED) | 0 | We recite them to you with the truth. | 这些是真主的迹象，我们真实地诵读给你。 | PRESERVED |
| 2:253 (PRESERVED) | 0 | We favored some of them over others. | 这些使者：我们使一些优于另一些。 | PRESERVED |
| 2:253 (PRESERVED) | 1 | And We gave Jesus, son of Mary, the clear proofs, and strengthened him with the Holy Spirit. | 真主与其中一些直接说话，使一些品级升高。我们把明证赐给马利亚之子耶稣， | PRESERVED |
| 2:254 (PRESERVED) | 0 | O you who believe, spend from what We provided you | 信道的人们啊！在既无买卖、又无友谊、 | PRESERVED |
| 2:259 (PRESERVED) | 0 | And We will make you a sign for the people. | 看你的食物和饮料——没有变质——看你的驴。我们要使你成为人类的奇观。看骨头， | PRESERVED |
| 2:259 (PRESERVED) | 1 | how We raise them | 我们怎样组合它们，然后给它们穿上肉。”当他明白了， | PRESERVED |
| 2:259 (PRESERVED) | 2 | then We clothe them with flesh." Then when it became clear to him, he said, "I know that God has power over all things." | 我们怎样组合它们，然后给它们穿上肉。”当他明白了， | PRESERVED |
| 2:267 (PRESERVED) | 0 | O you who believe, spend from the good things you earned, and from what We brought out for you from the earth. | 信道的人们啊！施舍你们所赚的佳美之物，和我们为你们从大地生产之物。 | PRESERVED |

### Surah 3

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 3:11 (PRESERVED) | 0 | Like the way of Pharaoh's people and those before them: they denied Our signs, so God seized them for their sins, and God is severe in retribution. | 如法老的宗族和他们之前的人的行径。他们否认我们的迹象，于是真主因他们的罪惩罚了他们。 | PRESERVED |
| 3:25 (PRESERVED) | 0 | So how will it be when We gather them for a Day there is no doubt about, and every soul is paid in full for what it earned, and they will not be wronged? | 当我们在无疑的一日集合他们，每个灵魂将因她的所获得到全额报酬， | PRESERVED |
| 3:44 (PRESERVED) | 0 | That is some of the news of the unseen We reveal to you. | 这些是幽玄的消息，我们启示给你。当他们掷签决定谁照管马利亚时， | PRESERVED |
| 3:58 (PRESERVED) | 0 | This is what We recite to you of the signs and the wise Reminder. | 这是我们诵读给你的节和睿智的记念。 | PRESERVED |
| 3:108 (PRESERVED) | 0 | We recite them to you in truth. | 这些是真主的启示。我们真实地诵读给你。 | PRESERVED |
| 3:118 (PRESERVED) | 0 | We have made the signs clear to you, if you use reason. | 但他们心中隐瞒的更恶。我们已为你们阐明信息，如果你们理解。 | PRESERVED |
| 3:140 (PRESERVED) | 0 | These are the days We turn among people, so God may know those who believe, and take witnesses from among you. | 类似的创伤已降临他人。我们在人们之间轮换这样的日子，以便真主知道信道的人， | PRESERVED |
| 3:145 (PRESERVED) | 0 | We give him some of it; | 在预定的时间。谁想要今世的报酬，我们给他一些； | PRESERVED |
| 3:145 (PRESERVED) | 1 | We give him some of it. | 谁想要后世的报酬，我们给他一些；我们将报答感恩者。 | PRESERVED |
| 3:145 (PRESERVED) | 2 | And We will reward the thankful. | 我们给他一些；我们将报答感恩者。 | PRESERVED |
| 3:147 (PRESERVED) | 0 | Their only words were: Our Lord, forgive us our sins and our going too far in our affairs, and make our feet firm, and help us against the disbelieving people. | 他们的话只是：“我们的主啊， | PRESERVED |
| 3:151 (PRESERVED) | 0 | We will cast dread into the hearts of those who disbelieve, because they gave God partners for which He sent down no authority. | 我们将把恐怖投入不信道者的心，因为他们把真主未降示任何凭据的伙伴归于真主。 | PRESERVED |
| 3:178 (PRESERVED) | 0 | Let those who disbelieve not think that Our giving them more time is good for them. | 不信道者不要以为我们宽限他们是对他们好。其实， | PRESERVED |
| 3:178 (PRESERVED) | 1 | We only give them more time so they pile up more sin | 不信道者不要以为我们宽限他们是对他们好。其实，我们只宽限他们以便他们增加罪恶。 | PRESERVED |
| 3:181 (PRESERVED) | 0 | We will write down what they said, and their killing of the prophets without right | 我们富裕”的人的话。我们将记录他们说的，和他们枉杀先知； | PRESERVED |
| 3:181 (PRESERVED) | 1 | and We will say: Taste the punishment of the burning. | 我们将说：“尝火烧的刑罚吧。” | PRESERVED |
| 3:191 (PRESERVED) | 0 | Those who remember God standing, sitting, and on their sides, and think about the making of the heavens and the earth: Our Lord, You did not make this for nothing | 他们思考天地的创造：“我们的主啊，你没有徒然创造这个， | PRESERVED |

### Surah 4

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 4:18 (PRESERVED) | 0 | We have prepared for them a painful punishment. | “现在我忏悔”，也不为死于不信的人。这些——我们为他们准备了痛苦的刑罚。 | PRESERVED |
| 4:30 (PRESERVED) | 0 | We will roast him in a Fire. | 谁出于敌对和不义那样做，我们将把他投入火狱。那对真主是容易的。 | PRESERVED |
| 4:31 (PRESERVED) | 0 | We will wipe away your bad deeds, and bring you in through a noble entrance. | 如果你们避免被禁止的最恶的，我们将赦你们的罪，使你们进入尊贵的门。 | PRESERVED |
| 4:33 (PRESERVED) | 0 | For everyone We have set heirs for what parents and close kin leave. | 每个人，我们都为父母亲属遗留的指定了受益人。 | PRESERVED |
| 4:37 (PRESERVED) | 0 | We have prepared for the disbelievers a humiliating punishment. | 劝人吝啬、隐瞒真主出于他的恩惠赐给他们的人。我们为不信道者准备了羞辱的刑罚。 | PRESERVED |
| 4:41 (PRESERVED) | 0 | How will it be when We bring a witness from every community, and bring you as a witness over these? | 当我们从每个共同体带来见证人，带来你作为对这些人的见证， | PRESERVED |
| 4:47 (PRESERVED) | 0 | believe in what We sent down, confirming what you have, before We wipe out faces and turn them backward, or curse them as We cursed the people of the Sabbath. | 曾受经典的人们啊！信我们降示的，证实你们所有的， | PRESERVED |
| 4:54 (PRESERVED) | 0 | We gave the family of Abraham the Scripture and the wisdom | 难道他们嫉妒人们，因为真主出于他的恩惠赐给他们吗？我们已把经典和智慧赐给亚伯拉罕的家族， | PRESERVED |
| 4:54 (PRESERVED) | 1 | and We gave them a great kingdom. | 我们已把经典和智慧赐给亚伯拉罕的家族，我们已赐给他们伟大的主权。 | PRESERVED |
| 4:56 (PRESERVED) | 0 | Those who disbelieve in Our signs | 否认我们迹象的人——我们将在火中烧灼他们。每当他们的皮被烤熟， | PRESERVED |
| 4:56 (PRESERVED) | 1 | We will roast them in a Fire. | 否认我们迹象的人——我们将在火中烧灼他们。每当他们的皮被烤熟，我们就换给他们别的皮， | PRESERVED |
| 4:56 (PRESERVED) | 2 | We will replace them with other skins, so they taste the punishment. | 我们就换给他们别的皮，以便他们尝刑罚。真主是万能的、 | PRESERVED |
| 4:57 (PRESERVED) | 0 | We will bring them into Gardens with rivers running under them, staying in them forever. | 至于信道且行善的人，我们将使他们进入河水流淌其下的乐园， | PRESERVED |
| 4:57 (PRESERVED) | 1 | and We will bring them into deep shade. | 他们在其中有纯洁的配偶，我们将使他们进入浓密的荫凉。 | PRESERVED |
| 4:62 (PRESERVED) | 0 | How will it be when a blow strikes them for what their hands sent ahead, then they come to you swearing by God: We wanted only kindness and reconciliation? | 凭真主发誓：“我们只想善意和和解”，那会怎样？ | PRESERVED |
| 4:64 (PRESERVED) | 0 | We sent no messenger except to be obeyed by God's leave. | 我们派遣任何使者，只为奉真主的许可被顺从。 | PRESERVED |
| 4:66 (PRESERVED) | 0 | If We had written for them: Kill yourselves, or: Leave your homes | 假若我们为他们规定：“杀死你们自己”， | PRESERVED |
| 4:67 (PRESERVED) | 0 | Then We would have given them from Ourselves a great wage. | 我们必从我们这里给他们丰厚的报酬。 | PRESERVED |
| 4:68 (PRESERVED) | 0 | And We would have guided them along a straight path. | 我们必引导他们走上正路。 | PRESERVED |
| 4:74 (PRESERVED) | 0 | We will give him a great wage. | 然后被杀或获胜，我们将给他重大的报酬。 | PRESERVED |
| 4:79 (PRESERVED) | 0 | We sent you to people as a messenger. | 降临你的坏来自你自己。我们派遣你作为给人类的使者，真主足为见证者。 | PRESERVED |
| 4:80 (PRESERVED) | 0 | We did not send you as a keeper over them. | 谁顺从使者就是顺从真主。谁背离——我们没有派遣你做他们的监视者。 | PRESERVED |
| 4:91 (PRESERVED) | 0 | Over these We have given you a clear warrant. | 处决他们。对这些人，我们已给你们明确的授权。 | PRESERVED |
| 4:105 (PRESERVED) | 0 | We sent down to you the Scripture with the truth, so you judge between people by what God showed you. | 我们已降示给你经典带着真理，以便你按真主指示你的在人们之间判决。 | PRESERVED |
| 4:114 (PRESERVED) | 0 | We will give him a great wage. | 谁为求真主的喜悦那样做，我们将给他重大的报酬。 | PRESERVED |
| 4:115 (PRESERVED) | 0 | We will leave him to what he turned to, and roast him in Hell | 追随信道者之路外的，就让他走向他选择的，我们把他投入火狱——那归宿真恶劣！ | PRESERVED |
| 4:122 (PRESERVED) | 0 | We will bring them into Gardens with rivers running under them, staying in them forever. | 至于信道且行善的人，我们将使他们进入河水流淌其下的乐园， | PRESERVED |
| 4:131 (PRESERVED) | 0 | We charged those given the Scripture before you, and you, to fear God. | 天地间的一切属于真主。我们已命令你们之前曾受经典的人，和你们， | PRESERVED |
| 4:151 (PRESERVED) | 0 | And We have prepared for the disbelievers a humiliating punishment. | 这些人是真正的不信道者。我们为不信道者准备了羞辱的刑罚。 | PRESERVED |
| 4:153 (PRESERVED) | 0 | But We pardoned that | 即使明证已降临他们。但我们宽恕了那，我们给了摩西明确的权柄。 | PRESERVED |
| 4:153 (PRESERVED) | 1 | and We gave Moses a clear warrant. | 但我们宽恕了那，我们给了摩西明确的权柄。 | PRESERVED |
| 4:154 (PRESERVED) | 0 | And We raised the mountain over them for their pledge | 我们按他们的约把山悬在他们上方，我们对他们说： | PRESERVED |
| 4:154 (PRESERVED) | 1 | and We said to them: Enter the gate bowing low. | 我们按他们的约把山悬在他们上方，我们对他们说：“谦卑地进城门”， | PRESERVED |
| 4:154 (PRESERVED) | 2 | And We said to them: Do not break the Sabbath. | “谦卑地进城门”，我们对他们说：“不要违反安息日”， | PRESERVED |
| 4:154 (PRESERVED) | 3 | And We took from them a firm pledge. | 我们对他们说：“不要违反安息日”，我们接受了他们庄严的约。 | PRESERVED |
| 4:160 (PRESERVED) | 0 | We forbade them good things that had been lawful for them | 因犹太人的不义，我们禁止他们曾合法的佳美食物； | PRESERVED |
| 4:161 (PRESERVED) | 0 | We have prepared for the disbelievers among them a painful punishment. | 尽管被禁止；因他们不义地吞食人们的财产。我们为他们中的不信道者准备了痛苦的刑罚。 | PRESERVED |
| 4:162 (PRESERVED) | 0 | We will give them a great wage. | 交纳天课的人，信真主和末日的人——我们将给这些人巨大的报酬。 | PRESERVED |
| 4:163 (PRESERVED) | 0 | We inspired you as We inspired Noah and the prophets after him. | 我们已启示你，如我们启示挪亚和他之后的先知。 | PRESERVED |
| 4:163 (PRESERVED) | 1 | And We inspired Abraham and Ishmael and Isaac and Jacob and the Patriarchs, and Jesus and Job and Jonah and Aaron and Solomon. | 我们启示亚伯拉罕、以实玛利、以撒、 | PRESERVED |
| 4:163 (PRESERVED) | 2 | And We gave David psalms. | 约拿、亚伦和所罗门。我们把诗篇赐给大卫。 | PRESERVED |
| 4:164 (PRESERVED) | 0 | Messengers We already told you about before, and messengers We did not tell you about. | 有些使者我们已告诉你，有些使者我们没告诉你。 | PRESERVED |
| 4:174 (PRESERVED) | 0 | and We sent down to you a clear light. | 众人啊！来自你们主的证据已来到你们，我们降示给你们了明确的光。 | PRESERVED |

### Surah 5

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 5:10 (PRESERVED) | 0 | Those who disbelieve and deny Our signs | 至于不信道并否认我们迹象的人——他们是火狱的居民。 | PRESERVED |
| 5:12 (PRESERVED) | 0 | and We raised among them twelve chiefs. | 真主曾与以色列的后裔立约，我们在他们中选出十二位首领。真主说： | PRESERVED |
| 5:13 (PRESERVED) | 0 | We cursed them, and made their hearts hard. | 因为他们破坏盟约，我们弃绝了他们，使他们的心变硬。 | PRESERVED |
| 5:14 (PRESERVED) | 0 | And from those who said: We are Christians | 那些说“我们是基督教徒”的人，我们也曾与他们立约， | PRESERVED |
| 5:14 (PRESERVED) | 1 | We took their pledge, but they forgot a share of what they were reminded of. | 那些说“我们是基督教徒”的人，我们也曾与他们立约， | PRESERVED |
| 5:14 (PRESERVED) | 2 | So We stirred up enmity and hatred among them until the Day of Resurrection. | 我们也曾与他们立约，但他们忘记了他们被提醒的一部分。所以我们使他们之间直到复活日都充满敌意和仇恨； | PRESERVED |
| 5:15 (PRESERVED) | 0 | Our Messenger has come to you, making clear to you much of what you hid of the Scripture, and passing over much. | 有经人啊！我们的使者已来到你们， | PRESERVED |
| 5:19 (PRESERVED) | 0 | Our Messenger has come to you, making things clear to you after a break between messengers | 有经人啊！在使者中断之后， | PRESERVED |
| 5:24 (PRESERVED) | 0 | We are sitting right here. | 你和你的主去战斗吧。我们就坐在这里。” | PRESERVED |
| 5:32 (PRESERVED) | 0 | For that We laid down for the Children of Israel: whoever kills a soul | 因此我们为以色列的后裔规定：谁杀害一个人——除非为抵命或为在大地上作恶——就如同杀害了全人类； | PRESERVED |
| 5:32 (PRESERVED) | 1 | Our messengers came to them with clear proofs, but after that many of them went too far in the land. | 就如同救活了全人类。我们的使者们已带着明证来到他们，但即使在那之后， | PRESERVED |
| 5:41 (PRESERVED) | 0 | do not let those who race into disbelief sadden you: those who say with their mouths We believe, but their hearts do not believe; | 不要让那些急于不信道的人使你悲伤——他们中有人口头说“我们信”，但心里不信；犹太教徒中有——专听谎言的人， | PRESERVED |
| 5:44 (PRESERVED) | 0 | We sent down the Torah, with guidance and light in it. | 我们确已降示讨拉特，其中有引导和光明。 | PRESERVED |
| 5:45 (PRESERVED) | 0 | We wrote for them in it: a life for a life, an eye for an eye, a nose for a nose, an ear for an ear, a tooth for a tooth, and wounds in equal measure. | 我们在其中为他们规定：以命抵命， | PRESERVED |
| 5:46 (PRESERVED) | 0 | We sent Jesus son of Mary on their tracks, confirming what came before him of the Torah. | 在他们之后，我们派遣马利亚之子耶稣， | PRESERVED |
| 5:46 (PRESERVED) | 1 | And We gave him the Gospel, with guidance and light in it, confirming what came before it of the Torah, and guidance and a lesson for the righteous. | 我们派遣马利亚之子耶稣，证实他之前的讨拉特；我们赐给他引支勒， | PRESERVED |
| 5:48 (PRESERVED) | 0 | We sent down to you the Scripture with the truth, confirming what came before it of the Scripture, and a guardian over it. | 我们已向你降示这部经典，带着真理， | PRESERVED |
| 5:48 (PRESERVED) | 1 | For each of you We set a law and a way. | 不要追随他们的私欲而偏离已降临你的真理。我们为你们每个人都制定了律法和道路。如果真主意欲， | PRESERVED |
| 5:64 (PRESERVED) | 0 | And We cast enmity and hatred between them until the Day of Resurrection. | 他随意施予。从你的主降示给你的确会增加他们中许多人的悖逆和不信。我们在他们之间放置了敌意和仇恨， | PRESERVED |
| 5:65 (PRESERVED) | 0 | We would have wiped away their bad deeds, and brought them into the Gardens of bliss. | 假若有经人信道并敬畏，我们必赦免他们的罪，必让他们进入幸福的乐园。 | PRESERVED |
| 5:70 (PRESERVED) | 0 | We took the pledge of the Children of Israel, and sent messengers to them. | 我们确曾与以色列的后裔立约，并向他们派遣使者们。 | PRESERVED |
| 5:75 (PRESERVED) | 0 | See how We make the signs clear to them | 他们俩都吃食物。你看我们如何向他们阐明启示；再看他们是如何被误导的。 | PRESERVED |
| 5:86 (PRESERVED) | 0 | Those who disbelieve and deny Our signs | 但至于不信道并否认我们迹象的人——他们是火狱的居民。 | PRESERVED |
| 5:92 (PRESERVED) | 0 | Our Messenger's only duty is clear delivery. | 服从使者，要谨慎。如果你们转身离去——要知道我们使者的职责只是明确的传达。 | PRESERVED |
| 5:106 (PRESERVED) | 0 | If you doubt, let them swear by God: We will not sell it for a price, even if he were close kin, and we will not hide God's testimony | 让他们以真主发誓：“我们不为任何代价出卖我们的证词，即使他是近亲， | PRESERVED |
| 5:107 (PRESERVED) | 0 | and they swear by God: Our testimony is truer than their testimony, and we did not overstep | 让他们以真主发誓：“我们的证词比他们的证词更真实，我们不偏袒， | PRESERVED |

### Surah 6

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 6:6 (PRESERVED) | 0 | Did they not see how many peoples We destroyed before them? | 他们难道没想过在他们之前我们毁灭了多少世代？我们曾使他们在大地上比使你们更稳固， | PRESERVED |
| 6:6 (PRESERVED) | 1 | We settled them on earth as We never settled you, sent the sky pouring down on them, and set rivers flowing beneath them | 他们难道没想过在他们之前我们毁灭了多少世代？我们曾使他们在大地上比使你们更稳固，我们曾使云降下丰沛的雨给他们， | PRESERVED |
| 6:6 (PRESERVED) | 2 | then We destroyed them for their sins, and raised up other peoples after them. | 我们曾使诸河流淌在他们之下。但我们因他们的罪毁灭了他们，并在他们之后建立了其他文明。 | PRESERVED |
| 6:7 (PRESERVED) | 0 | Had We sent down to you a book on parchment, and they touched it with their hands, the disbelievers would still say, "This is nothing but clear sorcery." | 假若我们给你降下一部写在纸上的经典，而他们亲手触摸它， | PRESERVED |
| 6:8 (PRESERVED) | 0 | They said, "Why was no angel sent down to him?" Had We sent down an angel, the matter would have been settled | 他们说：“为什么没有天使降临他？”假若我们降下一位天使， | PRESERVED |
| 6:9 (PRESERVED) | 0 | Had We made him an angel | 假若我们使他成为天使，我们必使他成为人， | PRESERVED |
| 6:9 (PRESERVED) | 1 | We would have made him a man | 假若我们使他成为天使，我们必使他成为人， | PRESERVED |
| 6:9 (PRESERVED) | 2 | and We would have confused them with what already confuses them. | 假若我们使他成为天使，我们必使他成为人，使他们更加困惑。 | PRESERVED |
| 6:20 (PRESERVED) | 0 | Those We gave the Book know him as they know their own sons. | 我们赐予这部经典的人，认识它如同认识自己的孩子； | PRESERVED |
| 6:22 (PRESERVED) | 0 | On the Day We gather them all together | 在那日我们把他们全体集合，然后对多神教徒说： | PRESERVED |
| 6:22 (PRESERVED) | 1 | We will say to those who associated others with God: Where are your partners | 在那日我们把他们全体集合，然后对多神教徒说：“你们曾妄称的偶像在哪里？ | PRESERVED |
| 6:25 (PRESERVED) | 0 | but We laid covers over their hearts, lest they understand it, and deafness in their ears. | 他们中有听你的人；但我们在他们心上放置覆盖物，免得他们理解它， | PRESERVED |
| 6:33 (PRESERVED) | 0 | We know what they say grieves you. | 我们知道他们所说的使你悲伤。他们否认的不是你， | PRESERVED |
| 6:34 (PRESERVED) | 0 | and they endured being called liars and being hurt, until Our help came to them. | 但他们忍受否认和迫害，直到我们的援助降临他们。真主的话不可更改。 | PRESERVED |
| 6:38 (PRESERVED) | 0 | We left nothing out of the Book | 天上没有一只用翅膀飞翔的鸟，不是像你们一样的群体。我们在经典中没有遗漏任何事物。 | PRESERVED |
| 6:39 (PRESERVED) | 0 | Those who denied Our signs are deaf and dumb, in darkness. | 否认我们启示的人是聋的、哑的， | PRESERVED |
| 6:42 (PRESERVED) | 0 | We sent messengers to communities before you | 我们确曾向你之前的民族派遣使者们，我们以苦难和艰辛折磨他们， | PRESERVED |
| 6:42 (PRESERVED) | 1 | then We seized them with hardship and suffering, so they might humble themselves. | 我们确曾向你之前的民族派遣使者们，我们以苦难和艰辛折磨他们，以便他们谦卑。 | PRESERVED |
| 6:43 (PRESERVED) | 0 | If only, when Our might came to them, they had humbled themselves | 但愿当我们的灾难降临他们时，他们谦卑了。 | PRESERVED |
| 6:44 (PRESERVED) | 0 | We opened to them the doors of all things | 然后，当他们忘记被提醒的，我们为他们打开万物之门。 | PRESERVED |
| 6:44 (PRESERVED) | 1 | We seized them suddenly | 我们突然抓住他们；顿时，他们陷入绝望。 | PRESERVED |
| 6:46 (PRESERVED) | 0 | Look how We turn the signs about | 除真主外哪位神明能把它们还给你们？”你看我们如何多方面阐明显迹，而他们仍转身离去。 | PRESERVED |
| 6:48 (PRESERVED) | 0 | We send messengers only as bearers of good news and warners. | 我们只派遣使者们作为报喜者和警告者。凡信道并改正的人， | PRESERVED |
| 6:49 (PRESERVED) | 0 | Those who denied Our signs | 但至于否认我们启示的人，刑罚将因他们的悖逆而降临他们。 | PRESERVED |
| 6:53 (PRESERVED) | 0 | So We tested some of them by others, that they say, "Are these the ones God favored among us?" Is God not most knowing of the thankful? | 我们这样以他们中的一些人考验另一些人，以便他们说： | PRESERVED |
| 6:54 (PRESERVED) | 0 | When those who believe in Our signs come to you, say: Peace be upon you. | 当信仰我们启示的人来见你，你说： | PRESERVED |
| 6:55 (PRESERVED) | 0 | So We spell out the signs | 我们这样阐明显迹，揭露犯罪者的道路。 | PRESERVED |
| 6:61 (PRESERVED) | 0 | until, when death comes to one of you, Our messengers take him, and they never fall short. | 直到死亡降临你们中的一人，我们的使者们收取他，他们从不失职。 | PRESERVED |
| 6:65 (PRESERVED) | 0 | Look how We turn the signs about, so they may understand. | 你看我们如何阐明显迹，以便他们理解。” | PRESERVED |
| 6:68 (PRESERVED) | 0 | When you see those who plunge into Our signs, turn away from them until they plunge into some other talk. | 当你遇到妄谈我们启示的人，避开他们， | PRESERVED |
| 6:75 (PRESERVED) | 0 | So We showed Abraham the dominion of the heavens and the earth | 我们这样向亚伯拉罕展示天地的国度，以便他成为确信者中的一员。 | PRESERVED |
| 6:83 (PRESERVED) | 0 | That is Our argument | 那是我们赐给亚伯拉罕驳斥他族人的论证。我们随意提升人的品级。 | PRESERVED |
| 6:83 (PRESERVED) | 1 | We gave it to Abraham against his people. | 那是我们赐给亚伯拉罕驳斥他族人的论证。我们随意提升人的品级。 | PRESERVED |
| 6:83 (PRESERVED) | 2 | We raise in rank whom We will. | 我们随意提升人的品级。你的主是至睿的、全知的。 | PRESERVED |
| 6:84 (PRESERVED) | 0 | We gave him Isaac and Jacob | 我们赐给他以撒和雅各——我们引导了他们每一个。我们以前引导了挪亚； | PRESERVED |
| 6:84 (PRESERVED) | 1 | each We guided. | 我们赐给他以撒和雅各——我们引导了他们每一个。我们以前引导了挪亚；以及他的后裔中的大卫、 | PRESERVED |
| 6:84 (PRESERVED) | 2 | Noah We guided before | 我们以前引导了挪亚；以及他的后裔中的大卫、所罗门、 | PRESERVED |
| 6:84 (PRESERVED) | 3 | So We repay those who do good. | 约瑟、摩西和亚伦。我们这样报酬行善者。 | PRESERVED |
| 6:86 (PRESERVED) | 0 | each We favored above the worlds. | 还有以实玛利、以利亚、约拿和罗得——我们使他们每一个都超越世人。 | PRESERVED |
| 6:87 (PRESERVED) | 0 | We chose them, and guided them to a straight path. | 还有他们的祖先、后裔和兄弟们——我们拣选了他们，引导他们走上正路。 | PRESERVED |
| 6:89 (PRESERVED) | 0 | Those are the ones We gave the Book, judgment, and prophethood. | 那些是我们赐予这部经典、智慧和先知职位的人。 | PRESERVED |
| 6:89 (PRESERVED) | 1 | We have entrusted it to a people who do not disbelieve in it. | 智慧和先知职位的人。如果这些人否认它们，我们已把它们托付给不否认它们的人。 | PRESERVED |
| 6:92 (PRESERVED) | 0 | This is a blessed Book We sent down, confirming what came before it | 这也是一部我们降示的经典——吉庆的——证实它之前的，以便你警告众城之母及其周围。 | PRESERVED |
| 6:94 (PRESERVED) | 0 | You have come to Us alone, as We created you the first time | “你们确已单独来到我们，如同我们初次创造你们， | PRESERVED |
| 6:94 (PRESERVED) | 1 | leaving behind your backs what We granted you. | 如同我们初次创造你们，抛下我们赐予你们的一切。我们看不到你们的说情者与你们同在——那些你们妄称的伙伴。 | PRESERVED |
| 6:94 (PRESERVED) | 2 | We do not see with you your intercessors | 如同我们初次创造你们，抛下我们赐予你们的一切。我们看不到你们的说情者与你们同在——那些你们妄称的伙伴。 | PRESERVED |
| 6:97 (PRESERVED) | 0 | We spelled out the signs for people who know. | 是他为你们创造星辰，以便你们在陆地和海洋的黑暗中以它们为引导。我们这样为有知识的人阐明显迹。 | PRESERVED |
| 6:98 (PRESERVED) | 0 | We spelled out the signs for people who understand. | 然后是一个居所，然后是一个寄存处。我们已为理解的人详述显迹。 | PRESERVED |
| 6:99 (PRESERVED) | 0 | then We brought out with it the growth of all things | 是他从天上降下水。我们以它生出各种植物， | PRESERVED |
| 6:99 (PRESERVED) | 1 | then We brought out from it green stalks, from which We bring out clustered grain | 我们以它生出各种植物，从中生出绿苗，从中生出成串的谷物。 | PRESERVED |
| 6:105 (PRESERVED) | 0 | So We turn the signs about | 我们这样多方面阐明显迹，以免他们说“你学过”， | PRESERVED |
| 6:105 (PRESERVED) | 1 | and so We make it clear for people who know. | 我们这样多方面阐明显迹，以免他们说“你学过”，并为有知识的人阐明它们。 | PRESERVED |
| 6:107 (PRESERVED) | 0 | We did not make you a keeper over them | 假若真主意欲，他们就不会崇拜偶像。我们没有任命你做他们的监护者， | PRESERVED |
| 6:108 (PRESERVED) | 0 | So We made fair to every community their deeds | 以免他们出于敌意和无知辱骂真主。我们使每个民族的行为在他们看来美好。然后他们归于他们的主， | PRESERVED |
| 6:110 (PRESERVED) | 0 | We turn their hearts and their sight about | 我们转移他们的心和他们的视线，如同他们第一次拒绝信它， | PRESERVED |
| 6:110 (PRESERVED) | 1 | and We leave them wandering blindly in their rebellion. | 我们转移他们的心和他们的视线，如同他们第一次拒绝信它，我们任他们在悖逆中盲目前行。 | PRESERVED |
| 6:111 (PRESERVED) | 0 | Had We sent down the angels to them, and the dead spoke to them | 即使我们给他们降下天使，死者对他们说话， | PRESERVED |
| 6:111 (PRESERVED) | 1 | and We gathered all things before them face to face | 死者对他们说话，我们把万物集合在他们面前，他们仍不信， | PRESERVED |
| 6:112 (PRESERVED) | 0 | So We set for every prophet an enemy | 同样，我们为每位先知指定了敌人——人类和精灵中的恶魔——互相以花言巧语启示以欺骗。 | PRESERVED |
| 6:114 (PRESERVED) | 0 | Those We gave the Book know it was sent down from your Lord in truth | “难道我舍真主而另寻判决者吗，而他是向你们降示这部详尽经典的？”我们赐予这部经典的人知道它是从你的主降示的真理。 | PRESERVED |
| 6:122 (PRESERVED) | 0 | then We gave him life | 曾死去、然后我们使他复活、 | PRESERVED |
| 6:123 (PRESERVED) | 0 | So We set in every town its greatest criminals, to plot in it | 我们这样在每座城市中设立其首恶的罪人，在其中密谋， | PRESERVED |
| 6:126 (PRESERVED) | 0 | We spelled out the signs for people who remember. | 这是你的主的正路。我们已为记念的人详述显迹。 | PRESERVED |
| 6:129 (PRESERVED) | 0 | So We set some wrongdoers over others, for what they used to earn. | 我们这样使一些不义者互为朋友，因为他们所做的。 | PRESERVED |
| 6:146 (PRESERVED) | 0 | To those who are Jewish We forbade every clawed animal | 对犹太教徒，我们禁止一切有爪的。 | PRESERVED |
| 6:146 (PRESERVED) | 1 | and of cattle and sheep We forbade them their fat | 我们禁止一切有爪的。至于黄牛和绵羊：我们禁止它们的脂肪， | PRESERVED |
| 6:146 (PRESERVED) | 2 | That We repaid them for their insolence | 内脏的、或与骨头相连的。我们这样因他们的不义惩罚他们。 | PRESERVED |
| 6:146 (PRESERVED) | 3 | and We are truthful. | 我们这样因他们的不义惩罚他们。我们确是诚实的。 | PRESERVED |
| 6:148 (PRESERVED) | 0 | nor forbidden anything." So those before them called it a lie, until they tasted Our might. | 直到他们尝到我们的威力。你说：“你们有可拿给我们的知识吗？ | PRESERVED |
| 6:150 (PRESERVED) | 0 | and do not follow the whims of those who denied Our signs, and those who do not believe in the Hereafter | ”如果他们作证，你不要与他们一同作证。不要追随那些否认我们启示、 | PRESERVED |
| 6:151 (PRESERVED) | 0 | We provide for you and for them | 你们孝敬父母；你们不因贫穷杀害孩子——我们供给你们和他们；你们不接近丑事， | PRESERVED |
| 6:152 (PRESERVED) | 0 | We burden no soul beyond its capacity. | 公平给斗。我们不使任何灵魂负担超过其能力。当你们说话， | PRESERVED |
| 6:154 (PRESERVED) | 0 | Then We gave Moses the Book | 然后我们赐给摩西经典，对行善者是完备的， | PRESERVED |
| 6:155 (PRESERVED) | 0 | This is a blessed Book We sent down | 这也是一部我们降示的吉庆经典；所以追随它， | PRESERVED |
| 6:157 (PRESERVED) | 0 | We will repay those who turn away from Our signs with an evil punishment for their turning away. | 谁比否认真主的迹象、转身离去的人更不义？我们将因他们转身离去， | PRESERVED |

### Surah 7

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 7:4 (PRESERVED) | 0 | How many a town We destroyed | 我们毁灭了多少城镇？我们的威力在夜间降临他们， | PRESERVED |
| 7:4 (PRESERVED) | 1 | Our might came to it by night, or while they napped at noon. | 我们毁灭了多少城镇？我们的威力在夜间降临他们，或在他们午睡时。 | PRESERVED |
| 7:5 (PRESERVED) | 0 | Their only cry, when Our might came to them, was to say, "We were wrongdoers." | 当我们的威力降临他们，他们唯一的呼喊是：“我们确是不义者。 | PRESERVED |
| 7:6 (PRESERVED) | 0 | We will question those to whom messengers were sent | 我们必审问被派遣使者的人，我们必审问使者们。 | PRESERVED |
| 7:6 (PRESERVED) | 1 | and We will question the messengers. | 我们必审问被派遣使者的人，我们必审问使者们。 | PRESERVED |
| 7:7 (PRESERVED) | 0 | We will recount to them with knowledge | 我们必以知识向他们讲述，因为我们从未缺席。 | PRESERVED |
| 7:7 (PRESERVED) | 1 | and We were never absent. | 我们必以知识向他们讲述，因为我们从未缺席。 | PRESERVED |
| 7:9 (PRESERVED) | 0 | they lost their souls, for wronging Our signs. | 但秤轻的人——他们丧失了自身，因为他们曾亏待我们的启示。 | PRESERVED |
| 7:10 (PRESERVED) | 0 | We settled you on earth, and made for you in it livelihoods. | 我们确已使你们在大地上稳固，为你们在其中造生计——但你们很少感谢。 | PRESERVED |
| 7:11 (PRESERVED) | 0 | We created you, then fashioned you | 我们创造了你们，然后塑造你们， | PRESERVED |
| 7:26 (PRESERVED) | 0 | We sent down to you clothing to cover your nakedness | 亚当的子孙啊！我们确已供给你们衣服遮盖你们的身体， | PRESERVED |
| 7:27 (PRESERVED) | 0 | We made the devils allies of those who do not believe. | 向他们显露羞体。他和他的族类从你们看不见他们的地方看见你们。我们使恶魔成为不信道者的朋友。 | PRESERVED |
| 7:32 (PRESERVED) | 0 | So We spell out the signs for people who know. | 在今世，但复活日专归他们。”我们这样为有知识的人详述显迹。 | PRESERVED |
| 7:36 (PRESERVED) | 0 | Those who denied Our signs and puffed themselves up against them | 但至于否认我们启示、骄傲地拒绝它们的人——他们是火狱的居民， | PRESERVED |
| 7:37 (PRESERVED) | 0 | until, when Our messengers come to take them, they say, "Where are those you called on besides God?" They will say, "They strayed from us" | 直到我们的使者们降临他们、收取他们的灵魂，他们将说： | PRESERVED |
| 7:40 (PRESERVED) | 0 | Those who denied Our signs and puffed themselves up against them | 否认我们启示、傲慢地拒绝遵行它们的人——天门不会为他们打开， | PRESERVED |
| 7:40 (PRESERVED) | 1 | So We repay the guilty. | 直到骆驼穿过针眼。我们这样报应犯罪者。 | PRESERVED |
| 7:41 (PRESERVED) | 0 | So We repay the wrongdoers. | 他们头上有火被。我们这样报应不义者。 | PRESERVED |
| 7:42 (PRESERVED) | 0 | We burden no soul beyond its capacity | 至于信道并行善的人——我们不使任何灵魂负担超过其能力——他们是乐园的居民，永居其中。 | PRESERVED |
| 7:43 (PRESERVED) | 0 | We stripped what was in their hearts of rancor | 我们将除去他们心中的一切怨恨。诸河在他们之下流淌。 | PRESERVED |
| 7:44 (PRESERVED) | 0 | The people of the Garden will call to the people of the Fire: We found what our Lord promised us true | “我们发现我们主应许我们的是真实的；你们发现你们主应许你们的是真实的吗？”他们将说： | PRESERVED |
| 7:51 (PRESERVED) | 0 | Today We forget them, as they forgot the meeting of this Day of theirs | 把它当笑话、被今世生活欺骗的人。今天我们将忽视他们， | PRESERVED |
| 7:51 (PRESERVED) | 1 | and as they rejected Our signs. | 如同他们忽视今日的相会，他们曾否认我们的启示。 | PRESERVED |
| 7:52 (PRESERVED) | 0 | We brought them a Book | 我们确已给他们一部经典，我们以知识详述它——作为信道的人的引导和慈悯。 | PRESERVED |
| 7:52 (PRESERVED) | 1 | We detailed it with knowledge | 我们确已给他们一部经典，我们以知识详述它——作为信道的人的引导和慈悯。 | PRESERVED |
| 7:57 (PRESERVED) | 0 | We drive them to a dead land | 然后，当它们聚集起重云，我们把它们赶到一片死地， | PRESERVED |
| 7:57 (PRESERVED) | 1 | So We bring out the dead | 在那里降下水，以它生出各种果实。我们这样使死者复活——也许你们会反思。 | PRESERVED |
| 7:58 (PRESERVED) | 0 | So We turn the signs about for thankful people. | 至于劣田，只产出艰难和苦楚。我们这样多方面为感谢的人阐明显迹。 | PRESERVED |
| 7:59 (PRESERVED) | 0 | We sent Noah to his people. | 我们派遣挪亚到他的族人。他说： | PRESERVED |
| 7:64 (PRESERVED) | 0 | so We saved him and those with him in the Ark | 但他们说他说谎。所以我们拯救他和与他在方舟中的人， | PRESERVED |
| 7:64 (PRESERVED) | 1 | and drowned those who denied Our signs. | 所以我们拯救他和与他在方舟中的人，淹死否认我们启示的人。他们是盲目的人。 | PRESERVED |
| 7:72 (PRESERVED) | 0 | We saved him and those with him, by mercy from Us | 所以我们以来自我们的慈悯拯救他和与他同在的人，剪除否认我们启示、 | PRESERVED |
| 7:72 (PRESERVED) | 1 | and cut off the last remnant of those who denied Our signs. | 剪除否认我们启示、不信道的人的根。 | PRESERVED |
| 7:83 (PRESERVED) | 0 | We saved him and his family | 但我们拯救他和他的家人，除了他的妻子； | PRESERVED |
| 7:84 (PRESERVED) | 0 | We rained on them a rain | 我们给他们降下雨；看犯罪者的后果。 | PRESERVED |
| 7:89 (PRESERVED) | 0 | We would have invented a lie against God, if we returned to your way after God saved us from it. | “如果在真主拯救我们脱离它之后我们回到你们的宗教，我们就是在捏造关于真主的谎言。 | PRESERVED |
| 7:94 (PRESERVED) | 0 | We sent no prophet to any town but We seized its people with hardship and suffering, so they might humble themselves. | 我们没有向任何城镇派遣先知，而不以苦难和艰辛折磨其居民， | PRESERVED |
| 7:95 (PRESERVED) | 0 | Then We replaced the bad with the good | 然后我们以顺境代替逆境。直到他们增加， | PRESERVED |
| 7:95 (PRESERVED) | 1 | and We seized them suddenly, though they did not feel it. | 说：“苦难和顺境曾降临我们的祖先。”然后我们在他们不知情时突然抓住他们。 | PRESERVED |
| 7:96 (PRESERVED) | 0 | We would have opened on them blessings from the sky and the earth | 假若城镇的居民信道并敬畏，我们必为他们打开天地的吉庆；但他们否认真理， | PRESERVED |
| 7:96 (PRESERVED) | 1 | but they called it a lie, so We seized them for what they earned. | 但他们否认真理，所以我们因他们所做的抓住他们。 | PRESERVED |
| 7:97 (PRESERVED) | 0 | Did the towns' people feel safe from Our might coming to them by night, while they slept? | 城镇的居民确信我们的威力不会在夜间、他们睡觉时降临他们吗？ | PRESERVED |
| 7:98 (PRESERVED) | 0 | Or did the towns' people feel safe from Our might coming to them in the forenoon, while they played? | 城镇的居民确信我们的威力不会在白天、他们游戏时降临他们吗？ | PRESERVED |
| 7:100 (PRESERVED) | 0 | that had We willed | 这不是引导吗：如果我们意欲，我们能因他们的罪打击他们？ | PRESERVED |
| 7:100 (PRESERVED) | 1 | We would have struck them for their sins? | 这不是引导吗：如果我们意欲，我们能因他们的罪打击他们？ | PRESERVED |
| 7:100 (PRESERVED) | 2 | We seal their hearts | 我们能因他们的罪打击他们？封住他们的心，使他们听不见？ | PRESERVED |
| 7:101 (PRESERVED) | 0 | We recount to you some of their tidings. | 这些城镇——我们向你讲述它们的一些故事。他们的使者们带着明证来到他们， | PRESERVED |
| 7:102 (PRESERVED) | 0 | We found no covenant in most of them | 我们发现他们中的大多数不守盟约；我们发现他们中的大多数悖逆。 | PRESERVED |
| 7:102 (PRESERVED) | 1 | and We found most of them transgressors. | 我们发现他们中的大多数不守盟约；我们发现他们中的大多数悖逆。 | PRESERVED |
| 7:103 (PRESERVED) | 0 | Then We sent Moses after them, with Our signs, to Pharaoh and his chiefs | 然后，在他们之后， | PRESERVED |
| 7:117 (PRESERVED) | 0 | We revealed to Moses: Throw your staff. | 我们启示摩西：“扔下你的杖。 | PRESERVED |
| 7:130 (PRESERVED) | 0 | We seized Pharaoh's people with years of drought, and shortage of fruits | 我们确以荒年和庄稼歉收折磨法老的人，以便他们记取。 | PRESERVED |
| 7:133 (PRESERVED) | 0 | We sent on them the flood, the locusts, the lice, the frogs, and the blood | 于是我们给他们降下洪水、蝗虫、 | PRESERVED |
| 7:135 (PRESERVED) | 0 | When We lifted the plague from them | 但当我们为他们解除灾难，到他们应满的期限， | PRESERVED |
| 7:136 (PRESERVED) | 0 | We took revenge on them | 于是我们报复他们，把他们淹死在海里——因为他们否认我们的迹象， | PRESERVED |
| 7:136 (PRESERVED) | 1 | for denying Our signs, and being heedless of them. | 于是我们报复他们，把他们淹死在海里——因为他们否认我们的迹象，不理会它们。 | PRESERVED |
| 7:137 (PRESERVED) | 0 | We gave the oppressed people to inherit the easts of the earth and its wests | 我们使受压迫的人继承我们赐福的大地的东方和西方。你的主对以色列后裔的美好诺言实现了， | PRESERVED |
| 7:137 (PRESERVED) | 1 | which We blessed. | 我们使受压迫的人继承我们赐福的大地的东方和西方。你的主对以色列后裔的美好诺言实现了，因为他们忍耐。 | PRESERVED |
| 7:137 (PRESERVED) | 2 | We leveled what Pharaoh and his people built, and what they raised. | 因为他们忍耐。我们毁灭法老和他族人建造的，以及他们收获的。 | PRESERVED |
| 7:138 (PRESERVED) | 0 | We brought the Children of Israel across the sea | 我们使以色列的后裔渡过海。当他们遇到一群虔诚供奉他们偶像的人， | PRESERVED |
| 7:141 (PRESERVED) | 0 | When We saved you from Pharaoh's people | 记念我们如何拯救你们脱离法老的人，他们使你们遭受最坏的苦难——杀你们的儿子， | PRESERVED |
| 7:142 (PRESERVED) | 0 | We appointed for Moses thirty nights | 我们与摩西约定三十夜，以十夜补足； | PRESERVED |
| 7:143 (PRESERVED) | 0 | When Moses came to Our appointment, and his Lord spoke to him, he said: My Lord | 当摩西来到我们的约会，他的主对他说话， | PRESERVED |
| 7:145 (PRESERVED) | 0 | We wrote for him on the tablets | 我们在法版上为他写下各样劝诫和对万物的决定性解释。“紧握它们， | PRESERVED |
| 7:146 (PRESERVED) | 0 | That is for denying Our signs, and being heedless of them. | 就把它当作路。那是因为他们否认我们的启示，不理会它们。 | PRESERVED |
| 7:147 (PRESERVED) | 0 | Those who denied Our signs and the meeting of the Hereafter | 否认我们启示和后世相会的人——他们的行为将化为乌有。他们受的报应难道不是按他们所做的吗？ | PRESERVED |
| 7:152 (PRESERVED) | 0 | So We repay the inventors. | 和今世的卑贱。我们这样报应捏造者。 | PRESERVED |
| 7:155 (PRESERVED) | 0 | Moses chose seventy men from his people for Our appointment. | 摩西从他的族人中选出七十人赴我们的约会。当震动震撼他们，他说： | PRESERVED |
| 7:156 (PRESERVED) | 0 | I will ordain it for the righteous, who give the zakat, and who believe in Our signs. | 信仰我们迹象的人。” | PRESERVED |
| 7:160 (PRESERVED) | 0 | We divided them into twelve tribes | 我们把他们分成十二个部族群体。当他的族人向他要水喝， | PRESERVED |
| 7:160 (PRESERVED) | 1 | We revealed to Moses, when his people asked him for water: Strike the rock with your staff. | 我们把他们分成十二个部族群体。当他的族人向他要水喝，我们启示摩西： | PRESERVED |
| 7:160 (PRESERVED) | 2 | We shaded them with clouds, and sent down on them manna and quails. | 每群人都知道自己的饮水处。我们以云荫蔽他们，给他们降下甘露和鹌鹑： | PRESERVED |
| 7:160 (PRESERVED) | 3 | Eat of the good things We provided you. | 给他们降下甘露和鹌鹑：“吃我们供给你们的佳美之物。”他们没有亏待我们， | PRESERVED |
| 7:160 (PRESERVED) | 4 | They did not wrong Us | ”他们没有亏待我们，但他们亏待自己。 | PRESERVED |
| 7:161 (PRESERVED) | 0 | We will forgive your faults. | 谦逊地说，谦卑地进城门——我们将赦宥你们的罪，提升行善者。 | PRESERVED |
| 7:161 (PRESERVED) | 1 | We will increase those who do good. | 谦卑地进城门——我们将赦宥你们的罪，提升行善者。” | PRESERVED |
| 7:162 (PRESERVED) | 0 | so We sent on them a plague from the sky, for their wrongdoing. | 但他们中的不义者把给他们的话换成别的话；所以我们因他们的不义给他们从天上降下灾难。 | PRESERVED |
| 7:163 (PRESERVED) | 0 | So We tested them for their transgression. | 当他们不守安息日，鱼就不来。我们这样因他们违抗而考验他们。 | PRESERVED |
| 7:165 (PRESERVED) | 0 | We saved those who forbade evil | 然后，当他们忘记被提醒的，我们拯救禁止作恶的人， | PRESERVED |
| 7:166 (PRESERVED) | 0 | We said to them: Be apes | 当他们违抗禁令，我们对他们说：“变成卑贱的猿。 | PRESERVED |
| 7:168 (PRESERVED) | 0 | We scattered them across the earth as communities. | 我们把他们分散成大地上的群体。他们中有正直的， | PRESERVED |
| 7:168 (PRESERVED) | 1 | We tested them with good and bad | 有不及的。我们以顺境和逆境考验他们，以便他们回归。 | PRESERVED |
| 7:170 (PRESERVED) | 0 | We do not waste the reward of those who set things right. | 那些坚持经典、谨守礼拜的人——我们不浪费改正者的报酬。 | PRESERVED |
| 7:171 (PRESERVED) | 0 | When We raised the mountain above them, as if it were a canopy | 当我们把山悬在他们头上，如同一把伞， | PRESERVED |
| 7:171 (PRESERVED) | 1 | and they thought it would fall on them: Hold with strength what We gave you | “紧握我们赐予你们的，记念其中所含的，以便你们得救。 | PRESERVED |
| 7:172 (PRESERVED) | 0 | Lest you say on the Day of Resurrection: We were heedless of this. | “我们不知道这事。” | PRESERVED |
| 7:174 (PRESERVED) | 0 | So We spell out the signs | 我们这样详述显迹，以便他们回归。 | PRESERVED |
| 7:175 (PRESERVED) | 0 | Recite to them the tidings of the one We gave Our signs | 向他们讲述那个人的故事：我们把我们的迹象给他，但他脱离了它们， | PRESERVED |
| 7:176 (PRESERVED) | 0 | Had We willed | 假若我们意欲，我们本可以它们提升他； | PRESERVED |
| 7:176 (PRESERVED) | 1 | We would have raised him with them | 假若我们意欲，我们本可以它们提升他； | PRESERVED |
| 7:176 (PRESERVED) | 2 | That is the likeness of the people who denied Our signs. | 它也吐舌。否认我们迹象的人的比喻就是这样。所以讲述故事， | PRESERVED |
| 7:177 (PRESERVED) | 0 | Evil is the likeness of the people who denied Our signs | 否认我们迹象、亏待自身的人的比喻真恶劣。 | PRESERVED |
| 7:179 (PRESERVED) | 0 | We created many jinn and mankind for Hell. | 我们确已为火狱注定许多精灵和人类。他们有心却不理解。 | PRESERVED |
| 7:181 (PRESERVED) | 0 | Among those We created is a community | 在我们创造的人中有一个群体——他们以真理引导，并以此主持公道。 | PRESERVED |
| 7:182 (PRESERVED) | 0 | Those who denied Our signs | 至于否认我们迹象的人，我们将从他们不知道的地方逐渐引导他们。 | PRESERVED |
| 7:182 (PRESERVED) | 1 | We will lure them on, from where they do not know. | 至于否认我们迹象的人，我们将从他们不知道的地方逐渐引导他们。 | PRESERVED |

### Surah 8

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 8:3 (PRESERVED) | 0 | Who keep up the prayer, and give from what We provided them. | 从我们供给他们的中，他们施舍。 | PRESERVED |
| 8:19 (PRESERVED) | 0 | We will return. | 对你们最好。如果你们再来，我们再来； | PRESERVED |
| 8:31 (PRESERVED) | 0 | When Our signs are recited to them, they say, "We heard. | 当我们的启示被诵读给他们，他们说： | PRESERVED |
| 8:41 (PRESERVED) | 0 | if you believed in God and what We sent down on Our servant, on the Day of Distinction | 孤儿、穷人和旅行者，如果你们信仰真主和我们在辨别之日——两军相遇之日——降示给我们仆人的。 | PRESERVED |
| 8:54 (PRESERVED) | 0 | so We destroyed them for their sins, and drowned Pharaoh's people. | 他们否认他们主的迹象，所以我们因他们的不义毁灭他们，淹死法老的人——他们全是不义者。 | PRESERVED |
| 8:59 (FLATTENED) | 0 | Let not the disbelievers think they outran Us. | 不要让不信道者以为他们领先。他们逃不掉。 | FLATTENED |

### Surah 9

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 9:11 (PRESERVED) | 0 | We spell out the signs for people who know. | 完纳天课，他们就是你们信仰上的兄弟。我们为有知识的人详述启示。 | PRESERVED |
| 9:66 (PRESERVED) | 0 | If We pardon a group of you | 你们在信仰之后已不信。如果我们赦免你们中的一些，我们将惩罚另一些， | PRESERVED |
| 9:66 (PRESERVED) | 1 | We will punish a group | 如果我们赦免你们中的一些，我们将惩罚另一些，因为他们有罪。 | PRESERVED |
| 9:101 (PRESERVED) | 0 | We know them. | 你不认识他们，但我们认识他们。我们将惩罚他们两次； | PRESERVED |
| 9:101 (PRESERVED) | 1 | We will punish them twice | 你不认识他们，但我们认识他们。我们将惩罚他们两次； | PRESERVED |
| 9:107 (PRESERVED) | 0 | They will swear: We wanted only the best. | 他们将发誓：“我们的意图只是好的。”但真主见证他们是说谎者。 | PRESERVED |

### Surah 10

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 10:2 (PRESERVED) | 0 | Was it a wonder to the people that We inspired a man from among them: Warn the people, and give good news to those who believe | 人们难道觉得奇怪吗？我们从他们中间启示了一个人：“警告人类， | PRESERVED |
| 10:7 (PRESERVED) | 0 | Those who do not hope to meet Us, and are content with the worldly life, and rest easy in it | 那些不盼望与我们相会的人，满足于今世的生活， | PRESERVED |
| 10:7 (PRESERVED) | 1 | and those who are heedless of Our signs: | 在其中安然自得，对我们的迹象毫不在意。 | PRESERVED |
| 10:11 (PRESERVED) | 0 | But We leave those who do not hope to meet Us wandering blindly in their defiance. | 如果真主像他们急切祈求福利一样急切地给人类降下灾难，他们的期限早就到了。但我们让那些不盼望与我们相会的人在他们的过分中盲目游荡。 | PRESERVED |
| 10:12 (PRESERVED) | 0 | When adversity touches the human being, he calls on Us | 每当灾难触及人类，他便祈求我们——躺着、坐着、 | PRESERVED |
| 10:12 (PRESERVED) | 1 | Then, when We lift his adversity from him, he goes on as if he had never called on Us over an adversity that touched him. | 坐着、站着。但当我们为他解除灾难， | PRESERVED |
| 10:13 (PRESERVED) | 0 | We destroyed the generations before you when they did wrong. | 在你们之前，我们确已毁灭了几代人， | PRESERVED |
| 10:13 (PRESERVED) | 1 | Thus We repay the criminal people. | 但他们不肯信道。我们就这样报应犯罪的人。 | PRESERVED |
| 10:14 (PRESERVED) | 0 | Then We made you successors on the earth after them, to see how you would act. | 然后我们在他们之后使你们成为大地上的继承者，以便看你们的行为如何。 | PRESERVED |
| 10:15 (PRESERVED) | 0 | When Our signs are recited to them, clear, those who do not hope to meet Us say: Bring a Quran other than this, or change it. | 当我们的明证被诵读给他们，不盼望与我们相会的人说： | PRESERVED |
| 10:21 (PRESERVED) | 0 | When We let people taste mercy after hardship touched them, at once they scheme against Our signs. | 当我们在灾难触及人们之后使他们尝到仁慈，他们便开始针对我们的迹象施展诡计。 | PRESERVED |
| 10:21 (PRESERVED) | 1 | Our messengers write down what you plot. | 你说：“真主的计谋更快。”我们的使者确在记录你们的诡计。 | PRESERVED |
| 10:23 (PRESERVED) | 0 | Then to Us is your return | 你们的作恶只害你们自己。这是今世生活的享受。然后你们归于我们， | PRESERVED |
| 10:23 (PRESERVED) | 1 | and We will tell you what you used to do. | 这是今世生活的享受。然后你们归于我们，我们将告诉你们你们曾经的行为。 | PRESERVED |
| 10:24 (PRESERVED) | 0 | The example of the worldly life is like water We sent down from the sky, with which the plants of the earth mingled | 今世生活的比喻是：我们从天上降下的水被大地上的植物吸收，人和牲畜都吃它。 | PRESERVED |
| 10:24 (PRESERVED) | 1 | until, when the earth took its adornment and was decked out, and its people thought they had power over it, Our command came to it by night or by day | 它的居民以为自己已掌控了它，我们的命令在夜里或白天降临，我们使它变成残茬， | PRESERVED |
| 10:24 (PRESERVED) | 2 | and We made it like a mown field, as if it had not flourished the day before. | 我们的命令在夜里或白天降临，我们使它变成残茬，仿佛昨天从未繁茂过。 | PRESERVED |
| 10:24 (PRESERVED) | 3 | Thus We spell out the signs for people who reflect. | 我们使它变成残茬，仿佛昨天从未繁茂过。我们就这样为反省的人阐明迹象。 | PRESERVED |
| 10:28 (PRESERVED) | 0 | On the Day We gather them all | 在我们将他们全部聚集的那天，我们对以物配主的人说： | PRESERVED |
| 10:28 (PRESERVED) | 1 | then We will say to those who associated: Stay in your place, you and your partners. | 在我们将他们全部聚集的那天，我们对以物配主的人说：“各就各位吧， | PRESERVED |
| 10:28 (PRESERVED) | 2 | And We will separate them. | ”然后我们在他们之间隔开，他们的配主说：“你们崇拜的并不是我们。 | PRESERVED |
| 10:46 (PRESERVED) | 0 | Whether We show you some of what We promised them, or take you in death | 无论我们让你看到我们许诺他们的一部分，还是取你的生命， | PRESERVED |
| 10:46 (PRESERVED) | 1 | to Us is their return. | 还是取你的生命，他们都要归于我们。真主见证他们所做的一切。 | PRESERVED |
| 10:61 (PRESERVED) | 0 | but We are witnesses over you as you engage in it. | 无论你诵读什么古兰经，无论你做什么，当你着手时， | PRESERVED |
| 10:70 (PRESERVED) | 0 | then to Us is their return. | 今世的一点享受；然后归于我们； | PRESERVED |
| 10:70 (PRESERVED) | 1 | Then We will make them taste the severe torment for their disbelief. | 今世的一点享受；然后归于我们；然后我们将因他们的不信道而让他们尝到严厉的刑罚。 | PRESERVED |
| 10:73 (PRESERVED) | 0 | They called him a liar, so We saved him and those with him in the Ark, and made them successors, and drowned those who denied Our signs. | 但他们否认了他，于是我们拯救了他和方舟上与他同在的人， | PRESERVED |
| 10:74 (PRESERVED) | 0 | Then after him We sent messengers to their peoples. | 然后，在他之后， | PRESERVED |
| 10:74 (PRESERVED) | 1 | Thus We seal the hearts of the hostile. | 他们带着明证来临，但他们不肯相信他们以前否认的东西。我们就这样在敌视者的心上打了封印。 | PRESERVED |
| 10:75 (PRESERVED) | 0 | Then after them We sent Moses and Aaron to Pharaoh and his chiefs with Our signs. | 然后，在他们之后， | PRESERVED |
| 10:76 (PRESERVED) | 0 | When the truth came to them from Us, they said: This is evident sorcery. | 当真理从我们这里降临他们，他们说：“这显然是魔术。 | PRESERVED |
| 10:78 (PRESERVED) | 0 | We will not believe you two. | 好让你在地上显赫吗？我们绝不信你。” | PRESERVED |
| 10:87 (PRESERVED) | 0 | We inspired Moses and his brother: Settle houses for your people in Egypt. | 我们启示摩西和他的兄弟：“为你们的族人在埃及安顿下来， | PRESERVED |
| 10:90 (PRESERVED) | 0 | We brought the Children of Israel across the sea. | 我们使以色列的后裔渡过海。法老和他的军队骄横地追击他们。 | PRESERVED |
| 10:92 (PRESERVED) | 0 | Today We will save you in your body, that you may be a sign for those after you. | 今天我们将保存你的身体，使你成为后来者的迹象。 | PRESERVED |
| 10:92 (PRESERVED) | 1 | Many people are heedless of Our signs. | 使你成为后来者的迹象。但大多数人对我们的迹象漫不经心。 | PRESERVED |
| 10:93 (PRESERVED) | 0 | We settled the Children of Israel in a position of honor, and provided them with good things. | 我们确已使以色列的后裔定居在尊贵之地，供给他们佳美的食物。 | PRESERVED |
| 10:94 (PRESERVED) | 0 | If you are in doubt about what We sent down to you, ask those who read the Book before you. | 如果你对我们降示给你的启示有所怀疑，就去问在你之前读经典的人。 | PRESERVED |
| 10:98 (PRESERVED) | 0 | We lifted from them the punishment of disgrace in the worldly life, and let them enjoy life for a time. | 除了约拿的民众。当他们信了，我们为他们解除了今世生活中的屈辱之苦， | PRESERVED |
| 10:103 (PRESERVED) | 0 | Then We save Our messengers and those who believed. | 然后我们拯救我们的使者和信道的人。拯救信道者是我们应尽的义务。 | PRESERVED |
| 10:103 (PRESERVED) | 1 | Thus it is binding upon Us: We save the believers. | 然后我们拯救我们的使者和信道的人。拯救信道者是我们应尽的义务。 | PRESERVED |

### Surah 11

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 11:8 (PRESERVED) | 0 | If We delay the punishment from them to a numbered span, they will say: What holds it back? | 如果我们把他们的刑罚推迟到定期，他们会说： | PRESERVED |
| 11:9 (PRESERVED) | 0 | If We let the human being taste mercy from Us, then strip it from him | 如果我们让人类尝到来自我们的仁慈，然后从他那里收回， | PRESERVED |
| 11:10 (PRESERVED) | 0 | If We let him taste blessing after hardship touched him, he says: The bad things have left me. | 如果我们在灾难触及他之后让他尝到繁荣，他会说： | PRESERVED |
| 11:15 (PRESERVED) | 0 | We will repay them their deeds in full therein, and they will not be shortchanged therein. | 谁欲求今世生活及其浮华——我们将在其中充分报偿他们的行为，他们在其中不受亏枉。 | PRESERVED |
| 11:25 (PRESERVED) | 0 | We sent Noah to his people: I am an evident warner to you — | 我们确已派遣挪亚去他的族人：“我是你们的明白警告者。 | PRESERVED |
| 11:27 (PRESERVED) | 1 | We see that only the worst among us have followed you | 我们看到追随你的只是我们中最下等、见识浅薄的人。我们看你们并不比我们优越。 | PRESERVED |
| 11:27 (PRESERVED) | 2 | We see you have no advantage over us. | 我们看你们并不比我们优越。事实上，我们认为你们是说谎者。 | PRESERVED |
| 11:27 (PRESERVED) | 3 | We think you are liars. | 我们认为你们是说谎者。” | PRESERVED |
| 11:37 (PRESERVED) | 0 | Build the Ark under Our eyes and by Our inspiration. | “在我们注视下，凭我们的启示建造方舟。 | PRESERVED |
| 11:40 (PRESERVED) | 0 | Until, when Our command came and the oven boiled over | 直到我们的命令降临，火山口喷发， | PRESERVED |
| 11:40 (PRESERVED) | 1 | We said: Load into it two of every pair, and your family | 直到我们的命令降临，火山口喷发，我们说： | PRESERVED |
| 11:48 (PRESERVED) | 0 | It was said: Noah, come down with peace from Us and blessings upon you, and upon nations from those with you. | “挪亚啊，带着来自我们的平安下船吧；祝福在你身上， | PRESERVED |
| 11:48 (PRESERVED) | 1 | And nations We will let enjoy life; | 也在与你同在的人的后裔身上。还有其他民族，我们将让他们繁荣， | PRESERVED |
| 11:48 (PRESERVED) | 2 | then a painful punishment from Us will touch them. | 然后来自我们的痛苦刑罚将降临他们。” | PRESERVED |
| 11:49 (PRESERVED) | 0 | We inspire them to you. | 这些是过去的故事，我们启示给你。在此之前， | PRESERVED |
| 11:53 (PRESERVED) | 0 | We will not leave our gods for your word. | “呼德啊，你没有给我们带来任何证据，我们不会因你一句话就放弃我们的神， | PRESERVED |
| 11:53 (PRESERVED) | 1 | We will not believe you. | 我们不会因你一句话就放弃我们的神，我们也不信你。” | PRESERVED |
| 11:54 (PRESERVED) | 0 | We say only: some of our gods struck you with evil. | “我们只说，我们的一些神以邪恶附了你的身。 | PRESERVED |
| 11:58 (PRESERVED) | 0 | When Our command came | 当我们的判决降临，我们以来自我们的仁慈拯救了呼德和与他一同信道的人， | PRESERVED |
| 11:58 (PRESERVED) | 1 | We saved Hud and those who believed with him, by mercy from Us. | 当我们的判决降临，我们以来自我们的仁慈拯救了呼德和与他一同信道的人， | PRESERVED |
| 11:58 (PRESERVED) | 2 | We saved them from a harsh punishment. | 我们以来自我们的仁慈拯救了呼德和与他一同信道的人，我们使他们脱离了严厉的刑罚。 | PRESERVED |
| 11:62 (PRESERVED) | 0 | We are in a troubling doubt about what you call us to. | 你要阻止我们崇拜我们祖先所崇拜的吗？我们对你所召唤我们的确深感怀疑。” | PRESERVED |
| 11:66 (PRESERVED) | 0 | When Our command came | 然后，当我们的命令降临， | PRESERVED |
| 11:66 (PRESERVED) | 1 | We saved Salih and those who believed with him, by mercy from Us, and from the disgrace of that Day. | 然后，当我们的命令降临， | PRESERVED |
| 11:69 (PRESERVED) | 0 | Our messengers came to Abraham with the good news. | 我们的使者带着喜讯来见亚伯拉罕。他们说： | PRESERVED |
| 11:71 (PRESERVED) | 0 | We gave her good news of Isaac, and beyond Isaac, Jacob. | 于是她笑了。我们向她报喜：以撒； | PRESERVED |
| 11:74 (PRESERVED) | 0 | When the fear left Abraham and the good news came to him, he argued with Us about the people of Lot. | 喜讯到达他时，他开始为罗得的族人向我们求情。 | PRESERVED |
| 11:77 (PRESERVED) | 0 | When Our messengers came to Lot, he was distressed for them and constrained in himself. | 当我们的使者来到罗得那里，他为他们焦虑， | PRESERVED |
| 11:82 (PRESERVED) | 0 | When Our command came | 当我们的命令降临，我们把它翻了个底朝天， | PRESERVED |
| 11:82 (PRESERVED) | 1 | We turned it upside down and rained upon it stones of baked clay, piled up — | 当我们的命令降临，我们把它翻了个底朝天， | PRESERVED |
| 11:91 (PRESERVED) | 0 | We see you as weak among us. | “舒艾卜啊，我们不大理解你说的话，我们看你在我们中间是软弱的。 | PRESERVED |
| 11:94 (PRESERVED) | 0 | When Our command came | 当我们的命令降临，我们以来自我们的仁慈拯救了舒艾卜和与他一同信道的人， | PRESERVED |
| 11:94 (PRESERVED) | 1 | We saved Shuayb and those who believed with him, by mercy from Us. | 当我们的命令降临，我们以来自我们的仁慈拯救了舒艾卜和与他一同信道的人， | PRESERVED |
| 11:96 (PRESERVED) | 0 | We sent Moses with Our signs and an evident authority — | 我们确已以我们的迹象和明白的授权派遣了摩西。 | PRESERVED |
| 11:100 (PRESERVED) | 0 | We recount them to you. | 这些是城镇的消息——我们向你讲述。有些还矗立着，有些已枯萎。 | PRESERVED |
| 11:101 (PRESERVED) | 0 | We did not wrong them; | 我们没有亏枉他们，而是他们亏枉了自己。 | PRESERVED |
| 11:104 (PRESERVED) | 0 | We delay it only for a counted term. | 我们只把它推迟到预定的时间。 | PRESERVED |
| 11:109 (PRESERVED) | 0 | We will pay them their share in full, undiminished. | 他们只像他们的祖先以前那样崇拜。我们必将把他们应得的足额付给他们，毫不减少。 | PRESERVED |
| 11:110 (PRESERVED) | 0 | We gave Moses the Book, but it was disputed. | 我们确已把经典赐给摩西，但人们对它有分歧。 | PRESERVED |
| 11:116 (PRESERVED) | 0 | except a few of those We saved among them? | 要是有有智慧的人，出来反对大地上的腐败就好了——除了我们拯救的少数人。但作恶者追逐他们所沉溺的奢华， | PRESERVED |
| 11:120 (PRESERVED) | 0 | Each of the messengers' tidings We recount to you | 我们向你叙述使者的历史的一切，都是为了借此坚定你的心。在这其中， | PRESERVED |
| 11:120 (PRESERVED) | 1 | with it We steady your heart. | 都是为了借此坚定你的心。在这其中，真理已降临你， | PRESERVED |

### Surah 12

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 12:2 (PRESERVED) | 0 | We sent it down as an Arabic recital, that you may use your minds. | 我们确已把它降示为阿拉伯文的古兰经，以便你们理解。 | PRESERVED |
| 12:3 (PRESERVED) | 0 | We recount to you the fairest of stories in what We inspired to you | 我们通过向你降示这部古兰经，向你叙述最准确的历史。 | PRESERVED |
| 12:15 (PRESERVED) | 0 | and We inspired to him: You will tell them of this deed of theirs, and they will not know. | 商定把他放在井底。我们启示他：“当他们浑然不觉时， | PRESERVED |
| 12:21 (PRESERVED) | 0 | Thus We established Joseph in the land, and to teach him the interpretation of events. | 他可能对我们有用，或者我们收他为儿子。”我们就这样使约瑟在那地站稳脚跟， | PRESERVED |
| 12:22 (PRESERVED) | 0 | We gave him judgment and knowledge. | 当他成年，我们赐给他智慧和知识。我们就这样报偿行善者。 | PRESERVED |
| 12:22 (PRESERVED) | 1 | Thus We repay those who do good. | 我们赐给他智慧和知识。我们就这样报偿行善者。 | PRESERVED |
| 12:24 (PRESERVED) | 0 | Thus We turned evil and indecency away from him. | 他也想要她，要不是他看见了他主的明证。我们就这样使罪恶和丑事远离他。 | PRESERVED |
| 12:24 (PRESERVED) | 1 | He was one of Our loyal servants. | 我们就这样使罪恶和丑事远离他。他是我们的忠诚仆人之一。 | PRESERVED |
| 12:30 (PRESERVED) | 0 | We see her in evident error. | 她深深爱上了他。我们看她确已迷误。” | PRESERVED |
| 12:44 (PRESERVED) | 0 | We know nothing of the interpretation of dreams. | 他们说：“是纷乱的梦，我们不懂解梦。 | PRESERVED |
| 12:56 (PRESERVED) | 0 | Thus We established Joseph in the land; | 我们就这样使约瑟在那地站稳脚跟，随意居住。 | PRESERVED |
| 12:56 (PRESERVED) | 1 | We touch with Our mercy whom We will. | 我们就这样使约瑟在那地站稳脚跟，随意居住。我们以我们的仁慈触及我们所意欲的人， | PRESERVED |
| 12:56 (PRESERVED) | 2 | We do not waste the wage of those who do good. | 随意居住。我们以我们的仁慈触及我们所意欲的人，我们永不浪费行善者的报酬。 | PRESERVED |
| 12:65 (PRESERVED) | 0 | We will bring food for our family, guard our brother, and gain a camel's load more. | 这是我们的货物，已退还给我们。我们将为家人提供给养， | PRESERVED |
| 12:68 (PRESERVED) | 0 | He was a person of knowledge, for We had taught him, but most people do not know. | 他实现了它。他因我们教过他而有知识，但大多数人不知道。 | PRESERVED |
| 12:75 (PRESERVED) | 0 | Thus We repay the wrongdoers. | 就把他归你们。我们就这样惩罚犯罪者。” | PRESERVED |
| 12:76 (PRESERVED) | 0 | Thus We devised a plan for Joseph; | 然后他从他弟弟的袋子里搜出了它。我们就这样为约瑟设了计；除非真主意欲， | PRESERVED |
| 12:76 (PRESERVED) | 1 | We raise in rank whom We will. | 他不能按国王的法律扣留他的弟弟。我们使我们所意欲的人逐级升高；在每个有知识的人之上， | PRESERVED |
| 12:78 (PRESERVED) | 0 | We see you are of those who do good. | 是很老的老人，所以把我们中的一个代替他吧。我们看你是个好人。 | PRESERVED |
| 12:81 (PRESERVED) | 0 | We testify only to what we know. | ‘父亲啊，你的儿子偷了。我们只见证我们所知道的， | PRESERVED |
| 12:81 (PRESERVED) | 1 | We could not guard the unseen. | 我们只见证我们所知道的，我们无法防范未知的。’” | PRESERVED |
| 12:82 (PRESERVED) | 0 | We are truthful. | 我们确是诚实的。” | PRESERVED |
| 12:88 (PRESERVED) | 0 | We brought scant goods. | “尊贵的长官啊，灾难降临了我们和我们的家人。我们带来了微薄的货物。 | PRESERVED |
| 12:102 (PRESERVED) | 0 | We inspire them to you. | 这是过去的消息，我们启示给你。当他们阴谋并商定计划时， | PRESERVED |
| 12:109 (PRESERVED) | 0 | We sent before you only men, whom We inspired, from the people of the towns. | 在你之前，我们只派遣了男人， | PRESERVED |
| 12:110 (PRESERVED) | 0 | Until, when the messengers despaired and thought they had been denied, Our help came to them; | 认为自己被否认时，我们的援助降临他们。我们拯救我们所意欲的人， | PRESERVED |
| 12:110 (PRESERVED) | 1 | We save whom We will. | 认为自己被否认时，我们的援助降临他们。我们拯救我们所意欲的人， | PRESERVED |
| 12:110 (PRESERVED) | 2 | Our severity is not turned back from the criminal people. | 我们的援助降临他们。我们拯救我们所意欲的人，我们的严厉不会从犯罪的人身上转开。 | PRESERVED |

### Surah 13

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 13:4 (PRESERVED) | 0 | We favor some of them over others in taste. | 同根或异根，用同样的水灌溉。我们使一些的味道胜过另一些。 | PRESERVED |
| 13:22 (PRESERVED) | 0 | And who were patient, seeking their Lord's presence, kept up the prayer, and gave from what We provided them | 谨守礼拜，从我们给他们的给养中秘密和公开地施舍，以善驱恶。 | PRESERVED |
| 13:30 (PRESERVED) | 0 | Thus We sent you among a community before which communities passed away, to recite to them what We inspired to you, while they disbelieve in the Beneficent. | 我们就这样把你派遣到一个民族中，在他们之前已有许多民族逝去， | PRESERVED |
| 13:36 (PRESERVED) | 0 | Those We gave the Book rejoice in what was sent down to you. | 我们赐给经典的人为降示给你的而欢喜，有些派别却拒绝其中的部分。 | PRESERVED |
| 13:37 (PRESERVED) | 0 | Thus We sent it down as an Arabic law. | 我们就这样把它降示为阿拉伯文的法典。如果你追随他们的私欲， | PRESERVED |
| 13:38 (PRESERVED) | 0 | We sent messengers before you and made for them spouses and children. | 我们确已在你之前派遣了使者，我们为他们安排了妻子和后裔。 | PRESERVED |
| 13:40 (PRESERVED) | 0 | Whether We show you some of what We promised them, or take you in death | 无论我们让你看到我们许诺他们的一部分，还是使你去世——你的职责是传达， | PRESERVED |
| 13:40 (PRESERVED) | 1 | upon you is only the delivery, and upon Us the reckoning. | 还是使你去世——你的职责是传达，清算归我们。 | PRESERVED |
| 13:41 (PRESERVED) | 0 | Have they not seen that We come to the land, reducing it from its edges? | 他们没看到我们如何对待大地，从边缘削减它吗？ | PRESERVED |

### Surah 14

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 14:1 (PRESERVED) | 0 | A Book We sent down to you, to bring people out of darkness into light | 阿里夫、拉姆、 | PRESERVED |
| 14:4 (PRESERVED) | 0 | We sent no messenger except in his people's tongue, to make clear to them. | 我们从未派遣任何使者，除非用他族人的语言， | PRESERVED |
| 14:5 (PRESERVED) | 0 | We sent Moses with Our signs: Bring your people out of darkness into light, and remind them of the Days of God. | 我们以我们的迹象派遣了摩西：“把你的族人从黑暗带到光明， | PRESERVED |
| 14:12 (PRESERVED) | 0 | We will be patient over what you hurt us with. | 我们为什么不托靠真主呢？我们必忍受你们的迫害。托靠者应当托靠真主。 | PRESERVED |
| 14:13 (PRESERVED) | 1 | Their Lord inspired to them: We will destroy the wrongdoers, | ”他们的主启示他们：“我们必毁灭不义者。” | PRESERVED |
| 14:14 (PRESERVED) | 0 | And We will settle you in the land after them. | “我们必使你们在他们之后定居这地。那是给畏惧我的威严、 | PRESERVED |
| 14:21 (PRESERVED) | 0 | The weak will say to those who were proud: We were your followers; | “我们是你们的追随者，你们能为我们抵挡真主的刑罚吗？”他们会说： | PRESERVED |
| 14:31 (PRESERVED) | 0 | Say to My servants who believed: keep up the prayer, and give from what We provided them | 你告诉信道的仆人们：谨守礼拜，从我们给他们的给养中秘密和公开地施舍， | PRESERVED |
| 14:45 (PRESERVED) | 0 | You lived in the dwellings of those who wronged themselves, and it became clear to you how We dealt with them | 你们曾住在亏枉自己的人的家里，我们如何对待他们已对你们明了，我们为你们举了例子。 | PRESERVED |
| 14:45 (PRESERVED) | 1 | and We set forth the examples for you. | 我们如何对待他们已对你们明了，我们为你们举了例子。 | PRESERVED |

### Surah 15

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 15:4 (PRESERVED) | 0 | We never destroyed a town without a fixed term, written down for it. | 我们从未毁灭一座城镇，除非它有定期。 | PRESERVED |
| 15:8 (PRESERVED) | 0 | We do not send down the angels except with the truth, and then they would not be given more time. | 我们降下天使，只凭真理， | PRESERVED |
| 15:9 (PRESERVED) | 0 | We Ourselves sent down the Reminder | 我们确已降示了讯息，我们确将保护它。 | PRESERVED |
| 15:9 (PRESERVED) | 1 | and We Ourselves guard it. | 我们确已降示了讯息，我们确将保护它。 | PRESERVED |
| 15:10 (PRESERVED) | 0 | We sent messengers before you to the parties of the earlier peoples. | 在你之前，我们向以前的民族派遣过别人。 | PRESERVED |
| 15:12 (PRESERVED) | 0 | So We slide it into the hearts of the guilty. | 我们就这样把它滑入犯罪者的心中。 | PRESERVED |
| 15:14 (PRESERVED) | 0 | Even if We opened a gate to the sky for them, and they kept climbing through it — | 即使我们为他们打开天上的一道门，他们开始从中上升。 | PRESERVED |
| 15:16 (PRESERVED) | 0 | We set great constellations in the sky and made it beautiful to look upon. | 我们在天上安置了星座，使它们对观看者美丽。 | PRESERVED |
| 15:17 (PRESERVED) | 0 | And We guarded it from every banished devil. | 我们保护它们免遭每个被驱逐的恶魔。 | PRESERVED |
| 15:19 (PRESERVED) | 0 | We spread it out, and set firm mountains on it, and grew on it everything in due measure. | 我们展开大地，在其中安置稳定器， | PRESERVED |
| 15:20 (PRESERVED) | 0 | And We made in it a livelihood for you, and for those you do not provide for. | 我们在其中为你们创造了生计，也为那些不是你们供给的人。 | PRESERVED |
| 15:21 (PRESERVED) | 0 | There is nothing but its stores are with Us | 没有一样东西，它的宝库不在我们这里，我们只按精确的定量降下它。 | PRESERVED |
| 15:21 (PRESERVED) | 1 | and We send it down only in a known measure. | 没有一样东西，它的宝库不在我们这里，我们只按精确的定量降下它。 | PRESERVED |
| 15:22 (PRESERVED) | 0 | And We sent the winds as bearers of seed, and sent down water from the sky | 我们发送授精的风；从天上降下水， | PRESERVED |
| 15:23 (PRESERVED) | 0 | And We alone give life and bring death | 是我们赐生致死，我们是继承者。 | PRESERVED |
| 15:23 (PRESERVED) | 1 | and We are the Inheritors. | 是我们赐生致死，我们是继承者。 | PRESERVED |
| 15:24 (PRESERVED) | 0 | We know those of you who went ahead | 我们知道你们中前进的人，也知道落后的人。 | PRESERVED |
| 15:24 (PRESERVED) | 1 | and We know those who hang back. | 我们知道你们中前进的人，也知道落后的人。 | PRESERVED |
| 15:26 (PRESERVED) | 0 | We created the human from dry clay, from dark, worked mud. | 我们用泥土、成型的泥创造了人类。 | PRESERVED |
| 15:27 (PRESERVED) | 0 | And the jinn We created before, from the scorching wind of fire. | 精灵，我们以前用穿透的火创造了他们。 | PRESERVED |
| 15:47 (PRESERVED) | 0 | And We will strip away from their chests any grudge | 我们将消除他们心中的一切怨恨——兄弟姐妹们，在相对的坐榻上。 | PRESERVED |
| 15:59 (PRESERVED) | 0 | We will save them, every one — | “除了罗得的家人；我们必拯救他们全部。” | PRESERVED |
| 15:60 (PRESERVED) | 0 | We decreed she would be among those who stay behind." | “除了他的妻子。”我们已判定她将是落后者之一。 | PRESERVED |
| 15:66 (PRESERVED) | 0 | "And We decreed for him that command: that their last man would be cut off by morning." | 我们告诉他我们的判决：这些人的最后残余将在清晨被连根拔起。 | PRESERVED |
| 15:74 (PRESERVED) | 0 | And We turned its high part low, and rained down on them stones of baked clay. | 我们把它翻了个底朝天，向他们降下烧硬的泥石之雨。 | PRESERVED |
| 15:79 (PRESERVED) | 0 | So We took vengeance on them | 于是我们惩罚了他们。两者都有明确记载。 | PRESERVED |
| 15:81 (PRESERVED) | 0 | And We gave them Our signs, but they turned away from them. | 我们给了他们我们的迹象，但他们转身离去。 | PRESERVED |
| 15:85 (PRESERVED) | 0 | We did not create the heavens and the earth, and what is between them, except with the truth. | 我们创造天地及其间的一切，只凭真理。 | PRESERVED |
| 15:87 (PRESERVED) | 0 | We gave you seven of the oft-repeated, and the great Quran. | 我们确已给你七个对偶，和伟大的古兰经。 | PRESERVED |
| 15:88 (PRESERVED) | 0 | Do not stretch your eyes toward what We let some of them enjoy, and do not grieve over them | 不要把你的眼睛伸向我们赐给他们中的一些夫妇享受的，不要为他们忧伤， | PRESERVED |
| 15:90 (PRESERVED) | 0 | As We sent down upon the dividers — | 正如我们降示给分裂者的一样。 | PRESERVED |
| 15:92 (PRESERVED) | 0 | We will question them, every one, | 以你的主发誓，我们必审问他们全部。 | PRESERVED |
| 15:95 (PRESERVED) | 0 | We are enough for you against the mockers — | 我们足以对付嘲笑者。 | PRESERVED |
| 15:97 (PRESERVED) | 0 | We know your chest tightens at what they say. | 我们知道你的心因他们的言语而紧缩。 | PRESERVED |

### Surah 16

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 16:36 (PRESERVED) | 0 | We sent a messenger to every community: | 我们向每个民族派遣了使者：“崇拜真主， | PRESERVED |
| 16:40 (PRESERVED) | 0 | Our word to a thing, when We will it, is only to say to it, "Be," and it is. | 当我们意欲一件事发生，我们对它说： | PRESERVED |
| 16:41 (PRESERVED) | 0 | We will settle them well in this world, and the reward of the Hereafter is greater, if they only knew. | 为真主而迁徙、在受迫害之后的人，我们将在今世使他们定居在好的地方； | PRESERVED |
| 16:43 (PRESERVED) | 0 | We sent no one before you but men | 在你之前，我们只派遣了我们启示的男人。 | PRESERVED |
| 16:43 (PRESERVED) | 1 | We inspired them. | 在你之前，我们只派遣了我们启示的男人。所以如果你们不知道， | PRESERVED |
| 16:44 (PRESERVED) | 0 | And We sent down to you the Reminder, to make clear to people what was sent down to them, so that they may think. | 带着阐明和经典。我们降示给你提醒，以便你向人们阐明降示给他们的， | PRESERVED |
| 16:55 (PRESERVED) | 0 | To deny what We gave them. | 以忘恩负义对待我们给他们的。享受吧。 | PRESERVED |
| 16:56 (PRESERVED) | 0 | They set aside for what they know nothing about a share of what We provided them. | 他们把我们给他们的给养的一部分分配给他们所不知道的东西。以真主发誓，你们必被审问关于你们所捏造的。 | PRESERVED |
| 16:63 (PRESERVED) | 0 | We sent messengers to communities before you | 以真主发誓，我们向你之前的民族派遣了使者， | PRESERVED |
| 16:64 (PRESERVED) | 0 | We sent down the Book to you only to make clear to them what they differed over | 我们降示给你经典，只是为了为他们阐明他们所分歧的， | PRESERVED |
| 16:66 (PRESERVED) | 0 | And in the livestock you have a lesson: We give you to drink from what is in their bellies | 牲畜中对你们确有教训：我们从它们的肚子里，从粪便和血液之间， | PRESERVED |
| 16:75 (PRESERVED) | 0 | and one We provided with good provision from Us, and he gives from it secretly and openly. | 对任何事无能为力；和一个我们赐给他丰厚给养、他秘密和公开施舍的人。 | PRESERVED |
| 16:84 (PRESERVED) | 0 | A Day when We raise a witness from every community | 在我们从每个民族中升起见证者的那天——不信道的人不被允许，也不被原谅。 | PRESERVED |
| 16:88 (PRESERVED) | 0 | We added punishment upon punishment for the corruption they spread. | 不信道且阻碍真主道路的人——我们将在他们的刑罚上增加刑罚，因为他们曾经作恶。 | PRESERVED |
| 16:89 (PRESERVED) | 0 | A Day when We raise in every community a witness against them from among themselves | 在我们从每个民族中升起针对他们的见证者、从他们中间的那天， | PRESERVED |
| 16:89 (PRESERVED) | 1 | and We brought you as a witness over these. | 从他们中间的那天，带来你作证这些人。我们降示给你经典， | PRESERVED |
| 16:89 (PRESERVED) | 2 | And We sent down the Book to you as an explanation of all things, and guidance, and mercy, and glad news for those who submit. | 带来你作证这些人。我们降示给你经典，作为对一切事物的解释， | PRESERVED |
| 16:96 (PRESERVED) | 0 | We will reward those who were patient with the best of what they did. | 你们所有的会用尽，但真主那里的永存。我们必按忍耐者最好的行为报偿他们。 | PRESERVED |
| 16:97 (PRESERVED) | 0 | We will give him a good life | 谁行善，无论男女，只要是信道者， | PRESERVED |
| 16:97 (PRESERVED) | 1 | and We will reward them with the best of what they did. | 无论男女，只要是信道者，我们必赐他美好的生活——我们必按他们最好的行为报偿他们。 | PRESERVED |
| 16:101 (PRESERVED) | 0 | When We replaced one sign with another | 当我们以一节经文代替另一节经文——真主最知道他所降示的——他们说：“你是捏造者。 | PRESERVED |
| 16:103 (PRESERVED) | 0 | We know they say, "Only a human teaches him." The tongue of the one they refer to is foreign | 我们很清楚他们说：“是人在教他。 | PRESERVED |
| 16:118 (PRESERVED) | 0 | We forbade what We told you about before. | 对犹太人，我们禁止了我们以前告诉你的。 | PRESERVED |
| 16:118 (PRESERVED) | 1 | We did not wrong them | 我们禁止了我们以前告诉你的。我们没有亏枉他们，而是他们亏枉自己。 | PRESERVED |
| 16:122 (PRESERVED) | 0 | We gave him good in this world | 我们在今世赐给他福利，在后世他必在正义者之中。 | PRESERVED |
| 16:123 (PRESERVED) | 0 | Then We inspired you: | 然后我们启示你：“追随亚伯拉罕的宗教， | PRESERVED |

### Surah 17

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 17:1 (PRESERVED) | 0 | whose surroundings We blessed | 为要让他看见我们的一些迹象。他确是全听的，全观的。 | PRESERVED |
| 17:1 (PRESERVED) | 1 | to show him some of Our signs. | 他确是全听的，全观的。 | PRESERVED |
| 17:2 (PRESERVED) | 0 | We gave Moses the Book and made it guidance for the children of Israel: | 我们赐给摩西经典，并使它成为以色列后裔的向导： | PRESERVED |
| 17:3 (PRESERVED) | 0 | Offspring of those We carried with Noah | （他们是）我们与挪亚一同载过的那些人的后裔。他确是一个感恩的仆人。 | PRESERVED |
| 17:4 (PRESERVED) | 0 | We decreed for the children of Israel in the Book: | 我们在经典中传谕以色列的后裔：你们必定要在大地上两次作恶， | PRESERVED |
| 17:5 (PRESERVED) | 0 | We sent against you servants of Ours, men of great might | 当两项许约中的第一项实现时，我们派遣拥有强大力量的仆人们去对付你们，他们搜遍了你们的家园。 | PRESERVED |
| 17:6 (PRESERVED) | 0 | Then We gave you back the upper hand over them, and supplied you with wealth and sons, and made you greater in number. | 然后我们把战胜他们的机会还给你们，并以财富和子孙援助你们， | PRESERVED |
| 17:8 (PRESERVED) | 0 | We return. | 但如果你们重犯，我们也会重来。我们已使火狱成为不信道者的监狱。 | PRESERVED |
| 17:8 (PRESERVED) | 1 | We made Hell a prison for the disbelievers. | 但如果你们重犯，我们也会重来。我们已使火狱成为不信道者的监狱。 | PRESERVED |
| 17:10 (PRESERVED) | 0 | We prepared for them a painful punishment. | 至于那些不信后世的人——我们已为他们预备了痛苦的刑罚。 | PRESERVED |
| 17:12 (PRESERVED) | 0 | We made the night and the day two signs | 我们使昼夜成为两种迹象。我们抹去了夜的迹象， | PRESERVED |
| 17:12 (PRESERVED) | 1 | then We blotted out the sign of the night, and made the sign of the day giving light, so you may seek bounty from your Lord, and know the number of years and the reckoning. | 我们使昼夜成为两种迹象。我们抹去了夜的迹象，使昼的迹象昭明， | PRESERVED |
| 17:12 (PRESERVED) | 2 | Everything We laid out in detail. | 知道年数和计算。我们已详细阐明一切事物。 | PRESERVED |
| 17:13 (PRESERVED) | 0 | We fastened his fate to his neck. | 我们已把每个人的命运系在他的颈项上。复活日， | PRESERVED |
| 17:13 (PRESERVED) | 1 | On the Day of Resurrection We will bring out for him a book he will find spread open. | 我们已把每个人的命运系在他的颈项上。复活日，我们将为他取出展开的记录。 | PRESERVED |
| 17:15 (PRESERVED) | 0 | We were never punishers until We sent a messenger. | 负重者不负别人的重担。在我们派遣使者之前，我们绝不惩罚。 | PRESERVED |
| 17:16 (PRESERVED) | 0 | When We willed to destroy a town | 当我们决定毁灭一个城市时，我们命令其中奢侈的人， | PRESERVED |
| 17:16 (PRESERVED) | 1 | We ordered its well-off | 当我们决定毁灭一个城市时，我们命令其中奢侈的人，他们在城中作恶， | PRESERVED |
| 17:16 (PRESERVED) | 2 | and We smashed it to ruin. | 于是对他们的判决成为定局，我们把那城彻底毁灭。 | PRESERVED |
| 17:17 (PRESERVED) | 0 | How many generations We destroyed after Noah! | 在挪亚之后，我们毁灭了多少世代！ | PRESERVED |
| 17:18 (PRESERVED) | 0 | We hurry for him in it what We will, for whom We will | 谁想要今世的速朽，我们就加速给他我们所意欲的，给我们所意欲的人。 | PRESERVED |
| 17:18 (PRESERVED) | 1 | then We made Hell for him. | 然后我们使他进入火狱，他在其中受烤，被谴责， | PRESERVED |
| 17:20 (PRESERVED) | 0 | We extend from your Lord's gift. | 这一切人和那一切人，我们都以你的主的恩赐供给他们。 | PRESERVED |
| 17:21 (PRESERVED) | 0 | See how We favored some of them over others | 你看我们怎样使他们中的一些人优于另一些人；但后世的品级更大， | PRESERVED |
| 17:31 (PRESERVED) | 0 | We provide for them and for you. | 不要因怕贫穷而杀害你们的子女。我们供给他们，也供给你们。 | PRESERVED |
| 17:33 (PRESERVED) | 0 | We gave his heir authority. | 谁被无理杀害，我们确已赋予他的近亲一定的权柄。但他在杀人时不要过分， | PRESERVED |
| 17:41 (PRESERVED) | 0 | We varied in this Quran, so they may take heed | 我们已在这部古兰经中反复阐明，为要他们记取， | PRESERVED |
| 17:45 (PRESERVED) | 0 | We set between you and those who do not believe in the Hereafter a hidden barrier. | 当你诵读古兰经时，我们在你与不信后世的人之间设置一道看不见的屏障。 | PRESERVED |
| 17:46 (PRESERVED) | 0 | We set coverings over their hearts, lest they understand it, and deafness in their ears. | 我们在他们心上覆盖了帷幕，使他们不能理解它， | PRESERVED |
| 17:47 (PRESERVED) | 0 | We know best what they listen for when they listen to you, and when they whisper among themselves | 我们最知道他们听什么，当他们听你讲话时； | PRESERVED |
| 17:54 (PRESERVED) | 0 | We did not send you as their guardian. | 如果他意欲，他会惩罚你们。我们没有派你做他们的保护者。 | PRESERVED |
| 17:55 (PRESERVED) | 0 | We favored some prophets over others | 你的主最知道诸天和大地中的一切。我们使一些先知优于另一些先知；我们赐给大卫诗篇。 | PRESERVED |
| 17:55 (PRESERVED) | 1 | and We gave David the Psalms. | 我们使一些先知优于另一些先知；我们赐给大卫诗篇。 | PRESERVED |
| 17:58 (PRESERVED) | 0 | There is no town but We will destroy it before the Day of Resurrection, or punish it severely. | 没有一个城市，我们不在复活日之前毁灭它， | PRESERVED |
| 17:59 (PRESERVED) | 0 | Nothing kept Us from sending the signs but that the former peoples called them lies. | 没有什么阻止我们降示迹象，除非古人否认它们。 | PRESERVED |
| 17:59 (PRESERVED) | 1 | We gave Thamud the she-camel, a clear sign | 除非古人否认它们。我们赐给赛莫德人母驼作为明证，但他们亏待了它。 | PRESERVED |
| 17:59 (PRESERVED) | 2 | We send the signs only as a warning. | 但他们亏待了它。我们降示迹象，只是为了使人敬畏。 | PRESERVED |
| 17:60 (PRESERVED) | 0 | When We said to you, "Your Lord surrounds the people" | 当时我们对你说：你的主是包罗人类的。 | PRESERVED |
| 17:60 (PRESERVED) | 1 | We made the vision We showed you only a trial for the people, and the cursed tree in the Quran. | 当时我们对你说：你的主是包罗人类的。我们没有使我们让你看到的异象成为对众人的考验， | PRESERVED |
| 17:60 (PRESERVED) | 2 | We frighten them, but it only adds to their great defiance. | 也没有使古兰经中被诅咒的树成为考验。我们警告他们，但那只增加他们的大逆不道。 | PRESERVED |
| 17:61 (PRESERVED) | 0 | When We said to the angels, "Bow down to Adam" | 当时我们对天使们说：“你们向亚当叩头。 | PRESERVED |
| 17:69 (PRESERVED) | 0 | then find none to hold Us to account for it? | 因你们的忘恩而淹死你们？然后你们找不到对抗我们的援助者。 | PRESERVED |
| 17:70 (PRESERVED) | 0 | We honored the children of Adam | 我们确已尊贵亚当的子孙，载他们在陆上和海上行驶， | PRESERVED |
| 17:70 (PRESERVED) | 1 | We carried them on land and sea, provided them with the good things, and favored them greatly over many of those We created. | 我们确已尊贵亚当的子孙，载他们在陆上和海上行驶， | PRESERVED |
| 17:71 (PRESERVED) | 0 | A Day when We call every people by their leader | 在那日，我们召唤每个民族和他们的领袖。 | PRESERVED |
| 17:73 (PRESERVED) | 0 | They nearly tempted you away from what We inspired to you, to invent against Us something else | 他们几乎把你从我们启示给你的中诱开，使你假借我们的名义捏造别的。那样的话， | PRESERVED |
| 17:74 (PRESERVED) | 0 | Had We not made you firm, you would nearly have leaned toward them a little. | 如果我们没有使你坚定，你几乎要稍微倾向他们了。 | PRESERVED |
| 17:75 (PRESERVED) | 0 | Then We would have made you taste double in life and double in death | 那样，我们必定让你在生前尝双倍的刑罚， | PRESERVED |
| 17:75 (PRESERVED) | 1 | then you would find no helper for you against Us. | 死后尝双倍的刑罚；然后你找不到对抗我们的援助者。 | PRESERVED |
| 17:77 (PRESERVED) | 0 | The way of those We sent before you of Our messengers | 这是我们之前派遣的使者们的惯例——你不会发现我们的法则有任何改变。 | PRESERVED |
| 17:77 (PRESERVED) | 1 | you will find no change in Our way. | 这是我们之前派遣的使者们的惯例——你不会发现我们的法则有任何改变。 | PRESERVED |
| 17:82 (PRESERVED) | 0 | We send down from the Quran what is healing and mercy for the believers | 我们在古兰经中降示对信道者的治疗和慈恩，但它只增加不义者的损失。 | PRESERVED |
| 17:83 (PRESERVED) | 0 | When We favor the human, he turns away and holds himself apart | 当我们施恩于人时，他转身离去， | PRESERVED |
| 17:86 (PRESERVED) | 0 | If We willed | 如果我们意欲，我们必定夺去我们启示给你的。 | PRESERVED |
| 17:86 (PRESERVED) | 1 | We would surely take away what We inspired to you | 如果我们意欲，我们必定夺去我们启示给你的。 | PRESERVED |
| 17:86 (PRESERVED) | 2 | then you would find no guardian for you against Us in it. | 我们必定夺去我们启示给你的。然后你找不到对抗我们的保护者。 | PRESERVED |
| 17:89 (PRESERVED) | 0 | We varied for people in this Quran every kind of example | 我们已在这部古兰经中为人类阐明了各种比喻，但大多数人只坚持否认真理。 | PRESERVED |
| 17:95 (PRESERVED) | 0 | We would have sent down to them an angel as messenger from the sky." | 你说：“如果大地上有安然行走的天使，我们必定从天上降下一位天使做使者给他们。 | PRESERVED |
| 17:97 (PRESERVED) | 0 | We will gather them on the Day of Resurrection on their faces | 复活日，我们将把他们集合起来，他们的脸朝下， | PRESERVED |
| 17:97 (PRESERVED) | 1 | We add to them a blaze. | 每当火势减弱，我们就为他们加旺火焰。 | PRESERVED |
| 17:98 (PRESERVED) | 0 | That is their recompense for disbelieving in Our signs, and saying, "When we are bones and dust | 因为他们否认我们的迹象，并且说：“当我们已变成枯骨和碎片时， | PRESERVED |
| 17:101 (PRESERVED) | 0 | We gave Moses nine clear signs | 我们赐给摩西九种明显的迹象——你去问以色列的后裔。当他来到他们那里时， | PRESERVED |
| 17:103 (PRESERVED) | 0 | so We drowned him and those with him, all. | 他决心把他们吓出这块土地，但我们淹死了他和与他在一起的全体。 | PRESERVED |
| 17:104 (PRESERVED) | 0 | After him We said to the children of Israel, "Dwell in the land | 在他之后，我们对以色列的后裔说： | PRESERVED |
| 17:104 (PRESERVED) | 1 | We will bring you all mixed together." | 当后世的许约到来时，我们将把你们全体带来。” | PRESERVED |
| 17:105 (PRESERVED) | 0 | With the truth We sent it down, and with the truth it came down. | 我们依真理降示了它，它也依真理降下。 | PRESERVED |
| 17:105 (PRESERVED) | 1 | We sent you only as a bearer of glad news and a warner. | 我们依真理降示了它，它也依真理降下。我们只派遣你做报喜者和警告者。 | PRESERVED |
| 17:106 (PRESERVED) | 0 | We divided it, to recite it to people over time | 一部古兰经，我们把它分开， | PRESERVED |
| 17:106 (PRESERVED) | 1 | and We sent it down in stages. | 我们把它分开，为要你慢慢地诵读给人们听。我们分阶段降示了它。 | PRESERVED |

### Surah 18

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 18:7 (PRESERVED) | 0 | We made what is on the earth an adornment for it, to test them: which of them does best in deeds. | 我们把大地上的东西作为它的装饰，为考验他们， | PRESERVED |
| 18:8 (PRESERVED) | 0 | And We will make what is on it a barren waste. | 我们必定把地上的东西变成荒芜的废墟。 | PRESERVED |
| 18:9 (PRESERVED) | 0 | Did you think the companions of the Cave and the inscription were a wonder among Our signs? | 难道你认为山洞的众人和铭文确是我们的奇妙迹象吗？ | PRESERVED |
| 18:11 (PRESERVED) | 0 | So We sealed their ears in the cave for a number of years. | 然后我们在山洞中封闭了他们的耳朵多年。 | PRESERVED |
| 18:12 (PRESERVED) | 0 | Then We raised them, to know which of the two parties counted best how long they stayed. | 然后我们唤醒他们，为知道两派中哪一派更能计算他们逗留的期限。 | PRESERVED |
| 18:13 (PRESERVED) | 0 | We tell you their story with the truth. | 我们据实向你讲述他们的故事。他们是信他们的一些青年， | PRESERVED |
| 18:13 (PRESERVED) | 1 | and We added to their guidance. | 他们是信他们的一些青年，我们增加了他们的引导。 | PRESERVED |
| 18:14 (PRESERVED) | 0 | We strengthened their hearts when they stood and said, "Our Lord is the Lord of the heavens and the earth | 我们坚定了他们的心，当他们站起来说： | PRESERVED |
| 18:18 (PRESERVED) | 0 | We turned them to the right and to the left | 你以为他们是醒着的，而他们在睡觉。我们使他们向右翻、 | PRESERVED |
| 18:19 (PRESERVED) | 0 | So We raised them, to question one another. | 就这样，我们唤醒了他们， | PRESERVED |
| 18:21 (PRESERVED) | 0 | So We caused them to be found, that they might know God's promise is true, and that the Hour has no doubt in it | 就这样，我们使他们被发现， | PRESERVED |
| 18:28 (PRESERVED) | 0 | Do not obey one whose heart We made heedless of Our remembrance, who followed his desire, and whose case is one of excess. | 不要把你的目光从他们身上移开，渴望今世的浮华。不要服从那个我们使他的心疏忽记念我们的人——于是他追随自己的私欲——他的事情是混乱的。 | PRESERVED |
| 18:29 (PRESERVED) | 0 | and whoever wills, let him disbelieve." We prepared for the wrongdoers a Fire whose walls close around them. | 就让他信；谁愿意，就让他不信。 | PRESERVED |
| 18:30 (PRESERVED) | 0 | We do not waste the reward of one who does best in deeds. | 至于那些信道且品行端正的人——我们绝不浪费行善者的报酬。 | PRESERVED |
| 18:32 (PRESERVED) | 0 | Set forth for them a parable of two men: We made for one of them two gardens of grapes, ringed them with palms, and set crops between them. | 你为他们举两个人的比喻。我们赐给其中一人两座葡萄园，我们用椰枣树环绕它们， | PRESERVED |
| 18:33 (PRESERVED) | 0 | and We made a river burst between them. | 两座园子都产出丰足的收成，毫无损失。我们使一条河流穿过它们。 | PRESERVED |
| 18:45 (PRESERVED) | 0 | Set forth for them the likeness of the worldly life: like water We sent down from the sky | 你为他们举今世的比喻：就像我们从天上降下的水，大地的植物吸收了它； | PRESERVED |
| 18:47 (PRESERVED) | 0 | A Day when We move the mountains, and you see the earth laid bare | 在那日，我们使群山移动； | PRESERVED |
| 18:47 (PRESERVED) | 1 | and We gathered them, leaving none behind. | 你看见大地显露；我们把他们集合起来，不遗留一人。 | PRESERVED |
| 18:48 (PRESERVED) | 0 | "You came to Us as We created you the first time. | 他们将成排地被带到你的主面前。“你们确已来到我们这里，如同我们初次创造你们时。 | PRESERVED |
| 18:48 (PRESERVED) | 1 | you claimed We would set no appointed meeting for you." | 如同我们初次创造你们时。虽然你们曾声称我们不会为你们设定约会。” | PRESERVED |
| 18:50 (PRESERVED) | 0 | When We said to the angels, "Bow down to Adam" | 当时我们对天使们说：“你们向亚当叩头。 | PRESERVED |
| 18:52 (PRESERVED) | 0 | and We set a deadly gulf between them. | ”他们呼唤他们，但他们不回应他们。我们在他们之间设置一道屏障。 | PRESERVED |
| 18:54 (PRESERVED) | 0 | We varied in this Quran for people every kind of example | 我们已在这部古兰经中为人们阐明了各种比喻，但人类是最爱争论的。 | PRESERVED |
| 18:56 (PRESERVED) | 0 | We send the messengers only as bearers of glad news and warners. | 我们只派遣使者们做报喜者和警告者。不信道者用虚妄争论， | PRESERVED |
| 18:57 (PRESERVED) | 0 | We set coverings over their hearts, lest they understand it, and deafness in their ears. | 他却转身离去，忘记他的双手所做的一切？我们在他们心上覆盖了帷幕， | PRESERVED |
| 18:59 (PRESERVED) | 0 | We destroyed them when they did wrong | 这些城市——当它们不义时，我们毁灭了它们， | PRESERVED |
| 18:59 (PRESERVED) | 1 | and We set an appointed time for their destruction. | 这些城市——当它们不义时，我们毁灭了它们，我们为它们的毁灭规定了期限。 | PRESERVED |
| 18:65 (PRESERVED) | 0 | We gave him mercy from Us, and taught him knowledge from Ourselves. | 然后他们遇见我们的一位仆人，我们从我们那里赐给他慈恩， | PRESERVED |
| 18:81 (PRESERVED) | 0 | We wanted their Lord to replace him for them with one better in purity and nearer in mercy. | 所以我们想让他们的主以一个在纯洁上更好、在慈爱上更近的孩子代替他。 | PRESERVED |
| 18:84 (PRESERVED) | 0 | We established him on the earth, and gave him a way to everything. | 我们在大地上确立了他，赐给他各种途径。 | PRESERVED |
| 18:86 (PRESERVED) | 0 | We said, "O Dhu al-Qarnayn | “祖勒盖尔奈英啊，你可以惩罚他们，或善待他们。 | PRESERVED |
| 18:90 (PRESERVED) | 0 | he found it rising on a people for whom We made no shelter from it. | 发现太阳升在一个民族之上，我们没有为他们在太阳之外设置遮蔽。 | PRESERVED |
| 18:91 (PRESERVED) | 0 | and We encompassed what he had in knowledge. | 就是这样。我们确已完全知道他所拥有的一切。 | PRESERVED |
| 18:99 (PRESERVED) | 0 | We left them that Day surging over one another | 在那日，我们让他们互相冲击。 | PRESERVED |
| 18:99 (PRESERVED) | 1 | and We gathered them together. | 号角将被吹响，我们把他们集合起来。 | PRESERVED |
| 18:100 (PRESERVED) | 0 | We displayed Hell that Day to the disbelievers, on display. | 在那日，我们把火狱展示给不信道者， | PRESERVED |
| 18:102 (PRESERVED) | 0 | We prepared Hell as a lodging for the disbelievers. | 不信道者以为他们能在我之外把我的仆人们当作保护者吗？我们已为不信道者预备了火狱作为款待。 | PRESERVED |
| 18:103 (FLATTENED) | 0 | Say, "Shall We tell you of the greatest losers in deeds? | 你说：“我告诉你们行为上损失最大的人吗？ | FLATTENED |
| 18:105 (PRESERVED) | 0 | We will set up no weight for them on the Day of Resurrection. | 所以他们的行为是徒劳的。复活日，我们不给他们称量。 | PRESERVED |
| 18:109 (PRESERVED) | 0 | even if We brought its like as more." | 在我主的言辞用完之前，海洋必定用完，”即使我们再带来同样多的来补充。 | PRESERVED |

### Surah 19

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 19:7 (PRESERVED) | 0 | We bring you good news of a boy. | “撒迦利亚啊，我们向你报喜： | PRESERVED |
| 19:7 (PRESERVED) | 1 | No one before him did We name with that name. | 他的名字是约翰，我们以前没有给任何人取过这个名字。” | PRESERVED |
| 19:12 (PRESERVED) | 0 | And We gave him wisdom while he was still a boy. | “约翰啊，你要紧握经典。”我们在他年幼时赐给他智慧。 | PRESERVED |
| 19:13 (PRESERVED) | 0 | And tenderness from Us, and purity. | 并从我们这里赐给他慈爱和纯洁。他是敬畏的。 | PRESERVED |
| 19:17 (PRESERVED) | 0 | and We sent her Our spirit, and he showed himself to her as a man, full and well-formed. | 她在他们之外设置了屏障，我们派我们的灵到她那里，他在她面前显现为一个完美的人。 | PRESERVED |
| 19:21 (PRESERVED) | 0 | And We will make him a sign to people, and a mercy from Us. | 你的主说：‘这对我是容易的，我们要使他成为人类的迹象， | PRESERVED |
| 19:38 (PRESERVED) | 0 | How well they will hear, and how well they will see, the day they come to Us. | 你听他们吧，看他们吧。但今天不义者完全迷误。 | PRESERVED |
| 19:40 (PRESERVED) | 0 | We | 我们必定继承大地和地上的一切，他们将被送回我们这里。 | PRESERVED |
| 19:40 (PRESERVED) | 1 | We alone inherit the earth and all who are on it, and to Us they are returned. | 我们必定继承大地和地上的一切，他们将被送回我们这里。 | PRESERVED |
| 19:49 (PRESERVED) | 0 | We gave him Isaac and Jacob. | 以及他们在真主之外所崇拜的，我们赐给他以撒和雅各。我们使他们每人都成为先知。 | PRESERVED |
| 19:49 (PRESERVED) | 1 | And each We made a prophet. | 我们赐给他以撒和雅各。我们使他们每人都成为先知。 | PRESERVED |
| 19:50 (PRESERVED) | 0 | And We gave them of Our mercy | 我们从我们的慈恩中赐给他们，并赐给他们崇高的诚实声誉。 | PRESERVED |
| 19:50 (PRESERVED) | 1 | and We gave them a tongue of truth, raised high. | 我们从我们的慈恩中赐给他们，并赐给他们崇高的诚实声誉。 | PRESERVED |
| 19:52 (PRESERVED) | 0 | And We called to him from the right side of the Mount, and drew him near, in close speech. | 我们从山的右侧召唤他，使他接近， | PRESERVED |
| 19:53 (PRESERVED) | 0 | And We gave him, of Our mercy, his brother Aaron, a prophet. | 出于我们的慈恩，我们把他的兄弟亚伦赐给他做先知。 | PRESERVED |
| 19:57 (PRESERVED) | 0 | And We raised him to a high place. | 我们把他提升到崇高的地位。 | PRESERVED |
| 19:58 (PRESERVED) | 0 | from the seed of Adam, and from those We carried with Noah, and from the seed of Abraham and Israel, and from those We guided and chose. | 出自亚当的后裔，出自我们与挪亚一同载过的，出自亚伯拉罕和以色列的后裔， | PRESERVED |
| 19:63 (PRESERVED) | 0 | That is the Garden We pass down as an inheritance to those of Our servants who guard themselves. | 这就是乐园，我们将把它继承给我们敬畏的仆人们。 | PRESERVED |
| 19:67 (PRESERVED) | 0 | Does man not remember that We made him before, and he was nothing? | 人难道不记得我们以前创造了他，而他一无所有吗？ | PRESERVED |
| 19:68 (PRESERVED) | 0 | We will gather them, and the devils | 以你的主发誓，我们必定集合他们和恶魔们， | PRESERVED |
| 19:68 (PRESERVED) | 1 | then We will bring them around Hell, kneeling. | 以你的主发誓，我们必定集合他们和恶魔们，然后使他们跪在火狱周围。 | PRESERVED |
| 19:69 (PRESERVED) | 0 | Then from every group We will seize those most hardened against the Beneficent. | 然后，我们从每个派别中揪出对至仁主最悖逆的人。 | PRESERVED |
| 19:70 (PRESERVED) | 0 | Then We best know who most deserves to be burned in it. | 我们最知道谁最该在其中受烤。 | PRESERVED |
| 19:72 (PRESERVED) | 0 | Then We will save those who guarded themselves, and leave the wrongdoers in it, kneeling. | 然后我们拯救敬畏的人，让不义者跪在其中。 | PRESERVED |
| 19:73 (PRESERVED) | 0 | And when Our clear signs are read to them, the disbelievers say to the believers, Which of the two groups stands better, and keeps better company? | 当我们的明显迹象被诵读给他们时，不信道者对信道者说： | PRESERVED |
| 19:74 (PRESERVED) | 0 | And how many a generation We destroyed before them | 在他们之前，我们毁灭了多少世代， | PRESERVED |
| 19:77 (PRESERVED) | 0 | Have you seen the one who disbelieved in Our signs and said, I will be given wealth and children? | 你看见那个否认我们的迹象、说“我必定被赐予财富和子女”的人了吗？ | PRESERVED |
| 19:79 (PRESERVED) | 0 | We will write down what he says, and stretch out his punishment, stretch by stretch. | 绝不！我们要记录他所说的， | PRESERVED |
| 19:80 (PRESERVED) | 0 | And We will inherit what he brags of, and he will come to Us alone. | 然后我们继承他所说的，他将独自来到我们这里。 | PRESERVED |
| 19:83 (PRESERVED) | 0 | Do you not see that We sent the devils against the disbelievers, driving them hard? | 你没看见我们怎样把恶魔们派到不信道者那里去煽动他们吗？ | PRESERVED |
| 19:84 (PRESERVED) | 0 | We are counting them down, day by day. | 所以不要对他们性急。我们在为他们倒数计时。 | PRESERVED |
| 19:85 (PRESERVED) | 0 | The day We gather the righteous to the Beneficent as an honored company. | 在那日，我们把敬畏者作为贵宾集合到至慈主那里。 | PRESERVED |
| 19:97 (PRESERVED) | 0 | We made it easy on your tongue, to bring good news with it to the righteous, and to warn with it a people hardened in dispute. | 我们使它在你的舌头上容易，为要你以此向敬畏者报喜， | PRESERVED |
| 19:98 (PRESERVED) | 0 | And how many a generation We destroyed before them. | 在他们之前，我们毁灭了多少世代！ | PRESERVED |

### Surah 20

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 20:2 (PRESERVED) | 0 | We did not send the Quran down on you to make you suffer. | 我们降示古兰经给你，不是为使你受苦。 | PRESERVED |
| 20:21 (PRESERVED) | 0 | We will return it to what it was at first. | 他说：“抓住它，不要怕。 | PRESERVED |
| 20:23 (PRESERVED) | 0 | To show you some of Our greatest signs. | 为要我们让你看见我们的一些大迹象。 | PRESERVED |
| 20:37 (PRESERVED) | 0 | And We favored you another time, before. | 我们确已在另一次施恩于你。 | PRESERVED |
| 20:38 (PRESERVED) | 0 | When We revealed to your mother what was revealed. | 当时我们启示你的母亲当启示的事。 | PRESERVED |
| 20:40 (PRESERVED) | 0 | Then We returned you to your mother, so her eyes would be set at rest, and she would not grieve. | 说：‘我告诉你们一个能抚养他的人吗？’于是我们把你送回你的母亲， | PRESERVED |
| 20:40 (PRESERVED) | 1 | and We saved you from the distress | 不忧愁。你杀了一个人，但我们拯救你脱离忧患； | PRESERVED |
| 20:40 (PRESERVED) | 2 | and We tried you with trials. | 你杀了一个人，但我们拯救你脱离忧患；我们彻底考验了你。 | PRESERVED |
| 20:45 (PRESERVED) | 0 | They said, Our Lord, we fear he may overstep against us, or go too far. | 他们说：“我们的主啊， | PRESERVED |
| 20:50 (PRESERVED) | 0 | He said, Our Lord is the One who gave everything its shape, then guided it. | 他说：“我们的主是赋予万物存在、 | PRESERVED |
| 20:53 (PRESERVED) | 0 | and We brought out with it pairs of every kind of plant. | 并在其中为你们开辟道路，从天上降下水，我们以此生出成双成对的各种植物。 | PRESERVED |
| 20:55 (PRESERVED) | 0 | From it We made you, and into it We return you, and from it We will bring you out once more. | 我们用它创造你们，我们使你们回归它， | PRESERVED |
| 20:56 (PRESERVED) | 0 | And We showed him all Our signs, and he called them lies and refused. | 我们把我们的迹象全部展示给他，但他否认并拒绝。 | PRESERVED |
| 20:58 (PRESERVED) | 0 | We will bring you magic like it. | 我们必定给你带来像它一样的魔术；你在我们与你之间定一个约期， | PRESERVED |
| 20:68 (PRESERVED) | 0 | We said, Do not fear. | 我们说：“不要怕， | PRESERVED |
| 20:72 (PRESERVED) | 0 | We will not put you above what came to us of the clear proofs, and the One who made us. | 他们说：“我们不会把你置于已来临我们的明证和创造我们的主之上。 | PRESERVED |
| 20:73 (PRESERVED) | 0 | We believe in our Lord, that He may forgive us our sins, and the magic you forced on us. | 我们已信我们的主，为要他饶恕我们的罪， | PRESERVED |
| 20:77 (PRESERVED) | 0 | And We revealed to Moses, Travel by night with My servants, and strike for them a dry road through the sea. | 我们启示摩西：“夜间带着我的仆人们出发， | PRESERVED |
| 20:80 (PRESERVED) | 0 | We saved you from your enemy | 以色列的后裔啊！我们确已拯救你们脱离你们的敌人， | PRESERVED |
| 20:80 (PRESERVED) | 1 | and We appointed for you the right side of the Mount, and sent down on you the manna and the quail. | 以色列的后裔啊！我们确已拯救你们脱离你们的敌人，在山的右侧与你们约定， | PRESERVED |
| 20:81 (PRESERVED) | 0 | Eat of the good things We provided you, and do not overstep in it, or My anger will fall on you. | 你们吃我们供给你们的佳美食物吧，但不要在其中过分， | PRESERVED |
| 20:85 (PRESERVED) | 0 | We have tried your people after you left, and the Samarian led them astray. | 他说：“在你之后， | PRESERVED |
| 20:87 (PRESERVED) | 0 | We did not break our word to you by our own will. | 他们说：“我们违背对你的许约不是出于自愿， | PRESERVED |
| 20:91 (PRESERVED) | 0 | We will not stop devoting ourselves to it until Moses returns to us. | 他们说：“在摩西回到我们这里之前， | PRESERVED |
| 20:97 (PRESERVED) | 0 | We will burn it, then scatter it in the sea, scattering. | 你看你一直崇拜的神——我们必定烧掉它，然后把它吹散到海里，化为粉末。 | PRESERVED |
| 20:99 (PRESERVED) | 0 | So We tell you some of the tidings of what went before. | 这样，我们向你叙述已往时代的消息； | PRESERVED |
| 20:99 (PRESERVED) | 1 | And We have given you, from Us, a remembrance. | 这样，我们向你叙述已往时代的消息；我们确已从我们这里赐给你教诲。 | PRESERVED |
| 20:102 (PRESERVED) | 0 | and We gather the guilty that day, bleary-eyed. | 在那日，号角被吹响——在那日我们把罪人们集合起来，他们发青。 | PRESERVED |
| 20:104 (PRESERVED) | 0 | We best know what they say, when the most upright of them says, You stayed only a day. | 我们最知道他们所说的，当时他们中行为最端正的人说： | PRESERVED |
| 20:113 (PRESERVED) | 0 | And so We sent it down, an Arabic Quran, and turned the warnings over in it, so they may guard themselves, or it may stir in them a remembrance. | 这样，我们降示它为阿拉伯文的古兰经， | PRESERVED |
| 20:115 (PRESERVED) | 0 | And We took a pledge from Adam before, and he forgot. | 我们以前确已与亚当立约，但他忘记了， | PRESERVED |
| 20:115 (PRESERVED) | 1 | We found no firm resolve in him. | 我们以前确已与亚当立约，但他忘记了，我们在他身上找不到决心。 | PRESERVED |
| 20:116 (PRESERVED) | 0 | And when We said to the angels, Bow down to Adam | 当时我们对天使们说：“你们向亚当叩头。 | PRESERVED |
| 20:117 (PRESERVED) | 0 | Then We said, O Adam, this is an enemy to you and to your wife. | 我们说：“亚当啊， | PRESERVED |
| 20:124 (PRESERVED) | 0 | and We will gather him on the Day of Resurrection, blind. | 复活日，我们使他瞎眼复活。” | PRESERVED |
| 20:126 (PRESERVED) | 0 | Our signs came to you, and you forgot them. | 他说：“就是这样。我们的迹象来到你， | PRESERVED |
| 20:127 (PRESERVED) | 0 | And so We repay whoever oversteps and does not believe in the signs of his Lord. | 我们这样报偿越轨、不信他的主的迹象的人。 | PRESERVED |
| 20:128 (PRESERVED) | 0 | how many a generation We destroyed before them, in whose dwellings they now walk? | 难道对他们没有教训吗？在他们之前我们毁灭了多少世代，他们在他们的住处行走？ | PRESERVED |
| 20:131 (PRESERVED) | 0 | And do not stretch your eyes toward what We let some of them enjoy | 不要把你的目光投向我们让他们中的一些人享受的——今世生活的繁华——为要我们以此考验他们。你的主的给养更好， | PRESERVED |
| 20:132 (PRESERVED) | 0 | We do not ask you for provision. | 你要命令家人谨守礼拜，坚持不懈。我们不向你要给养， | PRESERVED |
| 20:132 (PRESERVED) | 1 | We provide for you. | 我们不向你要给养，是我们供给你的。善果属于敬畏。 | PRESERVED |
| 20:134 (PRESERVED) | 0 | And if We had destroyed them with punishment before it, they would have said, Our Lord, if only You had sent us a messenger, we would have followed Your signs, before we were humbled and disgraced. | 如果我们在他之前以刑罚毁灭他们，他们必定说： | PRESERVED |

### Surah 21

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 21:6 (PRESERVED) | 0 | No town believed before them that We destroyed. | 在他们之前我们毁灭的城市没有一个信了。难道他们会信吗？ | PRESERVED |
| 21:7 (PRESERVED) | 0 | And We sent no one before you but men We revealed to. | 在你之前，我们只派遣我们启示的男人。 | PRESERVED |
| 21:8 (PRESERVED) | 0 | And We did not make them bodies that eat no food, and they were not to last forever. | 我们没有使他们成为不吃食物的躯体，他们也不是永生的。 | PRESERVED |
| 21:9 (PRESERVED) | 0 | Then We kept Our promise to them. | 然后我们对他们实现了许约，拯救了他们和我们所意欲的人， | PRESERVED |
| 21:9 (PRESERVED) | 1 | We saved them, and those We willed | 然后我们对他们实现了许约，拯救了他们和我们所意欲的人， | PRESERVED |
| 21:9 (PRESERVED) | 2 | and We destroyed the oversteppers. | 拯救了他们和我们所意欲的人，毁灭了过分的人。 | PRESERVED |
| 21:10 (PRESERVED) | 0 | We have sent down to you a Book in which is your remembrance. | 我们确已降示给你们一部经典，其中有你们的教诲。 | PRESERVED |
| 21:11 (PRESERVED) | 0 | And how many a town We crushed that did wrong, and raised up after it another people. | 我们粉碎了多少作恶的城市，此后建立了另一民族？ | PRESERVED |
| 21:12 (PRESERVED) | 0 | Then when they felt Our might | 当他们感觉到我们的威力时，他们开始逃跑。 | PRESERVED |
| 21:15 (PRESERVED) | 0 | And that cry of theirs did not leave them, until We made them like a harvested field, gone silent. | 这一直是他们的呼喊，直到我们使他们成为寂静的灰烬。 | PRESERVED |
| 21:16 (PRESERVED) | 0 | And We did not make the heaven and the earth, and what is between them, as a game. | 我们创造天与地及其间的一切，不是为了游戏。 | PRESERVED |
| 21:17 (PRESERVED) | 0 | If We had wanted a pastime | 如果我们想要游戏，我们会在我们自身中找到它， | PRESERVED |
| 21:17 (PRESERVED) | 1 | We would have taken it from what is with Us | 如果我们想要游戏，我们会在我们自身中找到它， | PRESERVED |
| 21:17 (PRESERVED) | 2 | if We did such things at all. | 我们会在我们自身中找到它，如果我们要做的话。 | PRESERVED |
| 21:18 (PRESERVED) | 0 | We hurl the truth at the falsehood, and it crushes it, and there it lies, vanishing. | 事实上，我们以真理打击虚妄， | PRESERVED |
| 21:25 (PRESERVED) | 0 | And We sent no messenger before you but We revealed to him, There is no god but I | 在你之前，我们未曾派遣一位使者而不启示他： | PRESERVED |
| 21:29 (PRESERVED) | 0 | him We repay with Hell. | 他们中谁说“我是他之外的神明”，我们就以火狱报偿他。我们这样报偿不义者。 | PRESERVED |
| 21:29 (PRESERVED) | 1 | So We repay the wrongdoers. | 我们就以火狱报偿他。我们这样报偿不义者。 | PRESERVED |
| 21:30 (PRESERVED) | 0 | and We split them? | 诸天与大地本是一团，我们把它们分开。我们用水造出一切生物。 | PRESERVED |
| 21:30 (PRESERVED) | 1 | And We made every living thing from water. | 我们把它们分开。我们用水造出一切生物。难道他们不信吗？ | PRESERVED |
| 21:31 (PRESERVED) | 0 | And We set firm mountains in the earth, so it would not shake with them | 我们在大地上设置了稳固的山，以免它随他们摇动， | PRESERVED |
| 21:31 (PRESERVED) | 1 | and We set through it wide roads, so they may find the way. | 以免它随他们摇动，我们在其中设置了通道和道路，为要他们得正道。 | PRESERVED |
| 21:32 (PRESERVED) | 0 | And We made the sky a guarded roof | 我们把天空作为受保护的天篷；但他们转身离去它的迹象。 | PRESERVED |
| 21:34 (PRESERVED) | 0 | And We did not grant any human before you lasting life. | 在你之前，我们没有给任何凡人永生。 | PRESERVED |
| 21:35 (PRESERVED) | 0 | And We test you with bad and good, as a trial. | 每个灵魂都要尝死亡。我们以祸福考验你们——一种考验。 | PRESERVED |
| 21:35 (PRESERVED) | 1 | And to Us you are returned. | 我们以祸福考验你们——一种考验。你们将被送回我们这里。 | PRESERVED |
| 21:43 (PRESERVED) | 0 | Or do they have gods to shield them from Us? | 难道他们有神明能在我们之外保护他们吗？他们无力自助，也得不到我们的保护。 | PRESERVED |
| 21:43 (PRESERVED) | 1 | They cannot help themselves, and they have no protector from Us. | 他们无力自助，也得不到我们的保护。 | PRESERVED |
| 21:44 (PRESERVED) | 0 | We let them and their fathers enjoy life, until life grew long for them. | 我们让这些人和他们的祖先享受，直到岁月在他们身上漫长。 | PRESERVED |
| 21:44 (PRESERVED) | 1 | Do they not see that We come to the land, shrinking it from its edges? | 直到岁月在他们身上漫长。难道他们没看见我们怎样从四周减少大地吗？难道他们是胜利者吗？ | PRESERVED |
| 21:47 (PRESERVED) | 0 | And We set the just scales for the Day of Resurrection. | 复活日，我们将设立公正的天平， | PRESERVED |
| 21:47 (PRESERVED) | 1 | We bring it. | 即使是一粒芥菜种的重量，我们也会带来。我们作为清算者是足够的。 | PRESERVED |
| 21:47 (PRESERVED) | 2 | And We are enough as reckoners. | 我们也会带来。我们作为清算者是足够的。 | PRESERVED |
| 21:48 (PRESERVED) | 0 | And We gave Moses and Aaron the Criterion, and a light, and a reminder for the righteous. | 我们赐给摩西和亚伦辨别的经典、光明和给敬畏者的教诲。 | PRESERVED |
| 21:50 (PRESERVED) | 0 | And this is a blessed reminder We sent down. | 这也是我们降示的受祝福的教诲。难道你们要否认它吗？ | PRESERVED |
| 21:51 (PRESERVED) | 0 | And We gave Abraham his right judgment before | 我们以前确已赐给亚伯拉罕正道，我们深知他。 | PRESERVED |
| 21:51 (PRESERVED) | 1 | and We knew him well. | 我们以前确已赐给亚伯拉罕正道，我们深知他。 | PRESERVED |
| 21:60 (PRESERVED) | 0 | We heard a young man speak against them. | 他们说：“我们听见一个青年提到它们。 | PRESERVED |
| 21:69 (PRESERVED) | 0 | We said, O fire, be cool, and safe, for Abraham. | 我们说：“火啊， | PRESERVED |
| 21:70 (PRESERVED) | 0 | and We made them the greatest losers. | 他们图谋害他，但我们使他们成为损失最大的人。 | PRESERVED |
| 21:71 (PRESERVED) | 0 | And We saved him, and Lot, to the land We blessed for the worlds. | 我们拯救了他和罗得，到我们为众世界祝福的大地。 | PRESERVED |
| 21:72 (PRESERVED) | 0 | And We gave him Isaac, and Jacob as a grandson. | 我们赐给他以撒和雅各作为恩赐；我们使他们每人都成为敬畏者。 | PRESERVED |
| 21:72 (PRESERVED) | 1 | And each We made righteous. | 我们赐给他以撒和雅各作为恩赐；我们使他们每人都成为敬畏者。 | PRESERVED |
| 21:73 (PRESERVED) | 0 | And We made them leaders, guiding by Our command. | 我们使他们成为领袖，奉我们的命令引导； | PRESERVED |
| 21:73 (PRESERVED) | 1 | And We revealed to them the doing of good deeds, and keeping up the prayer, and giving the zakat. | 我们使他们成为领袖，奉我们的命令引导；我们启示他们行善、 | PRESERVED |
| 21:73 (PRESERVED) | 2 | And they were worshipers of Us. | 完纳天课。他们是侍奉我们的仆人。 | PRESERVED |
| 21:74 (PRESERVED) | 0 | We gave him judgment and knowledge, and saved him from the town that worked filth. | 罗得——我们赐给他判断和知识，拯救他脱离做丑事的城市。 | PRESERVED |
| 21:75 (PRESERVED) | 0 | And We brought him into Our mercy. | 我们使他进入我们的慈恩；他确是敬畏者之一。 | PRESERVED |
| 21:76 (PRESERVED) | 0 | We answered him, and saved him and his people from the great distress. | 挪亚，当时他以前祈求。于是我们应答了他， | PRESERVED |
| 21:77 (PRESERVED) | 0 | And We helped him against the people who called Our signs lies. | 我们援助他对抗否认我们的迹象的民族。他们是邪恶的民族， | PRESERVED |
| 21:77 (PRESERVED) | 1 | so We drowned them all. | 他们是邪恶的民族，所以我们淹死了他们全体。 | PRESERVED |
| 21:78 (PRESERVED) | 0 | And We watched their judgment. | 当时一些人的羊群夜间在其中游荡；我们是他们判决的见证者。 | PRESERVED |
| 21:79 (PRESERVED) | 0 | And We gave Solomon the understanding of it. | 于是我们使所罗门理解它，我们赐给他们每人智慧和知识。 | PRESERVED |
| 21:79 (PRESERVED) | 1 | And each We gave judgment and knowledge. | 于是我们使所罗门理解它，我们赐给他们每人智慧和知识。我们使群山与大卫一起赞颂我们， | PRESERVED |
| 21:79 (PRESERVED) | 2 | And We made the mountains glorify with David, and the birds. | 我们赐给他们每人智慧和知识。我们使群山与大卫一起赞颂我们，飞鸟也一样——我们确这样做了。 | PRESERVED |
| 21:79 (PRESERVED) | 3 | And We did it. | 我们使群山与大卫一起赞颂我们，飞鸟也一样——我们确这样做了。 | PRESERVED |
| 21:80 (PRESERVED) | 0 | And We taught him the making of armor for you, to guard you from your violence. | 我们教他为你们制造盔甲，为保护你们免受你们的暴力。 | PRESERVED |
| 21:81 (PRESERVED) | 0 | And to Solomon the wind, blowing hard, running by his command to the land We blessed. | 奉他的命令吹向我们祝福的大地。我们知道一切。 | PRESERVED |
| 21:81 (PRESERVED) | 1 | And We know all things. | 奉他的命令吹向我们祝福的大地。我们知道一切。 | PRESERVED |
| 21:82 (PRESERVED) | 0 | And We kept watch over them. | 做其他小事的。但我们约束着他们。 | PRESERVED |
| 21:84 (PRESERVED) | 0 | Then We answered him, and lifted the harm from him. | 于是我们应答了他，解除他的痛苦， | PRESERVED |
| 21:84 (PRESERVED) | 1 | And We gave him his people, and as many more with them | 于是我们应答了他，解除他的痛苦，把他的家人还给他， | PRESERVED |
| 21:84 (PRESERVED) | 2 | a mercy from Us, and a reminder for the worshipers. | 把他的家人还给他，并赐给同样多的——出于我们的慈恩，给崇拜者的教诲。 | PRESERVED |
| 21:86 (PRESERVED) | 0 | And We brought them into Our mercy. | 我们使他们进入我们的慈恩。他们确是敬畏者。 | PRESERVED |
| 21:87 (PRESERVED) | 0 | when he went off in anger, and thought We would not hold him to it. | 当时他愤怒地离去，以为我们无力对付他。然后他在黑暗中呼求： | PRESERVED |
| 21:88 (PRESERVED) | 0 | Then We answered him, and saved him from the distress. | 于是我们应答了他，拯救他脱离忧患。 | PRESERVED |
| 21:88 (PRESERVED) | 1 | And so We save the believers. | 拯救他脱离忧患。我们这样拯救信道者。 | PRESERVED |
| 21:90 (PRESERVED) | 0 | Then We answered him, and gave him John, and made his wife sound for him. | 于是我们应答了他，赐给他约翰， | PRESERVED |
| 21:90 (PRESERVED) | 1 | They used to race to good deeds, and call on Us with longing and fear. | 他们曾争先行善，怀着爱和敬畏祈求我们，对我们谦卑。 | PRESERVED |
| 21:90 (PRESERVED) | 2 | And they were humble before Us. | 怀着爱和敬畏祈求我们，对我们谦卑。 | PRESERVED |
| 21:91 (PRESERVED) | 0 | We breathed into her of Our spirit, and made her and her son a sign to the worlds. | 那位守贞的女子。我们把我们的灵吹入她， | PRESERVED |
| 21:93 (PRESERVED) | 0 | Each will return to Us. | 但他们把他们的事务分裂成派别。他们都将回到我们这里。 | PRESERVED |
| 21:94 (PRESERVED) | 0 | And We write it down for him. | 他的努力不会被否认。我们为他记录它。 | PRESERVED |
| 21:95 (PRESERVED) | 0 | And forbidden to a town We destroyed | 我们毁灭的城市有禁令——他们不会回来。 | PRESERVED |
| 21:101 (PRESERVED) | 0 | Those for whom the good has gone before from Us | 至于那些从我们这里应得善果的人——这些人将被使远离它。 | PRESERVED |
| 21:104 (PRESERVED) | 0 | The day We roll up the sky like the rolling of the scroll for the writings. | 在那日，我们卷起天， | PRESERVED |
| 21:104 (PRESERVED) | 1 | As We began the first making | 如同卷起书卷。如同我们开始初次创造，我们将重演——这是我们必须履行的许约。 | PRESERVED |
| 21:104 (PRESERVED) | 2 | We return it. | 如同我们开始初次创造，我们将重演——这是我们必须履行的许约。我们必定实行。 | PRESERVED |
| 21:104 (PRESERVED) | 3 | A promise on Us. | 我们将重演——这是我们必须履行的许约。我们必定实行。 | PRESERVED |
| 21:104 (PRESERVED) | 4 | We will do it. | 我们将重演——这是我们必须履行的许约。我们必定实行。 | PRESERVED |
| 21:105 (PRESERVED) | 0 | And We wrote in the Psalms, after the remembrance, that the earth | 我们确已在诗篇中，在教诲之后写下： | PRESERVED |
| 21:107 (PRESERVED) | 0 | And We sent you only as a mercy to the worlds. | 我们派遣你，只是作为对众世界的慈恩。 | PRESERVED |

### Surah 22

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 22:5 (PRESERVED) | 0 | We made you from dust, then from a drop, then from a clot, then from a lump, shaped and unshaped, to make it plain to you. | 人们啊！如果你们怀疑复活——我们用尘土创造你们，然后用精液， | PRESERVED |
| 22:5 (PRESERVED) | 1 | And We settle in the wombs what We will, for an appointed term. | 然后用成形和未成形的肉块。为向你们阐明。我们把我们所意欲的安置在子宫中， | PRESERVED |
| 22:5 (PRESERVED) | 2 | Then We bring you out as children. | 到定期限，然后我们使你们作为婴儿出来，直到你们达到壮年。 | PRESERVED |
| 22:5 (PRESERVED) | 3 | then when We send water down on it, it stirs, and swells, and grows every lovely pair. | 但当我们降下水，它震动、膨胀， | PRESERVED |
| 22:9 (PRESERVED) | 0 | and We will make him taste the punishment of the burning on the Day of Resurrection. | 为误导人偏离真主的道路。他在今世有羞辱，复活日我们使他尝焚烧的痛苦。 | PRESERVED |
| 22:16 (PRESERVED) | 0 | And so We sent it down as clear signs. | 这样，我们降示它为明显的迹象， | PRESERVED |
| 22:25 (PRESERVED) | 0 | which We made for all people alike, the dweller in it and the visitor | 至于那些不信道、阻挡真主的道路和禁寺——我们已把它平等地指定给全人类，无论居住其中还是路过——并想在其中犯罪渎圣的人——我们使他尝痛苦的刑罚。 | PRESERVED |
| 22:25 (PRESERVED) | 1 | We will make him taste a painful punishment. | 阻挡真主的道路和禁寺——我们已把它平等地指定给全人类，无论居住其中还是路过——并想在其中犯罪渎圣的人——我们使他尝痛苦的刑罚。 | PRESERVED |
| 22:26 (PRESERVED) | 0 | And when We settled for Abraham the place of the House, Do not ascribe anything to Me. | 我们为亚伯拉罕指明天房的地点：“不要把任何物与我同等； | PRESERVED |
| 22:34 (PRESERVED) | 0 | And for every community We set a rite, to mention God's name over what He provided them of the livestock. | 我们为每个民族规定了仪式，为要他们为他供给他们的牲畜而记念真主之名。 | PRESERVED |
| 22:35 (PRESERVED) | 0 | Those whose hearts tremble when God is mentioned, and who bear what strikes them, and keep up the prayer, and give from what We provided them. | 那些谨守礼拜、从我们供给他们的中施舍的人。 | PRESERVED |
| 22:36 (PRESERVED) | 0 | We made them for you among God's sacred rites. | 我们把献祭的牲畜作为真主的圣仪给你们。其中对你们有好处。 | PRESERVED |
| 22:36 (PRESERVED) | 1 | So We made them serve you, so you may be thankful. | 喂养知足的和乞讨的。我们这样使它们顺服你们，为要你们感恩。 | PRESERVED |
| 22:40 (PRESERVED) | 0 | only that they say, Our Lord is God. | 那些无理被逐出家园的人，只因说“我们的主是真主”。若不是真主以一些人抵挡另一些人： | PRESERVED |
| 22:41 (PRESERVED) | 0 | Those who, when We settled them in the land, kept up the prayer, and gave the zakat, and commanded what is right, and forbade what is wrong. | 那些当我们使他们在大地上得势时，谨守礼拜、 | PRESERVED |
| 22:45 (PRESERVED) | 0 | And how many a town We destroyed while it did wrong | 我们毁灭了多少作恶的城市！它们倒塌在屋顶上； | PRESERVED |
| 22:51 (PRESERVED) | 0 | And those who strove against Our signs, trying to defeat them | 但那些对抗我们的迹象的人——这些是火狱的居民。 | PRESERVED |
| 22:52 (PRESERVED) | 0 | And We sent no messenger or prophet before you but, when he hoped, Satan cast into his hope. | 在你之前，我们未曾派遣一位使者或先知， | PRESERVED |
| 22:57 (PRESERVED) | 0 | And the disbelievers, who called Our signs lies | 但那些不信道、否认我们的迹象的人——这些人将有羞辱的刑罚。 | PRESERVED |
| 22:67 (PRESERVED) | 0 | For every community We set a rite they perform. | 我们为每个民族规定了功修，他们遵守它。 | PRESERVED |
| 22:72 (PRESERVED) | 0 | And when Our clear signs are read to them, you see denial in the faces of the disbelievers. | 当我们的明显迹象被诵读给他们时，你会在不信道者的脸上认出厌恶。 | PRESERVED |
| 22:72 (PRESERVED) | 1 | They nearly attack those who read Our signs to them. | 你说：“我告诉你们比那更坏的吗？火狱！ | PRESERVED |

### Surah 23

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 23:12 (FLATTENED) | 0 | And We made man from an extract of clay. | 我确已用泥土的精华创造了人。 | FLATTENED |
| 23:13 (FLATTENED) | 0 | Then We made him a drop, in a firm resting place. | 然后我使他成为精液，存于坚固的容器中。 | FLATTENED |
| 23:14 (FLATTENED) | 0 | Then We made the drop a clot, and made the clot a lump, and made the lump bones, and clothed the bones with flesh. | 然后我使精液变成血块，然后使血块变成肉团， | FLATTENED |
| 23:14 (FLATTENED) | 1 | Then We grew him into another making. | 然后给骨骼穿上肉，然后使它成为另一种生命。真主是至福的， | FLATTENED |
| 23:17 (FLATTENED) | 0 | And We made above you seven paths. | 我在你们之上创造了七条通道，我从不忽视所创造的万物。 | FLATTENED |
| 23:17 (FLATTENED) | 1 | And We are never heedless of the creation. | 我在你们之上创造了七条通道，我从不忽视所创造的万物。 | FLATTENED |
| 23:18 (FLATTENED) | 0 | And We sent water down from the sky in measure, and settled it in the earth. | 我从天空适量地降下雨水，并使之储存在大地中， | FLATTENED |
| 23:18 (FLATTENED) | 1 | And We can take it away. | 并使之储存在大地中，我确能收回它。 | FLATTENED |
| 23:19 (FLATTENED) | 0 | Then We grew for you with it gardens of palms and grapes. | 我借此为你们生产椰枣园和葡萄园，为你们结出丰盛的果实， | FLATTENED |
| 23:21 (FLATTENED) | 0 | We give you to drink from what is in their bellies, and you have many benefits in them, and from them you eat. | 牲畜中确有你们的教训：我让你们饮用它们腹中的东西，你们从它们身上获得许多益处， | FLATTENED |
| 23:23 (FLATTENED) | 0 | And We sent Noah to his people. | 我确已派遣挪亚去教化他的族人。他说： | FLATTENED |
| 23:24 (PRESERVED) | 0 | We never heard of this from our forefathers. | 假如真主意欲，他必会降下天使。我们从远古的祖先那里从未听说过这样的事。 | PRESERVED |
| 23:27 (FLATTENED) | 0 | Then We revealed to him, Make the ship under Our eyes, and by Our revelation. | 于是我启示他：“在我的注视之下， | FLATTENED |
| 23:27 (FLATTENED) | 1 | Then when Our command comes, and the oven boils over | 奉我的启示建造方舟。当我的命令降临，烘炉沸腾时， | FLATTENED |
| 23:30 (FLATTENED) | 0 | And We were testing. | 那其中确有许多迹象。我一直在考验。 | FLATTENED |
| 23:31 (FLATTENED) | 0 | Then We raised up after them another generation. | 然后，在他们之后， | FLATTENED |
| 23:32 (FLATTENED) | 0 | And We sent among them a messenger from them, Worship God. | 我在他们中间派遣了一位来自他们自身的使者：“侍奉真主吧， | FLATTENED |
| 23:33 (FLATTENED) | 0 | And the chiefs of his people, who disbelieved and called the meeting of the Hereafter a lie, and whom We gave ease in the worldly life, said, This is only a man like you. | 否认后世相会的人，我曾使他们在今世过着优渥的生活，他们说： | FLATTENED |
| 23:37 (PRESERVED) | 0 | We die and we live, and we will not be raised. | 只有我们在今世的生活。我们死，我们生， | PRESERVED |
| 23:41 (FLATTENED) | 0 | and We made them scum. | 巨声理所当然地袭击了他们，我使他们变成泡沫。让不义的民众灭亡吧。 | FLATTENED |
| 23:42 (FLATTENED) | 0 | Then We raised up after them other generations. | 然后，在他们之后， | FLATTENED |
| 23:44 (FLATTENED) | 0 | Then We sent Our messengers, one after another. | 然后我相继派遣了我的众使者。每当一位使者来到他的族人那里， | FLATTENED |
| 23:44 (FLATTENED) | 1 | Then We made some follow others, and made them tales. | 他们都否认他。于是我使他们一个接一个地灭亡，使他们成为历史。 | FLATTENED |
| 23:45 (FLATTENED) | 0 | Then We sent Moses and his brother Aaron, with Our signs and plain authority. | 然后我派遣摩西和他的兄弟亚伦，带着我的迹象和明显的权威。 | FLATTENED |
| 23:49 (FLATTENED) | 0 | And We gave Moses the Book, so they might be guided. | 我确已赐给摩西经典，以便他们遵循正道。 | FLATTENED |
| 23:50 (FLATTENED) | 0 | And We made the son of Mary and his mother a sign, and sheltered them on a high hill, with rest and running water. | 我使马利亚之子和他的母亲成为一个迹象，并让他们安居在有安宁和涌泉的高地上。 | FLATTENED |
| 23:55 (FLATTENED) | 0 | Do they think that what We extend to them of wealth and sons. | 难道他们以为，我供给他们的财富和子女， | FLATTENED |
| 23:56 (FLATTENED) | 0 | We are hurrying good to them? | 是我在争先赐予他们福泽吗？不， | FLATTENED |
| 23:62 (FLATTENED) | 0 | And We burden no soul beyond what it can bear. | 我不使任何灵魂负担超出其能力。在我这里有一部秉公记录的册籍， | FLATTENED |
| 23:62 (FLATTENED) | 1 | And with Us is a Book that speaks the truth. | 我不使任何灵魂负担超出其能力。在我这里有一部秉公记录的册籍，他们不会被亏待。 | FLATTENED |
| 23:64 (FLATTENED) | 0 | Until, when We seize their pampered ones with punishment | 直到当我以刑罚惩治他们中的奢靡者时，他们开始哀号。 | FLATTENED |
| 23:65 (FLATTENED) | 0 | You will not be helped by Us. | 今天不要哀号。你们得不到我的援助。 | FLATTENED |
| 23:71 (FLATTENED) | 0 | We brought them their remembrance, and they turn away from their remembrance. | 天地和其中的一切必已毁灭。不，我确已赐给他们教诲， | FLATTENED |
| 23:75 (FLATTENED) | 0 | And if We had mercy on them, and lifted the harm from them, they would persist in their overstepping, wandering blind. | 即使我慈悯他们，解除他们的困苦， | FLATTENED |
| 23:76 (FLATTENED) | 0 | And We seized them with punishment, and they did not humble themselves to their Lord, and did not plead. | 我确已以苦难惩治他们，但他们既不归顺他们的主， | FLATTENED |
| 23:77 (FLATTENED) | 0 | Until, when We opened on them a gate of hard punishment | 直到当我在他们面前打开严刑之门时，他们立刻绝望了。 | FLATTENED |
| 23:90 (FLATTENED) | 0 | We brought them the truth, and they are liars. | 不，我确已把真理赐给他们， | FLATTENED |
| 23:95 (FLATTENED) | 0 | And We can show you what We promise them. | 我确能让你看到我许诺他们的刑罚。 | FLATTENED |
| 23:96 (FLATTENED) | 0 | We best know what they ascribe. | 你以更好的品行回击恶行。我全知他们所描述的。 | FLATTENED |
| 23:106 (PRESERVED) | 0 | They will say, Our Lord, our wretchedness overcame us, and we were a people astray. | 他们会说：“我们的主啊， | PRESERVED |
| 23:115 (FLATTENED) | 0 | Did you think We made you as a game, and you would not be returned to Us? | 难道你们以为我徒然创造了你们，你们不会被召回到我这里吗？ | FLATTENED |

### Surah 24

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 24:1 (FLATTENED) | 0 | We sent it down, and made it binding, and sent down clear signs in it, so that you may take heed. | 这是我降示的一章，我使它成为定制， | FLATTENED |
| 24:34 (FLATTENED) | 0 | We have sent down to you clarifying signs, and an example from those who passed before you, and a warning for the righteous. | 我确已向你们降示阐明的启示、先亡者的前车之鉴， | FLATTENED |
| 24:46 (FLATTENED) | 0 | We have sent down clarifying signs. | 我确已降示阐明的启示，真主引导他所意欲者走上正道。 | FLATTENED |

### Surah 25

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 25:11 (FLATTENED) | 0 | and We have prepared a Blaze for whoever denied the Hour. | 不，他们否认了那时刻，我已为否认那时刻者准备了烈火。 | FLATTENED |
| 25:19 (FLATTENED) | 0 | We will make him taste a great punishment. | 也不能相助。你们中谁行不义，我将使他尝到重大的刑罚。 | FLATTENED |
| 25:20 (FLATTENED) | 0 | We sent no messengers before you but they ate food and walked in the markets. | 在你之前我未曾派遣任何使者，他们不吃饭、 | FLATTENED |
| 25:20 (FLATTENED) | 1 | We made some of you a trial for others | 他们不吃饭、不逛市场。我使你们中的一部分成为另一部分的考验——你们能忍耐吗？ | FLATTENED |
| 25:21 (FLATTENED) | 0 | "Those who do not expect to meet Us said, 'Why were no angels sent down to us, or we see our Lord?' They grew arrogant within themselves and became wildly defiant." | 不期望与我相会的人说：“要是有天使降给我们，或我们能看见我们的主就好了。 | FLATTENED |
| 25:23 (FLATTENED) | 0 | We will turn to the deeds they did and make them scattered dust. | 我将着手处理他们的行为，把它们变成飘散的尘埃。 | FLATTENED |
| 25:31 (FLATTENED) | 0 | So We made for every prophet an enemy from among the criminals. | 同样，我为每位先知从作恶者中安排了敌人。 | FLATTENED |
| 25:32 (FLATTENED) | 0 | We laid it out step by step." | ”这样做是为了坚定你的心，我分阶段降示它。 | FLATTENED |
| 25:33 (FLATTENED) | 0 | They bring you no example but We bring you the truth and the best explanation. | 无论他们带来什么论据，我都给你真理和更好的阐释。 | FLATTENED |
| 25:35 (FLATTENED) | 0 | We gave Moses the Book and placed with him his brother Aaron as his aide. | 我赐给摩西经典，并任命他的兄弟亚伦为他的助手。 | FLATTENED |
| 25:36 (FLATTENED) | 0 | "We said, 'Go to the people who denied Our signs' | 我说：“去教化否认我迹象的民众吧， | FLATTENED |
| 25:36 (FLATTENED) | 1 | and We utterly destroyed them." | “去教化否认我迹象的民众吧，”我彻底毁灭了他们。 | FLATTENED |
| 25:37 (FLATTENED) | 0 | We drowned them and made them a sign for mankind. | 挪亚的族人：当他们否认众使者时，我淹死了他们， | FLATTENED |
| 25:37 (FLATTENED) | 1 | We have prepared a painful punishment for the wrongdoers. | 我淹死了他们，使他们成为对人类的教训。我为不义者准备了痛苦的报应。 | FLATTENED |
| 25:39 (FLATTENED) | 0 | For each We struck examples, and each We crushed completely. | 我为每一方列举了比喻；每一方我都彻底摧毁。 | FLATTENED |
| 25:45 (FLATTENED) | 0 | then We made the sun a guide to it. | 他能使之静止。我使太阳成为它的指示者。 | FLATTENED |
| 25:46 (FLATTENED) | 0 | Then We pulled it back to Us, gently. | 然后我逐渐将它收回。 | FLATTENED |
| 25:48 (FLATTENED) | 0 | And We sent down purifying water from the sky. | 是他派遣报慈悯喜讯的风；我从天空降下纯净的水。 | FLATTENED |
| 25:49 (FLATTENED) | 0 | To give life with it to a dead land, and give drink from it to cattle and many people We created. | 借此复苏死亡的大地，供给饮水给我所创造的众多牲畜和人类。 | FLATTENED |
| 25:50 (FLATTENED) | 0 | We shared it out among them so they would remember | 我在他们之间循环它，以便他们反思， | FLATTENED |
| 25:51 (FLATTENED) | 0 | Had We willed | 如果我意欲，我能向每个城镇派遣一位警告者。 | FLATTENED |
| 25:51 (FLATTENED) | 1 | We would have raised a warner in every town. | 如果我意欲，我能向每个城镇派遣一位警告者。 | FLATTENED |
| 25:56 (FLATTENED) | 0 | We sent you only as a bearer of good news and a warner. | 我派遣你，只作为报喜者和警告者。 | FLATTENED |

### Surah 26

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 26:4 (FLATTENED) | 0 | If We willed | 如果我意欲，我能从天空给他们降下一个迹象， | FLATTENED |
| 26:4 (FLATTENED) | 1 | We could send down a sign to them from the sky, and their necks would stay bowed to it. | 如果我意欲，我能从天空给他们降下一个迹象， | FLATTENED |
| 26:7 (FLATTENED) | 0 | how much We grew in it of every noble kind? | 难道他们没看见大地，看我生产了多少美丽的成对之物吗？ | FLATTENED |
| 26:15 (FLATTENED) | 0 | go, both of you, with Our signs. | “不。你们俩带着我的证据去吧。我将与你们同在， | FLATTENED |
| 26:15 (FLATTENED) | 1 | We are with you, listening.'" | 你们俩带着我的证据去吧。我将与你们同在，倾听。 | FLATTENED |
| 26:16 (PRESERVED) | 0 | Go to Pharaoh and say, 'We are a messenger of the Lord of the worlds.' | 去见法老，说：‘我们是众世界主的使者。 | PRESERVED |
| 26:40 (PRESERVED) | 0 | We may follow the sorcerers, if they are the winners. | 如果魔术师们是胜利者，我们可以追随魔术师们。 | PRESERVED |
| 26:51 (PRESERVED) | 0 | We hope our Lord will forgive us our faults, for being the first of the believers. | 我们渴望我们的主饶恕我们的罪过，因为我们是最先信道的人。 | PRESERVED |
| 26:52 (FLATTENED) | 0 | "And We inspired Moses: 'Travel by night with My servants | 我启示摩西：“夜里带着我的仆人们出发。 | FLATTENED |
| 26:57 (FLATTENED) | 0 | So We drove them out of gardens and springs. | 于是我把他们赶出果园和泉水。 | FLATTENED |
| 26:59 (FLATTENED) | 0 | and We gave it all to the Children of Israel as inheritance. | 就是这样。我使以色列的后裔继承了它们。 | FLATTENED |
| 26:63 (FLATTENED) | 0 | "So We inspired Moses: 'Strike the sea with your staff.' It split, and each part was like a great mountain." | 我启示摩西：“用你的手杖击打大海。 | FLATTENED |
| 26:64 (FLATTENED) | 0 | And We brought the others near. | 在那里，我使另一群人靠近。 | FLATTENED |
| 26:65 (FLATTENED) | 0 | And We saved Moses and all who were with him. | 我拯救了摩西和同他在一起的人，全部。 | FLATTENED |
| 26:66 (FLATTENED) | 0 | Then We drowned the others. | 然后我淹死了其他人。 | FLATTENED |
| 26:119 (FLATTENED) | 0 | So We saved him and those with him in the laden ship. | 于是我拯救了他和同他在一起的人，让他们登上满载的方舟。 | FLATTENED |
| 26:120 (FLATTENED) | 0 | Then We drowned the rest. | 然后我淹死了其余的人。 | FLATTENED |
| 26:139 (FLATTENED) | 0 | and We destroyed them. | 于是他们否认了他，我毁灭了他们。 | FLATTENED |
| 26:170 (FLATTENED) | 0 | So We saved him and his family, all of them. | 于是我拯救了他和他的家属，全部。 | FLATTENED |
| 26:172 (FLATTENED) | 0 | Then We destroyed the others. | 然后我毁灭了其他人。 | FLATTENED |
| 26:173 (FLATTENED) | 0 | And We rained on them a rain | 我给他们降下了雨。被警告者的雨多么可怕。 | FLATTENED |
| 26:198 (FLATTENED) | 0 | Had We sent it down upon one of the non-Arabs. | 假如我把它降给一个外国人， | FLATTENED |
| 26:200 (FLATTENED) | 0 | So We slipped it into the hearts of the criminals. | 我这样使它穿过犯罪者的心。 | FLATTENED |
| 26:204 (FLATTENED) | 0 | Do they seek to hasten Our punishment? | 难道他们催促我的刑罚吗？ | FLATTENED |
| 26:205 (FLATTENED) | 0 | if We let them enjoy themselves for years. | 你想过吗：如果我让他们享乐若干年， | FLATTENED |
| 26:208 (FLATTENED) | 0 | We never destroyed a town but it had warners. | 我未曾毁灭任何城镇，除非它已有警告者。 | FLATTENED |
| 26:209 (FLATTENED) | 0 | and We were never wrongdoers. | 作为提醒——我从不亏待。 | FLATTENED |

### Surah 27

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 27:4 (FLATTENED) | 0 | We made their deeds seem fair to them, so they wander blindly. | 至于不信后世的人：我使他们的行为显得美好，所以他们漫无目的地游荡。 | FLATTENED |
| 27:13 (FLATTENED) | 0 | "When Our signs came to them, clear to see, they said, 'This is clear magic.'" | 当我阐明的迹象降临他们时，他们说： | FLATTENED |
| 27:15 (FLATTENED) | 0 | "We gave David and Solomon knowledge. | 我赐给大卫和所罗门知识。他俩说： | FLATTENED |
| 27:37 (PRESERVED) | 0 | We will come to them with troops they cannot face | 回去见他们吧。我们必带着他们无法抵抗的军队降临他们； | PRESERVED |
| 27:37 (PRESERVED) | 1 | and We will drive them out of it, humbled and low. | 我们必带着他们无法抵抗的军队降临他们；羞辱地把他们从那里驱逐出去。” | PRESERVED |
| 27:45 (FLATTENED) | 0 | "We sent to Thamud their brother Salih: 'Worship God' | 我派遣撒利哈去教化赛莫德的族人：“崇拜真主吧。 | FLATTENED |
| 27:50 (FLATTENED) | 0 | and We schemed a scheme, while they did not perceive. | 他们谋划，我也谋划，但他们未察觉。 | FLATTENED |
| 27:51 (FLATTENED) | 0 | We destroyed them and their people, all together. | 你注意他们谋划的结局吧；我毁灭了他们和他们的族人，全部。 | FLATTENED |
| 27:53 (FLATTENED) | 0 | And We saved those who believed and were righteous. | 我拯救了信道且敬畏的人。 | FLATTENED |
| 27:57 (FLATTENED) | 0 | So We saved him and his family | 于是我拯救了他和他的家属，除了他的妻子， | FLATTENED |
| 27:57 (FLATTENED) | 1 | We decreed her among those left behind. | 于是我拯救了他和他的家属，除了他的妻子，我注定她成为落后者。 | FLATTENED |
| 27:58 (FLATTENED) | 0 | And We rained on them a rain | 我给他们降下了雨。被警告者的雨多么悲惨。 | FLATTENED |
| 27:60 (FLATTENED) | 0 | Who created the heavens and the earth and sent down water for you from the sky, with which We grew gardens full of beauty | 为你们从天空降下雨水？我借此生产美丽的果园，你们不能生产其树木。 | FLATTENED |
| 27:81 (PRESERVED) | 0 | You can only make hear those who believe in Our signs | 你只能使信我们经文的人听见；他们是归顺者。 | PRESERVED |
| 27:82 (MIXED) | 0 | We will bring out for them a creature from the earth, to speak to them | 当判决降临他们时，我将从大地为他们带出一种生物， | FLATTENED |
| 27:82 (MIXED) | 1 | that people had no certainty in Our signs. | 它告诉他们：人们对我们的启示心存疑虑。 | PRESERVED |
| 27:83 (FLATTENED) | 0 | On the Day We gather from every nation a troop of those who denied Our signs | 那日，我从每个民族集合一群否认我们启示的人； | FLATTENED |
| 27:86 (FLATTENED) | 0 | Have they not seen that We made the night for them to rest in, and the day giving sight? | 难道他们没看见我使夜晚供他们休息，白天供人视物吗？ | FLATTENED |

### Surah 28

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 28:3 (FLATTENED) | 0 | We recite to you some of the news of Moses and Pharaoh, with the truth | 我向你叙述摩西和法老的历史——真实地——为信道的人们。 | FLATTENED |
| 28:5 (FLATTENED) | 0 | And We wanted to show favor to those who were crushed in the land | 但我意欲施恩于在大地上被压迫的人，使他们成为领袖， | FLATTENED |
| 28:7 (FLATTENED) | 0 | And We inspired Moses' mother: Suckle him. | 我启示摩西的母亲：“哺乳他； | FLATTENED |
| 28:7 (FLATTENED) | 1 | We will return him to you | 不要恐惧，不要悲伤；我必把他送回你身边， | FLATTENED |
| 28:7 (FLATTENED) | 2 | and We will make him one of the messengers. | 我必把他送回你身边，使他成为使者之一。” | FLATTENED |
| 28:10 (FLATTENED) | 0 | She nearly showed it, had We not fastened her heart | 她几乎泄露他的身份，若不是我使她的心安定，以便她保持信道。 | FLATTENED |
| 28:12 (FLATTENED) | 0 | And We had barred all wet nurses from him before, so she said, "Shall I point you to a household that will nurse him for you, and they will be faithful to him?" | 我起初禁止他吃奶。于是她说： | FLATTENED |
| 28:13 (FLATTENED) | 0 | So We returned him to his mother, that her eye might be comforted and she might not grieve | 这样我把他送回他母亲身边，以便她得到安慰， | FLATTENED |
| 28:14 (FLATTENED) | 0 | We gave him judgment and knowledge. | 当他达到壮年，成熟稳重时，我赐给他智慧和知识。 | FLATTENED |
| 28:14 (FLATTENED) | 1 | That is how We repay those who do good. | 我赐给他智慧和知识。我这样报偿行善者。 | FLATTENED |
| 28:35 (FLATTENED) | 0 | He said, "We will strengthen your arm with your brother | 他说：“我将以你兄弟增强你的力量， | FLATTENED |
| 28:35 (FLATTENED) | 1 | and We will give you both authority | “我将以你兄弟增强你的力量，赐你们权威，他们不能伤害你们。 | FLATTENED |
| 28:35 (FLATTENED) | 2 | By Our signs, you two and whoever follows you will be the victors." | 他们不能伤害你们。凭借我的迹象，你和追随你的人将是胜利者。 | FLATTENED |
| 28:36 (FLATTENED) | 0 | And when Moses came to them with Our clear signs, they said, "This is nothing but invented sorcery | 但当摩西带着我明白昭然的迹象来到他们面前时，他们说：“这不过是捏造的魔法， | FLATTENED |
| 28:39 (PRESERVED) | 0 | and they thought they would not be returned to Us. | 他和他的军队在大地上无理地骄傲自大。他们以为不会被召回我们这里。 | PRESERVED |
| 28:40 (FLATTENED) | 0 | So We seized him and his soldiers, and cast them into the sea. | 于是我惩治了他和他的军队，把他们投入海中。 | FLATTENED |
| 28:41 (FLATTENED) | 0 | And We made them leaders calling to the Fire. | 我使他们成为召唤人入火狱的领袖。复生日， | FLATTENED |
| 28:42 (FLATTENED) | 0 | And We followed them in this world with a curse | 我在今世以诅咒追随他们。复生日， | FLATTENED |
| 28:43 (FLATTENED) | 0 | And We gave Moses the Book, after We destroyed the former generations | 我在毁灭以前的世代之后，赐给摩西经典， | FLATTENED |
| 28:44 (FLATTENED) | 0 | And you were not on the western side when We decreed the matter to Moses, and you were not among the witnesses. | 当我向摩西颁布命令时，你不在西边，你也不是见证者之一。 | FLATTENED |
| 28:45 (FLATTENED) | 0 | But We raised up generations, and long life stretched over them. | 但我兴起了许多世代，岁月使他们衰老。 | FLATTENED |
| 28:45 (FLATTENED) | 1 | And you did not dwell among the people of Midian, reciting Our signs to them | 岁月使他们衰老。你也不在米甸人中向他们宣读我的启示。但我不断派遣使者。 | FLATTENED |
| 28:45 (FLATTENED) | 2 | but We were the senders. | 你也不在米甸人中向他们宣读我的启示。但我不断派遣使者。 | FLATTENED |
| 28:46 (FLATTENED) | 0 | And you were not by the side of the Mount when We called | 当我召唤时，你也不在山旁。而是来自你主的慈悯， | FLATTENED |
| 28:48 (FLATTENED) | 0 | But when the truth came to them from Us, they said, "If only he were given the like of what Moses was given." Did they not disbelieve what Moses was given before? | 但当真理从我这里降临他们时，他们说：“要是他被赐予像摩西被赐予的一样就好了。 | FLATTENED |
| 28:51 (FLATTENED) | 0 | And We have delivered the word to them in turn, that they might remember. | 我确已把言辞传达给他们，以便他们记取。 | FLATTENED |
| 28:52 (FLATTENED) | 0 | Those to whom We gave the Book before it | 在它之前我赐予经典的人信它。 | FLATTENED |
| 28:54 (FLATTENED) | 0 | and they meet the bad deed with the good one, and they give from what We provided them. | 他们以善抵恶；从我赐给他们的给养中施舍。 | FLATTENED |
| 28:57 (PRESERVED) | 1 | a safe sanctuary, to which the fruits of everything are brought, a provision from Us? | 作为来自我们的给养吗？但他们中的大多数不知道。 | PRESERVED |
| 28:58 (MIXED) | 0 | And how many a town We destroyed, whose living made it proud. | 我毁灭了多少城市，因为它们对其生计不知感恩！ | FLATTENED |
| 28:58 (MIXED) | 1 | And We were the inheritors. | 除了少数。我们成了继承者。 | PRESERVED |
| 28:59 (FLATTENED) | 0 | And your Lord would not destroy the towns until He sent in their mother-town a messenger, reciting Our signs to them. | 向他们宣读我的启示，就毁灭城市。我从不毁灭城市， | FLATTENED |
| 28:59 (FLATTENED) | 1 | And We would not destroy the towns unless their people were wrongdoers. | 就毁灭城市。我从不毁灭城市，除非其人民是不义者。 | FLATTENED |
| 28:61 (FLATTENED) | 0 | Is one whom We promised a good promise | 我给他美好许诺、必将实现的人， | FLATTENED |
| 28:61 (FLATTENED) | 1 | like one whom We let enjoy the goods of the worldly life, then on the Day of Resurrection he will be among those brought forth? | 我给他美好许诺、必将实现的人，能与我在今世赐予享受、 | FLATTENED |
| 28:75 (FLATTENED) | 0 | And We will pull from every nation a witness | 我将从每个民族选出一个见证人，说： | FLATTENED |
| 28:75 (FLATTENED) | 1 | and We will say, "Bring your proof." Then they will know that the truth is God's | 我将从每个民族选出一个见证人，说：“拿出你们的证据。 | FLATTENED |
| 28:76 (FLATTENED) | 0 | And We gave him of the treasures | 但他压迫他们。我赐给他宝藏，其钥匙重得一群壮汉都抬不动。 | FLATTENED |
| 28:81 (FLATTENED) | 0 | So We swallowed him and his house into the earth. | 于是我使大地吞没了他和他的宅邸。他没有帮手能从真主那里拯救他， | FLATTENED |
| 28:83 (FLATTENED) | 0 | We make it for those who want no high-handedness in the land, and no corruption. | 后世的那个家园——我把它赐给在大地上不寻求优越、也不寻求腐败的人。 | FLATTENED |

### Surah 29

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 29:3 (PRESERVED) | 0 | And We tested those before them. | 我们确已考验过他们之前的人。真主必将知道诚实的人， | PRESERVED |
| 29:4 (PRESERVED) | 0 | Or do those who do evil deeds think they will outrun Us? | 难道那些作恶的人以为他们能愚弄我们吗？他们的判断真恶劣！ | PRESERVED |
| 29:7 (PRESERVED) | 0 | We will surely wipe away their evil deeds | 信道而且行善的人——我们必为他们赦免罪过，并以他们所做的最好的行为报酬他们。 | PRESERVED |
| 29:7 (PRESERVED) | 1 | and We will surely repay them for the best of what they used to do. | 信道而且行善的人——我们必为他们赦免罪过，并以他们所做的最好的行为报酬他们。 | PRESERVED |
| 29:8 (PRESERVED) | 0 | And We enjoined upon man kindness to his parents. | 我们曾嘱咐人善待父母。但如果他们怂恿你以你所不知道的东西举伴我， | PRESERVED |
| 29:9 (PRESERVED) | 0 | We will surely bring them in among the upright. | 信道而且行善的人——我们必使他们进入敬畏者的行列。 | PRESERVED |
| 29:14 (PRESERVED) | 0 | And We sent Noah to his people, and he stayed among them a thousand years less fifty. | 我们确已派遣挪亚到他的宗族那里，他在他们中间住了九百五十年。 | PRESERVED |
| 29:15 (PRESERVED) | 0 | So We saved him and the people of the ship | 但我们拯救了他和方舟上的人，并使它成为众世界的一个迹象。 | PRESERVED |
| 29:15 (PRESERVED) | 1 | and We made it a sign for the worlds. | 但我们拯救了他和方舟上的人，并使它成为众世界的一个迹象。 | PRESERVED |
| 29:27 (PRESERVED) | 0 | And We gave him Isaac and Jacob | 我们赐给他以撒和雅各，把先知之职和经典授予他的后裔， | PRESERVED |
| 29:27 (PRESERVED) | 1 | and We placed among his offspring prophethood and the Book. | 我们赐给他以撒和雅各，把先知之职和经典授予他的后裔， | PRESERVED |
| 29:27 (PRESERVED) | 2 | And We gave him his reward in this world | 把先知之职和经典授予他的后裔，并在今世给他报酬；在后世， | PRESERVED |
| 29:33 (PRESERVED) | 0 | And when Our messengers came to Lot, he was distressed by them and felt helpless before them. | 当我们的众使者来到罗得那里时，他们受到虐待， | PRESERVED |
| 29:34 (PRESERVED) | 0 | We will send down upon the people of this town a foul punishment from the sky, for the defiance they used to show. | “我们必因他们的作恶，给这座城市的人降下天谴。 | PRESERVED |
| 29:35 (PRESERVED) | 0 | And We left from it a clear sign for people who use their minds. | 我们为能理解的人留下了它的明显痕迹。 | PRESERVED |
| 29:39 (FLATTENED) | 0 | and they were not outrunning Us. | 但他们在大地上傲慢。他们不能领先。 | FLATTENED |
| 29:40 (PRESERVED) | 0 | So each We seized for his sin. | 我们因每个人的罪过而惩治了他们。我们对其中一些人降下沙暴； | PRESERVED |
| 29:40 (PRESERVED) | 1 | Among them were those upon whom We sent a pelt of stones, and among them were those seized by the Blast, and among them were those We swallowed into the earth, and among them were those We drowned. | 我们因每个人的罪过而惩治了他们。我们对其中一些人降下沙暴；有些人被巨响击中； | PRESERVED |
| 29:43 (PRESERVED) | 0 | And these are the likenesses We strike for people. | 这些比喻——我们为人们提出，但只有有学问的人才能理解。 | PRESERVED |
| 29:47 (PRESERVED) | 0 | And thus We sent down the Book to you. | 同样，我们把经典降示给你。 | PRESERVED |
| 29:47 (PRESERVED) | 1 | And those to whom We gave the Book believe in it. | 同样，我们把经典降示给你。我们赐予经典的人信仰它， | PRESERVED |
| 29:47 (PRESERVED) | 2 | And none denies Our signs but the disbelievers. | 他们中的一些人也信仰它。只有不信道的人否认我们的启示。 | PRESERVED |
| 29:49 (PRESERVED) | 0 | And none denies Our signs but the wrongdoers. | 它是明证，存在于被赐予知识者的心中。只有不义的人否认我们的迹象。 | PRESERVED |
| 29:51 (PRESERVED) | 0 | Is it not enough for them that We sent down to you the Book, recited to them? | 难道这对他们还不够吗：我们把经典降示给你，有人诵读给他们听？ | PRESERVED |
| 29:57 (PRESERVED) | 0 | Then to Us you will be returned. | 人人都将尝到死亡。然后你们只被归于我们。 | PRESERVED |
| 29:58 (PRESERVED) | 0 | We will surely settle them in the Garden, in high rooms beneath which rivers flow, abiding there forever. | 信道而且行善的人——我们必使他们在乐园中安居，住进有诸河流淌其下的高楼， | PRESERVED |
| 29:66 (PRESERVED) | 0 | To disbelieve in what We gave them, and to enjoy themselves. | 以便他们辜负我们赐予他们的，并让他们享乐。 | PRESERVED |
| 29:67 (PRESERVED) | 0 | Have they not seen that We made a safe sanctuary | 难道他们没有看见，我们设立了一个安全的禁地， | PRESERVED |
| 29:69 (PRESERVED) | 0 | And those who strive in Us | 至于为我们而奋斗的人——我们必引导他们走我们的道路。真主确与行善的人同在。 | PRESERVED |
| 29:69 (PRESERVED) | 1 | We will surely guide them to Our paths. | 至于为我们而奋斗的人——我们必引导他们走我们的道路。真主确与行善的人同在。 | PRESERVED |

### Surah 30

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 30:16 (PRESERVED) | 0 | And as for those who disbelieved and called Our signs a lie, and the meeting of the Hereafter | 但至于不信、否认我们的迹象和后世相会的人——他们将被带入刑罚。 | PRESERVED |
| 30:28 (MIXED) | 0 | He has struck for you a likeness from yourselves: are any of those your right hands own your partners in what We provided you | 他为你们从你们自身中举出一个比喻：你们会让你们的奴仆成为真主赐予你们的财富的合伙人吗？你们敬畏他们如同你们彼此敬畏吗？ | FLATTENED |
| 30:28 (MIXED) | 1 | Thus We spell out the signs for people who use their minds. | 你们敬畏他们如同你们彼此敬畏吗？我们这样为理解的人阐明启示。 | PRESERVED |
| 30:34 (PRESERVED) | 0 | To disbelieve in what We gave them. | 以便辜负我们赐予他们的。你们享乐吧——你们必将知道。 | PRESERVED |
| 30:35 (PRESERVED) | 0 | Or did We send down to them an authority, and it speaks of what they join with Him? | 难道我们给他们降下了什么明证，支持他们的偶像吗？ | PRESERVED |
| 30:36 (PRESERVED) | 0 | And when We let people taste mercy, they rejoice in it. | 当我们让人们尝到慈悯时，他们为之欢喜。 | PRESERVED |
| 30:47 (PRESERVED) | 0 | And We sent before you messengers to their peoples, and they came to them with the clear proofs. | 在你之前，我们确已派遣众使者到他们的宗族那里。 | PRESERVED |
| 30:47 (PRESERVED) | 1 | So We took retribution from those who were guilty. | 我们确已派遣众使者到他们的宗族那里。他们带着明证来见他们。然后我们惩罚了犯罪的人。 | PRESERVED |
| 30:47 (PRESERVED) | 2 | And it was binding upon Us to help the believers. | 然后我们惩罚了犯罪的人。援助信士是我们的责任。 | PRESERVED |
| 30:51 (PRESERVED) | 0 | And if We sent a wind, and they saw it yellowed, they would go on disbelieving after it. | 但如果我们派遣一阵风，他们看见它使万物变黄， | PRESERVED |
| 30:53 (PRESERVED) | 0 | You make hear only those who believe in Our signs | 你只能使信仰我们的迹象、因而顺服的人听见。 | PRESERVED |
| 30:58 (PRESERVED) | 0 | And We have struck for people, in this Quran, every likeness. | 我们确已在这部古兰经中为人们列举了各种比喻。但即使你给他们带来一个奇迹， | PRESERVED |

### Surah 31

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 31:7 (PRESERVED) | 0 | And when Our signs are recited to him, he turns away, arrogant | 当我们的节文被诵读给他听时，他傲慢地转身离去， | PRESERVED |
| 31:10 (PRESERVED) | 0 | And We sent down water from the sky | 以免大地带着你们动摇；并在其中散布了各种动物。我们从天上降下雨水， | PRESERVED |
| 31:10 (PRESERVED) | 1 | and We grew in it every noble kind. | 我们从天上降下雨水，使其中生长出每一种珍贵的成对植物。 | PRESERVED |
| 31:12 (PRESERVED) | 0 | And We gave Luqman wisdom: Give thanks to God. | 我们确已赐予鲁格曼智慧：“你要感谢真主。 | PRESERVED |
| 31:14 (PRESERVED) | 0 | And We enjoined upon man his parents | 我们曾嘱咐人孝敬父母。他的母亲怀他受尽艰辛， | PRESERVED |
| 31:23 (PRESERVED) | 0 | To Us is their return | 谁不信——不要让他的不信使你悲伤。他们只归于我们。然后我们将把他们所做的告诉他们。 | PRESERVED |
| 31:23 (PRESERVED) | 1 | and We will tell them of what they did. | 他们只归于我们。然后我们将把他们所做的告诉他们。真主知道心中的一切。 | PRESERVED |
| 31:24 (PRESERVED) | 0 | We will let them enjoy a little | 我们让他们稍稍享乐，然后迫使他们受严厉的刑罚。 | PRESERVED |
| 31:24 (PRESERVED) | 1 | then We will drive them to a harsh punishment. | 我们让他们稍稍享乐，然后迫使他们受严厉的刑罚。 | PRESERVED |
| 31:32 (PRESERVED) | 0 | And none denies Our signs but every treacherous ingrate. | 但当他使他们平安到达陆地时，他们中有些人动摇。只有背信的否认者否认我们的启示。 | PRESERVED |

### Surah 32

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 32:13 (PRESERVED) | 0 | And had We willed | 如果我们意欲，我们必给每个灵魂它的引导， | PRESERVED |
| 32:13 (PRESERVED) | 1 | We would have given every soul its guidance | 如果我们意欲，我们必给每个灵魂它的引导， | PRESERVED |
| 32:14 (PRESERVED) | 0 | We have forgotten you. | 因为你们忘记了你们今日的相会；我们已忘记你们；所以你们尝永恒的刑罚吧， | PRESERVED |
| 32:15 (PRESERVED) | 0 | Only those believe in Our signs who, when they are reminded of them, fall down prostrating | 信仰我们启示的人，是那些当被提醒时俯伏叩拜、 | PRESERVED |
| 32:16 (PRESERVED) | 0 | and they give from what We provided them. | 出于敬畏和希望祈求他们的主；并从我们供给他们的中施舍。 | PRESERVED |
| 32:21 (PRESERVED) | 0 | And We will surely let them taste of the nearer punishment, short of the greater punishment | 我们必让他们在更大的刑罚之前尝较轻的刑罚，以便他们悔改。 | PRESERVED |
| 32:22 (PRESERVED) | 0 | We will surely take retribution from the guilty. | 当被提醒他主的启示时，他转身离去？我们必向犯罪者复仇。 | PRESERVED |
| 32:23 (PRESERVED) | 0 | And We gave Moses the Book | 我们确已把经典赐给摩西；所以不要怀疑与他的相会； | PRESERVED |
| 32:23 (PRESERVED) | 1 | And We made it a guidance for the Children of Israel. | 我们确已把经典赐给摩西；所以不要怀疑与他的相会；我们使它成为以色列后裔的向导。 | PRESERVED |
| 32:24 (PRESERVED) | 0 | And We made from them leaders, guiding by Our command, when they bore with patience | 我们从他们中任命了领袖，奉我们的命令引导人， | PRESERVED |
| 32:24 (PRESERVED) | 1 | and they were certain of Our signs. | 奉我们的命令引导人，只要他们忍耐并确信我们的启示。 | PRESERVED |
| 32:26 (PRESERVED) | 0 | how many generations We destroyed before them, whose dwellings they walk through? | 难道这对他们不是教训吗：我们在他们之前毁灭了多少世代，他们在那些人的住处行走？ | PRESERVED |
| 32:27 (PRESERVED) | 0 | Have they not seen that We drive the water to the barren land, and bring out with it crops | 难道他们没有看见，我们把水引到干旱的土地， | PRESERVED |

### Surah 33

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 33:7 (PRESERVED) | 0 | And when We took from the prophets their covenant | 当时我们从众先知，从你， | PRESERVED |
| 33:7 (PRESERVED) | 1 | And We took from them a weighty covenant. | 亚伯拉罕、摩西和马利亚之子耶稣接受了盟约。我们从他们接受了庄严的盟约。 | PRESERVED |
| 33:9 (PRESERVED) | 0 | and We sent upon them a wind, and soldiers you did not see. | 你们记念真主赐给你们的恩典吧，当时军队来攻打你们，我们对他们派遣了风和你们看不见的军队。 | PRESERVED |
| 33:31 (PRESERVED) | 0 | We will give her her reward twice over | 但你们中谁顺服真主和他的使者，而且行善，我们将给她双倍的报酬； | PRESERVED |
| 33:31 (PRESERVED) | 1 | and We have prepared for her a noble provision. | 而且行善，我们将给她双倍的报酬；我们已为她准备了丰厚的给养。 | PRESERVED |
| 33:37 (PRESERVED) | 0 | We married her to you | 然后，当载德与她断绝关系时，我们把她嫁给你， | PRESERVED |
| 33:45 (PRESERVED) | 0 | We sent you as a witness, and a bearer of glad tidings, and a warner. | 先知啊！我们确已派遣你作为见证者、 | PRESERVED |
| 33:50 (PRESERVED) | 0 | We made lawful for you your wives to whom you have given their dowries, and what your right hand owns of what God gave you as spoils, and the daughters of your paternal uncle, and the daughters of your paternal aunts, and the daughters of your maternal uncle, and the daughters of your maternal aunts who emigrated with you | 先知啊！我们确已准许你： | PRESERVED |
| 33:50 (PRESERVED) | 1 | We know what We decreed upon them concerning their wives and what their right hands own | 而非为信士们。我们知道我们为他们规定的关于他们的妻子和他们右手所管辖的人的律例。这是为了不使你为难。 | PRESERVED |
| 33:60 (PRESERVED) | 0 | We will surely rouse you against them. | 心中有病的人和城中散布谣言的人不停止，我们必使你对付他们；然后他们在那里与你为邻只住很短时间。 | PRESERVED |
| 33:72 (PRESERVED) | 0 | We offered the trust to the heavens and the earth and the mountains | 我们确已把信托展示给诸天、大地和群山； | PRESERVED |

### Surah 34

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 34:5 (PRESERVED) | 0 | And those who strove against Our signs, trying to outrun | 至于那些反对我们的启示、企图破坏它的人——他们将受痛苦瘟疫的刑罚。 | PRESERVED |
| 34:9 (PRESERVED) | 0 | If We willed | 诸天和大地的情形吗？如果我们意欲，我们能使大地在他们脚下塌陷， | PRESERVED |
| 34:9 (PRESERVED) | 1 | We would swallow them into the earth, or drop upon them pieces of the sky. | 如果我们意欲，我们能使大地在他们脚下塌陷，或使天的一部分落在他们身上。 | PRESERVED |
| 34:10 (PRESERVED) | 0 | And We gave David, from Us, a bounty: | 我们确已把来自我们的恩惠赐给大卫：“群山啊， | PRESERVED |
| 34:10 (PRESERVED) | 1 | and the birds." And We softened iron for him. | 飞鸟啊，与他一起赞美。”我们为他软化了铁。 | PRESERVED |
| 34:12 (PRESERVED) | 0 | And We made flow for him a spring of molten copper. | 我们使风为他服务——它早晨走一月的路程，晚上走一月的路程。我们使沥青泉为他流淌。 | PRESERVED |
| 34:12 (PRESERVED) | 1 | And whoever of them swerved from Our command | 有些精灵在他手下工作。但他们中谁违背我们的命令，我们就让他尝火狱的刑罚。 | PRESERVED |
| 34:12 (PRESERVED) | 2 | We would let him taste of the punishment of the Blaze. | 有些精灵在他手下工作。但他们中谁违背我们的命令，我们就让他尝火狱的刑罚。 | PRESERVED |
| 34:14 (PRESERVED) | 0 | And when We decreed death upon him, nothing showed them his death except a creature of the earth eating his staff. | 然后，当我们为他判决死亡时， | PRESERVED |
| 34:16 (PRESERVED) | 0 | So We sent upon them the flood of the dam, and exchanged their two gardens for two gardens of bitter fruit, and tamarisk, and a little lote. | 但他们转身离去，所以我们对他们放出水坝的洪水； | PRESERVED |
| 34:17 (PRESERVED) | 0 | That We repaid them for what they disbelieved. | 我们这样因他们的忘恩而惩罚他们。除了忘恩的人， | PRESERVED |
| 34:17 (PRESERVED) | 1 | And do We repay any but the ingrate? | 我们这样因他们的忘恩而惩罚他们。除了忘恩的人，我们还惩罚谁呢？ | PRESERVED |
| 34:18 (PRESERVED) | 0 | And We set between them and the towns We blessed, towns in sight | 在他们和我们祝福的城镇之间，我们安置了显眼的城镇， | PRESERVED |
| 34:18 (PRESERVED) | 1 | and We measured the journey in them: | 我们安置了显眼的城镇，我们使它们之间的旅行容易。“你们昼夜在它们之间平安旅行。 | PRESERVED |
| 34:19 (PRESERVED) | 1 | So We made them tales, and tore them to utter shreds. | ”他们亏待了自己；所以我们使他们成为历史，把他们驱散到各方。 | PRESERVED |
| 34:21 (PRESERVED) | 0 | except that We might know who believes in the Hereafter from who is in doubt about it. | 他对他们没有任何权力；只是我们要区分谁信仰后世，谁怀疑它。 | PRESERVED |
| 34:28 (PRESERVED) | 0 | And We sent you only to all people | 我们只派遣你普告全人类，作为报喜者和警告者， | PRESERVED |
| 34:33 (PRESERVED) | 0 | And We will set the shackles on the necks of the disbelievers. | ”当他们看见刑罚时，他们将隐藏懊悔。我们将在不信道的人的脖子上套枷锁。 | PRESERVED |
| 34:34 (PRESERVED) | 0 | And We sent no warner into a town but its spoiled ones said, "We disbelieve in what you were sent with." | 我们没有派遣警告者到任何城镇，其中的富人不说： | PRESERVED |
| 34:37 (PRESERVED) | 0 | And your wealth and your children are not what brings you near to Us in nearness | 你们的财富和子女都不能使你们亲近我们，但信道而且行善的人能。这些人将因他们所做的得双倍报酬； | PRESERVED |
| 34:38 (PRESERVED) | 0 | And those who strive against Our signs, trying to outrun | 但那些反对我们的启示、企图破坏它的人——他们将被带到刑罚中。 | PRESERVED |
| 34:42 (PRESERVED) | 0 | And We will say to those who did wrong, "Taste the punishment of the Fire, which you used to call a lie." | 你们彼此不能获利，也不能受害。”我们将对不义的人说： | PRESERVED |
| 34:43 (PRESERVED) | 0 | And when Our clear signs are recited to them, they said, "This is nothing but a man who wants to turn you from what your fathers used to worship." And they said, "This is nothing but an invented lie." And the disbelievers said of the truth when it came to them, "This is nothing but plain sorcery." | 当我们的明证被诵读给他们听时，他们说： | PRESERVED |
| 34:44 (PRESERVED) | 0 | And We did not give them books they study | 但我们没有给他们可研读的书，我们也没有在你之前派遣警告者给他们。 | PRESERVED |
| 34:44 (PRESERVED) | 1 | and We did not send to them, before you, any warner. | 但我们没有给他们可研读的书，我们也没有在你之前派遣警告者给他们。 | PRESERVED |
| 34:45 (PRESERVED) | 0 | and they did not reach a tenth of what We gave them. | 但他们还没有达到我们赐给他们的十分之一。他们否认了我的众使者，所以我的谴责是怎样的？ | PRESERVED |

### Surah 35

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 35:9 (PRESERVED) | 0 | and We drove it to a dead land | 风搅动云，我们把云赶到已死的地方，借以复活已死的大地。 | PRESERVED |
| 35:9 (PRESERVED) | 1 | and We gave life with it to the earth after its death. | 风搅动云，我们把云赶到已死的地方，借以复活已死的大地。 | PRESERVED |
| 35:24 (PRESERVED) | 0 | We sent you with the truth | 我们确已派遣你带着真理，作为报喜讯者和警告者。 | PRESERVED |
| 35:27 (PRESERVED) | 0 | and We brought out with it fruits, differing in their colors? | 难道你没有看见，真主从天上降下雨水吗？我们借以产生各种颜色的水果。 | PRESERVED |
| 35:29 (PRESERVED) | 0 | Those who recite God's Book, and keep up the prayer, and give from what We provided them | 诵读真主经典、谨守拜功、暗中和公开施舍我们供给他们的人， | PRESERVED |
| 35:31 (PRESERVED) | 0 | And what We revealed to you of the Book is the truth | 我们启示给你的经典就是真理，证实它之前的。 | PRESERVED |
| 35:32 (PRESERVED) | 0 | Then We made inherit the Book those We chose of Our servants. | 然后我们把经典传给我们拣选的仆人。他们中有亏待自己的， | PRESERVED |
| 35:36 (PRESERVED) | 0 | Thus We repay every ingrate. | 刑罚也不会为他们减轻。我们这样报酬每个忘恩的人。 | PRESERVED |
| 35:40 (PRESERVED) | 0 | Or did We give them a book, and they are upon a clear proof from it? | 还是他们在诸天中有份？”难道我们给过他们一本书，他们遵循其中的明证吗？ | PRESERVED |

### Surah 36

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 36:8 (PRESERVED) | 0 | We set shackles on their necks | 我们在他们脖子上套上枷锁，直达下巴， | PRESERVED |
| 36:9 (PRESERVED) | 0 | And We set before them a barrier, and behind them a barrier | 我们在他们前面设置屏障，在他们后面设置屏障， | PRESERVED |
| 36:9 (PRESERVED) | 1 | and We covered them, so they do not see. | 在他们后面设置屏障，我们遮蔽了他们，所以他们看不见。 | PRESERVED |
| 36:12 (PRESERVED) | 0 | We give life to the dead | 是我们复活死者；我们记录他们所做的和他们的遗迹。 | PRESERVED |
| 36:12 (PRESERVED) | 1 | and We write what they sent ahead, and their traces. | 是我们复活死者；我们记录他们所做的和他们的遗迹。 | PRESERVED |
| 36:12 (PRESERVED) | 2 | And everything We have counted in a clear register. | 我们记录他们所做的和他们的遗迹。我们把一切都统计在明册中。 | PRESERVED |
| 36:14 (PRESERVED) | 0 | When We sent to them two, and they called them liars | 我们派遣两位使者给他们，但他们否认了两人， | PRESERVED |
| 36:14 (PRESERVED) | 1 | so We strengthened with a third. | 但他们否认了两人，所以我们以第三位加强他们。他们说： | PRESERVED |
| 36:28 (PRESERVED) | 0 | And We did not send down upon his people after him any soldiers from the sky | 在他之后，我们没有从天上降军队给他的宗族； | PRESERVED |
| 36:28 (PRESERVED) | 1 | and We were not senders. | 我们没有从天上降军队给他的宗族；我们也从不降下。 | PRESERVED |
| 36:31 (PRESERVED) | 0 | Have they not seen how many generations We destroyed before them | 难道他们没有想过，我们在他们之前毁灭了多少世代；他们不会回到他们那里？ | PRESERVED |
| 36:32 (PRESERVED) | 0 | And all of them will surely be brought before Us. | 每一个人，都必被带到我们面前。 | PRESERVED |
| 36:33 (PRESERVED) | 0 | We gave it life | 已死的大地是他们的一个迹象：我们使它复活，从中产生他们吃的谷物。 | PRESERVED |
| 36:33 (PRESERVED) | 1 | and We brought out of it grain, and from it they eat. | 已死的大地是他们的一个迹象：我们使它复活，从中产生他们吃的谷物。 | PRESERVED |
| 36:34 (PRESERVED) | 0 | And We made in it gardens of palms and vines | 我们在其中安置椰枣和葡萄的花园，使泉水从中涌出。 | PRESERVED |
| 36:34 (PRESERVED) | 1 | and We burst in it springs. | 我们在其中安置椰枣和葡萄的花园，使泉水从中涌出。 | PRESERVED |
| 36:37 (PRESERVED) | 0 | We strip the day from it, and there they are, in darkness. | 夜晚是他们的另一个迹象：我们从中剥去白昼——他们陷入黑暗。 | PRESERVED |
| 36:39 (PRESERVED) | 0 | We measured it in stations, until it returned like the old palm stalk. | 月亮：我们为它规定了月相， | PRESERVED |
| 36:41 (PRESERVED) | 0 | And a sign for them is that We carried their offspring in the laden ship. | 他们的另一个迹象是：我们载他们的后代在满载的方舟中。 | PRESERVED |
| 36:42 (PRESERVED) | 0 | And We created for them, like it, what they ride. | 我们为他们创造了类似的，他们乘坐。 | PRESERVED |
| 36:43 (PRESERVED) | 0 | And if We willed | 如果我们意欲，我们能淹死他们——无人听见他们的呼救， | PRESERVED |
| 36:43 (PRESERVED) | 1 | We would drown them | 如果我们意欲，我们能淹死他们——无人听见他们的呼救， | PRESERVED |
| 36:44 (PRESERVED) | 0 | Except as a mercy from Us, and enjoyment for a while. | 除非我们的慈悯，和暂时的享受。 | PRESERVED |
| 36:53 (PRESERVED) | 0 | and there they are, all brought before Us. | 看哪，他们全体被带到我们面前。 | PRESERVED |
| 36:65 (PRESERVED) | 0 | Today We will seal upon their mouths | 在这一日，我们将封住他们的口， | PRESERVED |
| 36:65 (PRESERVED) | 1 | and their hands will speak to Us, and their feet will witness to what they used to earn. | 我们将封住他们的口，他们的手将对我们说话，他们的脚将见证他们所做的一切。 | PRESERVED |
| 36:66 (PRESERVED) | 0 | And had We willed | 如果我们意欲，我们能弄瞎他们的眼睛， | PRESERVED |
| 36:66 (PRESERVED) | 1 | We would have blotted out their eyes | 如果我们意欲，我们能弄瞎他们的眼睛， | PRESERVED |
| 36:67 (PRESERVED) | 0 | And had We willed | 如果我们意欲，我们能使他们在原地瘫痪； | PRESERVED |
| 36:67 (PRESERVED) | 1 | We would have transformed them in their place | 如果我们意欲，我们能使他们在原地瘫痪； | PRESERVED |
| 36:68 (PRESERVED) | 0 | And whom We give long life | 谁我们给他长寿，我们使他的发育倒退。 | PRESERVED |
| 36:68 (PRESERVED) | 1 | We turn him back in creation. | 谁我们给他长寿，我们使他的发育倒退。 | PRESERVED |
| 36:69 (PRESERVED) | 0 | And We did not teach him poetry | 我们没有教他诗歌，诗歌也不适合他。 | PRESERVED |
| 36:71 (PRESERVED) | 0 | Have they not seen that We created for them, of what Our hands made, cattle | 难道他们没有看见，我们为他们创造了我们亲手创造的、 | PRESERVED |
| 36:72 (PRESERVED) | 0 | And We made them tame for them | 我们使牲畜顺服他们。有些他们骑， | PRESERVED |
| 36:76 (PRESERVED) | 0 | We know what they hide and what they show. | 所以不要让他们的话使你悲伤。我们知道他们隐藏的，和他们公开的。 | PRESERVED |
| 36:77 (PRESERVED) | 0 | Has man not seen that We created him from a drop | 人难道没有想过，我们用一滴精液创造了他吗？ | PRESERVED |
| 36:78 (PRESERVED) | 0 | And he struck for Us a likeness, and forgot his creation. | 他为我们举出比喻，忘记了他自己的创造。 | PRESERVED |

### Surah 37

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 37:6 (PRESERVED) | 0 | We adorned the lowest heaven with the adornment of the stars. | 我们确已用行星的美丽装饰了近天。 | PRESERVED |
| 37:11 (PRESERVED) | 0 | So ask them: are they harder to create, or those We created? | “他们更难创造，还是我们创造的其他？”我们用粘土创造了他们。 | PRESERVED |
| 37:11 (PRESERVED) | 1 | We created them from clinging clay. | “他们更难创造，还是我们创造的其他？”我们用粘土创造了他们。 | PRESERVED |
| 37:34 (PRESERVED) | 0 | This is how We deal with the criminals. | 我们这样对待犯罪的人。 | PRESERVED |
| 37:63 (PRESERVED) | 0 | We made it a trial for the wrongdoers. | 我们使它成为不义者的考验。 | PRESERVED |
| 37:72 (PRESERVED) | 0 | though We sent warners among them. | 尽管我们派遣了众使者警告他们。 | PRESERVED |
| 37:75 (PRESERVED) | 0 | Noah called out to Us | 挪亚曾呼求我们，我们是最好的应答者。 | PRESERVED |
| 37:76 (PRESERVED) | 0 | We saved him and his household from the great distress, | 我们拯救了他和他的家属，免于大难。 | PRESERVED |
| 37:78 (PRESERVED) | 0 | And We left for him among later peoples: | 我们在后来的世代中留下对他的纪念。 | PRESERVED |
| 37:80 (PRESERVED) | 0 | This is how We reward those who do good. | 我们这样报酬敬畏者。 | PRESERVED |
| 37:81 (PRESERVED) | 0 | He was one of Our believing servants. | 他是我们信道的仆人之一。 | PRESERVED |
| 37:82 (PRESERVED) | 0 | Then We drowned the others. | 然后我们淹死了其他人。 | PRESERVED |
| 37:98 (PRESERVED) | 0 | but We made them the lowest. | 他们想害他，但我们使他们成为失败者。 | PRESERVED |
| 37:101 (PRESERVED) | 0 | So We gave him good news of a gentle boy. | 所以我们向他报喜：一个温和的男孩。 | PRESERVED |
| 37:104 (PRESERVED) | 0 | We called to him, 'Abraham!' | 我们呼唤他：“亚伯拉罕啊！ | PRESERVED |
| 37:105 (PRESERVED) | 0 | This is how We reward those who do good." | 你已实现了梦兆。”我们这样报酬行善的人。 | PRESERVED |
| 37:107 (PRESERVED) | 0 | And We ransomed him with a great sacrifice. | 我们以重大的牺牲赎回了他。 | PRESERVED |
| 37:108 (PRESERVED) | 0 | And We left for him among later peoples: | 我们在后来的世代中留下对他的纪念。 | PRESERVED |
| 37:110 (PRESERVED) | 0 | This is how We reward those who do good. | 我们这样报酬行善的人。 | PRESERVED |
| 37:111 (PRESERVED) | 0 | He was one of Our believing servants. | 他是我们信道的仆人之一。 | PRESERVED |
| 37:112 (PRESERVED) | 0 | And We gave him good news of Isaac | 我们向他报喜：以撒， | PRESERVED |
| 37:113 (PRESERVED) | 0 | We blessed him and Isaac. | 我们祝福他和以撒。但他们的后裔中有些是行善的， | PRESERVED |
| 37:114 (PRESERVED) | 0 | We favored Moses and Aaron. | 我们祝福摩西和亚伦。 | PRESERVED |
| 37:115 (PRESERVED) | 0 | We saved them and their people from the great distress, | 我们拯救了他们和他们的宗族，免于大难。 | PRESERVED |
| 37:117 (PRESERVED) | 0 | We gave them the Book that makes things clear, | 我们赐给他们阐明的经典。 | PRESERVED |
| 37:121 (PRESERVED) | 0 | This is how We reward those who do good. | 我们这样报酬敬畏者。 | PRESERVED |
| 37:122 (PRESERVED) | 0 | They were among Our believing servants. | 他们是我们信道的仆人。 | PRESERVED |
| 37:129 (PRESERVED) | 0 | And We left for him among later peoples: | 我们在后来的世代中留下对他的纪念。 | PRESERVED |
| 37:131 (PRESERVED) | 0 | This is how We reward those who do good. | 我们这样报酬行善的人。 | PRESERVED |
| 37:132 (PRESERVED) | 0 | He was one of Our believing servants. | 他是我们信道的仆人之一。 | PRESERVED |
| 37:134 (PRESERVED) | 0 | when We saved him and all his household, | 我们拯救了他和他的家属，全体。 | PRESERVED |
| 37:136 (PRESERVED) | 0 | Then We destroyed the others. | 然后我们消灭了其他人。 | PRESERVED |
| 37:145 (PRESERVED) | 0 | So We cast him onto the open shore, and he was sick. | 然后我们把他抛到荒野，他病了。 | PRESERVED |
| 37:146 (PRESERVED) | 0 | And We grew over him a gourd plant. | 我们使一棵葫芦树在他上面生长。 | PRESERVED |
| 37:147 (PRESERVED) | 0 | And We sent him to a hundred thousand, or more. | 然后我们派遣他到十万人，或更多。 | PRESERVED |
| 37:148 (PRESERVED) | 0 | They believed, so We let them enjoy life for a while. | 他们信仰了，所以我们让他们享受一段时间。 | PRESERVED |
| 37:150 (PRESERVED) | 0 | Or did We create the angels female, while they were watching? | 难道我们创造天使为女性，而他们见证了吗？ | PRESERVED |
| 37:165 (PRESERVED) | 0 | We are the ones lined up in ranks. | 我们确是列班者。 | PRESERVED |
| 37:166 (PRESERVED) | 0 | We are the ones who glorify. | 我们确是赞颂者。” | PRESERVED |
| 37:171 (PRESERVED) | 0 | Our word has already gone out to Our servants, the messengers: | 我们的断言已对我们的仆人众使者发出。 | PRESERVED |
| 37:173 (PRESERVED) | 0 | and Our forces will be the victors. | 我们的军队必是胜利者。 | PRESERVED |
| 37:176 (PRESERVED) | 0 | Is it Our punishment they are hurrying? | 他们想催促我们的刑罚吗？ | PRESERVED |

### Surah 38

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 38:3 (FLATTENED) | 0 | How many a generation We destroyed before them! | 在他们之前，我毁灭了多少世代？他们呼喊时， | FLATTENED |
| 38:16 (PRESERVED) | 0 | They say, 'Our Lord, hasten our share before the Day of Account.' | 他们说：“我们的主啊， | PRESERVED |
| 38:17 (FLATTENED) | 0 | Bear what they say with patience, and remember Our servant David, a man of strength. | 你要忍耐他们所说的话，记念我的仆人大卫，他足智多谋。 | FLATTENED |
| 38:18 (FLATTENED) | 0 | We set the mountains to glorify with him, evening and morning. | 我使群山在傍晚和清晨与他一起赞颂。 | FLATTENED |
| 38:20 (FLATTENED) | 0 | We made his kingdom strong, and gave him wisdom and decisive speech. | 我巩固了他的王国，赐给他智慧和果断的言辞。 | FLATTENED |
| 38:24 (FLATTENED) | 0 | except those who believe and do good deeds, and few are they.' And David realized We had tested him, so he asked his Lord for forgiveness, and fell down bowing, and turned back. | 但这样的人太少了。”大卫明白我是在考验他，于是向他的主求饶， | FLATTENED |
| 38:25 (FLATTENED) | 0 | So We forgave him that. | 于是我饶恕了他。他将在我这里获得亲近和美好的归宿。 | FLATTENED |
| 38:25 (FLATTENED) | 1 | He has nearness to Us, and a good place of return. | 于是我饶恕了他。他将在我这里获得亲近和美好的归宿。 | FLATTENED |
| 38:26 (FLATTENED) | 0 | We made you a deputy on earth, so judge between people with the truth, and do not follow desire | “大卫啊，我使你成为大地上的统治者， | FLATTENED |
| 38:27 (FLATTENED) | 0 | We did not create the heaven and the earth and what is between them for nothing. | 我创造天地和其中的万物，并非徒然。 | FLATTENED |
| 38:28 (FLATTENED) | 0 | Shall We make those who believe and do good deeds like the corrupters on earth? | 难道我要把信道行善的人，像在地上作恶的人一样对待吗？ | FLATTENED |
| 38:28 (FLATTENED) | 1 | Shall We make the righteous like the wicked? | 像在地上作恶的人一样对待吗？难道我要把敬畏者，像无耻的人一样对待吗？ | FLATTENED |
| 38:29 (FLATTENED) | 0 | A blessed Book We sent down to you, so they may ponder its verses, and those of understanding may take heed. | 这是一部我降示给你的吉祥的经典，以便他们思考其中的节文， | FLATTENED |
| 38:30 (FLATTENED) | 0 | We granted David Solomon | 我赐给大卫所罗门，他是一个优秀的仆人。 | FLATTENED |
| 38:34 (FLATTENED) | 0 | We tested Solomon, and cast a lifeless body on his throne. | 我考验了所罗门，在他的宝座上放了一个躯体； | FLATTENED |
| 38:36 (FLATTENED) | 0 | So We set the wind to serve him, blowing gently at his command wherever he headed. | 于是我使风服从他，奉他的命令轻柔地吹向他所指的地方。 | FLATTENED |
| 38:39 (FLATTENED) | 0 | "This is Our gift | “这是我的恩赐；你可以慷慨施予， | FLATTENED |
| 38:40 (FLATTENED) | 0 | He has nearness to Us, and a good place of return. | 他将在我这里获得亲近和美好的归宿。 | FLATTENED |
| 38:41 (FLATTENED) | 0 | And remember Our servant Job, when he called to his Lord, 'Satan has touched me with toil and punishment.' | 记念我的仆人约伯，当时他向他的主呼求： | FLATTENED |
| 38:43 (FLATTENED) | 0 | We granted him his household, and as many more with them | 我把他的家人还给他，还加倍赏赐他们； | FLATTENED |
| 38:43 (FLATTENED) | 1 | a mercy from Us, and a reminder for those of understanding. | 还加倍赏赐他们；这是来自我的慈悯，也是给有理智者的教训。 | FLATTENED |
| 38:44 (FLATTENED) | 0 | "Take a bundle in your hand and strike with it, and do not break your oath." We found him patient | 不要违背你的誓言。”我发现他是忍耐的。多么优秀的仆人！ | FLATTENED |
| 38:45 (FLATTENED) | 0 | And remember Our servants Abraham, Isaac, and Jacob | 记念我的仆人们：亚伯拉罕、 | FLATTENED |
| 38:46 (FLATTENED) | 0 | We set them apart with one pure thing: the remembrance of the Abode. | 我以一种独特的品质使他们出众：记念后世的家园。 | FLATTENED |
| 38:47 (FLATTENED) | 0 | With Us they are among the chosen, the best. | 在我看来，他们确是被拣选的、 | FLATTENED |
| 38:54 (FLATTENED) | 0 | This is Our provision | 这是我的恩赐，永不枯竭。 | FLATTENED |
| 38:61 (PRESERVED) | 0 | They will say, 'Our Lord, whoever brought this on us | 他们会说：“我们的主啊， | PRESERVED |

### Surah 39

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 39:2 (FLATTENED) | 0 | We sent the Book down to you with the truth | 我确已把这部经典带着真理降示给你，你当虔诚地崇拜真主， | FLATTENED |
| 39:3 (PRESERVED) | 0 | Those who take protectors besides Him say, 'We only worship them to bring us nearer to God.' God will judge between them over what they differ about. | 至于那些舍他而认保护者的人，说：“我们崇拜他们， | PRESERVED |
| 39:27 (FLATTENED) | 0 | We have struck every kind of parable for people in this Quran, that they may take heed — | 我确已在这部古兰经中为人类列举了各种比喻，以便他们觉悟。 | FLATTENED |
| 39:41 (FLATTENED) | 0 | We sent the Book down to you for people with the truth. | 我确已把这部经典带着真理降示给你，是为了人类。 | FLATTENED |
| 39:49 (PRESERVED) | 0 | When harm touches a man, he calls on Us. | 当灾难降临人时，他向我们祈求。但当我们赐给他来自我们的恩惠时， | PRESERVED |
| 39:49 (PRESERVED) | 1 | Then, when We grant him a blessing from Us, he says, 'I was given it because of knowledge.' No | 他向我们祈求。但当我们赐给他来自我们的恩惠时，他说： | PRESERVED |

### Surah 40

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 40:7 (PRESERVED) | 0 | Those who carry the Throne, and those around it, glorify their Lord with praise, believe in Him, and ask forgiveness for the believers: 'Our Lord, You embrace all things in mercy and knowledge | 信仰他，为信道者求饶：“我们的主啊， | PRESERVED |
| 40:11 (PRESERVED) | 0 | They will say, 'Our Lord, You made us die twice and gave us life twice. | 他们会说：“我们的主啊， | PRESERVED |
| 40:23 (FLATTENED) | 0 | We sent Moses with Our signs and a clear warrant — | 我确已派遣摩西带着我的迹象和明确的权威。 | FLATTENED |
| 40:25 (FLATTENED) | 0 | When he brought them the truth from Us, they said, 'Kill the sons of those who believe with him, and spare their women.' The plotting of the disbelievers only goes astray. | 当他带着来自我的真理来临他们时，他们说：“杀掉与他一同信道者的儿子们， | FLATTENED |
| 40:47 (PRESERVED) | 0 | When they argue in the Fire, the weak will say to the arrogant, 'We were your followers | 弱者将对傲慢者说：“我们曾是你们的追随者；你们能替我们分担一部分火吗？ | PRESERVED |
| 40:48 (PRESERVED) | 0 | The arrogant will say, 'We are all in it. | 傲慢者会说：“我们都在其中；真主已在仆人们之间判决了。 | PRESERVED |
| 40:51 (FLATTENED) | 0 | We will help Our messengers and the believers in the worldly life, and on the Day the witnesses stand. | 我确要在今世和见证者站起之日，援助我的使者们和信道者。 | FLATTENED |
| 40:53 (FLATTENED) | 0 | We gave Moses the guidance, and made the Children of Israel inherit the Book — | 我确已赐给摩西引导，使以色列的后裔继承经典。 | FLATTENED |
| 40:70 (FLATTENED) | 0 | Those who denied the Book, and what We sent Our messengers with | 那些否认经典和我派遣使者们所带来的——他们必将知道。 | FLATTENED |
| 40:77 (FLATTENED) | 0 | Whether We show you some of what We promise them, or take you before that | 所以你要忍耐。真主的许诺是真的。无论我让你看到我许诺他们的有些， | FLATTENED |
| 40:77 (FLATTENED) | 1 | to Us they will be returned. | 或使你归于我，他们都将被召归于我。 | FLATTENED |
| 40:78 (FLATTENED) | 0 | We sent messengers before you | 我确已在你之前派遣使者们。他们中有些我已告诉你， | FLATTENED |
| 40:78 (FLATTENED) | 1 | some We told you about, and some We did not tell you about. | 我确已在你之前派遣使者们。他们中有些我已告诉你，有些我没有告诉你。 | FLATTENED |
| 40:84 (FLATTENED) | 0 | When they saw Our might, they said, 'We believe in God alone, and disbelieve in what we used to set up as partners.' | 当他们看到我的惩罚时，他们说： | FLATTENED |
| 40:85 (FLATTENED) | 0 | Their faith did them no good when they saw Our might | 但当他们看到我的惩罚时，他们的信仰无益于他们。这是真主对待他的仆人们的一贯方式。 | FLATTENED |

### Surah 41

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 41:5 (PRESERVED) | 0 | They said, 'Our hearts are wrapped against what you call us to. | 他们说：“我们的心被遮蔽， | PRESERVED |
| 41:5 (PRESERVED) | 1 | Our ears are heavy, and between us and you is a veil. | 听不到你召我们去的，我们的耳朵聋了，我们和你之间有隔障。 | PRESERVED |
| 41:11 (PRESERVED) | 0 | He said to it and to the earth, 'Come, willingly or unwillingly.' They said, 'We come willingly.' | “我们自愿地来了。” | PRESERVED |
| 41:12 (FLATTENED) | 0 | We adorned the lowest heaven with lamps, and as a guard. | 我装饰了最低的宇宙，点缀明灯，并加以保护。 | FLATTENED |
| 41:14 (PRESERVED) | 0 | We disbelieve in what you were sent with.' | 所以，我们否认你们被派遣所带来的。” | PRESERVED |
| 41:15 (FLATTENED) | 0 | They denied Our signs. | 创造他们的真主比他们更有力吗？他们一直否认我的启示。 | FLATTENED |
| 41:16 (FLATTENED) | 0 | We sent on them a screaming wind on miserable days, to make them taste the punishment of shame in the worldly life. | 于是我在几个悲惨的日子里，对他们放出呼啸的风， | FLATTENED |
| 41:17 (FLATTENED) | 0 | We guided them | 至于赛莫德人，我引导了他们， | FLATTENED |
| 41:18 (FLATTENED) | 0 | We saved those who believed and were mindful. | 我拯救了信道而敬畏的人。 | FLATTENED |
| 41:25 (FLATTENED) | 0 | We set companions over them, who made fair to them what was before them and what was behind them. | 我曾为他们安排同伴，美化了他们面前和身后的事。 | FLATTENED |
| 41:27 (FLATTENED) | 0 | We will make the disbelievers taste a severe punishment, and repay them for the worst of what they used to do. | 我必使不信道者尝到严厉的刑罚，必按他们所做的最恶劣的报偿他们。 | FLATTENED |
| 41:28 (FLATTENED) | 0 | a recompense for denying Our signs. | 这就是真主的敌人的报偿——火狱——他们在其中有永久的家园，以报偿他们无视我的启示。 | FLATTENED |
| 41:29 (PRESERVED) | 0 | The disbelievers will say, 'Our Lord, show us the two who led us astray | 不信道者会说：“我们的主啊， | PRESERVED |
| 41:30 (PRESERVED) | 0 | Those who said, 'Our Lord is God,' then stood firm | 那些说“我们的主是真主”、然后端正的人， | PRESERVED |
| 41:39 (FLATTENED) | 0 | then, when We send down water on it, it stirs and swells. | 他的迹象中还有：你看到大地静止。但当我把雨水降在它上时， | FLATTENED |
| 41:40 (FLATTENED) | 0 | Those who twist Our signs are not hidden from Us. | 轻视我的启示的人瞒不过我。被投入火中的人更好？ | FLATTENED |
| 41:44 (FLATTENED) | 0 | Had We made it a foreign Quran, they would have said, 'Why are its verses not spelled out? | 如果我把它降为一部外语的古兰经，他们必说： | FLATTENED |
| 41:45 (FLATTENED) | 0 | We gave Moses the Book, and they differed over it. | 我确已赐给摩西经典，但人们对它起了争论。 | FLATTENED |
| 41:47 (PRESERVED) | 0 | On the Day He calls to them, 'Where are My partners?' they will say, 'We declare to You: none of us is a witness.' | “我们向你承认，我们中没有一个是见证者。” | PRESERVED |
| 41:50 (FLATTENED) | 0 | If We let him taste mercy from Us after harm touched him, he will say, 'This is mine. | 当我在灾难降临他之后，让他尝到来自我的慈悯时， | FLATTENED |
| 41:50 (FLATTENED) | 1 | And if I am returned to my Lord, I will have the best with Him.' We will tell the disbelievers what they did, and make them taste a harsh punishment. | 即使我被召归于我的主，我在他那里也必得最好的。”我必告诉不信道者他们所做的， | FLATTENED |
| 41:51 (FLATTENED) | 0 | When We bless a man, he turns away and keeps his distance. | 当我赐福于人时，他退避疏远； | FLATTENED |
| 41:53 (FLATTENED) | 0 | We will show them Our signs on the horizons and in themselves, until it is clear to them that it is the truth. | 我将向他们显示我在天边和他们自身中的迹象，直到他们明白它是真理。 | FLATTENED |

### Surah 42

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 42:7 (FLATTENED) | 0 | So We revealed to you an Arabic Quran, to warn the mother of towns and those around it, and to warn of the Day of Gathering | 我这样向你启示了一部阿拉伯文的古兰经，以便你警告众城之母和它周围的人， | FLATTENED |
| 42:13 (FLATTENED) | 0 | He laid down for you of the faith what He enjoined on Noah, and what We revealed to you, and what We enjoined on Abraham, Moses, and Jesus: 'Uphold the faith, and do not split over it.' What you call them to weighs heavy on the idolaters. | 和我启示给你的，和曾命谕亚伯拉罕、摩西、 | FLATTENED |
| 42:20 (FLATTENED) | 0 | We increase his harvest for him. | 谁欲后世的收获，我为他增加他的收获；谁欲今世的收获， | FLATTENED |
| 42:20 (FLATTENED) | 1 | We give him some of it | 谁欲今世的收获，我给他一些，他在后世没有份额。 | FLATTENED |
| 42:23 (FLATTENED) | 0 | We increase its goodness for him. | ”谁做一件善事，我为他增加它的善。真主是至赦的、 | FLATTENED |
| 42:35 (FLATTENED) | 0 | And those who dispute Our signs will know they have no escape. | 争论我的迹象的人知道，他们无处可逃。 | FLATTENED |
| 42:38 (FLATTENED) | 0 | those who answered their Lord, keep up the prayer, manage their affairs by consultation among them, and give from what We provided them — | 他们的事务由协商决定、施舍我供给他们的。 | FLATTENED |
| 42:48 (FLATTENED) | 0 | We did not send you as a keeper over them. | 但如果他们背离——我没有派遣你做他们的监护者。你的职责只是传达。 | FLATTENED |
| 42:48 (FLATTENED) | 1 | When We let man taste mercy from Us, he rejoices in it. | 你的职责只是传达。当我让人尝到来自我的慈悯时，他为此欢喜； | FLATTENED |
| 42:52 (FLATTENED) | 0 | So We revealed to you a spirit from Our command. | 我这样凭我的命令向你启示了精神。你以前不知道经典是什么， | FLATTENED |
| 42:52 (FLATTENED) | 1 | but We made it a light, guiding with it whom We will of Our servants. | 信仰是什么，但我使它成为光明，借此引导我所意欲的仆人。 | FLATTENED |

### Surah 43

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 43:3 (FLATTENED) | 0 | We made it an Arabic Quran, so that you may think. | 我确已把它降为一部阿拉伯文的古兰经，以便你们理解。 | FLATTENED |
| 43:4 (FLATTENED) | 0 | And with Us, in the Source Book, it stands high and wise. | 它在我这里，在根本经典中， | FLATTENED |
| 43:5 (PRESERVED) | 0 | Should We turn the Reminder away from you, just because you are a people who go too far? | 难道我们要因你们是过分的人而收回对你们的提醒吗？ | PRESERVED |
| 43:6 (FLATTENED) | 0 | How many prophets did We send among the ancients? | 我曾向古人派遣了多少先知？ | FLATTENED |
| 43:8 (FLATTENED) | 0 | So We destroyed peoples stronger than these in might | 我毁灭了比他们更强大的人，古人的例子已成过去。 | FLATTENED |
| 43:11 (FLATTENED) | 0 | and We bring a dead land back to life with it. | 是他从天上按定量降下雨水；我借此复活了死地。你们将这样被复活出来。 | FLATTENED |
| 43:21 (FLATTENED) | 0 | Or did We give them a book before this one, that they are holding fast to? | 难道我曾在这之前赐给他们一部经典，他们遵循它吗？ | FLATTENED |
| 43:23 (FLATTENED) | 0 | And so it was: We never sent a warner to a town before you without its pampered ones saying, "We found our fathers on a path, and we follow in their footsteps." | 同样，在你之前， | FLATTENED |
| 43:25 (FLATTENED) | 0 | So We took revenge on them | 于是我惩罚了他们。你看， | FLATTENED |
| 43:32 (FLATTENED) | 0 | We portioned out their livelihood among them in the worldly life, and raised some above others in rank, so that some may take others into service. | 难道是他们分配你的主的慈悯吗？是我在今世分配了他们的生计， | FLATTENED |
| 43:33 (FLATTENED) | 0 | We would have made for those who disbelieve in the Beneficent roofs of silver for their houses, and stairways to climb. | 若非人类将成为一个民族，我必给不信至仁者的人的房屋配上银的屋顶， | FLATTENED |
| 43:36 (FLATTENED) | 0 | We appoint a devil for him | 谁回避记念至仁者，我为他安排一个恶魔，做他的同伴。 | FLATTENED |
| 43:38 (FLATTENED) | 0 | Until, when he comes to Us, he says, "If only the distance between me and you were the distance between the two easts | 当他来临我时，他会说： | FLATTENED |
| 43:41 (FLATTENED) | 0 | Whether We take you away or not | 即使我使你去世，我必惩罚他们。 | FLATTENED |
| 43:41 (FLATTENED) | 1 | We will take revenge on them. | 即使我使你去世，我必惩罚他们。 | FLATTENED |
| 43:42 (FLATTENED) | 0 | Or We show you what We promised them | 或让你看到我许诺他们的；我对他们确是全能的。 | FLATTENED |
| 43:42 (FLATTENED) | 1 | We have full power over them. | 或让你看到我许诺他们的；我对他们确是全能的。 | FLATTENED |
| 43:45 (FLATTENED) | 0 | Ask those of Our messengers We sent before you: did We set up gods besides the Beneficent to be worshiped? | 你问问我在你之前派遣的使者们：“难道我曾指定至仁者之外的神受崇拜吗？ | FLATTENED |
| 43:46 (FLATTENED) | 0 | We sent Moses with Our signs to Pharaoh and his chiefs. | 我确已派遣摩西带着我的启示去见法老和他的贵族们。他说： | FLATTENED |
| 43:47 (FLATTENED) | 0 | But when he brought them Our signs, they laughed at them. | 但当他向他们显示我的迹象时，他们开始嘲笑它们。 | FLATTENED |
| 43:48 (FLATTENED) | 0 | Every sign We showed them was greater than the one before it. | 我向他们显示的每个迹象都比另一个更奇妙。我以灾难惩罚他们， | FLATTENED |
| 43:48 (FLATTENED) | 1 | We seized them with punishment, so that they might return. | 我向他们显示的每个迹象都比另一个更奇妙。我以灾难惩罚他们，以便他们悔改。 | FLATTENED |
| 43:50 (FLATTENED) | 0 | But when We lifted the punishment from them, they broke their word. | 但当我为他们解除刑罚时，他们立刻违背诺言。 | FLATTENED |
| 43:55 (FLATTENED) | 0 | When they angered Us | 当他们激怒我时，我惩罚了他们， | FLATTENED |
| 43:55 (FLATTENED) | 1 | We took revenge on them and drowned them all. | 当他们激怒我时，我惩罚了他们， | FLATTENED |
| 43:56 (FLATTENED) | 0 | We made them a lesson of the past, and an example for those who came after. | 于是我使他们成为前例和后人的鉴戒。 | FLATTENED |
| 43:59 (FLATTENED) | 0 | He is only a servant We blessed | 他只是一个我赐福的仆人，我使他成为以色列后裔的榜样。 | FLATTENED |
| 43:59 (FLATTENED) | 1 | and We made him an example for the Children of Israel. | 他只是一个我赐福的仆人，我使他成为以色列后裔的榜样。 | FLATTENED |
| 43:60 (FLATTENED) | 0 | Had We willed | 如果我意欲，我必从你们中造出天使， | FLATTENED |
| 43:60 (FLATTENED) | 1 | We could have made angels from among you to succeed you on earth. | 如果我意欲，我必从你们中造出天使， | FLATTENED |
| 43:69 (FLATTENED) | 0 | Those who believed in Our verses, and submitted. | 那些信仰我的启示、顺服的人。 | FLATTENED |
| 43:76 (FLATTENED) | 0 | We did them no wrong | 我没有亏待他们，是他们自己不义。 | FLATTENED |
| 43:78 (FLATTENED) | 0 | We brought you the truth, but most of you hate the truth. | 我确已把真理带来给你们，但你们大多厌恶真理。 | FLATTENED |
| 43:79 (FLATTENED) | 0 | Then We too have settled on one. | 难道他们策划了计谋吗？我也在策划。 | FLATTENED |
| 43:80 (FLATTENED) | 0 | Do they think We do not hear their secrets and their private talk? | 难道他们以为我听不到他们的秘密和密谋吗？是的， | FLATTENED |
| 43:80 (FLATTENED) | 1 | Our messengers are with them, writing it down. | 难道他们以为我听不到他们的秘密和密谋吗？是的，我的使者们在他们身边记录。 | FLATTENED |

### Surah 44

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 44:3 (FLATTENED) | 0 | We sent it down on a blessed night | 我在吉庆的夜晚降示了它——我确已警告。 | FLATTENED |
| 44:3 (FLATTENED) | 1 | We have always been warners. | 我在吉庆的夜晚降示了它——我确已警告。 | FLATTENED |
| 44:5 (FLATTENED) | 0 | A command from Us | 来自我的命令。我一直在派遣使者。 | FLATTENED |
| 44:5 (FLATTENED) | 1 | We have always been senders. | 来自我的命令。我一直在派遣使者。 | FLATTENED |
| 44:15 (FLATTENED) | 0 | We will lift the punishment for a little while | 我将稍稍减轻刑罚，但你们必重犯。 | FLATTENED |
| 44:16 (FLATTENED) | 0 | On the Day We strike the great blow | 在我发动大袭击之日——我必报复。 | FLATTENED |
| 44:16 (FLATTENED) | 1 | We will take revenge. | 在我发动大袭击之日——我必报复。 | FLATTENED |
| 44:17 (FLATTENED) | 0 | We tested Pharaoh's people before them, and a noble messenger came to them. | 在他们之前，我考验了法老的族人； | FLATTENED |
| 44:28 (FLATTENED) | 0 | and We passed it all to another people as inheritance. | 就是这样；我把它们传给了另一群人。 | FLATTENED |
| 44:30 (FLATTENED) | 0 | We rescued the Children of Israel from the humiliating punishment. | 我拯救了以色列的后裔，脱离耻辱的迫害。 | FLATTENED |
| 44:32 (FLATTENED) | 0 | We chose them, knowingly, above all peoples. | 我凭知识拣选他们，超越其他所有人。 | FLATTENED |
| 44:33 (FLATTENED) | 0 | We gave them signs in which was a clear test. | 我赐给他们许多迹象，其中有明显的考验。 | FLATTENED |
| 44:37 (FLATTENED) | 0 | We destroyed them | 还是图巴的族人和他们之前的人？我消灭了他们。他们是作恶者。 | FLATTENED |
| 44:38 (FLATTENED) | 0 | We did not create the heavens and the earth and all between them in play. | 我创造天地和其中的万物，不是为了游戏。 | FLATTENED |
| 44:39 (FLATTENED) | 0 | We created them only in truth | 我创造它们只为特定的目的，但他们大多不知道。 | FLATTENED |
| 44:54 (FLATTENED) | 0 | and We will pair them with wide-eyed companions. | 就是这样，我将把美貌的伴侣许配给他们。 | FLATTENED |
| 44:58 (FLATTENED) | 0 | We made it easy in your tongue, so that they may take heed. | 我使它在你的语言中易懂，以便他们记念。 | FLATTENED |

### Surah 45

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 45:6 (FLATTENED) | 0 | These are God's verses, which We recite to you in truth. | 这些是真主的节文，我带着真理诵读给你听。在真主和他的启示之后， | FLATTENED |
| 45:9 (FLATTENED) | 0 | When he learns anything of Our verses, he takes them as a joke. | 当他知道我的启示中的一些时，就加以嘲笑。 | FLATTENED |
| 45:16 (FLATTENED) | 0 | We gave the Children of Israel the Book, judgment, and prophethood, provided them with good things, and favored them above all peoples. | 我确已赐给以色列的后裔经典、智慧和预言； | FLATTENED |
| 45:17 (FLATTENED) | 0 | We gave them clear proofs of the matter. | 我赐给他们明确的律例。他们只是在知识降临他们之后， | FLATTENED |
| 45:18 (FLATTENED) | 0 | Then We set you on a clear path of the matter | 然后我使你走上信仰的大道，你当遵循它， | FLATTENED |
| 45:21 (FLATTENED) | 0 | Do those who commit evil deeds think We will make them like those who believe and do good deeds | 难道作恶者以为，我会把他们看作与信道行善的人相等， | FLATTENED |
| 45:25 (FLATTENED) | 0 | When Our clear verses are recited to them, their only plea is to say, "Bring our forefathers, if you are truthful." | 当我的阐明的节文被诵读给他们时，他们唯一的论据是说： | FLATTENED |
| 45:29 (FLATTENED) | 0 | This is Our book | 我的这部经典对你们说真话。我确已记录你们所做的。 | FLATTENED |
| 45:29 (FLATTENED) | 1 | We were recording what you used to do. | 我的这部经典对你们说真话。我确已记录你们所做的。” | FLATTENED |
| 45:34 (FLATTENED) | 0 | It will be said, "Today We forget you, as you forgot the meeting of this Day of yours. | 将说：“今日我忘记你们， | FLATTENED |

### Surah 46

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 46:3 (FLATTENED) | 0 | We created the heavens and the earth and all between them only in truth, and for a named term. | 我创造天地和其中的万物，只凭真理， | FLATTENED |
| 46:7 (FLATTENED) | 0 | When Our clear verses are recited to them, those who disbelieve say of the truth when it comes to them, "This is clear magic." | 当我的启示被明白清楚地诵读给他们时，不信道者对降临他们的真理说： | FLATTENED |
| 46:15 (FLATTENED) | 0 | We charged man with kindness to his parents. | 我曾命人孝敬父母。他的母亲艰难地怀他， | FLATTENED |
| 46:16 (FLATTENED) | 0 | Those are the ones from whom We accept the best of what they did | 这些人，我接受他们所做的最好的， | FLATTENED |
| 46:16 (FLATTENED) | 1 | and We overlook their evil deeds | 这些人，我接受他们所做的最好的，赦免他们的过错， | FLATTENED |
| 46:25 (FLATTENED) | 0 | So We repay the evildoing people. | 只见他们的住所。这就是我报偿犯罪的人。 | FLATTENED |
| 46:26 (FLATTENED) | 0 | We had settled them firmly in what We never settled you in, and gave them hearing, sight, and hearts | 我曾赐给他们像赐给你们一样的权势；我赐给他们听觉、 | FLATTENED |
| 46:27 (FLATTENED) | 0 | We destroyed the towns around you, and turned the signs every way, so that they might return. | 我确已毁灭了你们周围的许多城镇，多方显示迹象， | FLATTENED |
| 46:29 (FLATTENED) | 0 | When We turned a band of the jinn toward you to listen to the Quran | 你记念吧，当时我派遣一群精灵到你那里， | FLATTENED |

### Surah 47

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 47:13 (FLATTENED) | 0 | How many a town, stronger in might than your town that drove you out, did We destroy? | 我毁灭了它们，没有援助者帮助它们。 | FLATTENED |
| 47:30 (FLATTENED) | 0 | Had We willed | 如果我意欲，我必把他们指给你看， | FLATTENED |
| 47:30 (FLATTENED) | 1 | We would have shown them to you, and you would know them by their mark | 如果我意欲，我必把他们指给你看， | FLATTENED |
| 47:31 (FLATTENED) | 0 | We will test you until We know those among you who strive and those who are patient | 我必考验你们，直到我知道你们中奋斗的人和坚忍的人， | FLATTENED |
| 47:31 (FLATTENED) | 1 | and We will test what is in you. | 直到我知道你们中奋斗的人和坚忍的人，我将考验你们的表现。 | FLATTENED |

### Surah 48

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 48:1 (PRESERVED) | 0 | We gave you a clear victory. | 我们已赐给你一次明显的胜利。 | PRESERVED |
| 48:8 (PRESERVED) | 0 | We sent you as a witness, a bearer of good news, and a warner. | 我们派遣你来作见证者，作报喜者， | PRESERVED |
| 48:13 (PRESERVED) | 0 | We prepared a raging fire for the disbelievers. | 不信真主和他的使者的人——我们已为不信道者准备了烈火。 | PRESERVED |
| 48:25 (PRESERVED) | 0 | We would have punished the disbelievers among them with a painful punishment. | 是为了把他所意欲的人纳入他的慈恩。如果他们分散了，我们必以痛苦的刑罚惩罚他们中不信道的人。 | PRESERVED |

### Surah 49

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 49:13 (PRESERVED) | 0 | We created you from male and female, and made you nations and tribes so you may know one another. | 人们啊！我们从一男一女创造了你们， | PRESERVED |

### Surah 50

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 50:4 (PRESERVED) | 0 | We know what the earth takes from them | 我们确知大地从他们身上消耗了什么，我们这里有一部包罗万象的经典。 | PRESERVED |
| 50:4 (PRESERVED) | 1 | with Us is a preserving book. | 我们确知大地从他们身上消耗了什么，我们这里有一部包罗万象的经典。 | PRESERVED |
| 50:6 (PRESERVED) | 0 | how We built it and adorned it, with no cracks in it? | 我们怎样建造它、装饰它，它没有一点裂缝吗？ | PRESERVED |
| 50:7 (PRESERVED) | 0 | We spread it out, cast firm mountains in it, and grew in it every splendid kind. | 还有大地，我们怎样展开它， | PRESERVED |
| 50:9 (PRESERVED) | 0 | We sent down blessed water from the sky, and grew with it gardens and the grain of harvest. | 我们从天上降下吉祥的雨水，借以生长园圃和可收割的谷物。 | PRESERVED |
| 50:11 (PRESERVED) | 0 | and We brought a dead land to life with it. | 作为仆人们的给养。我们借它使一座死城复活。复活也是这样。 | PRESERVED |
| 50:15 (PRESERVED) | 0 | Were We worn out by the first creation? | 难道我们被第一次创造搞得疲惫了吗？不， | PRESERVED |
| 50:16 (PRESERVED) | 0 | We created man | 我们确已创造了人类，我们知道他的心灵向他低语什么。 | PRESERVED |
| 50:16 (PRESERVED) | 1 | and We know what his soul whispers to him | 我们确已创造了人类，我们知道他的心灵向他低语什么。 | PRESERVED |
| 50:16 (PRESERVED) | 2 | We are nearer to him than the jugular vein. | 我们确已创造了人类，我们知道他的心灵向他低语什么。我们比他的颈静脉更接近他。 | PRESERVED |
| 50:22 (PRESERVED) | 0 | We lifted your covering from you, so your sight today is sharp." | “你曾经忽视了这个，所以我们为你揭去了你的屏障，今天你的视力敏锐了。 | PRESERVED |
| 50:30 (PRESERVED) | 0 | On the Day We say to Hell, "Are you full?" It will say, "Is there more?" | 在那一天，我们将对火狱说： | PRESERVED |
| 50:35 (PRESERVED) | 0 | and with Us is more. | 在其中他们将拥有他们所想要的一切——我们还有更多。 | PRESERVED |
| 50:36 (PRESERVED) | 0 | How many a generation before them did We destroy | 在他们之前，我们毁灭了多少代人，他们比这些人更强大！ | PRESERVED |
| 50:38 (PRESERVED) | 0 | We created the heavens and the earth and all between them in six days | 我们在六天内创造了天地和它们之间的一切，没有一点疲惫触及我们。 | PRESERVED |
| 50:38 (PRESERVED) | 1 | no weariness touched Us. | 我们在六天内创造了天地和它们之间的一切，没有一点疲惫触及我们。 | PRESERVED |
| 50:43 (PRESERVED) | 0 | We give life and deal death | 是我们掌管生死，我们是归宿。 | PRESERVED |
| 50:43 (PRESERVED) | 1 | to Us is the destination. | 是我们掌管生死，我们是归宿。 | PRESERVED |
| 50:44 (PRESERVED) | 0 | that is a gathering easy for Us. | 大地为他们一下子裂开。那对我们来说是容易的集合。 | PRESERVED |
| 50:45 (PRESERVED) | 0 | We know best what they say | 我们完全知道他们所说的，你不是他们的强迫者。 | PRESERVED |

### Surah 51

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 51:35 (PRESERVED) | 0 | We brought out whoever was in it of the believers. | 我们把城中的信道者都撤了出来。 | PRESERVED |
| 51:36 (PRESERVED) | 0 | We found in it only one house of those who submit. | 但在其中只找到一户归顺的人家。 | PRESERVED |
| 51:37 (PRESERVED) | 0 | We left in it a sign for those who fear the painful punishment. | 我们在其中留下了一个迹象，给畏惧痛苦刑罚的人。 | PRESERVED |
| 51:38 (PRESERVED) | 0 | when We sent him to Pharaoh with clear authority. | 在摩西的故事中也是如此。我们派他带着明确的权威去见法老。 | PRESERVED |
| 51:40 (PRESERVED) | 0 | We seized him and his hosts and flung them into the sea | 于是我们擒住了他和他的军队，把他们扔进大海， | PRESERVED |
| 51:41 (PRESERVED) | 0 | when We sent the barren wind upon them. | 在阿德人的故事中也是如此。我们对他们放出毁灭性的大风。 | PRESERVED |
| 51:47 (PRESERVED) | 0 | We built it with power | 我们以大能建造了宇宙，我们确在扩展它。 | PRESERVED |
| 51:47 (PRESERVED) | 1 | and We are expanding it. | 我们以大能建造了宇宙，我们确在扩展它。 | PRESERVED |
| 51:48 (PRESERVED) | 0 | We spread it out. | 大地——我们展开了它——我们铺得多么好！ | PRESERVED |
| 51:49 (PRESERVED) | 0 | Of everything We created two | 我们把万物造成成双成对的，以便你们反思默想。 | PRESERVED |

### Surah 52

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 52:20 (PRESERVED) | 0 | and We paired them with wide-eyed companions. | 靠在华贵的卧榻上；我们将使他们与美丽的伴侣结合。 | PRESERVED |
| 52:21 (PRESERVED) | 0 | We will join their offspring to them | 信道者，以及他们的后代在信仰上追随他们的——我们将使他们与后代团聚，我们不会亏待他们的善功丝毫。 | PRESERVED |
| 52:21 (PRESERVED) | 1 | and We will not shortchange their deeds at all. | 以及他们的后代在信仰上追随他们的——我们将使他们与后代团聚，我们不会亏待他们的善功丝毫。每个人都是自己所挣得的抵押品。 | PRESERVED |
| 52:22 (PRESERVED) | 0 | We will supply them with fruit and meat, whatever they crave. | 我们将供给他们水果和肉食，随他们所欲。 | PRESERVED |
| 52:48 (PRESERVED) | 0 | you are before Our eyes. | 所以你要耐心等待你的主的判决，因为你是在我们的注视之下；当你起身时， | PRESERVED |

### Surah 53

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 53:29 (PRESERVED) | 0 | So turn away from whoever turned from Our reminder and wanted nothing but the worldly life. | 所以你要避开背转我们记念、只想要今世生活的人。 | PRESERVED |

### Surah 54

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 54:9 (PRESERVED) | 0 | They denied Our servant and said: A madman! | 他们拒绝了我们的仆人，说：“疯子。 | PRESERVED |
| 54:11 (PRESERVED) | 0 | And We opened the gates of heaven with pouring water, | 于是我们打开天门，倾盆大雨。 | PRESERVED |
| 54:12 (PRESERVED) | 0 | and We burst the earth into springs, and the waters met for a matter already decreed. | 我们使大地涌出泉水，众水相会， | PRESERVED |
| 54:13 (PRESERVED) | 0 | And We carried him on a craft of planks and nails, | 我们把他载在木板和钉子做的船上。 | PRESERVED |
| 54:14 (PRESERVED) | 0 | running under Our eyes | 在我们的注视下航行；这是给被拒绝者的报偿。 | PRESERVED |
| 54:15 (PRESERVED) | 0 | We left it as a sign. | 我们把它留作迹象。有谁愿意吸取教训吗？ | PRESERVED |
| 54:17 (PRESERVED) | 0 | We made the Quran easy for remembrance. | 我们使古兰经易于学习。有谁愿意学习吗？ | PRESERVED |
| 54:19 (PRESERVED) | 0 | We sent against them a screaming wind, on a day of unending ill-luck, | 我们在一个灾难连绵的日子对他们放出呼啸的大风。 | PRESERVED |
| 54:22 (PRESERVED) | 0 | We made the Quran easy for remembrance. | 我们使古兰经易于记诵。有谁愿意记诵吗？ | PRESERVED |
| 54:27 (PRESERVED) | 0 | We are sending the she-camel as a trial for them. | 我们将派母驼去考验他们；所以你要观察他们， | PRESERVED |
| 54:31 (PRESERVED) | 0 | We sent against them a single blast, and they became like dry stalks in a fenced pen. | 我们对他们只发出一声呐喊，他们就变成了碎干草。 | PRESERVED |
| 54:32 (PRESERVED) | 0 | We made the Quran easy for remembrance. | 我们使古兰经易于理解。有谁愿意理解吗？ | PRESERVED |
| 54:34 (PRESERVED) | 0 | We sent against them a rain of stones | 我们对他们降下石雨，除了罗得的家属； | PRESERVED |
| 54:34 (PRESERVED) | 1 | We saved them at dawn, | 除了罗得的家属；我们在黎明时拯救了他们。 | PRESERVED |
| 54:35 (PRESERVED) | 0 | a blessing from Us. | 这是来自我们的恩惠。我们这样报偿感恩的人。 | PRESERVED |
| 54:35 (PRESERVED) | 1 | This is how We reward the thankful. | 这是来自我们的恩惠。我们这样报偿感恩的人。 | PRESERVED |
| 54:36 (PRESERVED) | 0 | He warned them of Our grip, but they argued over the warnings. | 他曾警告他们我们的突袭，但他们轻视警告。 | PRESERVED |
| 54:37 (PRESERVED) | 0 | They tried to take his guests from him, so We blotted out their eyes: Taste My punishment and My warnings! | 他们甚至觊觎他的客人，于是我们抹去了他们的眼睛。“尝尝我的刑罚和我的警告吧。 | PRESERVED |
| 54:40 (PRESERVED) | 0 | We made the Quran easy for remembrance. | 我们使古兰经易于背诵。有谁愿意背诵吗？ | PRESERVED |
| 54:42 (PRESERVED) | 0 | They denied every one of Our signs, so We seized them with the seizing of a mighty, all-powerful one. | 他们拒绝了我们的全部迹象，于是我们擒住了他们——万能全能者的擒拿。 | PRESERVED |
| 54:49 (PRESERVED) | 0 | We created every thing by measure. | 我们创造的一切都有精确的定量。 | PRESERVED |
| 54:50 (PRESERVED) | 0 | Our command is only one | 我们的命令只有一次，像眨眼一样。 | PRESERVED |
| 54:51 (PRESERVED) | 0 | We destroyed the likes of you. | 我们已毁灭了你们的同类。有谁愿意深思吗？ | PRESERVED |

### Surah 55

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 55:31 (PRESERVED) | 0 | We will attend to you soon, O you two weighty ones. | 我们将料理你们，两个重要的群体啊。 | PRESERVED |

### Surah 56

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 56:35 (PRESERVED) | 0 | We made them anew, a fresh making, | 我们以特殊的创造创造了她们。 | PRESERVED |
| 56:57 (PRESERVED) | 0 | We made you | 我们创造了你们——但愿你们相信！ | PRESERVED |
| 56:59 (PRESERVED) | 0 | Is it you who make it, or are We the makers? | 是你们创造它，还是我们是创造者？ | PRESERVED |
| 56:60 (PRESERVED) | 0 | We decreed death among you | 我们已在你们之间注定了死亡，我们不会被超越。 | PRESERVED |
| 56:60 (PRESERVED) | 1 | and We are not to be outrun — | 我们已在你们之间注定了死亡，我们不会被超越。 | PRESERVED |
| 56:61 (PRESERVED) | 0 | so that We may replace your likes, and raise you up in what you do not know. | 用你们的同类代替你们，把你们变成你们不知道的样子。 | PRESERVED |
| 56:64 (PRESERVED) | 0 | Is it you who grow it, or are We the growers? | 是你们使它生长，还是我们是生长者？ | PRESERVED |
| 56:65 (PRESERVED) | 0 | If We willed | 如果我们意欲，我们能把它变成碎块； | PRESERVED |
| 56:65 (PRESERVED) | 1 | We would make it broken straw, and you would be left to lament: | 如果我们意欲，我们能把它变成碎块； | PRESERVED |
| 56:66 (PRESERVED) | 0 | We are penalized! | “我们受罚了。 | PRESERVED |
| 56:69 (PRESERVED) | 0 | Is it you who sent it down from the clouds, or are We the senders? | 是你们从云中降下它，还是我们是降下者？ | PRESERVED |
| 56:70 (PRESERVED) | 0 | If We willed | 如果我们意欲，我们能使它咸涩。 | PRESERVED |
| 56:70 (PRESERVED) | 1 | We would make it salty | 如果我们意欲，我们能使它咸涩。 | PRESERVED |
| 56:72 (PRESERVED) | 0 | Is it you who made its tree, or are We the makers? | 是你们生产它的树，还是我们是生产者？ | PRESERVED |
| 56:73 (PRESERVED) | 0 | We made it a reminder, and a comfort for travelers. | 我们使它成为提醒，成为使用者的慰藉。 | PRESERVED |
| 56:85 (PRESERVED) | 0 | and We are nearer to him than you, but you do not see — | 我们比你们更接近它，但你们看不见。 | PRESERVED |

### Surah 57

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 57:17 (PRESERVED) | 0 | We made the signs clear for you, so that you may think. | 真主使大地在死后复活。我们这样为你们解释启示，以便你们理解。 | PRESERVED |
| 57:19 (PRESERVED) | 0 | Those who disbelieved and denied Our signs | 他们将有他们的报酬和他们的光。至于不信而且否认我们的启示的人——这些人是烈火的居民。 | PRESERVED |
| 57:22 (PRESERVED) | 0 | No calamity strikes the earth, nor yourselves, but it is in a Book before We bring it about. | 大地上或你们自身中发生的灾难，无不在我们使它发生之前就在一部天经中。那对真主是容易的。 | PRESERVED |
| 57:25 (PRESERVED) | 0 | We sent Our messengers with clear proofs, and sent down with them the Book and the balance, so that people stand by fairness. | 我们派遣我们的使者们带着明确的证据，并和他们一起降下经典和天平， | PRESERVED |
| 57:25 (PRESERVED) | 1 | And We sent down iron | 好使人类维护正义。我们降下铁，其中有猛烈的力量， | PRESERVED |
| 57:26 (PRESERVED) | 0 | We sent Noah and Abraham, and placed in their offspring prophethood and the Book. | 我们派遣了挪亚和亚伯拉罕，在他们的后裔中确立了先知职分和经典。 | PRESERVED |
| 57:27 (PRESERVED) | 0 | Then We followed in their footsteps with Our messengers | 然后我们使我们的使者们相继而来，又使马利亚之子耶稣接踵而至， | PRESERVED |
| 57:27 (PRESERVED) | 1 | and We followed with Jesus son of Mary, and gave him the Gospel, and put in the hearts of those who followed him compassion and mercy. | 然后我们使我们的使者们相继而来，又使马利亚之子耶稣接踵而至，我们赐给他引支勒， | PRESERVED |
| 57:27 (PRESERVED) | 2 | We did not lay it on them, except seeking God's good pleasure | 并在追随他的人心中注入怜悯和慈爱。至于他们发明的修道主义——我们没有为他们规定它——只是为了寻求真主的喜悦。但他们没有如应尽地遵守它。 | PRESERVED |
| 57:27 (PRESERVED) | 3 | So We gave those of them who believed their reward, and many of them are corrupt. | 但他们没有如应尽地遵守它。所以我们把报酬给了他们中信道的人，但他们中许多人是罪恶的。 | PRESERVED |

### Surah 58

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 58:5 (PRESERVED) | 0 | We sent down clear signs. | 就像他们以前的人被制服一样。我们已降下明确的信息。不信道者将有屈辱的刑罚。 | PRESERVED |

### Surah 59

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 59:21 (FLATTENED) | 0 | If We had sent this Quran down on a mountain, you would have seen it humbled, split apart, from fear of God. | 假如我把这部古兰经降在一座山上，你必看到它因畏惧真主而颤抖、 | FLATTENED |
| 59:21 (FLATTENED) | 1 | These are the likenesses We strike for people, so that they may think. | 崩裂。这些比喻我为众人提出，以便他们反思。 | FLATTENED |

### Surah 61

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 61:14 (FLATTENED) | 1 | We strengthened those who believed against their enemy, and they came out on top. | ”于是以色列的后裔中一群人信道了，另一群人不信道。我援助了信道者对抗他们的敌人， | FLATTENED |

### Surah 63

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 63:10 (FLATTENED) | 0 | Give from what We provided you, before death comes to one of you and he says: My Lord, if only You held me back to a near term | 在死亡降临你们中一人之前，你们当从我供给你们的施舍， | FLATTENED |

### Surah 64

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 64:8 (FLATTENED) | 0 | So believe in God and His messenger, and the light We sent down. | 所以你们当信仰真主和他的使者，以及我所降示的光。真主彻知你们所做的一切。 | FLATTENED |
| 64:10 (FLATTENED) | 0 | Those who disbelieved and denied Our signs | 但那些不信道并否认我的启示的人——这些人是火狱的居民，永居其中； | FLATTENED |
| 64:12 (FLATTENED) | 0 | Our messenger need only deliver plainly. | 所以你们当服从真主，服从使者。但如果你们背离——我的使者只负责传达明确的信息。 | FLATTENED |

### Surah 65

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 65:8 (FLATTENED) | 0 | We called it to a harsh reckoning, and punished it with a dreadful punishment. | 有多少城镇违抗了其主和他的使者们的命令！于是我对它严格清算，并以可怕的刑罚惩罚了它。 | FLATTENED |

### Surah 66

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 66:12 (FLATTENED) | 0 | We breathed into it of Our spirit. | 还有仪姆兰的女儿马利亚，她保守了自己的贞洁，于是我把我的精神吹入她； | FLATTENED |

### Surah 67

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 67:5 (FLATTENED) | 0 | We dressed the lowest heaven with lamps, and made them stones pelted at the devils. | 我确已用灯装饰了近天，并使它们成为驱逐恶魔的武器； | FLATTENED |
| 67:5 (FLATTENED) | 1 | And We readied for them the punishment of the Blaze. | 我确已用灯装饰了近天，并使它们成为驱逐恶魔的武器；我已为他们准备了烈火的刑罚。 | FLATTENED |

### Surah 68

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 68:15 (FLATTENED) | 0 | When Our signs are recited to him, he says, "Tales of the old ones." | 当我的节文被诵读给他时，他说： | FLATTENED |
| 68:16 (FLATTENED) | 0 | We will brand him on the snout. | 我将在他的鼻子上烙印。 | FLATTENED |
| 68:17 (FLATTENED) | 0 | We tested them as We tested the owners of the garden | 我考验了他们，正如我考验了园主们， | FLATTENED |
| 68:35 (FLATTENED) | 0 | Should We make the Muslims like the criminals? | 难道我把穆斯林当作恶人一样对待吗？ | FLATTENED |
| 68:39 (FLATTENED) | 0 | Or do you hold oaths from Us, binding until the Day of Resurrection | 或者你们从我这里得到誓约，一直约束到复活日， | FLATTENED |
| 68:44 (FLATTENED) | 0 | We will draw them on, step by step, from where they do not know. | 所以把否认这篇训诫的人留给我吧；我将从他们不知之处逐步对付他们。 | FLATTENED |

### Surah 69

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 69:11 (FLATTENED) | 0 | We carried you on the running ship, | 当洪水泛滥时，我把你们载在航行的船上。 | FLATTENED |
| 69:44 (FLATTENED) | 0 | And if he had made up sayings against Us, | 假如他捏造一些言论归于我。 | FLATTENED |
| 69:45 (FLATTENED) | 0 | We would have grabbed him by the right hand, | 我必抓住他的右臂。 | FLATTENED |
| 69:49 (FLATTENED) | 0 | And We know that some of you call it a lie. | 我知道你们中有人将拒绝它。 | FLATTENED |

### Surah 70

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 70:7 (FLATTENED) | 0 | And We see it near. | 但我认为它临近。 | FLATTENED |
| 70:39 (FLATTENED) | 0 | We created them from what they know. | 绝不！我从他们所知道的创造了他们。 | FLATTENED |
| 70:40 (FLATTENED) | 0 | I swear by the Lord of the sunrises and the sunsets: We have the power | 我以东西方的主发誓，我确是全能的。 | FLATTENED |
| 70:41 (FLATTENED) | 0 | and none can outrun Us. | 把比他们更好的人替换他们，我不会被超越。 | FLATTENED |

### Surah 71

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 71:1 (FLATTENED) | 0 | We sent Noah to his people: | 我确已派遣挪亚到他的宗族：“在痛苦的刑罚降临他们之前， | FLATTENED |

### Surah 72

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 72:16 (FLATTENED) | 0 | We would have given them water in plenty, | 如果他们坚持正道，我必赐给他们充足的水喝。 | FLATTENED |

### Surah 73

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 73:5 (FLATTENED) | 0 | We will cast on you a heavy word. | 我即将给你沉重的信息。 | FLATTENED |
| 73:12 (FLATTENED) | 0 | With Us are shackles and a Blazing Fire, | 在我这里有枷锁，和烈焰。 | FLATTENED |
| 73:15 (FLATTENED) | 0 | We sent you a messenger | 我确已派遣一位使者到你们那里，作为你们的见证者， | FLATTENED |
| 73:15 (FLATTENED) | 1 | as We sent a messenger to Pharaoh. | 我确已派遣一位使者到你们那里，作为你们的见证者，正如我派遣一位使者到法老那里。 | FLATTENED |
| 73:16 (FLATTENED) | 0 | Pharaoh defied the messenger, so We seized him with a ruinous grip. | 但法老违抗了使者，于是我以可怕的抓拿抓住了他。 | FLATTENED |

### Surah 74

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 74:16 (FLATTENED) | 0 | He stood stubborn against Our signs. | 绝不！他对我的启示确是固执的。 | FLATTENED |
| 74:31 (FLATTENED) | 0 | We made the keepers of the Fire only angels. | 我只委派天使做火狱的看守，并使他们的数目成为不信道者的绊脚石； | FLATTENED |
| 74:31 (FLATTENED) | 1 | We made their number only a trial for the disbelievers | 我只委派天使做火狱的看守，并使他们的数目成为不信道者的绊脚石；以便被赐予经典的人达到确信； | FLATTENED |

### Surah 75

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 75:3 (FLATTENED) | 0 | Does man think We will never gather his bones? | 难道人以为我不会重组他的骨骼吗？ | FLATTENED |
| 75:4 (FLATTENED) | 0 | We have the power to shape his fingertips. | 不然；我确能重造他的指尖。 | FLATTENED |
| 75:17 (FLATTENED) | 0 | We will gather it, and recite it. | 它的收集和诵读确在我。 | FLATTENED |
| 75:18 (FLATTENED) | 0 | So when We recite it, follow its recital. | 然后，当我诵读它时， | FLATTENED |
| 75:19 (FLATTENED) | 0 | Then We will make its meaning clear. | 然后它的解释确在我。 | FLATTENED |

### Surah 76

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 76:2 (FLATTENED) | 0 | We made man from a mingled drop, to test him | 我从混合的液体中创造了人，为考验他； | FLATTENED |
| 76:2 (FLATTENED) | 1 | and We made him hearing and seeing. | 我从混合的液体中创造了人，为考验他；我使他能听能看。 | FLATTENED |
| 76:3 (FLATTENED) | 0 | We showed him the way | 我引导他走道路，或感恩， | FLATTENED |
| 76:4 (FLATTENED) | 0 | We readied for the disbelievers chains, and yokes, and a blazing fire. | 我已为不信道者准备了枷锁、项圈和烈火。 | FLATTENED |
| 76:23 (FLATTENED) | 0 | It is We who sent the Recital down to you, in stages. | 是我把古兰经逐步降示给你。 | FLATTENED |
| 76:28 (FLATTENED) | 0 | We created them, and braced their frames | 我创造了他们，加强了他们的体格； | FLATTENED |
| 76:28 (FLATTENED) | 1 | and when We will | 加强了他们的体格；每当我意欲，我能用像他们一样的人替换他们。 | FLATTENED |
| 76:28 (FLATTENED) | 2 | We can replace them with others like them. | 加强了他们的体格；每当我意欲，我能用像他们一样的人替换他们。 | FLATTENED |

### Surah 77

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 77:16 (FLATTENED) | 0 | Did We not destroy the earlier peoples? | 难道我没有毁灭古人吗？ | FLATTENED |
| 77:17 (FLATTENED) | 0 | Then We made the later ones follow them. | 然后使后人继他们之后？ | FLATTENED |
| 77:18 (FLATTENED) | 0 | This is how We deal with the guilty. | 我就是这样对待犯罪者。 | FLATTENED |
| 77:20 (FLATTENED) | 0 | Did We not create you from a lowly fluid? | 难道我没有从卑微的液体中创造你们吗？ | FLATTENED |
| 77:21 (FLATTENED) | 0 | Then We placed it in a firm resting place. | 然后把它安置在安全的地方？ | FLATTENED |
| 77:23 (FLATTENED) | 0 | We set its measure, and fine measurers are We. | 我精确地量定。我是最好的量定者。 | FLATTENED |
| 77:25 (FLATTENED) | 0 | Did We not make the earth a gathering place? | 难道我没有把大地造成家园吗？ | FLATTENED |
| 77:38 (FLATTENED) | 0 | We have gathered you and the earlier ones. | 这是分离之日；我已把你们和古人集合在一起。 | FLATTENED |
| 77:44 (FLATTENED) | 0 | This is how We reward the doers of good. | 我就是这样报酬行善者。 | FLATTENED |

### Surah 78

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 78:6 (PRESERVED) | 0 | Did We not make the earth a bed? | 难道我们没有把大地造成摇篮吗？ | PRESERVED |
| 78:28 (PRESERVED) | 0 | And they denied Our signs, calling them lies. | 他们彻底否认我们的启示。 | PRESERVED |
| 78:29 (PRESERVED) | 0 | And everything We recorded in a book. | 但我们把一切都记录在册。 | PRESERVED |
| 78:30 (PRESERVED) | 0 | We will only add to your punishment. | 你们尝吧！我们只会给你们增加刑罚。 | PRESERVED |
| 78:40 (PRESERVED) | 0 | We have warned you of a near punishment | 我们确已警告你们临近的刑罚——那天，每个人将看到他的双手所做的， | PRESERVED |

### Surah 80

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 80:25 (PRESERVED) | 0 | We poured the water down in a pouring. | 我们倾注了大量的水。 | PRESERVED |
| 80:26 (FLATTENED) | 0 | Then We split the earth in a splitting. | 然后把大地裂开。 | FLATTENED |

### Surah 83

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 83:13 (PRESERVED) | 0 | When Our signs are recited to him, he says, "Tales of the ancients." | 当我们的启示被诵读给他时，他说： | PRESERVED |

### Surah 87

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 87:6 (PRESERVED) | 0 | We will have you recite, and you will not forget. | 我们将使你诵读，所以不要忘记。 | PRESERVED |
| 87:8 (PRESERVED) | 0 | And We will smooth the easy path for you. | 我们将使你易于走上简易的道路。 | PRESERVED |

### Surah 88

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 88:25 (PRESERVED) | 0 | To Us is their return. | 他们确要回到我们这里。 | PRESERVED |
| 88:26 (PRESERVED) | 0 | Then on Us is their reckoning. | 然后，他们的清算确由我们负责。 | PRESERVED |

### Surah 90

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 90:4 (PRESERVED) | 0 | We created man in toil. | 我们确在艰辛中创造了人类。 | PRESERVED |
| 90:8 (PRESERVED) | 0 | Did We not make for him two eyes? | 难道我们没有给他两只眼睛吗？ | PRESERVED |
| 90:19 (PRESERVED) | 0 | And those who disbelieve in Our signs | 但否认我们的启示的人——这些是悲惨的人们。 | PRESERVED |

### Surah 92

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 92:7 (PRESERVED) | 0 | We will make the easy way easy for him. | 我们将使他易于走向顺利。 | PRESERVED |
| 92:10 (PRESERVED) | 0 | We will make the hard way easy for him. | 我们将使他易于走向艰难。 | PRESERVED |
| 92:12 (PRESERVED) | 0 | Guidance is on Us. | 引导确由我们负责。 | PRESERVED |

### Surah 94

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 94:1 (PRESERVED) | 0 | Did We not open your chest for you? | 难道我们没有使你的心舒畅吗？ | PRESERVED |

### Surah 95

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 95:4 (PRESERVED) | 0 | We created man in the best of molds. | 我们确以最好的形态创造了人类。 | PRESERVED |
| 95:5 (FLATTENED) | 0 | Then We returned him to the lowest of the low. | 然后把他降到最低下者之列。 | FLATTENED |

### Surah 96

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 96:15 (PRESERVED) | 0 | We will drag him by the forelock. | 不。如果他不停止，我们必揪住他的前额。 | PRESERVED |
| 96:18 (PRESERVED) | 0 | We will call the guards. | 我们将召唤卫士。 | PRESERVED |

### Surah 97

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 97:1 (PRESERVED) | 0 | We sent it down in the Night of Decree. | 我们在盖德尔之夜降下了它。 | PRESERVED |

### Surah 108

| Verse | # | EN clause | CN clause | Verdict |
|---|---|---|---|---|
| 108:1 (PRESERVED) | 0 | We have given you the Abundance. | 我们确已赐给你丰盛。 | PRESERVED |

