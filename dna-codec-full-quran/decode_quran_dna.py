#!/usr/bin/env python3
"""
Independent decoder for the Quran DNA lane (2026-11-14).

Written from scratch from the specification alone. It does NOT import,
read, or copy the encoder's or validator's code.

Codec: A=00, C=01, G=10, T=11. Four bases make one byte,
most significant pair first. The byte stream is UTF-8 text.

Source stream: the master's Arabic run sequence for Part I,
extracted by structural position (see extract_source_runs).
"""

import hashlib
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SEQ_PATH = BASE_DIR / "quran-dna-full.txt"
MANIFEST_PATH = BASE_DIR / "MANIFEST-DNA-FULL.md"
MASTER_PATH = Path.home() / "workspace" / "ayah-audit" / "corrected" / "ayah-companion-manuscript.md"

EXPECTED_MASTER_MD5 = "064ee170806bb31f5bac3e75d2aa4d94"

BASE_TO_BITS = {"A": 0, "C": 1, "G": 2, "T": 3}
BITS_TO_BASE = {0: "A", 1: "C", 2: "G", 3: "T"}

VERSE_LINE_RE = re.compile(r"^\*\*\d+:\d+\*\*")
SURAH_HEAD_RE = re.compile(r"^## (\d+)\.\s")
TITLE_LINE_RE = re.compile(r"^\*\*(.+?)\*\* · ")
MARKER_LINE_RE = re.compile(r"^\*\[.*\]\*$")


def contains_arabic(text):
    """True if text contains any Arabic-script character."""
    for ch in text:
        o = ord(ch)
        if (
            0x0600 <= o <= 0x06FF
            or 0x0750 <= o <= 0x077F
            or 0x08A0 <= o <= 0x08FF
            or 0xFB50 <= o <= 0xFDFF
            or 0xFE70 <= o <= 0xFEFF
        ):
            return True
    return False


def decode_bases(bases):
    """Decode a string of A/C/G/T bases to bytes. 4 bases -> 1 byte, MSB pair first."""
    if len(bases) % 4 != 0:
        raise ValueError(f"base count {len(bases)} is not divisible by 4")
    out = bytearray()
    for i in range(0, len(bases), 4):
        byte = 0
        for j in range(4):
            ch = bases[i + j]
            if ch not in BASE_TO_BITS:
                raise ValueError(f"invalid base {ch!r} at position {i + j}")
            byte = (byte << 2) | BASE_TO_BITS[ch]
        out.append(byte)
    return bytes(out)


def encode_bytes(data):
    """Encode bytes to bases with my own encoder logic (for spot proof)."""
    parts = []
    for byte in data:
        parts.append(BITS_TO_BASE[(byte >> 6) & 0b11])
        parts.append(BITS_TO_BASE[(byte >> 4) & 0b11])
        parts.append(BITS_TO_BASE[(byte >> 2) & 0b11])
        parts.append(BITS_TO_BASE[byte & 0b11])
    return "".join(parts)


def extract_source_runs(master_text):
    """
    Extract runs by structural position from Part I.

    Returns (runs, per_surah) where runs is a flat list of strings in order,
    and per_surah is a list of dicts with surah number, name run, frame run
    (or None), and verse runs.
    """
    lines = master_text.splitlines()

    # Locate Part I by its exact top-level heading, and Part II after it.
    try:
        part1_idx = lines.index("# Part I · The Translation")
    except ValueError:
        raise ValueError("Part I heading not found")
    try:
        part2_idx = lines.index("# Part II · Concordance", part1_idx)
    except ValueError:
        raise ValueError("Part II heading not found after Part I")
    part = lines[part1_idx:part2_idx]

    # Surah sections headed "## N. <title>"
    head_positions = []
    for idx, line in enumerate(part):
        m = SURAH_HEAD_RE.match(line)
        if m:
            head_positions.append((idx, int(m.group(1))))
    if [n for _, n in head_positions] != list(range(1, 115)):
        raise ValueError(f"surah headings are not 1..114 in order: {[n for _, n in head_positions]}")

    all_runs = []
    per_surah = []

    for si, (h_idx, surah_no) in enumerate(head_positions):
        sec_end = head_positions[si + 1][0] if si + 1 < len(head_positions) else len(part)
        section = part[h_idx:sec_end]

        # 1. Surah-header Arabic name: first title line **<name>** · ...
        name = None
        for line in section:
            m = TITLE_LINE_RE.match(line)
            if m:
                name = m.group(1)
                break
        if name is None:
            raise ValueError(f"surah {surah_no}: title line not found")

        # First verse line position within the section
        first_verse_idx = None
        for idx, line in enumerate(section):
            if VERSE_LINE_RE.match(line):
                first_verse_idx = idx
                break
        if first_verse_idx is None:
            raise ValueError(f"surah {surah_no}: no verse lines found")
        preamble = section[:first_verse_idx]

        # 2. Basmalah frame: a non-empty preamble line, before the first
        #    verse line, that does not start with "*" and contains Arabic.
        frame = None
        frame_candidates = []
        for line in preamble:
            if line.strip() == "":
                continue
            if line.lstrip().startswith("*"):
                continue
            if contains_arabic(line):
                frame_candidates.append(line)
        if frame_candidates:
            if len(frame_candidates) != 1:
                raise ValueError(
                    f"surah {surah_no}: expected at most 1 frame candidate, got {len(frame_candidates)}"
                )
            frame = frame_candidates[0]

        # 3. Verse blocks: from each "**s:v**" line to the next verse line
        #    or the section end. Verse Arabic = last line of the block that
        #    is non-empty, is not "---", and is not a *[...]* marker line.
        verse_starts = [idx for idx, line in enumerate(section) if VERSE_LINE_RE.match(line)]
        verse_runs = []
        for vi, v_idx in enumerate(verse_starts):
            block_end = verse_starts[vi + 1] if vi + 1 < len(verse_starts) else len(section)
            block = section[v_idx:block_end]
            arabic = None
            for line in reversed(block):
                stripped = line.strip()
                if stripped == "":
                    continue
                if stripped == "---":
                    continue
                if MARKER_LINE_RE.match(stripped):
                    continue
                arabic = line
                break
            if arabic is None:
                raise ValueError(f"surah {surah_no}: verse block at section offset {v_idx} has no Arabic line")
            verse_runs.append(arabic)

        surah_runs = [name]
        if frame is not None:
            surah_runs.append(frame)
        surah_runs.extend(verse_runs)

        per_surah.append(
            {
                "surah": surah_no,
                "name": name,
                "frame": frame,
                "verses": verse_runs,
                "runs": surah_runs,
            }
        )
        all_runs.extend(surah_runs)

    return all_runs, per_surah


def parse_manifest_hashes(manifest_text):
    arabic = None
    base = None
    m = re.search(r"SHA-256 of the Arabic byte stream:\s*`([0-9a-fA-F]{64})`", manifest_text)
    if m:
        arabic = m.group(1).lower()
    m = re.search(r"SHA-256 of the base stream:\s*`([0-9a-fA-F]{64})`", manifest_text)
    if m:
        base = m.group(1).lower()
    return arabic, base


def main():
    # Master MD5
    master_bytes = MASTER_PATH.read_bytes()
    master_md5 = hashlib.md5(master_bytes).hexdigest()
    print(f"master_md5={master_md5}")
    print(f"master_md5_expected={EXPECTED_MASTER_MD5}")
    print(f"master_md5_match={master_md5 == EXPECTED_MASTER_MD5}")

    # Sequence
    seq_raw = SEQ_PATH.read_text(encoding="ascii")
    bases = "".join(seq_raw.split())
    print(f"total_bases={len(bases)}")
    print(f"bases_alphabet_ok={set(bases) <= set('ACGT')}")

    # Decode
    decoded = decode_bases(bases)
    print(f"decoded_bytes={len(decoded)}")
    try:
        decoded_text = decoded.decode("utf-8")
        print("utf8_decode_ok=True")
    except UnicodeDecodeError as e:
        print(f"utf8_decode_ok=False error={e}")
        decoded_text = None

    # Source extraction
    master_text = master_bytes.decode("utf-8")
    runs, per_surah = extract_source_runs(master_text)
    verse_count = sum(len(s["verses"]) for s in per_surah)
    frame_count = sum(1 for s in per_surah if s["frame"] is not None)
    name_count = len(per_surah)
    print(f"total_runs={len(runs)}")
    print(f"name_runs={name_count}")
    print(f"frame_runs={frame_count}")
    print(f"verse_runs={verse_count}")

    source_bytes = "".join(runs).encode("utf-8")
    print(f"source_bytes={len(source_bytes)}")

    # Hashes
    sha_decoded = hashlib.sha256(decoded).hexdigest()
    sha_source = hashlib.sha256(source_bytes).hexdigest()
    sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
    print(f"sha256_decoded={sha_decoded}")
    print(f"sha256_source={sha_source}")
    print(f"sha256_bases={sha_bases}")
    print(f"decoded_equals_source_bytes={decoded == source_bytes}")
    print(f"sha_decoded_equals_source={sha_decoded == sha_source}")

    # Manifest comparison
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")
    man_arabic, man_base = parse_manifest_hashes(manifest_text)
    print(f"manifest_sha256_arabic={man_arabic}")
    print(f"manifest_sha256_base={man_base}")
    print(f"manifest_arabic_match={sha_decoded == man_arabic}")
    print(f"manifest_base_match={sha_bases == man_base}")

    # Per-surah spot proof for 1, 57, 114: re-encode and compare slice,
    # tracking base offsets as we go.
    offset = 0  # in bases, 0-based
    spot = {}
    for entry in per_surah:
        surah_bytes = "".join(entry["runs"]).encode("utf-8")
        surah_bases = encode_bytes(surah_bytes)
        start = offset
        end = offset + len(surah_bases)  # exclusive
        if entry["surah"] in (1, 57, 114):
            slice_ok = bases[start:end] == surah_bases
            spot[entry["surah"]] = (start, end, len(surah_bases), len(surah_bytes), slice_ok)
            print(
                f"spot_surah_{entry['surah']}: base_range_1based={start + 1}-{end} "
                f"bases={len(surah_bases)} bytes={len(surah_bytes)} match={slice_ok}"
            )
        offset = end
    print(f"final_offset_bases={offset}")
    print(f"offset_equals_total_bases={offset == len(bases)}")

    # Verdict assembled by caller / report; print summary flags
    checks = {
        "master_md5": master_md5 == EXPECTED_MASTER_MD5,
        "run_counts": (len(runs) == 6462 and verse_count == 6236 and name_count == 114 and frame_count == 112),
        "utf8": decoded_text is not None,
        "byte_equality": decoded == source_bytes,
        "manifest_arabic": sha_decoded == man_arabic,
        "manifest_base": sha_bases == man_base,
        "spot": all(v[4] for v in spot.values()) and len(spot) == 3,
    }
    for k, v in checks.items():
        print(f"check_{k}={v}")
    print("VERDICT: " + ("PASS" if all(checks.values()) else "FAIL"))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
