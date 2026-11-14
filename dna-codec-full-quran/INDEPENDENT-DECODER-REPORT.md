# Independent Decoder Report — Quran DNA (full text)

Date: 2026-11-14
Decoder: independent decoder for Robert Tilford's Quran DNA lane
Script: `decode_quran_dna.py` in this deposit, written from scratch from the specification alone. The encoder's and validator's code (`work/encode_quran_dna.py` and `validate_dna.py`) was not read, imported, or copied.

## Source of record — MD5 verification

- Master: `~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md`
- MD5 computed by this decoder: `064ee170806bb31f5bac3e75d2aa4d94`
- Expected MD5: `064ee170806bb31f5bac3e75d2aa4d94`
- Outcome: MATCH — the master's MD5 is `064ee170806bb31f5bac3e75d2aa4d94`, verified before extraction.

## Codec used

Each base is two bits — A=00, C=01, G=10, T=11. Four bases make one byte, most significant pair first. The byte stream is UTF-8 text. Decoding and the spot-proof re-encoding were both implemented independently in the decoder script.

## Extraction performed independently

The source stream was extracted by this decoder, by structural position, from Part I (the text between the "# Part I · The Translation" heading and the "# Part II · Concordance" heading), in order, over the 114 surah sections headed "## N. <title>". For each surah: (1) the surah-header Arabic name between the bold markers on the `**<Arabic name>** · <transliteration> · ...` title line; (2) the basmalah frame, where present — a non-empty preamble line before the first verse line (`**s:v**`) that does not start with "*" and contains Arabic-script characters; (3) for every verse block, the last line of the block that is non-empty, is not a "---" separator, and is not a bracketed marker line of the form `*[...]*`. The runs were concatenated with no separators and encoded as UTF-8.

## Figures computed

- Total bases in `quran-dna-full.txt` (all whitespace stripped): 5,423,660
- Bases use only A/C/G/T: yes
- Total bases divisible by 4: yes (5,423,660 / 4 = 1,355,915)
- Decoded bytes: 1,355,915
- Independently extracted source stream bytes: 1,355,915
- Total runs extracted: 6,462
- Surah-name runs: 114
- Basmalah frame runs: 112
- Verse runs: 6,236
- SHA-256 of the decoded byte stream: `fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`
- SHA-256 of the independently extracted source stream bytes: `fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`
- SHA-256 of the base stream (stripped sequence as ASCII): `d92efa7682d2047068d45804716978bc1667c98e38f6693c9f1f3b69eb658c10`
- SHA-256 printed in `MANIFEST-DNA-FULL.md` for the Arabic byte stream: `fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`
- SHA-256 printed in `MANIFEST-DNA-FULL.md` for the base stream: `d92efa7682d2047068d45804716978bc1667c98e38f6693c9f1f3b69eb658c10`

## Checks

a. Run counts — PASS. Verse runs counted separately are 6,236, and total runs are 6,462 = 114 names + 112 frames + 6,236 verses. Surahs 1 and 9 carry no frame under the structural detection; the other 112 do.

b. Full decode and UTF-8 — PASS. The full 5,423,660-base sequence decoded to 1,355,915 bytes, and those bytes decoded as UTF-8 with no error.

c. Decoded bytes vs. independently extracted source stream — PASS. The SHA-256 of the decoded bytes (`fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`) equals the SHA-256 of the independently extracted source stream bytes (same value), and the two byte streams are equal byte-for-byte.

d. Manifest figures — PASS, both. The SHA-256 of the base stream computed here (`d92efa7682d2047068d45804716978bc1667c98e38f6693c9f1f3b69eb658c10`) matches the figure printed in `MANIFEST-DNA-FULL.md`, and the SHA-256 of the decoded byte stream computed here (`fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`) matches the Arabic byte stream figure printed in `MANIFEST-DNA-FULL.md`.

e. Per-surah spot proof — PASS for all three surahs. Each surah's extracted runs were re-encoded with this decoder's own encoder logic, with base offsets tracked cumulatively through the whole sequence, and the corresponding slice of the sequence file matched exactly:

- Surah 1: base range 1–2280 (1-based), 2,280 bases, 570 bytes — exact match.
- Surah 57: base range 4831949–4873424 (1-based), 41,476 bases, 10,369 bytes — exact match.
- Surah 114: base range 5422097–5423660 (1-based), 1,564 bases, 391 bytes — exact match.

The cumulatively tracked final base offset is 5,423,660, equal to the total bases in the sequence file.

## Verdict

Every check passes: master MD5, run counts, UTF-8 decode, byte-for-byte and hash equality with the independently extracted source stream, both manifest SHA-256 figures, and the three per-surah spot proofs.

VERDICT: PASS
