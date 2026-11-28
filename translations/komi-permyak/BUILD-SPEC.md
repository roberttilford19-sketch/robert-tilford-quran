# Komi-Permyak lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-KOMI-PERMYAK.md (gate
conditions settled by Robert Tilford's ruling of 2026-11-27,
21:16 CST — the open-in-order queue: Lule Sámi, Erzya, Udmurt,
Moksha, Meadow Mari, Komi-Zyrian, **Komi-Permyak**, Chuvash,
Southern Sámi, Võro, North Frisian),
LICENCES-RECORDED-2026-11-28.md, ATTESTATION-AUDIT-2026-11-28.md.
Master of record: the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
MD5 ecc5b8e2848e5044186b7ad82bed9f4e); verse texts in
~/workspace/ayah-komi-permyak/master-verses.json (114 surahs,
6,236 verses, verified against the Master; identical copy to the
sibling lanes).

## Orthography and base (FIXED, per brief §8 condition 1)
- Norm: the modern Komi-Permyak literary standard, Cyrillic
  script (the Russian alphabet plus І/і and Ӧ/ӧ, 35 letters),
  based on the Kudymkar dialect of the central (Inva) group, in
  the norm of the GiellaLT `koi` resources. Komi-Permyak ONLY,
  ISO koi. The book's language name rides as перем коми кыв in
  the front matter, with коми-пермяцкӧй кыв recorded beside it
  (brief §§2/7 naming caution).
- KOMI-ZYRIAN BAR: Komi-Zyrian (kpv) and Komi-Yazva forms are
  NEVER seated. The two standards share an alphabet, so the
  fence is attestation-based: a form seats only if it traces to
  a `koi` inventory held at the desk (GiellaLT giella-koi stem
  and dictionary files, its Ponomareva-proofread paradigm test
  files, English Wiktionary Komi-Permyak entries). A form whose
  only attestation is a kpv page or the kpv lane's files does
  not seat — the Wiktionary pages for менам/тэнад, for example,
  carry Komi-Zyrian sections only and were NOT used; the
  pronoun paradigms seat from the giella-koi gt-norm YAML
  tests, proofread by Larisa Ponomareva (2019-10-22). Udmurt,
  Erzya, Moksha, Mari, Tatar, and Russian forms are never seated
  except where the form itself stands in the harvested koi
  inventories (flagged loans in the glossary).
- Do NOT run Komi-Permyak text through a Russian spellchecker;
  І must never be normalised to И.
- Capitalisation: sentence-initial and proper names only, plus
  Ен "God" where the Master capitalises.

## Base and honesty
- Base named on the book's face: modern literary Komi-Permyak
  built on the attested lexical base in the attestation audit —
  GiellaLT giella-koi (LGPL v3) and the Wiktionary Komi-Permyak
  lexicon (CC BY-SA) as attestation sources; the Batalova &
  Krivoshchekova-Gantman (1985) dictionary tradition and the
  New Testament control (Бур Юӧр 2019, Institute for Bible
  Translation, Finland) as controls by FACT AND CITATION ONLY
  (in copyright; their wording is never reproduced). The Bible
  control is New Testament ONLY — no complete Bible in
  Komi-Permyak was found (brief §4) — and the control's own
  orthographic variation from the current norm (Kielipankki's
  warning, brief §4) is disclosed on the book's face.
- No "first translation" claim anywhere (brief §5: NOT FOUND,
  with the NabiMuhammad.com "Komi коми" aggregator listing
  unresolved for both Komi lanes; brief §8 condition 7's
  catalogue pass not run, so no novelty wording).
- BUILD TIER, stated plainly: this is a first-pass,
  engine-rendered draft. Every verse seat is filled, seat by
  seat, from the verified dictionary; every Master content word
  with no verified seat carries the visible GAP marker rather
  than an invented or borrowed form. The GAP census is
  disclosed on the book's face. The draft stops before landing
  and before any independent check.

## Names policy
Personal names and scripture titles are carried in the Master's
forms (Moses, Jesus, Mary, Abraham, Noah, the Torah, the Gospel,
the Psalms, the Quran…), unaltered. Carried names ride an
EXPLICIT allowlist in the engine and in verify.py — the list is
never derived from the Master's capitalisation (the Komi-Zyrian
checker's §4 lesson, applied from the start). Any other
unseated word, capitalised or not, takes the GAP marker. The
disjointed letters at surah heads are carried as in the Master
("Alif, Lam, Meem.").

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line
(113 occurrences in the built text: 112 unnumbered + 1:1).
Seated form (fixed for the whole book):
**Енлӧн нимӧн, Милӧсьта, Милӧсьта.**
("In the name of God, the Merciful, the Merciful." Both mercy
names rest on the one attested mercy seat милӧсьта — a lemma of
the giella-koi inventory, of the мил- family attested by
милуйтны "миловать, любить" (to pardon, to love); the
single-stem seating and the seat's thin gloss trail are
disclosed on the book's face and in the glossary. Verse 1:3 is
the same two names without the frame: "Милӧсьта, Милӧсьта." —
seated exactly, by engine rule. The in-verse Basmalah at 27:30
is rendered on the same seats word by word.)

## GAP policy
A seat that cannot be carried on attested forms takes the
visible marker ⟦GAP: <english term>⟧ inline, the rest of the
verse rendered as far as attested forms allow. NEVER invent a
form; NEVER borrow silently from Komi-Zyrian, Komi-Yazva,
Udmurt, Erzya, Moksha, Mari, Tatar, or Russian. Russian-shaped
loans already in the attested koi inventory (ангел, пророк, рай,
ад, храм, трон, жертва, идол, джинн, мечеть, религия…) are
seated only as flagged in the audit. Standing GAP families,
GAP-marked at every seat, never retained in English: Sabbath,
pilgrimage (the technical term), Hajj, Umrah, usury (the
technical term), alms (the technical term), scripture as a
technical term (the generic seat rides гижӧт, flagged).
(Clarified at remediation, 2026-11-28, per checker §3: the
alms entry likewise carries a generic-seat exception — the
generic alms/charity seat rides the attested корӧм, whose
giella-koi dictionary gloss includes "милостыня, подаяние";
only the technical zakat term is GAP-marked as a family.)

## Grammar reference (the norm every batch follows)
Komi-Permyak is agglutinative, SOV-leaning, with no articles and
no grammatical gender. This first-pass draft follows a disclosed
plain style, kept close to the Master, clause by clause:
- Pronouns (paradigms proofread by Larisa Ponomareva in the
  giella-koi gt-norm tests): ме (I; acc менӧ, gen менам, dat
  меным), тэ (you sg; acc тэнӧ, gen тэнат), сія (he/she/it; acc
  сійӧ, gen сылӧн, dat сылӧ), ми (we; acc миянӧс, gen миян),
  ті (you pl, seated тэ by the plain device), нія (they; gen
  нылӧн). Self forms: ачым, ачыт, ачыс, асьным, асьныт, асьныс.
- "God" seats: Ен (nom), Енлӧн (gen, "of God"), Енлӧ (dat),
  Енӧс (acc) by the regular paradigm. "Lord" rides Ен by a
  disclosed device — no separate господь seat is attested in
  the koi inventories held; сар "king" is a different seat.
- Noun cases (regular paradigm, disclosed; plural and case
  shapes verified against the gt-norm paradigms): nom -Ø;
  gen -лӧн; acc -ӧс; dat -лӧ; iness -ын; elat -ись; illat -ӧ;
  plural: stem-final consonant doubled + -эз (горт → горттэз,
  пон → поннэз, кар → каррез), vowel-final stem + -эз
  (му → муэз, кага → кагаэз), -й stem + -ез (туй → туйез). The
  plural seats wherever the Master has a plural, consistently.
  The elative -ись and illative -ӧ also ride as separate tokens
  for the Master's "from"/"to" seats — a disclosed plain-style
  device, named here and on the book's face.
- Adjectives do not agree; they precede the noun unchanged:
  бур (good), лёк (bad/evil), ыджыт (big/great), ичӧт (small),
  виль (new), важ (old), веськыт (straight/just), вежа (holy),
  югыт (bright/light), пемыт (dark), сьӧд (black), чочком
  (white), гӧрд (red), сьӧкыт (heavy).
- Verbs seat in the infinitive's 3rd-person present form
  (stem + ӧ; irregulars овны→олӧ, кувны→кулӧ, воны→воӧ,
  лоны→лоӧ, локны→локтӧ, кывны→кылӧ, аддзыны→аддзӧ) — a
  disclosed plain-style device: person and tense are carried by
  the subject and by time words, exactly as the sibling lanes
  disclose their plain-style devices. The copula seats ride
  лоны. "Will/shall" seats ride the same present form.
- Negation: **оз** + verb stem (the attested Komi-Permyak
  negative auxiliary, paradigm ог/он/оз in the gt-norm tests),
  logged as a device. Existential "there is not / no" seats
  ride **абу**.
- "Say:" introducing speech — Шуӧ: with the Master's quotation
  marks (“ ”) kept.
- Numbers as in the Master (words where the Master has words):
  ӧтік (1), кык (2), куим (3), нёль (4), вит (5), квать (6),
  сизим (7), кыкьямыс (8), ӧкмыс (9), дас (10), дасӧтік (11),
  даскык (12), кыкдас (20), куимдас (30), нёльдас (40),
  витдас (50), кватьдас (60), сизимдас (70), кыкьямысдас (80),
  ӧкмысдас (90), дасдас (100), сюрс (1000). All are inventory
  lemmas, most gloss-verified in the giella-koi dictionary XML.
- Every seated lemma MUST trace to the harvested koi
  inventories (sources/giella-koi-lemmas.json,
  sources/koi-gloss-dict.json, sources/yaml-forms.json,
  sources/wikt-koi-parsed.json) or to a disclosed regular
  derivation of one (plural, case, present-tense, agent
  -ісь/-лісь, abstract -лун/-ӧм formations); an untraced word
  does not seat — it takes the GAP marker and is logged.

## Style
- Plain, close rendering of the Master, sentence by sentence.
  The Master's verse is the unit; do not merge or split verses.
- FIDELITY PROTOCOL (the Veps lesson, binding): every clause of
  the Master must be carried — every content word (nouns, verbs,
  adjectives, numbers, names, negations, conditions) carried by
  Komi-Permyak, by a glossary device, or by a logged GAP.
  Pronouns may never stand in place of dropped content words.
- The two Master seats carrying a literal "<redacted>"
  placeholder (39:7, 48:8) are rendered for their surrounding
  sense; the string "redacted" never appears in the Komi text.
- Core terms ride ONE seat each (the Komi-Zyrian checker's
  §8.1 lesson): angel ангел only; messenger ыстісь (device)
  only; believe эскыны / believer эскісь (device) only; sin
  мыж only; prayer келмӧм / pray кеймыны only.

## Output format
One store: ~/workspace/ayah-komi-permyak/verses-store.json,
{"S:V": "Komi-Permyak text"} — plain UTF-8 JSON, EVERY seat of
master-verses.json, no seat omitted, no seat added. The
rendering engine is work/build_engine.py, driven by the
verified dictionary work/dict_koi.json (built by
work/build_dict.py from work/dict_core_koi.py and
work/dict_rus.py) and the manual core in work/dict_core_koi.py;
dropped unverified entries are logged at
work/unverified-dict.json, unmatched English keys at
work/unmatched.json. Outputs: quran-koi.txt, quran-koi.json,
ayah-companion-manuscript-KOI.md — built, verified, and STOPPED
before landing: no shelving, no commit, no push.
