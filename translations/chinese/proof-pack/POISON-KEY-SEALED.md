# POISON KEY — SEALED

**SEALED — NEVER FEED TO GEMINI (OR ANY AUDITOR).** This key maps the poison mini-pack IDs (`POISON-FEED-A-CN.txt` / `POISON-FEED-B-EN.txt`) to their base verses, corruptions, and clean controls. If this file reaches the auditor, the sensitivity test is void.

- Built 2026-10-12, after Robert adopted the poison mini-pack (~23:19 CDT). **Amended the same night**: the original 5-entry all-corrupted pack was salted with 3 CLEAN CONTROLS (verbatim v5, zero corruption) after an external critique pointed out that an all-poison series can be "passed" trivially by flagging everything. The pack is now 8 entries: 5 corrupted + 3 clean; the auditor cannot assume any given entry is poisoned.
- Base texts: v5 master `d8e1d3c3…`; each base verse CLEAN in v5. Corrupted entries machine-diffed: fed text differs from v5 by the single intended corruption only (one diff region, inside the intended span; exact reconstruction — re-verified at amendment). Clean entries byte-identical to their v5 verse blocks (CN text portion, re-verified).
- Shuffle: deterministic — Python `random.Random(20261014).shuffle()` over the eight build slots (5 corrupted in original build order, then 3 clean controls); PZ-01…PZ-08 assigned in shuffled sequence. (Supersedes the original `random.Random(20261013)` 5-entry assignment; the five corrupted fed texts themselves are byte-identical to the original pack.)
- Feed order: AFTER the main 39 entries close. Expected behavior — corrupted entry: Step-1 blind translation exposes the corruption in English; Step-2 verdict = DIVERGENT quoting the corrupted token. A FAITHFUL or CONTROL-PASS on a corrupted entry = the auditor alarm failed on that corruption class. Clean control: expected FAITHFUL / CONTROL-PASS; a DIVERGENT on a clean entry = a false positive, scored against specificity.
- Overlap: none of the eight base verses is in the main 39; the three clean controls do not overlap the five poison bases. (2:257 chosen over 2:256 in the original build because 2:256 is PX-15; the two are the only 暴君 verses in the book.)

## PZ-01 — 108:1 — CORRUPTED — pronoun flattening 我们→我
- v5 original span: 「我们」
- Fed (corrupted) span: 「我」
- Full v5 verse: 我们确已赐给你丰盛。
- Fed verse: 我确已赐给你丰盛。
- Expected: DIVERGENT, quoting 「我」. Desk note: EN warrant: "We have given you the Abundance." — divine plural flattened to singular (P-03 signature fault).

## PZ-02 — 15:9 — CLEAN CONTROL — divine-We control
- Full v5 verse (= fed verse, verbatim): 我们确已降示了讯息，我们确将保护它。
- Expected: FAITHFUL / CONTROL-PASS. Desk note: Verbatim v5. Two divine 我们 clauses intact ("我们确已降示了讯息，我们确将保护它") — mirrors the pronoun-flattening class with zero corruption. Expected: FAITHFUL / CONTROL-PASS.

## PZ-03 — 31:4 — CORRUPTED — zakat breach 天课→施舍
- v5 original span: 「天课」
- Fed (corrupted) span: 「施舍」
- Full v5 verse: 他们谨守礼拜，完纳天课，确信后世。
- Fed verse: 他们谨守礼拜，完纳施舍，确信后世。
- Expected: DIVERGENT, quoting 「施舍」. Desk note: P-01 signature breach: EN "zakat" must carry 天课； 施舍 (charity/alms) is the classic substitution repaired 7x in Patch Set 1.

## PZ-04 — 12:4 — CLEAN CONTROL — ordinary narrative control
- Full v5 verse (= fed verse, verbatim): 当时约瑟对他的父亲说：“父亲啊，我梦见十一颗星星，还有太阳和月亮；我看见它们向我叩头。”
- Expected: FAITHFUL / CONTROL-PASS. Desk note: Verbatim v5. Joseph's dream — plain narrative verse, no locked-carrier tripwires. Expected: FAITHFUL / CONTROL-PASS.

## PZ-05 — 3:151 — CORRUPTED — dropped clause
- v5 original span: 「，因为他们把真主未降示任何凭据的伙伴归于真主」
- Fed (corrupted) span: *(span deleted; text runs on without it)*
- Full v5 verse: 我们将把恐怖投入不信道者的心，因为他们把真主未降示任何凭据的伙伴归于真主。他们的居所是火狱。作恶者的居所真恶劣。
- Fed verse: 我们将把恐怖投入不信道者的心。他们的居所是火狱。作恶者的居所真恶劣。
- Expected: DIVERGENT, quoting 「，因为他们把真主未降示任何凭据的伙伴归于真主」. Desk note: EN warrant contains the causal clause "because they gave God partners for which He sent down no authority" — dropped wholesale (P-10 omission class).

## PZ-06 — 2:257 — CORRUPTED — banned carrier 暴君→恶魔
- v5 original span: 「暴君」
- Fed (corrupted) span: 「恶魔」
- Full v5 verse: 真主是信道者的主；他把他们从黑暗带入光明。至于不信道者，他们的保护者是暴君；他们把他们从光明带入黑暗——这些人是火狱的居民，他们将永居其中。
- Fed verse: 真主是信道者的主；他把他们从黑暗带入光明。至于不信道者，他们的保护者是恶魔；他们把他们从光明带入黑暗——这些人是火狱的居民，他们将永居其中。
- Expected: DIVERGENT, quoting 「恶魔」. Desk note: Ruling 2A: EN "the tyrants" at 2:257 takes 暴君； 恶魔 is the taghoot breach carrier repaired in Patch Set 1.

## PZ-07 — 49:15 — CLEAN CONTROL — 信道者 control
- Full v5 verse (= fed verse, verbatim): 信道者是那些信真主和他的使者，然后毫不怀疑，并以财产和生命为真主的事业而奋斗的人。这些人是诚实的。
- Expected: FAITHFUL / CONTROL-PASS. Desk note: Verbatim v5. Carries the locked carrier 信道者 prominently ("信道者是那些…") — superficially resembles the 信徒-corruption class, but the text is untouched. Expected: FAITHFUL / CONTROL-PASS. A DIVERGENT here = false positive.

## PZ-08 — 8:4 — CORRUPTED — banned carrier 信道者→信徒
- v5 original span: 「信道者」
- Fed (corrupted) span: 「信徒」
- Full v5 verse: 这些是真正的信道者。他们在他们的主那里有高品级，有赦宥，有丰厚的给养。
- Fed verse: 这些是真正的信徒。他们在他们的主那里有高品级，有赦宥，有丰厚的给养。
- Expected: DIVERGENT, quoting 「信徒」. Desk note: "These are the true believers" — CN 信道者 is the locked carrier (P-05); 信徒 is the banned substitute.
