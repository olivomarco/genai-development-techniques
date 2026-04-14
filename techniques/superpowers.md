# Superpowers

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Superpowers                   |
| Category           | Skill-Based Development       |
| Source              | [obra/superpowers](https://github.com/obra/superpowers) / [blog.fsck.com](https://blog.fsck.com/2025/10/09/superpowers/) |
| Author/Org         | Jesse Vincent (obra) / Prime Radiant |
| License            | MIT                           |
| First Released     | October 2025                  |
| Current Version    | v5.0.7 (April 2026)          |
| Stars / Popularity | ~151,000 stars · 13,100+ forks · 28 contributors |
| Supported Tools    | Claude Code (primary), Cursor, Codex (OpenAI), OpenCode, GitHub Copilot CLI, Gemini CLI — broadly multi-tool |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ⚠️ Community — two VS Code Marketplace extensions (2,568 and 389 installs) bring Superpowers to Copilot Chat |
| GitHub Copilot Coding Agent (github.com) | ❌ Not supported |
| Claude Code | ✅ Primary — built on Claude Code's plugin system |
| Cursor | ✅ Supported — via plugin marketplace (`/add-plugin superpowers`) |
| OpenAI Codex (CLI) | ✅ Supported — via INSTALL.md instructions |
| Windsurf | ❌ Not supported |
| Gemini CLI | ✅ Supported — via gemini extensions system |
| Roo Code | ❌ Not supported |
| OpenCode | ✅ Supported — via INSTALL.md instructions |
| GitHub Copilot CLI | ✅ Supported — via copilot plugin marketplace |

## Overview

Superpowers is a complete software development workflow for coding agents, built on composable "skills" — Markdown-based behavioral instructions that teach AI agents reusable patterns for development tasks like TDD, debugging, planning, and code review. Created by Jesse Vincent (the founder of Keyboardio and co-founder of Best Practical), Superpowers evolved from his daily practice of working with Claude Code, systematizing months of accumulated process knowledge into a self-reinforcing skill system.

The core insight is that AI coding agents aren't unreliable because they lack capability — they're unreliable because they lack discipline. Superpowers addresses this by giving agents mandatory skills that they must search for and follow before performing any task. When combined with persuasion principles (drawn from Robert Cialdini's research, which has been scientifically validated to work on LLMs), these skills enforce systematic, test-driven development even when the AI would otherwise cut corners.

Superpowers describes itself as "an agentic skills framework & software development methodology." It started as a Claude Code plugin in October 2025 and has since expanded to support Cursor, Codex, OpenCode, Copilot CLI, and Gemini CLI. At 151K GitHub stars, it is the largest project in this comparison by a significant margin.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Largest community by far (151K stars, 13K+ forks) | ❌ No built-in team coordination — single-developer workflow |
| ✅ Composable, shareable, forkable skills system | ❌ Skills can become stale without deliberate maintenance |
| ✅ Token-light bootstrap (~2K tokens) with lazy skill loading | ❌ Installing on non-Claude-Code platforms requires manual steps |
| ✅ Broadest multi-tool support (6 tools) of any framework compared | ❌ Mandatory-skills philosophy may conflict with quick ad-hoc tasks |
| ✅ Self-improving — agent learns to create and refine skills | ❌ No enterprise governance, audit trails, or compliance features |
| ✅ Persuasion-tested skills ensure agent compliance under pressure | ❌ Rapid version iteration (v1→v5 in 6 months) may bring breaking changes |

> **In one sentence:** Superpowers is the most popular AI development framework — a skill-based methodology that teaches coding agents disciplined, test-driven behavior through composable Markdown skills that work across six different tools.

## Core Concepts

**Skills as Reusable Behavioral Modules.** Skills are Markdown files with YAML frontmatter (name, description, when_to_use, version, languages) that teach the agent how to perform a specific activity. They're not suggestions — they're mandatory workflows. Example: the TDD skill enforces RED-GREEN-REFACTOR: write a failing test first, watch it fail, write minimal code, watch it pass, commit.

**Bootstrap and Discovery.** On session start, the agent reads a lightweight bootstrap prompt (~2K tokens) that teaches it three things: (1) you have skills, (2) search for skills by running a script, (3) if you have a skill for something, you must use it. Skills are discovered at runtime via a CLI search tool, keeping initial context light while making the full library accessible.

**Subagent-Driven Development.** After brainstorming and planning with the user, Superpowers dispatches tasks one by one to subagents for implementation. Each subagent gets a fresh context, implements a single task, and has its work code-reviewed (two-stage: spec compliance, then code quality) before the next task begins.

**Persuasion-Tested Compliance.** Skills are tested against subagents using realistic pressure scenarios (time pressure, sunk cost, confidence bias) to ensure the agent will actually follow them. This was inspired by Cialdini's persuasion principles, scientifically validated to work on LLMs by a Wharton study.

**Self-Improving Skill System.** The "writing-skills" meta-skill teaches the agent how to create new skills. Users can feed books, documents, or extracted conversation memories to the agent and ask it to "mine for new skills." Skills are pressure-tested (TDD for skills) before being committed.

**Git Worktrees for Parallel Work.** After brainstorming, Superpowers automatically creates a git worktree for the project, enabling parallel tasks on the same repository without clobbering each other.

## How It Works

Superpowers follows a skill-driven workflow where each phase activates a specific skill:

| Phase | Skill Activated | Purpose |
|-------|----------------|---------|
| 1 | `brainstorming` | Refines rough ideas through Socratic questioning, explores alternatives, presents design in digestible sections for validation. Saves design document. |
| 2 | `using-git-worktrees` | Creates isolated workspace on new branch, runs project setup, verifies clean test baseline. |
| 3 | `writing-plans` | Breaks work into bite-sized tasks (2–5 minutes each). Every task has exact file paths, complete code, verification steps. |
| 4 | `subagent-driven-development` / `executing-plans` | Dispatches fresh subagent per task with two-stage review, or executes in batches with human checkpoints. |
| 5 | `test-driven-development` | Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests. |
| 6 | `requesting-code-review` | Reviews against plan, reports issues by severity. Critical issues block progress. |
| 7 | `finishing-a-development-branch` | Verifies tests, offers options (GitHub PR / merge worktree / keep / discard), cleans up worktree. |

Plans are written for "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing" — a deliberately low bar that ensures instructions are precise enough for a subagent with no prior context.

The Skills Library covers five domains:

- **Testing:** `test-driven-development`, testing anti-patterns
- **Debugging:** `systematic-debugging` (4-phase root cause), `root-cause-tracing`, `defense-in-depth`, `condition-based-waiting`, `verification-before-completion`
- **Collaboration:** `brainstorming`, `writing-plans`, `executing-plans`, `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch`, `subagent-driven-development`
- **Problem-Solving:** `collision-zone-thinking`, `meta-pattern-recognition`, `simplification-cascades`, `inversion-exercise`, `when-stuck` dispatch
- **Meta:** `writing-skills`, `using-superpowers`, `testing-skills-with-subagents`, `sharing-skills`, `pulling-updates`

Skills include Graphviz DOT diagrams that Claude can interpret as workflow instructions — a novel representation format for agent behavior.

### Philosophy

The underlying principles are explicit:

- **Test-Driven Development** — write tests first, always
- **Systematic over ad-hoc** — process over guessing
- **Complexity reduction / YAGNI** — simplicity as primary goal
- **Evidence over claims** — verify before declaring success

## Strengths

- **Largest community by far.** 151K GitHub stars and 13.1K+ forks make Superpowers the most popular AI development framework. That scale brings more contributors, more battle-tested skills, and faster iteration.
- **Skills are composable and shareable.** Users can fork, customize, and PR new skills. The skill format (Markdown + YAML frontmatter) is simple enough that anyone can author one.
- **Token-light bootstrap.** The ~2K token bootstrap keeps initial context minimal. Skills are loaded on demand via CLI search, avoiding the context bloat that plagues heavier frameworks.
- **Broadest multi-tool support.** Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode — no other framework in this comparison supports as many tools.
- **Self-improving system.** The agent can mine books, documents, and conversation histories for new skills. The `writing-skills` meta-skill closes the loop: the system teaches itself how to get better.
- **TDD enforcement catches quality issues.** The RED-GREEN-REFACTOR cycle is mandatory, not optional. Code written before tests is deleted. This is stricter than most approaches.
- **Subagent-driven development keeps context fresh.** Each task runs in a fresh subagent context, similar to GSD's approach, preventing context rot across long projects.
- **Persuasion-tested compliance.** Skills are stress-tested against pressure scenarios to ensure the agent follows them even when it would otherwise cut corners.

## Limitations

- **No built-in team coordination.** Superpowers is a single-developer workflow enhancement, not a multi-agent orchestration system. There's no role routing, shared decision ledger, or team ceremony support.
- **Skills can become stale.** The pressure-testing approach helps, but skills require deliberate maintenance. Unmaintained skills may drift as LLM behavior evolves.
- **Manual installation on non-Claude-Code platforms.** Installing on Cursor, Codex, or Gemini CLI requires following INSTALL.md instructions or using platform-specific extension mechanisms — not a one-click setup.
- **Mandatory-skills philosophy adds overhead.** For quick bug fixes or small scripts, the requirement to search for and follow skills before acting may feel heavy-handed.
- **No enterprise governance.** No audit trails, constraint enforcement, policy-as-code, or compliance features. Enterprise environments should consider HVE.
- **Rapid version churn.** v1 to v5 in six months means early adopters may face breaking changes. The skills repo (`obra/superpowers-skills`) was archived in October 2025 as skills moved into the main repo.

## Best For

- **Solo developers who want structured discipline** without enterprise overhead. Superpowers codifies best practices into enforceable skills rather than relying on developer memory.
- **Claude Code power users** who want the most comprehensive development methodology built for their tool.
- **Teams that want to accumulate and share AI agent knowledge** as versioned, testable, Markdown-based skills.
- **Projects that benefit from strict TDD enforcement** — the mandatory RED-GREEN-REFACTOR cycle catches regressions early.
- **Developers using multiple AI tools** who want consistent agent behavior across Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode.

## Not Ideal For

- **Teams needing multi-agent team coordination** — Squad or BMAD provide structured role separation and team dynamics that Superpowers lacks.
- **Enterprise environments requiring formal governance** — HVE offers audit trails, constraint enforcement, and policy-as-code.
- **Quick bug fixes or small scripts** where the skill-driven workflow overhead isn't justified.
- **IDE-only environments without CLI access** — skills bootstrap requires CLI interaction to search and load skills at runtime.

## Community & Ecosystem

Superpowers has the largest community of any AI development framework, with 151K GitHub stars and 13.1K forks. Created by Jesse Vincent (obra), who also founded Keyboardio and Best Practical (makers of Request Tracker). The framework is actively maintained by Jesse and the team at Prime Radiant, with 28 contributors. Community support is available via Discord, and the project has been covered by Simon Willison (simonwillison.net), Hacker News front page, and multiple YouTube tutorials. Jesse also created the claude-memory-extractor tool for mining conversation histories into skills. Sam Schillace (Microsoft) wrote about the related concept of self-improving agents in systems like Microsoft Amplifier.

## Community Ports & Unofficial Adaptations

Superpowers has the most active community porting activity of any technique in this comparison. Two VS Code Marketplace extensions bring Superpowers to GitHub Copilot Chat: **[Superpowers for Copilot Chat](https://marketplace.visualstudio.com/items?itemName=dwaintr.superpowers-vscode)** (2,568 installs) by Kaan Aslan provides a `@superpowers` chat participant with 14 slash commands, and **[Superpowers Copilot Agents](https://marketplace.visualstudio.com/items?itemName=anothel.superpowers-copilot-agents)** (389 installs) converts Superpowers workflow skills into VS Code Copilot agents. On GitHub, **[superpowers-copilot](https://github.com/varunr89/superpowers-copilot)** (4★) offers a multi-platform adaptation with `.copilot`, `.codex`, and `.claude-plugin` directories, while **[superpowers-for-copilot](https://github.com/jsloat/superpowers-for-copilot)** (3★) is a clean fork targeting Copilot CLI specifically.

The official project added Copilot CLI support natively in v5.0.7, closing the gap from the upstream side. Active community demand is evidenced by issues [#217](https://github.com/obra/superpowers/issues/217) and [#764](https://github.com/obra/superpowers/issues/764) on obra/superpowers.

## Comparison Notes

**vs. GSD:** Both enforce spec-driven development with TDD and subagent-based parallel execution. The fundamental difference is architecture: GSD uses slash commands and a Lean Orchestrator within Claude Code's native features; Superpowers uses composable, shareable skills that work across multiple tools. GSD has a more opinionated phase structure (6 steps); Superpowers has more reusable behavioral modules. GSD is Claude Code-native; Superpowers supports Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode. Superpowers has 3× the stars (151K vs. 51K), suggesting broader adoption.

**vs. BMAD:** BMAD simulates a full agile team (PM, Architect, Dev, QA) with structured phases and ceremonies; Superpowers enhances individual developer effectiveness through behavioral skills. BMAD's strength is process simulation — it creates distinct agent personas that challenge decisions; Superpowers' strength is process internalization — the agent doesn't play a role, it acquires abilities. Both support multiple tools. BMAD's 12+ agent personas are heavier than Superpowers' skill-based approach but provide more structured team dynamics.

**vs. Context Engineering:** Superpowers is arguably the most sophisticated implementation of context engineering principles. Skills ARE context engineering — they're Markdown documents that structure what the agent knows and how it behaves. But Superpowers goes further with a complete development workflow, TDD enforcement, subagent management, and a self-improving skill system. Context Engineering is the practice; Superpowers is a fully realized system built on that practice.
