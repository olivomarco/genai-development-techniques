# Neo — History

## Project Context
- **Project:** Comparison of GenAI development techniques
- **Goal:** Research and document frameworks like GSD, BMAD, SPEC-KIT, Squad, Ralph, and other techniques used to run GenAI development at scale
- **Stack:** Markdown documentation, research-heavy
- **User:** Marco Olivo
- **Created:** 2026-04-12

## Learnings

### 2026-04-12: Initial Research Scope Completed
- Identified 11 Tier 1 techniques for deep-dive comparison: GSD, BMAD, Spec Kit, Squad, Kiro, Tessl, SPARC, Roo/Boomerang, MetaGPT, Devin, Context Engineering
- GSD has massive traction (49.9k GitHub stars); it's spec-driven + meta-prompting + context engineering
- BMAD has two full names in circulation: "Build More Architect Dreams" (official docs) and "Breakthrough Method for Agile AI-Driven Development" (original). V6 is current. Uses specialized agent roles (Analyst, PM, Architect, Dev, QA)
- Spec Kit is GitHub's official open-source SDD toolkit, works with Copilot/Claude Code/Gemini CLI
- Kiro is AWS's agentic IDE — launched mid-2025, uses spec-driven workflow (user stories → technical design → tasks) + agent hooks
- Tessl is from Snyk founder Guy Podjarny — MCP-native spec-driven dev + spec registry for external deps
- SPARC (Specification, Pseudocode, Architecture, Refinement, Completion) — 5 phases, 17 specialized modes, often paired with Roo Code
- Roo Code's "Boomerang Tasks" = task orchestration to break projects into subtasks with context isolation
- MetaGPT simulates a full software company with SOP-driven agents; philosophy is "Code = SOP(Team)"
- Devin (Cognition AI) was first autonomous AI engineer but had low task-completion rates in early evaluations
- Context Engineering is a cross-cutting practice: 8-layer model from system instructions (CLAUDE.md, .cursorrules, etc.) down to auto-memory
- Key file: research-scope.md at repo root contains the full scope document
- Taxonomy: three categories (Spec-Driven, Multi-Agent Orchestration, Autonomous AI Engineers) + Context Engineering as cross-cutting
- Proposed 12 comparison dimensions including predictability, human control, and quality gates
- Left 4 open questions for Marco: depth vs breadth, audience, hands-on testing, recency cutoff

### 2026-04-12: Scope Revised per Marco's Feedback
- Marco directed: remove Roo Code/Boomerang and Devin from Tier 1, add Ralph (Wiggum) and HVE
- Ralph (Wiggum) is Geoffrey Huntley's autonomous iteration loop — a bash one-liner methodology, tool-agnostic, uses tests as backpressure and git as memory. Distinct from Squad's internal "Ralph" work monitor. Very high community adoption (VentureBeat coverage, official Claude Code plugin, Matt Pocock endorsement)
- HVE (Hypervelocity Engineering) is Microsoft ISE's enterprise AI-native SDLC — RPI workflow (Research → Plan → Implement → Review), 49 agents, 102 instructions, 63 prompts. GitHub Copilot-native. Key people: Robin Cole, Valentina Alto. 919 GitHub stars, MIT license
- Created two new taxonomy categories: "Autonomous Iteration" (Ralph) and "Enterprise AI-Native SDLC" (HVE)
- Added "Governance" as comparison dimension — critical for distinguishing HVE's constraint-based approach
- Moved Roo Code and Devin to Tier 2 with updated rationales (tool vs methodology, platform vs technique)
- Removed open questions section — Marco has given clear direction
- Updated status to APPROVED
- File list updated: `roo-boomerang.md` and `devin.md` removed from techniques/, `ralph.md` and `hve.md` added
- Appended sections 17 (Ralph) and 18 (HVE) to research-raw-findings.md with full research from Trinity

### 2026-04-12: Overview & README Written
- Wrote overview.md — the executive summary and master comparison document
- Contains 6 sections: Executive Summary, Comparison Matrix (13 dimensions × 8 techniques), Decision Guide (10 scenarios), Category Summaries (5 categories), Complexity vs. Speed ASCII spectrum, and Navigation links
- Comparison matrix scored all 8 Tier 1 techniques across: Approach, Human Control, Setup Complexity, Tool Compatibility, Scale, Predictability, Context Management, Quality Gates, Governance, Learning Curve, Ecosystem Maturity, Cost, Open Source
- Decision guide covers 10 practical "if you want X, use Y" scenarios
- MetaGPT had limited dedicated research data (no deep-dive section in raw findings) — scored conservatively from cross-cutting observations and scope document
- Updated README.md as project landing page with technique tables organized by category, links to all deep-dives, and project context
- Key architectural insight: the spectrum runs Context Eng → Ralph → GSD → Spec Kit → Squad → BMAD → HVE from least to most ceremony/structure
- All techniques converge on spec-first thinking and context engineering as foundational practices

### 2026-04-14: Integrated Superpowers across all interlinking docs
- Updated overview.md: exec summary, comparison matrix (now 9 techniques), star history, decision guide, category summaries (now 5 categories), spectrum, navigation
- Updated choosing-your-approach.md: all tables, flowchart, combining techniques, anti-patterns, costs, tool lock-in, summary
- Updated gsd.md and context-engineering.md comparison notes sections
- New "Skill-Based Development" category accepted — Superpowers positioned between Ralph and GSD on the ceremony spectrum
- Morpheus wrote the deep-dive page (`techniques/superpowers.md`) with all 12 template sections

### 2026-04-14: Scribe — Cross-agent update
- Morpheus wrote `techniques/superpowers.md` — full 12-section deep-dive (151K stars, Jesse Vincent, skill-based development)
- "Skill-Based Development" category accepted as fifth taxonomy category in decisions.md

### 2026-04-14: OpenSpec Scoping Decision
- Evaluated openspec.dev (Fission AI, @0xTab/TabishB) for inclusion — **APPROVED**
- OpenSpec: lightweight spec-driven framework, 39.9K GitHub stars, 2.7K forks, MIT license, v1.3.0, 25+ tool support
- Category: **Spec-Driven Development** (alongside GSD and Spec Kit) — no new category needed
- Key differentiator: change-centric workflow (each change gets proposal/specs/design/tasks folder) with spec deltas for reviewing requirement changes, not just code
- Spectrum position: between Superpowers and Spec Kit — more structured than GSD (dedicated CLI, change folders), more fluid than Spec Kit (no rigid phase gates)
- Technique count: 9 → 10. Category count remains 5 + cross-cutting
- Broadest tool compatibility of any spec-driven technique (25+ tools vs GSD's Claude Code primary vs Spec Kit's 4 tools)
- Impact: all interlinking docs need updates (overview.md, choosing-your-approach.md, new techniques/openspec.md, comparison notes in gsd.md, spec-kit.md, context-engineering.md)
- Concerns: Spec-Driven category now has 3 techniques (manageable), team features not yet shipped (Workspaces "coming soon"), potential overlap with Spec Kit needs Trinity to map differences
- Scoping decision filed to .squad/decisions/inbox/neo-openspec-scope.md

### 2026-04-14: Superpowers Integration — Cross-Document Interlinking
- Added Superpowers as the 8th Tier 1 technique, in a new category: **Skill-Based Development**
- Category count: 4 → 5 (Spec-Driven, Multi-Agent Orchestration, Autonomous Iteration, Skill-Based Development, Enterprise AI-Native SDLC) plus Context Engineering as cross-cutting
- Superpowers is the largest by community: 151K GitHub stars, active Discord, Prime Radiant backing
- Key differentiator: composable behavioral skills (not specs, not agent roles, not loops) — skills teach agents *how* to develop (TDD, code review, debugging) rather than *what* to build
- Tool compatibility: multi-tool (Claude Code primary, Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode) — broader than GSD, narrower than Ralph/Context Eng
- Spectrum position: between Ralph and GSD (Minutes setup, moderate structure, semi-autonomous)
- Updated overview.md: executive summary, comparison matrix (added column), star history chart, decision guide, category summaries (new section), ASCII spectrum (added box), navigation (new category)
- Updated choosing-your-approach.md: flowchart, all team size tables, all project type tables, regulated/non-regulated, development activity tables, development methodology tables, combining techniques (2 new combos), anti-patterns, cost considerations, tool lock-in matrix, summary table
- Updated gsd.md comparison notes: vs. Superpowers — both spec-driven with TDD but different mechanisms (slash commands vs composable skills), GSD is Claude Code-only while Superpowers is multi-tool, Superpowers has 3x stars
- Updated context-engineering.md comparison notes: vs. Superpowers — Superpowers is arguably the most sophisticated implementation of context engineering, skills ARE context engineering packaged as behavioral modules
- Filed categorization decision to .squad/decisions/inbox/neo-superpowers-categorization.md
