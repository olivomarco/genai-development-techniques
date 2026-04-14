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

---

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
