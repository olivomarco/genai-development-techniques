# GSD (Get Shit Done)

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Get Shit Done                 |
| Category           | Spec-Driven Development       |
| Source              | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) |
| Author/Org         | TÂCHES / gsd-build            |
| License            | MIT                           |
| First Released     | 2025                          |
| Current Version    | v1.35.0 (April 11, 2026)     |
| Stars / Popularity | ~51,100 stars · 4,300+ forks · 1,835+ commits |
| Supported Tools    | Claude Code (primary), OpenCode; community ports for Cursor and others |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ❌ Not natively supported |
| GitHub Copilot Coding Agent (github.com) | ❌ Not supported |
| Claude Code | ✅ Primary — built on native Claude Code features (sub-agents, slash commands, hooks) |
| Cursor | ⚠️ Community — [gsd-for-cursor](https://github.com/rmindel/gsd-for-cursor) (76★) |
| OpenAI Codex (CLI) | ❌ Not natively supported |
| Windsurf | ❌ Not natively supported |
| Gemini CLI | ❌ Not natively supported |
| Roo Code | ❌ Not natively supported |

## Overview

GSD is a lightweight, spec-driven development system that addresses one of the most persistent problems in AI-assisted coding: context rot — the gradual degradation of AI output quality as context windows fill up during long sessions. Rather than building a heavy framework, GSD is constructed entirely from native Claude Code features: roughly 50 Markdown files, a Node.js CLI helper, and a set of hooks that together orchestrate a complete software development lifecycle.

The core insight is that raw prompting doesn't scale for substantial projects. Features get forgotten, files get overwritten, and debugging cycles waste time. GSD solves this by enforcing a disciplined 6-step workflow where each phase ideally runs in a fresh context window, giving every spawned agent 100% clean context.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Eliminates context rot with fresh windows per task | ❌ Originally Claude Code-only — community ports lose depth |
| ✅ Low dependency footprint (~50 Markdown files) | ❌ Medium learning curve — 6-step workflow to internalize |
| ✅ Parallel execution (5+ agents via wave-based orchestrator) | ❌ Still requires upfront spec work that feels heavy for small fixes |
| ✅ Verification gates check actual codebase, not AI self-reports | ❌ No built-in team coordination — single-user focus |
| ✅ Atomic git commits for clean history and easy rollbacks | ❌ No enterprise governance or audit trails |
| ✅ 51K+ stars, active community, battle-tested at scale | ❌ XML prompt formatting may be unfamiliar |

> **In one sentence:** GSD is the go-to for solo Claude Code users who want structured discipline without enterprise overhead — it solves the #1 problem (context rot) with minimal ceremony.

## Core Concepts

**Context Engineering as Foundation.** GSD treats context management as the central engineering challenge. Each task spawned by the orchestrator receives a fresh context window, eliminating the accumulated noise that degrades output in long sessions.

**Lean Orchestrator.** GSD's multi-agent model groups tasks into "waves" by dependency and executes them in parallel — up to 5+ agents simultaneously. This is not a heavyweight agent framework; it is a thin orchestration layer that leverages Claude Code's native sub-agent spawning.

**Atomic Git Commits.** Each task produces a single, clean commit. This creates a traceable history and makes rollbacks straightforward.

**XML Prompt Formatting.** GSD uses XML-structured prompts for precision, reducing ambiguity in how the AI interprets instructions.

**Verification Gates.** Every phase ends with automated verification against the actual codebase, not just the AI's claims about what it did.

## How It Works

GSD follows a 6-step workflow executed via slash commands:

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `/gsd:new-project` | Capture the idea, research the domain, define requirements and roadmap |
| 2 | `/gsd:discuss-phase N` | Clarify implementation details for phase N |
| 3 | `/gsd:plan-phase N` | Create a task breakdown for phase N |
| 4 | `/gsd:execute-phase N` | Execute plans in parallel, one commit per task |
| 5 | `/gsd:verify-work N` | Validate that phase goals have been achieved |
| 6 | `/gsd:complete-milestone` | Archive, tag release, initialize next cycle |

The workflow is designed to be iterative. Each phase runs in a fresh context window. The planning step produces structured task definitions that the execution step parallelizes across multiple agents. Verification runs against the real codebase to close the loop.

GSD also offers a **Quick Mode** for smaller projects that compresses the workflow, and **Brownfield Support** for working with existing codebases rather than starting from scratch. **Workstreams** enable parallel development streams, and **Multi-Project Workspaces** allow managing multiple projects simultaneously.

## Strengths

- **Solves context rot directly.** Fresh context windows per task keep AI output quality high across long projects. This is the core problem most developers face when scaling AI-assisted work.
- **Low dependency footprint.** ~50 Markdown files and a CLI helper — no heavy framework, no proprietary runtime. The system is readable and forkable.
- **Battle-tested at scale.** Community reports include a production iOS-to-Android port completed in a 3-day sprint (90+ AI sessions, 23 plans executed), demonstrating real-world viability.
- **Strong parallel execution.** The wave-based orchestrator runs 5+ agents simultaneously, grouped by dependency, making efficient use of available compute.
- **Verification gates close the loop.** Unlike approaches that trust the AI's self-report, GSD verifies against the actual codebase after each phase.
- **Active community.** 51K+ stars, active LinkedIn community, blog coverage from codecentric.de, dev.to, and others.

## Limitations

- **Originally Claude Code-only.** GSD was designed for Claude Code. Community ports exist for other tools, but the primary workflow assumes Claude Code features (sub-agents, slash commands, hooks).
- **Medium learning curve.** The 6-step workflow is more involved than just prompting. Developers need to learn the phase structure, slash commands, and planning conventions.
- **Spec-driven overhead.** While lighter than BMAD, GSD still requires upfront planning and specification work that may feel heavy for quick scripts or bug fixes.
- **No built-in enterprise governance.** GSD lacks the constraint enforcement, audit trails, and policy-as-code features found in enterprise-focused approaches like HVE.
- **Single-user focus.** The workflow is designed for a solo developer directing AI agents. There is no built-in team coordination, role routing, or shared decision ledger.

## Best For

- **Solo developers working on medium-to-large projects** who have experienced context rot and want structured discipline without enterprise overhead.
- **Claude Code users** who want the most mature integration. GSD is built on native Claude Code features and takes full advantage of them.
- **Projects that benefit from parallel execution** — multi-module applications, feature-rich products, or codebases where multiple independent tasks can be worked simultaneously.
- **Developers who value traceability** — atomic commits and verification gates create a clean, auditable history.

## Not Ideal For

- **Quick bug fixes or small scripts** — the 6-step workflow is overkill for work that takes 15 minutes of direct coding.
- **Teams needing shared coordination** — GSD has no built-in mechanism for team routing, shared decisions, or multi-developer workflows. For that, look at Squad or BMAD.
- **Enterprise environments requiring governance** — no audit trails, constraint enforcement, or policy-as-code. HVE is the dedicated enterprise approach.
- **Developers not using Claude Code** — while community ports exist, the primary experience is Claude Code-native.

## Community & Ecosystem

GSD has one of the largest communities among AI development frameworks, with 51K+ GitHub stars and 4,300+ forks. The project is actively maintained (1,835+ commits, v1.35.0 as of April 2026) with frequent releases. Community adoption is evidenced by technical deep-dives on codecentric.de and dev.to, LinkedIn testimonials from production users (including a notable case at Whatnot), and community ports for non-Claude-Code environments. Documentation is inline — the ~50 Markdown files that compose the system also serve as its documentation.

## Community Ports & Unofficial Adaptations

The GSD ecosystem has expanded beyond its Claude Code origins through both official and community efforts. The official installer (`npx get-shit-done-cc`) now supports `--opencode`, `--codex`, and Gemini CLI flags natively. On the community side, **[gsd-for-cursor](https://github.com/rmindel/gsd-for-cursor)** (76★) provides a full Cursor IDE adaptation with install scripts and a migration guide, while **[gsd-pro](https://github.com/itsjwill/gsd-pro)** (66★) is an enhanced fork adding multi-model routing, rollback/recovery, and adaptive context management.

A grassroots Copilot effort exists via Kilo Code (documented on Reddit) but has no standalone published repo. No dedicated ports exist yet for Windsurf or Roo Code.

## Comparison Notes

**vs. BMAD:** Both are spec-driven, but GSD is lighter — ~50 Markdown files vs. BMAD's 12+ specialized agents and 34+ workflows. GSD focuses on context engineering and parallel execution; BMAD emphasizes structured agile process with distinct phase gates. A community observation: GSD delivers a "solid build in a few hours," while BMAD targets "complex or production-grade" work with heavier upfront investment. GSD is MIT-licensed; BMAD carries a proprietary trademark.

**vs. Spec Kit:** Both follow spec-driven development. GSD is more opinionated, providing a complete lifecycle (plan → execute → verify → release), while Spec Kit focuses on the specification and planning phases (spec → plan → tasks → implement). GSD is Claude Code-native; Spec Kit is agent-agnostic, working with Copilot, Claude Code, Gemini CLI, and Cursor. Spec Kit is backed by GitHub but still experimental (v0.6.2); GSD is community-driven but more mature.

**vs. Context Engineering (Practice):** GSD is one of the most explicit implementations of context engineering principles. Its fresh-context-per-task approach directly addresses the context rot problem that context engineering identifies. Where context engineering is a set of principles (curate context, version prompts, manage window limits), GSD is a concrete system that operationalizes those principles for Claude Code specifically.

**vs. Superpowers:** Both are spec-driven with TDD orientation, but the mechanisms differ. GSD uses slash commands and a 6-step workflow; Superpowers uses composable behavioral skills that agents load on demand. GSD is Claude Code-only (with community ports); Superpowers officially supports Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode. Superpowers has roughly 3x the GitHub stars (151K vs. 51K). GSD's strength is parallel wave execution and context rot prevention; Superpowers' strength is reusable skill modules and comprehensive quality gates (mandatory TDD, two-stage code review). They solve similar problems from different angles — GSD through workflow structure, Superpowers through behavioral enforcement.
