# Chukchi (ckt) Quran lane — INDEPENDENT CHECKER REPORT, ROUND 2 (2026-11-28)

Checker: independent re-checker (round 2; did none of the build and none
of the round-1 check). Method: round-1 report, PREBUILD-VERIFICATIONS.md
§5 (remediation addendum), BUILD-SPEC.md, ATTESTATION-AUDIT-2026-11-28.md
and LICENCES-RECORDED-2026-11-28.md read; verify.py re-run firsthand;
every numbered finding re-verified in the checker's own scripts against
verses-store.json, work/eng2ckt.json (451 keys), work/allowlist-purged.json,
work/ng-normalised-seats.json, work/gap-census.json, master-verses.json and
the files in sources/. No build file was edited. No git command was run.

One record note: the round-1 report file on disk truncates mid-§E (it ends
with a literal truncation marker; its later sections are not in the saved
file). The findings re-checked here are the ones enumerated in the tasking
and in §§A–E as saved, which cover every defect the remediation answers.

## VERDICT: PASS-WITH-GAP-TIER-RESERVATION — DRAFT — NOT PUBLISHED

Ground in one breath: every round-1 correctness defect is verified
repaired firsthand (the FALSE ethnonym seat is gone and GAPs, the
letterform breach is at zero, the allowlist is purged to the BUILD-SPEC
names policy, the sun seat is decapitalised, the stray U+2018 is gone),
the refusal list still holds completely, a fresh 15-seat attestation
sample grades 15 VERIFIED / 0 WEAK / 0 FALSE, and the GAP census
reconciles three ways (verify.py, the census file, and this checker's
own recomputation: 6,218 GAP seats of 6,236 verses, 67,251 markers,
5,807 distinct GAP terms, 451 dictionary keys, 18 fully seated verses).
What remains is thinness alone — a quantity, disclosed by the markers
themselves in every affected verse — not a correctness defect. The
reservation that carries this book must state that census plainly, in
the same breath as the pass.

---

## 1. even → ӄаарамкын (round-1 FALSE seat) — REPAIRED, verified

- `even` is not a key in work/eng2ckt.json.
- ӄаарамкын occurs **0 times** in verses-store.json and in no seat in
  eng2ckt.json.
- `even` now GAPs: ⟦GAP: even⟧ ×103 in the built text. At 24:35 the
  verse reads "…⟦GAP: illuminate⟧ ⟦GAP: even⟧ эвыр уйӈэ йынйын рытык
  ⟦GAP: touched⟧ ытлён…" — the Even-people ethnonym no longer stands
  where the Master means the adverb.

## 2. horse → мури and holiday → праздник — REPAIRED, verified

- Neither `horse` nor `holiday` is a key in eng2ckt.json.
- мури seats only `we` and `us` (the IBT Luke 5:5 pronoun, as the audit
  records); `horse` GAPs (⟦GAP: horse⟧ ×1).
- праздник occurs 0 times in the built text and in no seat.

## 3. U+04A3 letterform breach — REPAIRED, with two minor residuals noted

- Own recount on the built text (verses-store.json and quran-ckt.txt):
  **U+04A3 = 0**.
- The five affected seats now carry U+04C8 spellings, each exactly the
  source form with ң→ӈ applied: plant тыӈэчьын (×11 in text), rope
  танӈыӈэлгын (×7), winter льэлеӈ (×1), rainbow йыӈэттэтқымчучьын (×0),
  hunter гынниӈӈыттыльын (×0).
- Attestation of the ӈ spellings in sources/, checked headword by
  headword in sources/ruwikt-ckt-entries.json: plant's twin тыӈэчьын
  stands as its own headword (gloss растение) and in the en pair list;
  winter's twin льэлеӈ stands as its own headword (gloss зима);
  rainbow has an attested twin йыӈэттэтӄымчучьын (gloss радуга) — see
  residual (a); rope and hunter have no separate ӈ twin headword in the
  harvested record — their seats are the disclosed ң→ӈ normalisation of
  the attested source forms танңыңэлгын / гынниңңыттыльын themselves,
  of the same disclosed class as the §2 apostrophe normalisation.
- Disclosure: PREBUILD §5 records the normalisation in words, and
  work/ng-normalised-seats.json logs it seat by seat — all five seated
  source forms are present with the correct U+04A3 spellings. The log
  also carries four further entries (answer татлың, duck эмңээм,
  building яраңы, rope ңилгын) that are alternate source headwords
  normalised at inventory level, not the seats carried under those keys
  (answer seats очынʼатгыргын, duck ачьэқ, building выквыран; ңилгын's
  ӈ twin seats `belt`). The log is therefore over-inclusive and its key
  labels are approximate — recorded here as a disclosure imperfection,
  not a concealment: no seated normalised form is missing from it.
- Residual (a), dictionary-level only: the rainbow seat keeps the source
  form's қ (U+049B) where the attested twin йыӈэттэтӄымчучьын carries
  ӄ (U+04C4). The seat never fires (0 occurrences in the built text),
  so no wrong letter reaches a reader; the seat should be conformed to
  the twin at the next dictionary pass.

## 4. Names allowlist — REPAIRED, verified

- Own recount, GAP markers stripped: **127 distinct Latin types,
  1,093 tokens** retained in the built text (round 1: 244 types,
  1,889 tokens). Every retained type is on work/names-allowlist.json
  (131 types); off-allowlist types: **none**. Purged list: 117 types,
  with zero overlap against the keep list.
- Purged sample of 15, each confirmed absent from the allowlist, at
  0 retained tokens, and GAPping in the census (lowercase GAP-term
  counts): Hereafter (101), Knower (35), Paradise (34), Yes (21),
  Temple (1), Forgiver (16), Benevolent (2), Omniscient (8),
  Accepter (3), Books (3), Chamber (1), Deluge (1), Hellfire (2),
  Patriarchs (4) — and **O**: 0 retained tokens; the vocative is
  dropped by the article rule, as BUILD-SPEC always provided, and
  does not GAP (it is not a content word).
- Kept sample of 15, each confirmed on the allowlist and present as a
  genuine proper name in master-verses.json, with retained counts in
  the built text matching or one below the Master count (the shortfall
  is the dropped vocative/article contexts): Aaron 20/20, Abraham
  67/69, Adam 24/25, Ahmad 1/1, Azar 1/1, David 16/16, Elijah 2/2,
  Gabriel 3/3, Hud 7/7, Isaac 17/17, Jacob 16/16, Jesus 25/25,
  Mary 33/34, Moses 136/136, Noah 43/43 (built/Master).

## 5. sun — REPAIRED, verified

- The seat is lowercase **тиркытир** (ground: en.wikt pair 'Sun').
- It appears lowercase mid-verse: 6:96 "…ынкъам тиркытир ынкъам
  йъиԓгын…" and 18:17 "…рытык ⟦GAP: seen⟧ тиркытир ⟦GAP: when⟧…".
  Lowercase count in text: 31.
- The only capitalised Тиркытир occurrences (2) stand at verse-initial
  position (36:40, 55:5), which is the BUILD-SPEC capitalisation rule,
  not the seat's shape.
- The only capitalised seat in eng2ckt.json is the God-word
  (god → Тэнантомгыӈэн). Confirmed by scanning all 451 seats.

## 6. GAP hygiene — REPAIRED, verified

- **U+2018 = 0** in the built text (round 1 found one at 12:9). Verse
  12:9 now carries ⟦GAP: fathers⟧ with no stray quote shape anywhere.

## 7. verify.py and independent recomputation — PASS, reconciled

- verify.py re-run firsthand: exit 0, all 23 checks PASS, including the
  two checks round 1 found missing (U+04A3 = 0, U+2018 = 0). Its final
  line: "GAP census: 6218 seats; 67251 markers; 5807 distinct terms /
  VERDICT: PASS".
- Checker's own recomputation from verses-store.json: GAP seats
  **6,218**, markers **67,251**, distinct GAP terms **5,807**, total
  verses 6,236, fully seated verses **18** — identical to verify.py
  and to work/gap-census.json. (Fully seated verses fell from round
  1's 27 to 18 because verses formerly "complete" only through retained
  epithet Latin now honestly GAP; that is the purge working, not a
  regression.)
- Codepoint counts, checker's own, on the built text: U+052F **0**,
  U+0027 **0**, U+2019 **0**, U+04A3 **0**, U+2018 **0**; present as
  required: ԓ U+0513 1,825; ӄ U+04C4 4,219; ӈ U+04C8 6,782;
  ʼ U+02BC 838.

## 8. Spot-check: remediation broke nothing else — PASS

- Refusal list re-checked seat by seat against eng2ckt.json: prophet,
  prayer/pray, angel, book, sky, soul, sin, believe, create, king,
  life, and the extended set (mercy, merciful, fasting, alms,
  pilgrimage, revelation, covenant, temple, mosque, priest, law,
  judgment, paradise, hell) — **none seated**. The agricultural set
  (sow, sowing, seed, reap, reaping, harvest, garden, fruit, bread,
  sower) — **none seated**.
- Basmalah 1:1 exact: "Нынны та Тэнантомгыӈэн, ⟦GAP: beneficent⟧,
  ⟦GAP: merciful⟧." — matches BUILD-SPEC character for character.
- Seat-set equality: the store's seat set equals the Master's 6,236
  seats exactly (recomputed independently, and verify.py checks 1–4).

## 9. Fresh attestation sample — 15 seats not in the round-1 sample

Each ground verified firsthand in sources/ (form present in the cited
source with the cited gloss, under the disclosed normalisations):

| Seat | Form | Ground as verified |
|---|---|---|
| envy | ваннатгыргын | ru entry, gloss зависть |
| rain | илиил | en entry gloss 'rain'; ru дождь |
| food | роолӄыл | ru entry, gloss еда, пища |
| meat | тэкичгын | ru entry, gloss мясо |
| egg | ԓигԓиг | ru entry, gloss яйцо (with IBT Luke 11:12 example) |
| milk | лывээръын | ru entry, gloss молоко |
| house | яраӈы | en entry gloss 'house'; ru дом |
| belt | ӈилгын | ru entry ӈилгын, gloss ремень (its ң homograph glosses верёвка — the two entries stand separate in the source) |
| duck | ачьэқ | ru entry, gloss утка |
| building | выквыран | ru entry, gloss здание |
| other | ӄол | ru entry, gloss другой |
| what | ръэнут | en entry gloss 'what, something' |
| father | ытԓыгын | en entry gloss 'father' |
| mother | ытԓьа | en entry gloss 'mother'; ru мать |
| walrus | рыркы | en pair 'walrus' (first-listed of two); ru морж |

**Tally: VERIFIED 15 / WEAK 0 / FALSE 0.** Combined with round 1's
sample (56 VERIFIED / 7 WEAK / 1 FALSE, the FALSE and the
correctness-bearing WEAK seats now unseated or repaired), no seated
ground in either sample is fabricated.

## Tier judgment

Round 1's FAIL rested on two different kinds of ground, and they must
be separated. The correctness grounds — a FALSE seat printed 89 times,
a letterform breach, an allowlist carrying the very epithets the spec
forbids — were genuine blockers, and every one is now verified
repaired. The remaining ground is tier policy only: 67,251 GAP markers
against the Chuvash reservation's 23,456, with the tier-changing
remediation named as expanding the attested inventory to roughly
≤25,000 markers.

That remediation is not available under house law in this environment,
on the builder's own record (PREBUILD §5; LICENCES-RECORDED-2026-11-28):
the fuller dictionaries (Moll & Inenlikej 1957; Inenlikej 1976) and
Skorik's grammar are in copyright and may be used as fact and citation
only, never harvested as a seat base; the PanLex API was attempted and
is unreachable through the desk's network; the open record — both
Wiktionaries (CC BY-SA) plus the IBT control sentences — is what the
book lawfully stands on. A FAIL on this ground would not name a defect
the builder can lawfully fix; it would hold the lane failed for
declining to break the licence fence or for a network road that does
not exist here. That is not a correctness blocker, and dressing it as
one would misstate the record.

What the reservation exists for is exactly this case: a book whose
defects are repaired, whose gaps are honest, exactly counted, and
visible on its face — no reader can mistake a verse carrying ⟦GAP: …⟧
markers for a finished literary translation, and BUILD-SPEC says so in
words. The corrected book therefore lands as **DRAFT — NOT PUBLISHED
under PASS-WITH-GAP-TIER-RESERVATION**, the reservation stating the
census plainly: 6,218 of 6,236 verses carry GAP markers; 67,251
markers; 5,807 distinct GAP terms; 451 dictionary keys; 18 fully
seated verses. The two minor residuals (§3: the rainbow seat's U+049B,
which never reaches the text, and the ng log's over-inclusive key
labels) are recorded for the next dictionary pass and do not change
the verdict.
