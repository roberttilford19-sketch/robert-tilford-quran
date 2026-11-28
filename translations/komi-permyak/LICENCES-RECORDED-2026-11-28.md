# Komi-Permyak lane — licences recorded at point of use (2026-11-28)

Recorded before any seat was taken, per brief §8 condition 2.

- **GiellaLT / Giellatekno — giella-koi (UiT The Arctic
  University of Norway)** — the repository licence file was read
  at the desk on 2026-11-28 from the lang-koi repository itself
  (sources/lang-koi-main/LICENSE): **GNU Lesser General Public
  License, version 3 (LGPL v3)**. The finite-state stem files and
  dictionary XML (src/fst/morphology/stems/*.lexc, *_koi2x.xml,
  verbs.xml) and the gt-norm paradigm test files
  (src/fst/test/gt-norm-yamls/*.yaml, proofread by Larisa
  Ponomareva, 2019-10-22) were downloaded 2026-11-28
  (sources/lang-koi.zip) and parsed at the desk into
  sources/giella-koi-lemmas.json (77,661 lemmas),
  sources/koi-gloss-dict.json (14,725 lemmas with Russian —
  and a few Finnish/English — glosses) and
  sources/yaml-forms.json (15,533 paradigm forms). Use in this
  lane: attestation pointing and paradigm checking only — fact
  and citation, never a copying base. Recorded caution (brief
  §3): the Permyak description was initially derived from the
  Komi-Zyrian lexicon; seats in this build trace to the
  dictionary XML's own Komi-Permyak entries, the proofread
  paradigm files, or Wiktionary Komi-Permyak entries — the
  native-speaker correction layer — and the attestation audit
  names the seats whose trail is thin.
- **English Wiktionary Komi-Permyak entries** — **CC BY-SA**
  (Wiktionary's licence). Retrieved at the desk on 2026-11-28
  through the MediaWiki API (category walk from
  Category:Komi-Permyak lemmas, 337 pages) into
  sources/wikt-koi-parsed.json (334 headwords with English
  glosses) and sources/eng2koi-wikt.json. Use: attestation
  pointing only. **kaikki.org has no Komi-Permyak per-language
  download**: its dictionary index (read 2026-11-28) lists
  Komi-Zyrian but not Komi-Permyak, and every Komi-Permyak
  kaikki URL tried returned the same 162-byte 404 page — which
  is what the previous crew's truncated kaikki-koi.jsonl held.
  The harvest was therefore redone through the API above, and
  the bogus file was deleted.
- **The Komi-Permyak New Testament (Бур Юӧр 2019)** — Institute
  for Bible Translation, Finland. **In copyright; no open
  licence was found in the candidate brief's scout (brief §4)
  and none is assumed here.** No complete Bible in Komi-Permyak
  was found; the verified control is the complete New Testament
  (2019), verse-aligned in the PaBiVUS Korp corpus (Language
  Bank of Finland). Lawful house use only: fact and citation —
  the control's existence is cited; no Bible wording is held,
  copied, or reproduced in this build, and the control is never
  used as a spelling authority (brief §8 condition 3).
- **Batalova & Krivoshchekova-Gantman (1985) and the historical
  dictionary line (Rogov 1869, Popov 1785)** — in copyright or
  licence-unverified on the brief's record; cited as the norm's
  lexicographic tradition by fact and citation only. No text
  was copied from any of them in this build.
- **The Locked English Master**
  (~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
  MD5 ecc5b8e2848e5044186b7ad82bed9f4e) — Robert Tilford's own
  text; the build base, held at master-verses.json (114 surahs,
  6,236 verses, verified against the Master; identical copy to
  the sibling lanes).
