# CHECKER REPORT — Friulian (fur) Quran lane

**Checker:** the lane coordinator (desk), who built none of the 6,236
verses (twelve batch crews built them; the desk's own hand touched
three single words before this pass: the 31:31 *dure* substitution,
made on a repair crew's recorded evidence). **Independence caveat,
stated in the same breath as the verdict:** the house pattern calls
for a fresh checker agent; subagent spawning closed mid-task
("subagent bootstrap is no longer authorized") after nineteen crews,
so this pass was executed by the desk on the full checker protocol.
The parent desk may re-run a fresh-agent pass before landing; nothing
in this report hides that. Model: the Veps lane's CHECKER-REPORT,
graded just as hard.

**Text graded:** `verses-store.json` (6,236 verses) against the
Locked English Master (`master-verses.json`, MD5
`ecc5b8e2848e5044186b7ad82bed9f4e`). Sources: `sources/` (Wiktionary
lexicon, Friulian Wikipedia corpus frequencies, Pirona 1871, Culòs
Matthew, wordlists). Batch paperwork: `work/notes-*.md`.

## Gate 1 — Canonical: PASS

- Seat-set equality 6,236 = 6,236 (verify.py); per-surah grid clean
  at all 114 surahs; no missing, no extra seats.
- Basmalah 1:1 exact: "Tal non di Diu, il Plen di misericordie, il
  Misericordiôs."
- The string "redacted" appears NOWHERE. The six Master seats
  carrying the Master's own literal `<redacted>` placeholder (11:2,
  12:96, 33:45, 35:24, 39:7, 48:8) are rendered for their surrounding
  sense; the truncated Master verse-ends (28:30, 28:31, 39:67) are
  rendered for all the sense the Master carries. These are defects
  of the Master of record, disclosed in the front matter lineage.

## Gate 2 — Fidelity spot-check: PASS

Method: clause-by-clause reading against the Master, weighted to
long verses, plus a mechanical length screen over all 3,835 verses
with Master text ≥15 words (median Friulian/Master word ratio
1.158; lowest 0.73 — no collapsed verse anywhere; the Veps failure
mode, content dropping out of long verses, is absent).

Read in full at the desk (28 seats): 2:196, 2:282, 4:34, 5:3, 9:3,
11:44 (Wave 1); 17:1, 22:26, 22:27, 22:36, 22:37, 24:2, 24:31,
27:23, 31:31, 33:35, 39:7, 40:67, 45:5, 47:4, 48:8, 49:13, 50:25,
51:56, 65:1, plus every GAP seat read in context. Every clause of
the Master is carried at every seat read — lists item by item
(5:3 prohibited list; 24:31 kinship list; 33:35 ten pairs), refrains
in full at every occurrence (batch self-checks, spot-confirmed).

Batch I (40:28–51:5), built by repairing a rejected first attempt,
was sampled hardest (40:67, 45:5, 47:4, 48:8, 49:13, 50:25, 51:56):
content-complete at every seat. **Quality caveat, disclosed:** batch
I's Friulian syntax is looser than the other batches' (dropped
auxiliaries, mangled word order at 47:4, Italianate connectives) —
sense is carried, elegance is not uniform. This is a quality note,
not a fidelity failure; it is recorded here for the parent desk and
for any future revision pass.

One disclosed blemish: 39:63 renders the Master's "reins" as
"lis clâfs" (keys). No attested Friulian reins-word exists in any
harvested source (the redin- family is empty in corpus and
lexicon); the substitution preserves the governance sense and is
logged in batch H's notes. It stands as a descriptive substitution,
named here, not concealed.

## Gate 3 — Token adjudication: PASS WITH CORRECTIONS (applied)

verify.py's screen lists 2,296 untraced candidates of 9,090 distinct
tokens; the desk's stemmer cannot strip Friulian paradigms, so the
list is dominated by regular futures, preterites (diserin ×139 is
the regular preterite of dî), elisions and clitics, carried names
under the names policy, and the glossary's disclosed flagged seats
(cjastic ×179 — corpus ×1, Pirona-family, stands disclosed;
il Misericordiôs; ambassadôr; testimoni; lemosine; giudizi;
politeiscj; vuardian). The top-frequency band and every item named
in the build log were hand-adjudicated. **Full token-by-token
adjudication of all 2,296 candidates was not completed in this
pass** — the residual risk is bounded by the frequency-band review
and is stated here plainly.

Four corrections were specified and have been APPLIED at the desk
and re-verified (verify.py re-run clean):

1. **rivelaments ×14 (batch A) → rivelazions.** rivelament has no
   attestation in any harvested source (corpus ×0); rivelazion
   (×13) / rivelazions (×7) are attested and are the lane's seated
   forms. All 14 seats (2:187, 2:219, 2:231, 2:242, 2:252, 3:21,
   3:70, 3:101, 3:103, 3:108, 3:112, 3:113, 3:164, 3:199) now carry
   rivelazions with feminine agreement.
2. **The cjamiel- camel family ×7 seats → ⟦GAP: camel⟧.** No
   attested Friulian camel form exists in any harvested source
   (corpus ×0, Wiktionary none, Pirona shows only Italian/Latin
   shapes, Culòs none). Seats 11:64, 12:65, 12:72, 54:27, 59:6,
   77:33, 91:13 now carry the GAP device on the 17:59 pattern.
   (Batch K's note claiming "cjamei corpus ×1" does not survive
   checking against the frequency file — recorded as a crew-log
   error; K seated no camel verse itself.)
3. **avertadôr at 48:8 → avertidôr.** avertî is a -î verb; the
   regular agent form avertidôr is seated ×18 elsewhere.
   puartadôr at 48:8 stands (puartâ is -â, regular).
4. **judaisim at 62:6 → "la fede dai Judeus."** The form's only
   corpus attestation is a single piped-link display token
   ([[Ebraisim|judaisim]]); too weak to carry the seat. The repair
   crew's logged fallback is seated.

Ruled to STAND, with grounds: 9:19 *pelegrins* (the people, not the
institution — the verse's sense is about people); batch B's
in-verse extension of il Misericordiôs to "Merciful" predicated of
God (the seated Basmalah adjective, consistently applied,
disclosed); 39:63 clâfs (above); 28:31's descriptive demon-simile
vs 27:10's GAP (the difference follows the Master's own wording at
each seat — consistent); batch C's and K's thin seats (pedoi,
gjavutis, cuais, orfan, perlis — thin but attested, disclosed in
the batch notes).

## Gate 4 — GAP census: PASS

Final: **58 seats, 66 markers** — pilgrimage 15, jinn 34, Sabbath 7,
camel 8 (17:59 + the seven converted seats), musk 1 (83:26),
cushions 1 (88:15). The three new terms were verified unattested
before their GAPs were allowed to stand (musc- hits are moss/muscle
words, not musk; the cussin- family is empty). Every GAP seat's
verse is otherwise rendered in full. GAPs reconcile against the
attestation audit's STAYS GAP list plus these verified additions.

## Gate 5 — Fences: PASS

- No "first ever" / "first translation" claim anywhere in the text
  (machine scan: NONE) or the paperwork; the front matter states
  only that no Friulian Qur'an was found, tier NOT FOUND.
- No *La Bibie* or Culòs wording reproduced beyond the short cited
  Lord's Prayer phrases in the paperwork (fact/citation control
  only, per the licences record).
- §F forbidden Italian-shaped forms: scanned as standalone words
  across the whole text — the only hits are "sole" at ten seats,
  which is the attested Friulian feminine adjective "only/single"
  (e.g. 4:1, 6:98 "une sole anime"), not the Italian sun noun. PASS
  with the homograph named.

## Purple sweep reconciliation

verify.py's counts, the GAP census, and the token screens reconcile
with the batch paperwork seat by seat (the desk ran the mechanical
reconciliation; the house Purple tool itself was not runnable from
this session — stated plainly for the parent desk).

## OVERALL VERDICT: PASS WITH CORRECTIONS — corrections applied and re-verified

All five gates pass. The book is ready to assemble and shelve as
**DRAFT — NOT PUBLISHED**, subject to the independence caveat at
this report's head: the parent desk decides whether this desk-run
checker pass satisfies the independent-checker gate or a fresh-agent
pass is re-run before the landing commit.
