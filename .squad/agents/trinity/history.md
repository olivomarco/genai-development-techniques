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

### 2026-06-21: Freshness Pass — Rapid Post-April Movement
- Most documented projects advanced since April: GSD v1.42.3, BMAD v6.8.0, Spec Kit v0.11.3, OpenSpec v1.4.1, Squad v0.10.0, Superpowers v6.0.3, ralph-orchestrator v2.9.3.
- Big adoption changes: Superpowers ~234K★, Spec Kit ~114K★, GSD ~64K★, OpenSpec ~56K★, BMAD ~49K★; update star chart/README/deep dives.
- Squad v0.10.0 added state backends, governed memory, import/export, built-in RAI reviewer, MCP/frontmatter work, and broader Copilot CLI skill scanning; still Copilot-centric.
- BMAD v6.8.0 added `bmad-spec`, `bmad-ux`, Web Bundles for Gemini Gems/ChatGPT Custom GPTs, and alpha UI/dashboard work.
- Additional projects to consider: OpenHands, Open SWE, Goose, and Cline are strongest “must consider” adjacent candidates; Aider/OpenCode/Continue/Kilo/Pythagora are maybe/substrate candidates; Roo Code needs rebrand/archive follow-up.


### 2026-08-08: August Market/Freshness Pass — Skills Ecosystem
- **CRITICAL: GSD repo `gsd-build/get-shit-done` is ARCHIVED.** Moved to `open-gsd/gsd-core` (MIT, v1.10.0, npm `@opengsd/gsd-core`, ~7.9K★). Workflow changed 6-step → 5-step (Discuss→Plan→Execute→Verify→Ship). Star drop 64.7K→7.9K is migration, NOT decline — always footnote this.
- **Agent Skills is now a real spec.** `agentskills.io` + `agentskills/agentskills` (Apache-2.0, ~24K★) is vendor-neutral, NOT under `anthropics/`. Anthropic's own repo defers to it. This falsifies our "no standardization emerged" context-engineering claim for the skills layer (still true for rules files).
- **Key nuance for all future skills claims:** format convergence ≠ runtime parity. skills CLI matrix: basic skills 18/18 agents, `allowed-tools` 16/18, hooks 4/18, `context: fork` 1/18 (Claude Code only). Never infer parity from an install-target list.
- `.agents/skills/` is the emerging vendor-neutral install path — confirmed independently by vercel-labs/skills CLI and OpenSpec v1.8.0's `agents` target.
- **skills.sh = `vercel-labs/skills`** (Vercel-operated, MIT, ~28K★, npm `skills` v1.5.22, ~70 agent targets). It is installer + registry + leaderboard + portability layer, but NOT the standard. Uncurated by default (telemetry auto-lists skills); telemetry is opt-OUT.
- **mattpocock/skills = ecosystem, not methodology.** ~210K★ in 6 months but only 3 contributors. 14.4M installs via skills.sh. README explicitly attacks GSD/BMAD/Spec-Kit for "owning the process." Discrepancy: 35 SKILL.md in repo vs 51 listed on skills.sh — unresolved.
- **Best framing found:** Superpowers vs mattpocock/skills are opposing philosophies on the SAME SKILL.md primitive — enforce vs adapt. Better than any metric comparison.
- **Stars are now a broken ranking signal** in this market (Superpowers 269K, mattpocock 210K, anthropics 167K, Spec Kit 126K). Prefer install counts, release cadence, contributor counts.
- **Security gap is the segment's clearest weakness:** no signing, no attestation, no lockfile pinning anywhere; `allowed-tools` is Experimental; skills bundle executable scripts. skills.sh audits (Gen/Socket/Snyk) have partial coverage and Med Risk verdicts on top skills.
- Two watchlist repos silently relocated: `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`; `block/goose` → `aaif-goose/goose`.
- OpenSkills (`numman-ali/openskills`) is DEAD for our purposes — no push since 2026-01-18, superseded, ambiguous name (4+ projects share it), license metadata inconsistent.
- **HVE counts were all wrong:** repo `main` now has 70 agents / 80 instructions / 67 prompts / 58 SKILL.md (docs said 49/102/63/11). Skills jumped 11→58 — Microsoft is repackaging HVE onto the skills primitive. Latest STABLE is still v3.2.2 (Mar 2026); prereleases run to v3.3.101.
- Other version moves: Superpowers v6.2.0 (SDD workspace is now plan-scoped `.superpowers/sdd/<plan-basename>/` — old path claim wrong), Spec Kit v0.16.1, OpenSpec v1.8.0, BMAD v6.10.0 (`bmad-automator` DEPRECATED → `bmad-loop`), Squad v0.11.0 (`cast` replaces `hire`).
- Open SWE has ZERO releases and ZERO tags despite ~10.5K★ — useful maturity tell.
- **Method note:** GitHub API `full_name` reveals silent org renames when you request the old path. Cheap way to catch relocations — worth doing every freshness pass.

### 2026-08-08: GSD Core capability follow-up (Oracle B4)
- Full report: `.squad/research/gsd-core-followup-2026-08-08.md`. Primary sources: local clone of `open-gsd/gsd-core` at `main` SHA `b9f5183` + tag `v1.10.0` (`68a04cc`), plus the published npm tarball.
- **Main ≈ v1.10.0 for all docs cited.** Only `docs/COMMANDS.md` differs (3 unrelated paragraphs). Don't assume main/stable drift without diffing — here it was nil.
- **VERIFIED as current:** wave-based parallel execution; XML plan/prompt formatting (`docs/FEATURES.md:305` REQ-PLAN-03); `/gsd-quick`; brownfield onboarding (`/gsd-onboard`, ADR-1990, named module + tests — the strongest-evidenced item); `/gsd-workstreams` (ADR-0004); `/gsd-workspace`; `overview.md` "waves for parallelism".
- **DISPROVED — "5+ agents simultaneously."** Documented default is `max_concurrent_agents: 3` (`docs/CONFIGURATION.md:839` AND the archived repo's own v1.42.3 CONFIGURATION.md:523). The "5+" figure exists in NEITHER repo at any inspected tag — it is downstream embellishment, not archived-era fact. Only "five agents" hit is a *cost warning*.
- **DISPROVED — "~50 Markdown files and a CLI helper."** npm tarball: 879 files, 486 .md, 337 JS, ~11.2 MB, FOUR declared binaries. Off by ~10x. The defensible replacement claim is **two runtime dependencies** (`@anthropic-ai/claude-agent-sdk`, `ws`).
- **NOT VERIFIED — iOS-to-Android / 90+ sessions / 23 plans.** Zero hits in gsd-core main, its 567 KB CHANGELOG, or archived READMEs at v1.0.0/v1.10.0/v1.20.0/v1.42.3. Recommend deletion. NOTE: the anecdote is ALSO at `techniques/choosing-your-approach.md:240` — outside B4's line list, so it will survive the fix unless flagged.
- **Claude-native sub-agent spawning is now WRONG as a mechanism claim.** GSD Core has a 20-host `docs/reference/host-integration-capability-matrix.md` with per-axis cited evidence and 44 `capabilities/` descriptors; dispatch is negotiated, not hardcoded (ADR-1239: "no `runtime===` branch in the scheduler"). Claude Code is still deepest (only `dispatch.isolation: harness-worktree`; sole runtime dep is the Claude Agent SDK).
- **Best new sourced limitation for our pages: parallelism is not portable.** Copilot forces sequential inline execution regardless of the `parallelization` setting (`gsd-core/workflows/execute-phase.md:23-26,157-159`), and backgrounded Claude Code agents lose wave parallelism entirely (#853, ADR-1143:30). Stronger than the vague "runtime parity not verified" hedge.
- ADR-1143 (Claude Workflow-tool backend) is still `[Proposed]` and unratified even though the capability shipped — good reminder that shipped ≠ ratified in this repo.
- **Method that paid off:** clone + `npm pack`/registry `fileCount` beats reading marketing prose for any "footprint" claim; and checking the ARCHIVED repo at an old tag is how you tell "archived-era fact" from "never true anywhere."

### 2026-08-08: August refresh orchestration
- Trinity supplied the GSD Core verification ledger and primary-source snapshots used by Neo to close Oracle's B4 blocker. Trinity's market findings shaped the Skills ecosystem framing and the nine candidate dispositions.
