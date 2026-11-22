# Landing Report — Australian English Dialect Edition (2026-11-22)

The first book of the English Dialects wave, opened by Robert Tilford's
word on 2026-11-22 ("where is my Australian Koran … those are really low
hanging fruit"). Landed under the Pipeline Landing Authorization
(2026-11-14): the full loop passed clean, so no per-book decision point
was required.

## What this book is

A dialect edition of the Locked English Master — not a new translation.
The base is the corrected Ayah Companion manuscript
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md), the very
manuscript from which the locked shelf PDF at translations/english/ was
set (its build script names it as source), carrying every settled ruling
of the master, including the 6:86 correction (Elisha, Decision 36). The
master itself was not altered.

## Method

Token-level dialect conversion only, under a recorded list:
DIALECT-CONVERSION-LIST.tsv — 96 pairs, 386 word-forms changed across
the 6,236 verses. Classes: -ize→-ise (29 pairs), -yze→-yse, -or→-our in
the sanctioned set (35), double-l inflections (travelled, counsellors'
stem classed separately), double-p (worshipped family), fulfil family,
defence/offence, Australian headword forms (judgement, grey, jewellery,
plough, sceptic, adviser, moulded), cognisant, and the practise family.
One pair is seat-scoped: practice→practise at the 12 seats where the
master's word is a verb; at the 3 nominal seats (35:43; 5:3; 8:38) the
noun "practice" is already the Australian form and stands unchanged.
No pair was applied that the text did not attest; classes with no
attested member (-centre/-theatre, -logue, ae/oe digraphs) record zero
pairs. The seize family, horizon, bizarre, elaborate, pardon, the agent
-or nouns (Creator, Protector), the verb "tires", and "inquire" were
examined and left unchanged — they are spelled the same in Australian
English, or (inquire) both forms are current and the difference is one
of register, not correctness.

## Verification

- Extraction: 6,236 of 6,236 verses from the master, per-surah grid
  matching at all 114 surahs, no duplicates, no missing seats.
- Independent checker (check.py in the lane tree, written separately
  from the builder): PASS on all 18 checks — seat sets equal; headings
  matching the master's own Contents; basmalah lines at exactly the 112
  surahs that carry one; sajda notes at exactly the master's 15 seats,
  identical; token counts and non-token skeletons identical at every
  seat; every changed token explained by the list; per-pair tallies
  equal to the recorded counts; every pair validated against the
  checker's own sanctioned-pattern rules; no listed US form surviving.
- PDF (house book pattern, Typst): 455 pages, 6,236 verse references in
  the text layer, final page carries 114:6, full font coverage, title
  and status pages verified in the built file and read visually.

## Pack

ayah-companion-manuscript-AU.md; the book PDF;
DIALECT-CONVERSION-LIST.tsv; CHECKER-REPORT.md; this report;
MANIFEST.txt with machine-computed sizes and SHA-256 hashes.

Gift terms, as every folder on this shelf: free to read and free to
download, never sold; attribution requested.
