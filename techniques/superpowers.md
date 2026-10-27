# Superpowers

## At a glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Superpowers                   |
| Category           | Skill-Based Development       |
| Source              | [obra/superpowers](https://github.com/obra/superpowers) / [blog.fsck.com](https://blog.fsck.com/2025/10/09/superpowers/) |
| Author/Org         | Jesse Vincent (obra) / Prime Radiant |
| License            | MIT                           |
| First Released     | October 2025                  |
| Current Version    | v7.0.1 (October 2026)        |
| Stars / Popularity | ~306,000 stars (October 27, 2026 snapshot; fork count not independently re-verified this pass) |
| Supported Tools    | Claude Code (primary), plus Antigravity, Cursor, Codex App, Codex CLI, Devin CLI, Factory Droid, Gemini CLI, GitHub Copilot CLI, Grok Build CLI, Kimi Code, OpenCode, Pi, Qwen Code, Hermes Agent, and Muse — broadly multi-tool, with install depth per tool unverified beyond the documented setup steps |

## Compatible coding agents

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

Superpowers is a development workflow built from composable Markdown skills for TDD, debugging, planning, and code review. Jesse Vincent, founder of Keyboardio and co-founder of Best Practical, developed it from his daily work with Claude Code.

Superpowers requires agents to search for and follow relevant skills before acting. Its skills prescribe systematic, test-driven development and use persuasion principles drawn from Robert Cialdini's research. The project tests whether agents follow those instructions under pressure; this is not a guarantee of compliance.

Superpowers describes itself as "an agentic skills framework & software development methodology." It started as a Claude Code plugin in October 2025 and has since expanded its documented install paths to Antigravity, Cursor, Codex (CLI and App), Devin CLI, Factory Droid, Gemini CLI, Copilot CLI, Grok Build CLI, Kimi Code, OpenCode, Pi, Qwen Code, Hermes Agent, and Muse — one of the broadest tool lists of any technique in this comparison. Its large repository audience is a useful awareness signal, but not proof of production outcomes.

## Pros & cons at a glance

| Pros | Cons |
|------|------|
| ✅ Large community and active release cadence | ❌ No built-in team coordination — single-developer workflow |
| ✅ Composable, shareable, forkable skills system | ❌ Skills can become stale without deliberate maintenance |
| ✅ Token-light bootstrap (~2K tokens) with lazy skill loading | ❌ Installing on non-Claude-Code platforms requires manual steps |
| ✅ Broad multi-tool support (15+ documented install targets) for a skills methodology | ❌ Mandatory-skills philosophy may conflict with quick ad-hoc tasks |
| ✅ Agent can create and refine skills | ❌ No enterprise governance, audit trails, or compliance features |
| ✅ Skills tested against pressure scenarios | ❌ Rapid version iteration (v1→v7 in roughly 12 months) may bring breaking changes |

> Superpowers uses mandatory Markdown skills to structure test-driven implementation, debugging, and review.

## Core concepts

**Skills as Reusable Behavioral Modules.** Skills are Markdown files with YAML frontmatter (name, description, when_to_use, version, languages) that teach the agent how to perform a specific activity. They're not suggestions — they're mandatory workflows. Example: the TDD skill enforces RED-GREEN-REFACTOR: write a failing test first, watch it fail, write minimal code, watch it pass, commit.

**Bootstrap and Discovery.** On session start, the agent reads a lightweight bootstrap prompt (~2K tokens) that teaches it three things: (1) you have skills, (2) search for skills by running a script, (3) if you have a skill for something, you must use it. Skills are discovered at runtime via a CLI search tool, keeping initial context light while making the full library accessible.

**Subagent-Driven Development.** After brainstorming and planning with the user, Superpowers dispatches tasks one by one to subagents for implementation. Each subagent gets a fresh context, implements a single task, and has its work code-reviewed (two-stage: spec compliance, then code quality) before the next task begins.

**Persuasion-Tested Compliance.** The project tests skills against subagents under time pressure, sunk-cost pressure, and confidence bias to check whether agents follow them. The approach draws on Cialdini's persuasion principles.

**Skill authoring.** The "writing-skills" meta-skill guides agents in creating skills from books, documents, or conversation memories. Users can ask the agent to "mine for new skills." Skills are pressure-tested before being committed.

**Git Worktrees for Parallel Work.** After brainstorming, Superpowers automatically creates a git worktree for the project, enabling parallel tasks on the same repository without clobbering each other.

**Brainstorming (v7.0.0–v7.0.1).** v7.0.0 rebuilt the skill to clarify the request, restate its understanding, then choose between a quick task, a small chat-agreed change, and a full design document. A fresh subagent reads the design as its future implementer and lists open questions in one round, replacing the earlier spec-review step.

v7.0.1 adjusted the opening questions after users found the defaults formulaic. The skill now examines the project or supplied spec before asking questions. v7.0.0 also added a native Antigravity Marketplace plugin manifest.

## How it works

Superpowers follows a skill-driven workflow where each phase activates a specific skill:

| Phase | Skill Activated | Purpose |
|-------|----------------|---------|
| 1 | `brainstorming` | Clarifies ideas, explores alternatives, presents the design in sections for review, and saves a design document. |
| 2 | `using-git-worktrees` | Creates isolated workspace on new branch, runs project setup, verifies clean test baseline. |
| 3 | `writing-plans` | Breaks work into tasks of 2–5 minutes, each with exact file paths, complete code, and verification steps. |
| 4 | `subagent-driven-development` / `executing-plans` | Dispatches fresh subagent per task with two-stage review, or executes in batches with human checkpoints. |
| 5 | `test-driven-development` | Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests. |
| 6 | `requesting-code-review` | Reviews against plan, reports issues by severity. Critical issues block progress. |
| 7 | `finishing-a-development-branch` | Verifies tests, offers options (GitHub PR / merge worktree / keep / discard), cleans up worktree. |

Plans target a subagent with no prior project context, so each task includes the implementation and verification details it needs.

Version 6.2.0 stores review state in a plan-scoped workspace at `.superpowers/sdd/<plan-basename>/`. The workspace is deleted after the final clean review, and review-fix loops resume the original implementer rather than starting over. Release notes report 25/25 baseline and GREEN evaluation runs; treat these as vendor-reported results, not independent validation.

The Skills Library covers five domains:

- **Testing:** `test-driven-development`, testing anti-patterns
- **Debugging:** `systematic-debugging` (4-phase root cause), `root-cause-tracing`, `defense-in-depth`, `condition-based-waiting`, `verification-before-completion`
- **Collaboration:** `brainstorming`, `writing-plans`, `executing-plans`, `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch`, `subagent-driven-development`
- **Problem-Solving:** `collision-zone-thinking`, `meta-pattern-recognition`, `simplification-cascades`, `inversion-exercise`, `when-stuck` dispatch
- **Meta:** `writing-skills`, `using-superpowers`, `testing-skills-with-subagents`, `sharing-skills`, `pulling-updates`

Skills include Graphviz DOT diagrams that Claude can interpret as workflow instructions.

### Philosophy

The underlying principles are explicit:

- **Test-Driven Development** — write tests first, always
- **Systematic over ad-hoc** — process over guessing
- **Complexity reduction / YAGNI** — simplicity as primary goal
- **Evidence over claims** — verify before declaring success

## Strengths

- **Large community and current releases.** The repository had roughly 306K stars on October 27, 2026, and v7.0.1 shipped in October, continuing the project's steady release cadence.
- **Skills are composable and shareable.** Users can fork, customize, and PR new skills. The skill format (Markdown + YAML frontmatter) is simple enough that anyone can author one.
- **Token-light bootstrap.** The ~2K token bootstrap loads skills on demand via CLI search rather than loading the full library at session start.
- **Broad multi-tool support.** Claude Code remains primary, with documented paths to Antigravity, Cursor, Codex, Copilot CLI, Gemini CLI, Devin CLI, Factory Droid, Grok Build CLI, Kimi Code, OpenCode, Pi, Qwen Code, Hermes Agent, and Muse. OpenSpec and Spec Kit support more named tools overall, but Superpowers' list is now broad for a skill-based methodology.
- **Skill authoring.** The `writing-skills` meta-skill guides the agent in creating skills from books, documents, and conversation histories.
- **TDD enforcement catches quality issues.** The RED-GREEN-REFACTOR cycle is mandatory, not optional. Code written before tests is deleted. This is stricter than most approaches.
- **Fresh task context.** Each task runs in a fresh subagent context, similar to GSD's approach.
- **Pressure testing.** The project tests whether agents follow skills under pressure rather than relying only on the written instructions.

## Limitations

- **No built-in team coordination.** Superpowers is a single-developer workflow enhancement, not a multi-agent orchestration system. There's no role routing, shared decision ledger, or team ceremony support.
- **Skills can become stale.** The pressure-testing approach helps, but skills require deliberate maintenance. Unmaintained skills may drift as LLM behavior evolves.
- **Manual installation on non-Claude-Code platforms.** Installing on Cursor, Codex, or Gemini CLI requires following INSTALL.md instructions or using platform-specific extension mechanisms — not a one-click setup.
- **Mandatory-skills philosophy adds overhead.** For quick bug fixes or small scripts, the requirement to search for and follow skills before acting may feel heavy-handed.
- **No enterprise governance.** No audit trails, constraint enforcement, policy-as-code, or compliance features. Enterprise environments should consider HVE.
- **Rapid version churn.** v1 to v7 in roughly twelve months means early adopters may face breaking changes — brainstorming alone was rebuilt twice (v7.0.0, then retuned in v7.0.1) inside a few weeks. The skills repo (`obra/superpowers-skills`) was archived in October 2025 as skills moved into the main repo.

## Best for

- **Solo developers who want structured discipline** without enterprise overhead. Superpowers codifies best practices into enforceable skills rather than relying on developer memory.
- **Claude Code power users** who want a deeply integrated, skills-based development methodology for their tool.
- **Teams that want to accumulate and share AI agent knowledge** as versioned, testable, Markdown-based skills.
- **Projects that benefit from strict TDD enforcement** — the mandatory RED-GREEN-REFACTOR cycle catches regressions early.
- **Developers using multiple AI tools** who want consistent agent behavior across Claude Code and the project's 15+ other documented install targets.

## Not ideal for

- **Teams needing multi-agent team coordination** — Squad or BMAD provide structured role separation and team dynamics that Superpowers lacks.
- **Enterprise environments requiring formal governance** — HVE offers audit trails, constraint enforcement, and policy-as-code.
- **Quick bug fixes or small scripts** where the skill-driven workflow overhead isn't justified.
- **IDE-only environments without CLI access** — skills bootstrap requires CLI interaction to search and load skills at runtime.

## Community & ecosystem

Superpowers had roughly 306K GitHub stars on October 27, 2026. Created by Jesse Vincent (obra), the framework is maintained with Prime Radiant backing. Version 6.2.0 (superseded by the v7.x line) introduced plan-scoped state under `.superpowers/sdd/<plan-basename>/`, then deletes that workspace after a clean final review. Community support is available through Discord and third-party tutorials.

## Community ports & unofficial adaptations

Two VS Code Marketplace extensions bring Superpowers to GitHub Copilot Chat. **[Superpowers for Copilot Chat](https://marketplace.visualstudio.com/items?itemName=dwaintr.superpowers-vscode)** (2,568 installs) by Kaan Aslan provides a `@superpowers` chat participant with 14 slash commands. **[Superpowers Copilot Agents](https://marketplace.visualstudio.com/items?itemName=anothel.superpowers-copilot-agents)** (389 installs) converts workflow skills into VS Code Copilot agents.

On GitHub, **[superpowers-copilot](https://github.com/varunr89/superpowers-copilot)** (4★) offers a multi-platform adaptation with `.copilot`, `.codex`, and `.claude-plugin` directories. **[superpowers-for-copilot](https://github.com/jsloat/superpowers-for-copilot)** (3★) targets Copilot CLI.

The official project added Copilot CLI support natively in v5.0.7, closing the gap from the upstream side. Active community demand is evidenced by issues [#217](https://github.com/obra/superpowers/issues/217) and [#764](https://github.com/obra/superpowers/issues/764) on obra/superpowers.

## Comparison notes

**vs. GSD:** Both enforce structured development with fresh task contexts. GSD Core uses a five-step project workflow; Superpowers uses composable, mandatory skills. Repository metrics are not a meaningful adoption comparison because GSD migrated to a new repository.

**vs. BMAD:** BMAD simulates a full agile team with structured phases and ceremonies; Superpowers enhances individual developer effectiveness through behavioral skills. BMAD's strength is process simulation through distinct roles. Superpowers' strength is mandatory skills — TDD and code review you cannot skip.

**vs. Context Engineering:** Context engineering is the practice of curating what the agent receives. Superpowers applies it through Markdown skills, then adds a prescribed development workflow, mandatory TDD, subagent management, and skill-authoring tools.

**vs. the skills market:** Superpowers uses the `SKILL.md` format defined by [Agent Skills](https://agentskills.io) for a mandatory brainstorm → plan → TDD → review workflow. [`mattpocock/skills`](skills-libraries.md) and [`addyosmani/agent-skills`](skills-libraries.md) offer selectable or lifecycle-mapped skills without that mandatory sequence. [`pstack/poteto-mode`](skills-orchestrating-modes.md) routes requests to skills in a composable library. Choose Superpowers for a prescribed workflow, or a library with optional routing when you want to select and adapt practices yourself.

## Related pages

Superpowers appears under [Skills and Agent Frameworks](skills-ecosystem.md) because it uses skills as mandatory workflow controls.

- [State of the Skills Market](skills-ecosystem.md) — the market overview and taxonomy Superpowers is positioned against
- [Skill Libraries](skills-libraries.md) — composable and lifecycle libraries, for contrast with Superpowers' enforced sequence
- [Orchestrating Modes](skills-orchestrating-modes.md) — `pstack/poteto-mode`, the category closest in spirit to Superpowers' dispatch behavior
- [Distribution and Governance](skills-management.md) — installation, versioning, and provenance mechanics shared across the skills layer
- [Choosing a Skills Approach](skills-choosing.md) — decision guide for picking a methodology versus a library
- [Context Engineering](context-engineering.md) — the underlying practice Superpowers' skills implement
