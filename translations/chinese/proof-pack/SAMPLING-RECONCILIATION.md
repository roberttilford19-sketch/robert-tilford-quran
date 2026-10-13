# SAMPLING → INDEX RECONCILIATION — Chinese Ayah Companion

**Date:** 2026-10-12 (night, after Patch Set 1 application) · **Mode:** REPORT ONLY — no manuscript was edited.
**Question put:** the verified Surah 2 sampling fault at **2:93** received no row in the Patch Index or the Application Manifest and survived Patch Set 1 unrepaired. Is it the only escapee?
**Answer:** **No. There are three true escapees — 2:93, 2:286, and one sub-item at 2:285 — all verified REAL firsthand.** Two further sampling defects (2:26, 2:99) are uncovered by design (a logged hold, not an escape), and four sampling flags stand unrepaired because the sampling itself adjudicated them VARIATIONS, not defects. Everything else the sampling asserted is covered.

**Sources swept for fault assertions:**
- `~/workspace/ayah-chinese/sampling-2026-10-12/SURAH2-SAMPLING-REPORT.md` (the crew report, F-list)
- `~/workspace/ayah-chinese/sampling-2026-10-12/GEMINI-PREFLIGHT-PROPOSAL-UNEXECUTED.md` (Gemini's banked rule list — residue of its sampling findings)
- `~/workspace/ayah-chinese/sampling-2026-10-12/FULL-CENSUS-STEP1-2026-10-12.md` (Step-1 census, in the sampling folder)
- `~/workspace/ayah-chinese/sweep-2026-10-12/PROBE-PACK.md` (entries attributing faults to the sampling)
- `gemini-feed/SURAH2-FEED-1..6.txt` — swept: these are INPUT packs (prompts + verse texts); they carry no findings. Gemini's returned audits were graded in session; the graded items that survive on disk do so via the preflight list, the probe-pack attributions, and individually named catches in Awen's session record (2:249, 2:243, 2:258, 2:285, 2:286 — each checked below).

**Coverage set:** every verse address carrying a row in `APPLICATION-MANIFEST.md` (724 rows — parser count matches the file's stated total exactly, incl. preserve rows and the P-11 supplement) + `PARTICLE-SUPPLEMENT.md` (9 rows) + `P03-SUPPLEMENT.md` (48 rows) = **781 rows / 774 distinct addresses**. Address-level coverage was substance-checked wherever a covering row might address a different fault than the sampling asserted (2:98, 2:158, 2:221, 2:88, 2:285, 2:222 — results inline).

---

## 1. The discrepancy that prompted this reconciliation

The probe pack (Entry 26) asserts the 2:93 fault was "Verified in the Surah 2 sampling." **The sampling report's on-disk text contains no mention of 2:93 or the calf** (grep: no `2:93`, no `calf`, no 牛犊 in `SURAH2-SAMPLING-REPORT.md`). The finding's on-disk trail runs through Gemini's side of the sampling instead: the banked preflight rule list (`GEMINI-PREFLIGHT-PROPOSAL-UNEXECUTED.md`, rule-list line) names **牛犊的爱** among the patterns banked from Gemini's Surah 2 work, and the probe pack preserved the finding with full quotes. The crew report's F-list was compiled from the crew's own read plus *some* Gemini catches (2:46 also reached the probe pack without reaching the F-list — see §4), but the hand-off from "Gemini flag, verified" to "report F-item" was lossy. That lossy seam — not the sweep's index build, which faithfully indexed the report and lane reports it was given — is where all three escapees fell through.

## 2. TRUE ESCAPEES — verified firsthand (3)

Each was checked against the staging anchor CN (`~/workspace/robert-tilford-quran-staging/translations/chinese/ayah-companion-manuscript-ZH.md`, sha `2030fe97…`) and the Recital EN master (`~/workspace/original-recital/files/original-recital-FULL.txt`, sha `c47105f2…`), and confirmed still present, byte-identical, in the live patched master (`patched/ayah-companion-manuscript-ZH-PATCHED.md`).

### E-1 · 2:93 — the calf demetaphorized. REAL.
- **Asserted fault:** EN "the calf was poured into their hearts" → CN 牛犊的爱充满了他们的心 ("the LOVE of the calf filled their hearts"): the calf itself becomes *love of* the calf; "poured into" becomes "filled." Demetaphorization / traditional gravity (the Arabic أُشْرِبُوا…الْعِجْلَ is likewise rendered with an inserted "love" in conventional translations).
- **EN (master):** "…And **the calf was poured into their hearts**, for their disbelief…"
- **CN (staging = patched master, unchanged):** 「因他们的不信，**牛犊的爱充满了他们的心**。」
- **Trail:** preflight banked list (牛犊的爱）; PROBE-PACK.md Entry 26 (line 223). Absent from the report, the Patch Index, the manifest, and both supplements.

### E-2 · 2:286 — a 主 added to "You are our Protector." REAL.
- **Asserted fault:** Gemini's Surah 2 audit (Part 6) flagged "2:286 added 主"; graded real in Awen's session record. The report does not carry it — worse, the report lists 2:286 among the sound set-pieces ("the great set-pieces （宝座之节， 2:238, 2:282, 2:286) are sound," report line 187, severity-calibration paragraph).
- **EN (master):** "…**You are our Protector** — so help us against the disbelieving people."
- **CN (staging = patched master, unchanged):** 「**你是我们的主和保护者**，援助我们对抗不信道的人民。」 — "You are our **Lord and** Protector": 主 (Lord) is added; the EN's single title "Protector" (mawlā) becomes two. (The prayer's earlier vocatives 我们的主啊 answer to EN "Our Lord" and are faithful; only this final clause adds.)
- **Trail:** no occurrence of "2:286" as a fault in any sweep document (grep across manifest, both supplements, Patch Index, probe pack, We census: none). The fault is physically present in both the anchor and the patched master; its assertion survives in the session record of the graded Gemini return.

### E-3 · 2:285 (sub-item) — "We heard and we obeyed" → "我们听从，我们顺服." REAL as described.
- **Asserted fault:** Gemini Part 6 catch "heard→听从", graded real in the session record. The address carries a manifest row — but the row is **P-02** (His Books → 他的这部经典， manifest line 124) and does not touch this clause: a covered address with an unrepaired sub-item, the same species as 2:93.
- **EN (master):** "And they said, '**We heard and we obeyed.** Your forgiveness, our Lord…'"
- **CN (staging; patched master identical at this clause):** 「他们说：“**我们听从，我们顺服**。我们的主啊，求你的宽恕…”」 — 听从 ("heed/obey") stands where the EN has the hearing verb; "heard" has no counterpart.
- **Trail:** the report's positive-controls section calls the 2:285 closing clean (report, "2:255/256/285/286 closings all clean"); the clause-level catch never entered the F-list, the index, or the manifest.

## 3. UNCOVERED BY DESIGN — the logged hold (2)

### 2:26 + 2:99 — the fasiq pair (report F4.8, line 125). Wording verified REAL; absence is deliberate.
- EN 2:26: "He leads astray by it only **the disobedient**" → CN 「他借此只使**作恶者**迷误」. EN 2:99: "none disbelieve in them but **the disobedient**" → CN 「只有**犯罪者**否认它们」. Same EN word (al-fāsiqīn), two different CN carriers （作恶者 / 犯罪者）, neither the glossary's — the inconsistency is factually as asserted (both verses confirmed unchanged in the patched master).
- **Why no row:** the Application Manifest's own exclusion list (header, "Verses deliberately excluded as candidates-not-proposed," item 1) names this pair explicitly: *"P-09f fasiq pair — 2:26, 2:99 … held with P-11e per the index (low confidence each); carrier choice is Robert's."* A known, logged hold awaiting Robert's carrier ruling — not a silent escape. It belongs to the standing P-11e queue.

## 4. ASSERTED, ADJUDICATED VARIATION, LEFT STANDING (4)

The sampling flagged these but ruled them VARIATIONS (not defects); Patch Set 1 took up defects, so no rows were built. Each wording is verified present exactly as described — they are listed here so the record distinguishes "left by adjudication" from "lost."

| Verse | Report ref | Asserted wording (verified) | Sampling verdict |
|---|---|---|---|
| 2:175 | F2.11, line 69 | EN "How patient they are toward the Fire!" → CN 「但他们为什么坚持火狱？」 — exclamation of wonder converted to a question | VARIATION leaning defect |
| 2:188 | F2.12, line 73 | EN "bring it to the judges" → CN 「把它作为贿赂送给官员」 — judges → officials; "as a bribe" made explicit | VARIATION |
| 2:208 | F2.13, line 77 | EN "enter into the peace, all of you" → CN 「你们要全心进入归顺」 — "the peace" → submission; "all of you" → "wholeheartedly" | VARIATION |
| 2:282 | Class 5 section, line ~141 | EN "if one of them errs, the other reminds her" → CN 「如果其中一个忘记，另一个提醒她」 — errs narrowed to forgets | variation, low-moderate |

## 5. COVERED — the rest of the sampling's assertions (47 items)

**Report DEFECT flags — 36 of 38 covered** (the 2 exceptions are the §3 hold):

| Flag | Verses | Flag | Verses |
|---|---|---|---|
| F2.1 (L21) | 2:61 | F4.1 (L89) | 2:83, 2:110, 2:277 |
| F2.2 (L26) | 2:104 | F4.2 (L102) | 2:111 |
| F2.3 (L31) | 2:54 | F4.3 (L107) | 2:158, 2:196 |
| F2.4 (L36) | 2:205 | F4.4 (L110) | 2:245 |
| F2.5 (L41) | 2:256, 2:257 | F4.5 (L113) | 2:96, 2:105, 2:135, 2:221 |
| F2.6 (L46) | 2:115, 2:272 | F4.6 (L117) | 2:34 |
| F2.7 (L51) | 2:220 | F4.7 (L122) | 2:114, 2:144, 2:149, 2:150, 2:187 (+2:196) |
| F2.8 (L55) | 2:276 | F4.8 residue (L125) | 2:88 （忘恩→不信 repaired in its row), 2:221 signs （启示→迹象 repaired in its row), 2:158 Marwa （麦尔维→麦尔瓦 in its row's proposed final) |
| F2.9 (L59) | 2:243, 2:251 | Class-5 shifts (L~141) | 2:10, 2:193, 2:240, 2:258, 2:259 |
| F2.10 (L64) | 2:177 | Class-6 nit (L145) | 2:222 — stray quote repaired by its P-07 row; patched master verified clean |

**Findings recorded outside the report — 5 of 8 covered** (the 3 exceptions are §2):
- **2:46** (probe pack Entry 25: "Gemini's best catch of the sampling" — EN "think" → CN 确信） — covered (P-10e row).
- **2:98** (preflight list: 米卡伊勒） — covered in substance: its P-09 row (manifest line 80) repairs 米卡伊勒 → 米迦勒 per the biblical-names ruling.
- **2:214** (probe pack Entry 22: kalla "No —" dropped, "verified in the original Surah 2 audit") — covered (P-08 row).
- **2:247 + 2:249** (probe pack Entry 23; Patch Index lines 375/489: Talut → 扫罗； 2:249 also think→确信） — covered.
- **2:243, 2:258** (Gemini Part 6 catches also in the report: F2.9 / Class-5) — covered (counted above).

**Step-1 census extras (`FULL-CENSUS-STEP1`, sampling folder) — 5 of 5 covered:** 44:48 （地狱 singleton), 5:12 （善债 split), 9:99, 9:103, 41:51 （祈祷 pool). The census's two large pools （多神教徒 32 verses, 施舍 62-verse review pool) named no further individual addresses in that document; their adjudicated members flowed through the lanes and are inside the manifest's class rows.

## 6. Cross-checks run so this answer does not rest on the F-list alone

- **Census flags, Surah 2 (35):** 33 covered. The 2 uncovered — **2:275, 2:278** (USURY-LIXI) — are Ruling-1 no-change controls (EN "usury" → 利息 stands by Robert's locked ruling), i.e., not faults. No escapee hides in the mechanical census.
- **回忆当时 ×12** (2:49, 2:50, 2:51, 2:53, 2:54, 2:55, 2:58, 2:60, 2:61, 2:63, 2:67, 2:72): appears in the sampling record ONLY as an item in Gemini's declined pre-clean rule list and as a census term count — the report never asserts it as a fault, and the three verses that carry patch rows (2:53, 2:54, 2:61) keep 回忆当时 in their Robert-approved final texts. Specimen verified firsthand (2:49: EN "And when We saved you…" → CN 「回忆当时，我们拯救你们…」). Disposition: a checked candidate pattern that no adjudication ever sustained — **not escapees**. If Robert ever rules the opener a fault, 9 verses (all but 2:53/2:54/2:61) would need fresh rows and the other 3 a rider.
- **Divine-We MIXED verses** (2:57, 27:82, 28:58, 30:28 — the class where a half-repair could hide): all four carry P-03 rows (2:57 in the manifest; 30:28 additionally carries the P-03 supplement's Mode-D row). No escapee.

## 7. NOT-A-FAULT — adjudicated in the sampling (do not mistake for escapees)

- **2:58** — hitta rendered by its meaning 「宽恕」: legitimate variation (report line 81).
- **2:84, 2:85** — 同胞 making the mutual sense explicit: expressly **"Not flagged (legitimate variation)"** (report line 81). (Gemini's preflight list had banked 同胞 as a scrub pattern; the crew's adjudication overruled it.)
- **2:106** — 一节 for "sign": genuinely ambiguous, legitimate (line 81).
- **2:262, 2:264** — 施恩图报 for "reminding [of the favor]": legitimate (line 81).
- **"The Book" distribution** — 2:2's 这部经典 correct; the surah's other ~25 bare-经典 occurrences expressly *"noted for the record, not counted a defect"* (F4.8). (The sweep nonetheless repaired the definite-Book population book-wide via P-02; the census cross-check above shows those Surah 2 verses covered.)
- **Glossary pre-documented 待统一 pairs** — not defects by the glossary's own marking: Almighty 万能的/全能的 (2:20, 2:106, 2:129, 2:209, 2:220, 2:240, 2:260), Criterion 准则/辨别真伪的标准 (2:53, 2:185). Item-specific caveat: 2:220 and 2:240 carry *separate* real defects (F2.7; Class-5 shift) — both covered.
- **Correct-render controls inside defect flags:** 2:43 and 2:177 (zakat ✓ — 2:177's defect is F2.10's narrowing pair, covered), 2:105 (bounty ✓ — its defect is F4.5's 多神教徒， covered), 2:255 (Throne Verse: clean control; probe pack Entry 1).

## 8. Totals

| Category | Items | Covered | Held by design | Standing by adjudication (variation) | TRUE ESCAPEES |
|---|---|---|---|---|---|
| Report DEFECT flags (incl. F4.8, Class-5 shifts) | 38 | 36 | 2 (2:26, 2:99) | — | 0 |
| Report VARIATION flags | 5 | 1 (2:222) | — | 4 (2:175, 2:188, 2:208, 2:282) | 0 |
| Findings outside the report (Gemini-side trail) | 8 | 5 | — | — | **3 (2:93, 2:286, 2:285 sub-item)** |
| Step-1 census extras | 5 | 5 | — | — | 0 |
| **Total** | **56** | **47** | **2** | **4** | **3 — all verified REAL** |

**Bottom line:** 2:93 is not the only escapee. The complete escapee set is **{2:93, 2:286, 2:285 (the heard→听从 clause)}** — three items, one species: Gemini sampling catches that were verified during the sampling but never written into the crew report's F-list, and therefore never indexed. All three persist verbatim in the patched master and are repairable by three small rows whenever Robert rules them. Nothing else the sampling asserted is missing: the remaining gaps are a logged hold (2:26/2:99, Robert's carrier ruling) and four variations the sampling itself declined to call defects.
