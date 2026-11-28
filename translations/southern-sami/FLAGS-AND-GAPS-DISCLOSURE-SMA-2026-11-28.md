# Southern Sámi lane — flags and gaps disclosure (2026-11-28)

DRAFT — NOT PUBLISHED. This disclosure rides with the build in
~/workspace/ayah-southern-sami/ and is summarised on the face of
ayah-companion-manuscript-SMA.md.

## GAP census (verify.py, this build)
- Seats carrying GAP markers: 5,762 of 6,236.
- GAP markers total: 24,673. Distinct GAP terms: 3,509.
- Largest GAP terms: of 3,502; lord 972; by 414; nor 270;
  except 269; into 192; give 190; given 172; whom 155; any 154;
  everything 150; used 149; can 145; righteous 141; revealed 141;
  revelations 135; disbelieve 133; another 132; reward 120;
  worship 115; scripture 115. Full census: work/gap-census.json.
- Why "of" and "lord" dominate: Southern Sámi carries the
  genitive relation by case endings, and this plain-style draft
  generates no case suffixes (case formation involves Umlaut stem
  changes — see BUILD-SPEC.md), so "of" is held open rather than
  faked. For "lord", "angel", "prophet", "scripture", "reward",
  and "revelation" no attested seat was found in the
  licence-verified sources harvested for this build (the 2022
  public-domain dictionary and the GiellaLT inventory); under the
  gate law none was invented, and none was borrowed from Northern
  Sámi, Lule Sámi, Skolt Sámi, Norwegian, Swedish, Finnish, or
  Russian. One curated candidate was dropped as unverified and
  logged (work/unverified-dict.json): revelation → volverimmie.

## Screens (verify.py — instrument output, candidates for the
## independent checker, not verdicts)
- Seat-set equality with the Master: TRUE. Per-surah grid
  mismatches: NONE. Empty seats: NONE. 'redacted' seats: NONE.
- Basmalah: 1:1 == "Nomme Jupmele, Åårmegs, Åårmegs." TRUE;
  1:3 == "Åårmegs, Åårmegs." TRUE; 112 unnumbered Basmalah lines
  in quran-sma.txt (every surah except 1 and 9).
- Token attestation: 1,604 distinct seated tokens; 2 untraced
  candidates — (1) a punctuation-fused pair "jupmele?'“satne"
  (two attested words joined by Master punctuation without a
  space; a tokenisation artefact), and (2) one hyphenated
  compound "kraevies-åejjie-goelkh" with a part outside the
  harvested inventory. Both are left standing for the fresh
  independent checker.
- Retained-English screen against the explicit names allowlist
  (work/names-allowlist.json, 135 types): 0 non-allowlist
  candidates.
- Mixed-script screen on whitespace tokens: NONE.

## Flagged devices (all disclosed in BUILD-SPEC.md and glossary.md)
- Citation-form plain style: verbs and nouns seat in dictionary
  citation form; no case or plural suffix is generated.
- Pronouns seat in attested nominative forms for all seats.
- Norwegian spelling practice (æ/ø) applied mechanically to
  source forms in the Swedish practice (ä/ö); presentational
  only. The Swedish practice is preserved dissent.
- "man" seats almetje ("person"); "heaven"/"sky" seat elmie;
  the Basmalah's two mercy names rest on the single attested
  adjective åårmegs. Each is named in the glossary.
- Articles (the/a/an) and the vocative O are dropped.

## Status
The draft stops before landing: nothing landed, shelved,
committed, or pushed. It awaits a fresh independent checker.
