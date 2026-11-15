# MANIFEST — Classical Chinese Quran Pilot Specimen Encoded in DNA Letters (in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, on the rails of the Quran DNA and Bible DNA
lanes completed earlier the same day. The codec is the house codec demonstrated
on the Bismillah and used for the full Quran and the full Clear English Bible.

## PILOT SPECIMEN — READ THIS FACE FIRST

This deposit encodes a **PILOT specimen of an unsettled draft**, not a book
and not a finished translation. The source file is the Classical Chinese
(文言) pilot of Robert Tilford's Quran lane: Surah 1 (Al-Fatiha) and Surah 112
(Al-Ikhlas) only, rendered from the Locked English Master of record as a
style test. The lane's **divine-"We" rendering decision is still open with
Robert** (the master text's capital "We / Us / Our" seats and their
Classical Chinese rendering have not been ruled), and the pilot itself
carries marked lines on its face, including the disclosed sense-narrowing
at 112:2 (al-ṣamad rendered 至恆, the eternity facet; the refuge facet
unexpressed). The pilot's publication gate — a qualified classical-Chinese
/ sinologist reviewer — is unmet. Encoding this specimen preserves it
exactly as it stands today; it settles nothing, reviews nothing, and
publishes nothing beyond this shelf deposit.

The pilot file also carries, inside itself, the **Arabic lines** of Surah 1
and Surah 112 (with the Basmalah), extracted by code from the corrected
English master of record (MD5 `064ee170806bb31f5bac3e75d2aa4d94`, the
post-6:86-correction master) and byte-identical to it, alongside the
master's English wording for each verse. Those Arabic lines are encoded
here as part of the pilot file's bytes, exactly where they stand in it.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete text of the
pilot file of record below, written in the four DNA letters A, C, G, T under
the codec stated below. It is an **encoding, not a translation**: no wording
was translated, modernized, or altered in any way by this lane — the pilot
file's bytes were converted, exactly as they stand, and decoding returns
them exactly. **Nothing has been synthesized. No physical DNA exists.**
Physical synthesis is a separate future step that would require funding
and a laboratory; no funding is in place and no physical DNA has been made,
and synthesis is not part of this deposit. No claim of priority or
firstness is made anywhere in this deposit: what is claimed is only what
the verification figures below prove.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base stream
returns the byte stream exactly, which the separate decoder's report in
this deposit proves by hash.

## Source of record

- Source file: `PILOT-CLASSICAL-CHINESE.md` in Robert Tilford's Classical
  Chinese Quran lane folder (`ayah-classical-chinese/`): the pilot specimen
  of Surah 1 and Surah 112, with its front matter, its Arabic lines, the
  master's English wording, and its marked-lines section, encoded entire
  and exactly as it stands.
- The file was encoded **by code, byte for byte, never retyped**.
- Source file size: **4,489 bytes**
- SHA-256 of the source byte stream: `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`
- Base stream: **17,956 bases** (4 per byte)
- SHA-256 of the base stream: `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841`

## Structure of the encoded stream

The stream follows the pilot file's own structure, parsed by code and
verified as it was parsed: the front matter, then the Surah 1 section, the
Surah 112 section, and the marked-lines section. The segments tile the
stream exactly, with no gaps and no overlaps.

| Section | Source bytes | Bases | Base range |
|---|---|---|---|
| Front matter of the pilot (title, status, source note) | 759 | 3,036 | 1–3,036 |
| 第一章 開端章 (Surah 1 · Al-Fatihah · Meccan · 7 verses) | 1,412 | 5,648 | 3,037–8,684 |
| 第一一二章 忠誠章 (Surah 112 · Al-Ikhlas · Meccan · 4 verses) | 848 | 3,392 | 8,685–12,076 |
| Marked lines (flags carried on the face of the pilot) | 1,470 | 5,880 | 12,077–17,956 |

## Files in this deposit

- `classical-chinese-pilot-dna.txt` — the full base stream, wrapped at 60
  bases per line.
- `MANIFEST-DNA-CLASSICAL-CHINESE-PILOT.md` — this manifest.
- `encode_lzh_pilot_dna.py` — the encoder (structure parse + encoding).
- `validate_lzh_pilot_dna.py` — the hygiene validator (report-only).
- `decode_lzh_pilot_dna.py` — the separate decoder, written and run by a
  separate agent.
- `INDEPENDENT-DECODER-REPORT.md` — the separate decoder's verdict.
- `CLASSICAL-CHINESE-PILOT-DNA-PRINT.pdf` — the paper book typeset from the
  verified sequence file: **8 pages**, **17,908 bytes**,
  SHA-256 `d5361b642daf7bea2cbc206551e37cee421e65a7ca41c45a9b964d1fe9f8476c` (its printed base stream was re-verified equal
  to `classical-chinese-pilot-dna.txt` IN FULL by extraction of every
  printed page, and three 200-base slices of the extracted stream decode
  back to the source bytes at the corresponding offsets — see the lane's
  PDF verification record).

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 4,575 · C 5,165 · G 5,207 · T 3,009
- GC content: 57.7634%
- Homopolymer runs: 14,465 in total; longest run **6**;
  runs of length ≥ 4: 19 · ≥ 5: 8 · ≥ 6: 1 · ≥ 8: 0 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.

## Separate verification

A separate agent wrote a separate decoder from the specification alone — no encoder or validator code read or shared — and ran it end to end. **VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source file and hash to `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`, the source figure printed above; the base stream hashes to `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841`, also as printed above. Its spot proofs re-encoded the first, middle, and last 1,000 source bytes with its own logic and matched the sequence exactly at each place (17,956 bases in total; 4,489 bytes decoded). Its report, `INDEPENDENT-DECODER-REPORT.md`, is included in this deposit. The printed book's stream was additionally re-verified in full: every Courier span extracted from every page of the PDF, concatenated in order, equals `classical-chinese-pilot-dna.txt` exactly, and three 200-base slices of the extracted stream (start, midpoint, end) decode back to the source bytes at the corresponding offsets.
