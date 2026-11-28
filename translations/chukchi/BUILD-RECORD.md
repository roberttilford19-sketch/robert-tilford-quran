# BUILD RECORD — Chukchi (ckt) Quran translation lane

Lane opened by Robert Tilford's ruling, 2026-11-28 (tap + typed word,
on the desk's recommendation), on the conditions of
CANDIDATE-BRIEF-CHUKCHI.md §8 and his three rulings given with the
opening (standard literary norm only; letterform seats fixed before
verse 1 by machine count; the written standard's uniform practice for
the men's/women's consonants). Lane folder: ~/workspace/ayah-chukchi/.

## Build sequence, as run

1. **Pre-build verifications** — PREBUILD-VERIFICATIONS.md: fresh
   Master extraction (6,236 verses, seat set exactly the standard
   grid; Master MD5 ecc5b8e2848e5044186b7ad82bed9f4e); codepoint
   census over the 929-form harvested inventory and ten quoted IBT
   Luke (2017) sentences, fixing Ԓ/ԓ U+0512/0513 (ԯ U+052F: zero in
   both), Ӄ/ӄ, Ӈ/ӈ as single letters, ʼ U+02BC as the only glottal
   letter, with the word-initial digraph conversion disclosed;
   men's/women's written practice found uniform (р-forms) in all
   harvested written sources, no conflict; licences recorded before
   reliance (LICENCES-RECORDED-2026-11-28.md).
2. **Attestation audit** — ATTESTATION-AUDIT-2026-11-28.md: core
   religious vocabulary graded seat by seat. Seated: God
   Тэнантомгыӈэн (IBT running text), spirit, lord/master, servant,
   doubt, death, enmity, envy, hatred, gift, and the pronoun set on
   IBT practice. Refused (GAP): the full ruling-5 list and the whole
   agricultural register.
3. **Engine build** — build.py (own code): seat dictionary assembled
   from the CC BY-SA Wiktionary harvests (pairs, gloss inversion, a
   desk-built Russian→English gloss mapping) plus the curated control
   seats; every seat verified mechanically against the attestation
   inventory (unverified dropped and logged); unseated Master words
   rendered as visible ⟦GAP: word⟧ markers; names from an explicit
   allowlist. Method and devices: BUILD-SPEC.md.
4. **Canonical verification** — verify.py: PASS on all checks (23 in
   the final form): seat-set equality 6,236 = 6,236, per-surah grid,
   Basmalah 1:1 exact and 112 unnumbered lines, GAP census
   reconciled, codepoint zeros (U+052F, U+0027, U+2019, U+04A3,
   U+2018), token attestation screen 0 untraced, retained-Latin
   screen clean.
5. **Independent checker, round 1** — CHECKER-REPORT-INDEPENDENT-
   2026-11-28.md: **FAIL.** Refusal list and GAP honesty passed
   completely; three correctness defects found (FALSE seat even →
   ӄаарамкын, an ethnonym; U+04A3 letterform breach in five seats;
   an epithet-laden names allowlist retaining 1,889 English tokens),
   plus WEAK seats, plus the judgment that the thinness (66,690
   markers) exceeded the Chuvash GAP-tier reservation. Note: the
   round-1 report file as saved on disk truncates mid-§E (recorded
   by the round-2 checker); it travels unedited, as it stands.
6. **Remediation** — PREBUILD-VERIFICATIONS.md §5 (dated addendum):
   even, horse, holiday unseated; ң→ӈ normalised and logged seat by
   seat; allowlist purged to an explicit 131-type keep-set of genuine
   proper names (117 types purged, logged); sun decapitalised; GAP
   hygiene fixed; гымнин citation recorded in-lane. Rebuilt and
   re-verified.
7. **Independent checker, round 2** — CHECKER-REPORT-INDEPENDENT-R2-
   2026-11-28.md: every round-1 finding verified repaired firsthand;
   fresh 15-seat attestation sample VERIFIED 15 / WEAK 0 / FALSE 0;
   census independently recomputed, identical. **Verdict:
   PASS-WITH-GAP-TIER-RESERVATION — DRAFT — NOT PUBLISHED**, the
   reservation stating the census plainly. Ground, in the checker's
   words: the only remaining objection is thinness, which is a
   quantity, not a correctness defect, and is disclosed by the
   markers on the book's face; the tier-changing remediation
   (inventory expansion from fuller sources) is unavailable under
   house law, the fuller dictionaries being in copyright and
   PanLex unreachable.

## Final census (post-remediation, machine-counted)

- Verses: 6,236 (grid clean at all 114 surahs)
- GAP seats: 6,218 · GAP markers: 67,251 · distinct GAP terms: 5,807
- Fully seated verses: 18
- Seat dictionary: 451 keys · names allowlist: 131 types

## Landing — NOT EXECUTED by the building agent

The pack in this folder is complete and ready to land as
translations/chukchi/ in the shelf repository, DRAFT — NOT
PUBLISHED, under the Pipeline Landing Authorization, on the round-2
PASS-WITH-GAP-TIER-RESERVATION. The git landing itself (stage,
commit, push, origin-verify) was **not** executed by the building
agent: a security notice on the shelf repository bars this agent
from running git there. The landing step is flagged for the parent
desk to execute or to surface to Robert. Nothing has been staged,
committed, or pushed by this agent, and no file of this pack has
been copied into the repository by this agent.

## Contact

None. Silent build-and-gift, per the brief: no one was contacted.
