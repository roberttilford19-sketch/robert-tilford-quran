# North Frisian — Mooring (frr) Quran draft — INDEPENDENT CHECKER REPORT (2026-11-28)

Checker: fresh independent checker (built none of this text). Scope: verification only — nothing edited, landed, shelved, committed, or pushed. Every figure below was recomputed with the checker's own scripts against verses-store.json, master-verses.json, sources/kaikki-frr.jsonl, sources/mooring-forms.json, sources/mooring-plurals.json, and work/dict_core.py — not copied from verify.py or the build report.

## VERDICT: PASS-WITH-GAP-TIER-RESERVATION

All mechanical, fence, and honesty claims verify. The GAP-tier ruling is at §9, with its ground and conditions; it is the operative part of this report.

## 1. Seat grid — VERIFIED
- Store seats 6,236; Master seats 6,236; seat-set equality **true** (recomputed set comparison).
- Per-surah counts against the standard 114-surah grid: **mismatches NONE**.
- Empty seats: **NONE**. Seats containing "redacted": **NONE**.

## 2. GAP census — VERIFIED, exact
Recomputed from verses-store.json: **6,190 GAP-bearing seats; 50,826 markers; 5,551 distinct GAP terms** — identical to gap-census.json and the disclosure. Top terms match (god 2,786; for 1,744; who 1,724; those 1,189; lord 972; so 746; on 686; people 679; by 414). Only **46 of 6,236 seats are GAP-free** (mostly surah-head letter verses and short name verses); GAP seats are **99.26%** of the book, averaging 8.21 markers per GAP seat.

## 3. Basmalah — VERIFIED, exact at every occurrence
- Store 1:1 equals exactly «Önj noome ⟦GAP: god⟧, ⟦GAP: beneficent⟧, ⟦GAP: merciful⟧.»; 1:3 equals exactly «⟦GAP: beneficent⟧, ⟦GAP: merciful⟧.».
- In quran-frr.txt the fixed form occurs **113 times**: 112 unnumbered opening lines (every one byte-identical to the fixed form) plus numbered verse 1:1. Per-surah split confirms exactly one occurrence in each surah except surah 9, which carries **none**. No variant form occurs anywhere.

## 4. Dictionary — VERIFIED
- work/dict_core.py holds 494 candidate entries. Applying the checker's own inventory-trace test (every component of the Mooring form present in sources/mooring-forms.json): **429 verified, 65 unverified** — and the checker's unverified key set is exactly the set logged in work/unverified-dict.json and listed in the disclosure (after, against, ask, at, because, before, black, bright, by, …, who, why, without, work, young). The 65 are held as GAPs, not seated.

## 5. Harvest and dialect fence — VERIFIED (two clarifications, neither a failure)
- Checker's independent recount of kaikki-frr.jsonl under the disclosed screen rule: **463 Mooring-sensed entries, 113 untagged pan-dialect entries, 968 other-dialect-only entries** — exactly as claimed. These sum to 1,544; the dump's remaining 2 rows are index pages ("i/languages M to Z"), not entries, so the build's "1,546 entries" is the raw dump row count. Framing note only.
- sources/mooring-forms.json holds **3,685 forms** as listed (3,659 distinct lower-cased); sources/mooring-plurals.json holds **268** attested plurals; LearnFrisian Mooring pairs 178 — all as claimed.
- Token-trace screen (checker's own): 456 distinct seated tokens outside GAP markers; **every one traces to the Mooring inventory, the attested-plural set, or the explicit names allowlist — 0 untraced types, 0 tokens.** This is the operative retained-Latin result: the build's "0 candidates against the allowlist" claim is **confirmed independently**, and mixed-script (non-Latin) characters: **NONE**.
- Other-dialect-only forms: of 4,469 forms attested only for other dialects and absent from the Mooring inventory, **none is seated**, with two homograph exceptions that are not fence breaches: *Hud* (×7) and *Saad* (×3) are seated solely under the names policy — Hud the prophet (e.g. 11:50, "tu Aad, jare brouder Hud") and Saad as a surah-head letter name (e.g. "Kaf, Ha, Ya, Ayn, Saad.") — not as dialect vocabulary.
- Saterland / West Frisian fence: because 0 seated tokens are untraced, no Saterland or West Frisian form is seated either — any such form would appear as untraced unless it were simultaneously attested for Mooring, in which case it is a Mooring form by the gate's own rule. **Fence holds.**

## 6. Historical-control fence — VERIFIED
Bendsen 1860 forms are seated nowhere: seated-token counts for godd 0, göd 0, senne 0, gnahse 0, and none stands in the Mooring inventory. The 1860 spellings appear only in disclosure prose, as corroboration, exactly as the bar requires.

## 7. Headline GAP claim — VERIFIED by full-text reconciliation, not sampling alone
For each headline term, every Master occurrence is matched by a GAP marker in the built text (possessives reconciled: god+god's 2,810 Master = 2,810 GAP; lord+lord's 974 = 974):
god 2,786 (+24 god's), lord 972 (+2 lord's), heaven 40/40, heavens 192/192, angel 11/11, angels 77/77, soul 79/79, spirit 20/20, mercy 140/140, merciful 147/147, beneficent 20/20, sin 33/33, and the function words for 1,744/1,744, who 1,724/1,724, on 686/686, by 414/414. **None of these terms is silently seated anywhere.** The claim that they have no modern Mooring seat in the held inventories is also consistent with the harvest: no verified dictionary entry exists for any of them.

## 8. The three build bugs — VERIFIED FIXED
1. **gunge / "God":** DICT seats gunge only for "go"; "god" is not a dictionary entry at all. In the output, gunge occurs in 75 seats; the three seats where the Master also lacks go/going/gone were inspected individually — 11:123 ("authority goes back" → "gunge reeg"), 5:3 ("killed by a fall, gored…" — "gunge tu düüs", gone to death), 5:54 ("goes back on his religion" → "gunge reeg") — all genuine go-forms. No seat renders God as gunge.
2. **hat / "it":** hat is in the Mooring inventory, DICT seats "it" → hat, and 903 seats where the Master has "it" carry seated hat. The wrongful exclusion is gone.
3. **diling / "this":** DICT seats diling only for "today"; "this" has no entry and stands as ⟦GAP: this⟧ 437 times. All 34 seats containing seated diling have "today"/"this day" in the Master — none renders "this" as diling.

## 9. RULING ON THE GAP TIER — PASS-WITH-GAP-TIER-RESERVATION
The tier is extreme and is stated plainly: 6,190 of 6,236 seats (99.26%) carry GAP markers; 50,826 markers in total; the Basmalah itself — the most familiar line in the book — is GAP-bearing for god, beneficent, and merciful; core theological vocabulary (God, lord, heaven, angel, soul, spirit, mercy, sin) and core function words (for, who, on, by) are GAPs throughout; only 46 seats are GAP-free. This is materially beyond the GAP mass of the sibling lanes.

**Ruling: this tier does NOT cross into FAIL, and the draft IS landable as a DRAFT — NOT PUBLISHED skeleton under PASS-WITH-GAP-TIER-RESERVATION.** Ground, in order:
1. The gate law's own remedy for an unattested seat is the visible GAP marker, never an invented or borrowed form. Every alternative to this skeleton that would reduce the GAP count — seating Bendsen's 1860 spellings as modern forms, borrowing from Söl'ring/Fering-Öömrang, Saterland, West Frisian, German, or English — is expressly barred, and this checker verified none was used. A FAIL verdict here would punish the build for obeying the fence and would create a perverse incentive toward exactly the silent borrowing the gate exists to prevent.
2. Nothing is hidden: the GAP census, the God/mercy GAPs, and the Basmalah's GAP form are disclosed on the manuscript's face, in the build report's headline item, in BUILD-SPEC, in the glossary, and in the attestation audit — the same-breath standard is met. A reader meets the gaps before the text.
3. Every mechanical and fence claim the build made was recomputed by this checker and held exactly (§§1–8). The skeleton's seated 429-entry core is genuinely attested Mooring, and its GAP map (5,551 terms, counted) is itself a usable work product: it tells a future checker with the modern print Mooring dictionaries precisely which seats to close, in frequency order.

**Reservation, binding on any landing:** the reservation is the tier itself. What lands is a lexical skeleton and GAP map, not a readable Mooring translation of the Quran, and it must never be described — on the shelf, in a manifest, or in any post — as a translation without the GAP tier carried in the same breath (6,190 of 6,236 seats GAP-bearing; God and the Basmalah mercy names among the GAPs). Landing is authorised by this verdict only under the existing label **DRAFT — NOT PUBLISHED**, with the manuscript's current honest face unchanged. Any future reduction of the GAP tier must come from attested modern Mooring sources (the named print dictionaries, under fact-and-citation fair use), re-verified — never from relaxing the dialect or historical fences.

## 10. Honest labelling — VERIFIED
Manuscript face carries **DRAFT — NOT PUBLISHED** and states it has not been independently checked (true at build time; this report is that check) and not been published. No "first" claim in any form: the only "first" tokens are "first-pass" (a build-tier description) and ⟦GAP: first⟧ in the text — "first" is itself one of the 65 unverified candidates held as a GAP, which is the opposite of a novelty claim. The bounded finding ("no North Frisian Quran was found in the searches of 27 November 2026; not found is not proven non-existent") is carried verbatim in substance.

## Failure lists
None. No failing seats, no untraced tokens, no fence breaches, no count mismatches were found; accordingly there are no failure seat lists to attach. The two clarifications at §5 (1544 classified entries + 2 index rows = 1,546 dump rows; Hud/Saad homographs seated under the names policy only) are recorded for completeness and require no repair.

— Independent checker, 2026-11-28. This report makes no landing, shelving, commit, or push; the desk acts on §9.
