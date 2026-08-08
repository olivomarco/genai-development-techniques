# Oracle — History

## Project Context
- **Project:** Comparison of GenAI development techniques
- **Goal:** Research and document frameworks like GSD, BMAD, SPEC-KIT, Squad, Ralph, and other techniques used to run GenAI development at scale
- **Stack:** Markdown documentation, research-heavy
- **User:** Marco Olivo
- **Created:** 2026-04-12

## Learnings

- 2026-06-21: Freshness reviews should flag both stale metrics and overconfident capability claims; tool support and workspace/multi-repo wording need especially careful source grounding.
- 2026-06-21: Approval can stand when summary language remains broad but deep-dive caveats clearly distinguish support breadth from proven runtime parity.
- 2026-08-08: Rejected the August refresh. Verdict in `.squad/research/review-2026-08-08.md`; recommended Neo as revision owner with Trinity supplying GSD Core evidence.
- 2026-08-08: When a project migrates repositories, the danger is not the corrected page but the uncorrected ones. Grep every removed figure and every removed positioning phrase site-wide before approving.
- 2026-08-08: Removing a stale number from ASCII diagrams corrupts fixed-width cells. Always read the rendered block, not just the diff.
- 2026-08-08: A page can be factually correct about a successor project while silently importing the predecessor's unverified feature set. Check carried-forward capability prose, not only versions and metrics.
- 2026-08-08: Partial style conversions (sentence-case headings applied to some sections) create cross-file label drift. Treat half-finished conventions as consistency defects.
- 2026-08-08: Ecosystem-versus-methodology separation held well this pass; the layer map plus explicit "not a Tier 1 technique" statements in README, overview, and nav is a pattern worth reusing.

- 2026-08-08: Approved the August refresh on re-review. All six blockers closed; verdict appended to `.squad/research/review-2026-08-08.md`. Neo owned the revision under Morpheus lockout, with Trinity's `gsd-core-followup-2026-08-08.md` supplying the B4 evidence.
- 2026-08-08: Verify ASCII-art repairs by measuring row lengths in the built HTML after tag-stripping and entity-unescaping. Source-line byte counts lie when the art contains box-drawing characters.
- 2026-08-08: A rejection that names one line invites a one-line fix. Naming the grep instead ("no surviving instance of X site-wide") is what caught the duplicate anecdote in a file outside the enumerated blockers.
- 2026-08-08: The best resolution to an unverifiable metric is usually a different, smaller, genuinely sourced metric — here, two runtime dependencies replacing a wrong file count. Prefer that over hedging the original figure.
- 2026-08-08: Scoped re-reviews work. Declaring in advance which gates would not be reopened kept this pass to targeted greps, two file reads, and one build, with no re-litigation.

### 2026-08-08: August refresh orchestration
- Oracle performed the strict review, issued the rejection, and later re-reviewed Neo's revision; closed B1–B6 and approved the refresh. Emphasized rendered verification (HTML measurement) and targeted greps as verification techniques.
