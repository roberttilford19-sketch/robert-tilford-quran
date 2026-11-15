#!/usr/bin/env python3
"""ENCODER — Classical Chinese pilot DNA lane (2026-11-14).
Encodes the Classical Chinese Quran PILOT specimen file (Surah 1 +
Surah 112) EXACTLY as it stands, byte for byte, with the house codec
(UTF-8 bytes -> bits MSB-first -> 00=A 01=C 10=G 11=T). No extraction,
no retyping: the pilot file's raw bytes are the stream. The pilot is a
SPECIMEN of an unsettled draft — the lane's divine-"We" rendering
decision is still open with Robert — and this encoding changes nothing
about that status. Parses the file's own section headings (## ...) to
record per-section byte and base ranges. Aborts on any mismatch."""
import hashlib, json, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "dna-classical-chinese-pilot-2026-11-14"
SOURCE = ROOT / "ayah-classical-chinese/PILOT-CLASSICAL-CHINESE.md"
EXPECTED_BYTES = 4489
EXPECTED_SHA256 = "a2e848a30daffc805b6119d4eb0600b6c1b3efb9563498a85870f3975e781f61"

raw = SOURCE.read_bytes()
if len(raw) != EXPECTED_BYTES:
    sys.exit(f"ABORT: source is {len(raw)} bytes, expected {EXPECTED_BYTES}")
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SHA256:
    sys.exit(f"ABORT: source SHA-256 {sha} != expected {EXPECTED_SHA256}")
text = raw.decode("utf-8")

lines = text.split("\n")
offsets = []
pos = 0
for l in lines:
    offsets.append(pos)
    pos += len(l.encode("utf-8")) + 1
assert pos - 1 == len(raw) or (pos == len(raw) + 1 and lines[-1] == "")

head_lines = [(i, l[3:].strip()) for i, l in enumerate(lines) if l.startswith("## ")]
if len(head_lines) != 3:
    sys.exit(f"ABORT: found {len(head_lines)} section headings, expected 3")

def byte_span(start_line, end_line_exclusive):
    s = offsets[start_line]
    e = offsets[end_line_exclusive] if end_line_exclusive < len(lines) else len(raw)
    return s, e

segments = [("Front matter of the pilot (title, status, source note)", "front",
             0, offsets[head_lines[0][0]])]
for k, (li, title) in enumerate(head_lines):
    end_line = head_lines[k + 1][0] if k + 1 < len(head_lines) else len(lines)
    s, e = byte_span(li, end_line)
    kind = "section"
    segments.append((title, kind, s, e))

cursor = 0
for label, kind, s, e in segments:
    assert s == cursor, f"gap/overlap before segment {label}: {s} != {cursor}"
    cursor = e
assert cursor == len(raw), f"segments end at {cursor}, file is {len(raw)}"

ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw)

seq_path = LANE / "classical-chinese-pilot-dna.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "segments": [{"label": l, "kind": k, "byte_start": s, "byte_end": e,
                     "base_start": s * 4 + 1, "base_end": e * 4}
                    for l, k, s, e in segments]}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "segments": [(s["label"], s["base_start"], s["base_end"]) for s in fig["segments"]],
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
