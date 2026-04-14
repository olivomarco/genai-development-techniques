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
- **Additional techniques discovered:** Cline, Roo Code, Aider, Continue, OpenCode, Cursor Rules, copilot-instructions.md, CLAUDE.md memory system
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

### 2026-04-14: Community Ports & Adaptations Research
- **GSD:** rmindel/gsd-for-cursor (76★, 15 forks) is the primary community port. GSD also officially added --opencode, --codex, Gemini CLI support. A Copilot port exists as personal forks via Kilo Code bridge but no standalone repo. itsjwill/gsd-pro (66★) adds multi-model routing.
- **BMAD:** No community ports needed — V6 went officially multi-platform (Claude Code, Cursor, Windsurf, Copilot, Roo Code). Has MCP Server for cross-platform use.
- **Squad:** ZERO community ports. Entirely Copilot-locked. No unofficial adaptations found.
- **HVE:** ZERO community ports. Entirely Copilot-locked. Enterprise governance model makes porting difficult.
- **Spec Kit:** Agent-agnostic by design. Community extension catalog infrastructure exists. Fatima367/spec-kit-github-issues is the first community extension (1★, Apr 2026). Integration catalog system proposed (Issue #2066).
- **Ralph:** Thriving ecosystem. mikeyobrien/ralph-orchestrator (2.7K★, 246 forks, v2.9.2) is a major community tool — Rust-based, multi-backend (Claude, Roo, Copilot, Pi), web dashboard, MCP server. ghuntley/how-to-ralph-wiggum is at 1.4K★ (NOT 8.7K as previously noted — correction needed).
- **Superpowers:** Most active porting activity. dwaintr.superpowers-vscode (2.5K installs on VS Code Marketplace), anothel.superpowers-copilot-agents (389 installs), varunr89/superpowers-copilot (4★), jsloat/superpowers-for-copilot (3★). Official project added Copilot CLI support in v5.0.7.
- **Context Engineering:** Practice, not framework. Denis2054/Context-Engineering-for-Multi-Agent-Systems (555 commits) is the most comprehensive educational resource. No standardization framework has emerged.
- **Key insight:** Copilot-only tools (Squad, HVE) have zero community ports = platform lock-in risk. Tool-agnostic projects (Ralph, Superpowers) attract the most community activity.

### 2026-04-14: Deep Dive — OpenSpec (Fission AI)
- **OpenSpec** is a lightweight, open-source spec-driven development (SDD) framework by Fission AI (YC W26), created by Tabish Bidiwale (@TabishB / @0xTab on X)
- **GitHub:** github.com/Fission-AI/OpenSpec — 39.9K★, 2.7K forks, 59 contributors, MIT license, v1.3.0 (35 releases), TypeScript 98.9%, ~8 months old
- **Core concept:** "Version control for intent" — proposal-first workflow with delta specs (ADDED/MODIFIED/REMOVED markers) tracking changes against existing functionality
- **Three-phase state machine:** Propose → Apply → Archive. No code generation until human reviews and approves the proposal
- **Key philosophy:** "fluid not rigid, iterative not waterfall, easy not complex, brownfield-first"
- **Tool support:** 27+ AI coding tools — the WIDEST of any framework. Claude Code, Cursor, Copilot, Codex, Amazon Q, Gemini CLI, Windsurf, Cline, Continue, RooCode, Kilo Code, Kiro, OpenCode, Junie, IBM Bob, and more
- **Setup:** `npm install -g @fission-ai/openspec@latest && openspec init` — minutes, no API keys, no MCP
- **Brownfield-first design:** Only framework explicitly designed for modifying existing codebases. Delta markers are unique to OpenSpec
- **Lightweight output:** ~250 lines per spec vs. Spec Kit's ~800 lines — significantly less review overhead
- **Quality gates:** Proposal approval gates, `openspec validate --strict` catches missing scenarios, `/opsx:verify` checks implementation against specs
- **Governance:** Limited — no multi-repo, no SSO/SCIM, no enterprise compliance. Archive system provides audit trail but not enterprise-grade governance
- **Community:** Discord (discord.gg/YctCnvvshC), Slack for teams, GitHub Discussions, YC W26 backing, featured in Augment Code comparison and Better Stack, Cursor community showcase
- **Limitations:** Static specs (don't update during implementation), no multi-agent orchestration, single-repo focus, requires manual archive discipline
- **Category:** Spec-Driven Development — fits squarely alongside GSD and Spec Kit
- **Positioning within SDD:** GSD = structured greenfield, Spec Kit = comprehensive portable, OpenSpec = lightweight brownfield
- **Star ranking in comparison:** 4th highest (39.9K) — after Superpowers (151K), GSD (51K), BMAD (44K)
- **Recommendation:** Strong inclusion candidate. Significant traction (39.9K★), YC-backed, widest tool support, unique brownfield niche

