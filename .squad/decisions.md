# Squad Decisions

## Active Decisions

### 2026-06-21: Freshness Pass Approved With Taxonomy Unchanged

**Authors:** Neo (Lead), Trinity (Researcher), Morpheus (Writer), Oracle (Reviewer)  
**Status:** Accepted

The June 2026 freshness pass updates public documentation for current versions, adoption metrics, support matrices, and maturity language while preserving the existing methodology-first taxonomy: Spec-Driven Development, Multi-Agent Orchestration, Skill-Based Development, Autonomous Iteration, Enterprise AI-Native SDLC, with Context Engineering as a cross-cutting practice.

**Rationale:** Neo's scope review and Trinity's research found rapid project movement, but no new top-level methodology category that warranted restructuring the comparison. Morpheus refreshed the docs from research, and Oracle approved the final revision after blocker fixes.

**Impact:**
- Keep the documented Tier 1 set at ten approaches.
- Update stale metrics and internal count/spectrum consistency across public docs.
- Surface OpenHands, Open SWE, Goose, Cline, and other adjacent projects as watchlist candidates until transferable methodology fit is proven.
- Keep OpenSpec positioned between Superpowers and Spec Kit in the complexity spectrum.

### 2026-06-21: Capability Claims Must Distinguish Support Breadth From Runtime Parity

**Authors:** Oracle (Reviewer), Neo (Lead)  
**Status:** Accepted

Freshness wording must separate documented support from inferred parity. OpenSpec can be described as having broad 27+ native/pre-baked tool support, but not proven identical feature depth across every runtime. OpenSpec workspace language should stay limited to observed `workspace.yaml` evidence; full team workspace, multi-repo, and monorepo support remain unproven. BMAD Gemini Gems and ChatGPT Custom GPT support should be framed as Web Bundle/planning-bundle support, not full Gemini CLI or Codex-style runtime parity. GSD should be described as Claude Code-centered with meaningful official multi-runtime expansion.

**Rationale:** Oracle rejected the first freshness pass because some wording overstated support parity or made stronger claims than Trinity's research supported. Neo's revision resolved those blockers, and Oracle approved the final pass.

**Impact:**
- Future updates should avoid turning broad support lists into first-class parity claims without direct source evidence.
- Summary pages may stay compact, but technique pages must carry the important caveats.

### 2026-06-21: Freshness Watchlist Before New Tier 1 Deep Dives

**Authors:** Neo (Lead), Trinity (Researcher), Morpheus (Writer)  
**Status:** Accepted

Adjacent projects should be tracked as candidates before being promoted to full technique pages. OpenHands, Open SWE, Goose, and Cline are the strongest current watchlist candidates; Aider, OpenCode, Continue, Kilo Code, Pythagora/GPT Pilot, Roo Code, AutoGPT, SWE-agent, Plandex, and MetaGPT remain possible follow-up research targets depending on methodology signal.

**Rationale:** Popular AI coding products or runtimes should not become Tier 1 entries unless they represent a transferable development methodology rather than only a tool/platform.

**Impact:**
- Add concise watchlist language instead of creating new full deep dives during this pass.
- Require a separate scope decision before promoting any candidate to Tier 1.

### 2026-04-14: README Must Stay in Sync When Adding Techniques

**Authors:** Marco Olivo (via Copilot)  
**Status:** Accepted

When adding a new framework or technique to the comparison, always update `README.md` alongside `overview.md` and the new or changed deep-dive document. The README has its own Deep-Dive Documents table and must not lag behind the main comparison docs.

**Rationale:** The README was missed during the OpenSpec addition, creating cross-document drift.

**Impact:**
- Future technique additions require README, overview, choosing guide, and relevant cross-reference updates to be checked together.

### 2026-04-14: Superpowers Categorized as "Skill-Based Development"

**Authors:** Morpheus (Writer), Neo (Lead)
**Status:** Accepted

Superpowers is categorized as **Skill-Based Development** — a new, fifth category in the taxonomy, distinct from Spec-Driven Development, Multi-Agent Orchestration, Autonomous Iteration, and Enterprise AI-Native SDLC.

**Rationale:** Superpowers doesn't fit cleanly into any existing category. Its defining abstraction is the composable, mandatory skill — a reusable behavioral module that teaches agents *how* to develop (TDD, code review, debugging methodology) rather than *what* to build (specs) or *who does what* (agent roles). Both Morpheus and Neo independently converged on this categorization.

**Impact:**
- Technique count: 8 → 9
- Category count: 4 → 5 (plus Context Engineering as cross-cutting)
- Spectrum position: Between Ralph (less structure) and GSD (more structure)
- Future techniques with similar skill/plugin architectures could be classified under this category

**Open Questions:**
- Whether Superpowers is a mature implementation of Context Engineering vs. its own category
- Whether other skill-based frameworks will emerge to populate this category

### 2026-04-14: OpenSpec Added to Comparison
**Authors:** Trinity (Researcher), Neo (Lead), Morpheus (Writer)
**Status:** Accepted

OpenSpec is a lightweight, open-source spec-driven development framework by Fission AI (YC W26), created by Tabish Bidiwale. It enforces a proposal-first workflow with delta specs — a CLI-based state machine of Propose → Apply → Archive that acts as "version control for intent."

**Key Stats:** 39.9K GitHub stars, 2.7K forks, 59 contributors, MIT license, TypeScript, v1.3.0 (35 releases), 27+ compatible tools (widest in comparison).

**Scoping Decision:** INCLUDE. Meets all Tier 1 inclusion criteria. OpenSpec fills a gap as the only brownfield-first SDD framework in the comparison. Assigned to **Spec-Driven Development** category alongside GSD and Spec Kit, creating a three-way taxonomy:
- **GSD** — task-centric (fresh agents per task, wave parallelism)
- **OpenSpec** — change-centric (change folders, delta specs, fluid iteration)
- **Spec Kit** — project-centric (spec → plan → tasks, phase-gated)

**Spectrum Position:** Between Superpowers and Spec Kit (`Context Eng → Ralph → GSD → Superpowers → OpenSpec → Spec Kit → Squad → BMAD → HVE`).

**Artifacts Created:**
- `techniques/openspec.md` deep-dive created (all 27+ tools listed, four comparison subsections, community ports note)
- `overview.md` updated across comparison matrix, star chart, decision guide, category summary, complexity spectrum, and navigation

**Technique count:** 9 → 10 | **Category count:** 5 (Spec-Driven Development now has 3 techniques)

---

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction

---

# Merged inbox — 2026-08-08

The following decision proposals were merged from `.squad/decisions/inbox/` on 2026-08-08 and consolidated into the Squad Decisions ledger. Duplicates were deduplicated and contextual conflicts resolved per Neo's scope guidance.

## neo-august-refresh-scope.md
**Author:** Neo
**Date:** 2026-08-08
**Status:** Accepted (merged)

Summary: Preserve the five-category, methodology-first taxonomy; add a supporting "Skills ecosystem" page (lead: mattpocock/skills) outside the Tier 1 count; require primary-source traceability, Oracle claim review, and strict MkDocs build before completion. Authorized Morpheus to create `techniques/skills-ecosystem.md` and update specified pages; any Tier 1 promotion requires a new scope decision.

## neo-github-pages-docs.md
**Author:** Neo
**Date:** 2026-06-21
**Status:** Accepted (merged)

Summary: Use MkDocs Material with a staging script to publish Markdown source to GitHub Pages. The build stages public Markdown into `docs-staging/`, builds `site/` with MkDocs, and deploys artifacts. Keep source files in place; do not commit generated artifacts.

## trinity-august-market-findings.md
**Author:** Trinity
**Date:** 2026-08-08
**Status:** Proposed → Merged (research findings incorporated)

Summary: Market evidence for August 8, 2026: Agent Skills formalized (agentskills.io), skills CLI / skills.sh pattern, `mattpocock/skills` as an ecosystem profile (not Tier 1), GSD repository migration to `open-gsd/gsd-core`, security/provenance caveats for skills registries, and candidate dispositions for nine verification targets. Recommendations: treat skill packaging as a layer above rules files, prefer install telemetry / release cadence over raw star counts, and add a standing provenance/security caveat.

---

