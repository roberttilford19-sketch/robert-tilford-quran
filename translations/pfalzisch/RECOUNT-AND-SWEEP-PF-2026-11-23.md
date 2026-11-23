# RECOUNT AND SWEEP — Pfälzisch Quran, 2026-11-23

Manuscript: `QURAN-PFALZISCH-2026-11-23.md` (assembled from 17 worker chunks; pre-corrections copy preserved at `work/QURAN-PFALZISCH-PRE-CORRECTIONS.md`). Battery: `work/verify.py`, run against the Locked English Master parse (`work/master-parsed.json`).

## Recount — ALL PASS (post-corrections run)

- Verse count: **6,236 / 6,236**; verse-marker sequence **identical to the master**, seat for seat.
- Per-surah counts: **114 / 114** exact, zero mismatches (also reconciled at parse time against the verse counts printed in the master's own surah name lines).
- Arabic: **6,348 lines** (6,236 verse lines + 112 surah-opening Basmalah lines), **sequence byte-identical to the master** — the Arabic was never retyped; assembly reinserted it from the master parse programmatically.
- Basmalah: locked line *Ém Name vón Gott, de Gnädiche, de Barmherziche.* stands at all **112** surah openings (italic apparatus line); Surah 9 has none; 1:1 is the locked line itself as a verse; total locked-line occurrences 114 (112 openings + 1:1 + the letter of Solomon at 27:30, where the master's verse text itself carries the full line).
- Sajda notes: **15 / 15** at the master's own seats — 11 *empfohlen* (7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 22:77, 25:60, 27:26, 38:24, 84:21), 4 *gebott* (32:15, 41:38, 53:62, 96:19).
- No "%" and no "Prozent" anywhere — zakat carries no percentage, as the master gives none.
- Naming: the words Volga/Wolga occur exactly once in the manuscript — in the front matter's disclaimer sentence, "It is not Volga German." The book is nowhere labelled or described as Volga German.

## Attestation (Purple-style sweep, REPORT mode)

Computed over the book's own text only (verse text, surah summaries, Basmalah lines; front matter, chapter headings, surah name lines, and Arabic excluded), case-flexible, against the attestation lexicon of the control (`work/lexicon-nt.tsv`, 13,266 forms from 361,803 tokens of Zimmer's NT):

- **Post-corrections: 82.49%** of tokens attested in the control's vocabulary (124,947 / 151,475). Pre-corrections figure was 79.35% on the wider (apparatus-including) count.
- The figure is a floor, and the record says why: the lexicon was machine-tokenised from a pdftotext extraction and splits some of Zimmer's words at line-break artefacts, so forms verified present in the control by direct search — *wisse*, *gudd*, *Nòricht*, *Goddes* — nonetheless score as unattested in the token count. Attestation settles the existence of forms, not the fluency of the whole; the independent checker's sample grades carry that judgement.
- Largest remaining unattested classes, all disclosed: attested minority forms of the control itself (*dir*, *uns*); pattern forms built on Zimmer's own visible patterns (*geglaabt*, *Herze*, *Fraue*, *Gärde*, *werrde*, the locked *Gerechtichkät*); and the lengthened *wääß* for "knows" (Zimmer's ää-lengthening pattern applied to the wisse stem; his own 3rd-person form does not occur in the NT text).

## GAP seats

**363 bracketed seats** stand in the text, each held open rather than invented, each carried in the consolidated flag record (FLAGS-PF.md). The most frequent: [Partner] (partners ascribed to God), [Karawane], [Wüste-Araber], [Quran] (chunk-05 name-form brackets — see the checker report for the un-bracketing corrections), [pilgrim sanctity], [Zauberer], [Wächter], [polytheists], [swear]. The independent checker audited the bracket population for resolvability; its findings and the corrections taken from them are in CHECKER-REPORT-PF-2026-11-23.md and CORRECTIONS-PF-2026-11-23.md.

---

## Addendum — post-corrections, 2026-11-23

After the independent checker's 24 required corrections were applied (CORRECTIONS-PF-2026-11-23.md; 2,003 replacements), the battery was re-run on the final manuscript: **ALL PASS** — verse sequence identical to the master (6,236/6,236), per-surah 114/114, Arabic 6,348 lines sequence byte-identical, Basmalah 112/112 italic heads with 114 locked-line occurrences, sajda 15/15, no % / Prozent, naming check clean. Attestation recomputed: **83.63%** (126,681 / 151,472 tokens, same floor caveat). GAP seats standing: **311** by token count (309 by the battery's line count; the difference is apparatus brackets), all true gaps or disclosed devices. Final manuscript: 2,291,240 bytes, SHA-256 `6b3a57a7c44235476ff04a772ac58e445eeb49c104ee57f71bc94d8228ff00cb`.
