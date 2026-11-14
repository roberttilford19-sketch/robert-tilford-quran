#!/usr/bin/env python3
"""Machine check of the far room's Bismillah DNA sequence (2026-11-14).
Decodes A=00 C=01 G=10 T=11 -> bits -> UTF-8 bytes -> Arabic,
then re-encodes the Arabic forward and compares both ways.
Sequence copied verbatim from Robert's pasted message."""
import hashlib

SEQ = ("TCGAGGGATCGCGCAATCGAGTATTCGCGCAGTCGCGACCTCGCGCAAAGAATCGCGTACTCGCGACATCGCGACATCGCGATG"
       "TCGCGCACTCGCGTAATCGCGACTTCGCGCAAAGAATCGCGTACTCGCGACATCGAGTACTCGCGATGTCGCGCACTCGAGGT"
       "CTCGCGCAGTCGCGACCTCGCGATGTCGCGTAATCGCGACGTCGCGCAAAGAATCGCGTACTCGCGACATCGAGTACTCGCGA"
       "TGTCGCGCACTCGAGGTCTCGCGCAATCGCGAGGTCGCGACCTCGCGCAA")
ARABIC = "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"

dec = {"A": "00", "C": "01", "G": "10", "T": "11"}
enc = {"00": "A", "01": "C", "10": "G", "11": "T"}

print("sequence length:", len(SEQ), "bases; alphabet:", sorted(set(SEQ)))
bits = "".join(dec[b] for b in SEQ)
raw = int(bits, 2).to_bytes(len(bits) // 8, "big")
print("decoded bytes:", len(raw))
text = raw.decode("utf-8")
print("decoded text:", text)
print("matches printed Arabic:", text == ARABIC)

b2 = ARABIC.encode("utf-8")
print("arabic utf-8 bytes:", len(b2), "; byte-identical to decoded:", b2 == raw)
bitstr = "".join(f"{byte:08b}" for byte in b2)
fwd = "".join(enc[bitstr[i:i + 2]] for i in range(0, len(bitstr), 2))
print("forward re-encode == given sequence:", fwd == SEQ)
print("sha256 of arabic utf-8:", hashlib.sha256(b2).hexdigest())
