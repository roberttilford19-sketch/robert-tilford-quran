# CHECKER REPORT (INDEPENDENT) — Friulian (fur) Quran lane

**Checker:** a fresh checker agent that built none of this text and is
not the desk that gated its batches or ran the first checker pass.
This report is the deciding checker record for the landing gate; the
desk's CHECKER-REPORT-FUR-2026-11-27.md stands on record beside it,
not replaced.

**Text graded:** the staged shelving pack at
`~/workspace/robert-tilford-quran/translations/friulian/` — its
manuscript is byte-identical (MD5 317d36940046a948fc92d83b0ba22057)
to the build manuscript in `~/workspace/ayah-friulian/`, and the
build's `quran-fur.json` flattens exactly to `verses-store.json`
(6,236 seats, zero differences). All checks below were run by this
checker against the staged text and the Locked English Master
(`master-verses.json`, MD5 ecc5b8e2848e5044186b7ad82bed9f4e), with
this checker's own scripts, not the desk's verify.py output (the
desk's screen was used only as a candidate generator for Gate 3,
which is what it declares itself to be).

## Gate 1 — Canonical: PASS

Re-run independently, including a from-scratch parse of the staged
manuscript itself (not only the store):

- Seat-set equality 6,236 = 6,236; per-surah grid clean at all 114
  surahs, in the store and in the manuscript's own verse numbering
  (114 sections, numbering sequential 1..N at every surah, 6,236
  numbered verses in total).
- Manuscript text equals the store at every one of the 6,236 seats
  (0 differences).
- Basmalah 1:1 exact: "Tal non di Diu, il Plen di misericordie, il
  Misericordiôs."
- No empty verse anywhere; the string "redacted" appears in no seat
  of the store and nowhere in the staged manuscript.

## Gate 2 — Fidelity spot-check: PASS (fresh sample, 34 seats)

A fresh sample was drawn mechanically — the longest Master verses
not read by the desk, a batch-I block (the once-rejected batch,
40:28–51:5) weighted heaviest, a seeded random spread, and the
three lowest length-ratio verses in the book — and read clause by
clause against the Master. None of the desk's 28 seats was reused.
Seats read: 73:20, 5:110, 2:259, 4:12, 22:5, 24:61, 33:50, 3:154,
60:10, 74:31, 58:22, 48:29, 46:15, 42:15, 48:25, 41:50, 40:28,
47:15, 41:44, 42:13, 49:11, 3:13, 8:54, 10:13, 16:53, 18:15,
19:86, 21:5, 27:86, 44:49, 54:50, 39:48, 68:42, 39:35.

- Every clause of the Master is carried at every seat read. The
  long enumerations survive item by item (4:12 inheritance shares;
  24:61 the eleven-house list; 33:50 the kinship list; 47:15 the
  four rivers). The Veps failure mode — content words dropping out
  of long verses, pronouns standing in their place — is absent.
- This checker's own mechanical length screen over all 4,450 verses
  with Master text ≥12 words: median Friulian/Master word ratio
  1.143, minimum 0.67 (19:92, a 12-word verse); the three lowest
  ratio verses of any length (39:48, 68:42, 39:35) were read and
  are genuine concision, not collapse. No collapsed verse exists.
- **Quality caveat, confirmed independently:** batch I's Friulian
  syntax is markedly looser than the other batches' — Italianate
  connectives and copula ("Muhammad è il Ambassadôr", 48:29),
  mangled auxiliary chains (46:15, 42:15, 41:44), dropped articles.
  Sense is carried everywhere in the sample; elegance is not
  uniform. This is the desk's disclosed caveat, confirmed, and it
  is a quality note, not a fidelity failure. It should ride in
  FLAGS for any future revision pass.

## Gate 3 — Token adjudication: **FAIL**

### The four recorded corrections — three verified whole, one verified in part

1. **rivelaments → rivelazions:** verified. rivelaments occurs
   0 times in the staged text; all 14 named seats carry
   rivelazions.
2. **cjamiel- camel family → ⟦GAP: camel⟧:** verified. No
   cjamiel- form stands anywhere; all 7 named seats plus 17:59
   carry the GAP. (The remaining "cjame" hits in the text are
   *cjamese*, "shirt", a Wiktionary-lexicon lemma, and *discjame*
   at 7:157 — not camel forms.) This checker's own corpus check
   agrees there is no Friulian camel form to seat: the corpus hits
   are the Latin *camelus* name-forms and Italian plurals.
3. **avertadôr → avertidôr at 48:8:** verified at 48:8 — **and
   the condemned form still stands at three more seats.** See
   failure item A.
4. **judaisim → "la fede dai Judeus" at 62:6:** verified. 62:6
   carries the fallback; judaisim occurs nowhere in the text.

### Fresh band adjudication

A fresh band of the 45 highest-frequency untraced candidate tokens
(the desk's named adjudications excluded) was adjudicated by this
checker against the harvested sources (Wiktionary lexicon and raw
Wiktionary harvest, Friulian Wikipedia frequency list and full
corpus XML, Pirona 1871 full text, Culòs Matthew, the build
wordlists, glossary, attestation audit, batch notes). Passed, with
grounds: è (Pirona); àno (Pirona ×7, the 3pl of vê); l'infier and
l'ambassadôr (regular elisions of an attested noun and a disclosed
flagged form); dinearaîso (the Surah 55 refrain — Pirona's headword
for "deny" is Denea/Dineà, *dineâ*, and the enclitic future form is
disclosed with its family in batch notes D and J); the regular
preterite and future paradigms on attested stems (fasèrin,
mandàrin, cjapàrin, salvàrin, refudarin — also corpus ×1 —
perdonarà, viodaran, cjatarâs, metarìn, savarês, savaran,
savessin, savessis, crodarìn, judarà, jentraran, jentrait,
mangjait); avertidôr (regular -idôr agent on the corpus-attested
avert- stem: avertî, avertît, avertide, avertiment, avertencis);
perdonadôr (regular -adôr on perdonâ, -â class, attested in Culòs);
cognossidôr (cognossi corpus ×189, regular -idôr); busiâr and
busiârs (Pirona's busi- family — Busiz ×8, Businà, Businamènt —
plus regular agent derivation, disclosed in notes-J); diaui
(regular plural of diaul); injusts (the adjective is attested in
running corpus prose — "cussì injust inviers di lui", "lis leçs
injustis", "injustiziis" — thin, and this checker recommends it be
flagged in FLAGS, but it is attested, categorically unlike
judaisim's single piped-link display token); informarà (informâ
corpus ×2, informât ×4); partên and parten (the partignî family,
both spellings in corpus running text); àial and sêstu (regular
enclitics); veritîfs (corpus ×1, veritât family); purifiche
(purificâ corpus ×2; the -e 3sg present is the regular -â-class
form); cjastiarà (cjastiâ is a Wiktionary-lexicon lemma);
giudicarà (the giudic- verb is Pirona-attested: giudica,
giudicare, giudicato); graciôs (gracie family, regular -ôs
adjective, cf. Misericordiôs); sêit (jessi paradigm); parabule
(corpus ×1); ubidîtmi (ubidî plus enclitic -mi).

### Failure items — seated forms with no attestation in any harvested source, none of them disclosed flagged constructions

**A. avertadôr — 3 seats: 43:23, 46:9, 50:2.** The desk's own
correction 3 ruled this form wrong (avertî is a -î verb; the
regular agent is avertidôr) and repaired it at 48:8 only. The same
form stands unrepaired at three batch-I seats, all carrying the
"warner" sense. Attestation check by this checker: corpus avert-
family gives avertî, avertît, avertide, avertiment, avertencis —
no agent noun in either spelling's favour beyond the paradigm;
Wiktionary lexicon: no avert- lemma; Pirona: none; Culòs: none;
wordlists: none. The rejected batch I note's claim that avertadôr
was seated as an "attested lemma" does not survive checking.
Remediation is mechanical: avertidôr at the three seats, exactly
as at 48:8.

**B. The resussitâ family — 21 tokens at 20 seats** (2:259, 5:110,
6:29, 6:36, 7:14, 17:98, 19:33, 21:21, 22:7, 23:16, 23:37, 23:82,
23:100, 26:87, 27:65, 30:19, 64:7, 72:7, 80:22, 83:4; forms
resussitâ ×1, resussitât ×3, resussitâts ×13, resussitarà ×3,
resussitin ×1), carrying the resurrection sense at major seats.
Attestation check: Wiktionary lexicon — none; raw Wiktionary
harvest — 0 hits; corpus frequency list — 0; corpus XML — 0;
Culòs — none; wordlists — none. The attestation audit seats only
the noun **resurezion** (corpus ×27, verified) and never mentions
the verb; the glossary is likewise silent. What the harvested base
does hold: the corpus's own verb **resurî** (resurît ×3, resurî
×1, resuriment ×3), and Pirona's specimen text spells the stem
**resuscit-** ("al è resuscitàd", Luke 15, in Pirona 1871) — a
different stem spelling from the seated resussit-. The lane's own
precedent for exactly this situation (dijun, lemosine, ipocrit)
is a Pirona-era or dialect form seated in coinè spelling **with
the flag disclosed** in the audit and glossary. resussitâ carries
no such disclosure and, as spelled, no attestation. It cannot
stand as staged. Remediation is the desk's choice among attested
roads — resurî-family forms where the sense allows, the Pirona
resuscit- stem in coinè spelling with the flagged-construction
disclosure written into the audit, glossary and FLAGS, or GAP —
but one of those roads must actually be taken and recorded.

**C. epure — 12 seats** (8:34, 9:42, 9:99, 9:126, 35:12, 35:42,
36:45, 36:46, 36:74, 36:77, 39:7, 39:49), the connective "and
yet". Attestation check: corpus frequency list — 0 (the corpus
form is **epûr**, ×1); corpus XML — 0; Wiktionary lexicon and raw
harvest — 0; Pirona — 0; Culòs — 0; wordlists — 0. Undisclosed in
the audit, glossary and batch notes. epure is the Italian-shaped
form of the attested epûr. Remediation: epûr, or another attested
connective, seat by seat.

**D. The denegâ family — 10 tokens at 10 seats** (denegât 7:146;
deneghin 7:147, 10:39, 10:95; deneghe 7:176, 10:17; denegarin
8:54, 10:45, 11:59; denegâ 11:19). Found in this checker's sample
reading (8:54) and inventoried text-wide. Pirona settles the
stem: his Friulian headword is **Denea / Dineà** (*dineâ*), and
his Italian→Friulian index gives "Denegare — Dineà", i.e.
deneg- is the Italian side of Pirona's page, not a Friulian form.
No batch note discloses a denegâ choice; the lane's other batches
seat the attested dineâ family for the same English word.
Remediation: the corresponding dineâ-family forms at the ten
seats, as batches D and J already seat them.

Gate 3 therefore FAILS. The desk's pass stated plainly that full
token-by-token adjudication of all 2,296 candidates was not
completed in its pass; this independent pass, adjudicating a fresh
high-frequency band and the correction seats, found four
unattested, undisclosed families carrying load at 45 seats in
total. That is the Veps failure class — a borrowed-shaped stratum
seated against the lane's own attestation law — smaller in scale
than Veps, but the same kind, and the gate is the gate.

## Gate 4 — GAP census: PASS

Reconciled by this checker's own census of the staged manuscript
and the store (identical results): **58 seats, 66 markers** —
pilgrimage 15, jinn 34, Sabbath 7, camel 8, musk 1 (83:26),
cushions 1 (88:15). The first three reconcile exactly against the
attestation audit's STAYS GAP list. The three additions were
verified by this checker against the harvested sources: camel —
no Friulian common-noun form in running text (corpus hits are
Latin name-forms and Italian plurals); musk — every musc- corpus
hit is a muscle or moss word, none is the perfume; cushions — the
cussin- letter-sequence hits in the corpus are "stât cussinet"
(buffer state), cussince (conscience) and place names, no cushion
noun. Both spot-read GAP seats (83:26, 88:15) are otherwise
rendered in full. FLAGS' shorthand that the cussin- "family is
empty" is loose wording for the position just stated; the GAPs
themselves are justified and honestly held.

## Gate 5 — Fences: PASS

- No "first" claim anywhere in the pack: every occurrence of the
  word is an explicit negation ("No first-translation claim is
  made", front matter, README, MANIFEST) or process narrative
  (batch I's rejected first attempt). The front matter's novelty
  wording is the bounded house form: none found, tier NOT FOUND.
- No Bible wording beyond fact/citation: the manuscript contains
  no La Bibie or Culòs text; the paperwork cites only the short
  Lord's Prayer phrases as citation, per the licences record.
- DRAFT — NOT PUBLISHED stands on the manuscript (front matter
  and title block), the README and the MANIFEST.
- The language base is named on the book's face: standard
  Friulian, the furlan standard / normalizât coinè, official
  orthography (Regional Decree 392 of 25 October 1996), with the
  attested lexical base and the in-copyright controls named.

## OVERALL VERDICT: **FAIL — DO NOT LAND**

Gates 1, 2, 4 and 5 pass, two of them (canonical, GAP census)
exactly as reported. Gate 3 fails on four unattested, undisclosed
form families at 45 seats: avertadôr ×3 (43:23, 46:9, 50:2),
resussitâ family ×21 tokens at 20 seats, epure ×12, denegâ family
×10. The pack was NOT landed; nothing was staged, committed or
pushed by this checker.

**Remediation map, for the desk:** (1) avertadôr → avertidôr at
43:23, 46:9, 50:2; (2) the resussit- seats re-seated on an
attested road (resurî family, or the Pirona resuscit- stem in
coinè spelling with the flagged-construction disclosure written
into the audit, glossary and FLAGS), the road chosen recorded;
(3) epure → epûr or an attested connective at the 12 seats;
(4) the deneg- seats re-seated on the dineâ family. Then
canonical re-verify, a fresh targeted Gate 3 re-check on these
families plus a new high-frequency band, and the pack re-staged.
The batch-I syntax caveat (Gate 2) and the injust flagging
recommendation (Gate 3) ride as quality notes for the same pass,
neither of them gate grounds.
