# BUILD RECORD — Tundra Nenets Quran lane, 2026-11-28

Opened by Robert Tilford's ruling of 2026-11-28 (tap + typed word,
on the desk's recommendation), adopting the conditions of
CANDIDATE-BRIEF-TUNDRA-NENETS.md as build law. His orthography
ruling, given with the opening: the two glottal-stop letters are
seated exactly as the standard literary orthography writes them —
ʼ (U+02BC) and ˮ (U+02EE) — fixed for the whole build, disclosed on
the book's face, never silently normalised. Working papers:
`~/workspace/ayah-tundra-nenets/` (BUILD-SPEC, glossary, attestation
audit, licences record, pre-build verifications, batch files and
notes, checker reports, remediation log).

## Pre-build verifications (all recorded in PREBUILD-VERIFICATIONS.md; sources accessed 2026-11-28)

1. **GiellaLT lang-yrk licence read in the repo:** the LICENSE file
   is the GNU LGPL v3 — operative. (The project web page's dual
   CC BY-SA / GPL statement is noted as differing.) 15,864 dictionary
   lemmas with paradigm classes extracted.
2. **INEL Nenets Corpus licence verified verbatim: CC BY-NC-SA 4.0.**
   The Tundra subset actually used: 56 texts / 6,545 sentences /
   37,681 tokens, identified per text by the corpus's own COMA
   metadata key "3a Variety" = Tundra.
3. **IBT Four Gospels and Acts opened itself:** *Тет Маймбабцо Юн /
   Ӈэдаравыˮ манзараˮмаˮ*, Москва 2025, signed to print 25.08.2025,
   print run 3,000, copyright line verbatim «© Институт перевода
   Библии, 2025», ISBN 978-5-93943-369-3. The edition nowhere prints
   "Tundra/тундровый"; its lect is Tundra by its endonym ненэцяʼ вада
   and its Yamal/Salekhard team, recorded exactly so. Published
   extent: portions 1995–2021 (Luke selections 1995; Stories about
   Jesus 2003; Luke 2004; John 1:1-17 2008; Mark 2010; John 2014;
   Matthew 2018; Gospel Parables 2020; Jonah diglot 2021) plus the
   Four Gospels and Acts 2025 (announced 2025-10-01, presented
   Salekhard 2025-10-15); in progress in IBT's words: "the Epistles
   and the book of Ruth."
4. **UDHR lect established from the text itself: Tundra** (OHCHR
   Moscow 2009 booklet, translator Raisa Yaptune; ненэця 17× / вада
   41×, нешаӈ вата 0×, frequent initial ӈ-). Its codepoints carry
   only ʼ U+02BC, sparingly — recorded as NOT an orthographic model
   for ˮ.
5. **Salminen glossary restriction recorded as it stands:** "Not to
   be distributed without permission" — consultation and
   fact-and-citation only; the desk holds no copy. All dictionaries
   and the grammar (Tereshchenko; Pyrerka & Tereshchenko; Lehtisalo;
   Burkova et al.; Nikolaeva; Salminen) are in copyright: fact and
   citation only, never the maker's wording. The Bible control is
   fact and citation only.

## Attestation audit

Seat-by-seat for the core religious vocabulary across the GiellaLT
data, the INEL Tundra subset, the UD treebank, the UDHR text, and
the Bible control as citation (ATTESTATION-AUDIT-2026-11-28.md).
Attested base: 30,953 distinct tokens (IBT ~14,600, INEL-Tundra
17,510, UDHR). A 37-item vocabulary attestation list was built from
the IBT edition's own glossary (Вадиˮ хамэдиˮ, pp. 486–521). Each
fixed seat's stratum (traditional / Orthodox / Russian-mediated /
disclosed device) is shown in the glossary. Unattested terms are
GAPs, never invented, never borrowed silently from Forest Nenets,
Enets, Nganasan, Khanty, or Russian.

## Build shape

- Master: fresh extraction from the Locked English Master
  (`ayah-companion-manuscript.md`, MD5 ecc5b8e2848e5044186b7ad82bed9f4e),
  grid-verified 6,236 verses, no missing or extra seats.
- Basmalah seated: "Нумʼ нимня, Сянаваʼ Ерв, Сянана."
- The first build wave was REJECTED as method (word-mapping scripts,
  lemma-form renderings; batches A and B preserved as REJECTED in
  the lane record). The rebuild was translator-first in ten batches
  A–J under a BUILD-SPEC method section; GAP seats by batch: A 16,
  B 25, C 5, D 6, E 6, F 13, G 5, H 18, I 4, J 3.

## Checker rounds and remediation

- **Checker 1 (independent) — FAIL** (CHECKER-REPORT-INDEPENDENT-
  2026-11-28.md): canonical, codepoints, GAP, paperwork PASS;
  fidelity FAIL confined to 7 verses; attestation FAIL on a named
  token set (маслина, осёл, жемчуг, коралл, рубин, гранат fruit
  sense, кувшин, намг- spellings); the "what" word n-initial at 199
  seats. Desk evidence work overturned the пын flag firsthand
  (пыда is the GiellaLT pronoun lemma; IBT attests oblique
  пынʼ/пынаˮ) and established олива as IBT-attested for 24:35.
- **Remediation round 1** (REMEDIATION-2026-11-28.md): 305 verses
  re-rendered clause-complete; condemned tokens replaced or GAPped;
  намг→ӈамг at 287 seats / 351 tokens; пын audit (72 → пыдар,
  26 → пынʼ, zero bare пын remain); Latin "Satan" → Сатана at 7
  further seats. Census 116 seats / 142 markers.
- **Re-check — FAIL, narrowed** (CHECKER-REPORT-RECHECK-2026-11-28.md):
  everything round 1 claimed verified genuinely fixed; fidelity
  FAIL on 223 batch-A verses still fragmentary at Master ≥12 words;
  золото condemned at 3 seats. Desk ruling: серебро GAPped with
  золото (attested only in INEL Russian free-translation tiers).
- **Remediation round 2:** 248 distinct verses re-rendered;
  золото → GAP ×3, серебро → GAP ×1; book-wide under-40% count at
  Master ≥12 words recomputed at 0. Census 119 seats / 146 markers.
- **Deciding check — FAIL on two confined items**
  (CHECKER-REPORT-DECIDING-2026-11-28.md): batch A fidelity PASS
  46/46; gold/silver PASS; GAP recount PASS; regression B–J PASS
  12/12; FAIL on тэӈгы (unattested connective, 54 occurrences) and
  on names policy (Мария 11 seats, Евангелие 7 seats). Desk
  re-search found no attestation for тэӈгы anywhere; the
  condemnation stands.
- **Remediation round 3:** тэӈгы cleared at 53 seats / 54
  occurrences (34 named seats plus 19 sentence-initial capitalised
  seats the deciding enumeration missed, reconciling exactly with
  the Purple count of 54; at 52 seats the word was removed with
  every content word kept, at 13:6 re-seated with ӈодˮ in its
  attested postpositive position); Марияʼ → Maryʼ at 11 seats;
  Евангелие → Gospel at 7 seats. Zero тэӈг anywhere afterward.
- **Final deciding check — PASS** (CHECKER-REPORT-FINAL-2026-11-28.md):
  all six gates PASS — mechanical (6,236 = 6,236, grid clean at all
  114, codepoints U+02BC 21,350 / U+02EE 48,644, forbidden three at
  zero, compression criterion book-wide 0), тэӈгы closure, names
  closure (24 name pairs swept, every Russian form zero), GAP
  recount 119/146, fresh fidelity sample 12/12 with a 26-token
  attestation band (none condemned), fences. Two loosenesses
  recorded without failing (12:18, 10:42); neither drops a content
  word.

## Outcome

6,236 verses, complete. GAP census 119 seats / 146 markers.
LANDED as DRAFT — NOT PUBLISHED under the Pipeline Landing
Authorization (2026-11-14), on the final deciding checker's PASS.
Manuscript: ayah-companion-manuscript-YRK.md — 1,348,369 bytes,
SHA-256 4d7537743bb4f8af3df617234743979cef62551f2d07b995fdd727a1108e5eb5.
No first-translation claim is made anywhere. No PDF (no PDF engine
installed); Markdown is the landed form. Silent build-and-gift:
no one was contacted.
