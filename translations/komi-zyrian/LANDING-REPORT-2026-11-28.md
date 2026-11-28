# Landing Report — Komi-Zyrian (kpv) Quran

**Landed: 2026-11-28, under the Pipeline Landing Authorization.**
**Status on the shelf: DRAFT — NOT PUBLISHED.**

## What landed

- `ayah-companion-manuscript-KPV.md` — the book in companion
  manuscript form: 6,236 verses on the standard grid. Its front
  matter carries DRAFT — NOT PUBLISHED on its face, names the
  language base honestly (modern literary Komi-Zyrian, коми кыв,
  ISO 639-3 kpv — the Syktyvkar-based literary standard, in
  Cyrillic, the Russian alphabet plus і and ӧ, fenced distinct
  from Komi-Permyak (koi); GiellaLT giella-kpv, LGPL v3, and the
  Komi-Zyrian lexicon of English Wiktionary, CC BY-SA, as
  attestation sources, with the Lytkin dictionary tradition, the
  FU-Lab and web corpora, and the modern Komi-Zyrian New
  Testament (2008) as controls by fact and citation only),
  discloses the build tier, the GAP policy, and the flagged
  seats, and states that no claim is made that this is the first
  Komi-Zyrian Quran translation.
- `quran-kpv.txt` and `quran-kpv.json` — the built book exactly
  as passed by the re-check. Recount at landing, from the lane
  files of record, verified by this landing desk's own count:
  all 6,236 verse texts stand verbatim in both the built text
  and the companion manuscript (0 missing from either).
- `glossary.md` — the attested vocabulary of record.
- `CHECKER-REPORT-INDEPENDENT-2026-11-28.md` — first independent
  checker: FAIL.
- `REMEDIATION-RECORD-2026-11-28.md` — every repair, seat by seat
  (1,176 seats changed against the preserved pre-remediation
  store).
- `CHECKER-REPORT-RECHECK-2026-11-28.md` — fresh independent
  re-check of the remediated text: PASS, with the reservations
  carried below.
- `FLAGS-AND-GAPS-DISCLOSURE-KPV-2026-11-28.md` — census,
  flagged constructions, and disclosures.
- `ATTESTATION-AUDIT-2026-11-28.md` — seat-by-seat attestation
  audit.
- `LICENCES-RECORDED-2026-11-28.md` and `BUILD-SPEC.md` — the
  licence record and the lane build spec of record.
- `MANIFEST.txt` — SHA-256 of every file above.

All copies in this folder were verified byte-identical to the
lane originals in `~/workspace/ayah-komi-zyrian/` at landing.

## Gate record

1. Machine count — PASS: 6,236 of 6,236 verses; seat-set exactly
   equal to the Locked English Master (no missing, no extra);
   per-surah grid exact at all 114 surahs (grid sum 6,236);
   `quran-kpv.json` flattens to 6,236 seats and is identical to
   the verse store at every seat; no empty seats; the string
   "redacted" appears in no seat. First verse 1:1 «Енлӧн нимӧн,
   Милӧсьт, Милӧсьт.»; last verse 114:6 «Ысь пӧвстын джинн и
   пӧвстын войтыр.”»
2. Canonical verify — PASS: 1:1 equals the BUILD-SPEC fixed
   Basmalah form «Енлӧн нимӧн, Милӧсьт, Милӧсьт.» character for
   character, and that full string occurs exactly once inside
   the verse store (at 1:1); in `quran-kpv.txt` it occurs
   exactly 113 times (112 standalone unnumbered lines plus the
   numbered verse 1:1, with surah 9 correctly carrying none);
   seat 1:3 reads «Милӧсьт, Милӧсьт.» — the spec form, verified
   character for character; seat 27:30 carries the in-verse
   Basmalah on the 1:1 seating.
3. Independent checker — FAIL (the retained-Latin tier standing
   silently beside the GAP markers, seat 1:3 off the spec form,
   the Sabbath / Hajj / Umrah / pilgrimage families retained in
   Latin, the five split core terms — angel, messenger, believe,
   sin, prayer — and the пышйӧ reflect defect at 24 seats, among
   the recorded findings), then remediation in full of every
   verified finding, then a fresh independent re-check: PASS —
   every headline figure in the remediation record recomputes
   exactly (1,176 seats changed; GAP census 5,042 / 13,714 /
   1,194 / 4,299), the retained-Latin tier is closed with 0
   types and 0 tokens off the audited allowlist (128 occurring
   pure Latin types, 1,046 pure Latin tokens, plus 6 disclosed
   mixed genitive-on-names device tokens, 1,052 Latin-bearing
   tokens in all; exactly those 6 mixed-script tokens exist in
   the book), the five core terms are unified, and all 24
   пышйӧ reflect seats are reseated on мӧвпав- forms with the
   12 genuine flee seats untouched.
4. Purple sweep — reconciled, candidates only under house law:
   the re-checker's own replication of the attestation screen
   returns exactly 6 untraced Cyrillic candidates — локтӧ ×441,
   кулӧ ×56, юяс ×52, лӧн ×6, прӧститысь ×16 and
   прӧститысьяс ×1 — and all six adjudicate as disclosed
   paradigm or device forms, not unattested seats; no other
   untraced Cyrillic token was found. Distinct Cyrillic tokens
   1,000; tokens containing ӧ 476; tokens containing і 13.
5. GAP census (post-remediation, recomputed by the re-checker
   and verified at landing by this desk's own count): 5,042
   GAP seats, 13,714 GAP markers, 1,194 verses without a
   marker, 4,299 distinct GAP terms; bracket integrity 13,714
   opening ⟦ and 13,714 closing ⟧, no malformed seat. (The
   companion manuscript carries 13,715 markers — the text's
   13,714 plus the front matter's explanatory example.)

## Reservations carried with the landing

These ride with the landing, as the checkers state them; none
is hidden, and the first is the ground on which the book lands
at all.

1. **The GAP-tier reservation — stated plainly.** This book is
   landed under the original checker's ruling
   PASS-WITH-GAP-TIER-RESERVATION, which the re-check does not
   reopen. 5,042 of the 6,236 seats are GAP-bearing and only
   1,194 verses are rendered in full (19.1% clean-verse share).
   It is a first-pass engine build over a 1,314-entry verified
   dictionary: the remediation closed the invisible retained
   tier by moving it into the visible GAP census, which is what
   the reservation required, and a future GAP-reduction pass —
   enlarging the seated dictionary — remains open as ordinary
   revision work. The book is DRAFT — NOT PUBLISHED.
2. **The lesser splits — a disclosed reservation that may ride,**
   as ruled in §8 of the re-check. Sea: море ×31 beside саридз
   (as саридзяс) ×4, the four саридз seats being exactly the
   "two seas" seats (25:53, 27:61, 35:12, 55:19). Mountain:
   гӧра (as гӧраяс) ×36 beside керӧс ×5 tokens at 4 seats
   (7:143, 7:171, 11:43, 59:21), the керӧс seats being the
   singular, specific "the mountain" seats and гӧраяс carrying
   the plural "mountains" seats. Temple / mosque: храм ×1
   beside мечеть ×20, the single храм seat being 17:7, where
   the Master says "the Temple", and every мечеть seat being a
   seat where the Master says Mosque / mosques — a pair that
   follows the Master's own wording. Both forms in each pair
   are attested inventory forms; the counts on the minority
   side are small (4, 5, and 1 tokens); each pair follows a
   discernible pattern rather than arbitrary alternation; and
   a future unification pass on these three pairs remains open
   as ordinary revision work — it is not a landing gate.

## Notes

- No PDF is included: the manuscript Markdown, the built text,
  and the built JSON are the landed forms, on the pattern of
  the Moksha and Meadow Mari landings.
