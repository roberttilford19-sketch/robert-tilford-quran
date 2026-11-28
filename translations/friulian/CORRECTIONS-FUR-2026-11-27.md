# CORRECTIONS — Friulian Quran, 2026-11-27

## Checker corrections (from CHECKER-REPORT-FUR-2026-11-27.md; applied and re-verified)

1. **rivelaments → rivelazions, 14 seats** (2:187, 2:219, 2:231,
   2:242, 2:252, 3:21, 3:70, 3:101, 3:103, 3:108, 3:112, 3:113,
   3:164, 3:199). Ground: rivelament unattested (corpus ×0);
   rivelazion ×13 / rivelazions ×7 attested and lane-seated.
   Feminine agreement carried (i siei → lis sôs where possessive).
2. **cjamiel- camel family → ⟦GAP: camel⟧, 7 seats** (11:64, 12:65,
   12:72, 54:27, 59:6, 77:33, 91:13). Ground: no attested Friulian
   camel form in any harvested source; the GAP device follows the
   17:59 pattern ("la ⟦GAP: camel⟧ femine" for she-camel seats).
3. **avertadôr → avertidôr at 48:8.** Ground: avertî is a -î verb;
   avertidôr is the regular agent, seated ×18 elsewhere.
4. **judaisim → "la fede dai Judeus" at 62:6.** Ground: the form's
   only corpus attestation is one piped-link display token
   ([[Ebraisim|judaisim]]); the repair crew's logged fallback is
   seated instead.

After corrections: verify.py re-run — 6,236 = 6,236, grid clean,
GAP seats 58, markers 66, 1:1 exact, "redacted" NONE, rivelaments 0,
cjamiel- 0.

## Independent-checker remediation (from CHECKER-REPORT-INDEPENDENT-FUR-2026-11-27.md; applied 2026-11-27)

The independent (fresh-agent) checker pass failed Gate 3 on four
unattested, undisclosed families at 45 seats. All four findings
were desk-verified against the harvested sources and applied under
the audit-application standard (2026-11-27), most serious first in
the checker's order; a sibling sweep of the same four patterns
found and repaired five further tokens. 51 tokens changed at 50
seats; a diff against the pre-remediation store confirms no other
seat moved.

1. **avertadôr → avertidôr, 3 seats** (43:23, 46:9, 50:2). The
   desk's correction 3 above, completed: avertî is a -î verb and
   avertidôr is its regular agent, as already seated at 48:8.
   **Sibling found in the sweep:** averidôr ×2 (7:184, 7:188), the
   same warner-agent family with an unattested stem (the corpus
   avert- family is avertî, avertît, avertide, avertiment,
   avertencis — no aver- stem), likewise seated as avertidôr.
   Whole-text sweep of every -adôr agent confirms avertadôr was
   the only -adôr form standing on a -î verb: every other -adôr
   agent in the text stands on an -â-class stem (ambassadôr is the
   disclosed flagged construction, recorded in the audit), and
   every -idôr agent stands on a -î verb.
2. **The resussit- family → the Pirona resuscit- stem in coinè
   spelling, FLAGGED** — 21 tokens at 20 seats (resussitâ 2:259;
   resussitât 5:110, 19:33, 72:7; resussitâts 6:29, 7:14, 17:98,
   23:16, 23:37, 23:82, 23:100, 26:87, 27:65, 30:19, 64:7 ×2,
   83:4; resussitarà 6:36, 22:7, 80:22; resussitin 21:21), plus
   the sibling spelling **risussit-** ×3 found in the sweep
   (risussitâts 56:47; risussitarà 58:6, 58:18). Road chosen: the
   Pirona resuscit- stem in coinè spelling with the flagged-
   construction disclosure, over the resurî family and over GAP.
   Grounds: Pirona's specimen text (Luke 15, 1871) attests the
   stem ("al è resuscitàd"); the same stem was already seated at
   seven seats by other batches (15:36, 16:21, 16:38, 17:49,
   36:52, 37:16, 38:79), so the road also unifies the lane's own
   practice; the corpus resurî verb is attested only in three
   forms (resurî ×1, resurît ×3, resuriment ×3), too thin a
   paradigm to carry the participle and future forms these 23
   seats need without inventing formations; GAP would have
   opened 23 major seats the attested record can in fact carry.
   The disclosure is written into the attestation audit, the
   glossary (§H and §F) and FLAGS-FUR.md, on the lane's
   dijun/lemosine precedent. Seated forms: resuscitâ, resuscitât,
   resuscitâts, resuscitarà, resuscitin.
3. **epure → Epûr/epûr, 12 seats** (8:34, 9:42, 9:99, 9:126,
   35:12, 35:42, 36:45, 36:46, 36:74, 36:77, 39:49 sentence-
   initial Epûr; 39:7 mid-sentence epûr). epûr is the corpus form
   (×1); epure is its Italian-shaped doublet, unattested in every
   harvested source.
4. **The deneg- family → the dineâ family, 10 seats.** Pirona's
   Friulian headword is Denea/Dineà and his Italian index gives
   "Denegare — Dineà": deneg- is the Italian side of his page.
   Mapped seat by seat onto the lane's seated dineâ paradigm:
   denegât → dineât (7:146, on the 17:98 pattern "a àn dineât");
   deneghin → dinein (7:147, 10:39, 10:95); deneghe → dineie
   (7:176, 10:17, on the 3:19 pattern "al dineie i segns di Diu");
   denegarin → dinearin (8:54, 10:45, 11:59); the nominal seat
   denegâ → dineance (11:19, the attested noun, cf. 2:93, 3:52).

After remediation: canonical re-verify — store seats 6,236 =
master 6,236, per-surah grid clean at all 114, GAP seats 58,
markers 66, Basmalah 1:1 exact, "redacted" NONE; condemned forms
(avertadôr, averidôr, resussit-, risussit-, epure, deneg-) all at
zero in the text. The manuscript was re-assembled from the
remediated store (849,025 bytes, SHA-256
cfa30b7510ac80ff55ecbef4dc93c9ed0aedfd6465328f9bd48b08ec8887acd2)
and the pack re-staged. Landing waits on the fresh targeted
Gate 3 re-check recorded in the MANIFEST.

## Fresh re-check remediation (from CHECKER-REPORT-RECHECK-2026-11-27.md; applied 2026-11-27)

The fresh targeted re-check verified the remediation above in
full (its Checks 1, 2, 3 and 5 PASS, the diff confirmed at exactly
the 50 seats) but FAILED its Check 4: a new adjudication band
(frequency 2–5, seeded sample of 40 from 589 eligible candidates)
found the same unattested, undisclosed failure class at 15
further seats, and one referred doublet was condemned. Those
verified findings were likewise applied under the
audit-application standard: 18 tokens at 18 seats. A diff against
the original pre-remediation store now totals 68 changed seats;
no other seat moved in either round.

1. **beatitudin → felicitât, 5 seats** (9:21 "felicitât che e
   dure"; 10:9, 22:56, 26:85, 31:8 in the garden phrase, "Zardins
   de Felicitât"). beatitudin is zero-attested in every harvested
   source and was already named as unattested in the lane's own
   batch B screen and batch L notes. felicitât is batch L's own
   seated road for the same English word (82:13, 83:22, 102:8).
2. **blasfemie → the disclosed descriptive device, 4 seats, plus
   its agent sibling.** blasfem- (and biastem-) are zero-attested
   everywhere, and batch B's screen had named blasfemie
   unattested. No attested Friulian blasphemy noun exists in the
   harvested base, so the seats are rendered descriptively on
   attested words, on the lane's 39:63 precedent, and the device
   is disclosed in FLAGS and the glossary: the noun seats take
   **peraulis cuintri Diu** ("words against God") — 3:177 "a
   baratin lis peraulis cuintri Diu par fede"; 8:35 "par lis
   vuestris peraulis cuintri Diu"; 9:74 "la peraule cuintri Diu";
   14:28 "cu lis peraulis cuintri Diu" — and the agent sibling
   **blasfemadôr** at 76:24 (same condemned family, frequency 1,
   outside the checker's band) takes the device on the lane's
   104:1 pattern: "a chel che al dîs mâl di Diu".
3. **segnôr → Signôr, 4 seats** (40:64, 40:65, 40:66, 43:46, all
   in "Signôr dai monts"). An unattested doublet spelling of the
   lane's attested Lord-word (corpus ×60; 1:2) — the epure
   pattern; the repair is mechanical.
4. **avuartin → si inacuarzin, 2 seats** (16:26, 16:45). The
   avuart- stem is zero-attested; the lane's attested perceive
   family is (in)acuart- (corpus acuart ×19, acuarts ×23), seated
   as inacuarzin at eight seats, 27:65 supplying the exact
   construction ("lôr no si inacuarzin").
5. **Puessedidôr → Possedidôr, 2 seats** (6:133, 6:147), on the
   recheck's referred-doublet ruling: the puessed- stem is
   zero-attested in every source, while possedidôr (57:21, 57:29,
   62:4) stands on the attested possed- stem (corpus
   possediments ×17, possediment ×12) and was ruled MAY STAND.
   The other referred doublet, aministradôr (6:107) /
   amministradôr (4:132), was ruled MAY STAND on both sides
   (corpus-attested doublet) and is untouched.

After round 2: canonical re-verify — 6,236 = 6,236, grid clean,
GAP seats 58, markers 66, Basmalah 1:1 exact, "redacted" NONE;
round-2 condemned forms (beatitudin, blasfemie, blasfemadôr,
segnôr, avuartin, puessedidôr) all at zero. Manuscript
re-assembled (849,085 bytes, SHA-256
e4a15b9718183b60e2e92a8695d7475ce9e739f6925fe6dc99837aca8d51738d)
and the pack re-staged. **The landing still does not proceed:**
the recheck's own warning stands — with four condemned families
in 40 draws from a 589-candidate band, the unread remainder
cannot be treated as clean. The pack awaits a further fresh
re-check with a widened adjudication band, at the parent desk's
direction.

## Desk repairs during the build (before the checker pass)

Retained-English seats found by the desk's standing screen and
repaired on attested forms only: batch F 25:50, 26:166, 26:168;
batch K 69:32 (cubits → "setante misuris di braç"), 69:36 (scum →
sbrume); batch H 38:17, 38:44 (obedient → ubidient), 38:19
(obedients → ubidients), 39:21 (debris → "rests secs"), 39:41
(detriment → dam); batch G 32:16 (reverence → rispiet), 33:48
(insults → "lis lôr peraulis di mâl"), 31:31 (persevere → dure, on
Pirona's gloss of durâ); batch E 19:65 (persevere → dure; the
Italian-shaped perseverâ was checked and rejected as unattested).
Batch J unattested formations replaced: Compassionevol ×4 (52:28,
55:1, 57:9, 59:22 → the ruled Basmalah mercy seats), proviodidôr
×2 (51:58, 62:11 → descriptive on dâ), eiaculais ×1 (56:58 →
descriptive). Batch I's first attempt was rejected whole (471
retained English types) and re-dispatched; the re-dispatch screened
clean.

## Round 3 — full band adjudication (2026-11-27)

Acting on the recheck's closing warning, the desk adjudicated
EVERY remaining untraced candidate in the frequency 2–5 band
(533 tokens: 459 ATTESTED-REGULAR, 73 CONDEMNED, 1 FLAGGED
CONSTRUCTION — Dutpotent, disclosed in the attestation audit,
the glossary §H, and FLAGS). Every condemned token was re-seated
seat by seat against the Locked English Master on an attested
form, a disclosed descriptive device, or the text's own attested
equivalent: 199 verses changed, and a final token sweep confirms
every condemned form at zero in the text. The largest families:
the assocj- partner verb (→ associ-, corpus-attested), the
apartenignin/apartègnin doublets (→ apartenin), the refuge words
ricoar/refuji/refuç (→ ricet), the kneel family (→ Pirona's
inzenogl- forms), the soffl- family (→ Pirona's sofl-), the
sbefeâ mockery family (→ corpus ridiculizâ), qualsisei →
cualsisei (corpus ×80), dissêpui → dissepui (corpus ×20),
grembis → grîms (Pirona: grembo = grìm), menton → barbe
(Pirona: mento = barbe), murmuri → tananài (Pirona: bisbiglio),
sgjume → brume (Pirona: schiuma), spierme → semence, strionarie
→ magjie, l'essere uman → l'om, and the blasphemy verb seats on
the disclosed device (disin mâl). Canonical re-verify after
round 3: 6,236 = 6,236, per-surah grid clean at all 114,
Basmalah 1:1 exact, GAP census unchanged (58 seats / 66
markers), "redacted" NONE. Manuscript re-assembled (849,012
bytes, SHA-256 f7463dfa8aba2e4ce984ae90cf10392f6714bf3ff7a9637d2667e83fb2ebd629)
and the pack re-staged. Full per-token record:
ayah-friulian/work/adjudication/ADJUDICATION-RECORD.json;
seat-level changes: work/adjudication/round3-changes.json.
Residue flagged in FLAGS for a future pass (apartegn family,
distrusi/distruzarà, ringrazi- z-forms, miserabile, colpêvui) —
none in the adjudicated band.

## Addendum (2026-11-27, later the same night) — deciding checker FAIL

The deciding checker (CHECKER-REPORT-DECIDING-2026-11-27.md in
the lane folder) FAILED the pack: Gates 1, 3, 5 PASS; Gate 2
FAIL — apresiatîfs (6:53, 7:17) and sgarpade (12:26–28), both
ruled CONDEMNED in round 3, were omitted from the round-3
application tables and never re-seated, so the round-3 sentence
above claiming a final sweep confirmed every condemned form at
zero does not hold (71 of 73 stand at zero); rivelaments (3:98)
also still stands. Gate 4 FAIL — a fresh band above the
adjudicated frequency range condemned capâç (7 seats),
retaliazion (7 seats) and consapevui (7 seats), all
zero-attested and undisclosed. NOT LANDED; nothing committed.

## Round 4 (2026-11-27, later the same night) — deciding checker's map + full-pool adjudication

The deciding checker's findings are applied in full:
apresiatîfs → ricognossints (6:53, 7:17); sgarpade →
straçade (12:26, 12:27, 12:28); Rivelaments → Rivelazions
(3:98, with the article: lis Rivelazions); pintîs → pentîs
(9:3, ruled CONDEMNED as the unattested doublet); capâç →
capaci (41:22, 41:39, 42:29, 42:50, 43:18, 46:33 ×2, 48:21);
retaliazion → talion, the corpus word in the field (2:178,
2:179, 2:191, 2:194 ×2, 2:196, 2:211, 3:11, with agreement
adjusted seat by seat); consapevui re-seated on the savê
family seat by seat (6:81, 6:131, 6:156, 24:27, 24:31,
26:24, 39:55), and its singular consapevul at all 9 seats.

Beyond the map, the whole remaining untraced pool was
adjudicated (2,193 candidates; 610 prior rulings; 1,583
ruled this round — 1,444 ATTESTED-REGULAR, 3 FLAGGED
CONSTRUCTIONS, 136 CONDEMNED; remainder zero) and every
condemnation applied: 162 condemned forms standing at
application time, 190 verses changed, one new GAP (mustard,
31:16 — census now 59 seats / 67 markers). The application
set was built mechanically from the adjudication record and
spec coverage asserted before any swap ran; the zero-check
runs over the record's full condemned set (251 tokens, all
passes), case-insensitively, and returns NONE — quoted in
full in the attestation audit's round-4 section. Fifteen
bulk-tier passes on false-friend evidence were caught by
the lane's suspect scan and overridden to CONDEMNED in the
record with grounds stated (audit round-4 section).
Canonical re-verify after round 4: 6,236 = 6,236, per-surah
grid clean at all 114, Basmalah 1:1 exact, "redacted" NONE.
Manuscript re-assembled (848,987 bytes, SHA-256
31736cc4574599ff0a90225531b6f794a951f990e15ca3c947b38ca032ddc0f1)
and the pack re-staged. Full per-token record:
ayah-friulian/work/adjudication/ADJUDICATION-RECORD.json;
seat-level changes: work/adjudication/round4-changes.json;
zero-check: work/adjudication/zero-check-round4.txt.

## Round 6 (2026-11-28) — on the third deciding checker's prescription

Deciding checker 3 (CHECKER-REPORT-DECIDING3-2026-11-27.md)
passed Gates 1, 2, 3 and 5 and failed Gate 4 on three seated
rulings whose grounds rested on prefix/stem-string traces that
are not Friulian attestation — luserès, ruzave, rump — with the
desk's own admission that rumparà (3:9) cited the same false
trace. Round 6 executed the prescription in full:

1. **Named seats re-seated against the Locked English
   Master.** 24:35 luserès → lusarès (lusî family: Wiktionary
   lemma; Pirona headword Lusì). 69:6 ruzave → bruntulave and
   67:7 ruzâ → bruntulâ (Pirona part-2 "Brontolare —
   Bruntulà"; corpus bruntulant ×1). 2:80 and 2:256 rump →
   romp; 2:27 rumpin → rompin; 3:194 rumpis → rompis; 3:9
   rumparà → romparà (rompi: Pirona headword L58798; corpus
   romp ×17, rompin ×3). The phantom entry ingenoiin (0 seats)
   stands CONDEMNED on its true ground.
2. **Targeted ground sweep, exhaustive over the suspect
   class** — 1,621 of the 2,029 ATTESTED-REGULAR rulings whose
   grounds rest on family/prefix cites (pironafam, xmlfam,
   freqfam) or exact-attestation claims. A strict verifier
   (work/adjudication/sweep6.py) re-tested every cited form
   character-for-character: a Friulian form must show a
   lowercase occurrence in Friulian prose (capitalised-only
   traces fail as the proper-name class), an exact Friulian
   Pirona headword or part-2 Friulian form, a Wiktionary
   lemma, or a regular cell of a stem passing the same test.
   Arithmetic: 1,403 grounds verified as cited (two of them —
   luserès and ruzave — overturned on the deciding checker's
   firsthand evidence, which the machine cannot reach: a
   gazetteer headword and a noun standing for a verb); 145
   grounds corrected with the ruling standing (the cited forms
   do not re-derive as written; the token's own verified
   attestation is now the ground); 73 dossiers (32 FAIL6 +
   41 DOSSIER) ruled firsthand against the sources — 36 stand,
   most with grounds restated on quoted evidence, and 37 were
   CONDEMNED and re-seated on attested forms or reworded.
3. **Trace-sharing propagation.** The false Rump Parliament
   trace carried four rulings (rump, rumpin, rumpis,
   rumparà) — all condemned. The giud- dossiers exposed the
   whole giud- family: giudizi and giudicâ with all their
   cells (~75 seats) traced only through Pirona's Italian
   text and a verify-script waiver, while the corpus attests
   the jud- spelling (judizi ×37 bounded, judicâ ×8) — the
   family stands condemned whole and re-seated in the jud-
   spelling. A family screen over unrecorded seated tokens
   (57 suspects, 372 seats; the residue is irregular-verb
   cells, disclosed constructions, and attested variants)
   found one further unattested family: litig- (20 seats),
   condemned whole and re-seated on disputâ. The persever-,
   perseg-, boj-/buint and goce rulings propagated the same
   way.
4. **Totals.** 59 net-new CONDEMNED rulings (the set grows
   362 → 421; 58 seated, plus the ingenoiin phantom); 167
   grounds corrected with rulings standing (145 regenerated +
   22 hand-restated); 48 new ATTESTED-REGULAR entries for the
   re-seated forms. Application built mechanically from the
   record (58 condemned tokens with seats; spec coverage
   asserted before any swap): 137 token substitutions and 12
   phrase rewordings; 132 verses changed. Zero-check over the
   full updated CONDEMNED set (421 tokens), case-insensitive:
   NONE left over (work/adjudication/zero-check-round6.txt).
5. **Canonical re-verify after round 6:** 6,236 = 6,236,
   per-surah grid clean at all 114, GAP census unchanged
   (59 seats / 67 markers — no re-seat opened a GAP),
   Basmalah 1:1 exact, "redacted" NONE. Manuscript
   re-assembled (849,218 bytes, SHA-256
   94f83486da2c5dec9127af4360420cfc6fece185fa612b992c261832d021106d)
   and the pack re-staged. Full per-token record:
   work/adjudication/ADJUDICATION-RECORD.json; seat-level
   changes: work/adjudication/round6-changes.json.


## Round 7 (2026-11-28) — on the fourth deciding checker's prescription

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

Full per-token record: work/adjudication/ADJUDICATION-RECORD.json; seat-level changes: work/adjudication/round7-changes.json; zero-check: work/adjudication/zero-check-round7.txt; sweep machinery and results: work/adjudication/sweep7.py, sweep7b.py, sweep7c.py, sweep7-results.json, sweep7b-results.json, sweep7c-results.json; the 251 firsthand dossiers: work/adjudication/dossiers7.txt.


Correction (dated 2026-11-28, on deciding checker pass 5's finding): the round-7 grounds-restated tally given above as 688 is corrected to 696, the fresh deciding checker's independently derived count (CHECKER-REPORT-DECIDING5-2026-11-28.md, Gate 5). The discrepancy is a descriptive tally only; it touches no seat, ruling, or ground.
