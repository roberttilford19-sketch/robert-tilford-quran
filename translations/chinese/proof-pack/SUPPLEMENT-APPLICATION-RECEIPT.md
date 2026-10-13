# SUPPLEMENT APPLICATION RECEIPT — Chinese Ayah Companion, Patch Set 1

**Applied:** 2026-10-12 (evening) · **Result: 10 of 10 changes applied — 9 supplement rows + 1 harmonization; 0 forced, 0 failed. All gates PASS.**

**Approval basis:** Robert approved the 9-row Particle Supplement with **的确** for the three polarity flips, and ruled that **84:15 be harmonized to 的确** as well (his tap, 2026-10-12 ~22:15 CDT).

**Working file:** `patched/ayah-companion-manuscript-ZH-PATCHED.md` — edited in place.
**Freeze before editing:** the v2 state was copied to `patched/ayah-companion-manuscript-ZH-PATCHED-v2.md` and byte-verified identical (sha256 `11b3a78a…`) before any change was made. The working file was asserted byte-equal to the frozen v2 again inside the application script before the first replacement.

**Method (same discipline as the main application):** verse-block-scoped matching — each row's complete current CN was asserted **verbatim** inside its own verse block, then replaced with the approved final text. Any mismatch would have aborted the run with no file written; there were none.

---

## Per-row outcomes

| # | Verse | Class | Outcome | The change |
|---|-------|-------|---------|------------|
| 1 | 21:42 | DROPPED (bal rebuttal) | APPLIED | …至仁主？”**但**他们转身… → …至仁主？”**不然，**他们转身… |
| 2 | 37:29 | DROPPED (bal rebuttal) | APPLIED | 他们将说：“**不然，**你们自己不是信道者。 (row built on the patched text — the verse's applied P-05 信道者 repair preserved) |
| 3 | 37:30 | DROPPED (bal rebuttal) | APPLIED | …没有任何权力。**不然，**你们自己是叛逆的民众。 |
| 4 | 69:38 | DROPPED (oath-form) | APPLIED | **不——**我确以你们所见的发誓。 |
| 5 | 70:40 | DROPPED (oath-form) | APPLIED | **不——**我以东西方的主发誓，我确是全能的。 |
| 6 | 84:16 | DROPPED (oath-form) | APPLIED | **不——**我以晚霞起誓。 |
| 7 | 34:3 | POLARITY-FLIP (balā) | APPLIED | 你说：“**不然**，以我的主发誓…” → 你说：“**的确**，以我的主发誓…” |
| 8 | 64:7 | POLARITY-FLIP (balā) | APPLIED | 你说：“**不然**，以我的主发誓…” → 你说：“**的确**，以我的主发誓…” |
| 9 | 75:4 | POLARITY-FLIP (balā) | APPLIED | **不然；**我确能重造他的指尖。 → **的确，**我确能重造他的指尖。 (carrier only — the verse's We→我 residue is a P-03-supplement matter, untouched here, as the supplement row itself noted) |
| 10 | 84:15 | Harmonization (Robert's ruling) | APPLIED | **不然**，他的主一直在看着他。 → **的确**，他的主一直在看着他。 — carrier swap only; nothing else in the verse changed |

Carrier accounting after this pass: all four balā polarity verses (34:3, 64:7, 75:4, 84:15) now open with the affirmative **的确**, matching Robert's EN "Yes —" surface and the Arabic answer particle. The dropped-particle restorations use the manuscript's own faithful carriers （不然 for bal rebuttals, 不—— for the oath form), per the applied P-08 precedent.

---

## Gates (full suite re-run on v3 — all PASS)

- **Parity:** 6,236 / 6,236 verse markers, sequence identical to v2; header identical.
- **Arabic:** 639,899 characters in v2 and v3; the Arabic remainder of **every** verse block byte-identical v2→v3 — Arabic untouched.
- **Isolation:** v2→v3 differing blocks = **exactly the 10 target verses**; each new CN equals its approved final text verbatim (checked against the supplement's proposed texts and, for 84:15, against the ruling's specified result). No verse outside the 10 changed.
- **Do-not-touch:** 2:275, 5:60, 16:36, 39:17 byte-identical; 2:276 byte-identical with 利息 intact; 2:3 byte-identical with 幽玄 intact.
- **Census re-run** (census.py, pointed at v3): parity_bad 0 · total candidate flags **5, all USURY-LIXI** — the five ruled Ruling-1 controls (2:275, 2:276, 2:278, 3:130, 4:161), exactly as expected; every other flag class 0. Arabic total 639,899 confirmed by the census as well.

## Hash chain

| State | sha256 | Bytes |
|-------|--------|-------|
| Source anchor (staging, untouched throughout) | `2030fe97…` | — |
| v1 (first application, frozen) | `368835ad…` | 2,135,954 |
| v2 (quarantine clearance, frozen as `…-PATCHED-v2.md`) | `11b3a78a86d0e26c5f22d61e2bcc9ea3bf0ae1bb56e21a76955c069ac7f0691c` | 2,135,551 |
| **v3 (this pass — current working file)** | **`cf1c317bdb95b3e750d87cbb8b7b6805b84bb7cd5058242010880a0c8207b84e`** | **2,135,602** (+51 vs v2) |

**Files touched by this pass:** the working patched file (edited) + the frozen v2 copy and this receipt (created). Nothing else — no staging, no workspace manuscript, no git, no uploads. Propagation remains a separate step on Robert's word.
