# Spec Kit

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | GitHub Spec Kit (CLI: "Specify") |
| Category           | Spec-Driven Development       |
| Source              | [github/spec-kit](https://github.com/github/spec-kit) |
| Author/Org         | GitHub (Den Delimarsky, key contributor) |
| License            | Open source (GitHub)          |
| First Released     | 2025                          |
| Current Version    | v0.6.2 (April 2026)          |
| Stars / Popularity | 87.8K+ stars; broad community adoption |
| Supported Tools    | GitHub Copilot, Claude Code, Gemini CLI, Codex CLI, Cursor, Windsurf, and 20+ more |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Supported — pre-baked prompts included |
| GitHub Copilot Coding Agent (github.com) | ⚠️ Partial — spec files are readable but the workflow is interactive |
| Claude Code | ✅ Supported — pre-baked prompts included |
| Cursor | ✅ Supported — pre-baked prompts included |
| Windsurf | ✅ Supported — pre-baked prompts included |
| Gemini CLI | ✅ Supported — pre-baked prompts included |
| OpenAI Codex (CLI) | ✅ Supported — requires `--ai-skills`; installs skills into `.agents/skills/` |
| Roo Code | ✅ Supported — pre-baked prompts included |

## Overview

Spec Kit is GitHub's official open-source toolkit for spec-driven development (SDD). It provides a structured process for describing software projects in a way AI coding tools can interpret — bridging the gap between human intent and AI-generated code through explicit specifications written before code is written.

The core problem Spec Kit addresses is what might be called "vibes-based development" — the tendency for developers to jump straight into prompting an AI without clearly specifying what they want, then spending time correcting the AI's assumptions. Spec Kit inserts a specification layer between intent and implementation: you describe what you want, review and refine that description, then let the AI build from an explicit spec rather than an ambiguous prompt.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ GitHub-backed — institutional support and credibility | ❌ Still experimental (v0.6.0) — API and workflow may change |
| ✅ Truly agent-agnostic — works with Copilot, Claude Code, Gemini CLI, Cursor | ❌ Significant review overhead — Birgitta Böckeler noted it was comparable to just coding directly |
| ✅ Minimal footprint — Markdown files and a scaffolding CLI | ❌ One opinionated workflow — may not fit all task sizes |
| ✅ Specification quality checks (analyze, checklist commands) | ❌ No multi-agent orchestration — specification toolkit, not execution framework |
| ✅ Growing extension ecosystem (worktree isolation, git, diagrams) | ❌ Generates many Markdown files that need review and maintenance |
| ✅ Version-controlled specs as part of normal Git workflow | ❌ Agent may still ignore spec instructions — no enforcement mechanism |

> **In one sentence:** Spec Kit is GitHub's disciplined answer to "vibes-based development" — lightweight, agent-agnostic, and focused on getting the spec right before building, but still finding its footing at v0.6.0.

## Core Concepts

**Specifications as Source of Truth.** Everything starts with a `spec.md` file that captures project goals and requirements. This spec is version-controlled Markdown — reviewable, diffable, and auditable like any other source file.

**Progressive Refinement.** Spec Kit's workflow moves from broad intent to specific tasks through a series of refinement steps: specify → clarify → plan → tasks. Each step produces a Markdown artifact that can be reviewed before proceeding.

**Constitution.** An optional `constitution.md` defines project principles or standards (coding conventions, architectural constraints, quality requirements) that the AI must respect during implementation. This is Spec Kit's mechanism for persistent governance.

**Agent Agnosticism.** Unlike GSD (Claude Code-native) or Squad (Copilot-native), Spec Kit is designed to work across AI coding tools. The `specify` CLI scaffolds projects with pre-baked prompts for each supported agent.

## How It Works

Spec Kit organizes projects around Markdown files in a `.specify` directory:

- **spec.md** — Project goals and requirements
- **plan.md** — Technical approach and architecture
- **tasks/** — Individual work units derived from the plan
- **constitution.md** (optional) — Project principles and guardrails

The workflow operates through slash commands:

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `/speckit.constitution` | Define project constitutional guardrails |
| 2 | `/speckit.specify` | Build a specification from user prompt |
| 3 | `/speckit.clarify` | Ask clarification questions on the spec |
| 4 | `/speckit.plan` | Create a technical plan for the specification |
| 5 | `/speckit.tasks` | Break plan into individual tasks for the AI |
| 6 | `/speckit.analyze` | Analyze spec, plan, and tasks for inconsistencies |
| 7 | `/speckit.checklist` | Create "unit tests for English" for the spec |
| 8 | `/speckit.implement` | Implement based on all combined artifacts |

The CLI tool (`specify`) handles project scaffolding, generating the `.specify` directory structure with pre-baked prompts configured for the user's chosen AI tool. Installation is via `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.6.0`.

## Strengths

- **GitHub-backed.** Institutional support from GitHub — featured on the GitHub Blog, maintained by GitHub engineers. This provides a level of credibility and continuity that community projects may lack.
- **Truly agent-agnostic.** Works with GitHub Copilot, Claude Code, Gemini CLI, Cursor, and Windsurf. This is the broadest tool compatibility among spec-driven approaches in this comparison.
- **Minimal footprint.** The system revolves around prompts and a scaffolding CLI. No proprietary runtime, no heavy dependencies, no agent framework. The entire system is Markdown files in your repo.
- **Growing extension ecosystem.** Community extensions include Bugfix Workflow, Worktree Isolation, Git extension, Spec Diagram, Branch Convention, memorylint, and others — indicating active third-party development.
- **Specification quality checks.** The `/speckit.analyze` command checks specs, plans, and tasks for inconsistencies. The `/speckit.checklist` command creates "unit tests for English" — testable assertions about what the spec says.
- **Version-controlled specifications.** All artifacts are Markdown in the repo, making them part of the normal Git workflow — PRs, code review, blame, history.

## Limitations

- **Still experimental.** Spec Kit is explicitly labeled an experiment, not a product. At v0.6.2 (April 2026), it is the earliest-stage technique in this comparison.
- **Significant review overhead.** Martin Fowler's review (martinfowler.com) noted that the time spent reviewing generated specification files was comparable to the time spent just coding directly. The specs themselves become artifacts that need quality assurance.
- **One opinionated workflow.** Spec Kit prescribes a specific spec → plan → tasks → implement path. Real development doesn't always follow this sequence — bug fixes, exploratory prototyping, and iterative design may not fit cleanly.
- **No multi-agent orchestration.** Spec Kit is a specification toolkit, not an execution framework. It doesn't spawn parallel agents, manage context windows, or coordinate work across multiple AI instances.
- **Generates a lot of Markdown.** The `.specify` directory accumulates spec files, plan files, task files, checklists, and analysis output. For large projects, this documentation overhead is non-trivial.

## Best For

- **Teams working across multiple AI tools.** If the team uses Copilot, Claude Code, and Gemini CLI in different contexts, Spec Kit provides a consistent specification layer across all of them.
- **Projects where spec quality matters more than speed.** Regulated environments, contractual work, or projects where ambiguous requirements have historically caused costly errors.
- **Developers entering spec-driven development for the first time.** Spec Kit's focus on the specification phase (rather than the full lifecycle) makes it a contained introduction to SDD without the overhead of learning a complete framework.
- **Organizations already invested in the GitHub ecosystem.** Deep GitHub integration, official backing, and familiar tooling (Markdown, CLI, Git) reduce adoption friction.

## Not Ideal For

- **Rapid prototyping or exploratory coding.** The spec → plan → tasks → implement flow adds review overhead that slows down iteration when the goal is to see something running quickly.
- **Projects needing execution orchestration.** Spec Kit handles specification and planning, not execution. It doesn't manage parallel agents, context windows, or work queues. Pair it with GSD or Squad for execution.
- **Production environments needing stability guarantees.** At v0.6.2, Spec Kit is pre-1.0 and explicitly experimental. API and workflow changes are expected.
- **Solo developers on small tasks.** The specification overhead is hard to justify for tasks where the requirement is already clear and the implementation is straightforward.

## Community & Ecosystem

Spec Kit benefits from GitHub's institutional backing, including official GitHub Blog posts and advocacy from Den Delimarsky. External coverage includes Martin Fowler's analysis (martinfowler.com), writeups on Tessl, IntuitionLabs, and Level Up GitConnected. IBM released its own `iac-spec-kit` for infrastructure-as-code, indicating the SDD approach is gaining traction beyond GitHub's implementation. The community extensions ecosystem is growing, with contributions for worktree isolation, Git integration, spec diagrams, and linting tools. Monthly newsletters track progress and community contributions. However, as a v0.6.2 experiment, the ecosystem is young relative to GSD (51K stars) or BMAD (44K stars).

## Comparison Notes

**vs. GSD:** Both are spec-driven but at different scopes. GSD provides a complete lifecycle (spec → plan → execute → verify → release) with multi-agent orchestration and context engineering. Spec Kit focuses on the specification and planning phases, leaving execution to whatever AI tool the user prefers. GSD is Claude Code-native; Spec Kit is agent-agnostic. GSD is more mature (v1.35.0 vs. v0.6.2) and has a larger community.

**vs. BMAD:** BMAD covers the full development lifecycle with 12+ specialized agents and 34+ workflows. Spec Kit covers specification and planning only — it is deliberately narrow. BMAD is heavier in process and agent complexity; Spec Kit is lighter and more focused. BMAD works across AI tools but has agent-specific integrations; Spec Kit's agent-agnosticism is a core design goal.

**vs. Context Engineering (Practice):** Spec Kit is a concrete tool implementing context engineering principles at the specification layer. Spec files, plans, constitutions, and task breakdowns are all forms of curated context that structure what the AI receives. Where context engineering is the umbrella practice, Spec Kit is a specific tool for the "specification as context" subset — version-controlled documents that pre-load the AI's context with requirements and constraints.
