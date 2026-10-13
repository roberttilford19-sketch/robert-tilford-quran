# How This Edition Was Compiled — Process Note
### Chinese Ayah Companion — Revision 2026-10-12 — Patch Set 1
*This note accompanies the edition; it is not part of the Quran text. Final master: sha256 `50116db0f1a735917c1a91c0cf927006fd83784386610e8a1e3bf9a1216c2382`.*

## The text and its source

The Chinese text of this edition renders one source only: Robert Tilford's English Recital of the Quran. Where the Chinese, as first published, departed from that English — by importing the phrasing of earlier Chinese translations, by glossary drift, or by editorial furniture typeset into the verses — this revision restores the English reading, verse by verse. The Arabic was not touched: 639,899 characters, byte-identical before and after, across all 6,236 verses in 114 surahs.

## How the audit was run

1. **A deterministic census** of the full manuscript (every verse counted, paired, and flagged by machine rule).
2. **Four independent reading lanes**, each auditing a quarter of the book against the English, adjudicating every machine flag in context: 89 of 89 sustained.
3. **An application manifest** — every proposed repair written out in full before any file changed: the exact English warrant, the current Chinese, the proposed Chinese, one row per verse.
4. **Four rulings by the editor** where the audit reached a question of principle (the rendering of *riba*, of *taghoot*, of the worship sites, and of *al-Ghayb*), governed by one principle adopted during the work: *the Chinese matches the editor's English in the verse it stands in; uniformity never overrides a deliberate English variation.*
5. **Application under an assert-or-refuse rule** — a repair was written only where its target text matched exactly, inside its own verse; anything that failed to match was quarantined, diagnosed, and cleared in a second pass. Nothing was forced.
6. **Two further independent censuses** (of the divine pronoun "We" and of the corrective particles), built separately from the manifest. Each found faults the first pass had missed; each disagreement between instruments was reconciled in the open, and the additional repairs were approved by the editor and applied the same way.
7. **A final reconciliation sweep** across all earlier findings, which caught three verses that had fallen between reports — repaired before publication, not after.

In total: **780 approved repair rows** (719 in Patch Set 1, 9 particle repairs, 48 pronoun repairs, 3 reconciliation escapees, 1 probe mini-supplement), plus one carrier harmonization ruled separately — every row warranted, counted, and receipted.

## Five engines, one editor

This manuscript was audited with the participation of five advanced AI systems, each in a defined role: **Muse** (lead; verification of every flag against the source texts), **Gemini** (independent dual audit of Surah 2; blind back-translation auditor for the final probe), **Perplexity** (cross-review — its challenge corrected the scope of one ruling and caught a polarity reversal; it also reviewed this probe's closure statement), **Grok** (concurrence review of the term rulings), and **Claude** (review of the validation design).

No system's output was ever applied on its own authority. External flags were treated as unproven until verified line-by-line against the manuscripts — and a material number did not survive verification (24 lane addresses and 2 reported faults were discharged as unsustained; one external patch script was refused outright as corrupt). Every ruling in this edition was made by the editor, Robert Tilford, in person, one question at a time.

## Verification

Each stage closed with hard gates: verse parity (6,236 of 6,236, in sequence), Arabic invariance, byte-identity of every verse the editor ruled untouchable, and a full census re-run — which now returns five flags in the entire book, all five being verses the editor ruled shall keep their wording. The manuscript's history is a hash chain any reader can re-perform: anchor `2030fe97…` → `368835ad…` → `11b3a78a…` → `cf1c317b…` → `439bbac0…` → `d8e1d3c3…` → final `50116db0…`.

## The probe

As the final regression check, a 39-entry pack — drawn from every repair class, plus known-clean controls — was back-translated blind by an external engine (Gemini) that had not seen the English, then judged entry by entry against it, under decision rules committed to writing before the run began. Every return was verified at the lead desk against both manuscripts.

The probe found **one verified divergence**: at 23:27 a pronoun repair had swept a deliberately singular address ("do not speak to **Me**") into the plural. The external auditor, comparing his own blind translation against the English, flagged the same span independently. The editor approved a one-character repair; the patched master (v6, hash above) was re-probed at that entry under blind conditions, and the blind translation returned "speak to Me" — the repair confirmed in the text a reader receives. One further entry (17:7) proved to be a divergence of the *English* from the Arabic the Chinese follows; it is logged for the editor's English-side ruling and does not concern this edition's text. Of the five clean controls, four passed and one drew a false flag. One entry (2:255) could not be audited externally — the external engine repeatedly declined the text — and was adjudicated at the lead desk, clause by clause, and is recorded as such.

An 8-entry calibration pack (five deliberately corrupted texts, three clean) was then run to measure the auditor. In that run his verdict step **ceased to discriminate** altered from authentic text (sensitivity 0 of 5; specificity 3 of 3): two corruptions that reached his blind translations intact — a flattened divine pronoun and an amputated clause — were passed against English texts that contradicted them. Two lexical corruptions never reached his translations at all: the substituted words were observably replaced by the standard terms in his back-translations (alms-word in, "zakat" out; devils in, "tyrants" out). These are recorded as limits of that instrument. The assurance of this edition does not rest on the auditor's passes; it rests on the census, the lane audits, and the lead desk's verification, with the auditor's engaged-mode catch at 23:27 as corroboration.

## Honest limits

This edition was audited mechanically and by cross-model review; it has not had a native-speaker review. Claims made for it are limited to what the receipts in the accompanying proof pack can prove.

## The editor's assessment

*Check, recheck, and check again — that was the method. It is my assessment that this is the most advanced and best possible rendering under the circumstances of the present moment: five of the world's most advanced AI systems, working one manuscript, under one editor, with nothing applied that was not verified against the source. I know of no other effort that combines all of these.* — R.T.
