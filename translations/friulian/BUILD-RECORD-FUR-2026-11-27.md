# BUILD RECORD — Friulian Quran lane, 2026-11-27

Opened by Robert Tilford's ruling of 2026-11-27 (21:16 CST)
adopting the desk recommendations in CANDIDATE-BRIEF-FRIULIAN.md
wholesale. Working papers: `~/workspace/ayah-friulian/` (BUILD-SPEC,
glossary, attestation audit, licences record, batch files and
notes, checker report). Build log:
`~/workspace/goals/endangered-language-quran-translations/hidden_files/FRIULIAN-BUILD-LOG-2026-11-27.md`.

## Build shape

- Master: the Locked English Master, extracted as
  master-verses.json (114 surahs, 6,236 verses; manuscript MD5
  ecc5b8e2848e5044186b7ad82bed9f4e — the same extraction the Veps
  lane used).
- Twelve batches A–L of ~520 verses, each under a binding fidelity
  protocol (every clause carried; long verses >25 Master words
  listed and confirmed clause-complete) and the attestation law
  (attested form / descriptive rendering on attested words /
  visible GAP — no fourth move; never invented; never silently
  borrowed from Italian).
- A standing desk gate ran over every batch before merge: key-set
  equality, retained-English screen, GAP census, "redacted" scan.
- Batch I's first attempt was REJECTED at that gate (471 retained
  English word types across 301 of 520 seats) and re-dispatched;
  the re-dispatch screened clean.
- Desk fidelity spot-checks passed on every wave (Wave 1:
  2:282 entire, 2:196, 4:34, 5:3, 9:3, 11:44 clause by clause).

## Outcome

6,236 verses; 6,178 rendered in full; 58 GAP seats (66 markers).
Checker verdict: PASS WITH CORRECTIONS, all corrections applied
and re-verified. The pack in this folder is assembled and ready;
the landing commit is held for the parent desk's confirmation of
the checker gate, per the caveat at the head of the checker
report.

**Addendum (2026-11-27, later the same day):** the fresh-agent
independent checker pass (CHECKER-REPORT-INDEPENDENT-FUR-
2026-11-27.md) superseded the desk pass as the deciding record and
FAILED Gate 3 on four unattested families at 45 seats. The
remediation was applied the same day (51 tokens at 50 seats,
including five sibling tokens found by sweep), the manuscript was
re-assembled (849,025 bytes, SHA-256
cfa30b7510ac80ff55ecbef4dc93c9ed0aedfd6465328f9bd48b08ec8887acd2),
canonical re-verify passed, and the pack was re-staged. The
landing remains held, now for the fresh targeted Gate 3 re-check.
Full record: CORRECTIONS-FUR-2026-11-27.md and MANIFEST.txt.

**Addendum 2 (2026-11-27, later still):** the fresh targeted
re-check (CHECKER-REPORT-RECHECK-2026-11-27.md) verified the
first remediation in full but failed its new-band check on five
further families (17 seats) plus a condemned doublet (2 seats).
The second remediation was applied the same day (18 tokens at 18
seats; 68 seats across both rounds), the manuscript re-assembled
(849,085 bytes, SHA-256
e4a15b9718183b60e2e92a8695d7475ce9e739f6925fe6dc99837aca8d51738d),
canonical re-verify passed, and the pack re-staged. The landing
remains held — now for a further fresh re-check with a widened
adjudication band, per the recheck's warning. Full record:
CORRECTIONS-FUR-2026-11-27.md and MANIFEST.txt.

**Addendum 3 (2026-11-27, round 5):** the second deciding
checker (CHECKER-REPORT-DECIDING2-2026-11-27.md) passed
canonical, the condemned sweep, fidelity, the GAP census and
the fences, and failed Gate 4 on four rulings resting on
non-Friulian evidence. Its prescription — an exhaustive
ground-shape sweep of all 2,073 ATTESTED-REGULAR rulings —
was executed and applied: 322 grounds corrected with the
ruling standing, 109 rulings overturned (106 CONDEMNED, 3
FLAGGED CONSTRUCTION), 246 verses changed, the application
set built mechanically from the record (110 condemned tokens
with seats; spec coverage asserted before any swap), and the
zero-check over the full updated condemned set (362 tokens),
case-insensitive, returning NONE. Canonical re-verify passed
(6,236 = 6,236, grid clean, GAP 59/67, Basmalah exact,
"redacted" NONE). The manuscript was re-assembled (849,246
bytes, SHA-256
82f15a7412c2e85a382a4775be50d9d192e6ce9a89f997aeaee7d803d22c291e)
and the pack re-staged. The landing remains held — now for a
fresh deciding checker pass by an agent that did none of
this work, drawing a new adjudication spot-band weighted to
round-4 and round-5 rulings. Full record: the lane's
ATTESTATION-AUDIT-2026-11-27.md and REMEDIATION-2026-11-27.md
(round-5 sections) and work/adjudication/apply_round5.py.

## Round-6 addendum (2026-11-28)

On the third deciding checker's prescription (Gate 4 FAIL:
luserès, ruzave, rump — grounds resting on a place name, a
surname, a plant name, and an English proper name inside
Friulian sentences), the lane ran remediation round 6: the
named seats re-seated on the lusî, bruntulâ and rompi
families; an exhaustive targeted ground sweep over the
suspect class (1,621 ATTESTED-REGULAR rulings on family/
prefix cites or exact-attestation claims — 1,403 verified as
cited, 145 grounds corrected with rulings standing, 73
dossiers ruled firsthand: 36 stand, 37 condemned); and the
trace-sharing propagation, which condemned the giud- family
wholesale (re-seated in the corpus jud- spelling, ~75 seats)
and the unrecorded litig- family (20 seats, re-seated on
disputâ). 59 net-new CONDEMNED rulings (set 362 → 421), 167
grounds corrected, 48 new ATTESTED-REGULAR entries, 132
verses changed (137 token substitutions, 12 phrase
rewordings), application built mechanically from the record
with spec coverage asserted first. Zero-check over the full
updated condemned set (421 tokens), case-insensitive: NONE.
Canonical re-verify passed (6,236 = 6,236, grid clean, GAP
59/67 unchanged, Basmalah exact, "redacted" NONE). The
manuscript was re-assembled (849,218 bytes, SHA-256
94f83486da2c5dec9127af4360420cfc6fece185fa612b992c261832d021106d)
and the pack re-staged. The landing remains held — now for a
fresh deciding checker pass by an agent that did none of
this work, its adjudication band weighted to family/prefix-
cite and exact-attestation grounds, grounds verified
firsthand, plus the full condemned sweep. Full record: the
lane's ATTESTATION-AUDIT-2026-11-27.md and
REMEDIATION-2026-11-27.md (round-6 sections) and
work/adjudication/apply_round6.py.

## Deciding checker pass 4 (2026-11-28) — FAIL, not landed

The fresh deciding checker (CHECKER-REPORT-DECIDING4-2026-11-28.md,
lane record) passed Gates 1 (canonical — independently re-derived:
6,236 = 6,236, GAP 59/67, manuscript hash matching), 2 (condemned
sweep — its own code over all 421 CONDEMNED tokens: zero leftovers),
3 (fidelity fresh sample) and 5 (fences/paperwork — all round-6
claims re-derived and consistent), and confirmed every round-6
re-seat firsthand. Gate 4 FAILED on four rulings the round-6 sweep
did not reach: avvisadôr (67:8, 67:9, 67:26, 71:2 — ground names no
checkable form, the "evidence2 record" class; Pirona's Friulian for
Avvisare is Visa), bracialets (22:23 — cited traces are wrong
lexemes: braciants "day-labourers", bracie "arms"), aflit (41:50,
43:48, 68:6 — unattested; the seats' syntax is also garbled), and
disfurtune (9:98 — its round-6 restated ground cites disfâ, a
different lexeme). Ground repairs also named: salviaran (stands on
salvâ; its cited "salvi=7" does not re-derive) and mandaitlis.
LANDING STATUS: NOT LANDED. The pack stands re-staged and
uncommitted; a round-7 remediation on the checker's prescription —
condemn/re-seat or GAP the four, repair the 41:50/43:48 syntax,
restate the two grounds, and extend the sweep to every ruling whose
ground names no checkable form — awaits the parent desk's direction.


## Remediation round 7 (2026-11-28) — the no-form-ground sweep

The named families, seat by seat against the Locked English
Master: avvisadôr CONDEMNED (its ground named no checkable form;
Pirona's Friulian for the sense is the Visa family) and re-seated
avertidôr at 67:8, 67:9, 67:26, 71:2; aflit CONDEMNED (the Italian
afflitto stem, no cell of the lane's afligjâ) and re-seated on the
attested patî family (Pirona part-2 L52457; corpus patît x37) —
68:6 reworded "chel che al patìs", 43:48 reworded with fasèrin
patî and its garbled syntax repaired, 41:50 rewritten whole
against the Master (its English-order clauses, wrong-gender
articles and Italian copula forms removed); bracialets (22:23)
and its second spelling braçalets (18:31, 76:21) CONDEMNED (no
Friulian bracelet form in any source; Pirona carries the word
only inside Italian prose) — all three seats take GAP markers;
disfurtune CONDEMNED (its round-6 restated ground cites disfâ, a
different lexeme) and re-seated sfortune at 9:98, with its kin
disfurtunât re-seated sfortunât at 22:28 and disfurtunis
re-seated sfurtunis at 7:168 (sfortune corpus x1 in Friulian
prose; sfortunât x5). The salviaran and mandaitlis grounds are
restated on their true evidence (salvâ, Wiktionary lemma +
corpus x36, the salvi exact form at x2-3 including the Friulian
"che salvi i prâts"; mandâ corpus x31, the "mandai" cite struck
as not re-derived).

The sweep, exhaustive over the classes the earlier sweeps'
definitions did not reach: the no-form-ground class (grounds
naming no Pirona line, no corpus count, no lemma cite — the
"evidence2 record" shape) held 439 ATTESTED-REGULAR rulings:
365 grounded under a conservative verifier (the round-6 strict
test behind a one-strip derivation, built so the disfâ
over-strip is unreachable) and 74 went to firsthand dossiers.
The round-6 RESTATED guard re-ran over all 145 restated grounds:
118 pass with the cited stem verified as the token's own
lexeme, 27 to dossiers. The cited-ground classes were re-run
whole: of 2,035 ATTESTED-REGULAR rulings, 1,668 cited forms
verify, and every one of the 98 cited-failed and 32
cited-partial rulings was carried into the round-7 pools and
resolved (no orphans). The merged dossier pool held 251 tokens;
a lemma-derivation pass grounded 134 more, and the 117 residues
were ruled firsthand one by one: 102 stand with restated
checkable grounds, 14 condemned, and 1 (l'eternâl, 3:2) ruled
FLAGGED CONSTRUCTION with its non-attestation disclosed. The
firsthand work also condemned 27 further tokens the machine
sweeps had passed on wrong-lexeme or fragment evidence —
the inchin- family whole (its evidence was Pirona's Incinâ
"to notch" and the English word "inch"; re-seated on the
lane's prosternâsi), inciantarin/inciantânus (a strip-to-"inc"
fragment; reworded on fature), agjut (agjî "to act"; re-seated
aiût), cjamiei (a "cja" fragment; GAP, as the lane's camel
ruling), deleitin (the article "del"; re-seated gjodin),
meraveis ("mer" the sea; re-seated maraveis), bruisait ("bru";
re-seated brusait), cative ("freq:cat"; re-seated triste), the
adultery family (never adjudicated; its nine seats take GAP
markers), perseverais/perseveravin/perseverât (the family's
only corpus trace is the newspaper name "La Perseveranza";
reworded on pazience, the book's standing word, as
perseverin was in round 6), desiderôs (Italian meta-text
traces; reworded on Pirona's Vèje), ciecamentri (no Pirona
Ciec headword; reworded), fatûr (reworded "mestri di
fature"), litigôs (the litig- family's last form; reworded on
disputâ), sacrilegi (its claimed corpus forms occur nowhere;
reworded on violâ), l'iresistibil (reworded "che nissun i
pues resisti" at its three seats), stordît/stordiment
(Pirona's Friulian for the sense is Sturnî, part-2 L106127;
re-seated sturnît/sturniment), pançis (re-seated panzis on
panze), dispôs (re-seated disponût), ahî (the kallā seats'
own norm is "No!"; re-seated), antecessôrs (re-seated
antenâts). In all: 41 new CONDEMNED rulings (set 421 -> 462),
20 new ATTESTED-REGULAR entries for the replacement forms,
1 new FLAGGED CONSTRUCTION, and 688 grounds restated (577 by
the sweep machinery, the rest by hand). Application was
mechanical from the record (spec coverage asserted: 41
condemned tokens with seats = 41 in spec): 37 phrase swaps and
37 token-swap occurrences; 70 verses changed. Zero-check over
the full updated condemned set (462 tokens), case-insensitive:
NONE left over. Canonical re-verify after round 7: 6,236 =
6,236, per-surah grid clean at all 114, GAP census 73 seats /
86 markers (was 59 / 67: +3 bracelets, +2 camel, +9 adultery),
Basmalah 1:1 exact, "redacted" NONE.

Coverage, stated explicitly: cited-form grounds were swept in
rounds 5-6 and re-verified whole in round 7 (1,668 verified;
every failure resolved); no-form grounds were swept in round 7
(439, all resolved); round-6 RESTATED grounds were
lexeme-guarded in round 7 (145, all resolved). Classes not
swept by any round, named honestly: the 57 PRIOR PASS entries
(they carry the earlier checker passes' authority and state no
ground of their own), the 11 FLAGGED CONSTRUCTION entries
(their grounds name their evidence and their disclosure), and
seated base-vocabulary tokens that carry no record entry at
all (the builder's core vocabulary, e.g. pazience, triste —
outside the adjudication record by construction).

LANDING STATUS: NOT LANDED. The pack stands re-staged and uncommitted; the landing waits on a fresh deciding checker pass (pass 5) by an agent that did none of this work.


Correction (dated 2026-11-28, on deciding checker pass 5's finding): the round-7 grounds-restated tally given above as 688 is corrected to 696, the fresh deciding checker's independently derived count (CHECKER-REPORT-DECIDING5-2026-11-28.md, Gate 5). The discrepancy is a descriptive tally only; it touches no seat, ruling, or ground.
