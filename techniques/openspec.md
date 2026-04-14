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
| Current Version    | v1.3.0 (35 releases, April 2026) |
| Stars / Popularity | ~39,900 stars · 2,700+ forks · 59 contributors |
| Supported Tools    | 27+ tools — Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, Windsurf, Roo Code, and many more (widest in comparison) |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Natively supported |
| GitHub Copilot Coding Agent (github.com) | ⚠️ Partial — spec files are readable but the workflow is interactive CLI-driven |
| Claude Code | ✅ Natively supported |
| Cursor | ✅ Natively supported |
| OpenAI Codex (CLI) | ✅ Natively supported |
| Windsurf | ✅ Natively supported |
| Gemini CLI | ✅ Natively supported |
| Roo Code | ✅ Natively supported |
| Amazon Q Developer | ✅ Natively supported |
| Cline | ✅ Natively supported |
| Continue | ✅ Natively supported |
| Kilo Code | ✅ Natively supported |
| Kiro | ✅ Natively supported |
| OpenCode | ✅ Natively supported |
| Junie | ✅ Natively supported |
| Auggie | ✅ Natively supported |
| IBM Bob | ✅ Natively supported |
| CoStrict | ✅ Natively supported |
| Crush | ✅ Natively supported |
| Factory Droid | ✅ Natively supported |
| ForgeCode | ✅ Natively supported |
| iFlow | ✅ Natively supported |
| Pi | ✅ Natively supported |
| Qoder | ✅ Natively supported |
| Qwen Code | ✅ Natively supported |
| Trae | ✅ Natively supported |
| Antigravity | ✅ Natively supported |
| CodeBuddy | ✅ Natively supported |

OpenSpec has the widest tool compatibility of any technique in this comparison. All 27+ tools are first-class — no community ports, no workarounds, no reduced feature sets.

## Overview

OpenSpec is a lightweight, spec-driven development framework for AI coding assistants by Fission AI (Y Combinator W26). It organizes development around **changes** — each feature, bug fix, or modification gets its own folder containing a proposal, specs, design doc, and task checklist. The core workflow is three steps: propose a change, apply it, then archive it. This creates what OpenSpec calls "version control for intent" — a traceable record of not just *what* changed in the code, but *why* it changed.

The core problem OpenSpec addresses is brownfield development with AI. Most spec-driven tools assume you're starting fresh or building a complete project plan. OpenSpec starts from the opposite end: you have an existing codebase, and you need to make targeted changes without breaking what's already there. It uses **delta specs** — lightweight specifications annotated with ADDED, MODIFIED, and REMOVED markers — to track how changes affect existing functionality, not just what new code is being written.

At 39.9K GitHub stars and 35 releases, OpenSpec is the third spec-driven technique in this comparison (alongside GSD and Spec Kit) and the only one built explicitly for brownfield workflows. Its TypeScript CLI installs in minutes via npm, requires no API keys or MCP servers, and natively supports 27+ AI coding tools — more than any other framework compared.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Widest tool support in comparison (27+ tools, all native) | ❌ Static specs — don't update during implementation (drift risk on long tasks) |
| ✅ Brownfield-first — built for existing codebases, not just greenfield | ❌ No multi-agent orchestration or parallel execution |
| ✅ Lightest weight in SDD category (~250 lines, minutes setup) | ❌ Single-repo focus — no multi-repo or monorepo support |
| ✅ Delta specs make code review about intent, not just diffs | ❌ Requires manual discipline to archive completed changes |
| ✅ Proposal approval gate — no code until human reviews | ❌ Limited enterprise compliance — no SSO/SCIM, no policy-as-code |
| ✅ YC W26-backed with active development (daily commits) | ❌ Team workspaces feature still in development |

> **In one sentence:** OpenSpec is the lightest, widest-reaching spec-driven framework — built for brownfield codebases where you need to track *why* things changed, not just *what* changed, across 27+ AI coding tools.

## Core Concepts

**Change Folders.** Every feature, fix, or modification gets its own folder under `openspec/changes/<name>/`. Each folder contains a proposal, specs (with GIVEN/WHEN/THEN scenarios), a design doc, and a task checklist. The change folder is the atomic unit of work — it captures everything about a single change in one place.

**Delta Specs.** Rather than writing a complete specification from scratch, OpenSpec uses delta markers — `ADDED`, `MODIFIED`, `REMOVED` — to annotate how a change affects existing functionality. This is unique in the comparison: GSD writes full task specs, Spec Kit writes full project specs, but OpenSpec writes *change* specs that explicitly reference the existing codebase. This makes code review about reviewing intent ("what are we changing and why?") rather than just reviewing code diffs.

**Propose → Apply → Archive.** The core state machine. You **propose** a change (creating the change folder with specs and tasks), get human approval, **apply** it (implement the code), then **archive** it (move the completed change to the archive for audit trail). No code is generated until the proposal is reviewed and approved — this is the human-in-the-loop gate.

**Brownfield-First.** OpenSpec is built for codebases that already exist. Where GSD's 6-step workflow and Spec Kit's spec → plan → tasks flow are oriented toward building things from a plan, OpenSpec's change folder model assumes you already have working software and need to evolve it without breaking it.

**Artifact-Guided Workflow.** The `opsx` workflow (a rebuilt, expanded version of the original OpenSpec commands) treats each artifact — proposal, spec, design, tasks — as a living document that can be updated at any time. There are no rigid phase gates; you can revisit and refine artifacts fluidly as understanding evolves.

## How It Works

OpenSpec uses slash commands via the `opsx` workflow:

| Command | Purpose |
|---------|---------|
| `/opsx:new` | Start a new change — creates the change folder with proposal, specs, design, and tasks |
| `/opsx:propose` | Draft or refine a change proposal for human review |
| `/opsx:apply` | Implement the approved change — code generation begins here |
| `/opsx:archive` | Move a completed change to the archive (audit trail) |
| `/opsx:continue` | Resume work on an in-progress change (re-loads change context) |
| `/opsx:ff` | Fast-forward — catch up on changes made outside OpenSpec |
| `/opsx:verify` | Check implementation against specs (post-apply validation) |
| `/opsx:sync` | Synchronize specs with the current codebase state |
| `/opsx:bulk-archive` | Archive multiple completed changes at once |
| `/opsx:onboard` | Introduce a new team member or AI session to the project's OpenSpec state |

The typical workflow proceeds as:

1. **`/opsx:new`** — Developer describes the change they want. OpenSpec creates a change folder with scaffolded artifacts (proposal, spec with GIVEN/WHEN/THEN, design doc, tasks).
2. **`/opsx:propose`** — The proposal is refined and reviewed. Delta markers (ADDED/MODIFIED/REMOVED) annotate how this change affects existing functionality.
3. **Human review** — The proposal is approved before any code is generated. This is the gate.
4. **`/opsx:apply`** — The AI implements the approved change, guided by the spec and task checklist.
5. **`/opsx:verify`** — Validates that the implementation matches the spec.
6. **`/opsx:archive`** — Moves the completed change to the archive, preserving the *why* alongside the *what* for future reference.

For validation, `openspec validate --strict` catches missing GIVEN/WHEN/THEN scenarios in specs, enforcing a minimum quality bar before implementation begins. The archive serves as an audit trail — a chronological record of every change, its rationale, and its specs.

## Strengths

- **Widest tool compatibility.** 27+ tools natively supported — no ports, no adapters, no reduced functionality. This is more than any other technique in the comparison and eliminates tool lock-in entirely.
- **Lightest weight in the SDD category.** ~250 lines of configuration, minutes to set up (`npm install -g @fission-ai/openspec@latest && openspec init`). No API keys, no MCP server, no complex scaffolding.
- **Brownfield-first design.** The only framework in this comparison built explicitly for evolving existing codebases. Delta markers (ADDED/MODIFIED/REMOVED) are a unique mechanism for tracking change impact.
- **Intent-level code review.** Delta specs shift code review from "what code changed?" to "what was the intent and how does it affect existing functionality?" This is a meaningful workflow improvement for teams that review PRs.
- **Proposal-before-code gate.** Explicit human approval before any code generation. The AI cannot proceed until the human reviews and approves the proposal — a strong HITL mechanism.
- **YC-backed with commercial trajectory.** Y Combinator W26 backing provides funding, credibility, and a commercial incentive to keep developing. Team workspaces and enterprise features are on the roadmap.
- **Zero-dependency setup.** A single npm install and init command. No additional configuration, no API keys, no server process. The lowest friction entry point of any spec-driven technique.

## Limitations

- **Static specs.** Specs are written at proposal time and don't automatically update as implementation progresses. On long or complex tasks, specs can drift from reality — you must manually `/opsx:sync` to reconcile.
- **No multi-agent orchestration.** OpenSpec is a single-agent workflow. It doesn't spawn parallel agents, manage context windows across agents, or coordinate work across multiple AI instances. GSD and Squad handle this; OpenSpec does not.
- **Single-repo focus.** No multi-repo or monorepo support. The "Workspaces" feature for larger codebases is in development but not yet shipped. Enterprise teams with complex repo structures will hit this limit.
- **Manual archive discipline.** Completed changes must be manually archived via `/opsx:archive` or `/opsx:bulk-archive`. Without discipline, the `openspec/changes/` directory accumulates stale change folders that clutter context.
- **Limited enterprise governance.** No SSO/SCIM, no policy-as-code, no constraint enforcement, no compliance features. The archive provides a lightweight audit trail, but it's not enterprise-grade governance.
- **Young project.** At ~8 months old and v1.3.0, OpenSpec is still early. The `opsx` workflow was recently rebuilt, indicating the API surface is still evolving.

## Best For

- **Brownfield development.** Teams evolving an existing codebase who need to track how changes affect existing functionality. OpenSpec's delta markers are purpose-built for this.
- **Multi-tool teams.** Organizations where different developers use different AI coding tools. OpenSpec's 27+ tool support means everyone can use the same spec workflow regardless of their editor or agent.
- **Lightweight spec-driven development.** Developers who want the discipline of spec-driven development without the overhead of a full lifecycle framework. OpenSpec is lighter than GSD (6-step workflow) and Spec Kit (phase-gated).
- **Solo developers and small teams.** The current sweet spot — fast setup, low ceremony, no team infrastructure required.
- **Intent-level code review workflows.** Teams that want to review *why* a change was made, not just *what* code changed. Delta specs make this native to the workflow.

## Not Ideal For

- **Large-scale parallel development.** No multi-agent orchestration, no wave-based parallelism. For parallel execution across multiple agents, GSD or Squad are better choices.
- **Enterprise environments requiring compliance.** No SSO, SCIM, policy-as-code, or enterprise audit features. HVE is the dedicated enterprise approach.
- **Multi-repo or monorepo architectures.** Single-repo only until the Workspaces feature ships. Large organizations with complex repo structures should wait or look elsewhere.
- **Greenfield projects needing full lifecycle structure.** OpenSpec is change-centric, not project-centric. For structured greenfield builds with phase gates and project-level planning, GSD or Spec Kit provide more scaffolding.
- **Teams needing strict governance.** The archive provides a lightweight audit trail, but there's no constraint enforcement, no mandatory checks beyond the proposal gate, and no policy-as-code.

## Community & Ecosystem

OpenSpec has built significant community traction in ~8 months: 39.9K GitHub stars, 2.7K forks, 59 contributors, and daily commit activity. The project is backed by Y Combinator (W26 batch) through Fission AI, giving it commercial backing uncommon among open-source AI development frameworks in this comparison. Community channels include an active Discord (discord.gg/YctCnvvshC), a Slack channel for teams (teams@openspec.dev), and GitHub Discussions. The founder Tabish Bidiwale is active on LinkedIn and YouTube. OpenSpec has been featured in Augment Code's "6 Best SDD Tools" roundup, Better Stack, and Cursor community discussions. The project is actively inviting enterprise early partners for the upcoming Workspaces (multi-repo) feature.

## Community Ports & Unofficial Adaptations

OpenSpec natively supports 27+ AI coding tools out of the box — the widest compatibility of any technique in this comparison. Because of this breadth, there is no need for community ports or unofficial adaptations. Where GSD required community forks for Cursor support and Superpowers needed marketplace extensions for Copilot, OpenSpec ships with first-class support for all major tools from day one. This is a deliberate architectural decision: the TypeScript CLI and Markdown-based spec format are tool-agnostic by design, with pre-baked configurations for each supported tool.

## Comparison Notes

**vs. GSD:** Both are spec-driven, but they target different workflows and codebases. GSD is greenfield-oriented — its 6-step lifecycle (new-project → discuss → plan → execute → verify → complete) builds things from scratch with fresh context windows per task. OpenSpec is brownfield-oriented — its change folder model assumes existing code and tracks modifications with delta markers. GSD manages context rot through fresh agent spawning; OpenSpec manages context through scoped change folders. GSD supports ~6 tools (primarily Claude Code); OpenSpec supports 27+. GSD offers parallel execution via wave-based orchestration; OpenSpec is single-agent. GSD is more mature (v1.35.0, 51K stars); OpenSpec is younger but growing fast (v1.3.0, 39.9K stars). Choose GSD for structured greenfield builds with parallelism; choose OpenSpec for lightweight brownfield changes across any tool.

**vs. Spec Kit:** Both are spec-driven and multi-tool, making them the closest comparison pair in this category. The key differences are weight and philosophy. Spec Kit produces comprehensive, portable specifications (~800 lines of spec artifacts) through a phase-gated workflow (specify → clarify → plan → tasks → implement). OpenSpec produces lightweight delta specs (~250 lines) through a fluid, change-centric workflow with no rigid phase gates. Spec Kit is GitHub-backed and still experimental (v0.6.2); OpenSpec is YC-backed and more aggressively versioned (v1.3.0, 35 releases). Spec Kit's agent-agnosticism covers 20+ tools via pre-baked prompts; OpenSpec's covers 27+ tools natively. Spec Kit focuses on the specification phase and leaves execution to the user's tool; OpenSpec covers the full change lifecycle (propose → apply → verify → archive). Spec Kit has richer quality checks (analyze, checklist); OpenSpec has a stronger human gate (proposal approval before any code). They're complementary in principle — Spec Kit for upfront project specification, OpenSpec for ongoing change management — but in practice they occupy overlapping territory.

**vs. Context Engineering:** OpenSpec is a concrete implementation of context engineering principles applied to change management. Change folders are curated context — each one scopes what the AI sees to a single change and its relevant specs, design, and tasks. Delta markers are a form of structured context annotation — they tell the AI not just what to build, but what already exists and how it's being modified. The proposal → approval → apply flow is a context quality gate — ensuring the AI works from reviewed, human-approved context rather than raw prompts. Where context engineering is the underlying practice, OpenSpec is one specific operationalization of it for brownfield spec-driven development.

**vs. Superpowers:** Both have broad multi-tool support (27+ vs. 6 tools) and both are lighter than GSD or Spec Kit, but they solve different problems. Superpowers is a skill-based methodology — composable behavioral modules that teach agents *how* to develop (TDD, code review, debugging). OpenSpec is a spec-driven workflow — structured change tracking that defines *what* to build and *why*. Superpowers enforces development discipline through mandatory skills and persuasion-tested compliance; OpenSpec enforces change discipline through proposal gates and delta specs. Superpowers has the larger community (151K vs. 39.9K stars) and a different category (Skill-Based Development vs. Spec-Driven Development). They're complementary: Superpowers could govern how an agent implements code, while OpenSpec governs what changes are being made and why.
