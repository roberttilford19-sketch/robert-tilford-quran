# Komi-Zyrian lane — attestation audit (2026-11-28)

Method: every seat in the build dictionaries was checked
mechanically against the inventories harvested at the desk on
2026-11-28 — GiellaLT giella-kpv stem files (193,665 clean
Cyrillic lemmas, sources/giella-lemmas-full.json, each carrying
the Finnish gloss where the stem file gives one) [G] and English
Wiktionary via kaikki.org (1,006 headwords,
sources/kaikki-kpv-parsed.json; 29,484 declined forms,
sources/kaikki-kpv-forms.json) [W]. A seat is seated only where
the lemma stands in [G] and/or [W], or is a disclosed regular
derivation of such a lemma (plural -яс/-ъяс, case endings,
present-tense -ӧ, agent -ысь/-лысь, abstract -лун/-ӧм).
Dictionary use is fact and citation only, never the maker's
wording (house law). Entries that failed verification at build
time were dropped automatically and are logged at
work/unverified-dict.json (26 entries; corrected 2026-11-28 —
see the addendum at the foot of this audit).

Build dictionaries: work/dict_core.py (desk-curated core),
work/dict_nouns.py (crew-curated, 272 mapped / 15 not found),
work/dict_verbs.py (crew-curated, 270 mapped / 68 not found).
Final seated dictionary after verification: recorded in the
build run output and the flags-and-gaps disclosure.

## Core religious seats — attested
- God — **ен** [G: fin "Jumala"; W]. Genitive енлӧн, dative
  енлы by the regular paradigm (BUILD-SPEC).
- Lord — **мезӧс** [G: fin "Herra"].
- Name — **ним** [G: fin "nimi"].
- Mercy / Merciful — **милӧсьт** [G]. The Basmalah's two mercy
  names both rest on милӧсьт — a single-stem seating, disclosed
  on the book's face.
- Prayer — **кевмӧм** on кевмыны [G: fin "rukoilla"]; pray —
  **кевмыны** [G].
- Heaven / sky — **енэж** [G: fin "taivas"]; paradise — **рай**
  [G, flagged loan].
- Hell — **ад** [G, flagged loan].
- Angel — **ангел** [G, flagged loan].
- Spirit / soul — **лов** [G,W]; Holy Spirit — **Вежа Лов**
  device on вежа [G: fin "pyhä"] + лов, flagged.
- Prophet — **пророк** [G, flagged loan]. Messenger —
  **ыстысь** device on ыстыны [G: fin "lähettää"], flagged.
- Book — **небӧг** [G,W: fin "kirja"]; word — **кыв** [G: fin
  "kieli"]; sign — **пас** [G].
- Light — **югыд** [G]; darkness — **пемыдлун** device on пемыд
  [G] + abstract -лун, flagged (the lemma's gloss in the stem
  file is a homonym sense; the dark sense is the Wiktionary
  sense).
- Earth/land — **му** [G: fin "pelto"; W: "earth, land"];
  world — **мир** [G].
- Sun/day — **шонді** [G: fin "aurinko"] / **лун** [G,W: fin
  "päivä"]; moon/month — **тӧлысь** [G: fin "kuu"]; star —
  **кодзув** [G: fin "tähti"]; sea — **море** [W]; river —
  **ю** [G,W]; mountain — **керӧс** [G,W]; water — **ва** [G:
  fin "vesi"]; fire — **би** [G: fin "tuli"]; wind — **тӧв**
  [W: "wind"]; cloud — **кымӧр** [G: fin "pilvi"]; rain —
  **зэр** [G]; snow — **лым** [G].

## People and kin — attested
person/human — **морт** [G: fin "ihminen"]; woman — **ань**
[G,W]; mother — **мам** [G: fin "äiti"]; father — **ай** [G];
son — **пи** [G,W]; daughter — **ныв** [G: fin "tyttö"]; child —
**кага** [G]; people — **войтыр** [G]; enemy — **враг** [G:
cf. вӧрӧг in the crew chunk]; friend — **ёрт** [G,W: fin
"toveri"]; heart — **сьӧлӧм** [G,W: fin "sydän"]; blood —
**вир** [G]; hand — **ки** [G,W]; foot — **кок** [G]; head —
**юр** [G]; eye — **син** [G,W]; ear — **пель** [G]; voice —
**гӧлӧс** [G].

## Faith, judgement, the last things — attested
faith — **эскӧм** on эскыны [G: fin "uskoa (jhonk)"];
believe — **эскыны** [G]; believer — **эскысь** regular agent,
device flagged; disbelievers — **Оз эскысьяс** negated device,
flagged; truth/true — **збыль** [G]; sin — **мыж** [G];
sinner — **грека** [G: fin "syntinen"]; forgive —
**прӧститны** [G]; forgiveness — **прӧща** [G: fin
"anteeksianto"]; judgement — **мыждӧм** [G]; punish —
**мыждыны** [G]; judge — **суддя** [G]; covenant/promise —
**кӧсйысьӧм** [G: fin "lupaus"]; power — **вын** [G];
fear (v) — **повны** [G: fin "pelätä jtak"]; love (v) —
**радейтны** [G lemma; gloss in the stem file is "pitää
huolta" — lemma-attested, gloss-thin, flagged]; devil/Satan —
**шайтан** [G]; fasting — **вежӧм**, flagged; alms — the
technical-term seats are held as GAPs (милостыня failed
verification in its Russian spelling and was not seated);
sacrifice — **жертва** [G, flagged loan]; reward — **дон**
[G]; witness — **свидетель** [G: fin "todistaja"]; revelation —
no direct lemma: device **восьтӧм** on восьтыны [G: fin
"avaaminen"], flagged; refuge — device **дорйӧм** on дорйыны
[G], flagged; guide — **веськӧдлысь** device on веськӧдлыны,
flagged; straight path — **веськыд туй** (веськыд [G] + туй
[G]); temple — **храм** [G lemma, flagged loan]; throne —
**трон** [G, flagged loan]; jinn — **джинн** [G lemma, no gloss
carried in the stem file, flagged].

## Common verbs — attested [G and/or W]
say **шуны** [G: fin "sanoa, että"] · tell **висьтавны** [G:
fin "kertoa; julistaa"] · know **тӧдны** [G: fin "tietää"] ·
see **аддзыны** [G,W] · hear **кывны** [G: fin "kuulla"] ·
give **сетны** [G: fin "antaa"] · take **босьтны** [G,W: fin
"ottaa"] · come **локны** [G] · go **мунны** [G: fin "mennä"] ·
do/make/create seats **вӧчны** [G: fin "tehdä"] · live **овны**
[G: fin "elää"] · die **кувны** [G: fin "kuolla"] · send
**ыстыны** [G: fin "lähettää"] · open **восьтыны** [G,W] ·
read/recite **лыддьыны** [G: fin "lukea"] · write **гижны**
[G: fin "kirjoittaa"] · seek **корсьны** [G: fin "etsiä"] ·
be born **чужны** [G: fin "syntyä"] · grow **быдмыны** [G: fin
"kasvaa"] · eat **сёйны** [G: fin "syödä"] · drink **юны**
[G: fin "juoda"] · sleep **узьны** [G: fin "nukkua"] · weep
**бӧрдны** [G: fin "itkeä"] · laugh **серавны** [G: fin
"nauraa"] · ask **юавны** [G: fin "kysyä"] · forget
**вунӧдны** [G: fin "unohtaa"] · sell **вузавны** [G: fin
"myydä"] · listen **кывзыны** [G: fin "kuunnella"] · plus the
270-seat crew-curated verb chunk at work/dict_verbs.py, each
seat gloss-matched there.

## Numbers — attested [G/W]
ӧти (1) · кык (2) · куим (3) · нёль (4) · вит (5) · квайт (6)
· сизим (7) · кӧкъямыс (8) · ӧкмыс (9) · дас (10) · кызь (20)
· сё (100) · сюрс (1000).

## Standing GAP families (no attested Komi-Zyrian form found)
pilgrimage (technical term) · Sabbath · usury (technical term)
· scripture as a technical term (the generic seat rides
гижӧд, flagged) · marriage / murder / adultery / fornication
(technical terms, crew chunk not-found list) · wisdom as a
noun (crew chunk: мудерлун rejected, glossed "cunning") ·
account / reckoning (technical terms) · and the long tail of
low-frequency Master vocabulary, logged term by term in
work/notes-A.md … work/notes-M.md. Render the rest of the
verse fully around the marker ⟦GAP: …⟧.

## The Komi-Permyak fence check
Every seat was drawn from the kpv inventories only. No
Komi-Permyak (koi), Komi-Yazva, Udmurt, Erzya, Moksha, or Mari
inventory was consulted as a seating source. Because the two
Komi standards share an alphabet, this fence is attestation-
based, not letter-based (brief §2), and the verification screen
in verify.py traces tokens to the kpv inventories specifically.

## Addendum (2026-11-28, remediation)

The dropped-entries figure in the first paragraph of this audit
originally read 25. The file of record, work/unverified-dict.json,
holds 26 entries, which is the figure the flags-and-gaps
disclosure used and the independent checker verified
(CHECKER-REPORT-INDEPENDENT-2026-11-28.md §5). The figure above
is corrected to 26; the true figure is 26 everywhere in the
lane's record from this date.
