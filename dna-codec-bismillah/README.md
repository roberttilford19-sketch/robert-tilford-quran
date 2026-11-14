# The Bismillah as a DNA Sequence — a Demonstration

This folder holds a small, exact demonstration: the Bismillah — بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, "In the name of God, the Beneficent, the Merciful" — written as a sequence of DNA bases.

The method is a simple codec, stated in full so anyone can check it. The Arabic text is taken as its UTF-8 bytes, 75 bytes in all. Each byte is read as eight bits, and each pair of bits becomes one DNA base: 00 becomes A, 01 becomes C, 10 becomes G, and 11 becomes T. Seventy-five bytes make 600 bits, and 600 bits make exactly 300 bases. The sequence stands in `bismillah-dna.txt`, with the Arabic it encodes written under it.

The encoding was verified by machine at this desk on November 14, 2026, in both directions. Decoding the 300 bases returns the Arabic byte for byte, and encoding the Arabic forward again reproduces the sequence character for character. The checking script is in this folder as `check-bismillah-dna.py`, and its actual output from the verification run is kept beside it in `VERIFICATION.txt`.

The credit is stated plainly. The sequence was generated in Robert Tilford's conversation with Google's LLM on November 14, 2026, at his direction. The verification was performed by Awen by Muse by Meta.

The honest scope of this deposit is narrow, and it is stated here so no one has to guess. This is an in-silico demonstration only — a sequence on a screen and in this file. Nothing has been synthesized. No physical DNA exists, and nothing in this folder is or claims to be a biological artifact.

On the question of whether this has been done before, the house wording is the careful one, and it is carried here exactly: a published, complete, machine-verified encoding of the Bismillah under a stated codec was **none found after research** as of November 14, 2026. That sentence is narrow on purpose, because the broader ground is already occupied, and the precedents are named in this same breath: Joe Davis's *Malus ecclesia* project inserted a verse of the Quran into the genome of an apple tree, and a Harvard–MIT conference paper published a DNA encoding of the Arabic phrase "Subhan Allah." Because those stand on the record, no broad first claim is made here — only the narrow one, with its evidence beside it.

Physical synthesis — ordering this sequence from a laboratory and holding it in a vial — is a separate, future, funded lab project, and it is not part of this deposit.
