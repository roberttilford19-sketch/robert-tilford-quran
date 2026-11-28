# Komi-Permyak (koi) Quran draft — REMEDIATION RECORD (2026-11-28)

Remediation of the independent checker's FAIL verdict
(CHECKER-REPORT-INDEPENDENT-2026-11-28.md), applied under the
standing gate law, most serious first, in the checker's §10
order. This crew built none of the original text. Every fix
was made in the engine's source and the whole book rebuilt
from it — no output file was hand-patched. **STOP state:
nothing landed, shelved, committed, or pushed. The lane
awaits a fresh independent re-check PASS.**

## 1. The Zyrian plurals re-seated in Permyak shape (checker §7, §10.1)

Fault: эскісьяс "believers/disbelievers" (272 tokens, 250
seats) and вӧчісьяс in "wrongdoers" (67 tokens, 66 seats) —
339 tokens in 313 seats — carried the Komi-Zyrian plural
suffix -яс, against BUILD-SPEC's own Permyak plural rule
(stem-final consonant doubled + -эз). Provenance: the PHRASES
table in work/dict_core_koi.py, copied from the Zyrian lane's
phrase table with і substituted.

Fix, in source: work/dict_core_koi.py PHRASES (formerly lines
261–263) now seats, with the replacement forms disclosed
exactly:

- ("believers", "Эскісьяс") → **Эскісььэз**
- ("disbelievers", "Оз эскісьяс") → **Оз эскісььэз**
- ("wrongdoers", "Лёк вӧчісьяс") → **Лёк вӧчісььэз**

Replacement shape: the book's own attested Permyak agent
plural — stem-final consonant сь doubled + -эз, exactly as in
ыстісььэз "messengers" (3:184) and адззылісььэз "witnesses"
(2:282), per the checker's §10.1 prescription. The singular
phrase seats (Оз эскісь, Лёк вӧчісь) are unchanged.

Rebuilt result, recomputed at this desk: эскісььэз 272 tokens
in 250 seats; вӧчісььэз 67 tokens in 66 seats; union 313
seats — seat-for-seat the checker's §7 list, including the
three seats carrying both tokens (2:254, 17:82, 34:31, each
verified to carry both new forms). **-яс plural tokens in
the rebuilt book: 0** (no token ending in -яс anywhere in
the store, the built text, or the manuscript).

## 2. Seat 1:7's final clause (checker §8, §10.3)

Fault, confirmed by the checker: the final clause of 1:7
("nor of those who are misguided") seated the guide verb —
"ни эна кин лоӧ нуӧтӧ", "nor those who are guided", the
opposite sense. Route: the engine's inflection matching
stripped the prefix mis- from "misguided" and seated "guide"
(нуӧтны).

Fix, in source: a direct OVERRIDE entry in
work/dict_core_koi.py — "misguided": ("вошны", "V") — seating
the token on the glossary's own astray seat вошны, whose
present form is вошӧ (the same seat the book already uses
for "astray", e.g. 2:26 "олӧ вошӧ"). The direct dictionary
seat takes precedence over the prefix-stripping route, so
the fault cannot recur through that route for this token.

Rebuilt 1:7: «Туй эна тэ кутӧ ⟦GAP: blessed⟧, оз эна паныт
кинӧ ло ⟦GAP: anger⟧, ни эна кин лоӧ вошӧ.» — final clause
"ни эна кин лоӧ вошӧ", "nor those who go astray". The same
direct seat corrects every other seat carrying the exact
token "misguided" (7 seats in all): 1:7, 16:25, 18:104,
26:86, 27:41, 36:47, 56:51 — each now reads вошӧ where it
previously read нуӧтӧ. No other token's seat changed by
this item; "misguide/misguides/misguidance" verb forms were
not in the checker's finding and were left as built, for
the re-checker to sample.

## 3. Alms standing-family reconciliation (checker §3, §10.3)

Discrepancy: the attestation audit named alms (technical
term) as a standing GAP family with no exception noted, yet
the generic alms seat rides the attested корӧм at every
generic seat (2:110 "сетӧ корӧм"; 5:12 "мед корӧм"), as the
generic scripture seat rides гижӧт under the exception the
audit's list did note. No text seat was wrong; the list was.

Reconciliation, all dated 2026-11-28: (a) an addendum to
ATTESTATION-AUDIT-2026-11-28.md stating the reconciled
rule — alms as a technical term (zakat) is a standing GAP
family; the generic alms/charity seat rides корӧм, whose
giella-koi dictionary gloss includes "милостыня, подаяние"
(alms, almsgiving); (b) BUILD-SPEC's GAP policy clarified
in place with the same generic-seat exception, dated;
(c) the glossary's core section (work/make_glossary.py,
regenerated) now carries an explicit "alms / charity
(generic) — корӧм" entry with the ground stated. No seat
changed.

## 4. Record correction and the verify.py screen (checker §6, §10.2)

Closed records were corrected by dated addendum, never
silently rewritten:

- ATTESTATION-AUDIT-2026-11-28.md — addendum naming the
  phrase-table residue and its repair, correcting the
  "Zyrian plural shapes removed" claim (войтыр's removal
  and the irregular-plural table's replacement stand as
  originally stated; the phrase table was the missed
  route), and carrying the alms reconciliation in §3 above.
- BUILD-REPORT-KOI-2026-11-28.md — addendum in the same
  terms, with the post-remediation figures.
- FLAGS-AND-GAPS-DISCLOSURE-KOI-2026-11-28.md — addendum
  correcting its repeated removal sentence, the confirmed
  1:7 item, and the alms list entry.

verify.py tightened, in source: the single-letter endings
"а", "я", "м", "д", "с", "н" are removed from the ENDINGS
decomposition list, and traces() now rejects any
non-inventory token ending in -яс outright (the Zyrian
nominal plural; the Permyak plural is -эз/-ез). The old
decomposition absorbed -яс letter by letter (эскісьяс →
эскісья → эскісь, a seated stem), which is why the original
screen reported 0 untraced over a text carrying 339 such
tokens. Demonstration, run at this desk before the rebuild:
**the tightened screen on the unrepaired text returns
exactly two untraced candidates — эскісьяс ×272 and
вӧчісьяс ×67** — and no others. On the repaired text it
returns 0 (see §5).

## 5. Rebuild and machine verification of the whole book

Rebuild chain, all from source: work/build_engine.py →
verses-store.json (dict seats 1,318, dropped unverified 0);
build.py → quran-koi.txt and quran-koi.json; assemble.py →
ayah-companion-manuscript-KOI.md; work/make_glossary.py →
glossary.md. Figures below were recomputed by the tightened
verify.py and independently at this desk with separate
counts:

- Verses **6,236 / 6,236**; store seat-set exactly equal to
  the Master seat-set; per-surah grid exact, mismatches
  NONE; empty seats NONE; "redacted" NONE. quran-koi.json,
  flattened, equals the store seat for seat.
- Basmalah: 1:1 equals the fixed form «Енлӧн нимӧн,
  Милӧсьта, Милӧсьта.» exactly; 1:3 equals «Милӧсьта,
  Милӧсьта.» exactly, per spec; **113** occurrences in
  quran-koi.txt (112 unnumbered + 1:1; surah 9 none).
- GAP census, recomputed: **5,444 GAP seats, 16,840 GAP
  markers, 4,728 distinct GAP terms, 792 verses without a
  marker** — all unchanged from the pre-remediation census
  (no remediation item added or removed a marker). The
  manuscript carries 16,841 markers, the one extra being
  its front-matter explanatory example, as before.
- Script purity: retained Latin, whitespace tokens with GAP
  interiors excluded, against the explicit allowlist —
  allowlisted 129 types / 1,056 tokens; **non-allowlist
  retained Latin 0 types / 0 tokens**. Mixed-script tokens:
  **exactly the 6 disclosed** name + -лӧн genitive tokens
  (Adamлӧн 5:27; Pharaohлӧн 7:127, 40:28, 40:37; Abrahamлӧн
  11:74; Josephлӧн 12:58); other mixed tokens NONE.
- Cyrillic attestation (tightened screen): **841 distinct
  Cyrillic tokens, 0 untraced candidates**; tokens
  containing ӧ 369 types, containing і 35 types. Counts are
  unchanged from before remediation — the two -яс types are
  replaced one-for-one by the two -ьэз types, which trace
  by the doubled-consonant plural rule to the seated stems
  эскісь and вӧчісь.
- **-яс plural tokens: 0** in store, text, and manuscript.
- Seated dictionary: **1,318 entries** (was 1,317; +1 for
  the direct "misguided" seat in §2); dropped as
  unverified: 0.

## 6. Stop state

Nothing was landed, shelved, committed, or pushed in this
pass; there is no koi folder on the GitHub shelf
(~/workspace/robert-tilford-quran/translations/ holds no
koi entry, verified at this desk). The book's face still
says DRAFT — NOT PUBLISHED. The lane awaits a fresh
independent re-check PASS before any landing, exactly as
its disclosure states.
