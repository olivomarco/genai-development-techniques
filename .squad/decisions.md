# Squad Decisions

## Active Decisions

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
