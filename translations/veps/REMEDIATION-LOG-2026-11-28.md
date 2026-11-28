# Veps Remediation Log — 2026-11-28

Executed under Robert's audit-application standard (2026-11-27) on the findings of
CHECKER-REPORT.md. The frozen first build is preserved at
`work/remediation/verses-store-PRE-REMEDIATION.json`. Working store and all patch
files are in `work/remediation/`.

## 1. Fidelity repair

- **2,214 of 6,236 verses changed** against the frozen build; **1,556 verses fully
  re-rendered** from the Locked English Master (patch-12a/b, 13, 14, 15, 16a/b, 17a/b,
  18a/b, 19a/b, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37a/b), the rest by the token
  pass and the finalize sweeps.
- All **18 named fidelity-failed verses** (27:23, 36:60, 37:162, 28:31, 29:12, 30:36,
  31:28, 33:73, 13:2, 13:35, 15:47, 16:15, 17:65, 32:2, 34:8, 35:15, 14:7, 12:93) are
  inside the re-rendered surahs.
- Systematic pass: a collapse classifier (Veps/Master token ratio + function-word
  share, validated against known-good and known-bad batches) flagged **797 verses**,
  concentrated in surahs 12–19 (172) and 27–37 (595). Surahs 27–37 were re-rendered
  essentially whole; surahs 12–19 likewise; the ~30 scattered flags elsewhere were
  judged verse by verse (nearly all sound — tiny verses; three repaired: 20:97, 51:56,
  68:18).

## 2. Token adjudication repair

Zero SUSPECT tokens remain book-wide (final residue scan). Adjudications:

| Family | Disposition |
|---|---|
| kield-/kielt-/hülgä- | → kelʹta family, form-for-form (147 + 49 + hülgä seats; paradigm from dict-rus-vep XML, запрещать) |
| kärzind-/kärsind-/kärsi- | → tirpta constructions, seat by seat (incl. 21:85, 22:35, 25:20, 25:42, 20:130, 20:132) |
| -nug singular participles | → -nuded norm: 151 tokens in the finalize sweep plus the token-pass conversions; freq-attested -nugoi plurals stand (uskonugoi → usknugoi) |
| selʹkt- | → selʹged family; 25:33 → selʹgenzoituz (disclosed derivation) |
| päiči | → vaiše; postposed possessor seats → sijas; 48:27 → ližaks |
| tyo (41) + tyospäi (47:16) | → allative -le / läz / polele / -päi per seat |
| päi (free) | → bound -späi (book's attested elative forms) |
| rauh | → mir (greetings, sakina, Abode of Peace) / kožmuz (reconciliation) |
| mörinä | → pätetud / pätanuh constructions |
| maistta | → mujada family; 6:141 → magu |
| jokčč- | → joga/jogahine family |
| ilma | prose seats deleted or restructured; "ilma + abessive" seats (27:12, 28:32, 28:39, 28:50, 30:29, 31:6, 31:20, 32:2) → bare abessive |
| hüvästʹtud (blessed adj.) | no attested replacement: 4 seats → ⟦GAP: blessed⟧ (21:50, 23:29, 24:35, 24:61); 6 judgment seats → Kitketud (book's attested "Praiseworthy" epithet pattern); hüväst- verb family (batch D/G/H seats) → kitta family (glorify), melhe constructions (approve), hüvüt constructions (benefit), kitketud (blessed land, 21:71/81), arvosta (honour, 22:18), valinnuded (24:55) |
| välleng-/heikendel- | → välleta forms; 3:146 antonym restructures (logged judgment seats); 47:35 → ala välleta |
| perindon (89:19) | → ⟦GAP: inheritance⟧ (no attested form) |
| veka | → vedä (40:8, 44:47) |
| kogokoi (75:3) | → keragoi construction |
| estai (50:25) | → heitai (disclosed -i agent construction on attested heitta) |
| kiälta (19:82, batch C) | → kelʹtaba |

**Disclosed flagged constructions introduced by the remediation** (regular derivations
on attested stems, kirjutai/sudii pattern): kelʹtai, kelʹtand, tirptai, tirptand,
tirptajad, heitai, selʹgenzoituz / selʹgenzoitta agent forms, libutamine
("Libutamižen Päiv", from book-attested libuta-), voittand, eläbetai (30:50),
pidämižen (31:22), muštelend (the Reminder).

**Judgment seats logged:** Kitketud for "blessed" at 22:24, 22:64, 23:14, 25:1, 25:10,
25:61 and adjectivally at 34:18; "God blesses a person" verb seats → hüvüden andand
(37:113/114, 18:65 pattern); 3:146 antonym seats; 74:51 lev seated (W-attested, was
wrongly GAPped); 19:52 wrong ⟦GAP: horse⟧ (for the Mount) removed.

## 3. Disciples seats

openikad seated at **3:52, 5:111, 5:112** (checker-verified attestation: Wiktionary
lemma, GiellaLT dict-rus-vep, GiellaLT frequency list). The three ⟦GAP: disciples⟧
markers are gone.

## 4. GAP census reconciliation

Frozen: 495 seats / 692 markers / 323 terms → Remediated: **551 seats / 760 markers /
330 terms** (verify.py and assemble.py agree; counted mechanically from the store).

- Terms removed: disciples 3 (seated), ancestor 6 (→ tatad descriptive, "fathers who
  were before"), lion 1 (lev seated), horse 1 (error corrected).
- Terms added by fidelity re-renders (originals had dropped or borrowed the content):
  tar 3, blessed 5, ants 2, ant 1, spider 2, bee 1, hoopoe 1, breastfeeding 1, bush 1,
  bricks 1, pens 1, armor 1, statues 1.
- Judgment-GAP seats absorbed by fuller attested renderings inside re-rendered
  verses, disclosed for the checker's adjudication: well 6→2, measure 7→4, mouth 1→0
  (13:14), weight 1→0 (18:105, jügedus), generation 4→3, descendants 5→4, cave 11→9,
  provisions 5→4.
- Count growth in standing terms (oath 24→37, curse 7→17, jinn 16→27, semen 1→6,
  dust 1→7, fruit 8→12) is the fidelity repair surfacing content the collapsed
  originals had dropped; each such seat now carries the book's standing GAP term.

## 5. Mechanical gates after remediation (desk-run)

- Canonical verify: 6,236 = 6,236, per-surah mismatches NONE.
- Apostrophe audit: only U+02B9 (three ASCII apostrophes in surah 27 found and fixed).
- Angel seats: 86 (unchanged, matches aggregate).
- 1:1 = seated basmalah. Cyrillic: none. Bare "keske": none. "sspäi": none.
- Manuscript reassembled: ayah-companion-manuscript-VEP.md — 5,685 fully rendered
  verses + 551 GAP seats = 6,236.

## 6. What the fresh checker must still rule on

The remediation desk does not grade its own work. Open for the independent checker:
fidelity of the re-renders on a fresh long-verse-weighted sample; the disclosed
constructions and judgment seats above; the absorbed well/measure/mouth/weight GAP
seats; vinmarjoidenke (36:34); kelastades (69:44); Kaclei (25:20); the -nugoi
non-frequency forms left standing on attested stems.

## ADDENDUM — 2026-11-28, after the fresh checker pass

The independent checker (CHECKER-REPORT-REMEDIATION-2026-11-28.md) ruled Gates 1–4
PASS and **Gate 5 FAIL** on a bounded residue the first token pass missed because it
matched lowercase only. The log's claim "zero SUSPECT tokens remain" was WRONG when
written and is corrected here, not edited above. Residue found by the checker and
cleared the same day (checker-verified findings, applied under the audit-application
standard):

- Päiči sentence-initial ×9 (38:74, 38:83, 43:27, 44:42, 60:4, 70:22, 70:30, 72:23,
  72:27) → Vaiše.
- Jokčč- capitalized ×8 (7:38, 7:134, 7:160, 9:8, 9:122, 9:124, 10:12, 10:47) →
  jogahine family.
- Kärsi/Kärzii ×3 (64:17, 73:10, 76:24) → tirpta constructions; Hüvästa imperatives
  ×2 (87:1, 110:3) → Kitä; Maista ×1 (44:49) → Muja.
- Free päi ×9 (12:24, 12:33, 12:34, 15:34, 19:16, 33:10, 34:51, 34:52, 34:53) →
  bound -späi forms / hänespäi, minuspäi restructures.
- sanug as singular participle ×2 (12:80, 18:76) → sanunuded. (sanug "Say:"
  imperative ×116 stands, paradigm-adjacent to freq-attested sanugaha/sanugat —
  checker's ruling.)
- palʹm-: the checker failed palʹmidenke at 36:34 (no harvested source; palm is a
  STAYS GAP term). Applied book-wide for consistency: 36:34 plus the six standing
  batch seats (20:71, 23:19, 26:148, 54:20, 55:11, 55:68) and 69:7 → ⟦GAP: palm⟧
  forms. Palm markers now 15.
- voitt-/voittand family (24 seats): stem untraced in every harvested source —
  replaced by sense: "can/able" seats → voida forms (12:43, 14:21, 42:31, 47:22);
  "overcome" seats → vägestada forms (56:60, 70:41, 54:10 vägestetud); "victory"
  seats → vägestajad / vägestuz (30:3, 37:116, 37:173, 28:35, 33:71, 61:14);
  "prosper/succeed" seats → päzuta / päzujad (12:23, 16:116, 28:37, 28:67, 28:82,
  30:38, 31:5, 58:22, 59:9, 59:20, 64:16). vägestada/vägestai/vägestetud are
  regular derivations on dict-attested vägestuz (победа → vägestuz) — the family
  already stands in the book at 4:75, 5:56, 6:61 (Vägestai), seats the checker
  passed; päzui is the -i agent of book-used päzuta. Both disclosed here and in
  glossary §K.
- Corrections to §5 of this log: (a) "bare keske: none" was wrong — three
  punctuation-shielded instances stood (17:53, 18:93, 34:54); now keskes. The
  checker graded the point a form note only. (b) kelʹtai, disclosed in §2 as a
  paradigm form, occurs in zero seats (kelʹtand is the seated form, attested in
  the dict's own example sentence — checker's finding).
- Census after residue repair: **558 seats / 768 markers / 330 terms**; verses
  changed vs frozen: **2,249**. verify.py re-run: grid equal, apostrophes clean,
  angel 86, basmalah seated. A fresh delta checker pass on Gate 5 was commissioned;
  its report governs landing.

## ADDENDUM 2 — 2026-11-28, after the delta checker pass

The delta checker (CHECKER-REPORT-DELTA-2026-11-28.md) confirmed every item of
Addendum 1 — all predecessor residue zero on a case-insensitive sweep, all repaired
seats verified against the Master, vägest- and päzu- families ruled SEATABLE on
attestation stronger than claimed (vägestada and vägestai attested outright in
dict-rus-vep; päzui frequency-attested ×14) — and confirmed the mechanical gates
and the 558/768/330 census. It ruled Gate 5 FAIL on two further seats, both
pre-dating the remediation in batch G: **selʹgenzim at 57:17** and
**selʹgenzusidenke at 64:6**, bare-stem forms of the batch-C coinage selʹgenz-.
Repaired the same day: 57:17 → selʹgenzoitim (past of attested selʹgenzoitta);
64:6 → selʹgenzoitusidenke (of sanctioned selʹgenzoituz). Book-wide sweep for
bare selʹgenz(?!o): zero remain. Census unchanged (558/768/330); verses changed
vs frozen now 2,251. A second delta checker pass was commissioned; its report
governs landing.
Correction to Addendum 2's count, same day: verses changed vs frozen are **2,250**
(mechanical count after the two-seat repair; one of the two seats already differed
from the frozen text). The figure 2,251 above stands corrected here.

## ADDENDUM 3 — 2026-11-28, after the second delta checker pass

The second delta checker (CHECKER-REPORT-DELTA2-2026-11-28.md) confirmed the
two-seat selʹgenz repair, confirmed the full commissioned SUSPECT sweep clean for
the first time, and confirmed all mechanical gates and the census — but its wider
sentence-initial hunt (867 capitalised sentence-initial forms screened; the 81
never-lowercase forms checked one by one against every harvested source) found ten
further tokens of the same case-mode, and ruled Gate 5 FAIL. Repaired the same day:
Joka → Jogahine (74:38, 74:52, 80:37, 81:14, 82:5), jokale → jogahižele (104:1),
Silloin → Siloi (38:10; siloi is the attested lemma), Päinvastoin → restructured
"No loiče Jumalad" (39:66), Olles → Oldes (33:19, 35:43 — Olles was introduced by
the remediation's own re-renders; oldes is frequency-attested ×61). The checker's
form note Sinanvedäjid (6:10) was also corrected to Sananvedäjid. Census unchanged
(558/768/330); verses changed vs frozen now 2,259. Items the checker named but did
NOT grade (küž- ž-variant ×22; the never-adjudicated epäil-, valehtelij-, ihmeh-,
hänelle, judalai- families) are referred, untouched, and recorded in its report §5
for a future adjudication — they are outside the commissioned gate. A third delta
checker pass, replicating the wider hunt independently, governs landing.

## ADDENDUM 4 — 2026-11-28, after the third delta checker pass

The third delta checker (CHECKER-REPORT-DELTA3-2026-11-28.md) verified all eleven
Addendum-3 seats, the full SUSPECT sweep, and all mechanical gates and census
figures — and ruled Gate 5 FAIL on three further sentence-initial tokens from its
own wider hunt (880 forms; 208 never-lowercase screened): **Sama at 2:233**
(Finnish/Karelian "same", unattested) → Se-žo; **Vird at 13:17** (Karelian-shaped
"current") → Josmuz (the dict's own Veps equivalent for течение); **Saan at
11:72** (Finnish 1sg of saada) → San (frequency-attested ×23). Its five form
notes were normalised in the same pass: Miks → Mikš (74:49, 95:7), Nis → Niš
(98:3), Eisa → restructured (52:33), Kuverz → Kuverzʹ (7:4), Minele → Minei
(14:22). A split token in the original 2:233 ("küzu s") was also repaired
("ühtes pagiždes"). Census unchanged (558/768/330); verses changed vs frozen now
2,262. A fourth delta checker pass, replicating the wider hunt independently,
governs landing.
Correction to Addendum 4's count, same day: verses changed vs frozen are **2,266**
(mechanical count; the form-note seats were previously unchanged verses). The
figure 2,262 above stands corrected here.

## ADDENDUM 5 — 2026-11-28, GATE 5 PASS and landing

The fourth delta checker (CHECKER-REPORT-DELTA4-2026-11-28.md) ruled **Gate 5
PASS**: all Addendum-4 seats verified; its independent wider hunt (882
sentence-initial forms, 207 never-lowercase screened, plus all 1,410 capitalised
non-initial forms) found no residue; the full SUSPECT sweep stands clean for the
third consecutive pass; mechanical gates and census (558/768/330, palm 15;
2,266 verses changed vs frozen) confirmed exactly. With Gates 1–4 passed by the
first checker (canonical, census, fences, fidelity — 46-verse fresh sample, zero
failures), every gate stands passed and the book lands on the GitHub shelf under
the Pipeline Landing Authorization, labelled DRAFT — NOT PUBLISHED. Referred
ungraded items (küž- variant; epäil-, valehtelij-, ihmeh-, hänelle, judalai-
families) remain on the record in the checker reports for a future adjudication;
they were outside the commissioned gate in every round.
