# Chuvash lane — build specification (fixed 2026-11-28)

Governing documents: CANDIDATE-BRIEF-CHUVASH.md (PASS-CANDIDATE, conditions 1–7), settled for build by Robert Tilford's ruling of 2026-11-27, 21:16 CST (open-in-order queue: … Komi-Permyak, Chuvash, Southern Sámi, Võro, North Frisian). Master of record: the Locked English Master (~/workspace/ayah-audit/corrected/ayah-companion-manuscript.md, MD5 ecc5b8e2848e5044186b7ad82bed9f4e — verified at build time); verse texts in ~/workspace/ayah-chuvash/master-verses.json (114 surahs, 6,236 verses, machine-verified against the Master grid).

## Orthography and base
- Norm: literary Chuvash in the modern Cyrillic standard (Russian alphabet plus Ӑӑ, Ӗӗ, Ҫҫ, Ӳӳ), the Anatri-weighted literary base named in brief §2, as used in the 2009 Bible, the Cheboksary dictionaries, and current press. Chuvash ONLY, ISO chv.
- OGHURIC BAR: no Tatar, Turkish, or other Common Turkic form is ever seated as Chuvash (brief head note). Russian-shaped loans seat only where they stand in the harvested Chuvash inventories themselves.
- The four extra letters are never normalised to their Russian look-alikes.

## Base and honesty
- BUILD TIER: first-pass, engine-rendered draft. Every verse seat is filled from the verified dictionary; every Master content word with no verified seat carries the visible GAP marker. The GAP census is large and disclosed on the book's face.
- NO "first" wording anywhere (brief §5/§8 condition 7): a partial Chuvash Qur'an tafsir by Ruslan Saifutdinov exists (2006 commission; juzʾ 30 volume, 2020). The draft's front matter acknowledges it plainly.
- Bible control (complete Bible, 2009, Institute for Bible Translation, Moscow) and the Saifutdinov tafsir: FACT AND CITATION ONLY; licence unverified, recorded in LICENCES-RECORDED-2026-11-28.md.
- The draft stops before landing and before any independent check.

## Names policy
Personal names and scripture titles are carried in the Master's forms, against the explicit allowlist in work/names-allowlist.json (135 types seated). Capitalised Master epithets are NOT names and never ride the allowlist (the Komi-Zyrian checker lesson). Satan seats as Шуйттан (kaikki-attested).

## The Basmalah
Surah 1:1 IS the Basmalah, translated as verse 1:1. Every other surah except 9 carries it as an unnumbered opening line (112 lines). Seated form: **Турӑ ятпа, Аван, Аванлӑх.** — "In the name of God, the Good, the Kindness": ятпа is the regular instrumental of ят "name" (kaikki headword); Beneficent seats аван "good" and Merciful seats аванлӑх "kindness" (аван + -лӑх, both kaikki-attested), because no attested mercy noun was found in the harvested inventories; disclosed on the book's face and in the glossary. Verse 1:3 is the same two names without the frame: "Аван, Аванлӑх."

## GAP policy
A seat that cannot be carried on attested forms takes ⟦GAP: <english term>⟧ inline. NEVER invent a form; NEVER borrow silently from Tatar, Turkish, Russian, or any other language.

## Grammar / plain-style devices (all disclosed)
- Verbs seat in the dictionary citation form; person and tense are carried by subject and time words.
- Plural: the suffix -сем (kaikki suffix entry) seats wherever the Master has a plural noun.
- Locative -ра and ablative -рен (kaikki suffix entry '-рен') seat as separate words for in / from / than — the sibling lanes' suffix-device pattern.
- among/between seats хушшинчи, the attested inessive form in the Apertium lexc paradigm examples.
- Copula/auxiliary devices: be-family → пул; will/shall/would → пулӗ; have-family → пур (the Chuvash existential possession construction); do-family → ту (kaikki verb "to do").
- Pronouns seat in attested kaikki forms (nominative, genitive, accusative paradigms).
- Articles (the/a/an) and the vocative O are dropped; Chuvash has neither.
- The two Master seats carrying a literal "<redacted>" placeholder are rendered for their surrounding sense; the string "redacted" never appears.

## Verification (verify.py)
Seat-set equality and per-surah grid; GAP census; Basmalah checks; 'redacted' and empty-seat checks; token attestation screen (0 untraced candidates at build); whitespace-token retained-Latin screen against the explicit allowlist (0 non-allowlist); mixed-script screen on whitespace tokens (NONE). Instrument output is a candidate list for the fresh independent checker, not a verdict.
