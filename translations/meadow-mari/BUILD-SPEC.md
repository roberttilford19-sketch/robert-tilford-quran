# Meadow Mari lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-MEADOW-MARI.md (conditions
settled by Robert Tilford's ruling of 2026-11-27, 21:16 CST — the
nightly board ruling adopting the desk's recommendations; Meadow
Mari fifth in the OPEN-IN-ORDER QUEUE after Lule Sámi, Erzya,
Udmurt, Moksha), LICENCES-RECORDED-2026-11-28.md,
ATTESTATION-AUDIT-2026-11-28.md.
Master of record: the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
MD5 ecc5b8e2848e5044186b7ad82bed9f4e); verse texts in
~/workspace/ayah-meadow-mari/master-verses.json (114 surahs,
6,236 verses, verified against the Master; identical copy to the
Erzya/Udmurt/Moksha lanes).

## Orthography and base (FIXED, per brief §8 condition 1)
- Norm: the modern Meadow Mari literary standard, Cyrillic
  script (the Russian alphabet plus Ҥ/ҥ, Ӧ/ӧ, Ӱ/ӱ), based on the
  Yoshkar-Ola dialect, in the norm of the 2011 orthographic
  dictionary, the Vienna Mari–English Dictionary, and the New
  Testament control (У Сугынь). Meadow Mari ONLY, ISO mhr.
- HILL MARI BAR: Hill Mari (mrj) and Northwestern Mari forms are
  NEVER seated. Any token containing ӓ or ӹ is a Hill /
  Northwestern intrusion and fails canonical verification.
  Erzya (myv), Udmurt (udm), Moksha (mdf), Tatar, and Russian
  forms are never seated except where the form itself stands in
  the harvested mhr inventories (flagged loans in the glossary).
- Do NOT run Meadow Mari text through a Russian spellchecker.
- Capitalisation: sentence-initial and proper names only, plus
  Юмо "God" and its pronouns where the Master capitalises.

## Base and honesty
- Base named on the book's face: modern literary Meadow Mari
  built on the attested lexical base in the attestation audit —
  GiellaLT giella-mhr (LGPL v3) and the Wiktionary/kaikki harvest
  (CC BY-SA) as attestation sources; the Vienna Mari–English
  Dictionary (Creative Commons, attribution; exact variant not
  named in the pages retrieved), the Corpus of Literary Mari,
  the ten-volume Yoshkar-Ola dictionary, and the New Testament
  (У Сугынь, Institute for Bible Translation, Finland, 1986 /
  2007) as controls by FACT AND CITATION ONLY (in copyright;
  their wording is never reproduced). The narrower Bible control
  (complete New Testament only; no complete Bible verified, no
  Old Testament portion verified) is disclosed on the book's face.
- No "first translation" claim anywhere (brief §5: NOT FOUND in
  the searched sources — a bounded result, not proof; brief §8
  condition 7's Russian-language and catalogue pass not run, so
  no novelty wording).

## Names policy
Personal names and scripture titles are carried in the Master's
forms (Moses, Jesus, Mary, Abraham, Noah, the Torah, the Gospel,
the Psalms…), unaltered. The disjointed letters at surah heads
are carried as in the Master ("Alif, Lam, Meem.").

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line.
Seated form (fixed for the whole book):
**Юмын лӱмеш, Серлагыш, Серлагыш.**
("In the name of God, the Merciful, the Merciful." Both mercy
names rest on the one attested mercy stem серлагыш — Giella,
"mercy, charity, kindness" — and that single-stem seating is
disclosed on the book's face and in the glossary. Verse 1:3 is
the same two names without the frame: "Серлагыш, Серлагыш.")

## GAP policy
A seat that cannot be carried on attested forms takes the
visible marker ⟦GAP: <term>⟧ inline, the rest of the verse
rendered as far as attested forms allow. Standing GAP terms:
jinn, hell (term seats), covenant (term seats), pilgrimage
(term seats), Sabbath, usury, scripture (generic term seats).
NEVER invent a form; NEVER borrow silently from Hill Mari,
Erzya, Udmurt, Moksha, Tatar, or Russian. Russian-shaped loans
already in the attested mhr inventory (рай, книга, вера, храм,
трон, поп, корабль, милостынь, пророк, грех is NOT in the
inventory — sin seats ride сулык only) are seated only as
flagged in the audit.

## Grammar reference (the norm every batch follows)
Meadow Mari is agglutinative, SOV-leaning, with no articles and
no grammatical gender. Keep sentences plain and close to the
Master, clause by clause. Every lemma MUST be checked against
sources/mhr-lemmas.json (or the glossary) before seating; an
unchecked word does not seat — GAP-device it and log it.
- Pronouns: мый (I), тый (you sg), тудо (he/she/it/that),
  ме (we), те (you pl), нуно (they). Possessive suffixes and
  genitive forms: мыйын, тыйын, тудын, мемнан, тендан, нунын.
- "God" seats: Юмо (nom), Юмын (gen, "of God"), Юмылан (dat,
  "to God"), Юмышто (iness, "in God"), Юмо гыч (elat phrasing,
  "from God"), Юмышке (ill, "into God").
- Noun cases (regular paradigm, disclosed): nom -Ø; gen -н
  (юмо→юмын, еҥ→еҥын, кече→кечын); acc -м; dat -лан
  (еҥлан); iness -ште/-што/-штӧ (пӧртыштӧ, каваште); illat
  -шке/-шко/-шкӧ and short -ш (пӧртышкӧ); elat -гыч (пӧрт
  гыч); lat -шке/-ш; compar -ла; comit -ге; caritive -де.
  Plural -влак (regular Mari plural suffix, paradigm seat).
  Use plural -влак where the Master has a plural, consistently.
- Adjectives do not agree; they precede the noun unchanged:
  кугу (big/great), изи (small), у (new), акрет (old, only if
  in inventory, else тошто — check inventory first), сай
  (good), уда (bad — check inventory; else йоҥылыш phrasing,
  logged), чын (true), тӧр (straight/just), шнуй (holy),
  волгыдо (bright), шем (black/dark — check inventory),
  шучко (terrible), писе (swift), вий-ан forms ride вий.
- Verb infinitive -аш/-еш/-аш: ышташ (do), каласаш (say),
  кутыраш (speak), палаш (know), ончаш (see/look), колаш
  (hear; also die — context decides, log ambiguous seats),
  пуаш (give), налаш (take), толаш (come, flagged citation
  form), каяш (go), лекташ (go out), колташ (send), ончыкташ
  (show), лудаш (read), вучаш (wait), аралаш (save/protect),
  кычалаш (seek), муаш (find), шочаш (be born), кушкаш
  (grow), нӧлташ (rise), шинчаш (sit), тӱҥалаш (begin),
  пушташ (kill), кочкаш (eat), йӱаш (drink), малаш (sleep),
  шорташ (weep), воштылаш (laugh), йодаш (ask), вашешташ
  (answer), ӱжаш (call), мондаш (forget), ужалаш (sell),
  шелаш (break), пӧртылаш (return), ӧкынаш (repent), кумалаш
  (pray/bow), чоклаш (pray/sacrifice), илаш (live), лӱдаш
  (fear), инанаш (believe), ӱшанаш (believe/hope), касараш
  (forgive/atone, flagged), судитлаш (judge, flagged),
  жертвоватлаш (sacrifice, flagged), почаш (open), петыраш
  (close), кучаш (hold), тунемаш (learn), туныкташ (teach).
- Present tense (plain style): 1sg -ам/-ем (ыштем is the
  attested-shaped 1sg of ышташ — where a paradigm form is
  unsure, use the form you know or restructure, and log it),
  2sg -ат/-ет, 3sg -а/-е (каласа, ышта, ила, пале), 1pl
  -ына/-ена, 2pl -ыда/-еда, 3pl -ат/-ет with plural subject.
  RULE: where a 3pl or other paradigm is unsure, use the 3sg
  form with the plural subject named — a disclosed plain-style
  device, logged once per batch.
- Past tense: 1sg -ым/-ем, 2sg -ыч/-еч, 3sg -е/-о (каласe
  shape: -ш past marker in -ым/-ыш forms; standing narrative
  3sg past: verb stem + ш, e.g. каласыш, ыштыш — where unsure
  use present with a time word, logged), 1pl -на, 2pl -да,
  3pl -ыт.
- Future: тӱҥалаш-auxiliary and present forms carry future
  sense (standing Mari usage; тӱҥалаш is itself glossed "used
  to mark future tense" in Wiktionary).
- Negation: present — огыл + connegative / ам/ем/ом negative
  verb family (уке "is not", огыл "is not" are attested);
  standing plain device: **огыл** + present stem form, and
  **уке** for existential "there is not", logged. Past
  negation: ыш (attested preterite negative) + stem, logged.
  Imperative negation rides огыл + imperative, logged.
- Imperative: 2sg stem form; 2pl stem + -за/-са where sure,
  else 2pl present as command, logged.
- "Say:" introducing speech — Каласе: / Каласыш: with the
  Master's quotation marks (“ ”) kept.
- Conjunctions/postpositions seated (check inventory):
  да (and — inventory), але (or — check), но (but, loan in
  inventory), кунам (when), кузе (as/how), молан (why/for),
  дене (with), деч (from, postposition), гыч (from/out of),
  лан (to/for — dative suffix seats), шеҥгеч (behind/after —
  check inventory), ончыч (before — check), йымалне (under —
  check), ӱмбалне (on — from ӱмбал "top"), покшелне (among —
  from покшел "middle"), воктене (beside — check). Every
  function word MUST be checked against sources/mhr-lemmas.json
  before seating.
- Numbers as in the Master (words where the Master has words):
  ик (1), кок (2), кум (3), ныл (4), вич (5), куд (6), шым (7),
  кандаш (8), индеш (9), лу (10), коло (20), шӱдӧ (100),
  тӱжем (1000). All are inventory lemmas.
- Relative clauses: кудо (which/who — W-attested relative) +
  verb, or the -ше participle forms in the inventory (ыштыше
  "one who does", ужшо "witness/one who sees", инаныше
  "believer") — regular agent formations on attested stems,
  disclosed as devices.

## Style
- Plain, close rendering of the Master, sentence by sentence.
  The Master's verse is the unit; do not merge or split verses.
- FIDELITY PROTOCOL (the Veps lesson, binding): every clause of
  the Master must be carried — every content word (nouns, verbs,
  adjectives, numbers, names, negations, conditions) carried by
  Meadow Mari, by a glossary device, or by a logged GAP.
  Pronouns may never stand in place of dropped content words.
  For verses over 25 Master words, re-read and confirm
  clause-complete before shipping; log the long-verse check in
  the batch notes.
- God's pronoun: Тудо, capitalised as in the Master.
- Numbers written as in the Master.
- The two Master seats carrying a literal "<redacted>"
  placeholder (39:7, 48:8) are rendered for their surrounding
  sense; the string "redacted" never appears in the Mari text.

## Output format
Batch files: ~/workspace/ayah-meadow-mari/work/batch-<X>.json,
{"S:V": "Meadow Mari text"} — plain UTF-8 JSON, EVERY seat in
the batch's master-<X>.json, no seat omitted, no seat added.
Each batch ships with work/notes-<X>.md logging: every GAP seat,
every flagged-construction seat beyond routine repetition, every
uncertainty, and the fidelity self-check record (the batch's
verses over 25 Master words, each confirmed clause-complete
after re-reading).
