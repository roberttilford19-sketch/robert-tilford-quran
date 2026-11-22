# PACK MANIFEST — Lakota Completion Wave Landing Pack

Assembled 2026-11-22 by the Concordance Rebuilder (Lakota Completion Wave).
This pack is assembled for the desk to settle the landing later; no lane file
outside `wave/` was modified, and nothing in this pack has been published or
sent anywhere.

## Contents

1. **ayah-companion-manuscript-LKT.md** — the manuscript, unchanged.
   Byte-identical copy of `../ayah-companion-manuscript-LKT.md`;
   MD5 d5467e986832cc110b7dcbbae38024af (verified against the value of record
   d5467e986832cc110b7dcbbae38024af).
2. **GLOSSARY-LKT.md** — the glossary, unchanged. Byte-identical copy of
   `../GLOSSARY-LKT.md` (MD5 c1d4bde10a761ad2c3e804d6737f40d1).
3. **concordance-full-wave.json** — the merged concordance (new). Built from
   `../concordance-full-lkt.json` by applying, in order: (1) the 134 published
   receipts of 2026-11-18 (`../receipts-2026-11-18-lkt.json`, source keys
   expanded to full citations from that file's `sources` table), receipt class
   "published citation — 2026-11-18 receipt pass"; then (2) the wave's 1,240
   receipts (`wave/receipts-wave-final.json`), receipt class "published
   citation — 2026-11-22 completion wave". Each applied receipt was verified
   against the concordance entry's occurrence count; mismatches found:
   0. Forms still without receipts keep `receipt = null` and
   carry `wave_examined = true` (all 5323 of them appear in
   `wave/unreceipted-final.json`).
4. **gaps-register.json** — the gaps register (new). Every form still
   unreceipted, as {form, occ, reason}. Reasons are taken from
   `wave/notreceipted-band-*.json`, overridden by `wave/notreceipted-sweep.json`
   where a form appears in both (a form's last examination governs;
   484 sweep reasons applied).
5. **PACK-MANIFEST.md** — this file.

## Flags note

FLAGS-LKT.md is unchanged. Its adjudication stands as the dated layer
FLAGS-ADJUDICATION-2026-11-22.md.

## Final counts (computed from the merged concordance entries)

- Distinct forms: 7011
- Total tokens: 114365
- Receipted forms (all classes): 1688
- Published-citation receipted forms: 1374
- Unreceipted forms (examined-and-unattested, disclosed gaps): 5323

Receipt-class counts:

- fixed renderings (normalization): 5
- key terms, leading forms (§4): 50
- locked (§§1-2): 10
- proper names (§3): 35
- published citation — 2026-11-18 receipt pass: 134
- published citation — 2026-11-22 completion wave: 1240
- recorded variants (§4 / normalization): 38
- surah titles (§5): 176
