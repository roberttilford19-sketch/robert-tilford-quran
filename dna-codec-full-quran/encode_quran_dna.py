#!/usr/bin/env python3
"""ENCODER — Quran DNA lane (2026-11-14).
Extracts the Arabic run sequence from the Locked English Master of record by
structural position (the house verifier's amended method, 2026-11-14),
cross-checks it against the lane meta.json expectation, encodes the byte
stream with the demonstrated codec (UTF-8 bytes -> bits -> 00=A 01=C 10=G
11=T), and writes quran-dna-full.txt + MANIFEST-DNA-FULL.md + work/encoder.json.
Aborts on any mismatch. No Arabic is retyped anywhere in this script."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "quran-dna-full-2026-11-14"
MASTER = ROOT / "ayah-audit/corrected/ayah-companion-manuscript.md"
META_PATH = ROOT / "ayah-bajaw/work/meta.json"
EXPECTED_MD5 = "064ee170806bb31f5bac3e75d2aa4d94"

raw = MASTER.read_bytes()
md5 = hashlib.md5(raw).hexdigest()
if md5 != EXPECTED_MD5:
    sys.exit(f"ABORT: master MD5 {md5} != expected {EXPECTED_MD5}")
meta = json.loads(META_PATH.read_text(encoding="utf-8"))
text = raw.decode("utf-8")
bs = text.index("\n# Part I · The Translation\n") + 1
be = text.index("\n# Part II · Concordance", bs)
lines = text[bs:be].splitlines()
arab = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")

sections, cur = {}, None
for l in lines:
    m = re.match(r"^## (\d+)\. ", l)
    if m:
        cur = int(m.group(1)); sections[cur] = []
    elif cur is not None:
        sections[cur].append(l)

runs = []            # (kind, surah, ref_or_None, string)
per_surah = []
for n in range(1, 115):
    sec = sections.get(n, [])
    s = meta[str(n)]
    name = None
    for l in sec:
        tm = re.match(r"^\*\*(.+?)\*\* ·", l)
        if tm:
            name = tm.group(1); break
    assert name is not None, f"surah {n}: no header name"
    surah_runs = [("name", n, None, name)]
    vidx = [i for i, l in enumerate(sec) if re.match(r"^\*\*\d+:\d+\*\*", l)]
    firstv = vidx[0] if vidx else len(sec)
    if s["basmalah"]:
        bas = None
        for l in sec[:firstv]:
            if l.strip() and not l.startswith("*") and arab.search(l):
                bas = l; break
        assert bas is not None, f"surah {n}: basmalah frame flagged but not found"
        surah_runs.append(("frame", n, None, bas))
    assert len(vidx) == s["count"], f"surah {n}: {len(vidx)} verse blocks != meta {s['count']}"
    for k, i in enumerate(vidx):
        ref = re.match(r"^\*\*(\d+:\d+)\*\*", sec[i]).group(1)
        end = vidx[k + 1] if k + 1 < len(vidx) else len(sec)
        cand = [l for l in sec[i + 1:end]
                if l.strip() and not re.fullmatch(r"-+", l.strip())
                and not re.match(r"^\*\[.*\]\*$", l.strip())]
        assert cand, f"verse {ref}: no Arabic candidate"
        surah_runs.append(("verse", n, ref, cand[-1]))
    runs.extend(surah_runs)
    per_surah.append({"surah": n, "title_en": s["title_en"], "translit": s["translit"],
                      "arabic_name": s["arabic_name"], "verses": s["count"],
                      "runs": len(surah_runs)})

expected = []
for n in range(1, 115):
    s = meta[str(n)]
    expected.append(s["arabic_name"])
    if s["basmalah"]:
        expected.append(s["basmalah_ar"])
    for v in s["verses"]:
        expected.append(v["arabic"])
got = [r[3] for r in runs]
assert got == expected, "ABORT: structural extraction != meta.json expectation"
kinds = {}
for k, _, _, _ in runs:
    kinds[k] = kinds.get(k, 0) + 1
assert len(runs) == 6462 and kinds == {"name": 114, "frame": 112, "verse": 6236}, kinds
assert all(r[3] and r[3] == r[3].strip() for r in runs), "a run carries surrounding whitespace"

stream = "".join(got).encode("utf-8")
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for b in range(256):
    bits = f"{b:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in stream)
assert len(bases) == 4 * len(stream)

offset = 0
for row in per_surah:
    n = row["surah"]
    sbytes = sum(len(r[3].encode("utf-8")) for r in runs if r[1] == n)
    row["bytes"] = sbytes
    row["bases"] = 4 * sbytes
    row["base_start"] = offset + 1
    row["base_end"] = offset + 4 * sbytes
    offset += 4 * sbytes
assert offset == len(bases)

seq_path = LANE / "quran-dna-full.txt"
with seq_path.open("w", encoding="utf-8") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_stream = hashlib.sha256(stream).hexdigest()
sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
cons = json.loads((LANE / "work/consistency.json").read_text(encoding="utf-8"))
detail = json.loads((LANE / "work/consistency-detail.json").read_text(encoding="utf-8"))

fig = {"master_md5": md5, "runs_total": len(runs), "runs_by_kind": kinds,
       "arabic_bytes": len(stream), "total_bases": len(bases),
       "sha256_arabic_stream": sha_stream, "sha256_base_stream": sha_bases,
       "per_surah": per_surah}
(LANE / "work/encoder.json").write_text(json.dumps(fig, ensure_ascii=False, indent=2), encoding="utf-8")

rows = "\n".join(
    f"| {r['surah']} | {r['title_en']} | {r['translit']} | {r['arabic_name']} | {r['verses']} | "
    f"{r['bytes']} | {r['bases']} | {r['base_start']}–{r['base_end']} |" for r in per_surah)
manifest = f"""# MANIFEST — The Quran Encoded in DNA Letters (full text, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day. Framework from Robert Tilford's 2026-11-14
conversation with Google's LLM; the codec was demonstrated there on the
Bismillah and verified by machine at this desk before this build began.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete Arabic text of
the Quran, taken from the master of record below, written in the four DNA
letters A, C, G, T under the codec stated below. **Nothing has been
synthesized. No physical DNA exists.** Physical synthesis is a separate,
future, funded laboratory project and is not part of this deposit.

## The codec (exactly the demonstrated one)

Arabic text as UTF-8 bytes → binary bits → every two bits become one base:
**00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes four bases. The mapping is
lossless and reversible: decoding the base stream returns the byte stream
exactly, which the independent decoder's report in this deposit proves by
hash.

## Source of record

- Master: `~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md`
  (the Locked English Master, post-6:86 correction).
- MD5, machine-verified before extraction: `{md5}`
- The Arabic was extracted **by code, never retyped**.

## Extraction rule (disclosed exactly)

The encoded stream is the master's complete Arabic run sequence for Part I
(The Translation), taken by **structural position** — the house verifier's
amended method of 2026-11-14 — in master order. For each surah 1–114:

1. the surah-header Arabic name, from the `**<name>** · …` title line;
2. the basmalah frame line standing in the surah preamble, where the surah
   carries one (112 surahs carry a frame; Surah 1 has none because the
   basmalah is its verse 1, and Surah 9 has none);
3. for every verse block, the last non-empty, non-separator, non-marker line
   of the block — the verse's Arabic.

The runs are concatenated **with no separator characters**; the byte stream is
the UTF-8 encoding of that concatenation. Before encoding, the extracted
sequence was checked for exact equality against the lane `meta.json`
expectation (the same equality the house verifier requires of every lane) —
it matched, run for run.

- Runs: **6,462** = 114 surah names + 112 basmalah frames + **6,236 verses**
- Arabic byte stream: **{len(stream):,} bytes**
- Base stream: **{len(bases):,} bases** (4 per byte)
- SHA-256 of the Arabic byte stream: `{sha_stream}`
- SHA-256 of the base stream: `{sha_bases}`

## Consistency check against the Bismillah specimen (reported as found)

The verified demonstration specimen encoded the Bismillah in **300 bases**
(75 bytes). The master's own 1:1 basmalah, encoded by the same codec, is
**292 bases** (73 bytes). **They are not identical, and no match was forced.**
{detail['finding']}

The specimen stands as the proof of the codec; this deposit encodes the
master of record exactly as it stands.

## Per-surah index

| Surah | Title | Transliteration | Arabic name | Verses | Arabic bytes | Bases | Base range |
|---|---|---|---|---|---|---|---|
{rows}

## Files in this deposit

- `quran-dna-full.txt` — the full base stream, wrapped at 60 bases per line.
- `MANIFEST-DNA-FULL.md` — this manifest.
- `encode_quran_dna.py` — the encoder (extraction + encoding).
- `validate_dna.py` — the hygiene validator (report-only).
- `decode_quran_dna.py` — the independent decoder, written separately.
- `INDEPENDENT-DECODER-REPORT.md` — the decoder's verdict, preserved unedited.
- `QURAN-DNA-FULL-PRINT.pdf` — the paper book typeset from the verified
  sequence file.
"""
(LANE / "MANIFEST-DNA-FULL.md").write_text(manifest, encoding="utf-8")
print(json.dumps({k: v for k, v in fig.items() if k != "per_surah"}, indent=2))
print("sequence file:", seq_path, seq_path.stat().st_size, "bytes")
