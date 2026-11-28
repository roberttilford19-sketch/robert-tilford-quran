# Romansh lane — licence verification record
Recorded 2026-11-27 (build opening), per CANDIDATE-BRIEF-ROMANSH.md §8
caveats and the lane's build conditions (Robert's ruling of 2026-11-27,
21:16 CST, adopting the brief's desk recommendations wholesale; edition
in Rumantsch Grischun; per-title Bible-control licence verification a
named build condition).
House rule applied throughout: dictionary and Bible material is used
for FACT AND CITATION ONLY, never the maker's wording, whatever its
licence. Every licence below was read at the source named, at harvest,
2026-11-27.

## A. Lexical and attestation sources

### A1. Pledari Grond (Lia Rumantscha) — the lane's lexical base
- Data harvested from the official Pledari Grond monorepo
  (github.com/plattafurma-libra/pledari-grond, the Lia Rumantscha's
  own repository for the dictionary), files:
  maalr.conjugator/data/genfiles/entries_RG-DE.txt (215,614
  Rumantsch Grischun → German entry lines) and
  maalr.conjugator/data/db/verbs.sql (3,817 Rumantsch Grischun verbs
  with full conjugations), plus infinitives.txt.
- Repository licence: Apache License 2.0 (the repository's LICENSE
  file, read at harvest; saved at sources/pg-LICENSE.txt).
- Underlying dictionary rightsholder position, per the RUMLEM paper
  (University of Zurich / ZurichNLP) as recorded in the lane brief §3:
  the Pledari Grond dictionaries for Rumantsch Grischun, Surmiran,
  Sursilvan and Sutsilvan are openly licensed (© Lia Rumantscha
  1980–2025). The Vallader and Putèr dictionaries are © Uniun dals
  Grischs, all rights reserved — NOT relied on in this lane, which is
  built in Rumantsch Grischun only.
- House use: attestation-pointing, paradigm-checking and
  spelling-checking. The dictionary's German glosses and example
  phrases are cited as evidence in the attestation audit; the maker's
  wording is never copied into the book.

### A2. Hunspell spellchecker dictionaries (FAR / Lia Rumantscha)
- File: dictionaries/rm-rumgr/rm-rumgr.dic + rm-rumgr.aff from
  github.com/farscrl/spellcheckers-rumantschs — 160,802 Rumantsch
  Grischun word forms, stated in that repository's README to be
  derived from the Pledari Grond.
- Licence file read in full at harvest
  (dictionaries/rm-rumgr/rm-rumgr_LICENSE.txt): MIT License,
  © 2026 Lia Rumantscha / Pro Svizra Rumantscha.
- House use: the lane's form inventory — every word form seated in
  the translation must trace to this inventory, to the Pledari Grond
  paradigms (A1), to the glossary, or stand as a visible GAP.

### A3. RUMLEM (ZurichNLP, University of Zurich)
- Repository licence: MIT (GitHub licence record, read at harvest).
- Used as evidence for the Pledari Grond licence position in A1 and
  as a lemmatisation reference. No RUMLEM code is run in the build.

### A4. English Wiktionary Romansh entries, via kaikki.org
- Harvest: kaikki.org-dictionary-Romansh.jsonl (2,455 entries,
  2026-11-27). Wiktionary text is CC BY-SA.
- House use: POINTER only — English-gloss orientation for the audit;
  every seat must point back to Pledari Grond (A1), the form
  inventory (A2), or the running corpus (A5). Wiktionary's Romansh
  headwords lean toward Sursilvan and were never seated on their own
  authority; where kaikki's candidate form and the Pledari Grond /
  spellchecker spelling differed (e.g. casa/tgaun against the
  inventory's chasa/chaun), the inventory's Rumantsch Grischun
  spelling governed.

### A5. Romansh Wikipedia (rm.wikipedia.org)
- Dump of 2026-11-01 (7,132 pages; ~3.58 million tokens), text under
  CC BY-SA as with all Wikipedias.
- House use: running-text attestation and frequency evidence only —
  which forms actually occur in modern written Romansh. Not a copying
  base. (The Wikipedia is written in Rumantsch Grischun and the
  idioms; a form attested only there is corroboration, never the sole
  authority for a seat — seats rest on A1/A2.)

### A6. Dicziunari Rumantsch Grischun (DRG)
- The 13-volume historical dictionary, online at the Institut dal
  Dicziunari Rumantsch Grischun, described by the Trier Center for
  Digital Humanities as made freely available as an online
  dictionary. No bulk-reuse licence for the DRG data was stated in
  the sources consulted (brief §3).
- House use: consultation and fact-and-citation only. Not harvested,
  not a build base.

### A7. Rumantsch Grischun grammar (Caduff, Caprez, Darms, 2009)
- *Grammatica per l'instrucziun dal rumantsch grischun* (University
  of Fribourg Romansh seminar), in copyright.
- House use: fact and citation only — the paradigm norm the checker
  enforces is in any case carried mechanically by A1's conjugation
  database and A2's form inventory, not by this book's wording.

## B. Bible-control titles — per-title verification

Verification pass: BIBLE-CONTROL-VERIFICATION-2026-11-27.md in this
lane folder (completed before any verse was seated; its findings are
summarised here title by title, and the full record with sources
stands in that file).

1. **Bifrun, New Testament (Putèr), 1560** — text PUBLIC DOMAIN by
   age (published 1560). Digitised on e-rara (Kantonsbibliothek
   Graubünden, DOI 10.3931/e-rara-19331), freely downloadable; that
   record's own licence field was not rendered in the fetched page,
   so the scan licence is recorded CANDIDATE (platform pattern:
   Public Domain Mark). House use: citation-grade control only.
2. **Luci Gabriel, New Testament (Sursilvan), 1648** — text PUBLIC
   DOMAIN by age (1648; translator d. 1663 per e-rara contributor
   data). No digital copy of the 1648 edition was found; Gabriel's
   text is reachable in the 1870 BFBS printing (Google Books full
   view). House use: citation-grade control only, via title 5.
3. **Dorta / Vulpi, complete Bible (Vallader), Scuol 1679** — text
   PUBLIC DOMAIN by age (translators d. ca 1697 / 1706, per King's
   College London). Digital text NOT VERIFIED: no scan found on
   e-rara, HathiTrust, Google Books or Internet Archive, so this
   title cannot serve as the digital control. Recorded, not relied on.
4. **Bibla da Cuera (Sursilvan), 1717–1719** — text PUBLIC DOMAIN,
   VERIFIED on facts (imprint 1718 [1719], Chur, Andrea Pfeffer; all
   named contributors d. by 1743). Complete digitised copy with
   searchable OCR text layer on e-rara (Zentralbibliothek Zürich,
   Bibl 121), freely downloadable; per-title scan licence field not
   directly rendered — recorded as platform-pattern Public Domain
   Mark, CANDIDATE. House use: a principal citation-grade lexical
   control (historical Sursilvan; control value lexical/historical,
   as the verification record states).
5. **BFBS Bible (Sursilvan), 1870** — PUBLIC DOMAIN VERIFIED on two
   grounds: age, and HathiTrust's own rights rule (non-US pre-1901 =
   public domain, full view worldwide). Full view at HathiTrust
   (Record 009784222) and Google Books (University of Bern copy).
   House use: a principal citation-grade lexical control.
6. **Bibla ecumena romontscha (Sursilvan)** — IN COPYRIGHT. Volumes:
   New Testament 1988, Prophets 2004, Psalms 2010, Poetic Books 2014,
   Pentateuch 2022 (a later volume than the brief knew of); History
   Books outstanding. It is in Sursilvan, not Rumantsch Grischun
   (deliberate commission choice, per kath.ch). No digital text
   found. Publisher/rights holder NOT VERIFIED — no source named the
   rights holder in so many words. House use: fact and citation only,
   never a copying base; not relied on for any seat.
7. **Platform sweep (ISO roh / rm)** — Scripture Earth carries a
   verified roh index listing for Romansh/Switzerland, but the text,
   idiom and licence behind it could NOT be verified. Digital Bible
   Platform / Faith Comes By Hearing, eBible.org, Bible.com /
   YouVersion, BibleGateway: no Romansh text found (searches
   repeatedly surfaced Romani/Romanian, checked and excluded).
   Recorded as found; nothing relied on from any platform.

**Control position for the build (per the verification's closing
answer):** at least two complete historical Romansh Bibles have
freely usable digital texts for citation-grade lexical control —
the Bibla da Cuera (1718/1719, e-rara, public-domain text) and the
1870 BFBS Bible (HathiTrust / Google Books full view, public domain).
Both are Sursilvan-side historical texts; their control value for a
Rumantsch Grischun build is lexical and historical. The operative
lexical authority for Rumantsch Grischun forms remains Pledari
Grond (A1) with the form inventory (A2). No Bible wording, of any
title, is copied into this book; Bible material is fact and citation
only, exactly as house law requires.

## C. In-copyright sources — no licence relied on
- Bibla ecumena romontscha (see B6): fact and citation only.
- The RG grammar (A7): fact and citation only.
- La Quotidiana and RTR corpus material named in the brief: licences
  not stated in the sources consulted; NOT harvested and NOT relied
  on in this build.
