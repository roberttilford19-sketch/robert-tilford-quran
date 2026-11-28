# Võro (vro) Quran draft — build report (2026-11-28)

**Status: BUILD COMPLETE — STOPPED BEFORE LANDING, as ordered.**
Nothing was shelved, committed, or pushed. The draft stands in
~/workspace/ayah-voro/ only, labelled DRAFT — NOT PUBLISHED, and
awaits a fresh independent checker who did not build it.

## Lane authority
Opened in order under Robert Tilford's ruling of 2026-11-27,
21:16 CST (queue … Southern Sámi, Võro, North Frisian; Southern
Sámi landed first). Settled rulings R1/R2 from the candidate
brief were followed: the modern Võro literary norm excluding
Seto is the build norm, and the archaic South Estonian Bible
(*Wastne Testament*, 1686) stands as historical control only,
never as a source of modern forms.

## Counts (machine-verified, verify.py final run)
- Verses built: **6,236 / 6,236** — seat-set equality with the
  Locked English Master grid: true; per-surah mismatches: NONE;
  empty seats: NONE.
- Basmalah: 1:1 = "Jumala nimeh, Arm, Arm." (exact); 1:3 =
  "Arm, Arm." (exact); Basmalah lines in built text: 113
  (112 unnumbered openings + verse 1:1); surah 9 carries none.
- GAP census: **6,009 seats** carry GAP markers; **29,698
  markers**; **5,300 distinct GAP terms**. Census file:
  gap-census.json; disclosure: FLAGS-AND-GAPS-DISCLOSURE-VRO-
  2026-11-28.md.
- Dictionary size: **504 verified English–Võro entries** seated
  (work/dict_core.py, screened by work/build_engine.py);
  27 concepts unverified and held as GAPs (listed in the
  disclosure). Attestation inventories: 20,632 GiellaLT lemmas,
  81,133 corpus word forms, 606 kaikki/Wiktionary headwords
  (7,543 forms).
- Screens, run from the start as ordered: whitespace-token
  retained-Latin screen with explicit allowlist — **0 candidate
  types, 0 tokens**; mixed-script (Cyrillic) screen — **NONE**;
  "redacted" string — NONE. Two screen bugs were found and fixed
  during the build and are part of the record: an early
  normalisation stripped diaereses (ü→u) and falsely dropped
  verified forms, and the allowlist's disjointed-letter entry
  "Sin" briefly captured the English word "sin" (145+ seats) —
  both fixed, re-verified clean.

## Sources
GiellaLT lang-vro (LGPL v3; stems, wordfreq corpus list);
Wiktionary via kaikki (CC BY-SA); Võro Institute dictionary
(synaq.org / Iva 2002) and *Wastne Testament* (1686) as controls
by fact and citation only. Full record:
LICENCES-RECORDED-2026-11-28.md. No bulk scraping of synaq.org;
no person or institution contacted.

## Files
- ayah-companion-manuscript-VRO.md — the draft with its honest
  face (DRAFT — NOT PUBLISHED, base, GAP census, devices).
- quran-vro.txt / quran-vro.json — built text (6,236 verses).
- verses-store.json — seat store; master-verses.json — Master grid.
- BUILD-SPEC.md, glossary.md, build.py, verify.py, assemble.py,
  work/build_engine.py, work/dict_core.py,
  work/unverified-dict.json, work/verify-candidates.json.
- sources/ — kaikki-vro.jsonl, giella-lemmas.json,
  wordfreq-forms.json, est2vro-giella.json, giella-vro/stems/,
  giella-vro-LICENSE.txt, wordfreq.txt.

## Novelty wording
No "first ever" claim anywhere. The bounded brief form stands:
the first complete Võro Qur'an translation found — after
research (27 November 2026).

## Next step (not taken)
A fresh independent checker pass, then Robert's word before any
landing. This build does not land, shelve, commit, or push.
