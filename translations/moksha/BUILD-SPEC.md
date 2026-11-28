# Moksha lane — build specification (fixed 2026-11-27)

Governing documents: CANDIDATE-BRIEF-MOKSHA.md (conditions settled
by Robert Tilford's ruling of 2026-11-27, 21:16 CST — the nightly
board ruling adopting the desk's recommendations; Moksha fourth in
the OPEN-IN-ORDER QUEUE after Lule Sámi, Erzya, Udmurt),
LICENCES-RECORDED-2026-11-27.md, ATTESTATION-AUDIT-2026-11-27.md.
Master of record: the Locked English Master
(~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md,
MD5 ecc5b8e2848e5044186b7ad82bed9f4e); verse texts in
~/workspace/ayah-moksha/master-verses.json (114 surahs, 6,236
verses, verified against the Master; identical copy to the
Erzya/Udmurt lanes).

## Orthography and base (FIXED, per brief §8 condition 1)
- Norm: the modern literary standard, Cyrillic script with
  spelling rules identical to those of Russian (the same
  33-letter alphabet, no additional letters), based on the
  Central group (M-I) in its ä-retaining form, particularly the
  dialect of Krasnoslobodsk, in the norm of the Saransk
  dictionaries and the 2016 New Testament. The developed but
  never implemented Latin orthography is NOT a build target.
  Scholarly transliteration is NOT community orthography.
- Moksha ONLY, ISO mdf. Erzya (myv) forms are NEVER seated:
  Паз (God), чи (sun/day), кедь (hand), теште (star), баславамс,
  кинига, казне are ERZYA forms and are barred. The Moksha seats
  are Шкай, ши, кядь, тяште, бславамс, книга. NEVER use
  Erzya–Moksha MT output as a drafting base (brief §3 bar).
- Do NOT run Moksha text through a Russian spellchecker.
- The /e, ɛ, ə/ spelling seat (brief §2): the standard spelling
  does not differentiate these in all positions; follow the
  attested inventory's spellings exactly, never normalise.
- Capitalisation: sentence-initial and proper names only, plus
  Шкай "God" and its pronouns where the Master capitalises.

## Base and honesty
- Base named on the book's face: modern literary Moksha built on
  the attested lexical base in the attestation audit — GiellaLT
  giella-mdf (LGPL v3) and the Wiktionary/kaikki harvest
  (CC BY-SA) as attestation sources; the 2016 New Testament and
  the modern dictionaries as controls by FACT AND CITATION ONLY
  (in copyright; their wording is never reproduced). The narrower
  Bible control than Erzya's (New Testament only; no complete
  Bible, no named modern Old Testament portion found) is
  disclosed on the book's face.
- No "first translation" claim anywhere (brief §5: NOT FOUND in
  the searched sources — a bounded result, not proof; brief §8
  condition 7's catalogue pass not run, so no novelty wording).

## Names policy
Personal names and scripture titles are carried in the Master's
forms (Moses, Jesus, Mary, Abraham, Noah, the Torah, the Gospel,
the Psalms…), unaltered. The disjointed letters at surah heads
are carried as in the Master ("Alif, Lam, Meem.").

## The Basmalah
Surah 1:1 IS the Basmalah and is translated as verse 1:1. Every
other surah except 9 carries it as an unnumbered opening line.
Seated form (fixed for the whole book):
**Шкаень лемса, Милостивай, Милостивай.**
("In the name of God, the Merciful, the Merciful." Both mercy
names rest on the one attested mercy stem милостивай — Giella,
fin "laupias, armollinen" — and that single-stem seating is
disclosed on the book's face and in the glossary. Verse 1:3 is
the same two names without the frame: "Милостивай,
Милостивай.")

## GAP policy
A seat that cannot be carried on attested forms takes the
visible marker ⟦GAP: <term>⟧ inline, the rest of the verse
rendered as far as attested forms allow. Standing GAP terms:
jinn, pilgrimage (term seats), Sabbath (term seats), usury.
NEVER invent a form; NEVER borrow silently from Erzya, Russian,
or Finnish. Russian-shaped loans already in the attested
inventory (рай, пост, ангел, книга, мир, грех, сатана, ад,
враг, корабль, война, верблюд, золота, союз, казня, свидетель)
are seated only as flagged in the audit.

## Grammar reference (the norm every batch follows)
Moksha has no articles and no grammatical gender. Keep sentences
plain and close to the Master, clause by clause.
- Pronouns: мон (I), тон (you sg), сон (he/she), минь (we),
  тинь (you pl), синь (they). Possessive/genitive: монь, тонь,
  сонь, минь, тинь, синь (context forms). Reflexive/own: эсь.
- "God" seats: Шкай (nom), Шкаень (gen, "of God"), Шкайнди
  (dat, "to God"), Шкайста (elat, "from God"), Шкайса (iness,
  "in God"), Шкайс (ill, "into God"). Definite nominative: Шкайсь.
- Noun cases (indefinite): nom -Ø; gen -нь (шкай→шкаень,
  ломань→ломанень, ши→шинь); dat -нди (ломаненди); abl -да/-дэ
  (модада); iness -са/-сэ (кудса, менельса); elat -ста/-стэ
  (кудста); illat -с (кудс); prol -га/-ка/-ва (кива "along the
  road"); compar -шка; abess -фтома ("without"). Definite sg
  nom -сь (ломанесь, шкайсь); definite pl nom -тне (ломантне);
  indefinite pl nom -т (ломанть, шить). Use definite forms where
  the Master has "the", indefinite where it has "a" —
  consistently, not mechanically in every seat.
- Adjectives do not agree; they precede the noun unchanged:
  оцю (big — check inventory; if unsure use покш ONLY if in the
  mdf inventory, otherwise log), вишкине (small), пара (good),
  берянь (bad/evil), од (new), сире (old), виде (true/right),
  кеме (firm/strong), валда (bright), шобда (dark), милостивай
  (merciful). Where an adjective is unsure, check
  sources/mdf-lemmas.json first; if absent, GAP-device it and log.
- Verb infinitive -мс: тиемс (do/make), азомс (say), мярьгомс
  (say), корхтамс (speak), содамс (know), кемамс (believe),
  озондомс (pray), эрямс (live), куломс (die), кельгомс (love),
  пелемс (fear), няемс (see), кулемс (hear), марямс (hear/feel),
  максомс (give), сявомс (take), самс (come), молемс (go), тумс
  (depart/go), лисемс (go out), сувамс (enter), стямс (rise/
  stand), улемс is NOT seated (Erzya-shaped seat) — "be" seats
  ride ули (in inventory) / present-tense zero copula, logged;
  кирдемс is NOT seated unless in inventory — hold/endure seats
  ride ваномс/учемс phrasing, logged; панжемс (open), кучемс
  (send), няфтемс (show), судендамс (judge), прощандамс family
  (forgive, flagged), пандомс is NOT seated — pay seats ride
  максомс, logged; лувомс (read/recite), сёрматкшнемс (write,
  flagged frequentative on сёрма), учемс (wait), арьсемс
  (think), ваномс (look/guard), идемс (save), вельмомс
  (rise again/revive), кадомс (leave), вешемс (seek), мумс
  (find), шачемс (be born), касомс (grow), озамс (sit),
  ушедомс (begin), ётамс (pass — only if in inventory, else
  молемс phrasing, logged), кандомс is NOT seated — bring/carry
  seats ride максомс/молемс phrasing, logged; вятемс (lead/
  guide — Giella, fin "johtaa"). "Follow" = молемс мельга
  device is NOT seated (мельга unverified); follow seats ride
  молемс + genitive + ингеле-васта phrasing ONLY where sure,
  otherwise descriptive молемс фтала? NO — standing device:
  "follow" = вятемс in passive sense is wrong; use
  **молемс сонь мельганза** ONLY if мельга is in the inventory,
  else restructure as "walk in his path" — **молемс сонь кинц
  эзга** (ки + эзга "through", both attested), logged.
- Present tense (objective, no object): 1sg -ан/-ян (тиан,
  содан, кеман, азян? — азомс 1sg is азян on the -омс stem
  pattern; where unsure use a verb whose paradigm you do know),
  2sg -ат/-ят, 3sg -ы/-и (тии, соды, кеми, эри, азы), 1pl
  -тама/-тяма (титама, содатама), 2pl -тада/-тяда, 3pl
  -ыхть/-ихть (тиихть, содыихть is wrong shape — 3pl is
  -ыхть/-ихть on the stem: содыихть NOT used; standing 3pl:
  тиихть, содаыхть is NOT used. RULE: where a 3pl paradigm is
  unsure, use the 3sg form with the plural subject named —
  a disclosed plain-style device, logged once per batch.)
- Past tense: 1sg -ыне/-ине (тиине, содыне), 2sg -ыть/-ить,
  3sg -сь (тиись, содась, азьсь is NOT used — "he said" seats:
  азсь on азомс, regular, is the standing narrative form),
  1pl -ынек/-инек, 2pl -ыде/-иде, 3pl -ысть/-исть.
- Future: present forms carry future sense (standing Moksha
  usage), or кармамс + infinitive devices avoided; use present.
- Negation: present/future — аф + present form (аф содан "I do
  not know", аф тиихть "they do not do"); аф is the attested
  Moksha negation (NOT Erzya а alone). Past — аше family is NOT
  in the inventory: RULE: if a past-negation paradigm is unsure,
  render the clause in the present-negation frame with the time
  carried by a time word (ингеле-васта devices avoided; use
  пинге phrasing) — log it in batch notes. Imperative negation:
  иля + imperative is Erzya-shaped and NOT seated; command
  negation seats ride аф + 2pl present as command, logged.
- Imperative: 2sg stem (тий, азь, сака is NOT used); plural/
  polite -к forms (тийк, азьк) and 2pl present as command where
  unsure — log it.
- "Say:" introducing speech — Азьк: / Азсь: with the Master's
  quotation marks (“ ”) kept.
- Conjunctions/postpositions seated (all in the mdf inventory):
  и (and), а (and/but, by position), но (but, loan in
  inventory), эли is NOT seated — "or" = али (only if in
  inventory, else но-phrasing, logged); кода (as/when/how),
  мзярда (when), мезенкса devices avoided — "therefore" =
  тянь инкса phrasing ONLY if инкса in inventory, else кода
  phrasing, logged; коса (where — only if in inventory),
  эзда (from), лангса (on, inessive), лангс (onto), алда
  (under), вельде (over/by means of), ваксса (beside), ёткса
  (through/among), туркс (across), пеле (towards — only if in
  inventory). Every function word MUST be checked against
  sources/mdf-lemmas.json before seating; an unchecked function
  word does not seat.
- Numbers as in the Master (words where the Master has words):
  фкя (1), кафта (2), колма (3), ниле (4), вете (5), кота (6),
  сисем (7), кафкса (8), вейхкса (9), кемонь (10), комсь (20),
  сяда (100), тёжянь (1000). All are inventory lemmas or regular
  compounds of them.
- Relative clauses: use кона (who/which — only if in inventory,
  else кда/кие phrasing, logged) + verb, or the -ця participle
  is Erzya-shaped and NOT seated; Moksha agent nouns ride the
  -й/-ф participle forms in the inventory (тии "one who does",
  няи "one who sees", соды "one who knows") — regular agent
  formations on attested stems, disclosed as devices.

## Style
- Plain, close rendering of the Master, sentence by sentence.
  The Master's verse is the unit; do not merge or split verses.
- FIDELITY PROTOCOL (the Veps lesson, binding): every clause of
  the Master must be carried — every content word (nouns, verbs,
  adjectives, numbers, names, negations, conditions) carried by
  Moksha, by a glossary device, or by a logged GAP. Pronouns may
  never stand in place of dropped content words. For verses over
  25 Master words, re-read and confirm clause-complete before
  shipping; log the long-verse check in the batch notes.
- God's pronoun: Сон, capitalised as in the Master.
- Numbers written as in the Master.
- The two Master seats carrying a literal "<redacted>"
  placeholder (39:7, 48:8) are rendered for their surrounding
  sense; the string "redacted" never appears in the Moksha text.

## Output format
Batch files: ~/workspace/ayah-moksha/work/batch-<X>.json,
{"S:V": "Moksha text"} — plain UTF-8 JSON, EVERY seat in the
batch's master-<X>.json, no seat omitted, no seat added.
Each batch ships with work/notes-<X>.md logging: every GAP seat,
every flagged-construction seat beyond routine repetition, every
uncertainty, and the fidelity self-check record (the batch's
verses over 25 Master words, each confirmed clause-complete
after re-reading).
