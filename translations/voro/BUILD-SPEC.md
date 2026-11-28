# Võro lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-VORO.md (in
~/workspace/goals/endangered-language-quran-translations/hidden_files/);
conditions settled by Robert Tilford's ruling of 2026-11-27, 21:16 CST
(the open-in-order queue … Southern Sámi, **Võro**, North Frisian —
Southern Sámi has landed, so this lane opens in order), with the
brief's two rulings settled on the desk's recommendations the same
day: R1 — the modern Võro literary standard (Võro Institute norm)
only, Seto, Mulgi and Tartu expressly out of scope; R2 — the archaic
South Estonian Bible (*Wastne Testament*, 1686) stands as historical
control / corroboration only, never as a source of modern forms;
modern attestation (synaq.org / Võro Institute dictionary as fact
and citation, GiellaLT analyser, modern corpora) satisfies the
source gate for religious vocabulary, with any term lacking modern
attestation held as a visible GAP.
Master of record: the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md);
verse texts in ~/workspace/ayah-voro/master-verses.json (114 surahs,
6,236 verses, verified against the Master; identical copy to the
sibling lanes).

## Orthography and base (FIXED)
- Norm: the modern Võro literary standard, Latin script, in the
  norm of the Võro Institute and the GiellaLT `vro` resources.
  Võro ONLY, ISO vro.
- SETO BAR: Seto forms are NEVER seated. A form seats only if it
  traces to a `vro` inventory held at the desk (GiellaLT lang-vro
  stem files, wordfreq corpus forms, English Wiktionary Võro
  entries via kaikki). Standard Estonian forms are never seated
  unless independently attested for Võro in those inventories.
- Palatalisation marks and archiphoneme symbols in the GiellaLT
  source files are normalised for the attestation screen
  (combining marks stripped, glottal `q` retained); the seated
  text uses plain modern Võro spelling as in the corpus forms.
- Capitalisation: sentence-initial and proper names only, plus
  Jumal "God" where the Master capitalises.

## Base and honesty
- Base named on the book's face: modern literary Võro built on
  the attested lexical base — GiellaLT lang-vro (LGPL v3) and the
  Wiktionary/kaikki harvest (CC BY-SA) as attestation sources; the
  Võro Institute dictionary (synaq.org; Iva 2002) and *Wastne
  Testament* (1686, public domain) as controls by FACT AND
  CITATION ONLY (the dictionary's wording is never reproduced).
- No modern Võro Bible was found (brief §4); that absence is
  disclosed on the book's face.
- "First" wording: none anywhere except the bounded form the
  brief establishes — "the first complete Võro Qur'an translation
  found — after research (27 November 2026)" — and even that only
  in the build report, not as a cover claim.
- BUILD TIER, stated plainly: this is a first-pass, engine-rendered
  draft. Every verse seat is filled, seat by seat, from the
  verified dictionary; every Master content word with no verified
  seat carries the visible GAP marker rather than an invented or
  borrowed form. The GAP census is disclosed on the book's face.
  The draft stops before landing and before any independent check.

## Names policy
Personal names and scripture titles are carried in the Master's
forms (Moses, Jesus, Mary, Abraham, Noah, the Torah, the Gospel,
the Psalms, the Quran…), unaltered. The disjointed letters at
surah heads are carried as in the Master ("Alif, Lam, Meem.").

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line.
Seated form (fixed for the whole book):
**Jumala nimeh, Arm, Arm.**
("In the name of God, the Merciful, the Merciful." Both mercy
names rest on the one attested mercy stem arm — and that
single-stem seating is disclosed on the book's face and in the
glossary. Verse 1:3 is the same two names without the frame:
"Arm, Arm.")

## GAP policy
A seat that cannot be carried on attested forms takes the visible
marker ⟦GAP: <english term>⟧ inline, the rest of the verse
rendered as far as attested forms allow. NEVER invent a form;
NEVER borrow silently from Seto, Mulgi, Tartu, or Standard
Estonian.

## Grammar reference (the norm every batch follows)
Võro is agglutinative, SVO-leaning, with no articles and no
grammatical gender. This first-pass draft follows a disclosed
plain style, kept close to the Master, clause by clause:
- Pronouns: maq (I), saq (you sg), tä (he/she), miq (we),
  tiq (you pl), nääq (they); oblique forms as attested.
- "God" seats: Jumal (nom), Jumala (gen, "of God").
- Articles (the / a / an) and the genitive linker "of" seat as
  zero — a disclosed plain-style device: Võro has no articles,
  and the genitive relation is carried by juxtaposition in this
  first-pass draft.
- Nouns seat in the nominative dictionary form; the plural seats
  wherever the Master has a plural, by the regular nominative
  plural suffix -q on the seated stem (disclosed regular
  derivation, screened in verify.py).
- Verbs seat in the dictionary (ma-infinitive) form — a disclosed
  plain-style device: person and tense are carried by the subject
  and by time words, exactly as the sibling lanes disclose their
  plain-style devices.
- Negation: **ei** + verb (the attested Võro negative).
- "Say:" introducing speech — Ütle: with the Master's quotation
  marks (“ ”) kept.
- Numbers as in the Master (words where the Master has words):
  üts (1), kats (2), kolm (3), neli (4), viis (5), kuus (6),
  säidse (7), katõssa (8), ütessä (9), kümme (10), säda (100),
  tuhat (1000). All are inventory forms.
- Every seated lemma MUST trace to the harvested inventories
  (sources/giella-lemmas.json, sources/wordfreq-forms.json,
  kaikki headwords/forms) or to a disclosed regular derivation
  of one (plural -q); an untraced word does not seat — it takes
  the GAP marker and is logged.

## Style
- Plain, close rendering of the Master, sentence by sentence.
  The Master's verse is the unit; do not merge or split verses.
- FIDELITY PROTOCOL (the Veps lesson, binding): every clause of
  the Master must be carried — every content word (nouns, verbs,
  adjectives, numbers, names, negations, conditions) carried by
  Võro, by a glossary device, or by a logged GAP.
- The two Master seats carrying a literal "<redacted>"
  placeholder (39:7, 48:8) are rendered for their surrounding
  sense; the string "redacted" never appears in the Võro text.

## Output format
verses-store.json: {"S:V": "Võro text"} — plain UTF-8 JSON,
EVERY seat in master-verses.json, no seat omitted, no seat added.
The rendering engine is work/build_engine.py, driven by the
verified dictionary work/dict_core.py; dropped unverified entries
are logged at work/unverified-dict.json. The build stops before
landing: no shelving, no commit, no push.
