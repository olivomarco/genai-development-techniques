# Trinity — History

## Project Context
- **Project:** Comparison of GenAI development techniques
- **Goal:** Research and document frameworks like GSD, BMAD, SPEC-KIT, Squad, Ralph, and other techniques used to run GenAI development at scale
- **Stack:** Markdown documentation, research-heavy
- **User:** Marco Olivo
- **Created:** 2026-04-12

## Learnings

### 2026-04-12: Initial Research Sweep
- **Researched 15 techniques/frameworks** across the GenAI development landscape
- **Top frameworks by GitHub stars:** GSD (~51K), BMAD (~44K) — both are dominant in spec-driven development
- **Key finding:** The entire space has converged on "spec-driven development" (SDD) as the paradigm — write specs before code
- **Context engineering** has replaced "prompt engineering" as the core skill (Andrej Karpathy, June 2025)
- **Ralph is NOT a separate framework** — it's a built-in component of Squad (the "Work Monitor" agent)
- **Spec Kit** is GitHub's official SDD toolkit (v0.6.0), agent-agnostic, with a growing community extensions catalog
- **Squad** (by Brady Gaster at MSFT) is unique as an agent *orchestration* system — it creates a team of named AI agents, not just a workflow
- **Kiro** is AWS's standalone IDE for SDD — not a framework, it's a whole product
- **Tessl** is in closed beta but has a fascinating spec registry (10K+ library specs) — could be the "NPM for AI knowledge"
- **Additional techniques discovered:** Cline, Roo Code, Aider, Continue, OpenCode, Cursor Rules, CLAUDE.md memory system, copilot-instructions.md
- **Key sources:** GitHub repos, GitHub Blog, Martin Fowler (martinfowler.com), codecentric.de, dev.to, thomy.tech, multiple LinkedIn posts
- **Important distinction:** Tools vs. Methodologies vs. Platforms — these are different categories but often compared as if equivalent
- **The complexity spectrum runs:** Raw prompting → .cursorrules → GSD → Spec Kit → Squad → BMAD → Kiro

### 2026-04-12: Deep Dive — Ralph Loop & HVE
- **Ralph IS a standalone technique** — correction from initial research. Created by Geoffrey Huntley (ghuntley.com/ralph/), NOT by Brady Gaster/Squad
- Ralph's core: `while :; do cat PROMPT.md | claude-code ; done` — a bash loop running AI coding agents iteratively
- Named after Ralph Wiggum from The Simpsons — "perpetually confused, never stops"
- Squad's "Ralph" work monitor agent is INSPIRED BY the Ralph Wiggum technique but is a different implementation
- Ralph has its own ecosystem: official Claude Code plugin, community forks (ralph-claude-code 364★, ralph-orchestrator), MCP Market skill
- Geoffrey Huntley used Ralph to build "CURSED" — an entire programming language with LLVM compiler over 3 months
- Key differentiator: Ralph is TOOL-AGNOSTIC — works with any AI coding CLI, not just Claude
- Matt Pocock (TypeScript educator) is a prominent advocate
- **HVE (Hypervelocity Engineering)** is Microsoft's methodology — much more than a technique
- HVE created by Microsoft ISE team, championed by Robin Cole (VP Engineering)
- GitHub repo: microsoft/hve-core — 919★, 141 forks, 54 contributors, MIT license
- HVE's core workflow: RPI (Research → Plan → Implement → Review) with 4 specialized agents
- Massive scope: 49 agents, 102 instructions, 63 prompts, 11 skills in the hve-core package
- Has a VS Code extension and is on Microsoft Learn (HVE Accelerators Hub)
- Enterprise-focused: governance, constraint-based workflows, validated artifacts, audit trails
- Tightly coupled to GitHub Copilot ecosystem (unlike tool-agnostic Ralph)
- Key distinction: Ralph = autonomous loop (AFK coding), HVE = structured phased workflow with governance
- Both solve "how to use AI for software development at scale" but from opposite philosophies: Ralph trusts iteration, HVE trusts structure

