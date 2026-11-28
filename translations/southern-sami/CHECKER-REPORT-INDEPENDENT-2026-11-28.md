# Southern Sámi (sma) Quran draft — FRESH INDEPENDENT CHECKER REPORT

Checker date: 2026-11-28. Checker built none of this text and edits nothing: no text edited, landed, shelved, committed, or pushed by this check.
Materials checked: BUILD-REPORT.md, BUILD-SPEC.md, LICENCES-RECORDED-2026-11-28.md, FLAGS-AND-GAPS-DISCLOSURE-SMA-2026-11-28.md, glossary.md, ayah-companion-manuscript-SMA.md, quran-sma.json/.txt, verses-store.json, master-verses.json, verify.py, work/{eng2sma.json, gap-census.json, names-allowlist.json, unverified-dict.json, verify-candidates.json}, sources/{attestation-inventory.json, dict-2022-parsed.json, eng-saami.txt, lang-sma lexc stems}, and the candidate brief CANDIDATE-BRIEF-SOUTHERN-SAMI.md.
Method: every figure below was recomputed by the checker's own scripts from the seat files themselves. verify.py was read for its stated method but its output was not taken as evidence; where the checker's tokenisation differs from verify.py's, the difference is stated and resolved.

## Verdict

**PASS-WITH-GAP-TIER-RESERVATION.**

Every mechanical claim in the build report and the flags disclosure recomputes exactly as stated (sections 1–6 below), the Sámi fence holds (section 5), and the labelling is honest (section 6). The reservation is the GAP tier, ruled on explicitly in section 7: 5,762 of 6,236 seats (92.4%) carry GAP markers and the core theological terms lord / angel / prophet / scripture / reward / revelation carry no attested seat at all. That load is fully disclosed on the book's face and held open under the gate law — nothing invented, nothing borrowed — so, as with the sibling lanes, it passes as a first-pass GAP-tier draft. It does not pass, and is not labelled, as a readable finished translation.

## 1. Master, seat set, grid, empty/redacted seats — all claims CONFIRMED

- Locked English Master file (~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md) MD5 recomputed: **ecc5b8e2848e5044186b7ad82bed9f4e** — matches the claimed MD5 exactly.
- verses-store.json: **6,236 seats**; master-verses.json: **6,236 seats**; quran-sma.json: **6,236 seats**. Seat-set equality store == master == quran-sma.json: **TRUE** on all pairs, and quran-sma.json texts are identical to verses-store.json texts at every seat.
- Per-surah grid against the standard 6,236 grid (sums to 6,236): **mismatches NONE** for both store and master; out-of-grid seat keys: NONE.
- Empty seats: **NONE**. Whitespace-padded seats: NONE.
- 'redacted' seats in the draft: **NONE** — verified by byte search of verses-store.json and quran-sma.json, not only by display reading. Note for the record: the held master-verses.json copy and the Locked Master .md also contain no literal "redacted" string on byte search, so build.py's `replace("<redacted>", " ")` is a safeguard that fires on nothing in the held copies; the two seats the spec names (39:7, 48:8) were read directly and render their surrounding sense with GAP markers where unseated (39:7 and 48:8 texts inspected in full). The claim as made about the draft — no 'redacted' seats — holds.
- Manuscript cross-check: ayah-companion-manuscript-SMA.md carries exactly **6,236 numbered verse refs**, 114 surah headings, and its verse texts are **identical to verses-store.json at all 6,236 seats** (0 differences). Its body carries exactly 24,673 GAP markers; the one further '⟦GAP' occurrence is the front matter's own explanation of the marker format.

## 2. Basmalah — CONFIRMED

- 1:1 == **«Nomme Jupmele, Åårmegs, Åårmegs.»** — exact.
- 1:3 == **«Åårmegs, Åårmegs.»** — exact.
- quran-sma.txt: lines exactly equal to the Basmalah: **112**, all unnumbered; per-block count confirms every surah except 1 and 9 carries exactly one, surah 9 carries none (first line is 9:1), and surah 1 carries none beyond the numbered 1:1. 114 surah headers present.
- The three Basmalah seats are attested: nomme, Jupmele, åårmegs all stand in the attestation inventory; the single-form mercy seating (both mercy names on the one attested adjective åårmegs) is disclosed in BUILD-SPEC.md, the glossary, and the manuscript front matter.

## 3. Dictionary and attestation inventory — CONFIRMED, with the union arithmetic stated

- work/eng2sma.json: **4,308 English seat keys** — exact.
- GiellaLT lemmas, re-harvested by the checker from the lang-sma lexc stem files (same harvest rules: citation form before ':', %-escapes stripped, Norwegian-practice conversion, token filter): **55,600** — exact.
- 2022-dictionary forms, re-harvested by the checker from sources/eng-saami.txt: **6,808** — exact.
- Union: 55,600 + 6,808 − 5,248 forms present in both = **57,160** — the stored sources/attestation-inventory.json is **identical as a set** to the checker's recomputed union. (The build report's phrasing "57,160 forms (55,600 + 6,808)" is a union figure, not a sum; the overlap of 5,248 is stated here so the figure travels with its arithmetic.) Dictionary-only contribution: 1,560 forms.
- Stored sources/dict-2022-parsed.json (3,523 single-word keys) is identical to the checker's re-parse.
- Every eng2sma value (3,143 distinct forms) traces to the inventory — no eng2sma seat stands outside the attested base.
- The one dropped unverified seat: work/unverified-dict.json holds exactly {revelation → volverimmie}; 'revelation' is **not** a key in eng2sma.json and 'volverimmie' appears **nowhere** in the draft text or the dictionary values. CONFIRMED.

## 4. GAP census — CONFIRMED figure for figure

Recomputed from verses-store.json with the checker's own marker extraction:

- Seats carrying GAP markers: **5,762 of 6,236** (474 seats carry none).
- GAP markers total: **24,673**. Distinct GAP terms: **3,509**.
- Largest terms, recomputed: **of 3,502; lord 972; by 414**; nor 270; except 269; into 192; give 190; given 172; whom 155; any 154; everything 150; used 149; can 145; righteous 141; revealed 141; revelations 135; disbelieve 133; another 132; reward 120; worship 115; scripture 115 — matching the disclosure's top list in order and count.
- work/gap-census.json's stored counter is **identical** to the recomputed counter, term for term.
- Marker hygiene: malformed markers (⟦GAP without ⟧): 0; stray ⟦/⟧ outside well-formed markers: NONE.

## 5. Screens and the Sámi fence — CONFIRMED, exactly the 2 disclosed candidates

- Token attestation: with verify.py-equivalent tokenisation the checker counts **1,604 distinct seated tokens**, matching the claim. Untraced candidates: **exactly 2, and no others** —
  1. `jupmele?'“satne` at **5:116** — two attested words (Jupmele, satne) fused by Master punctuation without a space; a tokenisation artefact, as disclosed.
  2. `kraevies-åejjie-goelkh` at **73:17** — hyphenated compound; parts checked individually by the checker: kraevies ∈ inventory, åejjie ∈ inventory, **goelkh ∉ inventory** as a standalone part (the two-part compound åejjie-goelkh does stand in the inventory as a whole, which is how its other seats at 19:4 and 30:54 trace). As disclosed: a compound with a part outside the harvested inventory. It stands as a disclosed candidate, not a hidden defect; a future repair seat, not a failure of this check.
- Tokenisation note (the checker's own stricter passes, resolved): a whitespace-only tokeniser produces ~300 further "untraced" strings, every one an em-dash-joined pair of attested words (the Master joins clauses with — without spaces) or a hyphen-edge fragment; splitting on em/en dashes and stripping edge punctuation — as verify.py does — resolves all of them to attested parts. No additional untraced token survives that resolution beyond the 2 above.
- Retained English: whitespace-token screen against the names allowlist (**135 types** recomputed — the stored file holds exactly 135, every one of them a capitalised word that actually occurs in the Master): **0 non-allowlist candidates**, under both verify.py-equivalent and the checker's refined tokenisation. Cross-check from the other direction: of the Master's 1,074 distinct capitalised words, **none** of the 939 non-allowlist words appears verbatim anywhere in the draft — capitalised epithets did not ride the allowlist.
- Mixed script: **NONE** — no token mixes scripts; stronger, the draft contains **no non-Latin-script letters at all**.
- The Sámi fence: every seated token traces to the Southern Sámi attestation inventory (GiellaLT lang-sma + the 2022 dictionary) or the names allowlist, so no Northern Sámi (sme), Lule Sámi (smj), or Skolt Sámi (sms) form is seated. Corroborating probes by the checker: no token carries the distinctive sme/smj diacritics (á, č, đ, ŋ, š, ŧ, ž) or sms characters; distinctive sme forms (e.g. Ipmil for God) are absent — God is seated Jupmele throughout. One probe word required a direct ruling: the token **hearra** (seats 5:63, 5:82, 9:31, 9:34, seating "priests") looks like Northern Sámi hearrá "lord", but it stands in GiellaLT lang-sma's own nouns.lexc as a Southern Sámi noun (hearra+N, Sem/Hum) and in the sma inventory — it is sma-attested, carries no á, and seats "priests", not "lord" (lord is GAP at 9:31 itself). The fence holds; the homograph is recorded here so a later reader does not mistake it.
- Orthography practice: the draft contains **zero** ä/ö/Ä/Ö characters; æ (1,433), ø (1,492), å (18,771) and ï (5,704) carry the text — the Norwegian spelling practice (æ/ø) is applied throughout, mechanically only, with the Swedish practice (ä/ö) recorded as preserved dissent in BUILD-SPEC.md, exactly as claimed.

## 6. No attested seat claimed for the six terms; labelling — CONFIRMED

- lord, angel, prophet, scripture, reward, revelation: **none is a key in eng2sma.json**; all ride GAP markers (recomputed GAP counts: lord 972, scripture 115, reward 120, prophet 53, revelation 13, angel 11 — the singular-term counts; related forms such as revelations 135 and angels likewise GAP). The glossary states the same in words: "Lord, angel, prophet, scripture, reward, revelation and 'of' carry GAP markers: no attested seat was found… and none was invented or borrowed." No document in the lane claims an attested seat for any of the six.
- Honest labelling: the manuscript's front matter carries **DRAFT — NOT PUBLISHED** and states the machine-rendered first-pass nature, the GAP census, the fence, and the fact-and-citation-only controls on its face. "First" wording: a full-text search of the manuscript, build report, spec, disclosure, glossary, and licence record finds "first" only in "first-pass" (the draft's tier), in the build report's explicit "NO 'first' wording" statement, and as a dictionary entry in the glossary (first — voestegh). **No "first translation" claim of any kind appears anywhere.**
- Prior-translation position: the manuscript and build report state that no Southern Sámi Qur'an was found in the searches named in the candidate brief (web search by name including Norwegian and Swedish forms, QuranEnc list, Quran Touch list), tier **not found, not proven non-existent** — identical to the brief's §6 finding and tier. Nothing stronger is claimed anywhere in the lane.
- Landing state: the shelf at ~/workspace/robert-tilford-quran/translations/ contains **no southern-sami / sma folder** (northern-sami and lule-sami folders present are other lanes' work). Nothing in this lane has been landed or shelved, consistent with the build report.

## 7. Ruling on the GAP tier (explicit, as the sibling-lane checkers ruled)

The GAP load is the largest fact about this draft: 24,673 markers across 5,762 of 6,236 seats (92.4% of seats; only 474 seats marker-free), 3,509 distinct unseated terms, and the unseated set is not peripheral — it includes the genitive relation itself (of, 3,502) and the core theological vocabulary (lord, angel, prophet, scripture, reward, revelation, worship, righteous). A reader meeting this text meets a Southern Sámi frame carrying its central content as visible English GAP terms.

The tier is nevertheless honestly carried, on four grounds the checker verified rather than assumed: (1) every marker is visible inline in the text and in the manuscript, and the census is printed on the book's face, not buried; (2) the held-open seats are exactly the seats the harvested licence-verified sources do not attest — the checker's re-harvest reproduced the attested base form-for-form, and the one curated seat that failed verification (revelation → volverimmie) was dropped and logged rather than seated; (3) no gap was filled by invention or by borrowing from Northern Sámi, Lule Sámi, Skolt Sámi, or any neighbouring language — the fence screens in section 5 are the evidence; (4) the draft labels itself a machine-rendered first pass, DRAFT — NOT PUBLISHED, everywhere it presents itself.

**Ruling: the GAP tier stands as disclosed. The draft passes at the GAP tier — a complete, honest, seat-for-seat first-pass skeleton with its gaps held open — and the reservation on the verdict records that it is not, and must not be represented as, a readable Southern Sámi translation of the Quran. Closing the reservation would require attested seats for the core terms from sources not harvested here (e.g. a licence-read Bergsland & Magga (1993) or the 2024 New Testament's vocabulary harvested under a verified licence), which is a build decision for Robert, not a checker repair.**

## Failure lists

None. No claim failed recomputation, so no failure seat lists arise. The two disclosed untraced candidates (5:116 punctuation fusion; 73:17 kraevies-åejjie-goelkh) stand as disclosed in the flags file and are recorded in section 5 with their seats; neither is a failure of any stated claim.

*End of checker report. The checker edited no text and took no landing, shelving, commit, or push action.*
