# Flags and Gaps Disclosure — Moksha (mdf) Quran

Status: DRAFT — NOT PUBLISHED. Built under Robert Tilford's ruling
of 2026-11-27 (21:16 CST, OPEN-IN-ORDER QUEUE — Lule Sámi, Erzya,
Udmurt, Moksha, …; Lule Sámi and Erzya landed, Udmurt in
remediation, Moksha next), under the Pipeline Landing Authorization
(2026-11-14). This build has NOT been landed, shelved, committed,
or pushed. It awaits an independent checker (a fresh agent who
built none of it) before any landing.

## Counts, in the same breath

Complete rendering: 6,236 of 6,236 verses; seat-set equality with
the Locked English Master exact; per-surah grid clean at all 114
surahs; 6,179 rendered in full; 57 verses carry one or more visible
⟦GAP: …⟧ markers — 67 markers in all: jinn 31, pilgrimage 16,
usury 8, Sabbath 7, apes 2, gnat 1, cucumber 1, fig 1. Standing GAP
terms (attestation audit): jinn, pilgrimage as a term, the Sabbath
as an institution, and usury are never invented and never silently
borrowed; the single-term GAPs (apes, gnat, cucumber, fig) are
seats where no attested Moksha form was found for that item.
GAP seats: 2:26, 2:61, 2:65, 2:158, 2:189, 2:196, 2:197, 2:275,
2:276, 2:278, 3:97, 3:130, 4:47, 4:154, 4:161, 5:1, 5:2, 5:60,
5:95, 5:96, 6:100, 6:112, 6:128, 6:130, 7:38, 7:163, 7:179, 9:3,
9:19, 11:119, 15:27, 16:124, 17:88, 18:50, 22:27, 27:17, 27:39,
28:31, 30:39, 32:13, 34:41, 37:158, 41:25, 41:29, 46:18, 46:29,
51:56, 55:15, 55:33, 55:39, 55:56, 55:74, 72:1, 72:5, 72:6, 95:1,
114:6.

## Base

Modern literary Moksha (ISO 639-3 mdf), Cyrillic with spelling
rules identical to those of Russian (33-letter alphabet, no
additional letters), Central-dialect-based in its ä-retaining
Krasnoslobodsk form. Moksha only — no Erzya (myv) form is seated,
and no Erzya–Moksha MT output was used as a drafting base.
Attestation base: GiellaLT giella-mdf (LGPL v3) and the English
Wiktionary Moksha harvest via kaikki.org (CC BY-SA); the 2016
Moksha New Testament and the modern dictionaries are controls by
fact and citation only, their wording never reproduced. The Bible
control is narrower than Erzya's — New Testament (2016) only; no
complete Bible and no named modern Old Testament portion found —
and that is disclosed on the book's face. No first-translation
claim is made anywhere in the book.

## Mechanical verification (verify.py, this build)

- Store seats 6,236 = master seats 6,236, sets equal: True.
- Per-surah mismatches: NONE. Empty seats: NONE.
- 1:1 equals the fixed Basmalah exactly: Шкаень лемса,
  Милостивай, Милостивай.
- The string "redacted" appears in no seat (the Master's
  placeholder seats — 39:7, 48:8 per the spec, and 33:45, 35:24,
  11:2, 12:96, 17:105 as they stand in the lane master copies —
  were rendered for their surrounding sense).
- ERZYA-BAR screen: zero whole-token seats of паз, чи, кедь,
  теште, кинига, казне, пежеть, шайтян, пророк, баславамс,
  седеймариця in the finished book.
- Purple-style token screen: 9,923 distinct Cyrillic tokens;
  4,955 untraced candidates — a CANDIDATE list for the independent
  checker, not a verdict (the Erzya lane's screen likewise
  returned 3,038 candidates at its build stage). The bulk are
  paradigm forms the decomposition screen cannot resolve (short
  stems such as азомс: азсь, азыхть, азьк; possessive/definite
  chains such as менельхнень, тевснон). High-frequency candidates
  the checker must settle first are named in the next section.
- Retained-Latin candidates: 13 distinct tokens, mostly fragments
  (ze, na, onte, nte, ade, ke) plus manna and Bedouin — for the
  checker's seat-by-seat review against the names policy.

## Open items carried to the independent checker (from batch notes)

1. **што / штоба** (untraced, ~348 / ~275 tokens): Russian-shaped
   conjunctions seated by several batches; batch D eliminated
   them, others did not. Not verified in the mdf inventory.
2. **мельга / мельге** (~48 мельга tokens): the spec's follow
   device is молемс … кинц эзга; batches B (6:153) and F (22:3,
   22:4, 23:44, 23:71, 24:21, 25:8) seated мельга forms, batch H
   reports мельге as an inventory lemma, batches I/K/L/M held
   the spec line. The checker must settle мельге's attestation
   and regularise the follow seats one way.
3. **иля / иляда prohibitive** (batch D, passim in command
   speeches): the spec prescribed аф + 2pl present; batch D kept
   иля for readability and disclosed it as a deviation that
   converts mechanically if barred.
4. **эли** (~127 tokens): the spec seated "or" only conditionally;
   the checker must verify its inventory standing.
5. **канд- forms** (batch C: 7:106, 9:92, 10:24): кандомс was not
   a seated lemma in the spec; logged by the batch as a deviation
   risk (максомс/молемс phrasing is the spec road).
6. **казнефт participles** (batch H: 34:35, 37:59): regular
   formations on the flagged Moksha loan казня (punishment) —
   not the barred Erzya noun казне, but flagged for confirmation.
7. **4:23** (batch B): the clause "the wives of your genetic
   sons" is compressed; flagged by the batch as its weakest seat.
8. **кда** (~865 tokens): the "when/if" conjunction seated by the
   BUILD-SPEC's own relative-clause note; untraced by the screen
   because it is a function word, carried here for the checker's
   confirmation against the inventory.
9. Descriptive devices beyond the glossary's flagged list, each
   logged in its batch notes (hypocrites devices in batches C/H/J,
   "Desert-Arabs" in C, earthworm in H, lion/crystal/pearls/olives
   phrasings in L, fig/olive phrasings in M, and similar).

## Flagged seats and devices (glossary §G, attestation audit)

- Basmalah: both mercy names rest on the one attested stem
  милостивай — Шкаень лемса, Милостивай, Милостивай.
- Descriptive devices, disclosed: Шкаень кучф (prophet/messenger),
  Судонь ши (Day of Judgement), Ине Вайме (Holy Spirit), Шкаень
  няфтема (revelation), виде ки (straight path), азор васта
  (throne), азор phrasing (kingdom), максомс phrasing (zakāh — no
  rate ever stated; reward), вельмомс Шкайнди (repent), молемс
  сонь кинц эзга (follow), кеми / аф кеми (believer/disbeliever),
  берянь вайме (devil), озкс куд (temple).
- Attested loans, flagged: рай, пост, ангел, книга, мир, грех,
  сатана, ад, враг, корабль, война, верблюд, золота, союз,
  казня, свидетель, король, молитва, поп/бачка.
- Regular formations flagged: бславама, вельмома, прощандама
  family.
- Thin seats flagged in the audit: дива (miracle), надияфтома
  (promise), варама (oath), мудрайши (wisdom), озкс (sacrifice —
  the traditional Moksha prayer feast).
