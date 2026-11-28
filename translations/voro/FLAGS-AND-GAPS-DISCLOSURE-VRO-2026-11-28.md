# Võro lane — flags and gaps disclosure (2026-11-28)

- **GAP census (machine count, verify.py):** 6,009 of 6,236 seats
  carry at least one GAP marker; 29,698 GAP markers in total;
  5,300 distinct English GAP terms. Full census: gap-census.json.
  Top GAP terms: except (269), whoever (232), made (218),
  away (218), most (188), sent (172), given (172), believers (159),
  everything (150), until (149), like (148), merciful (145).
- **Dictionary:** 504 verified English–Võro entries seated;
  27 concepts dropped as unverified and held as GAPs throughout:
  camel, close, curse, darkness, desert, eighty, follow, forgive,
  forgiveness, moment, mosque, pray, resurrection, rise, safe,
  servant, seventy, sorrow, swear, temple, thank, throne, turn,
  until, wall, week, worship. Dropped-entry log:
  work/unverified-dict.json (final run lists these 27).
- **Single-stem mercy seating:** both Basmalah mercy names seat
  on arm; disclosed on the manuscript face and in the glossary.
- **Plain-style devices:** verbs in dictionary (ma-infinitive)
  form; nominative nouns with regular plural -q; articles and
  "of" as zero; case markers lõ / h as separate words; vocative
  "O" as zero. All disclosed in BUILD-SPEC and on the face.
- **Screens (verify.py, final run):** seat-set equality true;
  per-surah mismatches NONE; retained-Latin candidates
  (non-allowlist, untraced) 0 types / 0 tokens; Cyrillic
  (mixed-script) candidates NONE; "redacted" seats NONE; empty
  seats NONE; 1:1 and 1:3 equal the fixed Basmalah forms;
  Basmalah string count in built text 113 (112 unnumbered +
  verse 1:1).
- **Known limits:** this is a first-pass engine draft, not a
  literary translation. Word order follows the Master closely;
  Võro case government, verb inflection, and palatalisation
  marking await the independent checker. The GiellaLT Estonian
  gloss bridge was used only to find candidates; every seated
  form still had to trace to a Võro inventory.
- **Seto / Estonian fence:** no Seto form seated (norm R1); no
  Standard Estonian form seated unless independently attested
  in a Võro inventory (the verification screen enforces this
  mechanically against the held inventories).
