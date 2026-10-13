# PARTICLE CENSUS — Corrective Particles (kalla / balaa), EN Master ↔ Chinese Staging

**Built:** 2026-10-12 · **Helper B (particle census crew)** · Data file only — no manuscript edited.
**Sources:** EN `~/workspace/original-recital/files/original-recital-FULL.txt` · CN staging `~/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md` · Pairing script: `particle-census.py` (this folder); candidates: `particle-candidates.json`.

## Method

Three deterministic nets, unioned, then EVERY candidate hand-checked in context against both full verses:
- **NET-EN** — EN verse carries a corrective surface token: "Yes —", "No —", "But no —", "Then no —", "So no —" (oath form, caught on a second sweep), "No indeed —", "No indeed.", "Yes indeed —", "Yes, by …".
- **NET-KALLA** — Arabic standalone كَلَّا, token-tested so كُلًّا ("all/each": 4:130, 6:84, 11:111, 17:20) and substring look-alikes (أَكَلَا "they ate", تَأْكُلُونَ "you eat") never qualify; kaf-vowel test (fatha vs damma) confirms. Yield: exactly the canonical 33 kalla verses.
- **NET-BALAA** — Arabic بَلَىٰ after normalization. Yield: 22 verses.

**Universe: 151 corrective occurrences across 148 verses.** Verdicts grade the EN↔CN surface relation per the census brief: FAITHFUL (corrective force and polarity carried — 不然 / 不 / 绝不 / 是的 / 当然 / idiomatic rebuttal) · DROPPED (no corrective at the corresponding point — including softening to 但 / 然而 / 唉） · POLARITY-FLIP (EN affirmative rendered negative-form, or the reverse) · OTHER (carrier substitution — 其实 / 事实上 / 确实 factual pivots, absorption — force preserved, surface changed). No candidate proved to be ordinary negation: every EN-token occurrence is a genuine corrective (balaa / bal / kalla / oath-laa in Robert's rebuttal style).

## Totals

| Verdict | Count |
|---|---|
| FAITHFUL | 88 |
| DROPPED | 45 |
| POLARITY-FLIP | 4 |
| OTHER (carrier substitution) | 14 |
| **Total occurrences** | **151** |

**Confirmed faults: 49** (45 dropped + 4 polarity flips), listed in full below. A further 14 carrier substitutions (OTHER) change the particle's surface without losing its force — flagged in the table for the manifest crew, not counted as faults.

Cross-checks: all 13 of Lane D's known kalla drops (74:52, 74:54, 75:5, 75:14, 75:20, 75:26, 78:4, 78:5, 81:15, 90:1, 102:3, 102:4, 102:5) confirmed DROPPED here; 2:214 (P-08) confirmed; 84:15 confirmed as the polarity type specimen.

EN-side note (not CN faults): at 56:75, 75:1 and 75:2 Robert's EN itself renders the oath-laa without any "No" ("I swear by…"), and the CN matches the EN — outside this census by design (the census is EN-anchored).

## Confirmed faults — POLARITY-FLIP (4)

- **34:3** — EN: "sbelievers said, "The Hour will not come to us." Say, "Yes — by my Lord, it will surely come to you — the Knower of the unsee" · CN: 「你说：不然，以我的主发誓，它必降临你们。」 — EN affirmative balaa ("Yes — by my Lord") answered with negative-form 不然. Sense survives as rebuttal of the deniers' "will not come"; surface polarity vs EN flipped.
- **64:7** — EN: "The disbelievers claim they will never be raised. Say: Yes — by my Lord, you will be raised, then told what you did. That is" · CN: 「你说：不然，以我的主发誓，你们必被复活；」 — Same construction as 34:3: "Yes — by my Lord, you will be raised" → 不然. Surface flip; sense preserved as rebuttal.
- **75:4** — EN: "Yes indeed — We have the power to shape his fingertips." · CN: 「不然；我确能重造他的指尖。」 — EN "Yes indeed — We have the power" → 不然；我确能…. Surface flip; capability still affirmed after the particle.
- **84:15** — EN: "Yes — his Lord was watching him." · CN: 「不，他的主一直在看着他。」 — Type specimen (PATCH-INDEX Addendum 2 §6). EN "Yes — his Lord was watching him" → 不，他的主一直在看着他. The corrective's affirmative force is negated at the surface.

## Confirmed faults — DROPPED (45)

- **2:170** — EN "No —" → CN 「有人对他们说：追随真主所降示的，他们说：我们追随我们发现祖先追随的。」 (no corrective)
- **2:214** — EN "No —" → CN 「真主的援助确是近的。」 (no corrective) — Known item (P-08). CN closes the verse 真主的援助确是近的 with no corrective at the pivot.
- **3:150** — EN "No —" → CN 「真主是你们的主，他是最好的援助者。」 (no corrective)
- **6:28** — EN "No —" → CN 「他们以前隐藏的将对他们显明。」 (no corrective)
- **12:18** — EN "No —" → CN 「他说：是你们的心怂恿你们做了这件事。」 (no corrective)
- **15:63** — EN "No —" → CN 「他们说：我们带来他们所怀疑的。」 (no corrective)
- **16:75** — EN "No —" → CN 「一切赞颂全归真主，但大多数人不知道。」 (no corrective)
- **16:101** — EN "No —" → CN 「但大多数人不知道。」 (no corrective)
- **18:48** — EN "No —" → CN 「虽然你们曾声称我们不会为你们设定约会。」 (no corrective)
- **18:58** — EN "No —" → CN 「但他们有一个约期，他们在它之外找不到逃避处。」 (no corrective)
- **20:66** — EN "No —" → CN 「他说：你们扔吧。」 (no corrective)
- **21:5** (occurrence 1 of 3) — EN "No —" → CN 「他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。」 (no corrective)
- **21:5** (occurrence 2 of 3) — EN "No —" → CN 「他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。」 (no corrective)
- **21:5** (occurrence 3 of 3) — EN "No —" → CN 「他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。」 (no corrective)
- **21:24** — EN "No —" → CN 「但他们中的大多数不知道真理，所以他们转身离去。」 (no corrective)
- **21:26** — EN "No —" → CN 「他们只是受尊贵的仆人。」 (no corrective)
- **21:42** — EN "No —" → CN 「但他们转身离去他们主的教诲。」 (no corrective)
- **21:44** — EN "No —" → CN 「我们让这些人和他们的祖先享受，直到岁月在他们身上漫长。」 (no corrective)
- **21:56** — EN "No —" → CN 「他说：你们的主是诸天与大地的主，创造它们的主，我对此作证。」 (no corrective)
- **23:63** — EN "No —" → CN 「但他们的心因这部经典而迷惑；」 (no corrective)
- **30:29** — EN "No —" → CN 「但不义的人无知地追随私欲。」 (no corrective)
- **34:33** — EN "No —" → CN 「被压迫的人将对傲慢的人说：是你们昼夜的阴谋；」 (no corrective)
- **36:19** — EN "No —" → CN 「但你们是奢侈的民众。」 (no corrective)
- **37:29** — EN "No —" → CN 「他们将说：你们自己不是信士。」 (no corrective)
- **37:30** — EN "No —" → CN 「你们自己是叛逆的民众。」 (no corrective)
- **48:12** — EN "No —" → CN 「但你们以为使者和信道者们再也不会回到他们的家眷那里去了，这在你们心中显得顺理成章；」 (no corrective)
- **54:46** — EN "No —" → CN 「复活时是他们的约期——复活时更灾难，更苦涩。」 (no corrective)
- **67:21** — EN "No —" → CN 「但他们仍固执于违抗和厌恶。」 (no corrective)
- **68:27** — EN "No —" → CN 「我们现在被剥夺了。」 (no corrective)
- **69:38** — EN "So no —" → CN 「我确以你们所见的发誓。」 (no corrective)
- **70:40** — EN "So no —" → CN 「我以东西方的主发誓，我确是全能的。」 (no corrective)
- **74:52** — EN "No —" → CN 「但他们每人都想被赐予展开的卷轴。」 (no corrective)
- **74:54** — EN "No indeed —" → CN 「然而，它是一种教诲。」 (no corrective) — Kalla answered with 然而 ("however") — contrastive conjunction, no corrective.
- **75:5** — EN "No —" → CN 「但人想否认在他前面的。」 (no corrective)
- **75:14** — EN "No —" → CN 「人将成为不利于自己的证据。」 (no corrective)
- **75:20** — EN "No —" → CN 「唉，你们喜爱短暂的人生。」 (no corrective) — Kalla answered with the lament interjection 唉 — no corrective.
- **75:26** — EN "No —" → CN 「当灵魂到达锁骨时。」 (no corrective)
- **78:4** — EN "No —" → CN 「他们一定会知道的。」 (no corrective)
- **78:5** — EN "Then no —" → CN 「他们确切地会知道的。」 (no corrective)
- **81:15** — EN "So no —" → CN 「我以银河起誓。」 (no corrective)
- **84:16** — EN "So no —" → CN 「我以晚霞起誓。」 (no corrective)
- **90:1** — EN "No —" → CN 「我以这片土地起誓。」 (no corrective) — Oath laa ("No — I swear"); CN renders the oath plainly. Same drop at 69:38, 70:40, 81:15, 84:16 ("So no —").
- **102:3** — EN "No —" → CN 「你们一定会知道。」 (no corrective)
- **102:4** — EN "Then no —" → CN 「你们确切地会知道。」 (no corrective)
- **102:5** — EN "No —" → CN 「假如你们确切地知道。」 (no corrective)

## Carrier substitutions — OTHER (14)

Corrective force preserved under a different surface: 其实 ×6 (2:12, 2:13, 2:100, 3:169, 3:180, 48:15), 事实上 ×3 (21:18, 21:40, 21:97), 确实 ×3 (58:18, 58:19, 58:22), absorption into the verb 信 (2:260), 够了 answering the prior verse (3:125).

## Full table (151 occurrences, verse order)

| Verse | Particle | EN corrective | CN rendering (clause) | Verdict |
|---|---|---|---|---|
| 2:12 | EN | But no — it is they who are the corrupters, and yet they do not  | 其实，他们才是作恶者，但他们不觉悟。 | OTHER |
| 2:13 | EN | " they say, "Should we believe as the fools believed?" But no —  | 其实，他们才是愚人，但他们不知道。 | OTHER |
| 2:81 | BALAA+EN | No — whoever earns evil and his sin surrounds him: those are the | 不然，谁作恶并被自己的罪恶包围——他们是火狱的居民，他们将永居其中。 | FAITHFUL |
| 2:88 | EN | And they said, "Our hearts are covered." No — God cursed them fo | 不然，真主因他们的忘恩而诅咒了他们。 | FAITHFUL |
| 2:100 | EN | r they made a covenant, a party of them threw it away? No — most | 其实，他们多数人不信。 | OTHER |
| 2:112 | BALAA+EN | No — whoever submits his face to God, and is a doer of good: for | 不然，谁归顺真主并行善，谁将在他的主那里得到报酬——他们没有恐惧，也不忧愁。 | FAITHFUL |
| 2:116 | EN | And they said, "God took a son." Glory be to Him. No — His is wh | 不然，天地间的一切都属于他； | FAITHFUL |
| 2:135 | EN | id, "Be Jews or Christians, you will be guided." Say, "No — the  | 你说：不然，是亚伯拉罕的宗教，认一者； | FAITHFUL |
| 2:154 | EN | not say of those who are killed in God's way, "dead." No — they  | 不然，他们是活的，但你们不感知。 | FAITHFUL |
| 2:170 | EN | said to them, "Follow what God sent down," they say, "No — we fo | 有人对他们说：追随真主所降示的，他们说：我们追随我们发现祖先追随的。 | DROPPED |
| 2:214 | EN | hose who believed with him said, "When is God's help?" No — God' | 真主的援助确是近的。 | DROPPED |
| 2:259 | EN | said, "I remained a day, or part of a day." He said, "No — you r | 他说：不。你停留了一百年。 | FAITHFUL |
| 2:260 | BALAA+EN | the dead." He said, "Have you not believed?" He said, "Yes — but | 他说：信，但为了让我的心安宁。 | OTHER |
| 3:76 | BALAA+EN | No — whoever keeps his pledge and fears God — God loves the righ | 不然，谁践约并保持敬畏——真主喜欢敬畏者。 | FAITHFUL |
| 3:125 | BALAA+EN | Yes — if you stay patient and fear God, and they rush at you all | 够了；但如果你们坚忍并谨慎，他们突然袭击你们，你们的主将以五千训练有素的天使支援你们。 | OTHER |
| 3:150 | EN | No — God is your Protector, and He is the best of helpers. | 真主是你们的主，他是最好的援助者。 | DROPPED |
| 3:169 | EN | Do not think those killed in God's cause are dead. No — they are | 其实，他们是活的，在他们的主那里，蒙受给养。 | OTHER |
| 3:180 | EN | gave them of His bounty not think it is good for them. No — it i | 其实，那对他们坏。 | OTHER |
| 4:49 | EN | ve you not seen those who claim purity for themselves? No — God  | 不然，真主净化他所意欲的人，他们不被亏待丝毫。 | FAITHFUL |
| 4:65 | EN | No — by your Lord, they will not believe until they make you jud | 不然，以你的主发誓，他们不信，直到他们请你仲裁他们的争端，然后心中对你的判决毫无怨恨，完全顺服。 | FAITHFUL |
| 4:158 | EN | No — God raised him up to Himself. And God is Almighty, Wise. | 不然，真主把他提升到自己那里。 | FAITHFUL |
| 5:18 | EN | ones. Say: Why then does He punish you for your sins? No — you a | 不然，你们是他所创造的人类中的一员。 | FAITHFUL |
| 5:64 | EN | s are chained, and they are cursed for what they said. No — His  | 不然，他的手是展开的； | FAITHFUL |
| 6:28 | EN | No — what they hid before has now appeared to them. If they were | 他们以前隐藏的将对他们显明。 | DROPPED |
| 6:30 | BALAA+EN | He will say, "Is this not the truth?" They will say, "Yes — by o | 他们将说：是的，以我们的主发誓。 | FAITHFUL |
| 6:41 | EN | No — it is Him you call on, and He lifts what you call on Him fo | 不然，你们只祈求他； | FAITHFUL |
| 7:114 | EN | He said: Yes — and you will be of those brought near. | 他说：是的，你们将是我的亲信。 | FAITHFUL |
| 7:172 | BALAA+EN | stify about themselves: Am I not your Lord? They said: Yes — we  | 他们说：是的，我们作证。 | FAITHFUL |
| 10:39 | EN | No — they denied what they could not grasp in knowledge, and its | 不，他们否认他们知识所不能及、其阐释尚未到达他们的东西。 | FAITHFUL |
| 10:53 | EN | They ask you for news: Is it true? Say: Yes, by my Lord — it is  | 你说：是的，以我的主发誓，它确是真实的，你们无法逃脱。 | FAITHFUL |
| 12:18 | EN | They came with his shirt bearing lying blood. He said: No — your | 他说：是你们的心怂恿你们做了这件事。 | DROPPED |
| 15:63 | EN | "No — we came to you with what they used to doubt." | 他们说：我们带来他们所怀疑的。 | DROPPED |
| 16:28 | BALAA+EN | es — they offered submission: "We were doing no evil." No — God  | 不，你们作了。 | FAITHFUL |
| 16:38 | BALAA+EN | heir most solemn oaths: "God will not raise the dead." No — it i | 不，确是他应尽的许诺，但大多数人不知道。 | FAITHFUL |
| 16:75 | EN | tly and openly. Are they equal? All praise is for God. No — most | 一切赞颂全归真主，但大多数人不知道。 | DROPPED |
| 16:101 | EN | at He sends down — they said, "You are only a forger." No — most | 但大多数人不知道。 | DROPPED |
| 18:48 | EN | nks: "You came to Us as We created you the first time. No — you  | 虽然你们曾声称我们不会为你们设定约会。 | DROPPED |
| 18:58 | EN | t they earned, He would hurry the punishment for them. No — they | 但他们有一个约期，他们在它之外找不到逃避处。 | DROPPED |
| 19:79 | EN+KALLA | No indeed. We will write down what he says, and stretch out his  | 绝不！我们要记录他所说的，并不断延长他的痛苦。 | FAITHFUL |
| 19:82 | EN+KALLA | No indeed. They will deny their worship, and turn against them a | 绝不！他们将否认对他们的崇拜，成为他们的对头。 | FAITHFUL |
| 20:66 | EN | He said, No — you throw. And there: their ropes and their staffs | 他说：你们扔吧。 | DROPPED |
| 21:5 | EN | No — they say, A jumble of dreams. No — he forged it. No — he is | 他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。 | DROPPED |
| 21:5 | EN | No — they say, A jumble of dreams. No — he forged it. No — he is | 他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。 | DROPPED |
| 21:5 | EN | No — they say, A jumble of dreams. No — he forged it. No — he is | 他们说：一堆杂乱的梦，又说：他捏造了它，又说：他是个诗人，让他给我们带来迹象，像派给古人的一样。 | DROPPED |
| 21:18 | EN | No — We hurl the truth at the falsehood, and it crushes it, and  | 事实上，我们以真理打击虚妄，它粉碎它，于是它消失。 | OTHER |
| 21:24 | EN | those with me, and the remembrance of those before me. No — most | 但他们中的大多数不知道真理，所以他们转身离去。 | DROPPED |
| 21:26 | EN | hey say, The Beneficent has taken a son. Glory to Him. No — they | 他们只是受尊贵的仆人。 | DROPPED |
| 21:40 | EN | No — it will come on them suddenly, and stun them. They cannot t | 事实上，它会突然降临他们，使他们惊愕。 | OTHER |
| 21:42 | EN | ho guards you by night and by day from the Beneficent? No — they | 但他们转身离去他们主的教诲。 | DROPPED |
| 21:44 | EN | No — We let them and their fathers enjoy life, until life grew l | 我们让这些人和他们的祖先享受，直到岁月在他们身上漫长。 | DROPPED |
| 21:56 | EN | He said, No — your Lord is the Lord of the heavens and the earth | 他说：你们的主是诸天与大地的主，创造它们的主，我对此作证。 | DROPPED |
| 21:63 | EN | He said, No — this biggest one of them did it. Ask them, if they | 他说：不，是它们中这个最大的做的。 | FAITHFUL |
| 21:97 | EN | the disbelievers. Woe to us. We were heedless of this. No — we w | 事实上，我们是不义者。 | OTHER |
| 23:56 | EN | We are hurrying good to them? No — they do not feel it. | 不，他们一无所知。 | FAITHFUL |
| 23:63 | EN | No — their hearts are in a flood of confusion about this, and th | 但他们的心因这部经典而迷惑； | DROPPED |
| 23:70 | EN | Or do they say madness is in him? No — he brought them the truth | 还是他们说：他着魔了？不，他给他们带来了真理，但他们中的大多数厌恶真理。 | FAITHFUL |
| 23:71 | EN | heavens and the earth and all in them would be ruined. No — We b | 假如真理顺从他们的私欲，天地和其中的一切必已毁灭。不，我确已赐给他们教诲，但他们 | FAITHFUL |
| 23:81 | EN | No — they say what the former ones said. | 不，他们说的话像古人所说的一样。 | FAITHFUL |
| 23:90 | EN | No — We brought them the truth, and they are liars. | 不，我确已把真理赐给他们，而他们是说谎者。 | FAITHFUL |
| 23:100 | EN+KALLA | So I may do right in what I left behind. No indeed. It is a word | 绝不！那只是他随口说出的话。 | FAITHFUL |
| 26:15 | EN+KALLA | "He said, 'No — go, both of you, with Our signs. We are with you | 你们俩带着我的证据去吧。 | FAITHFUL |
| 26:42 | EN | "He said, 'Yes — and then you will be among those brought near.' | 他说：有，你们将成为受宠者之一。 | FAITHFUL |
| 26:62 | EN+KALLA | "He said, 'No — my Lord is with me; He will guide me.'" | 他说：不；我的主与我同在，他将引导我。 | FAITHFUL |
| 29:49 | EN | No — it is clear signs in the breasts of those given knowledge.  | 不然，它是明证，存在于被赐予知识者的心中。 | FAITHFUL |
| 30:29 | EN | No — those who did wrong followed their desires without knowledg | 但不义的人无知地追随私欲。 | DROPPED |
| 31:11 | EN | eation — so show me what those apart from Him created. No — the  | 不然，不义的人确在明显的迷误中。 | FAITHFUL |
| 31:21 | EN | said to them, "Follow what God sent down," they say, "No — we fo | 当有人对他们说：你们跟随真主所降示的吧，他们说：不，我们跟随我们发现我们的祖先所奉行的。 | FAITHFUL |
| 32:3 | EN | Or do they say, "He invented it"? No — it is the truth from your | 不然，它是你主的真理，以便警告在你之前没有警告者来过的民众，好让他们得引导。 | FAITHFUL |
| 32:10 | EN | are lost in the earth — will we be in a new creation?" No — they | 不然，他们否认与他们主的相会。 | FAITHFUL |
| 34:3 | BALAA+EN | sbelievers said, "The Hour will not come to us." Say, "Yes — by  | 你说：不然，以我的主发誓，它必降临你们。 | POLARITY-FLIP |
| 34:8 | EN | nvented a lie against God, or is there madness in him? No — thos | 不然，不信后世的人在刑罚中，误入远途。 | FAITHFUL |
| 34:27 | EN+KALLA | Say, "Show me those you joined with Him as partners. No — He is  | 绝不！但他是真主，全能的、睿智的。 | FAITHFUL |
| 34:32 | EN | id we turn you from the guidance after it came to you? No — you  | 不然，你们自己就是犯罪的。 | FAITHFUL |
| 34:33 | EN | who were crushed will say to those who were arrogant, "No — the  | 被压迫的人将对傲慢的人说：是你们昼夜的阴谋； | DROPPED |
| 34:41 | EN | ory be to You. You are our protector, apart from them. No — they | 不然，他们崇拜精灵，他们大多数信仰精灵。 | FAITHFUL |
| 35:40 | EN | them a book, and they are upon a clear proof from it? No — the w | 不然，不义的人彼此许诺的只是幻影。 | FAITHFUL |
| 36:19 | EN | our omen is with you. Is it because you were reminded? No — you  | 但你们是奢侈的民众。 | DROPPED |
| 36:81 | BALAA+EN | heavens and the earth able to create the like of them? Yes — and | 当然能。他是至知的创造者。 | FAITHFUL |
| 37:18 | EN | Say, 'Yes — and you will be humbled.' | 你说：是的，你们将被彻底制服。 | FAITHFUL |
| 37:29 | EN | They will say, 'No — you were no believers.' | 他们将说：你们自己不是信士。 | DROPPED |
| 37:30 | EN | "We had no power over you. No — you were a rebellious people." | 你们自己是叛逆的民众。 | DROPPED |
| 37:37 | EN | No — he brought the truth, and confirmed the messengers. | 不然，他带着真理而来，证实了众使者。 | FAITHFUL |
| 38:8 | EN | "Was the Reminder sent down to him, of all of us?" No — they are | 不然，他们怀疑我的警告。 | FAITHFUL |
| 38:8 | EN | all of us?" No — they are in doubt about My Reminder. No — they  | 不然，他们还没有尝过我的刑罚。 | FAITHFUL |
| 38:60 | EN | They will say, 'No — no welcome for you! You brought this on us. | 对你们也没有欢迎！ | FAITHFUL |
| 39:49 | EN | om Us, he says, 'I was given it because of knowledge.' No — it i | 不然，这是一种考验，但他们大多不知道。 | FAITHFUL |
| 39:59 | BALAA+EN | "No — My signs came to you, and you denied them, and were too pr | 不然！我的节文确已降临你，但你否认了它们，傲慢自大，成为不信道者。 | FAITHFUL |
| 39:66 | EN | No — worship God, and be among the thankful. | 不然，你当崇拜真主，做感恩的人。 | FAITHFUL |
| 39:71 | BALAA+EN | ing you of meeting this Day of yours?' They will say, 'Yes — but | 他们会说：是的，但刑罚的判决对不信道者已成定局。 | FAITHFUL |
| 40:50 | BALAA | (no EN dash token) They will say, 'Did your messengers not come to  | 他们会说：是的。 | FAITHFUL |
| 40:74 | EN | sides God?" They will say, 'They have strayed from us. No — we w | 不然，我们以前并未祈求任何东西。 | FAITHFUL |
| 43:22 | EN | No — they say, "We found our fathers on a path, and we are guide | 不，他们说：我们发现我们的祖先遵循一种道路，我们追随他们的足迹得到引导。 | FAITHFUL |
| 43:80 | BALAA+EN | k We do not hear their secrets and their private talk? Yes indee | 是的，我的使者们在他们身边记录。 | FAITHFUL |
| 46:24 | EN | alleys, they said, "This is a cloud bringing us rain." No — it i | 不然，这正是你们急求的：带来痛苦刑罚的风。 | FAITHFUL |
| 46:33 | BALAA+EN | re in creating them, is able to give life to the dead? Yes indee | 他对万物是全能的。 | FAITHFUL |
| 46:34 | BALAA+EN | to the Fire: "Is this not the truth?" They will say, "Yes, by ou | 他们会说：是的，以我们的主发誓。 | FAITHFUL |
| 48:12 | EN | No — you thought the messenger and the believers would never ret | 但你们以为使者和信道者们再也不会回到他们的家眷那里去了，这在你们心中显得顺理成章； | DROPPED |
| 48:15 | EN | id so before." They will say, "You are jealous of us." No — they | 其实，他们只懂一点点。 | OTHER |
| 50:15 | EN | Were We worn out by the first creation? No — they are in doubt a | 难道我们被第一次创造搞得疲惫了吗？不，他们对新的创造心存怀疑。 | FAITHFUL |
| 51:53 | EN | Did they bequeath it to one another? No — they are an oversteppi | 难道他们互相嘱托过吗？不，他们是悖逆的人。 | FAITHFUL |
| 52:33 | EN | Or do they say, "He forged it"? No — they do not believe. | 难道他们说：他编造了它？不，他们不信。 | FAITHFUL |
| 52:36 | EN | Or did they create the heavens and the earth? No — they are not  | 难道他们创造了天地？不，他们不确信。 | FAITHFUL |
| 54:25 | EN | Was the reminder cast down on him alone among us? No — he is a l | 难道在我们所有人中，启示独独给了他吗？不，他是个邪恶的撒谎者。 | FAITHFUL |
| 54:46 | EN | No — the Hour is their appointed time, and the Hour is more terr | 复活时是他们的约期——复活时更灾难，更苦涩。 | DROPPED |
| 56:67 | EN | No — we are being deprived! | 不，我们被剥夺了。 | FAITHFUL |
| 57:14 | BALAA+EN | ill call to them: Were we not with you? They will say: Yes — but | 他们将说：是的，但你们欺骗了自己的灵魂，等待，怀疑，被妄想迷惑，直到真主的命令降临； | FAITHFUL |
| 58:18 | EN | they swear to you, and think they stand on something. No — they  | 确实，他们自己是撒谎者。 | OTHER |
| 58:19 | EN | de them forget God's reminder. They are Satan's party. No — Sata | 确实，撒旦的党羽是失败者。 | OTHER |
| 58:22 | EN | , and they are pleased with Him. They are God's party. No — God' | 确实，真主的党羽是成功者。 | OTHER |
| 64:7 | BALAA+EN | The disbelievers claim they will never be raised. Say: Yes — by  | 你说：不然，以我的主发誓，你们必被复活； | POLARITY-FLIP |
| 67:9 | BALAA+EN | They say, "Yes — a warner did come to us, but we called him a li | 他们将说：有，警告者确曾到来过我们，但我们不信，还说：真主没有降示任何东西； | FAITHFUL |
| 67:21 | EN | his, who will feed you if He holds back His provision? No — they | 但他们仍固执于违抗和厌恶。 | DROPPED |
| 68:27 | EN | "No — we are shut out." | 我们现在被剥夺了。 | DROPPED |
| 69:38 | EN | So no — I swear by what you see, | 我确以你们所见的发誓。 | DROPPED |
| 70:15 | EN+KALLA | No indeed. It is a raging fire, | 绝不！它是烈焰。 | FAITHFUL |
| 70:39 | EN+KALLA | No indeed. We created them from what they know. | 绝不！我从他们所知道的创造了他们。 | FAITHFUL |
| 70:40 | EN | So no — I swear by the Lord of the sunrises and the sunsets: We  | 我以东西方的主发誓，我确是全能的。 | DROPPED |
| 74:16 | KALLA | (no EN dash token) No. He stood stubborn against Our signs. | 绝不！他对我的启示确是固执的。 | FAITHFUL |
| 74:32 | EN+KALLA | No indeed — by the moon, | 不！以月亮发誓。 | FAITHFUL |
| 74:52 | EN | No — each one of them wants to be handed scriptures unrolled. | 但他们每人都想被赐予展开的卷轴。 | DROPPED |
| 74:53 | EN+KALLA | No indeed — they do not fear the Hereafter. | 绝不！但他们不畏惧后世。 | FAITHFUL |
| 74:54 | EN+KALLA | No indeed — it is a reminder. | 然而，它是一种教诲。 | DROPPED |
| 75:4 | BALAA+EN | Yes indeed — We have the power to shape his fingertips. | 不然；我确能重造他的指尖。 | POLARITY-FLIP |
| 75:5 | EN | No — man wants to sin on ahead. | 但人想否认在他前面的。 | DROPPED |
| 75:11 | EN+KALLA | No indeed — no refuge. | 绝不！没有避难所。 | FAITHFUL |
| 75:14 | EN | No — man is a witness against himself, | 人将成为不利于自己的证据。 | DROPPED |
| 75:20 | EN+KALLA | No — you love the fleeting life, | 唉，你们喜爱短暂的人生。 | DROPPED |
| 75:26 | EN+KALLA | No — when it reaches the collarbone, | 当灵魂到达锁骨时。 | DROPPED |
| 78:4 | EN+KALLA | No — they will soon know. | 他们一定会知道的。 | DROPPED |
| 78:5 | EN+KALLA | Then no — they will soon know. | 他们确切地会知道的。 | DROPPED |
| 80:11 | EN+KALLA | No — this is a reminder. | 不该这样。这确是教训。 | FAITHFUL |
| 80:23 | EN+KALLA | No — he has not yet done what He commanded him. | 不，他没有完成他所命令他的。 | FAITHFUL |
| 81:15 | EN | So no — I swear by the retreating stars. | 我以银河起誓。 | DROPPED |
| 82:9 | EN+KALLA | No — you deny the Judgment. | 不，你们否认宗教。 | FAITHFUL |
| 83:7 | EN+KALLA | No — the record of the wicked is in Sijjin. | 不。恶人们的记录确在锡吉尼。 | FAITHFUL |
| 83:14 | EN+KALLA | No — rust has covered their hearts from what they used to earn. | 不。他们的心被他们所赚取的腐蚀了。 | FAITHFUL |
| 83:15 | EN+KALLA | No — they will be shut off from their Lord that Day. | 不。那天，他们确被遮蔽，见不到他们的主。 | FAITHFUL |
| 83:18 | EN+KALLA | No — the record of the virtuous is in Illiyyin. | 不。善人们的记录确在伊利因。 | FAITHFUL |
| 84:15 | BALAA+EN | Yes — his Lord was watching him. | 不，他的主一直在看着他。 | POLARITY-FLIP |
| 84:16 | EN | So no — I swear by the twilight glow. | 我以晚霞起誓。 | DROPPED |
| 85:21 | EN | No — it is a glorious Quran. | 不，它是荣耀的古兰经。 | FAITHFUL |
| 89:17 | EN+KALLA | No — you do not honor the orphan. | 不。你们不尊敬孤儿。 | FAITHFUL |
| 89:21 | EN+KALLA | No — when the earth is pounded to powder. | 不——当地球被夷平、碾碎时。 | FAITHFUL |
| 90:1 | EN | No — I swear by this city. | 我以这片土地起誓。 | DROPPED |
| 96:6 | EN+KALLA | No — man oversteps. | 不，人确超越界限。 | FAITHFUL |
| 96:15 | EN+KALLA | No — if he does not stop, We will drag him by the forelock. | 不。如果他不停止，我们必揪住他的前额。 | FAITHFUL |
| 96:19 | EN+KALLA | No — do not obey him. Bow down and draw near. | 不，不要服从他； | FAITHFUL |
| 102:3 | EN+KALLA | No — you will soon know. | 你们一定会知道。 | DROPPED |
| 102:4 | EN+KALLA | Then no — you will soon know. | 你们确切地会知道。 | DROPPED |
| 102:5 | EN+KALLA | No — if you knew with certain knowledge. | 假如你们确切地知道。 | DROPPED |
| 104:4 | EN+KALLA | No — he will surely be thrown into the Crusher. | 绝不。他将被扔进碾碎者。 | FAITHFUL |

## Verse notes

- **2:214** — Known item (P-08). CN closes the verse 真主的援助确是近的 with no corrective at the pivot.
- **2:260** — Abraham's "Yes —" absorbed into the verb 信 ("[I] believe, but…"); affirmative polarity preserved, particle not carried.
- **3:125** — Balaa "Yes —" folded into 够了 answering v.124's question; the verse-initial affirmative particle is not rendered in place.
- **34:3** — EN affirmative balaa ("Yes — by my Lord") answered with negative-form 不然. Sense survives as rebuttal of the deniers' "will not come"; surface polarity vs EN flipped.
- **40:50** — Balaa with no EN dash token (EN: plain "'Yes.'"); CN 是的 carries it.
- **48:15** — God's corrective rendered 其实； CN additionally inserts 不 into the laggards' quoted speech, where the EN has no particle.
- **58:22** — CN verse text runs into the Surah 59 header in the staging file (extraction boundary, cf. Lane reports); the particle grading is unaffected.
- **64:7** — Same construction as 34:3: "Yes — by my Lord, you will be raised" → 不然. Surface flip; sense preserved as rebuttal.
- **74:16** — Kalla with no EN dash token (EN: "No."); CN 绝不！ restores the exclamatory corrective.
- **74:54** — Kalla answered with 然而 ("however") — contrastive conjunction, no corrective.
- **75:4** — EN "Yes indeed — We have the power" → 不然；我确能…. Surface flip; capability still affirmed after the particle.
- **75:20** — Kalla answered with the lament interjection 唉 — no corrective.
- **84:15** — Type specimen (PATCH-INDEX Addendum 2 §6). EN "Yes — his Lord was watching him" → 不，他的主一直在看着他. The corrective's affirmative force is negated at the surface.
- **90:1** — Oath laa ("No — I swear"); CN renders the oath plainly. Same drop at 69:38, 70:40, 81:15, 84:16 ("So no —").
- **96:19** — CN verse text runs into sajda furniture + Surah 97 header (P-07 territory); particle 不，不要服从他 is intact.
