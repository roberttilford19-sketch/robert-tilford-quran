#!/usr/bin/env python3
"""
Independent decoder for the Classical Chinese pilot DNA lane.
Written from the written specification alone (2026-11-14).

Codec from spec:
  A=00, C=01, G=10, T=11
  Four bases make one byte, most significant pair first.
  Sequence file is wrapped at 60 bases per line; strip all whitespace.
Usage:
  python3 decode_lzh_pilot_dna.py [source_path]
  source_path defaults to ~/workspace/ayah-classical-chinese/PILOT-CLASSICAL-CHINESE.md
"""

import hashlib
import re
import sys
from pathlib import Path

HOME = Path.home()
SEQ_PATH = HOME / "workspace" / "dna-classical-chinese-pilot-2026-11-14" / "classical-chinese-pilot-dna.txt"
MANIFEST_PATH = HOME / "workspace" / "dna-classical-chinese-pilot-2026-11-14" / "MANIFEST-DNA-CLASSICAL-CHINESE-PILOT.md"
DEFAULT_SOURCE_PATH = HOME / "workspace" / "ayah-classical-chinese" / "PILOT-CLASSICAL-CHINESE.md"
EXPECTED_BASE_COUNT = 17956

# --- Decoder (written from spec) ---
PAIR_VALUE = {"A": 0, "C": 1, "G": 2, "T": 3}


def decode_bases(bases: str) -> bytes:
    """Convert a string of A/C/G/T bases to bytes, 4 bases per byte, MSB pair first."""
    if len(bases) % 4 != 0:
        raise ValueError(f"base count {len(bases)} is not divisible by 4")
    out = bytearray()
    for i in range(0, len(bases), 4):
        chunk = bases[i : i + 4]
        try:
            v0 = PAIR_VALUE[chunk[0]]
            v1 = PAIR_VALUE[chunk[1]]
            v2 = PAIR_VALUE[chunk[2]]
            v3 = PAIR_VALUE[chunk[3]]
        except KeyError as exc:
            raise ValueError(f"invalid base {exc} at position {i}") from exc
        out.append((v0 << 6) | (v1 << 4) | (v2 << 2) | v3)
    return bytes(out)


# --- Re-encoder (separately written, for spot proofs only) ---
ORDERED_BASES = "ACGT"


def encode_bytes(data: bytes) -> str:
    """Convert bytes back to bases by extracting 2-bit fields, high to low."""
    pieces = []
    for byte in data:
        for shift in (6, 4, 2, 0):
            pair = (byte >> shift) & 0b11
            pieces.append(ORDERED_BASES[pair])
    return "".join(pieces)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_manifest(path: Path):
    text = path.read_text(encoding="utf-8")
    m_src = re.search(r"SHA-256 of the source byte stream:\s*`([0-9a-fA-F]{64})`", text)
    m_base = re.search(r"SHA-256 of the base stream:\s*`([0-9a-fA-F]{64})`", text)
    if not m_src or not m_base:
        raise ValueError("could not parse both SHA-256 figures from manifest")
    return m_src.group(1).lower(), m_base.group(1).lower()


def spot_proof(label: str, source: bytes, bases: str, byte_start: int, byte_end: int) -> bool:
    segment = source[byte_start:byte_end]
    reencoded = encode_bytes(segment)
    expected_slice = bases[byte_start * 4 : byte_end * 4]
    ok = reencoded == expected_slice
    print(
        f"spot[{label}]: source bytes {byte_start}..{byte_end - 1} "
        f"({len(segment)} bytes), bases {byte_start * 4}..{byte_end * 4 - 1} "
        f"({len(expected_slice)} bases), match={ok}"
    )
    return ok


def main(argv) -> int:
    source_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_SOURCE_PATH

    raw_seq_text = SEQ_PATH.read_text(encoding="utf-8")
    # Strip all whitespace per spec
    bases = "".join(raw_seq_text.split())

    source_bytes = source_path.read_bytes()
    manifest_source_sha, manifest_base_sha = parse_manifest(MANIFEST_PATH)

    # (a) base count, alphabet, divisibility
    alphabet = set(bases)
    count_ok = len(bases) == EXPECTED_BASE_COUNT
    alphabet_ok = alphabet == {"A", "C", "G", "T"}
    divisible_ok = (len(bases) % 4 == 0)
    check_a = count_ok and alphabet_ok and divisible_ok
    print(f"(a) base_count={len(bases)} expected={EXPECTED_BASE_COUNT} count_ok={count_ok}")
    print(f"    alphabet={sorted(alphabet)} alphabet_ok={alphabet_ok} divisible_by_4={divisible_ok}")
    print(f"    check_a={'PASS' if check_a else 'FAIL'}")

    # Decode
    decoded = decode_bases(bases)
    print(f"decoded_bytes={len(decoded)} source_bytes={len(source_bytes)}")

    # (b) valid UTF-8
    try:
        decoded.decode("utf-8")
        utf8_ok = True
    except UnicodeDecodeError as exc:
        utf8_ok = False
        print(f"    UTF-8 error: {exc}")
    print(f"(b) valid_utf8={utf8_ok} check_b={'PASS' if utf8_ok else 'FAIL'}")

    # (c) byte equality + SHA-256
    source_sha = sha256_hex(source_bytes)
    decoded_sha = sha256_hex(decoded)
    equal_ok = decoded == source_bytes
    sha_ok = decoded_sha == source_sha
    check_c = equal_ok and sha_ok
    print(f"(c) bytes_equal={equal_ok} source_sha256={source_sha}")
    print(f"    decoded_sha256={decoded_sha} sha_match={sha_ok}")
    print(f"    check_c={'PASS' if check_c else 'FAIL'}")

    # (d) manifest figures
    # Base stream hash: hash of the stripped base stream as bytes (ASCII)
    base_sha = sha256_hex(bases.encode("ascii"))
    manifest_source_match = manifest_source_sha == source_sha
    manifest_base_match = manifest_base_sha == base_sha
    check_d = manifest_source_match and manifest_base_match
    print(f"(d) manifest_source_sha256={manifest_source_sha} match_computed_source={manifest_source_match}")
    print(f"    manifest_base_sha256={manifest_base_sha}")
    print(f"    computed_base_sha256={base_sha} match={manifest_base_match}")
    print(f"    check_d={'PASS' if check_d else 'FAIL'}")

    # (e) spot proofs: first, middle (centered on midpoint), last 1000 source bytes
    n = len(source_bytes)
    mid = n // 2
    first_ok = spot_proof("first", source_bytes, bases, 0, 1000)
    middle_ok = spot_proof("middle", source_bytes, bases, mid - 500, mid + 500)
    last_ok = spot_proof("last", source_bytes, bases, n - 1000, n)
    check_e = first_ok and middle_ok and last_ok
    print(f"(e) first={first_ok} middle={middle_ok} last={last_ok} check_e={'PASS' if check_e else 'FAIL'}")

    all_ok = check_a and utf8_ok and check_c and check_d and check_e
    print(f"VERDICT: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
