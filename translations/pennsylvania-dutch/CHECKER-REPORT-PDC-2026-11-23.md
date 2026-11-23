# Independent Checker Report — Pennsylvania Dutch (Deitsch) Quran
**Date:** 2026-11-23 · **Checker:** independent pass (did not build the manuscript)
**Manuscript checked:** `ayah-companion-manuscript-PDC.md` — 6,236 verses (count re-verified by my own parse: 6,236 PDC verse headings, 6,236 in the English master; no verse missing or duplicated in the parse)

## Verdict: PASS WITH CORRECTIONS

The book is a real Deitsch rendering in the Bible's frame — grammar, pronouns, perfect tense with *hott/henn* + k-participles, and vocabulary are the control's throughout, with zero standard-German leakage (my token scan of all verse text: *und* 0, *ist* 0, *nicht* 0, *von* 0) and zero English leakage. It does not pass clean, because a set of systematic spelling variants departs from the control's forms at scale, and the divine name ar-Rahman is rendered three different ways at the seats where the master's English itself varies, one of them an unattested coinage. Every correction required is mechanical and is listed exactly in §7. No correction touches a verse's meaning except §4's name seats, where the fix restores the brief's locked terminology.

**How each claim below was checked** (house rule: an instrument output is a candidate, not a conclusion): I parsed the manuscript and the master myself, counted every variant form in the manuscript against word-boundary counts in `bible-control-text.txt` and verse-level reads in `bible-verses.json`, checked dictionary attestation by grepping Lambert (1924) and Lins (1895) directly, read a 42-verse language sample verse-by-verse against the master, and read all 13 flag files in full.

---

## 1. Language sample — 42 verses

Sample: at least 2 verses per chunk range, including long legal verses (2:282, 4:11, 5:6), narrative (12:4, 12:86, 19:16, 28:15), and short late surahs (93, 103, 112). Grades: **(a) 31 · (b) 11 · (c) 0.**

**(a) Real Deitsch in the Bible's spelling and grammar — 31 verses:** 1:1, 1:7, 2:2, 2:62, 2:153, 4:11, 4:135, 5:44, 6:151, 7:54, 8:46, 12:4, 12:86, 14:35, 16:90, 18:29, 19:16, 19:33, 20:14, 21:107, 28:15, 28:77, 36:58, 40:60, 48:29, 55:26, 67:1, 78:1, 93:1, 103:1, 112:1.
Evidence: 12:86 — „Ich beklawg yo blos mei drau un sorg zu Gott, un ich vays funn Gott, vass diah nett visset" (*vays/vayst* is the control's own "know" paradigm: Gen 3:5 "Gott vayst"). 19:33 — "So is Freed uf mia, am Daak vo ich geboahra voah, un am Daak vo ich shteahb, un am Daak vo ich levendich uffashtay" — clean except the *Daak* spelling ruled on in §2. 4:11 renders the full inheritance fractions completely and correctly in descriptive Deitsch.

**(b) Deitsch frame with spelling drift, coinage, or uncertain lexis — 11 verses:** 2:255 (*vees*, §2.8), 2:282 (*sawva*, §2.6), 3:7 (*vees*), 3:19 (see §3), 4:34 (*gayyich*, §2.2), 5:6 (*veisht* "wipe" — the control's *veist* means "shows"; the wiping verb is uncertain lexis, meaning still clear), 10:90 (*dass*, §2.5), 24:35 (*vist*, §2.8), 25:63 (*saage* "they say", §2.9; and *Bamhatzicha* for ar-Rahman, §4), 33:40 ("am visse funn allem" — awkward nominalised "know" form, meaning intact), 55:1 (§4).

**(c) Effectively not Deitsch — 0 verses.** No sampled verse, and no verse found by the whole-book German/English token scan, is standard German or English in disguise.

**On the desk's 83.87% token-attestation figure:** I judge it a harvest artifact, not a quality measure. The harvest is surface forms; the single largest blocks of "unattested" tokens are precisely the systematic variants in §2 (daak 460, sawva 208, iahna 175, dass 173, vees/veess 123, avver 106, kumt 66, gayyich 49 — together ≈1,360 tokens) plus inflected forms and Quran-only proper names. After the §2 conforms are applied, the attested share rises materially. The number is not a ground for failure; the variants themselves are the finding, and they are correctable mechanically.

---

## 2. Variant rulings (apply mechanically; counts are my own recounts)

Control citations are from `bible-verses.json` (Di Heilich Shrift).

1. **daak (460) → CONFORM to `dawk`.** Control: *dawk* 1,815, *daak* 0. Citation: Gen 1:5 — "Gott hott di helling "dawk" kaysa… da eahsht dawk."
2. **gayyich (~49) → CONFORM to `geyyich`.** Control: *geyyich* 1,692, *gayyich* 0. Citation: Gen 2:8 — "en goahra geblanst in Ayden geyyich di east."
3. **kumt (66) → CONFORM to `kumd`.** Control: *kumd* 727, *kumt* 0. Citation: Gen 10:30 — "biss ma an Sephar kumd."
4. **avver (106, chunks 007–010 only) → CONFORM to `avvah`.** Control: *avvah* 4,609, *avver* 0. Citation: Gen 2:6 — "Avvah en nevvel is als ruff kumma…" The rest of the book already writes *avvah* (1,203 in the manuscript); this is one worker's drift.
5. **dass (173, chunks 007–010 and 021–026) → CONFORM to `es`.** The control writes the conjunction *es* (21,955) and never *dass*. Note for the record: Lambert does attest the dialect form — headword *ass*, "ass = dass (conj), that. G dass" — so *dass* is a real dialect word, dictionary-grade. The brief, however, makes the Bible's spelling govern ("the Bible's spelling governs"), and the rest of the book writes *es*; uniformity on the governing authority wins. Ruling stands as CONFORM.
6. **sawva (208) → CONFORM to `sawwa`.** Identification: *sawva* is "they say" (present plural of "say"). The control's form is *sawwa*, 963 occurrences, *sawva* 0. Citation: Gen 10:9 — "Fa sell, sawwa di leit…"; Gen 12:12 — "sawwa si, 'Dess is sei fraw.'" The manuscript itself writes *sawwa* correctly 70 times elsewhere. The v-for-w spelling is a drift, not a dialect form: neither dictionary attests *sawva*.
7. **iahna (175, surahs 40–74) → CONFORM to `eena`.** Identification: *iahna* is the object pronoun "them." The control writes *eena* (2,130 in the control text; 976 already in the manuscript) and never *iahna* (0 in control, absent from the attested lexicon). Citation: Gen 6:1 — "mayt geboahra vadda zu eena." *Iahna* is a blend of *iahra* ("their") and *eena*, unattested in Bible, Lambert, and Lins.
8. **vees (85) / veess (38) → CONFORM to the control's "know" paradigm: `vayst` (he/she/it knows), `vissa` (to know / they know).** The control's forms: *vayst* 148 (Gen 3:5 "Gott vayst"; Jos 22:22 "Eah vayst"), *vissa* the infinitive/plural (Gen 15:8 "vi kann ich vissa"). Neither *vees* nor *veess* occurs in the control (0) or the attested lexicon. The split is chunk-shaped: *vees* in chunks 001–003/007–010 and late chunks, *veess* only in chunk 004–006 (e.g. 4:25–26 "Gott veess") — two workers, one error. Same ruling for the related form **vist (34) → `vayst`** (e.g. 24:35 "Gott vist alles" → "Gott vayst alles"). The manuscript already uses *vays/vayst* correctly 82 times.
9. **saage (105, found by this check at scale) → CONFORM to `sawwa`** where it means "they say" (e.g. 25:63 "saage si: 'Fridda'" → "sawwa si"). *Saage* is the German-shaped form; the control has no *saage/saag* present-plural seat (its paradigm is *sawwa* / *ksawt*).

No other systematic variant at scale was found: *dawk, geyyich, kumd, avvah, eena, vissa* all also appear in their correct control forms in other chunks, confirming these are per-worker drifts, not a second orthography.

---

## 3. Fidelity spot-check — 10 verses against the master, word by word

Checked: 2:255, 4:34, 5:6 with its note, 24:35, 55:1 (required), plus 3:7, 3:19, 12:86, 21:107, 48:29.

- **2:255 — faithful.** Every clause present: Living/Sustainer ("da Levendich, da Halda"), slumber/sleep, intercession by permission, before/behind them, knowledge grasped only as He wills, Throne over heavens and earth, no burden, Most High/Great. *Drohn* (Throne) is dictionary-grade per the worker's own flag; meaning unshifted. Only defect is the *vees* spelling (§2.8).
- **4:34 — faithful, including the hard seat.** "Strike them" is rendered as the master reads ("dann shlohgt si"), neither softened nor strengthened; protectors/maintainers, advantage, spending, admonish → abandon in beds → strike, "if they obey you seek no way against them," Sublime/Great — all present, nothing added.
- **5:6 — faithful, and the translator's note is faithfully carried.** The note in the manuscript — "*[Manche layysa veida dess ma veisht biss zu dee feess; di laysung vo do gedrukt is sawgt vasha.]*" — says exactly what the master's note says ("Some readings continue the wiping to the feet; the reading printed here says wash"), in the same position. The verse body keeps wash/wipe exactly where the master puts them, the impurity/illness/travel/toilet/contact sequence, and the clean-earth provision complete.
- **24:35 — faithful in substance.** Niche, lamp, glass, brilliant planet, blessed olive tree neither eastern nor western, oil almost illuminating untouched by fire, Light upon Light, guidance, parables — all present. Two form defects: *vist* (§2.8) and "Gott gevva so di Gleichnissa" (present-shaped *gevva* for the master's "thus cites") — a tense wobble, not a meaning change.
- **55:1 — meaning shifted by terminology, see §4.** The master's "The Compassionate" (ar-Rahman) is rendered "Da Bamhatzich" (the Merciful, ar-Rahim's locked term). One word, but it is the surah's title-word and the wrong member of the locked pair.
- **3:7 — faithful; the master's own ambiguity is preserved, not resolved.** The master leaves "except God and those firmly rooted in knowledge say…" grammatically open; the Deitsch keeps the same openness. Not a defect.
- **3:19 — one genuine shift.** The master's "Religion with God is Islam" becomes "Da Glawva bei Gott is Hingevving" — *Glawva* is "faith/belief," narrower than "religion." The *Hingevving* (submission) rendering of "Islam" is the disclosed descriptive device used consistently (flagged at 3:67) and is defensible; the *Religion → Glawva* narrowing is not flagged and should be noted as a minor shift. Meaning is dented, not reversed.
- **12:86 — faithful, clean.**
- **21:107 — minor narrowing.** "Mercy to mankind" → "Bamhatzichkeit foh di Leit" ("mercy for the people"). The locked "worlds" form was not owed here (the master says "mankind," not "the worlds"), but "di Leit" is narrower than "mankind." Minor.
- **48:29 — faithful in substance; two small softenings.** "Seeking blessings from God" → "Goodness funn Gott… sucha" (blessings → goodness) and "a great reward" → "en grohsi Bezahlung" (reward → payment). Neither reverses meaning; both are noted, neither is a correction I require.

**Net fidelity finding:** no verse in the check lost a clause, added a doctrine, or reversed a meaning. The only required fidelity correction is §4.

---

## 4. Divine names and locked terms

*Gott* and *da Hah* are consistent throughout (no exceptions found in the sample or the name scans). The Basmalah is uniform — "Im nohma funn Gott, da Gnaydich, da Bamhatzich" — at all 115 Basmalah seats my count found (112 surah openings + surah 1's verse + 27:30's in-text Basmalah and repetitions), matching the locked pair *da Gnaydich* (ar-Rahman) / *da Bamhatzich* (ar-Rahim).

The failure is exactly where the master's English itself varies, as the task suspected:

| Seat | Master | Manuscript | Judgment |
|---|---|---|---|
| 2:163 | "the Benevolent, the Compassionate" | "da Gnaydich, da Bamhatzich" | **Defensible and correct in effect.** Both English words name the Rahman/Rahim pair in reverse dress; the manuscript maps the pair onto the locked pair. The seat reads as the Basmalah pair, which is what the Arabic pair is. No correction. |
| 55:1 | "The Compassionate" | "Da Bamhatzich" | **Not defensible.** The Compassionate is ar-Rahman; the locked term is *da Gnaydich*. The manuscript gives ar-Rahim's name to ar-Rahman's seat — and this is the title verse of Surah ar-Rahman. Correct to "Da Gnaydich." |
| 59:22 | "the Compassionate, the Merciful" | "da Mitgefeelsich, da Bamhatzich" | **Not defensible.** *Mitgefeelsich* is a coinage (Mitgefühl + -ich): 0 in the control, absent from the attested lexicon, attested in neither dictionary. Correct to "da Gnaydich, da Bamhatzich." |
| 67:3 | "the Compassionate" | "da Mitgefeelsich" | **Not defensible** — same coinage. Correct to "da Gnaydich." Also at 67:19, 67:20, 67:29 (same master's word, same coinage, found by my scan). |

Elsewhere the manuscript handles the master's variation correctly: where the master writes "the Benevolent / the Beneficent" for ar-Rahman (13:30, 21:112, 36:11, 41:2, and 25 more seats — 29 *Gnaydich* seats in total), it writes *da Gnaydich* consistently. So the book has three competing treatments of one name — locked *Gnaydich* (29 seats, correct), *Bamhatzich* (55:1, wrong member of the pair), *Mitgefeelsich* (5 seats, coinage) — and the correction is to bring the 6 deviant seats onto the locked term the other 29 already use.

All other locked terms spot-checked hold: *Oahma-Geld* for charity/alms, *Gebayt/bayda*, *Fashta*, *Bayt-Haus*, *Koran*, *di Shrift / es Buch* matched to the master's word, *dee Glawvicha / dee Unglawvicha*, *Heichlah*, *Gott sei Kshikta*, *Brofayt*, *Goahra / Paradees*, *Feiyah / Hell*, *Engel*, *Geisht*, *Sayl*, *Bund*, *Zaycha*, *es Gricht*, *Uffashtayung*, *Effangaylium*, *Torah*, *da Hah funn di Velda*, *da Awlmechtich*.

---

## 5. Quran-alone discipline — PASS

Checked by full-manuscript scans plus the sample read: no percentage anywhere (scans for `%`, *Prozent*, "2.5", tithe/tenth forms: all 0); the word *zakat* never appears and no rate is attached to *Oahma-Geld* at any seat; no hadith material (scan for *hadith*: 0; the 3 substring hits for "sunna" are parts of ordinary Deitsch words, e.g. *di Sunn*, not the tradition term); no traditional specifics (names, dates, ritual details) appear in any sampled verse that are not in the master. Where the master is silent, the Deitsch is silent.

---

## 6. Flags review — 220 flags, all 13 files read

Count re-verified: the 13 files carry 220 flag entries (16+14+15+12+19+14+15+16+16+18+19+22+24).

My classification, by reading each flag against the sources:

- **Settled by attestation in the sources — ≈150.** These are the brief-required first-use flags for the locked devices (*Gott sei Kshikta* on attested *kshikt*; *Bayt-Haus* on Mt 21:13 "house of prayer"; *Koran* as the locked loanword), dictionary-grade forms (e.g. 2:61 *Gnoblich/Linsa*; 90:15 *Vaysa-Kind* on Lins's "Weisa kind, orphan"; 90:13 *Badeenda* on Lins's *badeena*), and descriptive compounds built on attested bases (*senf-sohma*, *Kamel-Weib*, *heiraht-geld*). The attestation the flag claims is real in each case I tested.
- **Disclosed uncertainties, no defect — ≈65.** Honest flags where no attested word exists and a descriptive phrase carries the seat complete (Night of Decree, atom's weight, forelock, hamstringing, the Hereafter phrase "es Layva noch demm Doht"). These are the brief's own prescribed fallback, disclosed as required. They stand.
- **Genuine defects — 5 flags describe a form I judge wrong, not merely uncertain:**
  1. **24:58 — "Pubertät"** for puberty: a standard-German loanword in German spelling, attested in no source, and not the descriptive phrasing the brief prescribes. Wrong form.
  2. **22:17 — "di Zoroastrians"**: the master's English word carried over unchanged. Violates the attested-forms rule the flag itself invokes; a descriptive rendering was owed.
  3. **95:1 — "di Olliv"**: loan-form for the olive, flagged as unverified; Lins attests only *Bawm-olich* (olive oil). The fruit form is a coinage as it stands.
  4. **109:2 — "ahbayt"** for "I do not worship": the flag concedes the control form was never verified; the form as printed is not the control's worship verb. Uncertain lexis presented as text.
  5. **27:87 — "posaun"** is flagged as unverified; I record it as a defect of verification only — the desk should confirm the control's trumpet form before landing, since the worker did not.

The most serious terminology defect in the book — *Mitgefeelsich* at 59:22 and 67:3/19/20/29 (§4) — appears in **no flag file**. The flag system caught spelling-level uncertainty well and missed the one systematic coinage. That gap is noted for the desk's process record; it does not change the verdict, because the coinage is correctable under §7.

---

## 7. Corrections required (for the desk to apply from these rulings; the checker has not edited the manuscript)

1. `daak` → `dawk` (460 occurrences).
2. `gayyich` → `geyyich` (~49).
3. `kumt` → `kumd` (66).
4. `avver` → `avvah` (106).
5. `dass` → `es` (173).
6. `sawva` → `sawwa` (208).
7. `iahna` → `eena` (175).
8. `vees` / `veess` → `vayst` or `vissa` seat-by-seat per §2.8 (123 total); `vist` → `vayst` (34).
9. `saage` → `sawwa` where it means "they say" (105).
10. 55:1: "Da Bamhatzich" → "Da Gnaydich". 59:22, 67:3, 67:19, 67:20, 67:29: "da Mitgefeelsich" → "da Gnaydich".
11. 24:58: replace "Pubertät" with a descriptive Deitsch phrase (e.g. the age of growing up, phrased on attested words) — desk to render and disclose. 22:17: replace "di Zoroastrians" with a descriptive rendering — desk to render and disclose. 95:1 and 109:2: verify the form against the control/dictionaries and conform or replace descriptively. 27:87: verify the control's trumpet form and conform.

After corrections 1–10 are applied mechanically and 11 is rendered, the manuscript in my judgment meets the build's own standard: attested forms only, the Bible's spelling, locked terminology uniform, fidelity to the master intact, Quran-alone discipline kept.

*— Independent checker, 2026-11-23*
