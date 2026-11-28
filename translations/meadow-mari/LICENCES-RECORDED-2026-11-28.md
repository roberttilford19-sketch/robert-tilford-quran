# Meadow Mari lane — licence verification record
Recorded 2026-11-28 (build opening), per CANDIDATE-BRIEF-MEADOW-MARI
§§3, 8 and Robert Tilford's ruling of 2026-11-27 (21:16 CST, the
OPEN-IN-ORDER QUEUE: Lule Sámi, Erzya, Udmurt, Moksha, Meadow Mari,
…; Meadow Mari fifth in that queue). House rule applied throughout:
dictionary and Bible material is used for FACT AND CITATION ONLY,
never the maker's wording, whatever its licence.

## Open sources harvested at the desk
- **GiellaLT / Giellatekno — giella-mhr (lang-mhr), UiT The Arctic
  University of Norway** — the repository's LICENSE file was read
  in full at the desk 2026-11-28: GNU Lesser General Public License
  v3 (incorporating GPL v3). The full repository archive was
  retrieved from github.com/giellalt/lang-mhr 2026-11-28 and is held
  at sources/lang-mhr.zip (the unpacked tree was parsed into the
  inventories below and then removed to save space; the archive is
  the copy of record). The stem
  XML files (src/fst/morphology/stems/*.xml) carry lemma, part of
  speech, and Finnish / English / Russian glosses seat by seat; the
  parsed inventory (50,921 Giella lemmas; 51,416 with the Wiktionary
  harvest below) is held at sources/mhr-lemmas.json, with full gloss
  data at sources/giella-lemmas-full.json. House use:
  attestation-pointing (that a form exists, and what it means) —
  never a copying base for running text. Scale on the record
  (brief §3, Kielipankki): 438 continuation lexica, approximately
  156,490 lemma-stem pairs, approximately 25,881 common nouns,
  10,305 adjectives, and 7,643 verbs.
- **English Wiktionary Meadow Mari ("Eastern Mari") entries, via
  kaikki.org (wiktextract)** — CC BY-SA (Wiktionary's licence). The
  full kaikki.org Eastern Mari JSONL (1,220 headwords, 5.0 MB) was
  retrieved 2026-11-28 and is held at sources/kaikki-mhr.jsonl;
  the parsed gloss index is at sources/kaikki-mhr-parsed.json.
  House use: attestation-pointing with corroboration in giella-mhr
  for load-bearing seats, per brief §3.
- **Mari–English Dictionary (University of Vienna, Mari Web
  Project; eds. Riese, Bradley, Guseva; FWF grant P22786-G20)** —
  42,561 headwords, Meadow Mari literary standard only, published
  under a Creative Commons licence with attribution (press release,
  25 July 2014, as recorded in brief §3). The exact Creative Commons
  variant was not named in the pages retrieved by the brief and was
  NOT separately re-verified at build opening; it is recorded here
  exactly as the brief records it, and the house use in this build
  does not rely on the dictionary as a copying base in any case:
  the build's attestation base is the GiellaLT and Wiktionary
  inventories above, harvested at the desk. Recorded as an open
  seat for the independent checker.
- **Corpus of Literary Mari (mari-language.com)** — 57.38 million
  tokens of Meadow Mari (Hill Mari portion fenced out). No blanket
  reuse licence was stated in the pages retrieved by the brief;
  licence unverified / fair-use only. NOT harvested as a build base
  in this build; cited on the record only.

## In-copyright sources (no licence relied on)
- **У Сугынь [New Testament] in Meadow Mari** (Institute for Bible
  Translation, Finland; first published 1986, current text 2007,
  version MNT07) — IN COPYRIGHT, no open licence found (brief §4).
  Control by fact and citation only: it was NOT harvested and NOT
  consulted as a wording base in this build; the brief's record of
  its existence and scope (complete New Testament; no complete
  Meadow Mari Bible verified, no Old Testament book or portion
  verified) is the citation relied on. That narrower control is
  disclosed inside the book.
- **The ten-volume Словарь марийского языка / Марий йылме мутер
  (МарНИИЯЛИ, Yoshkar-Ola, 1990–2005) and the 2011 orthographic
  dictionary (Ivanov et al., Марий орфографий мутер)** — in
  copyright; fact and citation only; not harvested.
- **Riese, Bradley & Yefremova, Mari (марий йылме): An Essential
  Grammar for International Learners (University of Vienna, 2022)**
  — in copyright; reference, fact, and citation only.

## The Meadow / Hill fence (brief §§1–2, 8 condition 1)
Meadow Mari (ISO 639-3 mhr) ONLY. Hill Mari (mrj) is a separate
literary standard with its own alphabet (Ӓ ӓ, Ӧ ӧ, Ӱ ӱ, Ӹ ӹ; no ҥ);
no Hill Mari form is seated as a Meadow Mari form, and canonical
verification for this lane rejects any token containing ӓ or ӹ.
Northwestern Mari forms are likewise never seated. Erzya (myv),
Udmurt (udm), Moksha (mdf), Tatar, and Russian forms are never
seated as Meadow Mari forms except where the form itself stands in
the harvested mhr inventories (attested loans are flagged in the
glossary).

## Master of record
The Locked English Master (~/workspace/ayah-audit/corrected/
ayah-companion-manuscript.md, MD5 ecc5b8e2848e5044186b7ad82bed9f4e);
verse texts in master-verses.json (114 surahs, 6,236 verses,
verified against the Master, identical copy to the
Erzya/Udmurt/Moksha lanes).
