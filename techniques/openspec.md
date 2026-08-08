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
| Current Version    | v1.8.0 stable (August 5, 2026); prerelease channel also exists |
| Stars / Popularity | ~64,300 stars · 4,400+ forks |
| Supported Tools    | Broad native/pre-baked support, including a vendor-neutral `agents` target plus MiniMax Code and Rovo Dev CLI |

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

OpenSpec presents its supported tools as native/pre-baked integrations rather than community ports. Version 1.8.0 added three targets, bringing the previously documented list to at least 30, but the exact current total and identical feature depth across runtimes were not verified.

## Overview

OpenSpec is a lightweight, spec-driven development framework for AI coding assistants by Fission AI (Y Combinator W26). It organizes development around **changes** — each feature, bug fix, or modification gets its own folder containing a proposal, specs, design doc, and task checklist. The core workflow is three steps: propose a change, apply it, then archive it. This creates what OpenSpec calls "version control for intent" — a traceable record of not just *what* changed in the code, but *why* it changed.

The core problem OpenSpec addresses is brownfield development with AI. Most spec-driven tools assume you're starting fresh or building a complete project plan. OpenSpec starts from the opposite end: you have an existing codebase, and you need to make targeted changes without breaking what's already there. It uses **delta specs** — lightweight specifications annotated with ADDED, MODIFIED, and REMOVED markers — to track how changes affect existing functionality, not just what new code is being written.

At roughly 64K GitHub stars and v1.8.0, OpenSpec is the third spec-driven technique in this comparison (alongside GSD and Spec Kit) and the only one built explicitly for brownfield workflows. Its TypeScript CLI installs in minutes via npm, requires no API keys or MCP servers, and offers broad native/pre-baked support across many AI coding tools.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Broad native/pre-baked tool support | ❌ Static specs — don't update during implementation (drift risk on long tasks) |
| ✅ Brownfield-first — built for existing codebases, not just greenfield | ❌ No multi-agent orchestration or parallel execution |
| ✅ Lightest weight in SDD category (~250 lines, minutes setup) | ❌ Team workspace and multi-repo support not yet proven in public research |
| ✅ Delta specs make code review about intent, not just diffs | ❌ Requires manual discipline to archive completed changes |
| ✅ Proposal approval gate — no code until human reviews | ❌ Limited enterprise compliance — no SSO/SCIM, no policy-as-code |
| ✅ YC W26-backed with active development | ❌ Team workspaces feature still in development |

> **In one sentence:** OpenSpec is a lightweight spec-driven framework for brownfield codebases where you need to track *why* things changed across a broad set of AI coding tools.

## Core Concepts

**Change Folders.** Every feature, fix, or modification gets its own folder under `openspec/changes/<name>/`. Each folder contains a proposal, specs (with GIVEN/WHEN/THEN scenarios), a design doc, and a task checklist. The change folder is the atomic unit of work — it captures everything about a single change in one place.

**Delta Specs.** Rather than writing a complete specification from scratch, OpenSpec uses delta markers — `ADDED`, `MODIFIED`, `REMOVED` — to annotate how a change affects existing functionality. This is unique in the comparison: GSD writes full task specs, Spec Kit writes full project specs, but OpenSpec writes *change* specs that explicitly reference the existing codebase. This makes code review about reviewing intent ("what are we changing and why?") rather than just reviewing code diffs.

**Propose → Apply → Archive.** The core state machine. You **propose** a change (creating the change folder with specs and tasks), get human approval, **apply** it (implement the code), then **archive** it (move the completed change to the archive for audit trail). No code is generated until the proposal is reviewed and approved — this is the human-in-the-loop gate.

**Brownfield-First.** OpenSpec is built for codebases that already exist. Where GSD Core's five-step workflow and Spec Kit's spec → plan → tasks flow are oriented toward building things from a plan, OpenSpec's change folder model assumes you already have working software and need to evolve it without breaking it.

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

- **Broad tool compatibility.** Native/pre-baked integrations reduce tool lock-in, while exact feature parity across every runtime remains unverified.
- **Skills convention support.** Version 1.8.0 added a vendor-neutral `agents` target that writes skills to `.agents/skills/`, linking OpenSpec to the emerging [skills ecosystem](skills-ecosystem.md).
- **Lightest weight in the SDD category.** ~250 lines of configuration, minutes to set up (`npm install -g @fission-ai/openspec@latest && openspec init`). No API keys, no MCP server, no complex scaffolding.
- **Brownfield-first design.** The only framework in this comparison built explicitly for evolving existing codebases. Delta markers (ADDED/MODIFIED/REMOVED) are a unique mechanism for tracking change impact.
- **Intent-level code review.** Delta specs shift code review from "what code changed?" to "what was the intent and how does it affect existing functionality?" This is a meaningful workflow improvement for teams that review PRs.
- **Proposal-before-code gate.** Explicit human approval before any code generation. The AI cannot proceed until the human reviews and approves the proposal — a strong HITL mechanism.
- **YC-backed with commercial trajectory.** Y Combinator W26 backing provides funding, credibility, and a commercial incentive to keep developing. Team workspaces and enterprise features are on the roadmap.
- **Zero-dependency setup.** A single npm install and init command. No additional configuration, no API keys, no server process. The lowest friction entry point of any spec-driven technique.

## Limitations

- **Static specs.** Specs are written at proposal time and don't automatically update as implementation progresses. On long or complex tasks, specs can drift from reality — you must manually `/opsx:sync` to reconcile.
- **No multi-agent orchestration.** OpenSpec is a single-agent workflow. It doesn't spawn parallel agents, manage context windows across agents, or coordinate work across multiple AI instances. GSD and Squad handle this; OpenSpec does not.
- **Workspace support still unproven.** The available research does not establish full team workspace, multi-repo, or monorepo support. Enterprise teams with complex repo structures should validate this before standardizing on OpenSpec.
- **Manual archive discipline.** Completed changes must be manually archived via `/opsx:archive` or `/opsx:bulk-archive`. Without discipline, the `openspec/changes/` directory accumulates stale change folders that clutter context.
- **Limited enterprise governance.** No SSO/SCIM, no policy-as-code, no constraint enforcement, no compliance features. The archive provides a lightweight audit trail, but it's not enterprise-grade governance.
- **Young project.** At under a year old and v1.8.0, OpenSpec is still evolving. A prerelease channel exists, so distinguish stable releases from beta artifacts.

## Best For

- **Brownfield development.** Teams evolving an existing codebase who need to track how changes affect existing functionality. OpenSpec's delta markers are purpose-built for this.
- **Multi-tool teams.** Organizations where different developers use different AI coding tools. OpenSpec's broad native/pre-baked support lets many teams share the same spec workflow.
- **Lightweight spec-driven development.** Developers who want the discipline of spec-driven development without the overhead of a full lifecycle framework. OpenSpec is lighter than GSD Core's five-step workflow and Spec Kit's phase gates.
- **Solo developers and small teams.** The current sweet spot — fast setup, low ceremony, no team infrastructure required.
- **Intent-level code review workflows.** Teams that want to review *why* a change was made, not just *what* code changed. Delta specs make this native to the workflow.

## Not Ideal For

- **Large-scale parallel development.** No multi-agent orchestration, no wave-based parallelism. For parallel execution across multiple agents, GSD or Squad are better choices.
- **Enterprise environments requiring compliance.** No SSO, SCIM, policy-as-code, or enterprise audit features. HVE is the dedicated enterprise approach.
- **Complex workspace architectures.** Full team workspace, multi-repo, and monorepo support is not proven by the current public research. Large organizations with complex repo structures should pilot carefully or look elsewhere.
- **Greenfield projects needing full lifecycle structure.** OpenSpec is change-centric, not project-centric. For structured greenfield builds with phase gates and project-level planning, GSD or Spec Kit provide more scaffolding.
- **Teams needing strict governance.** The archive provides a lightweight audit trail, but there's no constraint enforcement, no mandatory checks beyond the proposal gate, and no policy-as-code.

## Community & Ecosystem

OpenSpec had roughly 64K GitHub stars and 4.4K forks on August 8, 2026. Version 1.8.0 merged 34 pull requests from 15 contributors. It also made GitHub Copilot cloud-agent file generation opt-in, defaulting to No, and added `retire_capabilities: true` during archive. These are shipped stable-release changes; full multi-repo workspace availability remains unverified.

## Community Ports & Unofficial Adaptations

OpenSpec ships native/pre-baked configurations for many major tools, reducing the need for community ports. Version 1.8.0 added a vendor-neutral `agents` target, MiniMax Code, and Rovo Dev CLI. Treat this as documented support breadth, not proof of runtime parity.

## Comparison Notes

**vs. GSD:** Both are spec-driven, but they target different workflows. GSD Core uses a five-step project loop and fresh task contexts; OpenSpec organizes targeted brownfield changes around delta specs. Both document broad runtime targets, but parity is unverified. Choose GSD for structured project execution and OpenSpec for lightweight change governance.

**vs. Spec Kit:** Both are spec-driven and multi-tool. Spec Kit produces project-level specifications through a phase-gated workflow and remains pre-1.0 at v0.16.1. OpenSpec uses lightweight delta specs and a change-centric v1.8.0 workflow. Spec Kit emphasizes upfront specification quality; OpenSpec emphasizes proposal approval and ongoing change records.

**vs. Context Engineering:** OpenSpec is a concrete implementation of context engineering principles applied to change management. Change folders are curated context — each one scopes what the AI sees to a single change and its relevant specs, design, and tasks. Delta markers are a form of structured context annotation — they tell the AI not just what to build, but what already exists and how it's being modified. The proposal → approval → apply flow is a context quality gate — ensuring the AI works from reviewed, human-approved context rather than raw prompts. Where context engineering is the underlying practice, OpenSpec is one specific operationalization of it for brownfield spec-driven development.

**vs. Superpowers:** Superpowers is a skill-based methodology that teaches agents *how* to develop. OpenSpec defines *what* changes to make and *why*. Version 1.8.0 also exports to the shared `.agents/skills/` path, so OpenSpec can participate in the skills layer without becoming a skill-based methodology.
