# Komi-Zyrian lane — flags-and-gaps disclosure (2026-11-28)

This disclosure rides with the draft at
~/workspace/ayah-komi-zyrian/ayah-companion-manuscript-KPV.md
(DRAFT — NOT PUBLISHED). It is the book's honest status, carried
inside the lane record. The build stopped before landing; the
lane's first independent check
(CHECKER-REPORT-INDEPENDENT-2026-11-28.md) returned FAIL, its
verified findings were remediated the same day
(REMEDIATION-RECORD-2026-11-28.md), and landing waits on a fresh
independent checker PASS under the Pipeline Landing
Authorization. The GAP tier itself was ruled
PASS-WITH-GAP-TIER-RESERVATION by that check (§9): no
GAP-reduction pass is required or was made; the remediation
closed the separate, invisible retained-English tier the check
found beside the GAP tier.

## Build tier — stated first, in the same breath as the figures
This is a **first-pass, engine-rendered draft**, not a
hand-finished translation of the sibling lanes' kind. It was
rendered seat by seat from the Locked English Master by
work/build_engine.py on a mechanically verified dictionary of
**1,314 seated English→Komi entries** (26 candidate entries were
dropped at verification and are logged at
work/unverified-dict.json — the true figure is 26; the
attestation audit's original "25" was corrected by dated
addendum on 2026-11-28). Every Master content word with no
verified Komi-Zyrian seat carries the visible GAP marker rather
than an invented or borrowed form. The GAP census below is
therefore large — far larger than the hand-built sibling lanes
(Meadow Mari 298 GAP seats, Moksha 58, Erzya 56; Udmurt 1,732) —
and it is disclosed here and on the book's face, not hidden.
What the draft guarantees is narrower and exact: every one of
the 6,236 seats is present, in order, with its Master clause
carried by a verified seat, a disclosed device, a carried name
on the recorded allowlist, or a logged GAP.

## Mechanical figures (verify.py as fixed 2026-11-28, run on the remediated store)
- Verse count: **6,236 of 6,236**. Seat-set equality with the
  Master: **exact** (store keys == master keys == 6,236 grid).
- Per-surah grid: **no mismatches** against the standard grid
  (114 surahs; grid printed in verify.py).
- Verses rendered without a GAP marker: **1,194**. GAP seats:
  **5,042**. GAP markers in all: **13,714**. Distinct GAP terms:
  **4,299** (the long tail is low-frequency Master vocabulary;
  the largest single terms are hereafter ×101, painful ×67,
  wronged ×39, destroyed ×34, disbelief ×29, presence ×29,
  beyond ×28, bounty ×28, sincere ×26, provision ×26,
  ancients ×26, polytheists ×25, settled ×25). Before
  remediation the census was 1,366 / 4,870 / 12,899 / 4,183;
  the increase is exactly the 815 formerly retained English
  tokens now GAP-marked, in 172 seats that had carried no
  marker before.
- GAP census by batch (seats / markers): A 423/1,533 ·
  B 417/1,603 · C 470/1,566 · D 486/1,350 · E 367/980 ·
  F 366/1,010 · G 397/934 · H 367/987 · I 445/1,106 ·
  J 352/809 · K 421/1,059 · L 400/585 · M 131/192. Every GAP
  seat and every GAP term is listed in work/notes-A.md …
  work/notes-M.md (build record; the remediation's own seat
  list is work/remediation-log-2026-11-28.json).
- Basmalah: 1:1 equals the fixed seated form **Енлӧн нимӧн,
  Милӧсьт, Милӧсьт**; 1:3 equals the BUILD-SPEC form
  **Милӧсьт, Милӧсьт.**; the in-verse Basmalah at 27:30 is
  completed on the same seating as 1:1; the built text
  (quran-kpv.txt) carries the Basmalah **113 times** — 112
  unnumbered opening lines (every surah except 1 and 9) plus
  verse 1:1 itself.
- Script purity (fixed screens, whitespace tokens, GAP
  interiors excluded): distinct Cyrillic tokens **1,000**;
  tokens containing ӧ: **476**; tokens containing і: **13**;
  retained Latin stands only on the recorded allowlist of
  carried names — **128 types, 1,052 tokens** (1,046 pure Latin
  tokens plus the 6 device tokens below); retained-Latin
  candidates off the allowlist: **0 types, 0 tokens**;
  mixed-script tokens: exactly **6**, all the disclosed
  genitive-on-names device (Adamлӧн 5:27; Pharaohлӧн 7:127,
  40:28, 40:37; Abrahamлӧн 11:74; Josephлӧн 12:58), and no
  others; the string "redacted": **NONE**; empty seats:
  **NONE**. (The build's original disclosure claimed
  mixed-script NONE and retained-Latin 0 on screens that could
  not see Latin; those claims were false and are replaced by
  the figures above, measured by the fixed verify.py.)
- Purple sweep (verify.py) — candidates only: untraced
  Cyrillic token candidates **6** — локтӧ ×441 (the disclosed
  irregular present of локны "come"), кулӧ ×56 (the disclosed
  irregular present of кувны "die"), юяс ×52 (regular plural of
  ю "river", stem too short for the screen's length rule),
  лӧн ×6 (the genitive suffix as split by the screen from
  carried names, e.g. Adamлӧн), прӧститысь ×16 and
  прӧститысьяс ×1 (the remediation's Forgiver seat: regular
  agent -ысь formation on прӧститны "forgive", disclosed in
  glossary §J). Each is a disclosed paradigm form, not an
  unattested seat; they are carried here as candidates for the
  independent re-checker, not as a verdict.

## Flagged seats and devices (glossary §§A, I, J)
Енлӧн нимӧн, Милӧсьт, Милӧсьт (the Basmalah; both mercy names on
the one attested stem милӧсьт) · Оз эскысьяс (disbelievers) ·
Лёк вӧчысьяс (wrongdoers) · Вежа Лов (Holy Spirit) · восьтӧм
(revelation, on восьтыны "open") · дорйӧм (refuge, on дорйыны
"protect") · ыстысь (messenger, on ыстыны "send") · дзик ӧти
(the Absolute) · став вына (the Almighty; also the remediation
seat for Omnipotent) · кывзысь / тӧдысь (the Listener / the
Knower, regular agent formations; кывзысь is also the
remediation seat for Hearer) · милӧсьта (the attested mercy
adjective; remediation seat for the Beneficent / Benevolent /
Compassionate epithets outside the Basmalah seats) ·
прӧститысь (Forgiver, regular agent on прӧститны) · вӧчысь
(Maker, regular agent on вӧчны) · радейтны (love —
lemma-attested in GiellaLT, gloss-thin in the stem file,
flagged) · джинн (jinn — GiellaLT lemma without a gloss in the
stem file, flagged) · гижӧд (scripture, generic seat on the
attested "writing" lemma, flagged) · пемыдлун (darkness,
abstract formation on пемыд, flagged) · attested loans seated
as flagged: ангел, пророк, рай, ад, храм, трон, жертва, идол,
религия, факт, группа, поколение, победа, приказ, средство,
коллектив, лицензия, джинн.
Plain-style devices disclosed in BUILD-SPEC: verbs in the
3rd-person present form throughout; negation оз + verb stem;
copula лоны; regular plural -яс/-ъяс; genitive -лӧн including
on carried names (Adamлӧн).

## Remediation seats (2026-11-28; full record in REMEDIATION-RECORD-2026-11-28.md)
- Core terms unified to one form book-wide (glossary §J):
  angel ангел/ангеляс · messenger ыстысь/ыстысьяс · believe
  эскыны, believer эскысь/эскысьяс, faith эскӧм · sin
  мыж/мыжяс, sinner мыжа/мыжаяс · prayer кевмӧм/кевмӧмяс. The
  displaced forms (идӧг, гӧнец, верит-, грек, буркыв) occur
  zero times in the remediated text. Lesser splits noted by
  the checker but outside its required list — sea море/саридз,
  mountain керӧс/гӧра, temple храм/мечеть — stand as recorded
  reservations for the re-checker; they were not unified in
  this pass.
- Standing GAP families held at every seat: Sabbath ×7,
  Hajj ×7, Umrah ×3, pilgrimage ×3 — all GAP-marked.
- The Master's "reflect" seats (24) ride мӧвпавны "think,
  ponder"; пышйыны "flee" remains only at flee seats.
- Carried names ride the explicit allowlist recorded in the
  remediation record and in verify.py (128 types seated).

## The Komi-Permyak fence
Attestation was against kpv inventories only (GiellaLT
giella-kpv; English Wiktionary Komi-Zyrian via kaikki). No
Komi-Permyak (koi) form was seated from any koi source. The two
standards share an alphabet, so the fence is attestation-based
(brief §2); the verify.py screen traces tokens to the kpv
inventories specifically.

## Bible control — honest scope
Verified control: the complete Komi-Zyrian New Testament
(2008; Mark 1995, John 1997; Institute for Bible Translation,
Finland), cited by fact only. The Коми Библия 2023 complete
Bible indicated by directory listings was **not** verified
book-by-book (brief §8 condition 3 remains open); no
complete-Bible claim is made anywhere in the book.

## Novelty
No first-translation claim is made anywhere in the book or this
disclosure (brief §5: not found in the searched sources, with
the NabiMuhammad.com "Komi коми" aggregator listing unresolved;
the Russian-language and catalogue pass of brief §8 condition 7
was not run).
