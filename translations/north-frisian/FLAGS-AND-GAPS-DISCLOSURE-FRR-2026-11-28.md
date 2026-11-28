# North Frisian (Mooring) lane — flags and gaps disclosure (2026-11-28)

- **GAP census (machine count, verify.py):** 6,190 of 6,236 seats
  carry at least one GAP marker; 50,826 GAP markers in total;
  5,551 distinct English GAP terms. Full census: gap-census.json.
  Top GAP terms: god (2,786), for (1,744), who (1,724),
  those (1,189), lord (972), so (746), on (686), people (679),
  by (414), before (299), upon (279), which (277), there (274),
  except (269), only (265), messenger (235), whoever (232).
- **Dictionary:** 429 verified English–Mooring entries seated;
  65 candidate entries dropped as unverified and held as GAPs
  throughout: after, against, ask, at, because, before, black,
  bright, by, certain, dance, deed, down, dream, fear, few,
  first, follow, food, for, fruit, full, gate, glory, green,
  heavy, hour, judge, learn, light, many, money, morning, much,
  number, on, over, poor, power, red, send, show, side, silver,
  snake, so, some, song, strong, there, thing, true, under, up,
  upon, voice, wait, wall, weak, wheat, who, why, without,
  work, young. Dropped-entry log: work/unverified-dict.json.
  Most of the 65 were desk-side cognate candidates that the
  Mooring inventory correctly refused — the gate working as
  designed, recorded rather than hidden.
- **The God / mercy GAPs:** God, lord and both Basmalah mercy
  names stand as GAPs throughout, including in the fixed
  Basmalah line. Ground: no modern Mooring seat in the held
  inventories; Bendsen's 1860 spellings (Godd / Göd) held as
  historical corroboration only under the Historical Control
  Bar. Disclosed on the manuscript face, in BUILD-SPEC, in the
  glossary and in ATTESTATION-AUDIT-2026-11-28.md.
- **Dialect fence:** no Söl'ring, Fering-Öömrang, Heligoland,
  Halligen, Wiedingharde or Goesharde form seated (968
  other-dialect-only kaikki entries excluded by harvest.py);
  no Saterland Frisian and no West Frisian form seated or
  touched.
- **Plain-style devices:** verbs in dictionary (infinitive)
  form; nominative nouns with attested plurals where held,
  otherwise the same form; articles and "of" as zero (gendered
  articles cannot be assigned mechanically); "you" seated as
  singular dü throughout. All disclosed in BUILD-SPEC and on
  the face.
- **Screens (verify.py, final run):** seat-set equality true;
  per-surah mismatches NONE; retained-Latin candidates
  (non-allowlist, untraced) 0 types / 0 tokens; non-Latin
  (mixed-script) candidates NONE; "redacted" seats NONE; empty
  seats NONE; 1:1 and 1:3 equal the fixed Basmalah forms;
  Basmalah string count in built text 113 (112 unnumbered +
  verse 1:1).
- **Known limits:** this is a first-pass engine draft, not a
  literary translation. Word order follows the Master closely;
  Mooring gender, article selection, verb inflection and V2
  order await the independent checker. The GAP mass is larger
  than in sibling lanes because the held modern Mooring
  inventories are small (463 Mooring-sense entries) and no
  same-dialect Bible control exists; the modern print Mooring
  dictionaries named in LICENCES-RECORDED-2026-11-28.md are
  the checker's road to closing the function-word and
  theological GAPs.
