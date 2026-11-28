# Komi-Permyak lane — attestation audit (2026-11-28)

Method: every seat in the build dictionaries was checked
mechanically against the inventories harvested at the desk on
2026-11-28 — GiellaLT giella-koi stem files (77,661 lemmas,
sources/giella-koi-lemmas.json), the giella-koi dictionary XML
(14,725 lemmas carrying Russian — and a few Finnish/English —
glosses, sources/koi-gloss-dict.json), the giella-koi gt-norm
paradigm test files (15,533 forms, sources/yaml-forms.json;
proofread by Larisa Ponomareva, 2019-10-22), and English
Wiktionary Komi-Permyak entries via the MediaWiki API (334
headwords with English glosses, sources/wikt-koi-parsed.json)
[G = GiellaLT, Y = paradigm tests, W = Wiktionary]. A seat is
seated only where the lemma stands in one of those koi
inventories, or is a disclosed regular derivation of such a
lemma (plural, case, present-tense -ӧ, agent -ісь/-лісь,
abstract -лун/-ӧм). Dictionary use is fact and citation only,
never the maker's wording (house law). Entries that failed
verification at build time were dropped automatically and are
logged at work/unverified-dict.json (**0 entries** in the final
build). kaikki.org has no Komi-Permyak per-language download
(its index lists Komi-Zyrian only; every koi URL returned the
162-byte 404 page the previous crew's truncated file held), so
the Wiktionary harvest ran through the API directly.

Build dictionaries: work/dict_core_koi.py (desk-curated core:
function, pronoun, number seats and the manual overrides),
work/dict_koi.json (712 seats matched by work/build_dict.py —
Wiktionary English glosses first, then Russian gloss-head
matching against the giella-koi dictionary XML via
work/dict_rus.py and work/dict_rus2.py; 283 curated Russian
keys found no koi seat and are logged at work/unmatched.json).
Final seated dictionary: **1,317 entries** (engine count).

## The Komi-Zyrian fence, stated and enforced
Every seat was drawn from the koi inventories only. No
Komi-Zyrian (kpv) inventory, dictionary file, or Wiktionary page
was consulted as a seating source: where a Wiktionary page
carries only a Komi-Zyrian section (the pronoun forms менам,
тэнад are such pages), it was NOT used — the pronoun paradigms
seat from the giella-koi gt-norm tests [Y], proofread by the
native-speaker Permyak scholar Larisa Ponomareva. Two Zyrian
forms that entered the first engine draft by copying the model
lane's tables were caught by the attestation screen and
removed before the final build: войтыр ("people"; the Permyak
seat is отир, UDHR-attested) and the Zyrian plural shapes in
the irregular-plural table (replaced by the Permyak paradigm
shapes аннез, пиннез, кагаэз [Y]). Because the two Komi
standards share an alphabet, this fence is attestation-based,
not letter-based (brief §2), and verify.py traces tokens to the
koi inventories specifically. The brief's sharper caution —
that the giella-koi description was initially derived from the
Zyrian lexicon — is answered by the seating rule above: seats
trace to the dictionary XML's own Komi-Permyak entries, the
proofread paradigm files, or Wiktionary Komi-Permyak entries,
i.e. to the native-speaker correction layer, and the seats
whose trail is thinnest are flagged below and in the glossary.

## Core religious seats — attested
- God — **ен** [G: rus "бог"]. Genitive енлӧн, dative енлӧ by
  the regular paradigm (BUILD-SPEC).
- Lord — **ен** by disclosed device: no separate господь seat
  is attested in the koi inventories held (the сар seat is
  "king" [G: rus "царь"]). Disclosed on the book's face.
- Name — **ним** [G: rus "имя"].
- Mercy / Merciful — **милӧсьта** [G lemma of the inventory;
  the seat's own gloss is not carried in the XML subset —
  flagged thin. The мил- family is gloss-attested by милуйтны
  "миловать, любить" (to pardon, to love)]. The Basmalah's two
  mercy names both rest on милӧсьта — a single-stem seating,
  disclosed on the book's face.
- Prayer — **келмӧм** [G: rus "молитва", marked Usol. dialect —
  flagged]; pray — **кеймыны** [G: rus "молиться"].
- Heaven / sky — **енӧж** [G: rus "небо"]; paradise — **рай**
  [G lemma, flagged loan]; hell — **ад** [G lemma, flagged
  loan].
- Angel — **ангел** [G lemma, flagged loan]. Prophet —
  **пророк** [G lemma, flagged loan]. Messenger — **ыстісь**,
  regular agent derivation of ыстыны [G: rus "послать"],
  flagged device.
- Spirit / soul — **лов** [W: "soul, spirit"]; Holy Spirit —
  **Вежа Лов** device on вежа [G: rus "святой"] + лов, flagged.
- Book — **небӧг** [G: rus "книга"]; word — **кыв** [G,W];
  sign — **пас** [G lemma, flagged thin].
- Light — **югыт** [G: rus "свет, светлый"]; darkness —
  **пемыт** [G: rus "тёмный"].
- Earth/land/world — **му** [G: rus "земля; мир"]; sun —
  **шонді** [G: rus "солнце"]; moon/month — **тӧлісь** [G: rus
  "луна; месяц"]; star — **кодзув** [G lemma, flagged thin];
  sea — **саридз** [G lemma, flagged thin]; river — **ю** [G:
  rus "река"]; mountain — **гӧра** [G: rus "гора"] (керӧс is
  the second attested seat and is NOT used — one seat per
  term); water — **ва** [G: rus "вода"]; fire — **би** [G,W:
  rus "огонь"]; wind — **тӧв** [G]; cloud — **кымӧр** [G: rus
  "облако"]; rain — **зэр** [G: rus "дождь"]; snow — **лым**
  [G: rus "снег"].

## People and kin — attested
person/human — **морт** [W: "man, human, person"; G]; people —
**отир** [G lemma; UDHR Article 1 running text]; woman —
**ань** [G,W]; mother — **мам** [G: rus "мать"]; father —
**ай** [G]; son — **пи** [G lemma]; daughter — **ныв** [W:
"daughter, girl"]; child — **кага** [G: rus "ребёнок"];
wife — **гӧтыр** [G: rus "жена"]; friend — **ёрт** [G];
enemy — **враг** [G lemma, flagged loan]; servant — **слуга**
[G lemma, flagged loan]; king — **сар** [G: rus "царь"];
heart — **сьӧлӧм** [W: "heart"]; blood — **вир** [G: rus
"кровь"]; hand — **ки** [G: rus "рука"]; foot — **кок** [G:
rus "нога"]; head — **юр** [G: rus "голова"]; eye — **син**
[G: rus "глаз"]; ear — **пель** [G: rus "ухо"]; voice —
**гӧлӧс** [G lemma].

## Faith, judgement, the last things — attested
faith — **эскӧм**, regular -ӧм noun of эскыны [G: rus
"верить"], flagged device; believe — **эскыны** [G];
believer — **эскісь** regular agent, flagged device;
disbelievers — **Оз эскісьяс** negated device, flagged;
truth — **быль** [G: rus "правда"]; righteous — **веськыт**
[G: rus "прямой" — the straight/just seat; no праведный gloss
is attested in the koi sources held, and the device is
flagged]; sin — **мыж** [G lemma; gloss not carried in the XML
subset — flagged thin]; forgive — **прӧститны** [G lemma];
forgiveness — **прӧститӧм** regular -ӧм device, flagged;
punishment — **пикӧтӧм** [device on пикӧтны, G: rus
"наказывать"]; covenant/promise — **кӧсйӧм** [G: rus
"обещание"]; power — **вын** [G: rus "сила; мощь"]; fear (v)
— **повны** [G,W: rus "бояться"]; love (v) — **радейтны**
[G: rus "любить"]; devil/Satan — **шайтан** [G lemma, flagged
loan]; fasting — **видз** [G: rus "пост" attested, homonym
"meadow" — flagged], fast (v) — **видзавны** [G: rus
"соблюдать пост"]; sacrifice — **жертва** [G lemma, flagged
loan]; reward — **дон** [W: "price" — flagged thin];
witness — **адззылісь** [G: rus "свидетель"]; revelation —
device **восьтӧм** on восьтыны [G lemma "to open"], flagged;
refuge — **дорйӧм** [G: rus "защита" family, on дорйыны
"защищать"]; guide (v) — **нуӧтны** [G: rus "водить, вести
(кого-либо)"]; knower — **тӧдісь** [G: rus "знающий"];
hearer — **кывзісь** regular agent of кывзыны [G: rus
"слушать"], flagged device; warner — **казьмӧтісь** device on
казьмӧтны [G: rus "напоминать, напомнить" — "remind" seated
for "warn", flagged]; hereafter — **мӧд олӧм** device ("the
other life": мӧд + олӧм [G: rus "жизнь"]), flagged;
temple — **храм** [G lemma, flagged loan]; mosque —
**мечеть** [G lemma, flagged loan]; throne — **трон** [G
lemma, flagged loan]; jinn — **джинн** [G lemma, no gloss
carried — flagged]; scripture as a technical term is a
standing GAP family (the generic seat rides гижӧт [G: rus
"письмо" — "writing, letter"], flagged).

## Common verbs — attested [G and/or W]
say **шуны** [G: rus "говорить, сказать"] · tell
**висьтавны** [G] · know **тӧдны** [G: rus "знать"] · see
**адззыны** [G: rus "видеть"] · hear **кывны** [G: rus
"слышать"] · give **сетны** [G: rus "давать"] · take
**босьтны** [G: rus "брать"] · come **локны** [G,Y] · go
**мунны** [G,Y] · do/make **вӧчны** [G: rus "делать"] ·
create **аркмӧтны** [G: rus "создать"] · produce **керны**
[G: rus "делать"] · live **овны** [G,Y: rus "жить"] · die
**кувны** [G: rus "умирать"] · send **ыстыны** [G: rus
"послать"] · open **восьтыны** [G lemma] · read/recite
**лыддьыны** [G: rus "читать"] · write **гижны** [G] · seek
**корсьны** [G lemma] · eat **сёйны** [G: rus "есть"] ·
drink **юны** [G: rus "пить"] · sleep **узьны** [G: rus
"спать"] · weep **бӧрдны** [G: rus "плакать"] · ask
**юавны** [G: rus "спрашивать"] · forget **вунӧтны** [G:
rus "забыть"] · listen **кывзыны** [G: rus "слушать"] ·
remember **касьтывны** [G: rus "вспоминать"] · repent
**каитчыны** [G: rus "каяться"] · save **мезмӧтны** [G: rus
"освобождать, освободить" — "free, release" seated for
"save", flagged] · follow **мунны бӧрын** [device: "go
after"] · plus the matched dictionary at work/dict_koi.json,
each seat gloss-matched there by construction.

## Numbers — attested [G/W/Y]
ӧтік (1) · кык (2) · куим (3) · нёль (4) · вит (5) · квать (6)
· сизим (7) · кыкьямыс (8) · ӧкмыс (9) · дас (10) · дасӧтік
(11) · даскык (12) · кыкдас (20) · куимдас (30) · нёльдас (40)
· витдас (50) · кватьдас (60) · сизимдас (70) · кыкьямысдас
(80) · ӧкмысдас (90) · дасдас (100) · сюрс (1000). Ordinals:
первӧй, кыкӧт, куимӧт, нёльӧт, сизимӧт, дасӧт [G].

## Standing GAP families (no attested Komi-Permyak form found)
pilgrimage (technical term) · Sabbath · Hajj · Umrah · usury
(technical term) · alms (technical term) · wisdom as a noun ·
justice as a noun · doubt · permission · blessings (the noun)
· glory · patience (the noun) · and the long tail of
low-frequency Master vocabulary, logged term by term in the
flags-and-gaps disclosure. Render the rest of the verse fully
around the marker ⟦GAP: …⟧.

## Matched-dictionary caution (for the independent checker)
The 712 gloss-matched seats of work/dict_koi.json were matched
mechanically (first gloss segment, POS-filtered). Homonym traps
found and removed by hand during the build: панлавны (glossed
"предупреждать" in its "overtake" sense) was unseated from
"warn"; веськӧтлыны (glossed "выпрямлять" — "to straighten")
was unseated from "guide"; тор (glossed "кусок" — "piece") was
left unseated from "things", which therefore GAPs. The checker
should sample the matched dictionary for further homonym
seats; two known candidates are recorded in the disclosure
(peace riding му, pay riding мед).

---

## Addendum — 2026-11-28 (remediation pass; this addendum corrects the record above, which is not rewritten)

The independent checker report of 2026-11-28 (CHECKER-REPORT-INDEPENDENT-2026-11-28.md, verdict FAIL, §7) established that the sentence above — "Two Zyrian forms that entered the first engine draft … were caught by the attestation screen and removed before the final build: войтыр … and the Zyrian plural shapes in the irregular-plural table" — was incomplete as a claim about the text. войтыр was truly absent and the irregular-plural table was truly replaced, but the Zyrian plural shapes had NOT been removed from the text: the phrase table in work/dict_core_koi.py (PHRASES, lines 261–263) still seated эскісьяс "believers/disbelievers" (272 tokens, 250 seats) and вӧчісьяс in "wrongdoers" (67 tokens, 66 seats) — 339 tokens in 313 seats in all, carrying the Komi-Zyrian plural suffix -яс against this audit's own and BUILD-SPEC's Permyak plural rule (stem-final consonant doubled + -эз). The line in the Faith section above reading "disbelievers — Оз эскісьяс" is one instance of that residue in this audit's own text; it stands unrewritten here, and is corrected by this addendum. The original verify.py screen could not see the fault: its ending-stripping decomposition absorbed -яс letter by letter (see the build report's addendum of the same date).

Remediation, applied 2026-11-28 and recorded in full in REMEDIATION-RECORD-2026-11-28.md: the PHRASES table now seats the Permyak agent plurals эскісььэз and вӧчісььэз (stem-final сь doubled + -эз, the book's own shape in ыстісььэз and адззылісььэз); the build was re-run from the engine; -яс plural tokens in the rebuilt text are 0; and verify.py was tightened (single-letter endings removed; an explicit -яс rejection added), after which it returns 0 untraced candidates on the repaired text and returned exactly the two fault tokens as candidates on the unrepaired text.

Alms reconciliation (checker §3/§10.3), in the same addendum: the "Standing GAP families" list above names "alms (technical term)" with no exception noted, yet the generic alms seat rides корӧм at every generic seat (e.g. 2:110; мед корӧм at 5:12) — exactly as the generic scripture seat rides гижӧт under the exception that list does note. The list is reconciled as follows, and the glossary now states it in its core section: **alms as a technical term (zakat) is a standing GAP family; the generic alms/charity seat rides the attested корӧм** — the giella-koi dictionary gloss for корӧм includes "милостыня, подаяние" (alms, almsgiving). No seat changed for this item; the discrepancy was in the list, not the text.
