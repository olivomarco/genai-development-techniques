# Spec Kit

## At a glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | GitHub Spec Kit (CLI: "Specify") |
| Category           | Spec-Driven Development       |
| Source              | [github/spec-kit](https://github.com/github/spec-kit) |
| Author/Org         | GitHub (Den Delimarsky, key contributor) |
| License            | Open source (GitHub)          |
| First Released     | 2025                          |
| Current Version    | v1.2.3 (October 22, 2026); crossed 1.0 at v1.0.0 on August 21, 2026 |
| Stars / Popularity | ~143,100 stars · 12,800+ forks |
| Supported Tools    | GitHub Copilot, Claude Code, Gemini CLI, Codex CLI, Cursor, Windsurf, and 30+ more integrations |

## Compatible coding agents

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

Spec Kit is GitHub's open-source toolkit for giving AI coding agents structured processes, reusable templates, and documented outcomes. It shipped originally as a single spec-driven workflow; at v1.0.0 it reorganized around three independent entry points plus a set of composable mechanisms for building your own process.

Spec Kit asks developers to describe, review, and refine requirements before implementation. The agent then builds from the specification rather than inferring requirements from an initial prompt.

Since v1.0.0, Spec Kit also ships bug fixing and idea assessment as separate installable extensions, and exposes extensions, presets, workflows, bundles, and catalogs so teams can adapt or replace the default process instead of being locked into one path.

## Pros & cons at a glance

| Pros | Cons |
|------|------|
| ✅ Maintained by GitHub | ❌ Three processes plus a catalog system raise the learning curve versus a single linear workflow |
| ✅ 30+ integrations including Copilot, Claude Code, Gemini CLI, Cursor | ❌ Older reviews (e.g., Birgitta Böckeler's, predating the 1.0 restructuring) found review overhead comparable to coding directly; not reverified against the current toolkit |
| ✅ Minimal footprint — Markdown files and a scaffolding CLI | ❌ No multi-agent orchestration — a specification and process toolkit, not an execution framework |
| ✅ Specification quality checks (`/speckit-analyze`, `/speckit-checklist`) plus a `/speckit-converge` loop | ❌ Generates many Markdown files that need review and maintenance |
| ✅ Mature extension/preset/bundle catalog with community and private sources | ❌ Catalog listings are not audited or endorsed — review community source before installing |
| ✅ Version-controlled specs as part of normal Git workflow | ❌ Agent may still ignore spec instructions — no enforcement mechanism |

> Spec Kit provides separate processes for spec-driven feature work, bug fixing, and idea assessment, with extensions and presets for adapting each process.

## Core concepts

**Three Independent Processes.** Since v1.0.0, Spec Kit ships three entry points instead of one: **Spec-Driven Development** (spec → plan → tasks → implement → converge) for building a feature, **Bug fixing** (assess → fix → test) for diagnosing and repairing broken behavior, and **Idea assessment** (intake → research → define → shape → decide) for deciding whether an idea is worth building. SDD ships in core; bug fixing and assessment are extensions you install with `specify extension add bug` or `specify extension add assess` when needed. None of the three is a mandatory phase gate for the others.

**Specifications as Source of Truth.** SDD still starts with a `spec.md` file that captures project goals and requirements. This spec is version-controlled Markdown — reviewable, diffable, and auditable like any other source file.

**Convergence.** Run `/speckit-implement` and `/speckit-converge` in a loop until the latter reports `Converged`. Converge checks the implementation against the spec, a step the original specify → plan → tasks → implement flow lacked.

**Constitution.** An optional `constitution.md` defines project principles or standards (coding conventions, architectural constraints, quality requirements) that the AI must respect during implementation. This is Spec Kit's mechanism for persistent governance, created once per project with `/speckit-constitution`.

**Composable Mechanisms.** Beyond the three built-in processes, Spec Kit exposes extensions (add commands or whole processes), presets (adapt templates, commands, or terminology, including for regulatory traceability), workflows and workflow overlays (automate prompts, commands, and gates without forking), and bundles (package a curated setup for a role or team). Catalogs — community or private — distribute all of these; catalog listings are not audits or endorsements, so review source before installing.

**Agent Agnosticism.** Spec Kit targets 30+ AI coding tool integrations through a single `--integration <key>` flag at project init, and lets you switch or add integrations later. Commands are invoked as "skills" in the agent's chat (GitHub Copilot's default syntax), hyphenated commands, `$` commands, or another native form depending on the agent — not run in the terminal.

## How it works

Spec Kit organizes projects around Markdown files in a `.specify` directory: `spec.md` (goals and requirements), `plan.md` (technical approach), `tasks/` (work units derived from the plan), and an optional `constitution.md` (project principles). Bug fixing and assessment extensions add their own artifact directories (`.specify/bugs/<slug>/`, `.specify/assessments/<slug>/`).

The default SDD flow, shown here with GitHub Copilot's skill syntax:

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `/speckit-constitution` | Define project constitutional guardrails (once per project) |
| 2 | `/speckit-specify` | Build a specification from user prompt |
| 3 | `/speckit-clarify` | Ask clarification questions on the spec |
| 4 | `/speckit-plan` | Create a technical plan for the specification |
| 5 | `/speckit-tasks` | Break plan into individual tasks for the AI |
| 6 | `/speckit-analyze` | Analyze spec, plan, and tasks for inconsistencies |
| 7 | `/speckit-checklist` | Create "unit tests for English" for the spec |
| 8 | `/speckit-implement` | Implement based on all combined artifacts |
| 9 | `/speckit-converge` | Check implementation against spec; repeat with implement until `Converged` |

Bug fixing runs `/speckit-bug-assess`, `/speckit-bug-fix`, then `/speckit-bug-test`, ending in a `verified`, `partial`, or `failed` verdict. Idea assessment runs intake → research → define → shape → decide, ending in `go`, `needs-clarification`, or `kill`; a `go` decision hands its summary to `/speckit-specify` to start SDD.

The CLI tool (`specify`) handles project scaffolding and integration management (`specify integration install/switch/uninstall`). Installation is `uv tool install specify-cli` (pin a release with `--from git+https://github.com/github/spec-kit.git@v1.2.3` if you need a specific version), then `specify init my-project --integration copilot`.

## Strengths

- **GitHub-backed.** Institutional support from GitHub — featured on the GitHub Blog, maintained by GitHub engineers, and covered on GitHub's "Open Source Friday" series, including a dedicated episode on the 1.0 restructuring (October 16, 2026).
- **Agent-agnostic design.** 30+ integrations, from GitHub Copilot and Claude Code to Gemini CLI, Cursor, Windsurf, and Codex CLI. Support lists change quickly, so validate the depth of the integration you plan to use.
- **Small project footprint.** A scaffolding CLI generates Markdown prompts and artifacts in your repo. Spec Kit does not add its own agent execution runtime.
- **Mature extension and catalog ecosystem.** Extensions, presets, workflows, and bundles are discoverable via `specify extension search`, `specify preset search`, `specify workflow search`, and `specify bundle search`, with both community and private catalog support. Recent releases focused on hardening this system — rejecting malformed catalog entries, confining workflow cache writes, and validating integration descriptors.
- **Specification quality checks plus convergence.** `/speckit-analyze` checks specs, plans, and tasks for inconsistencies; `/speckit-checklist` creates "unit tests for English"; `/speckit-converge` verifies the implementation actually matches the spec instead of stopping at `/speckit-implement`.
- **Version-controlled specifications.** All artifacts are Markdown in the repo, making them part of the normal Git workflow — PRs, code review, blame, history.
- **Stable since 1.0.** Spec Kit crossed 1.0.0 on August 21, 2026, after a year of development. The project's own release notes argue version-number stability matters less now that agents can apply migration diffs directly — treat that as the maintainers' framing, not an external guarantee.

## Limitations

- **More moving parts than a single workflow.** Three processes (SDD, bug fixing, idea assessment) plus extensions, presets, workflows, and bundles raise the learning curve compared with a single linear spec → plan → tasks → implement path. Teams that only need SDD can ignore the rest, but the capability surface is larger than before.
- **Review overhead is undocumented post-restructuring.** Earlier reviews (e.g., Birgitta Böckeler's, predating the 1.0 toolkit) found reviewing generated specification files comparable in time to coding directly. That assessment predates the three-process model and convergence loop, so treat it as historical context, not a current measurement.
- **No multi-agent orchestration.** Spec Kit is a specification and process toolkit, not an execution framework. It doesn't spawn parallel agents, manage context windows, or coordinate work across multiple AI instances.
- **Documentation overhead.** The `.specify` directory accumulates spec, plan, task, checklist, bug, and assessment artifacts that need review and maintenance.
- **Catalog listings aren't vetted.** Community catalogs are real and actively maintained, but inclusion is not an audit or endorsement. Review third-party extension and preset source before installing.

## Best for

- **Teams working across multiple AI tools.** If the team uses Copilot, Claude Code, and Gemini CLI in different contexts, Spec Kit provides a consistent specification layer and integration-switching across all of them.
- **Projects where spec quality matters more than speed.** Regulated environments, contractual work, or projects where ambiguous requirements have historically caused costly errors — presets can enforce regulatory traceability on top of the base workflow.
- **Teams that also need bug fixing and idea-assessment processes.** Rather than adopting SDD for everything, you can install only the extension that matches the job: feature work, a bug, or a go/no-go decision.
- **Organizations already invested in the GitHub ecosystem.** Deep GitHub integration, official backing, and familiar tooling (Markdown, CLI, Git) reduce adoption friction.

## Not ideal for

- **Rapid prototyping or exploratory coding.** The spec → plan → tasks → implement → converge flow adds review overhead that slows down iteration when the goal is to see something running quickly.
- **Projects needing execution orchestration.** Spec Kit handles specification, planning, and process structure, not execution. It doesn't manage parallel agents, context windows, or work queues. Pair it with GSD or Squad for execution.
- **Solo developers on small tasks.** The specification overhead is hard to justify for tasks where the requirement is already clear and the implementation is straightforward.

## Community & ecosystem

Spec Kit crossed 1.0.0 on August 21, 2026, after roughly a year as "an experiment, not a product." The restructuring split the single workflow into SDD core plus bug-fixing and idea-assessment extensions, with catalogs for extensions, presets, workflows, and bundles. GitHub's "Open Source Friday" covered the toolkit on October 16, 2026. At the October 27 observation, v1.2.3 had roughly 143,100 stars and 12,800 forks. Releases v1.2.0–v1.2.3 focused on catalog correctness, workflow fixes, and documentation rather than new features.

## Community ports & unofficial adaptations

Spec Kit's catalog infrastructure supports community extensions, presets, and bundles directly — `specify extension search` and related commands query both community and private catalogs. Recent community catalog additions include Linear Weave, Applied Epistemic Engineering, DocGuard (CDD enforcement), Evaluator Contract, Intake Sequencing Governance, Inventory Alignment, Spec Inventory, and AgentDocx, among others, alongside ongoing updates to existing extensions like Security Review and MAQA. Catalog listings are not audits; review source before installing or running community components.

## Comparison notes

**vs. GSD:** Both are spec-driven but at different scopes. GSD Core provides a complete Discuss → Plan → Execute → Verify → Ship loop. Spec Kit now covers specification, planning, bug fixing, and idea assessment as separate processes, leaving execution to the selected AI tool. Both target many runtimes; published target lists do not prove identical feature depth.

**vs. OpenSpec:** Both are spec-driven and agent-agnostic. OpenSpec is lighter and change-centric, built for brownfield work with delta specs (ADDED/MODIFIED/REMOVED) and a propose → apply → archive loop. Spec Kit is heavier, with three separate processes and a full extension/preset/bundle/catalog system for customizing or replacing any of them. Both are stable, non-experimental releases as of October 2026 (OpenSpec v1.15.0, Spec Kit v1.2.3).

**vs. BMAD:** BMAD covers the full development lifecycle with specialized roles and modular workflows. Spec Kit's SDD process covers specification, planning, and convergence; bug fixing and idea assessment are separate installable processes rather than roles. BMAD is heavier in process and agent complexity; Spec Kit is lighter and more modular per process.

**vs. Context Engineering (Practice):** Spec Kit applies context engineering at the specification layer. Version-controlled specs, plans, constitutions, and task breakdowns supply requirements and constraints to the agent.

**vs. the managed-skills layer:** Spec Kit is a process framework that delivers some commands as skills. Since v1.0.0, GitHub Copilot invokes them with syntax such as `/speckit-specify`, and the Codex CLI integration installs skills into `.agents/skills/` with `--ai-skills`. These commands implement Spec Kit's processes. They are not general-purpose capabilities selected independently from a library such as `mattpocock/skills`.

**vs. Superpowers:** Both take a structured approach to AI-assisted development, but at different layers. Spec Kit focuses on process structure across three entry points (build, fix, assess) — getting the requirements or diagnosis right before acting. Superpowers focuses on the implementation methodology — teaching the agent *how* to build through composable skills (TDD, code review, debugging). Spec Kit is agent-agnostic across 30+ integrations; Superpowers is a complete development workflow supporting six specific tools. They're complementary: Spec Kit could define what to build or fix, Superpowers could enforce how to build it.
