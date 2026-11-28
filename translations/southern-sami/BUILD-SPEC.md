# Southern Sámi lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-SOUTHERN-SAMI.md (PASS-CANDIDATE;
admitted to the candidate queue 2026-11-27), settled for build by
Robert Tilford's ruling of 2026-11-27, 21:16 CST (open-in-order queue:
… Chuvash, Southern Sámi, Võro, North Frisian — Chuvash landed, so
this lane opens in order; no fresh ruling needed). Master of record:
the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
MD5 ecc5b8e2848e5044186b7ad82bed9f4e); verse texts in
~/workspace/ayah-southern-sami/master-verses.json (114 surahs,
6,236 verses, identical copy to the sibling lanes).

## Orthography and base (per brief §3 and §9 condition 2)
- Norm: the settled official Southern Sámi orthography in the
  NORWEGIAN spelling practice (⟨æ⟩, ⟨ø⟩, ⟨å⟩), per the brief's desk
  recommendation adopted in the queue ruling — matching the larger
  Norwegian speaker share and the 2024 New Testament's Norwegian
  Bible Society co-publication. The Swedish practice (⟨ä⟩, ⟨ö⟩) is
  recorded as preserved dissent in the working record.
- The difference is presentational, not phonological (brief §3):
  source forms seated with ⟨ä⟩/⟨ö⟩ are converted mechanically to
  ⟨æ⟩/⟨ø⟩. No other letter is altered. ⟨ï⟩ is kept as in the
  sources.
- Southern Sámi ONLY, ISO sma. Northern Sámi (sme) and Lule Sámi
  (smj) forms are NEVER seated; Skolt Sámi (sms) is permanently
  closed and is not touched in any way.

## Base and honesty
- BUILD TIER: first-pass, engine-rendered draft. Every verse seat
  is filled from the verified dictionary; every Master content word
  with no verified seat carries the visible GAP marker rather than
  an invented or borrowed form. The GAP census is disclosed on the
  book's face.
- Seat sources, licence-verified open only: (1) the English–South
  Saami Dictionary (2022), public domain by its authors' own
  statement; (2) GiellaLT lang-sma (GPL v3 or later) as the
  attestation inventory and morphology control. dict-sma-mul
  (CC BY 3.0, sma–nob/swe) supports the inventory only.
- Controls by FACT AND CITATION ONLY: Bergsland & Magga (1993),
  Magga (2009), Hasselbrink (1981–85), the SIKOR corpus texts, and
  the 2024 New Testament (Orre testamente) — licences unverified;
  their wording is never reproduced.
- No "first" wording anywhere (brief §6: no Southern Sámi Qur'an
  found in the searches named there — tier: not found, not proven
  non-existent; no bounded first-claim has been ruled, so none is
  printed).

## Names policy
Personal names and scripture titles are carried in the Master's
forms, against an explicit allowlist (work/names-allowlist.json).
A capitalised Master word counts as a name only if it stands on
that list; capitalised epithets are NOT names and never ride the
allowlist (the Komi-Zyrian checker lesson). The disjointed letters
at surah heads are carried as in the Master.

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line
(112 lines). Seated form (fixed for the whole book, citation-form
plain style, disclosed):
**Nomme Jupmele, Åårmegs, Åårmegs.**
("Name God, the Merciful, the Merciful" — nomme "name" and
åårmegs "merciful" and Jupmele "God (Christian)" all attested in
the 2022 public-domain dictionary; both mercy names rest on the
one attested adjective åårmegs, and that single-form seating is
disclosed on the book's face and in the glossary. Verse 1:3 is
the same two names without the frame: "Åårmegs, Åårmegs.")

## GAP policy
A seat that cannot be carried on attested forms takes the visible
marker ⟦GAP: <english term>⟧ inline, the rest of the verse
rendered as far as attested forms allow. NEVER invent a form;
NEVER borrow from Northern Sámi, Lule Sámi, Skolt Sámi, Norwegian,
Swedish, Finnish, or Russian.

## Grammar / plain-style devices (all disclosed)
- Verbs and nouns seat in the dictionary citation form; person,
  tense, case, and number are carried by the subject and by time
  words — the sibling lanes' disclosed plain-style device. No
  plural or case suffix is generated, because Southern Sámi case
  and plural formation involves stem changes (Umlaut) that a
  regular-suffix device cannot carry honestly.
- Pronouns seat in the GiellaLT-attested nominative forms:
  manne (I), datne (you sg), satne (he/she), mijjieh (we),
  dijjieh (you pl), sijjieh (they); oblique seats ride the same
  nominative forms under the plain-style device, disclosed here.
- Articles (the/a/an) and the vocative O are dropped; Southern
  Sámi has no articles.
- The two Master seats carrying a literal "<redacted>" placeholder
  (39:7, 48:8) are rendered for their surrounding sense; the string
  "redacted" never appears in the Southern Sámi text.

## Verification (verify.py)
Seat-set equality and per-surah grid (6,236/6,236); GAP census;
Basmalah checks; 'redacted' and empty-seat checks; token
attestation screen — every seated token must trace to the
GiellaLT lemma inventory, the 2022 dictionary's forms, or the
glossary; whitespace-token retained-English screen against the
explicit names allowlist (any other pure-English token is a
candidate — the Komi-Zyrian checker lesson, applied from the
start); mixed-script screen on whitespace tokens (tokens mixing
Latin with any other script are listed; NONE is the pass mark).
Instrument output is a candidate list for the fresh independent
checker, not a verdict.
