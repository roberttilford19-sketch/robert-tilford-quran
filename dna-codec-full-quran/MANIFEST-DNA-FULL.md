# MANIFEST — The Quran Encoded in DNA Letters (full text, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day. Framework from Robert Tilford's 2026-11-14
conversation with Google's LLM; the codec was demonstrated there on the
Bismillah and verified by machine at this desk before this build began.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete Arabic text of
the Quran, taken from the master of record below, written in the four DNA
letters A, C, G, T under the codec stated below. **Nothing has been
synthesized. No physical DNA exists.** Physical synthesis is a separate,
future, funded laboratory project and is not part of this deposit.

## The codec (exactly the demonstrated one)

Arabic text as UTF-8 bytes → binary bits → every two bits become one base:
**00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes four bases. The mapping is
lossless and reversible: decoding the base stream returns the byte stream
exactly, which the independent decoder's report in this deposit proves by
hash.

## Source of record

- Master: `~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md`
  (the Locked English Master, post-6:86 correction).
- MD5, machine-verified before extraction: `064ee170806bb31f5bac3e75d2aa4d94`
- The Arabic was extracted **by code, never retyped**.

## Extraction rule (disclosed exactly)

The encoded stream is the master's complete Arabic run sequence for Part I
(The Translation), taken by **structural position** — the house verifier's
amended method of 2026-11-14 — in master order. For each surah 1–114:

1. the surah-header Arabic name, from the `**<name>** · …` title line;
2. the basmalah frame line standing in the surah preamble, where the surah
   carries one (112 surahs carry a frame; Surah 1 has none because the
   basmalah is its verse 1, and Surah 9 has none);
3. for every verse block, the last non-empty, non-separator, non-marker line
   of the block — the verse's Arabic.

The runs are concatenated **with no separator characters**; the byte stream is
the UTF-8 encoding of that concatenation. Before encoding, the extracted
sequence was checked for exact equality against the lane `meta.json`
expectation (the same equality the house verifier requires of every lane) —
it matched, run for run.

- Runs: **6,462** = 114 surah names + 112 basmalah frames + **6,236 verses**
- Arabic byte stream: **1,355,915 bytes**
- Base stream: **5,423,660 bases** (4 per byte)
- SHA-256 of the Arabic byte stream: `fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`
- SHA-256 of the base stream: `d92efa7682d2047068d45804716978bc1667c98e38f6693c9f1f3b69eb658c10`

## Consistency check against the Bismillah specimen (reported as found)

The verified demonstration specimen encoded the Bismillah in **300 bases**
(75 bytes). The master's own 1:1 basmalah, encoded by the same codec, is
**292 bases** (73 bytes). **They are not identical, and no match was forced.**
The two strings are the same visible words. They differ in codepoint makeup: (1) in the divine name the specimen carries U+0670 ARABIC LETTER SUPERSCRIPT ALEF after the shadda, which the master does not carry at that place (net +1 codepoint, +2 bytes, +8 bases in the specimen); (2) at three places (the divine name and the two Rahman/Rahim words) the order of U+064E ARABIC FATHA and U+0651 ARABIC SHADDA around the letter differs between the two strings — same marks, different stored order, which changes the bytes and therefore the bases. The first 81 bases are identical; the sequences diverge from base 82. This lane encodes the MASTER of record exactly as it stands; the specimen stands as the codec proof. Neither string was altered to force a match.

The specimen stands as the proof of the codec; this deposit encodes the
master of record exactly as it stands.

## Per-surah index

| Surah | Title | Transliteration | Arabic name | Verses | Arabic bytes | Bases | Base range |
|---|---|---|---|---|---|---|---|
| 1 | The Opening | Al-Fatihah | ٱلْفَاتِحَة | 7 | 570 | 2280 | 1–2280 |
| 2 | The Heifer | Al-Baqarah | ٱلْبَقَرَة | 286 | 107111 | 428444 | 2281–430724 |
| 3 | The Family of Imran | Aal-Imran | آلِ عِمْرَان | 200 | 60781 | 243124 | 430725–673848 |
| 4 | The Women | An-Nisa | ٱلنِّسَاء | 176 | 66180 | 264720 | 673849–938568 |
| 5 | The Table | Al-Ma'idah | ٱلْمَائِدَة | 120 | 49579 | 198316 | 938569–1136884 |
| 6 | The Cattle | Al-An'am | ٱلْأَنْعَام | 165 | 52632 | 210528 | 1136885–1347412 |
| 7 | The Elevations | Al-A'raf | ٱلْأَعْرَاف | 206 | 58761 | 235044 | 1347413–1582456 |
| 8 | The Spoils of War | Al-Anfal | ٱلْأَنْفَال | 75 | 22039 | 88156 | 1582457–1670612 |
| 9 | The Repentance | At-Tawbah | ٱلتَّوْبَة | 129 | 44846 | 179384 | 1670613–1849996 |
| 10 | Jonah | Yunus | يُونُس | 109 | 31118 | 124472 | 1849997–1974468 |
| 11 | Hud | Hud | هُود | 123 | 32360 | 129440 | 1974469–2103908 |
| 12 | Joseph | Yusuf | يُوسُف | 111 | 30088 | 120352 | 2103909–2224260 |
| 13 | The Thunder | Ar-Ra'd | ٱلرَّعْد | 43 | 14744 | 58976 | 2224261–2283236 |
| 14 | Abraham | Ibrahim | إِبْرَاهِيم | 52 | 14564 | 58256 | 2283237–2341492 |
| 15 | The Rock City | Al-Hijr | ٱلْحِجْر | 99 | 11648 | 46592 | 2341493–2388084 |
| 16 | The Bee | An-Nahl | ٱلنَّحْل | 128 | 32102 | 128408 | 2388085–2516492 |
| 17 | The Night Journey | Al-Isra | ٱلْإِسْرَاء | 111 | 27254 | 109016 | 2516493–2625508 |
| 18 | The Cave | Al-Kahf | ٱلْكَهْف | 110 | 26954 | 107816 | 2625509–2733324 |
| 19 | Mary | Maryam | مَرْيَم | 98 | 16345 | 65380 | 2733325–2798704 |
| 20 | Ta-Ha | Ta-Ha | طه | 135 | 22327 | 89308 | 2798705–2888012 |
| 21 | The Prophets | Al-Anbiya | ٱلْأَنْبِيَاء | 112 | 20608 | 82432 | 2888013–2970444 |
| 22 | The Pilgrimage | Al-Hajj | ٱلْحَجّ | 78 | 21768 | 87072 | 2970445–3057516 |
| 23 | The Believers | Al-Mu'minun | ٱلْمُؤْمِنُون | 118 | 18172 | 72688 | 3057517–3130204 |
| 24 | The Light | An-Nur | ٱلنُّور | 64 | 23609 | 94436 | 3130205–3224640 |
| 25 | The Criterion | Al-Furqan | ٱلْفُرْقَان | 77 | 15747 | 62988 | 3224641–3287628 |
| 26 | The Poets | Ash-Shu'ara | ٱلشُّعَرَاء | 227 | 22579 | 90316 | 3287629–3377944 |
| 27 | The Ants | An-Naml | ٱلنَّمْل | 93 | 19665 | 78660 | 3377945–3456604 |
| 28 | The Narrations | Al-Qasas | ٱلْقَصَص | 88 | 24319 | 97276 | 3456605–3553880 |
| 29 | The Spider | Al-Ankabut | ٱلْعَنْكَبُوت | 69 | 17518 | 70072 | 3553881–3623952 |
| 30 | The Romans | Ar-Rum | ٱلرُّوم | 60 | 14287 | 57148 | 3623953–3681100 |
| 31 | Luqman | Luqman | لُقْمَان | 34 | 8995 | 35980 | 3681101–3717080 |
| 32 | The Prostration | As-Sajdah | ٱلسَّجْدَة | 30 | 6413 | 25652 | 3717081–3742732 |
| 33 | The Allies | Al-Ahzab | ٱلْأَحْزَاب | 73 | 23322 | 93288 | 3742733–3836020 |
| 34 | Sheba | Saba | سَبَأ | 54 | 14792 | 59168 | 3836021–3895188 |
| 35 | The Originator | Fatir | فَاطِر | 45 | 13319 | 53276 | 3895189–3948464 |
| 36 | Ya-Sin | Ya-Sin | يس | 83 | 12461 | 49844 | 3948465–3998308 |
| 37 | Those Ranked in Columns | As-Saffat | ٱلصَّافَّات | 182 | 15568 | 62272 | 3998309–4060580 |
| 38 | Sad | Sad | ص | 88 | 12631 | 50524 | 4060581–4111104 |
| 39 | The Throngs | Az-Zumar | ٱلزُّمَر | 75 | 20002 | 80008 | 4111105–4191112 |
| 40 | The Forgiver | Ghafir | غَافِر | 85 | 20785 | 83140 | 4191113–4274252 |
| 41 | Detailed | Fussilat | فُصِّلَت | 54 | 13871 | 55484 | 4274253–4329736 |
| 42 | The Consultation | Ash-Shura | ٱلشُّورَىٰ | 53 | 14484 | 57936 | 4329737–4387672 |
| 43 | The Ornaments of Gold | Az-Zukhruf | ٱلزُّخْرُف | 89 | 14810 | 59240 | 4387673–4446912 |
| 44 | The Smoke | Ad-Dukhan | ٱلدُّخَان | 59 | 6040 | 24160 | 4446913–4471072 |
| 45 | The Kneeling | Al-Jathiyah | ٱلْجَاثِيَة | 37 | 8574 | 34296 | 4471073–4505368 |
| 46 | The Sand Dunes | Al-Ahqaf | ٱلْأَحْقَاف | 35 | 10974 | 43896 | 4505369–4549264 |
| 47 | Muhammad | Muhammad | مُحَمَّد | 38 | 9994 | 39976 | 4549265–4589240 |
| 48 | The Victory | Al-Fath | ٱلْفَتْح | 29 | 10212 | 40848 | 4589241–4630088 |
| 49 | The Chambers | Al-Hujurat | ٱلْحُجُرَات | 18 | 6337 | 25348 | 4630089–4655436 |
| 50 | Qaf | Qaf | ق | 45 | 6259 | 25036 | 4655437–4680472 |
| 51 | The Scattering Winds | Adh-Dhariyat | ٱلذَّارِيَات | 60 | 6314 | 25256 | 4680473–4705728 |
| 52 | The Mount | At-Tur | ٱلطُّور | 49 | 5474 | 21896 | 4705729–4727624 |
| 53 | The Star | An-Najm | ٱلنَّجْم | 62 | 5953 | 23812 | 4727625–4751436 |
| 54 | The Moon | Al-Qamar | ٱلْقَمَر | 55 | 6206 | 24824 | 4751437–4776260 |
| 55 | The Beneficent | Ar-Rahman | ٱلرَّحْمَٰن | 78 | 6841 | 27364 | 4776261–4803624 |
| 56 | The Inevitable | Al-Waqi'ah | ٱلْوَاقِعَة | 96 | 7081 | 28324 | 4803625–4831948 |
| 57 | The Iron | Al-Hadid | ٱلْحَدِيد | 29 | 10369 | 41476 | 4831949–4873424 |
| 58 | The Pleading Woman | Al-Mujadila | ٱلْمُجَادِلَة | 22 | 8426 | 33704 | 4873425–4907128 |
| 59 | The Exile | Al-Hashr | ٱلْحَشْر | 24 | 7995 | 31980 | 4907129–4939108 |
| 60 | The Examined One | Al-Mumtahanah | ٱلْمُمْتَحَنَة | 13 | 6453 | 25812 | 4939109–4964920 |
| 61 | The Column | As-Saff | ٱلصَّفّ | 14 | 3964 | 15856 | 4964921–4980776 |
| 62 | The Congregation | Al-Jumu'ah | ٱلْجُمُعَة | 11 | 3156 | 12624 | 4980777–4993400 |
| 63 | The Hypocrites | Al-Munafiqun | ٱلْمُنَافِقُون | 11 | 3362 | 13448 | 4993401–5006848 |
| 64 | The Mutual Loss | At-Taghabun | ٱلتَّغَابُن | 18 | 4508 | 18032 | 5006849–5024880 |
| 65 | The Divorce | At-Talaq | ٱلطَّلَاق | 12 | 5136 | 20544 | 5024881–5045424 |
| 66 | The Prohibition | At-Tahrim | ٱلتَّحْرِيم | 12 | 4582 | 18328 | 5045425–5063752 |
| 67 | The Sovereignty | Al-Mulk | ٱلْمُلْك | 30 | 5573 | 22292 | 5063753–5086044 |
| 68 | The Pen | Al-Qalam | ٱلْقَلَم | 52 | 5280 | 21120 | 5086045–5107164 |
| 69 | The Inevitable Reality | Al-Haqqah | ٱلْحَاقَّة | 52 | 4647 | 18588 | 5107165–5125752 |
| 70 | The Ways of Ascent | Al-Ma'arij | ٱلْمَعَارِج | 44 | 3993 | 15972 | 5125753–5141724 |
| 71 | Noah | Nuh | نُوح | 28 | 3976 | 15904 | 5141725–5157628 |
| 72 | The Jinn | Al-Jinn | ٱلْجِنّ | 28 | 4669 | 18676 | 5157629–5176304 |
| 73 | The Enwrapped One | Al-Muzzammil | ٱلْمُزَّمِّل | 20 | 3566 | 14264 | 5176305–5190568 |
| 74 | The Cloaked One | Al-Muddaththir | ٱلْمُدَّثِّر | 56 | 4321 | 17284 | 5190569–5207852 |
| 75 | The Resurrection | Al-Qiyamah | ٱلْقِيَامَة | 40 | 2888 | 11552 | 5207853–5219404 |
| 76 | Man | Al-Insan | ٱلْإِنْسَان | 31 | 4454 | 17816 | 5219405–5237220 |
| 77 | Those Sent Forth | Al-Mursalat | ٱلْمُرْسَلَات | 50 | 3505 | 14020 | 5237221–5251240 |
| 78 | The Great News | An-Naba | ٱلنَّبَأ | 40 | 3219 | 12876 | 5251241–5264116 |
| 79 | Those Who Extract | An-Nazi'at | ٱلنَّازِعَات | 46 | 3235 | 12940 | 5264117–5277056 |
| 80 | He Frowned | Abasa | عَبَسَ | 42 | 2424 | 9696 | 5277057–5286752 |
| 81 | The Overthrowing | At-Takwir | ٱلتَّكْوِير | 29 | 1818 | 7272 | 5286753–5294024 |
| 82 | The Cleaving | Al-Infitar | ٱلْإِنْفِطَار | 19 | 1433 | 5732 | 5294025–5299756 |
| 83 | The Defrauders | Al-Mutaffifin | ٱلْمُطَفِّفِين | 36 | 3101 | 12404 | 5299757–5312160 |
| 84 | The Splitting Open | Al-Inshiqaq | ٱلْإِنْشِقَاق | 25 | 1894 | 7576 | 5312161–5319736 |
| 85 | The Constellations | Al-Buruj | ٱلْبُرُوج | 22 | 1936 | 7744 | 5319737–5327480 |
| 86 | The Nightcomer | At-Tariq | ٱلطَّارِق | 17 | 1113 | 4452 | 5327481–5331932 |
| 87 | The Most High | Al-A'la | ٱلْأَعْلَىٰ | 19 | 1297 | 5188 | 5331933–5337120 |
| 88 | The Overwhelming | Al-Ghashiyah | ٱلْغَاشِيَة | 26 | 1645 | 6580 | 5337121–5343700 |
| 89 | The Dawn | Al-Fajr | ٱلْفَجْر | 30 | 2456 | 9824 | 5343701–5353524 |
| 90 | The City | Al-Balad | ٱلْبَلَد | 20 | 1475 | 5900 | 5353525–5359424 |
| 91 | The Sun | Ash-Shams | ٱلشَّمْس | 15 | 1060 | 4240 | 5359425–5363664 |
| 92 | The Night | Al-Layl | ٱللَّيْل | 21 | 1375 | 5500 | 5363665–5369164 |
| 93 | The Morning Light | Ad-Duha | ٱلضُّحَىٰ | 11 | 774 | 3096 | 5369165–5372260 |
| 94 | The Expansion | Ash-Sharh | ٱلشَّرْح | 8 | 498 | 1992 | 5372261–5374252 |
| 95 | The Fig | At-Tin | ٱلتِّين | 8 | 783 | 3132 | 5374253–5377384 |
| 96 | The Clot | Al-Alaq | ٱلْعَلَق | 19 | 1257 | 5028 | 5377385–5382412 |
| 97 | The Decree | Al-Qadr | ٱلْقَدْر | 5 | 638 | 2552 | 5382413–5384964 |
| 98 | The Clear Evidence | Al-Bayyinah | ٱلْبَيِّنَة | 8 | 1749 | 6996 | 5384965–5391960 |
| 99 | The Earthquake | Az-Zalzalah | ٱلزَّلْزَلَة | 8 | 733 | 2932 | 5391961–5394892 |
| 100 | The Chargers | Al-Adiyat | ٱلْعَادِيَات | 11 | 785 | 3140 | 5394893–5398032 |
| 101 | The Striking Calamity | Al-Qari'ah | ٱلْقَارِعَة | 11 | 712 | 2848 | 5398033–5400880 |
| 102 | Competition in Increase | At-Takathur | ٱلتَّكَاثُر | 8 | 591 | 2364 | 5400881–5403244 |
| 103 | The Declining Day | Al-Asr | ٱلْعَصْر | 3 | 368 | 1472 | 5403245–5404716 |
| 104 | The Traducer | Al-Humazah | ٱلْهُمَزَة | 9 | 664 | 2656 | 5404717–5407372 |
| 105 | The Elephant | Al-Fil | ٱلْفِيل | 5 | 483 | 1932 | 5407373–5409304 |
| 106 | Quraysh | Quraysh | قُرَيْش | 4 | 396 | 1584 | 5409305–5410888 |
| 107 | The Neighborly Assistance | Al-Ma'un | ٱلْمَاعُون | 7 | 537 | 2148 | 5410889–5413036 |
| 108 | The Abundance | Al-Kawthar | ٱلْكَوْثَر | 3 | 270 | 1080 | 5413037–5414116 |
| 109 | The Disbelievers | Al-Kafirun | ٱلْكَافِرُون | 6 | 487 | 1948 | 5414117–5416064 |
| 110 | The Support | An-Nasr | ٱلنَّصْر | 3 | 412 | 1648 | 5416065–5417712 |
| 111 | The Palm Fiber | Al-Masad | ٱلْمَسَد | 5 | 429 | 1716 | 5417713–5419428 |
| 112 | The Sincerity | Al-Ikhlas | ٱلْإِخْلَاص | 4 | 288 | 1152 | 5419429–5420580 |
| 113 | The Daybreak | Al-Falaq | ٱلْفَلَق | 5 | 379 | 1516 | 5420581–5422096 |
| 114 | Mankind | An-Nas | ٱلنَّاس | 6 | 391 | 1564 | 5422097–5423660 |

## Files in this deposit

- `quran-dna-full.txt` — the full base stream, wrapped at 60 bases per line.
- `MANIFEST-DNA-FULL.md` — this manifest.
- `encode_quran_dna.py` — the encoder (extraction + encoding).
- `validate_dna.py` — the hygiene validator (report-only).
- `decode_quran_dna.py` — the independent decoder, written separately.
- `INDEPENDENT-DECODER-REPORT.md` — the decoder's verdict, preserved unedited.
- `QURAN-DNA-FULL-PRINT.pdf` — the paper book typeset from the verified
  sequence file.

## Independent verification

A separate agent wrote an independent decoder from the specification alone —
no encoder code read or shared — and ran it end to end. **VERDICT: PASS.**
Its decoded bytes are byte-for-byte equal to its own independent extraction
of the master's Arabic stream; both hash to
`fbeb0083b2f46b2f5e6d27dd6ce6b38867f91a8b52d612bd96143b58b9f6ec6d`, and the base stream hashes to
`d92efa7682d2047068d45804716978bc1667c98e38f6693c9f1f3b69eb658c10` — the figures printed above. Its verse count:
6,236 of 6,236; total runs 6,462. Its report,
`INDEPENDENT-DECODER-REPORT.md`, is preserved unedited in this deposit.

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 1,063,652 · C 1,532,904 · G 1,784,439 · T 1,042,665
- GC content: 61.1643%
- Homopolymer runs: 4,908,376 in total; longest run 4;
  runs of length ≥ 4: 10,538; ≥ 6: 0; ≥ 8: 0; ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. A synthesis-grade layer would add
screening, addressing, and error correction on top of this codec.
