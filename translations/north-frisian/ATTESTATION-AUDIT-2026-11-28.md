# North Frisian (Mooring) lane — attestation audit (2026-11-28)

Scope: what the held inventories attest FOR MOORING, and what
they do not. Method: sources/harvest.py over the kaikki.org
North Frisian dump (1,546 entries) plus the hand-harvested
LearnFrisian Mooring column (178 pairs).

- Entries carrying at least one Mooring-tagged sense: **463**.
- Entries with no dialect tag on any sense (pan-dialect, e.g.
  the pronoun hi): **113** — seated under disclosed rule (b)
  of BUILD-SPEC.
- Entries attested only for other dialects (Söl'ring,
  Fering-Öömrang, Heligoland, Halligen, Wiedingharde,
  Goesharde): **968** — excluded entirely; no form from them
  seats.
- Mooring inventory after the screen: **3,685 forms**,
  including **268 attested plural forms**
  (sources/mooring-plurals.json).

## The central negative finding

The held modern inventories attest NO Mooring seat for: god,
lord, heaven, heavens, angel, soul, spirit, mercy, merciful,
beneficent, sin, prophet, messenger (noun), truth (noun),
sign, judgment, punishment, reward, faith (noun), wisdom,
knowledge (noun), holy, blessed, worship, forgive, prayer
(noun), resurrection, scripture. Each stands as a GAP
throughout the draft. Bendsen (1860) attests several of these
in 1860 Mooring spelling (God: Godd / Göd; sin: Senne; grace:
Gnahse; heaven: Himmel in a garbled OCR reading) — held as
historical corroboration that the words exist in Mooring, and
barred as seats because the build norm is the modern spelling.
A checker with the modern print Mooring dictionaries
(Petersen 1973; Jörgensen 1978; Sjölin/Walker/Wilts 1988;
Basiswörterbuch 2000) can close many of these seats; that is
the first task named for the independent checker.

Everyday function words likewise unattested for Mooring in
the held inventories — for, who, on, by, before, after,
against, upon, there, some — stand as GAPs. They are GAPs of
the held record, not claims that Mooring lacks the words.

## Screen bugs found and fixed during the build

1. The engine's stem device stripped a final "d", seating
   "God" as gunge ("to go"). Fixed by removing that variant;
   God now takes its GAP, and 1:1 re-verified exact.
2. The first harvest excluded an entry's headword whenever any
   Mooring-tagged alternative form existed, which wrongly
   excluded hat ("it" — its Mooring alternative jü belongs to
   the entry's "she" sense). Fixed: the headword of a
   Mooring-sense entry always enters the inventory, alongside
   its Mooring-tagged forms; disclosed in harvest.py.
3. A sample read caught "this" seated as diling — which is
   "today". The entry was removed; "this" now stands as a GAP,
   and the full pipeline was re-run (final census: 6,190 GAP
   seats, 50,826 markers, 5,551 distinct terms; 429 verified
   dictionary entries).
