# GSD (Get Shit Done)

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Get Shit Done                 |
| Category           | Spec-Driven Development       |
| Source              | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) |
| Author/Org         | open-gsd                      |
| License            | MIT                           |
| First Released     | 2025                          |
| Current Version    | GSD Core v1.10.0 (August 8, 2026) |
| Stars / Popularity | ~7,900 stars · 550+ forks on the active successor; archived predecessor has ~64,700 stars |
| Supported Tools    | Installer targets include Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Documented installer target |
| GitHub Copilot Coding Agent (github.com) | ❌ Not supported |
| Claude Code | ✅ Deepest integration — nested dispatch, background agents, and worktree isolation are documented |
| Cursor | ✅ Documented installer target |
| OpenAI Codex (CLI) | ✅ Documented installer target |
| Windsurf | ✅ Documented installer target |
| Gemini CLI | ⚠️ Not listed by name in the current GSD Core README |
| Roo Code | ⚠️ Not verified |

GSD Core documents capability profiles for 20 hosts and negotiates dispatch behavior from available host features. This does not establish identical feature depth: Copilot defaults execution to sequential inline mode because subagent completion signals are unreliable.

## Overview

GSD is a lightweight, spec-driven development system that addresses context rot — the gradual degradation of AI output quality as context windows fill during long sessions. The original [`gsd-build/get-shit-done`](https://github.com/gsd-build/get-shit-done) repository was archived in 2026 with a "GSD Has Moved" notice. Active development continues as **GSD Core** in [`open-gsd/gsd-core`](https://github.com/open-gsd/gsd-core), installed from npm as `@opengsd/gsd-core`.

The core insight is that raw prompting doesn't scale for substantial projects. GSD Core packages a five-step loop — Discuss → Plan → Execute → Verify → Ship — with entry points for new and existing projects. The successor reset the version line from the archived package's v1.42.3 to GSD Core v1.10.0; this is a repository and package migration, not a maturity regression.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Eliminates context rot with fresh windows per task | ❌ Claude Code remains the deepest integration despite official multi-runtime expansion |
| ✅ Multi-runtime installer targets | ❌ Medium learning curve — five-step workflow to internalize |
| ✅ Wave-based parallel execution with configurable concurrency (default 3 agents) | ❌ Still requires upfront spec work that feels heavy for small fixes |
| ✅ Verification gates check actual codebase, not AI self-reports | ❌ No built-in team coordination — single-user focus |
| ✅ Atomic git commits for clean history and easy rollbacks | ❌ No enterprise governance or audit trails |
| ✅ Active successor, multilingual READMEs, Discord, and CI | ❌ Migration makes old tutorials, commands, and metrics stale |

> **In one sentence:** GSD Core is a structured, multi-runtime spec-driven workflow for developers who want fresh context, planned execution, and verification without enterprise governance.

## Core Concepts

**Context Engineering as Foundation.** GSD treats context management as the central engineering challenge. Each task spawned by the orchestrator receives a fresh context window, eliminating the accumulated noise that degrades output in long sessions.

**Lean Orchestrator.** GSD groups plans into dependency waves. Waves run sequentially, while non-file-overlapping plans within a wave can run in parallel with configurable concurrency; the documented default is three simultaneous agents. Dispatch is negotiated against host capabilities rather than depending on a Claude-only mechanism, although Claude Code remains the deepest integration.

**Atomic Git Commits.** Each task produces a single, clean commit. This creates a traceable history and makes rollbacks straightforward.

**XML Prompt Formatting.** GSD uses XML for plan task structure and prompt sectioning, reducing ambiguity without treating XML as a universal wire format.

**Verification Gates.** Every phase ends with automated verification against the actual codebase, not just the AI's claims about what it did.

## How It Works

Install the active package with:

```bash
npx @opengsd/gsd-core@latest
```

GSD Core documents a five-step loop. `/gsd-new-project` starts a new project and `/gsd-onboard` brings an existing codebase into the workflow.

| Step | Stage | Purpose |
|------|-------|---------|
| 1 | Discuss | Clarify goals, constraints, and implementation choices |
| 2 | Plan | Create an executable task breakdown |
| 3 | Execute | Implement the plan with scoped agent work |
| 4 | Verify | Check the result against the codebase and acceptance criteria |
| 5 | Ship | Complete the work and prepare delivery |

The workflow is designed to be iterative. Each phase runs in a fresh context window. The planning step produces structured task definitions that the execution step parallelizes across multiple agents. Verification runs against the real codebase to close the loop.

GSD also offers **`/gsd-quick`** for ad-hoc tasks that do not need a full phase and **`/gsd-onboard`** for brownfield onboarding. **Workstreams** maintain separate state for concurrent milestone areas. **Workspaces** isolate multi-repo work behind independent `.planning/` state using git worktrees or clones; the documentation does not claim simultaneous multi-project management.

## Strengths

- **Solves context rot directly.** Fresh context windows per task keep AI output quality high across long projects. This is the core problem most developers face when scaling AI-assisted work.
- **Small runtime dependency tree.** The published package has two production dependencies: `@anthropic-ai/claude-agent-sdk` and `ws`. Its package payload is substantial, so this claim concerns dependencies rather than file count.
- **Strong parallel execution where the host supports it.** The wave orchestrator groups plans by dependency and parallelizes non-file-overlapping work, with a documented default maximum of three simultaneous agents.
- **Verification gates close the loop.** Unlike approaches that trust the AI's self-report, GSD verifies against the actual codebase after each phase.
- **Active successor.** GSD Core released v1.10.0 on August 8, 2026, with multilingual READMEs, a Discord, and CI badges.

## Limitations

- **Runtime behavior degrades by host capability.** GSD Core documents 20 host profiles and negotiates dispatch rather than assuming parity. Copilot forces sequential inline execution; backgrounded Claude Code agents can also lose nested dispatch and wave parallelism.
- **Medium learning curve.** The five-step workflow is more involved than direct prompting. Developers need to learn its stages, commands, and planning conventions.
- **Spec-driven overhead.** While lighter than BMAD, GSD still requires upfront planning and specification work that may feel heavy for quick scripts or bug fixes.
- **No built-in enterprise governance.** GSD lacks the constraint enforcement, audit trails, and policy-as-code features found in enterprise-focused approaches like HVE.
- **Single-user focus.** The workflow is designed for a solo developer directing AI agents. There is no built-in team coordination, role routing, or shared decision ledger.

## Best For

- **Solo developers working on medium-to-large projects** who have experienced context rot and want structured discipline without enterprise overhead.
- **Developers using one of the documented installer targets** who want a structured spec-driven loop and are willing to validate runtime-specific behavior.
- **Projects that benefit from parallel execution** — multi-module applications, feature-rich products, or codebases where multiple independent tasks can be worked simultaneously.
- **Developers who value traceability** — atomic commits and verification gates create a clean, auditable history.

## Not Ideal For

- **Quick bug fixes or small scripts** — the five-step workflow is overkill for work that takes 15 minutes of direct coding.
- **Teams needing shared coordination** — GSD has no built-in mechanism for team routing, shared decisions, or multi-developer workflows. For that, look at Squad or BMAD.
- **Enterprise environments requiring governance** — no audit trails, constraint enforcement, or policy-as-code. HVE is the dedicated enterprise approach.
- **Teams that require proven cross-runtime parity** — the current evidence verifies installer targets, not equivalent execution semantics.

## Community & Ecosystem

The archived predecessor retains roughly 64.7K stars and 5.5K forks. The active GSD Core successor had roughly 7.9K stars and 550 forks on August 8, 2026. Report these as separate repository snapshots: the migration reset repository metrics even though the project lineage continued. GSD Core is MIT-licensed, publishes through npm, and was current at v1.10.0 on the observation date.

## Community Ports & Unofficial Adaptations

The GSD Core installer now names Cursor, Copilot, and Windsurf among its targets, reducing the role of older community ports. Whether `gsd-for-cursor`, `gsd-pro`, or other adaptations tracked the migration was not verified in this refresh. Treat old port guidance and the frozen `get-shit-done-cc` package as migration-era material.

## Comparison Notes

**vs. BMAD:** Both structure AI-assisted development, but GSD is lighter. GSD focuses on context engineering and planned execution; BMAD emphasizes specialized roles, modules, and agile phase gates. GSD is MIT-licensed; BMAD carries a proprietary trademark.

**vs. Spec Kit:** Both follow spec-driven development. GSD Core provides a complete Discuss → Plan → Execute → Verify → Ship loop, while Spec Kit focuses on specification and planning artifacts. Both target multiple agents; neither target list alone proves runtime parity. Spec Kit remains pre-1.0, while GSD Core uses a post-migration v1.x line.

**vs. Context Engineering (Practice):** GSD is one of the most explicit implementations of context engineering principles. Its fresh-context-per-task approach directly addresses the context rot problem that context engineering identifies. Where context engineering is a set of principles (curate context, version prompts, manage window limits), GSD is a concrete multi-host system that operationalizes them through capability-negotiated workflows.

**vs. Superpowers:** GSD Core structures work through a five-step project workflow; Superpowers uses mandatory behavioral skills. GSD's strength is planned execution and context management. Superpowers' strength is reusable enforcement of TDD and review. Repository star counts are not directly comparable because GSD migrated to a new repository.
