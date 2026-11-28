# Moksha lane — licence verification record
Recorded 2026-11-27 (build opening), per CANDIDATE-BRIEF-MOKSHA
§§3, 8 and Robert Tilford's ruling of 2026-11-27 (21:16 CST,
the OPEN-IN-ORDER QUEUE: Lule Sámi, Erzya, Udmurt, Moksha, …;
Lule Sámi and Erzya landed, Udmurt in remediation, Moksha next).
House rule applied throughout: dictionary and Bible material is
used for FACT AND CITATION ONLY, never the maker's wording,
whatever its licence.

## Open sources harvested at the desk
- **GiellaLT / Giellatekno — giella-mdf (lang-mdf), UiT The Arctic
  University of Norway** — the repository's LICENSE file was read
  in full at the desk 2026-11-27: GNU Lesser General Public License
  v3 (incorporating GPL v3). The full repository archive was
  retrieved from github.com/giellalt/lang-mdf 2026-11-27 and is held
  at sources/giella/ (12 MB archive at sources/giella-mdf-lexicon.zip).
  The stem XML files (src/fst/morphology/stems/*.xml) carry lemma,
  part of speech, and Finnish / French glosses seat by seat; the
  parsed inventory (27,691 Giella lemmas; 29,515 with the Wiktionary
  harvest below) is held at sources/mdf-lemmas.json. House use:
  attestation-pointing (that a form exists, and what it means) —
  never a copying base for running text. Scale on the record
  (Kielipankki, attestation 2024-07-24): ~852 continuation lexica,
  189,476 lemma-stem pairs, ~13,200 common nouns, ~13,500 verbs,
  over 11,000 adjectives, plus a shared set of over 94,000 proper
  nouns.
- **English Wiktionary Moksha entries, via kaikki.org (wiktextract)**
  — CC BY-SA (Wiktionary's licence). The full kaikki.org Moksha
  JSONL (2,566 entries, 5.1 MB) was retrieved 2026-11-27 and is held
  at sources/kaikki-mdf.jsonl; the English-gloss index is at
  sources/eng2mdf.json. House use: attestation-pointing with
  corroboration in giella-mdf for load-bearing seats, per brief §3.
- **UD_Moksha-JR treebank (Universal Dependencies)** — licence
  stated by the source: CC BY-SA 4.0 (brief §3). Not harvested as a
  build base; cited as a syntax/annotation control on the record.
- **ERME corpora / PaBiVUS, Language Bank of Finland (Kielipankki /
  FIN-CLARIN)** — NOT harvested in this build. The brief records
  that the licence limits the context shown to a "necessary one"
  and that subcorpus terms govern each part; no reliance beyond the
  brief's own citation of the corpora's existence and design was
  made. Recorded here so the non-reliance is on the record.
- **Akusanat / Veʹrdd dictionary datasets (Giella XML dictionaries
  on GitHub)** — named in brief §3; the giella-mdf stem XML harvested
  above is the same Giella infrastructure family and is the copy of
  record for this build. No separate Akusanat dataset was bulk-relied on.

## In-copyright sources (no licence relied on)
- **New Testament in Moksha, 2016** (translator Valentina Mishanina,
  named by Kielipankki; Institute for Bible Translation associated
  with the Moksha Gospel programme) — IN COPYRIGHT, no open licence
  found (brief §4). Control by fact and citation only: it was NOT
  harvested and NOT consulted as a wording base in this build; the
  brief's record of its existence and scope (complete New Testament
  2016; Gospel of Mark 1995 test translation; Gospel of John 1901,
  public domain by age, as historical corroboration) is the citation
  relied on. No complete Moksha Bible and no named modern Moksha Old
  Testament portion was found (brief §4) — disclosed inside the book.
- **Herrala & Feoktistov (1998), Moksha–Finnish Dictionary, and the
  Saransk-school Moksha–Russian dictionaries; Poljakov (ed.) (2004),
  Moksha–Erzya–Russian trilingual dictionary; Paasonen, Dictionary
  of Mordvin Dialects** — fact and citation only in any case; not
  harvested. The comparative volumes keep Moksha and Erzya in
  separate columns and were used, on the brief's record, only that way.

## The Moksha / Erzya fence (brief §§1–2, 8 condition 1)
Moksha (ISO 639-3 mdf) ONLY. Erzya (myv) is a separate language with
its own standard; no Erzya form is seated as a Moksha form, and no
Erzya–Moksha machine-translation output was used as a drafting base
(brief §3 bar). Every seated lemma in this build traces to the mdf
inventories above, never to an Erzya (myv) inventory.

## Master of record
The Locked English Master (~/workspace/ayah-audit/corrected/
ayah-companion-manuscript.md, MD5 ecc5b8e2848e5044186b7ad82bed9f4e);
verse texts in master-verses.json (114 surahs, 6,236 verses,
verified against the Master, identical copy to the Erzya/Udmurt lanes).
