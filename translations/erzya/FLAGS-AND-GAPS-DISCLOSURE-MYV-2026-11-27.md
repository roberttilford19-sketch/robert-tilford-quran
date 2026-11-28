# Flags and Gaps Disclosure — Erzya (myv) Quran

Status: DRAFT — NOT PUBLISHED. Built under Robert Tilford's ruling
of 2026-11-27 (21:16 CST, OPEN-IN-ORDER QUEUE, second after Lule
Sámi), under the Pipeline Landing Authorization (2026-11-14).

## Counts, in the same breath

Complete rendering: 6,236 of 6,236 verses; 6,180 rendered in full;
56 verses carry one or more visible ⟦GAP: …⟧ markers — 70 markers
in all: jinn 30, pilgrimage 19, usury 8, Sabbath 7, apes 2, ape 1,
cucumber 1, lentils 1, hoopoe 1. Standing GAP terms (attestation
audit): jinn, pilgrimage as a term, the Sabbath as an institution,
and usury are never invented and never silently borrowed; the
single-term GAPs (cucumber, lentils, apes/ape, hoopoe) are seats
where no attested Erzya form was found for that item.

## Base

Modern literary Erzya (ISO 639-3 myv), Cyrillic as used for Russian
with no modifications, Central-dialect-based, post-2002 Saransk
norm. Erzya only — no Moksha (mdf) form is seated. Attestation
base: GiellaLT giella-myv (LGPL v3) and the English Wiktionary
Erzya harvest via kaikki.org (CC BY-SA); the 2006 Erzya New
Testament and the modern dictionaries are controls by fact and
citation only, their wording never reproduced. No first-translation
claim is made anywhere in the book.

## Flagged seats and devices (glossary §G, attestation audit)

- Basmalah: both mercy names rest on the one attested stem
  седеймариця — Пазонь лемсэ, Седеймариця, Седеймариця.
- Descriptive devices, disclosed: Пазонь кучовкс (messenger),
  Судонь чи (Day of Judgement), Ине Ойме (Holy Spirit),
  Пазонь невтема (revelation), виде ки (straight path),
  певтеме эрямо (eternal life), казне максомс (zakāh — no rate
  ever stated), велявтомс Пазонтень (repent), молемс мельга
  (follow), кемиця / а кемиця (believer / disbeliever),
  тамаша device at sorcery seats, пакся garden device,
  оршамопель garment device, прамо prostration device.
- Attested loans, flagged: рай, пост / постовамс, ангел,
  архангел, ханства, сатана, шайтян.
- Regular -мо formations flagged: баславамо, простямо, вельмема.
- Thin seats flagged in the audit: тамаша (miracle), кармавтома
  (covenant), пежедема (oath), озкс (sacrifice — the traditional
  Erzya rite), озатя (priest).

## Disclosures added at checker direction (2026-11-27)

Full record: REMEDIATION-LOG-MYV-2026-11-27.md, entries D1–D4.

- D1: мерсь, the paradigm-regular 3sg past of меремс (printed in
  the build spec's own paradigm), is used 161 times against the
  spec's stated preference for ёвтась (310 times). Disclosed,
  not regularised.
- D2: inventory-attested Russian-shaped loans seated beyond the
  audit's flagged list: искушения ×3, средства ×6 in 5 seats,
  чеснок ×1, and проказа at 5:110 (an exact GiellaLT lemma whose
  own definition is the contagious skin disease; seated at the
  leper seat in remediation).
- D3: capitalisation of divine pronouns and epithet participles
  (Минь, Сон, Содыця, Простиця) mid-sentence goes beyond the
  build spec's letter; the practice is consistent through the
  book and is disclosed here.
- D4: the Master's Latin vocative "O" is carried ×40 with names
  under the names policy, while Erzya vocative practice (Эй, /
  Cyrillic О) appears elsewhere; the inconsistency is disclosed.

## Checker history

- First independent checker (CHECKER-REPORT-MYV-2026-11-27.md):
  FAIL — canonical PASS, clause fidelity PASS with isolated
  failures; attestation FAIL on знярдо ×318 (a form the build
  spec forbade by name), GAP honesty FAIL at 7:166, orthography
  FAIL at 48:29, retained English "the" in 5 seats.
- Remediation (REMEDIATION-LOG-MYV-2026-11-27.md): знярдо → зярдо
  at all 318 occurrences; 7:166 GAPped; 48:29 repaired; "the"
  dropped at all 8 occurrences; clause repairs at 27:19, 5:110,
  65:4, 31:25, 22:5; disclosures D1–D4 written.
- Independent re-check (CHECKER-REPORT-RECHECK-MYV-2026-11-27.md):
  every remediation claim verified, all 12 repaired seats PASS,
  fresh 24-verse clause sample PASS — but FAIL on one new finding:
  13 Cyrillic–Latin homoglyph-mixed tokens in 12 seats, found by
  a codepoint-level sweep.
- Homoglyph repair (remediation log, Repair 6): all 13 tokens
  normalised to pure Cyrillic on attested stems; codepoint sweep
  clean (0 mixed tokens outside the names-policy hyphenated forms
  and the 5:60 GAP-suffix token).
- Final delta re-check: CHECKER-REPORT-DELTA-MYV-2026-11-27.md.
