# Chuvash (chv) Quran translation draft — build report

Status: IN PROGRESS — DRAFT — NOT PUBLISHED. NOT landed, NOT shelved, NOT committed, NOT pushed. Stops before landing per task instruction; awaits a fresh independent checker.

Lane authority: Robert Tilford's ruling 2026-11-27 21:16 CST (open-in-order queue: … Komi-Permyak, Chuvash, Southern Sámi, Võro, North Frisian). Brief: CANDIDATE-BRIEF-CHUVASH.md, gate outlook PASS-CANDIDATE, conditions 1–7.

Honesty notes carried from the brief:
- A partial Chuvash Qur'an tafsir by Ruslan Saifutdinov exists (2006 commission of the Spiritual Administration of Muslims of the Chuvash Republic; juz' 30 volume, Cheboksary: Novoe Vremya, 2020). NO "first" wording appears anywhere in this build.
- The Bible control (complete Bible, 2009, Institute for Bible Translation, Moscow) and modern dictionaries/corpora have unverified licences: used as fact/citation/control only, never copied wording.
- Target standard: single settled literary Chuvash in the modern Cyrillic standard (Russian alphabet plus Ӑӑ, Ӗӗ, Ҫҫ, Ӳӳ), Anatri-weighted literary base as recorded in the brief §2.
- Oghuric bar: no Tatar, Turkish, or other Common Turkic form is seated as Chuvash on kinship grounds.

Build method: first-pass engine-rendered draft following the sibling-lane (Komi-Zyrian) spec pattern — every verse seat filled from a verified attested dictionary; every Master content word with no verified seat carries the visible marker ⟦GAP: <english term>⟧; names and scripture titles carried in the Master's forms; Basmalah: 1:1 translated as verse 1:1, unnumbered opening line at every other surah except 9.

## Result (2026-11-28)

BUILD COMPLETE as a first-pass draft. STOPPED BEFORE LANDING as instructed: nothing landed, shelved, committed, or pushed. The draft awaits a fresh independent checker.

- Counts: 6,236 / 6,236 verses built from the Locked English Master (MD5 ecc5b8e2848e5044186b7ad82bed9f4e, verified); seat-set equality with the Master: TRUE; per-surah grid mismatches: NONE; empty seats: NONE; 'redacted' seats: NONE.
- Basmalah: seated form «Турӑ ятпа, Аван, Аванлӑх.»; 1:1 is the Basmalah verse; 112 unnumbered Basmalah lines in quran-chv.txt (every surah except 1 and 9); 1:3 == «Аван, Аванлӑх.» Mercy seating disclosed (no attested mercy noun in the harvested inventories; аван "good" / аванлӑх "kindness", both kaikki-attested).
- Dictionary: 2,223 English seat keys — 2,088 gloss-inverted from kaikki Chuvash entries (CC BY-SA) plus a curated core, every curated seat verified mechanically against the attestation inventory; unverified curated seats dropped and logged (work/unverified-dict.json). Attestation inventory: kaikki 1,003 headwords + 2,047 forms; Apertium apertium-chv 75,337 stem/form tokens; union 77,249 forms (sources/attestation-inventory.json).
- GAP census: 5,842 of 6,236 seats carry GAP markers; 23,456 markers; 4,384 distinct GAP terms. Largest: down 214, away 211, punishment 207, sent 172, out 164, at 149, revelations 135, reward 120, knowledge 111. Full census: work/gap-census.json; disclosure: FLAGS-AND-GAPS-DISCLOSURE-CHV-2026-11-28.md. The census is large because kaikki carries only ~1,000 Chuvash headwords; it is disclosed on the book's face.
- Screens (verify.py, the Komi-Zyrian checker lesson applied from the start): token attestation — 651 distinct Cyrillic tokens, 0 untraced candidates; whitespace-token retained-Latin against the explicit allowlist (work/names-allowlist.json) — 134 types / 1,064 tokens allowlisted, 0 non-allowlist candidates; mixed-script on whitespace tokens — NONE.
- Sources: kaikki.org Chuvash dictionary dump (CC BY-SA); Apertium apertium-chv lexc (GPL platform) as attestation inventory; Bible control (IBT 2009) and Saifutdinov tafsir as fact/citation only, licences unverified — full record in LICENCES-RECORDED-2026-11-28.md. Hugging Face datasets, Turku corpus, and the Skvortsov/Ashmarin dictionaries were NOT used for seats (licences unverified).
- Files: verses-store.json, master-verses.json, quran-chv.json, quran-chv.txt, ayah-companion-manuscript-CHV.md (front matter carries the DRAFT — NOT PUBLISHED label, the Saifutdinov acknowledgement, and the GAP disclosure; no "first" wording anywhere), glossary.md, BUILD-SPEC.md, verify.py, work/build.py, work/assemble.py, work/manuscript.py, work/gap-census.json, work/verify-candidates.json.
- Next step, not taken: a fresh independent checker pass. No landing action of any kind has been taken or will be taken by this build.
