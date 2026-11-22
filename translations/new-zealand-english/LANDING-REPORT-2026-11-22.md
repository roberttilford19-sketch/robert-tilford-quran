# Landing Report — New Zealand English Dialect Edition (2026-11-22)

The third book of the English Dialects wave, following the Australian
English edition (commit 17403ca) and the South African English edition
(commit 7d34833) landed earlier the same day. Landed under the Pipeline
Landing Authorization (2026-11-14): the full loop passed clean, so no
per-book decision point was required.

## What this book is

A dialect edition of the Locked English Master — not a new translation.
The base is the corrected Ayah Companion manuscript
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md), the very
manuscript from which the locked shelf PDF at translations/english/ was
set, carrying every settled ruling of the master, including the 6:86
correction (Elisha, Decision 36). The master itself was not altered.

## Method

Token-level dialect conversion only, under a recorded list:
DIALECT-CONVERSION-LIST.tsv — 98 pairs, 388 word-forms changed across
the 6,236 verses. New Zealand English follows British spelling
conventions and is very close to Australian; on every attested pair New
Zealand usage is the same as the Australian and South African
conversions of this same master, so the New Zealand list is the South
African list whole — the 96 pairs the Australian lane attested plus the
two further attested seats that lane added, meager→meagre at 34:16
(the -er→-re class) and maneuvering→manoeuvring at 8:16 (the oe digraph
restored), which New Zealand usage also writes otherwise. This identity
is disclosed here, not dressed up as difference: a vocabulary scan of
the master (6,441 distinct tokens) found no further US form that New
Zealand usage writes differently. Classes: -ize→-ise (29 pairs),
-yze→-yse, -or→-our in the sanctioned set (35), double-l inflections
(travelled family), double-p (worshipped family), fulfil family,
defence/offence, British headword forms (judgement, grey, jewellery,
plough, sceptic, adviser, moulded, counsellors), cognisant, the
practise family, and the two seats above. One pair is seat-scoped:
practice→practise at the 12 seats where the master's word is a verb; at
the 3 nominal seats (35:43; 5:3; 8:38) the noun "practice" is already
the New Zealand form and stands unchanged. No pair was applied that
the text did not attest; classes with no attested member (-centre/
-theatre nouns, -logue, licence) record zero pairs. The seize family,
horizon, bizarre, elaborate, pardon, the agent -or nouns (Creator,
Protector), the verb "tires", "story/stories" (all narrative in the
master; "storey" in the building sense is unattested), "installed",
"dispatch", and "inquire" were examined and left unchanged — they are
spelled the same in New Zealand English, or (inquire) both forms are
current and the difference is one of register, not correctness.

## Verification

- Extraction: 6,236 of 6,236 verses from the master, per-surah grid
  matching at all 114 surahs, no duplicates, no missing seats;
  basmalah surahs 112; sajda notes 15.
- Independent checker (check.py in the lane tree, written separately
  from the builder): PASS on all 19 checks — seat sets equal; headings
  matching the master's own Contents; basmalah lines at exactly the 112
  surahs that carry one; sajda notes at exactly the master's 15 seats,
  identical; token counts and non-token skeletons identical at every
  seat; every changed token explained by the list; per-pair tallies
  equal to the recorded counts; every pair validated against the
  checker's own sanctioned-pattern rules; meagre at 34:16 and
  manoeuvring at 8:16 converted exactly; no listed US form surviving.
- PDF (house book pattern, Typst): 455 pages, 6,236 verse references in
  its text layer, final page carries 114:6, full font coverage, title
  and status pages verified in the built file and read visually.

## Pack

ayah-companion-manuscript-NZ.md; the book PDF;
DIALECT-CONVERSION-LIST.tsv; CHECKER-REPORT.md; this report;
MANIFEST.txt with machine-computed sizes and SHA-256 hashes.

Gift terms, as every folder on this shelf: free to read and free to
download, never sold; attribution requested.
