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

