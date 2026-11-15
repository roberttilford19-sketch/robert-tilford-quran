# Independent Decoder Report — Classical Chinese Pilot DNA

Date: 2026-11-14

This decoder script (`decode_lzh_pilot_dna.py`) was written from the specification alone. The following files were not read, imported, or copied: `encode_lzh_pilot_dna.py`, `validate_lzh_pilot_dna.py`, and anything under `~/workspace/dna-classical-chinese-pilot-2026-11-14/work/`.

## Codec

Each base is two bits: A=00, C=01, G=10, T=11. Four bases make one byte, most significant pair first. The sequence file is wrapped at 60 bases per line; all whitespace was stripped before decoding. A separately written re-encoder in the same script (extracting 2-bit fields from each byte, high to low, through the ordered bases ACGT) was used only for the spot proofs in check (e).

## Source of record

- Source file: `~/workspace/ayah-classical-chinese/PILOT-CLASSICAL-CHINESE.md`
- Sequence file: `~/workspace/dna-classical-chinese-pilot-2026-11-14/classical-chinese-pilot-dna.txt`
- Manifest file: `~/workspace/dna-classical-chinese-pilot-2026-11-14/MANIFEST-DNA-CLASSICAL-CHINESE-PILOT.md`
- Decoder script: `~/workspace/dna-classical-chinese-pilot-2026-11-14/decode_lzh_pilot_dna.py` (accepts the source path as an optional argv[1], defaulting to the source path above)

## Figures computed

- Total bases (after stripping all whitespace): 17,956
- Expected base count: 17,956
- Alphabet observed: {A, C, G, T}
- Decoded bytes: 4,489
- Source bytes: 4,489
- SHA-256 of the source byte stream (computed): `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`
- SHA-256 of the decoded byte stream (computed): `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`
- SHA-256 of the base stream (computed, over the stripped base stream as ASCII bytes): `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841`
- SHA-256 of the source byte stream (from manifest): `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`
- SHA-256 of the base stream (from manifest): `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841`

## Checks

- (a) Base count, alphabet, and divisibility — PASS: base count is 17,956, equal to the expected 17,956; alphabet is exactly {A, C, G, T}; 17,956 is divisible by 4 (17,956 / 4 = 4,489).
- (b) Full decode is valid UTF-8 — PASS: the 4,489 decoded bytes decode as UTF-8 with no error.
- (c) Decoded bytes equal the source byte-for-byte, with matching SHA-256 — PASS: decoded bytes are 4,489 and source bytes are 4,489, byte-for-byte equal; SHA-256 of the source is `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61` and SHA-256 of the decoded bytes is `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61`, identical.
- (d) Both manifest SHA-256 figures match the computed values — PASS: manifest source figure `a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61` matches the computed source SHA-256, and manifest base-stream figure `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841` matches the computed base-stream SHA-256 `4cd1d212f04c08431e5a2aa055e054373ee9fd588396d90ecf2da0ac50943841`.
- (e) Spot proofs by independent re-encoding — PASS: first 1,000 source bytes (source bytes 0–999, bases 0–3999, 4,000 bases) re-encode exactly to the corresponding sequence slice; middle 1,000 source bytes centred on the file midpoint 2,244 (source bytes 1744–2743, bases 6976–10975, 4,000 bases) re-encode exactly to the corresponding sequence slice; last 1,000 source bytes (source bytes 3489–4488, bases 13956–17955, 4,000 bases) re-encode exactly to the corresponding sequence slice. All three slices matched.

## Verdict

All checks (a)–(e) passed. The base stream in `classical-chinese-pilot-dna.txt` decodes, under the codec stated above, to exactly the bytes of `PILOT-CLASSICAL-CHINESE.md`, and both manifest SHA-256 figures match the values computed independently by this decoder.

VERDICT: PASS
