# PACK MANIFEST — Navajo Completion Wave Landing Pack

Assembled 2026-11-24. This pack is assembled for the desk to settle the landing;
no lane file outside `wave/` was modified by the wave, and the manuscript's text
was not edited: MD5 408b7bb97269c65ce2e85d39dc886e6a, identical before and after.

## Contents

1. **ayah-companion-manuscript-NV.md** — the manuscript, unchanged.
   Byte-identical copy of `../ayah-companion-manuscript-NV.md`
   (MD5 408b7bb97269c65ce2e85d39dc886e6a).
2. **GLOSSARY-NV.md** — the glossary, unchanged. Byte-identical copy of
   `../GLOSSARY-NV.md`.
3. **concordance-full-wave-nv.json** — the merged concordance (new). Built from
   `../concordance-full-nv.json` by applying the wave's 495 published-citation
   receipts (`wave/receipts-wave-nv.json`), receipt class "published citation —
   2026-11-24 completion wave". Each applied receipt was verified against the
   concordance entry's occurrence count; mismatches found: 0. Forms still
   without receipts keep `receipt = null` and carry `wave_examined = true`
   (all 9,757 of them appear in `wave/notreceipted-wave-nv.json`).
4. **gaps-register-nv.json** — the gaps register (new). Every form still
   unreceipted, as {form, occ, reason}: 3,826 forms are Arabic transliterations
   or proper names, outside the Navajo dictionary record by design; 5,931
   carry "no attestation found in the openly published record searched
   (Wiktionary/Kaikki Navajo; Young & Morgan 1943)".
5. **PACK-MANIFEST.md** — this file.

## Flags note

FLAGS-NV.md is unchanged. Its adjudication stands as the dated layer
FLAGS-ADJUDICATION-2026-11-24-NV.md in the lane folder (4,459 bullets:
1,155 settled on attestation, 2,485 partly settled, 814 confirmed ungrounded,
5 with no checkable form).

## Final counts (computed from the merged concordance entries)

- Distinct forms: 10,443
- Total tokens: 64,894
- Receipted forms (all classes): 686
- Published-citation receipted forms: 495
- Unreceipted forms (examined, disclosed gaps): 9,757
- Receipted occurrences: 41,747 of 64,894 (64.3%)

Receipt classes:

- lane records (locked terminology, proper names, fixed renderings — from
  WORKER-BRIEF-NV.md and GLOSSARY-NV.md): 191 forms
- published citation — 2026-11-24 completion wave: 495 forms
  (Basis A: 342 — the form stands in a published entry, Wiktionary/Kaikki or
  Young & Morgan 1943; Basis B: 153 — a regular derivation of an attested form,
  rule named in each receipt)
