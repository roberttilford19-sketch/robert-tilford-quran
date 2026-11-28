# FLAGS AND GAPS — Chukchi (ckt) draft

Status of the book: DRAFT — NOT PUBLISHED, shelved under the tier
PASS-WITH-GAP-TIER-RESERVATION (independent checker, round 2,
2026-11-28). This file is the book's gaps disclosure; it travels with
the book.

## GAP census (machine-counted, reconciled by verify.py and by the
## checker's independent recomputation — identical figures)

- Verses carrying at least one ⟦GAP: …⟧ marker: **6,218 of 6,236**
- GAP markers in total: **67,251**
- Distinct English terms gapped: **5,807**
- Verses fully seated: **18**
- Seat dictionary: **451 English keys**, every seat verified against
  the attestation inventory; unverified and remediated seats logged
  in work/unverified-dict.json (lane record).

## What is GAP, by class

- **Core religious vocabulary (audited seat by seat before the
  build):** prophet, prayer/pray, fasting, alms, pilgrimage,
  revelation, mercy/merciful/beneficent, judgment, paradise, hell,
  angel, scripture, book, heaven/sky, soul, sin, forgive, worship,
  believe, create, king, slave, mosque, temple, priest, law,
  covenant, sign, miracle, reward, punish, truth, life. The Basmalah
  itself carries two GAPs (beneficent, merciful) at 1:1, 1:3 and all
  112 unnumbered lines.
- **Agricultural register — all GAP**, exactly as the IBT
  translator's record (Desnitsky 2018) predicts for a land without
  agriculture: sow, seed, reaping, harvest, garden, fruit, bread,
  and their kin. No agricultural term was coined.
- **Function words unattested in the harvested open record:** of, to,
  for, from, who, will/would, do/did, say/said, when, but, so, then,
  which, among, before, nor, except, only, know, and others. The
  conjunctions the record does attest are seated (and ынкъам, or
  эвытԓым, if эвыр, not/no уйӈэ).
- **Epithets and titles** (Knower, Forgiver, Hereafter, Paradise as a
  common noun, and the rest of the purged list): these do not ride
  the names allowlist under the BUILD-SPEC policy and GAP where no
  attested seat exists.

## Known wrinkles, disclosed

- Oblique pronouns ride the attested paradigm forms (me = гым, them
  = ыргынан, and so on); case is carried by context, not by form.
- "God" and lower-case "god" are both seated with the control's
  God-word Тэнантомгыӈэн; no distinct attested seat for "a god"
  exists in the harvested record.
- The rainbow seat keeps its source's қ (U+049B) where its ӈ-twin is
  spelled with ӄ (U+04C4) — a dictionary-only residual found by the
  round-2 checker; the seat never fires in the built text.
- The ң→ӈ normalisation log (work/ng-normalised-seats.json)
  over-includes four alternate-headword seat calls beyond the five
  seats that reached the text; the five are named in PREBUILD §5.
- One seat (гымнин, "my/mine") rests on a lesson-title citation
  recorded at sources/fieldasr-lesson-titles.md; the round-1 checker
  graded it WEAK on that ground and the citation stands as recorded.
- The full IBT Luke text was not machine-harvested (publisher's
  e-book page script-driven; app download and two mirror roads
  failed or were blocked). The control was used as fact and citation
  from the brief's verified record plus ten dictionary-quoted IBT
  sentences. No seat rests on an unharvested source.

## Fences verified by the independent checker (both rounds)

- Refusal list: complete — no fenced term seated, round 1 and
  round 2.
- Norm fence: no Telqep (Dunn), southern, Koryak, Amguema
  (Chuklang), or Salminen seat; no women's ц-variant anywhere
  (count 0 in dictionary and text).
- Codepoint integrity, machine counts on the built text: U+052F = 0,
  U+0027 = 0, U+2019 = 0, U+04A3 = 0, U+2018 = 0.
