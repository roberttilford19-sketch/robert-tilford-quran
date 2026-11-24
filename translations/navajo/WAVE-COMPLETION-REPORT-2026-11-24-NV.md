# Navajo Completion Wave — Report, 2026-11-24

*Run under Robert Tilford's standing three-lane completion order of 2026-11-18: Navajo,
Western Apache, and Lakota are to be worked all the way to completion, toolkits and
concordances included, under the rulings already given, with no decision point returned
to him unless genuinely new. Western Apache landed on 2026-11-22 and Lakota's completion
wave landed the same day; this wave closes the Navajo lane on the same pattern. The Quiet
Protocol stood throughout — no outreach of any kind was made. The manuscript's verse text
was not edited by the wave; its MD5 is 408b7bb97269c65ce2e85d39dc886e6a, byte-identical
before and after.*

## What was unfinished when the wave went out

The manuscript and its full concordance already stood on the shelf (landed 2026-11-18 on
Robert's push ruling), and the concordance's own builder's note stated the position
plainly: of the manuscript's 10,443 distinct word forms (64,894 tokens in 6,236 verses),
only 191 forms carried a receipt, and every one of those receipts rested on the lane's
own records — the locked terminology table and the glossary — with no published citation
behind any individual word. The remaining 10,252 forms, carrying 35,195 occurrences,
stood unreceipted, and the lane's flags file held 4,459 verse-level bullets whose
attestation questions no published source had yet been asked. The grounding loop that
Lakota's wave had closed — published receipts, a gaps register, an adjudicated flags
layer, an independent check — had never been run for Navajo.

## What the wave did

The wave first assembled every openly published Navajo source that could be
machine-read: Wiktionary's Navajo entries as extracted by Kaikki.org (25,894 entries,
25,538 distinct headwords, 28,966 listed forms), and Young & Morgan's *The Navaho
Language* (first edition, 1943, a publication of the Education Division of the U.S.
Office of Indian Affairs), whose Navaho–English vocabulary stands openly readable on
the Internet Archive. The Franciscan Fathers' *Ethnologic Dictionary* (1910) and
*Vocabulary of the Navaho Language* (1912) were also acquired and are held in the wave
folder; no receipt in this wave claims them — their pre-Young-&-Morgan orthography,
compounded by the state of the archive OCR, did not yield headword matches a checker
could walk back at the wave's standard, and the wave says so rather than borrow their
authority.

One standard governed every receipt, Robert's dictionary fair-use law: take the fact
only — the word and its meaning — state every gloss as a short equivalent in the desk's
own words, and cite the source so any checker can walk the word back. A form standing
in a published entry — as headword or listed form, exactly, with tone marking
normalised, or as a hyphenated bound form as postpositions and stems are listed —
earned a Basis A receipt. A regular derivation of an attested form — a possessive or
person prefix, a nominalising or subordinating suffix, an interrogative suffix, a
postpositional suffix on an attested base, an unwritten final glottal stop, or a
diacritic-free skeleton match that cannot distinguish tone or nasalisation — earned
Basis B with the rule named in the receipt. Two guards were absolute. A form bearing
Arabic transliteration marks, or standing in the transliteration wordlist, was never
receipted from a Navajo dictionary at all: the draft's Arabic is transliteration by
design, and a coincidental collision with a Navajo entry is not attestation. And no
Navajo form was invented at any point in the wave.

## The first check failed, and the wave was repaired

The first independent checker passed the wave's counts, disjointness, manuscript
integrity, and spot token counts exactly — and failed it on receipt quality. Four of
forty sampled receipts rested on wrapped English gloss lines in the 1943 OCR that the
extractor had mistaken for headwords, and ten sampled receipts carried the source's
gloss wording verbatim, truncated mid-phrase. The wave was rebuilt on the record:
the 1943 headword set was re-extracted behind an English stoplist built from the
book's own English–Navaho part and a Navaho-orthography signal requirement, which
cut it from 6,201 candidate keys to 948 and left exactly two Young & Morgan receipts
standing, both verified by the second checker at the line; the Arabic guard above was
added; and every gloss was re-stated as the shortest equivalent clause in the desk's
own words. The second independent checker, who had done none of the grounding, then
ran six checks and passed the lane on all six: counts recomputed exactly, receipts
and gaps disjoint and complete, manuscript integrity confirmed by hash on both
copies, the Arabic guard verified across all 495 receipts, both 1943 receipts
verified in place, and a fresh sample of forty receipts — twenty-eight Basis A,
twelve Basis B — verified one by one against the cited sources, forty passed, none
failed, with no gloss in the whole build longer than six words. Both check reports
stand in the wave folder.

## The counted result

The wave wrote 495 new published-citation receipts — 342 on Basis A and 153 on
Basis B — covering 12,048 occurrences. With the lane's own 191 receipts, 686 of the
manuscript's 10,443 distinct forms now carry a receipt, and those receipts cover
41,747 of its 64,894 occurrences (64.3 percent of the text as read). Every one of
the 495 wave receipts carries a published citation a checker can follow. The
manuscript's remaining 9,757 forms were each examined and stand in the pack's gaps
register with the reason recorded: 3,826 are Arabic transliterations or proper
names — outside the Navajo dictionary record by design, the draft's locked
transliteration standing in for Navajo vocabulary — and 5,931 found no attestation
in the openly published record searched, the great mass of them inflected verb
forms, which no published Navajo dictionary lists one by one. No form was removed
or replaced: the gaps stand in the concordance and the register as
examined-and-unattested — disclosed gaps, not hidden ones. Turning the
transliteration mass and the unattested inflections into attested Navajo would be
re-translation, and the wave was not commissioned to re-translate; it is named
here as the largest piece of work that remains, and it is Robert's to commission.

## The flags

All 4,459 flag bullets in FLAGS-NV.md's standard verse-level format were adjudicated
against the finished grounding record in a dated layer
(FLAGS-ADJUDICATION-2026-11-24-NV.md) that leaves FLAGS-NV.md itself untouched:
1,155 bullets are settled on attestation — every form in the line they quote now
carries a receipt; 2,485 are partly settled; 814 are confirmed the other way, their
forms standing ungrounded as the flags suspected; 5 name no checkable form. The
adjudication answers attestation only. The bullets' semantic, fidelity, and fluency
judgements stay open exactly as written, and nothing in the layer is framed as
awaiting native review: under Robert's ruling of 2026-11-18 the desk's verification
against published sources is the standard.

## The sweep position, stated plainly

The Purple measure (`purple_measure.py`) runs on lanes built by the newer pipeline
and requires per-lane build inputs — `work/meta.json`, frontmatter and titles
files — that this lane, built on 2026-09-24 by the earlier companion pipeline,
does not have; no Purple sweep could be run on it, and none is claimed. The
reconciled sweeps of record for this lane are the Black fix sweep of 2026-11-18
(independent checker PASS, in the shelf's git history), the lane's structural
verification of record (VERIFICATION-NV.md: 114 surahs, 6,236 verses, every Arabic
line byte-identical to the master), and this wave's two independent checks, the
second passing on all six axes after the first's failures were repaired in the
open.

## The landing

The landing pack stands assembled in the wave's folder: the manuscript
byte-identical, the glossary unchanged, the rebuilt concordance carrying the
finished counts and an honest status — every form the openly published record
attests now carries its citation, and every form it does not attest is listed as
a disclosed gap — the gaps register, the flags adjudication, and this report.
The loop the commission specified is complete: inventory verified, grounding
carried to the limit of the openly published record, flags adjudicated as far as
sources allow, concordance rebuilt and reconciled by count, and an independent
check passed on every axis. On that basis the lane is landed under the Pipeline
Landing Authorization, as a completed, desk-verified draft whose gaps and open
judgements are disclosed in the pack itself rather than smoothed over.
