# Udmurt remediation record — 2026-11-28 (second remediation attempt)

Crew stance: this crew built none of the text; it applied the verified
findings of CHECKER-REPORT-INDEPENDENT-2026-11-27.md (verdict FAIL)
under the audit-application standard. Script: work/remediate.py.
Pre-remediation store preserved at work/verses-store-PRE-REMEDIATION.json.
NOT landed, NOT shelved, NOT committed — awaiting fresh independent
re-check by a checker who built/remediated none of it.

## Seats changed, by checker category
1. Script contamination (4 seats): 2:109 оskemды→оскемды; 2:272
   уjed→ужед; 17:72 кошkoz→кошкоз; 20:123 кошke→кошке. Post-check:
   zero Latin-inside-Cyrillic words remain (GAP markers with Cyrillic
   suffixes follow the book's existing GAP+suffix convention).
2. Russian stems/letters: прощ- 41 occurrences (31 verses, surahs
   4–6) → stem гажаса мозмыт- (book's own forgive seat, 2:199/3:135);
   грех 28 occurrences (24 verses) → сьӧлык, plus грешникъёс→
   сьӧлыкасьёс at 7:19; свидетель (person forms, batch A) → адӟись
   (book's seat at 48:8), свидетельлык forms → ⟦GAP: testimony⟧ so
   testimony is GAP-marked consistently book-wide; наказани- forms
   (batch B) and наказать (5:118) → шуккон / шуккыны (book's seat,
   59:7). Scattered forms → GAP: финик→dates (5 seats), Катастрофа
   79:34, падчерицаос 4:23, Храмэ 17:7, христианъёс 22:17, дворец
   27:44 (×2), пастухъёс 28:23, сахар 16:67, горчица 31:16,
   матрацъёсын 56:34, пастбище 79:31/87:4, Эх 75:20/78:40→alas;
   степь 12:100 → ⟦GAP: wilderness⟧; блуждать 2:15 → сюресэз ыштыса.
   Post-check: ZERO tokens containing ф, х, ц, or щ remain book-wide.
3. Number: 18:25 куать→укмыс ("nine").
4. J/L silent seats: Святой/святой (18 tokens book-wide, incl. 59:23,
   62:1, 79:16 and the batch-A Sacred Mosque/month seats) → Сӥлы/сӥлы;
   проклят- (81:25, 111:1 ×2) → ⟦GAP: cursed⟧; колдунство 113:4 →
   ⟦GAP: sorcery⟧; верблюд (54:27, 56:55, 59:6, 88:17, 91:13) →
   ⟦GAP: camel(s)⟧; весы (101:6, 101:8, 17:35) → ⟦GAP: scales⟧;
   столб (89:7, 104:9) → ⟦GAP: pillars⟧.
5. Batch B over-marking un-GAPped onto book seats: messenger 62
   markers, garden 16 (incl. ⟦GAP: gardens of bliss⟧ 5:65 → садъёс),
   witness 25 + witnessing (5:8 → адӟись луыса), wise 15, wisdom 4
   (→ визь). Testimony stays GAP (see §2 — now consistent book-wide).
   Disclosure for the re-checker: garden/witness/wisdom GAPs remain
   at a few seats OUTSIDE batch B (garden 11, witness 5, wisdom 17,
   wise 1 at 2:32) — outside the checker's batch-B finding and this
   task's scope; the re-checker may wish to rule on them.
6. Messenger unified: ыстэм мурт book-wide (322 occurrences after
   remediation); пайгамбар-for-messenger removed at all twelve
   surah 24–25 seats plus 22:78 (14 tokens) — пайгамбар is prophet
   only (zero пайгамбар at messenger-only master seats, verified);
   GAP-messenger markers: zero remain. ⟦GAP: Satan⟧ at 58:10, 58:19
   (4 markers) → Satan per names policy. Disclosure of the
   compositional ыстэм мурт seat recorded in glossary.md and in a
   dated addendum to ATTESTATION-AUDIT-2026-11-27.md.
7. Unifications: Resurrection Day → Суд нунал at all 68 master
   "Day of Resurrection" seats (26 seats changed: 10 Улӟон Нунал in
   batch A, 9 GAP forms in batch B, 7 GAP forms in batch H; verified
   zero Day-of-Resurrection seats without Суд нунал). Holy Spirit →
   Сӥлы Лул at all four term seats (2:87, 2:253, 5:110, 16:102).
8. Front matter: quran-udm.txt now opens "QURAN — UDMURT DRAFT /
   DRAFT — NOT PUBLISHED" with a status note (build.py amended).
9. Lesser fidelity: 59:7 эшъёслы→матысь муртъёслы (relatives);
   12:4 "eleven planets" → ⟦GAP: planets⟧ (was кизили, stars);
   11:41 Куштӥсь→Гажаса мозмытӥсь (Forgiving); 24:2 Бӧрысь Нуналлы→
   Берпул Нуналлы; 39:53 янгышъёсты→сьӧлыкъёсты and Каллен улӥсь→
   Гажась (the Clement); 14:4 Тодос→Визь (the Wise). Satan/devil
   name forms restored to the Master's word at 4:117, 12:100,
   18:63, 19:44 (×2), 19:45, 19:68, 19:83, 21:82, 22:3, 41:36
   (Devil), and 38:37 "demons" → ⟦GAP: demons⟧.

## Rebuilt counts (verify.py, run 2026-11-28 after final rebuild)
- Store seats 6,236 / master seats 6,236 / seat-set equal: True.
- Per-surah mismatches: NONE. Empty seats: NONE. "redacted": NONE.
- 1:1 == Basmalah: True.
- Built quran-udm.json == verses-store.json at every seat: True.
- All twelve work/batch-*.json files identical to the store: True.
- GAP census after remediation: 1,732 GAP seats / 2,430 GAP markers
  (before: 1,759 seats / 2,534 markers).
- Purple sweep reconciled: work/purple-untraced.json regenerated;
  5,364 untraced candidate types (candidates only, per house law);
  none of the checker's flagged Russian forms appears in the new list.

Status: STOPPED as instructed — not landed, not shelved, not
committed. Ready for a fresh independent re-check.
