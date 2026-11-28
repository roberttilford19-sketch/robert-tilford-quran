# Komi-Zyrian lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-KOMI-ZYRIAN.md (conditions
settled by Robert Tilford's ruling of 2026-11-27, 21:16 CST — the
nightly board ruling adopting the desk's recommendations; the
open-in-order queue Lule Sámi, Erzya, Udmurt, Moksha, Meadow Mari,
**Komi-Zyrian**, Komi-Permyak, Chuvash, Southern Sámi, Võro, North
Frisian — the lanes before Komi-Zyrian have all landed),
LICENCES-RECORDED-2026-11-28.md, ATTESTATION-AUDIT-2026-11-28.md.
Master of record: the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
MD5 ecc5b8e2848e5044186b7ad82bed9f4e); verse texts in
~/workspace/ayah-komi-zyrian/master-verses.json (114 surahs,
6,236 verses, verified against the Master; identical copy to the
Erzya/Udmurt/Moksha/Meadow Mari lanes).

## Orthography and base (FIXED, per brief §8 condition 1)
- Norm: the modern Komi-Zyrian literary standard, Cyrillic script
  (the Russian alphabet plus І/і and Ӧ/ӧ, 35 letters), based on
  the Syktyvkar (Prisyktyvkarsky / Sysola) dialect, in the norm
  of the GiellaLT `kpv` resources and the New Testament control.
  Komi-Zyrian ONLY, ISO kpv.
- KOMI-PERMYAK BAR: Komi-Permyak (koi) and Komi-Yazva forms are
  NEVER seated. The two standards share the alphabet, so the
  fence is attestation-based: a form seats only if it traces to a
  `kpv` inventory held at the desk (GiellaLT giella-kpv stem
  files; English Wiktionary Komi-Zyrian entries via kaikki).
  Udmurt (udm), Erzya (myv), Moksha (mdf), Mari, Tatar, and
  Russian forms are never seated except where the form itself
  stands in the harvested kpv inventories (flagged loans in the
  glossary).
- Do NOT run Komi-Zyrian text through a Russian spellchecker;
  І must never be normalised to И.
- Capitalisation: sentence-initial and proper names only, plus
  Ен "God" and Мезӧс "the Lord" where the Master capitalises.

## Base and honesty
- Base named on the book's face: modern literary Komi-Zyrian
  built on the attested lexical base in the attestation audit —
  GiellaLT giella-kpv (LGPL v3) and the Wiktionary/kaikki harvest
  (CC BY-SA) as attestation sources; the Lytkin dictionary
  tradition, the FU-Lab and web corpora, and the New Testament
  (2008, Institute for Bible Translation, Finland) as controls by
  FACT AND CITATION ONLY (in copyright; their wording is never
  reproduced). The unverified status of the Коми Библия 2023
  complete-Bible record (brief §4/§8 condition 3 — indicated by
  directory listings, not verified book-by-book) is disclosed on
  the book's face; the verified control is the complete New
  Testament (2008).
- No "first translation" claim anywhere (brief §5: NOT FOUND in
  the searched sources, with the NabiMuhammad.com "Komi коми"
  aggregator listing unresolved — a bounded result, not proof;
  brief §8 condition 7's Russian-language and catalogue pass not
  run, so no novelty wording).
- BUILD TIER, stated plainly: this is a first-pass,
  engine-rendered draft. Every verse seat is filled, seat by
  seat, from the verified dictionary; every Master content word
  with no verified seat carries the visible GAP marker rather
  than an invented or borrowed form. The GAP census is large
  (see the flags-and-gaps disclosure) and is disclosed on the
  book's face. The draft stops before landing and before any
  independent check.

## Names policy
Personal names and scripture titles are carried in the Master's
forms (Moses, Jesus, Mary, Abraham, Noah, the Torah, the Gospel,
the Psalms, the Quran…), unaltered. A capitalised Master word
counts as a name only if it never occurs lowercased in the
Master. The disjointed letters at surah heads are carried as in
the Master ("Alif, Lam, Meem.").

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line.
Seated form (fixed for the whole book):
**Енлӧн нимӧн, Милӧсьт, Милӧсьт.**
("In the name of God, the Merciful, the Merciful." Both mercy
names rest on the one attested mercy stem милӧсьт — and that
single-stem seating is disclosed on the book's face and in the
glossary. Verse 1:3 is the same two names without the frame:
"Милӧсьт, Милӧсьт.")

## GAP policy
A seat that cannot be carried on attested forms takes the
visible marker ⟦GAP: <english term>⟧ inline, the rest of the
verse rendered as far as attested forms allow. NEVER invent a
form; NEVER borrow silently from Komi-Permyak, Komi-Yazva,
Udmurt, Erzya, Moksha, Mari, Tatar, or Russian. Russian-shaped
loans already in the attested kpv inventory (ангел, пророк, рай,
ад, храм, трон, жертва, идол, джинн, религия, факт…) are seated
only as flagged in the audit.

## Grammar reference (the norm every batch follows)
Komi-Zyrian is agglutinative, SOV-leaning, with no articles and
no grammatical gender. This first-pass draft follows a disclosed
plain style, kept close to the Master, clause by clause:
- Pronouns: ме (I), тэ (you sg), сійӧ (he/she/it), ми (we),
  ті (you pl, seated тэ by the plain device), найӧ (they);
  oblique stems мен-, миян-, сы-, на- per the paradigm.
- "God" seats: Ен (nom), Енлӧн (gen, "of God"), Енлы (dat),
  Енӧс (acc), Енын (iness), Енысь (elat).
- Noun cases (regular paradigm, disclosed): nom -Ø; gen -лӧн;
  acc -ӧс; dat -лы; iness -ын; elat -ысь; illat -ӧ; plural
  -яс/-ъяс (regular Komi plural suffix). The plural suffix
  seats wherever the Master has a plural, consistently.
- Adjectives do not agree; they precede the noun unchanged:
  бур (good), лёк (bad/evil), ыджыд (big/great), ичӧт (small),
  выль (new), важ (old), збыль (true), веськыд (straight/just),
  вежа (holy), югыд (bright), пемыд (dark), сьӧд (black),
  еджыд (white), гӧрд (red), кокни (light/easy), сьӧкыд (heavy).
- Verbs seat in the infinitive's 3rd-person present form
  (stem + ӧ; irregulars овны→олӧ, кувны→кулӧ, воны→воӧ,
  лоны→лоӧ, локны→локтӧ, кывны→кылӧ, аддзыны→аддзӧ) — a
  disclosed plain-style device: person and tense are carried by
  the subject and by time words, exactly as the sibling lanes
  disclose their plain-style devices. The copula seats ride
  лоны. "Will/shall" seats ride the same present form.
- Negation: **оз** + verb stem (the attested Komi negative
  auxiliary construction), logged as a device. Existential
  "there is not / no" seats ride **абу**.
- "Say:" introducing speech — Шуӧ: with the Master's quotation
  marks (“ ”) kept.
- Numbers as in the Master (words where the Master has words):
  ӧти (1), кык (2), куим (3), нёль (4), вит (5), квайт (6),
  сизим (7), кӧкъямыс (8), ӧкмыс (9), дас (10), кызь (20),
  сё (100), сюрс (1000). All are inventory lemmas.
- Every seated lemma MUST trace to the harvested inventories
  (sources/giella-lemmas-full.json, kaikki headwords or kaikki
  declined forms) or to a disclosed regular derivation of one
  (plural, case, present-tense, agent -ысь/-лысь, abstract
  -лун/-ӧм formations); an untraced word does not seat — it
  takes the GAP marker and is logged in the batch notes.

## Style
- Plain, close rendering of the Master, sentence by sentence.
  The Master's verse is the unit; do not merge or split verses.
- FIDELITY PROTOCOL (the Veps lesson, binding): every clause of
  the Master must be carried — every content word (nouns, verbs,
  adjectives, numbers, names, negations, conditions) carried by
  Komi-Zyrian, by a glossary device, or by a logged GAP.
  Pronouns may never stand in place of dropped content words.
  For verses over 25 Master words, the batch notes record the
  long-verse check.
- The two Master seats carrying a literal "<redacted>"
  placeholder (39:7, 48:8) are rendered for their surrounding
  sense; the string "redacted" never appears in the Komi text.

## Output format
Batch files: ~/workspace/ayah-komi-zyrian/work/batch-<X>.json,
{"S:V": "Komi-Zyrian text"} — plain UTF-8 JSON, EVERY seat in
the batch's master-<X>.json, no seat omitted, no seat added.
Each batch ships with work/notes-<X>.md logging: every GAP seat,
every GAP term with its count, the flagged constructions, and
the fidelity self-check record for the batch's long verses.
The rendering engine is work/build_engine.py, driven by the
verified dictionaries work/dict_core.py, work/dict_nouns.py and
work/dict_verbs.py; dropped unverified entries are logged at
work/unverified-dict.json.
