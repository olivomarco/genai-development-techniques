# OpenSpec

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | OpenSpec                      |
| Category           | Spec-Driven Development       |
| Source              | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) |
| Author/Org         | Fission AI / Tabish Bidiwale (@0xTab) |
| License            | MIT                           |
| First Released     | August 2025                   |
| Current Version    | v1.15.0 (October 24, 2026)    |
| Stars / Popularity | ~73,100 stars · 5,000 forks |
| Supported Tools    | 30+ AI assistants via slash commands, including a vendor-neutral `agents` target, Zed Agent, MiniMax Code, Rovo Dev CLI, and — as of v1.14.0 — GSD |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Supported |
| GitHub Copilot Coding Agent (github.com) | ⚠️ Partial — spec files are readable but the workflow is interactive CLI-driven |
| Claude Code | ✅ Supported |
| Cursor | ✅ Supported |
| OpenAI Codex (CLI) | ✅ Supported |
| Windsurf | ✅ Supported |
| Gemini CLI | ✅ Supported |
| Roo Code | ✅ Supported |
| Amazon Q Developer | ✅ Supported |
| Cline | ✅ Supported |
| Continue | ✅ Supported |
| Kilo Code | ✅ Supported |
| Kiro | ✅ Supported |
| OpenCode | ✅ Supported |
| Junie | ✅ Supported |
| Auggie | ✅ Supported |
| IBM Bob | ✅ Supported |
| CoStrict | ✅ Supported |
| Crush | ✅ Supported |
| Factory Droid | ✅ Supported |
| ForgeCode | ✅ Supported |
| iFlow | ✅ Supported |
| Pi | ✅ Supported |
| Qoder | ✅ Supported |
| Qwen Code | ✅ Supported |
| Trae | ✅ Supported |
| Antigravity | ✅ Supported |
| CodeBuddy | ✅ Supported |

OpenSpec presents its supported tools as native/pre-baked integrations rather than community ports. Its own README claims 30+ AI assistants via slash commands; v1.14.0 added ten more tools (including GSD — the spec-driven technique covered elsewhere on this site — as an installable target), so the exact current total moves release to release and identical feature depth across runtimes isn't verified.

## Overview

OpenSpec is a lightweight, spec-driven development framework for AI coding assistants by Fission AI (Y Combinator W26). It organizes development around **changes** — each feature, bug fix, or modification gets its own folder containing a proposal, specs, design doc, and task checklist. The core workflow is three steps: propose a change, apply it, then archive it. This creates what OpenSpec calls "version control for intent" — a traceable record of not just *what* changed in the code, but *why* it changed.

The core problem OpenSpec addresses is brownfield development with AI. Most spec-driven tools assume you're starting fresh or building a complete project plan. OpenSpec starts from the opposite end: you have an existing codebase, and you need to make targeted changes without breaking what's already there. It uses **delta specs** — lightweight specifications annotated with ADDED, MODIFIED, and REMOVED markers — to track how changes affect existing functionality, not just what new code is being written.

At roughly 73K GitHub stars and v1.15.0, OpenSpec is the third spec-driven technique in this comparison (alongside GSD and Spec Kit) and the only one built explicitly for brownfield workflows. It now installs as a single standalone binary (no Node.js required) or via npm/Homebrew, requires no API keys or MCP servers, and offers broad native/pre-baked support across many AI coding tools. The default profile is now intentionally minimal — just `/opsx:explore` and `/opsx:propose` — with the fuller command set available as an opt-in "expanded" profile.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Broad native/pre-baked tool support (30+ assistants) | ❌ Static specs — don't update during implementation (drift risk on long tasks) |
| ✅ Brownfield-first — built for existing codebases, not just greenfield | ❌ No multi-agent orchestration or parallel execution |
| ✅ Lightest weight in SDD category (~250 lines, minutes setup) | ❌ Cross-repo team workspaces ("Stores") are in beta, not production-proven |
| ✅ Delta specs make code review about intent, not just diffs | ❌ Requires manual discipline to archive completed changes |
| ✅ Proposal approval gate — no code until human reviews | ❌ Limited enterprise compliance — no SSO/SCIM, no policy-as-code |
| ✅ YC W26-backed with active, frequent releases (weekly cadence) | ❌ Default profile now covers only explore/propose — the expanded workflow needs explicit opt-in |

> **In one sentence:** OpenSpec is a lightweight spec-driven framework for brownfield codebases where you need to track *why* things changed across a broad set of AI coding tools, with cross-repo team planning now arriving as a beta feature.

## Core Concepts

**Change Folders.** Every feature, fix, or modification gets its own folder under `openspec/changes/<name>/`. Each folder contains a proposal, specs (with GIVEN/WHEN/THEN scenarios), a design doc, and a task checklist. The change folder is the atomic unit of work — it captures everything about a single change in one place.

**Delta Specs.** Rather than writing a complete specification from scratch, OpenSpec uses delta markers — `ADDED`, `MODIFIED`, `REMOVED` — to annotate how a change affects existing functionality. This is unique in the comparison: GSD writes full task specs, Spec Kit writes full project specs, but OpenSpec writes *change* specs that explicitly reference the existing codebase. This makes code review about reviewing intent ("what are we changing and why?") rather than just reviewing code diffs.

**Propose → Apply → Archive.** The core state machine. You **propose** a change (creating the change folder with specs and tasks), get human approval, **apply** it (implement the code), then **archive** it (move the completed change to the archive for audit trail). No code is generated until the proposal is reviewed and approved — this is the human-in-the-loop gate.

**Brownfield-First.** OpenSpec is built for codebases that already exist. Where GSD Core's five-step workflow and Spec Kit's spec → plan → tasks flow are oriented toward building things from a plan, OpenSpec's change folder model assumes you already have working software and need to evolve it without breaking it.

**Artifact-Guided Workflow.** The `opsx` workflow (a rebuilt, expanded version of the original OpenSpec commands) treats each artifact — proposal, spec, design, tasks — as a living document that can be updated at any time. There are no rigid phase gates; you can revisit and refine artifacts fluidly as understanding evolves.

## How It Works

As of v1.15.0, OpenSpec ships every workflow as both an **Agent Skill** (`.agents/skills/openspec-*`, auto-invoked when relevant) and a **slash command** (`/opsx:*`, typed explicitly) — delivery is configurable per project (`skills`, `commands`, or `both`, default `both`).

The default `core` profile installs six workflows:

| Command | Purpose |
|---------|---------|
| `/opsx:explore` | Think through an idea before it becomes a change proposal (read-only; asks before writing anything) |
| `/opsx:propose` | Create a change proposal and generate all its planning artifacts (proposal, specs, design, tasks) in one step |
| `/opsx:apply` | Implement a change proposal's tasks |
| `/opsx:update` | Revise a change proposal's existing planning artifacts |
| `/opsx:sync` | Merge a change proposal's spec updates into `specs/` without archiving it |
| `/opsx:archive` | Move a finished change proposal to the archive |

Six more workflows are available in the `custom` profile (`openspec config profile`): `new` and `continue` build a proposal artifact-by-artifact instead of all at once; `ff` ("fast-forward") creates a full proposal in one pass; `verify` checks implementation against the proposal; `bulk-archive` archives several proposals at once; and `onboard` walks a new contributor through one real change end to end. This replaces the single flat command list from earlier versions — OpenSpec now distinguishes a minimal default loop from an opt-in expanded set.

The typical core-profile workflow:

1. **`/opsx:explore`** (optional) — Think an idea through with the agent; it investigates the codebase, asks questions, and writes nothing unless you ask it to.
2. **`/opsx:propose`** — The proposal is drafted: a change folder with proposal, specs (GIVEN/WHEN/THEN scenarios), design doc, and tasks. Delta markers (ADDED/MODIFIED/REMOVED) annotate how it affects existing functionality.
3. **Human review** — The proposal is approved before any code is generated. This is the gate.
4. **`/opsx:apply`** — The AI implements the approved change, guided by the spec and task checklist. Best started in a fresh context window.
5. **`/opsx:archive`** — Updates the main specs with the change's requirements and moves the change folder to the archive, preserving the *why* alongside the *what*.

For validation, `openspec validate --strict` catches missing GIVEN/WHEN/THEN scenarios and other quality issues in specs, enforcing a minimum bar before implementation begins. The archive serves as an audit trail — a chronological record of every change, its rationale, and its specs.

## Strengths

- **Broad tool compatibility.** Native/pre-baked integrations across 30+ assistants reduce tool lock-in, while exact feature parity across every runtime remains unverified.
- **Dual-form skills and commands ecosystem.** Every workflow installs as both an Agent Skill under `.agents/skills/openspec-*` and a slash command, directly participating in the shared [skills ecosystem](skills-ecosystem.md) rather than only exposing OpenSpec-specific commands. v1.10.0 added a dedicated Zed Agent target that is skills-only.
- **Lightest weight in the SDD category.** ~250 lines of configuration, minutes to set up. v1.15.0 added a standalone binary install (`curl ... | sh`, no Node.js needed) alongside the existing npm and Homebrew paths. No API keys, no MCP server, no complex scaffolding.
- **Brownfield-first design.** The only framework in this comparison built explicitly for evolving existing codebases. Delta markers (ADDED/MODIFIED/REMOVED) are a unique mechanism for tracking change impact.
- **Intent-level code review.** Delta specs shift code review from "what code changed?" to "what was the intent and how does it affect existing functionality?" This is a meaningful workflow improvement for teams that review PRs.
- **Proposal-before-code gate.** Explicit human approval before any code generation. The AI cannot proceed until the human reviews and approves the proposal — a strong HITL mechanism.
- **YC-backed with commercial trajectory and a cross-repo beta.** Y Combinator W26 backing funds weekly releases. **Stores** (beta) — a separate OpenSpec repo shared across multiple code repos via `git push` — is the first concrete answer to the team-workspace gap called out in earlier reviews.
- **Zero-dependency setup.** A single install command (binary, npm, or Homebrew) and `openspec init`. No additional configuration, no API keys, no server process.

## Limitations

- **Static specs.** Specs are written at proposal time and don't automatically update as implementation progresses. On long or complex tasks, specs can drift from reality — you must manually run `/opsx:sync` to reconcile.
- **No multi-agent orchestration.** OpenSpec is a single-agent workflow. It doesn't spawn parallel agents, manage context windows across agents, or coordinate work across multiple AI instances. GSD and Squad handle this; OpenSpec does not.
- **Stores are beta, not proven at scale.** Cross-repo planning now exists as a shipped feature, not just a roadmap item, but OpenSpec's own docs label it beta. Teams with complex multi-repo or monorepo structures should validate it before standardizing.
- **Manual archive discipline.** Completed changes must be manually archived via `/opsx:archive` or `/opsx:bulk-archive` (the latter requires the expanded profile). Without discipline, the `openspec/changes/` directory accumulates stale change folders that clutter context.
- **Limited enterprise governance.** No SSO/SCIM, no policy-as-code, no constraint enforcement, no compliance features. The archive provides a lightweight audit trail, but it's not enterprise-grade governance.
- **Default profile is now narrower.** Only `explore` and `propose` plus the implicit `apply`/`archive`/`update`/`sync` core six are installed by default; teams that want `verify`, `bulk-archive`, `new`/`continue`/`ff`, or `onboard` must explicitly switch to the expanded `custom` profile.

## Best For

- **Brownfield development.** Teams evolving an existing codebase who need to track how changes affect existing functionality. OpenSpec's delta markers are purpose-built for this.
- **Multi-tool teams.** Organizations where different developers use different AI coding tools. OpenSpec's broad native/pre-baked support, including dual skill/command delivery, lets many teams share the same spec workflow.
- **Lightweight spec-driven development.** Developers who want the discipline of spec-driven development without the overhead of a full lifecycle framework. OpenSpec is lighter than GSD Core's five-step workflow and Spec Kit's three-process toolkit.
- **Solo developers and small teams.** The current sweet spot — fast setup, low ceremony, no team infrastructure required.
- **Early adopters of cross-repo planning.** Teams that want to pilot Stores for shared, cross-repo specs, understanding it's a beta feature.
- **Intent-level code review workflows.** Teams that want to review *why* a change was made, not just *what* code changed. Delta specs make this native to the workflow.

## Not Ideal For

- **Large-scale parallel development.** No multi-agent orchestration, no wave-based parallelism. For parallel execution across multiple agents, GSD or Squad are better choices.
- **Enterprise environments requiring compliance.** No SSO, SCIM, policy-as-code, or enterprise audit features. HVE is the dedicated enterprise approach.
- **Complex workspace architectures needing proven stability.** Stores (beta) now exist for cross-repo and shared-team planning, but OpenSpec itself labels the feature beta. Large organizations with complex repo structures should pilot carefully rather than standardize immediately.
- **Greenfield projects needing full lifecycle structure.** OpenSpec is change-centric, not project-centric. For structured greenfield builds with phase gates and project-level planning, GSD or Spec Kit provide more scaffolding.
- **Teams needing strict governance.** The archive provides a lightweight audit trail, but there's no constraint enforcement, no mandatory checks beyond the proposal gate, and no policy-as-code.

## Community & Ecosystem

OpenSpec had roughly 73K GitHub stars and 5K forks as of late October 2026, with a release cadence close to weekly since v1.8.0. v1.14.0 added ten new tool targets (including GSD itself as an installable target — one spec-driven technique now supports generating artifacts for another). v1.15.0 added a standalone, Node.js-free install path with signed binaries for macOS, Linux, and Windows. Cross-repo **Stores** shipped as a beta feature with its own documentation section, directly addressing the earlier "team workspace unproven" gap, though it remains beta rather than GA.

## Community Ports & Unofficial Adaptations

OpenSpec ships native/pre-baked configurations for 30+ tools, reducing the need for community ports. Recent additions include a vendor-neutral `agents` target, a dedicated Zed Agent target, MiniMax Code, Rovo Dev CLI, Command Code, SourceCraft, and GSD. OpenSpec's own docs describe third-party schema bundles (distributed as standalone repositories) as directly comparable to [Spec Kit's community extension catalog](https://github.com/github/spec-kit/tree/main/extensions). Treat all of this as documented support breadth, not proof of runtime parity.

## Comparison Notes

**vs. GSD:** Both are spec-driven, but they target different workflows. GSD Core uses a five-step project loop and fresh task contexts; OpenSpec organizes targeted brownfield changes around delta specs. As of v1.14.0, OpenSpec can even generate GSD-formatted artifacts as one of its installable tool targets — the two techniques now interoperate at the tooling level even though they remain distinct in scope. Both document broad runtime targets, but parity is unverified. Choose GSD for structured project execution and OpenSpec for lightweight change governance.

**vs. Spec Kit:** Both are spec-driven and multi-tool, and both are now stable, non-experimental releases (OpenSpec v1.15.0, Spec Kit v1.2.3, both past 1.0). Spec Kit is the heavier toolkit — three separate processes (spec-driven development, bug fixing, idea assessment) plus a full extension/preset/bundle/catalog system. OpenSpec stays lightweight and change-centric, with delta specs and a six-workflow core profile. Spec Kit emphasizes upfront specification quality across more scenario types; OpenSpec emphasizes proposal approval, brownfield change records, and now cross-repo Stores.

**vs. Context Engineering:** OpenSpec is a concrete implementation of context engineering principles applied to change management. Change folders are curated context — each one scopes what the AI sees to a single change and its relevant specs, design, and tasks. Delta markers are a form of structured context annotation — they tell the AI not just what to build, but what already exists and how it's being modified. The proposal → approval → apply flow is a context quality gate — ensuring the AI works from reviewed, human-approved context rather than raw prompts. Where context engineering is the underlying practice, OpenSpec turns it into a working system for brownfield spec-driven development.

**vs. the managed-skills layer:** OpenSpec is a lifecycle framework, not a skill library — its job is deciding what changes to make and when, not supplying general-purpose reusable capabilities. But its distribution mechanism now overlaps directly with the skills layer: every core workflow installs as an Agent Skill under `.agents/skills/openspec-*` (alongside a slash command), and the Zed Agent target is skills-only. This makes OpenSpec a *producer* that feeds the shared `.agents/skills/` convention described in the [skills ecosystem](skills-ecosystem.md) page, alongside the `skills` CLI and Spec Kit's Codex integration — without OpenSpec itself becoming a skill library like `mattpocock/skills` or a skill-based methodology like Superpowers.

**vs. Superpowers:** Superpowers is a skill-based methodology that teaches agents *how* to develop. OpenSpec defines *what* changes to make and *why*. OpenSpec's workflows are also now delivered as Agent Skills by default, so the two projects both use the Agent Skills format — but for different ends: Superpowers' skills encode mandatory development discipline, while OpenSpec's skills encode its own lifecycle commands.
