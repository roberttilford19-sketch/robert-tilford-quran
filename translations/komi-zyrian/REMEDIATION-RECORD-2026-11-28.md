# Komi-Zyrian (kpv) Quran draft — REMEDIATION RECORD (2026-11-28)

Crew stance: this crew built none of the text under remediation.
It applied the verified findings of
CHECKER-REPORT-INDEPENDENT-2026-11-28.md (verdict FAIL; GAP tier
separately ruled PASS-WITH-GAP-TIER-RESERVATION, §9 of that
report) in full, most serious first, under the
audit-application standard. No GAP-reduction pass was required
or made. Script: work/remediate-2026-11-28.py (asserted,
counted replacements; it aborts on any unexpected count), with
its seat-level log at work/remediation-log-2026-11-28.json.
Pre-remediation store preserved before any edit at
work/verses-store-PRE-REMEDIATION.json (md5
5d24591b32d8486b2e55dbbf661f8e66, identical to the build's
verses-store.json at preservation). The same edits were applied
to verses-store.json and to the work/batch-*.json sources, so
the lane cannot regress on a re-merge; the book files were then
rebuilt with build.py and assemble.py. Seats changed against
the pre-remediation store: **1,176**.

**Status after this record: DRAFT — NOT PUBLISHED. Nothing was
landed, shelved, committed, or pushed. Landing waits on a fresh
independent re-check PASS, which has not been run.**

## 1. Retained Latin tier (checker §4 — the FAIL ground) — CLOSED

Pre-remediation census (recomputed by this crew, matching the
checker's figures exactly): 470 Latin types / 1,945 tokens in
the verse text, of which the proven non-name class (checker
Classes A/B) was 219 types / 484 tokens / 438 seats, beside the
capitalised epithet tier headed by Hereafter ×101. Every such
token was closed seat by seat, on whitespace tokens with GAP
interiors excluded, under one rule: a token is **kept** only if
it stands on the explicit allowlist below; a token on the
device map is **seated** on its attested Komi-Zyrian form;
every other token is **GAP-marked** ⟦GAP: <term>⟧.

**Kept — the named allowlist (128 types, 1,052 tokens).**
Personal names and carried designations of named individuals:
Moses, Abraham, Noah, Mary, Jesus, Joseph, Pharaoh, Adam,
Aaron, Isaac, Solomon, Jacob, David, Ishmael, Shuaib, Saleh,
Hud, Zechariah, John, Jonah, Job, Gabriel, Michael, Imran,
Goliath, Saul, Elisha, Enoch, Elijah, Ezekiel, Luqman, Ezra,
Elias, Azar, Harut, Marut, Zaid, Ahmad, Muhammad, Malek,
Christ, Messiah, Hamaan, Quaroon, Samarian, Zul, Qarnain, Gog,
Magog, Tubba, Abee, Lahab, Baal, Lat, Uzza, Manat, Wadd, Souwa,
Yaghoos, Yaooq, Nassr, Bahirah, Saibah, Wasilah, Hami.
Scripture titles: Quran, Torah, Gospel, Psalms. Places and
named registers, fountains and stars: Israel, Egypt, Medina,
Mecca, Babylon, Sinai, Tuwa, Sheba, Badr, Hunayn, Yathrib,
Arafat, Marwa, Bekka, Kaabah, Judi, Arras, Russ, Median,
Sirius, Tariq, Saqar, Sijjeen, Elliyyeen, Elliyyoon, Tasneem,
Zanjabeel, Salsabeel. Peoples, communities and language proper
names: Jews, Jew, Jewish, Christians, Christian, Muslims,
Muslim, Islam, Judaism, Sabeans, Sabians, Zoroastrians,
Romans, Arabs, Arab, Arabic, Bedouins, Thamood, Aad, Egyptian.
Disjointed letters: Alif, Lam, Meem, Ha, Ra, Ya, Sin, Ta, Ayn,
Saad, Qaf, Shin (the spellings Ain, Nun, Kaf stand on the list
but do not occur). Of the 1,052 kept tokens, 6 carry the
Cyrillic genitive suffix as the disclosed device of §5 below.

**Seated — device map (8 types, 75 tokens).** Beneficent ×17,
Benevolent ×2, Compassionate ×11 → милӧсьта, the attested mercy
adjective (glossary §E: merciful / gracious), the same mercy
stem the BUILD-SPEC fixes for the Basmalah; Hearer ×16 →
кывзысь, the disclosed Listener device (so 2:127 now reads
кывзысь beside тӧдысь, as the checker required the family to
be consistent); Forgiver ×16 → прӧститысь and Forgivers ×1 →
прӧститысьяс, regular agent -ысь formations on прӧститны
"forgive" (the disclosed derivation class of ыстысь, эскысь,
тӧдысь); Omnipotent ×7 → став вына, the glossary §I Almighty
device; Maker ×5 → вӧчысь, regular agent on вӧчны (cf. the
disclosed Лёк вӧчысьяс device). The remaining two Beneficent
tokens stand at the special seats below.

**GAP-marked (332 types, 815 tokens).** Everything else,
Hereafter ×101 first, then Capable, Blaze, Clement, Mount,
Knowledgeable, Ark, Bliss, Trumpet, Sublime, Cognizant,
Guardian, Monotheist, Criterion, Repentance, Eden, Inferno,
Hellfire, Reality, Sustainer, and the long tail — each now a
visible marker, counted in the revised census (§6). The five
retained types that had unverified dictionary entries
(Reckoning, Build, Submit, Weak, Painful) were GAP-marked, not
seated: their entries stand in work/unverified-dict.json,
dropped at verification, so no verified seat exists for them.

**Special seats.** 1:3 now reads the BUILD-SPEC fixed form
**Милӧсьт, Милӧсьт.** (was "Beneficent, милӧсьта."). The
in-verse Basmalah at 27:30 is completed on the same seating as
1:1 ("Милӧсьт, Милӧсьт" inside the quotation). 55:1, whose whole
verse was the retained word "Compassionate.", now reads
"Милӧсьта." 2:163's two retained mercy names now both ride
милӧсьта.

**The screens are fixed, not just the text.** verify.py no
longer builds its name whitelist from every capitalised Master
word (the construction that returned a vacuous "0"); it carries
the explicit allowlist above, tests retained Latin and
mixed-script on whitespace tokens rather than a Cyrillic-only
stream, and asserts 1:3 against the spec form. Run on the
remediated store it returns: retained-Latin candidates off the
allowlist **0 types, 0 tokens**; allowlisted 128 types / 1,046
tokens (plus the 6 device tokens of §5, counted there).
work/build_engine.py is fixed at the source so a rebuild cannot
regress: its NAMES set is the same explicit allowlist (no longer
derived from Master capitalisation); the branch that retained
every capitalised non-initial token in English is removed —
unseated words GAP-mark, capitalised or not; and its
verb-inflection fallback now strips a suffix only when the word
actually ends with it (see §4 for the defect that guard closes).
The build dictionaries were unified to match §3, and
dict_verbs.py gains reflect — мӧвпавны (§4).

## 2. Standing GAP families (checker §8.2) — HELD

Sabbath ×7 tokens (2:65, 4:47, 4:154, 7:163 ×3, 16:124),
Hajj ×7 (2:189, 2:196, 2:197 ×3), Umrah ×3 (2:196), and
pilgrimage ×3 are all GAP-marked, consistent with the
attestation audit's standing GAP families and with sibling
practice. The hyphen-split compounds are closed with them:
4:47 now reads ⟦GAP: sabbath⟧ - жуглӧ and 9:90 ⟦GAP: desert⟧ -
Arabs (Arabs kept as a people name on the allowlist).

## 3. Core-term splits (checker §8.1) — UNIFIED

Each pair was unified onto one form book-wide. Ground, per the
desk ruling for this remediation: where BUILD-SPEC or the
glossary fixes a form, that form wins; otherwise the majority
native form wins. In all five pairs the glossary-fixed form is
also the majority or the native form, so no pair needed the
tiebreak to be argued further.

- **angel** — ангел wins (glossary §A/§D seat, the flagged
  attested loan). идӧгяс ×75 and Идӧгяс ×2 → ангеляс / Ангеляс
  (plural by the book's regular -яс device). Post-check: идӧг
  0 tokens; ангел family 88 (11 singular + 77 plural).
- **messenger** — ыстысь wins (glossary §A disclosed device on
  ыстыны "send"). гӧнецяс ×121 and Гӧнецяс ×5 → ыстысьяс /
  Ыстысьяс. Post-check: гӧнец 0; ыстысь family 361
  (235 + 126). 2:87's two competing seats in one verse are
  gone.
- **believe** — эск- wins (glossary §A/§F seat эскыны). The
  верит- family occurred only as the believer noun:
  веритысь ×16 → эскысь, веритысьяс ×153 and Веритысьяс ×6 →
  эскысьяс / Эскысьяс (175 tokens). Post-check: верит- 0.
- **sin** — мыж wins (glossary §A/§D seat). грекяс ×51 (sins)
  → мыжяс; грека ×6 (sinner) → мыжа and грекаяс ×33 → мыжаяс,
  the attested мыж-family adjective (glossary §E: guilty)
  nominalised by the plain device. Post-check: грек 0;
  мыж family 446 (356 + 90).
- **prayer** — кевмӧм wins (glossary §A seat on кевмыны).
  буркывяс ×32 → кевмӧмяс. Post-check: буркыв 0; кевмӧм 87
  (55 + 32).

Total split tokens reseated: 500. The unified seats are
recorded in glossary §J, which supersedes the conflicting
§§G–H seats; the dictionary files were updated to match.
**Reservation recorded for the re-checker:** the checker's
lesser splits — sea море ×31 / саридз ×4, mountain керӧс ×5 /
гӧра ×36, temple храм ×1 / мечеть ×20 — were outside the
required unification list for this pass and were not unified;
both forms in each pair are attested, and the Master's own
wording varies for the temple seats.

## 4. Minor items (checker §§4–5, 8.3) — DONE

- **Dropped-dictionary count.** The true figure is **26**:
  work/unverified-dict.json holds 26 entries. The attestation
  audit's "25" is corrected to 26 in place with a dated
  addendum at the audit's foot; the disclosure already carried
  26 and now states the correction.
- **"Scriputure"** ×1 (5:65, the Master's own misspelling
  carried unaltered) → гижӧд, the flagged generic scripture
  seat. **"Salomon"** ×1 (2:102) → Solomon, the Master's name
  form, on the allowlist.
- **пышйӧ ("flee") at reflect seats.** The mechanism is proven,
  not guessed: the engine's verb fallback stripped the prefix
  re- from "reflect" to "flect", then applied its ("ed" → "e")
  rule without checking that the word ends in -ed, landing on
  "flee" — so пышйыны was seated wherever the Master says
  "reflect". The checker named 3:191, 30:21, 51:49; this crew
  checked every пышй- token against its Master verse and found
  the same defect at **24 seats**: 2:266, 3:191, 7:57, 10:3,
  10:24, 11:24, 13:3, 14:25, 16:44, 16:69, 23:85, 25:50,
  25:62, 30:8, 30:21, 32:4, 34:9, 34:46, 37:155, 39:42, 40:58,
  45:23, 51:49, 59:21. Each is reseated on the attested think
  verb мӧвпавны (glossary §F: think; present мӧвпавӧ, negated
  stem мӧвпав after оз), recorded in glossary §J and in
  dict_verbs.py. The 12 genuine flee tokens (3:111, 27:80,
  28:31, 33:13, 33:16, 40:33, 51:50, 59:12, 62:8, 72:12,
  74:51, 80:34) keep пышй-; post-check пышй- tokens: 12, all
  at flee seats.
- **Mixed-script claim.** The 6 name + -лӧн tokens (Adamлӧн
  5:27; Pharaohлӧн 7:127, 40:28, 40:37; Abrahamлӧн 11:74;
  Josephлӧн 12:58) are the glossary's disclosed genitive
  device. This remediation keeps the forms and corrects the
  claim, the first of the two roads the checker offered: the
  revised disclosure and the fixed verify.py report exactly
  these 6 tokens as the disclosed device, and no others.
- **Front matter.** The manuscript's claim about unrendered
  words now matches the remediated reality (assemble.py): apart
  from the carried names, every unseated Master word carries
  the GAP marker and no English word is retained silently; the
  build-tier paragraph now states the check, the FAIL, the
  remediation, and the awaited re-check, in place of the
  build's "has not had an independent check".

## 5. Rebuilt counts (verify.py as fixed, run 2026-11-28 after the rebuild)

- Store seats 6,236 / master seats 6,236 / seat-set equal:
  True. Per-surah mismatches: NONE. Empty seats: NONE.
  "redacted": NONE.
- 1:1 == Basmalah: True. 1:3 == spec form "Милӧсьт, Милӧсьт.":
  True. Basmalah in quran-kpv.txt: 113 (112 unnumbered + 1:1);
  in the manuscript: 113.
- Built quran-kpv.json == verses-store.json at every seat:
  True. All thirteen work/batch-*.json files identical to the
  store at every seat: True.
- GAP census after remediation: **5,042 seats / 13,714
  markers / 1,194 verses without a marker / 4,299 distinct
  terms** (before: 4,870 / 12,899 / 1,366 / 4,183; the marker
  increase is exactly the 815 GAP-marked tokens of §1).
  Manuscript marker count 13,715 — the text's 13,714 plus the
  front matter's explanatory example, as before.
- Retained Latin: allowlist only — 128 types, 1,052 tokens;
  off-allowlist candidates 0. Mixed-script: the 6 disclosed
  device tokens, no others.
- Purple sweep reconciled: 6 untraced Cyrillic candidates —
  the build's 4 disclosed paradigm forms (локтӧ ×441, кулӧ
  ×56, юяс ×52, лӧн ×6) plus the remediation's Forgiver forms
  (прӧститысь ×16, прӧститысьяс ×1), adjudicated in the revised
  disclosure as disclosed regular derivations, candidates only.
- Distinct Cyrillic tokens 1,000; tokens containing ӧ: 476;
  tokens containing і: 13.

Status: STOPPED as instructed — not landed, not shelved, not
committed, not pushed. Ready for a fresh independent re-check.
