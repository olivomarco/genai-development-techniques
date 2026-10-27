# BMAD Method

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Build More Architect Dreams (originally "Breakthrough Method for Agile AI-Driven Development") |
| Category           | Multi-Agent Orchestration      |
| Source              | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) / [docs.bmad-method.org](https://docs.bmad-method.org) |
| Author/Org         | bmad-code-org                 |
| License            | Open source (proprietary trademark on name) |
| First Released     | 2025                          |
| Current Version    | v6.12.4 stable (October 14, 2026); a V7 preview alpha, distributed as installable skills, is also under active development |
| Stars / Popularity | ~54,600 stars · 6,100+ forks |
| Supported Tools    | Claude Code, Cursor, Windsurf, Copilot, Roo Code; MCP Server; Web Bundles for Gemini Gems and ChatGPT Custom GPTs; a Codex plugin marketplace in the V7 preview alpha |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Supported (V6) |
| GitHub Copilot Coding Agent (github.com) | ❌ Not supported — interactive workflow requires human-driven sessions |
| Claude Code | ✅ Primary |
| Cursor | ✅ Primary |
| Windsurf | ✅ Primary |
| OpenAI Codex (CLI) | ⚠️ Official V7 preview alpha via a Codex plugin marketplace, alongside older community/indirect ports — not yet the same maturity as the V6.12 stable line |
| Gemini CLI | ⚠️ Community/indirect — official support is for Gemini Gems Web Bundles, not CLI runtime parity |
| Roo Code | ⚠️ Community — via V6 cross-platform agent support |

## Overview

BMAD is a comprehensive AI-driven agile development framework that simulates an entire software development team using specialized AI agents. Where most AI coding tools produce linear output from a single agent, BMAD provides a suite of named agents — each with distinct roles, commands, and artifact outputs — that guide developers through a structured agile process from analysis to deployment.

The framework addresses the gap between casual AI prompting and production-grade development. It transforms AI coding from trial-and-error into a structured, repeatable workflow with clear phases, quality gates, and role separation. BMAD explicitly positions itself not as a tool that "does the thinking for you" but as expert collaborators guiding structured processes.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Broad lifecycle coverage | ❌ Heavy upfront investment in spec generation and planning |
| ✅ Scale-adaptive — adjusts planning depth to project complexity | ❌ Steep learning curve — many agents, workflows, and modules |
| ✅ Cross-platform support (Claude Code, Cursor, Windsurf, Copilot) | ❌ Can generate overwhelming volumes of specification documents |
| ✅ Rich module ecosystem (BMad Builder, BMad Test Architect, BMad Game Dev Studio, Creative Intelligence Suite) | ❌ Team simulation can feel overly ceremonial for solo developers |
| ✅ 54K+ stars, active Discord community, strong ecosystem | ❌ Proprietary trademark on the BMAD name |
| ✅ 100% free and open source | ❌ Four-phase process front-loads significant work before implementation |

> **In one sentence:** BMAD is the deepest agile role simulation among AI coding frameworks — useful when your project is complex enough to justify having a PM, an architect, and (with the Test Architect module) a dedicated test role challenge every decision before code is written.

## Core Concepts

**Specialized Agent Roles.** The core BMad Method module (BMM) ships five named agent skills: Mary (Analyst) handles market research and requirements elicitation; John (PM) drives PRD creation; Winston (Architect) designs the technical approach; Sally (UX Designer) owns interaction design; and Amelia (Dev) implements stories with test-first discipline. QA is no longer part of this base roster — it now lives in the separate BMad Test Architect module, run by its own agent, Murat.

**Scale-Adaptive Intelligence.** BMAD automatically adjusts planning depth based on project complexity. A bug fix gets a lightweight process; an enterprise system gets the full agile treatment. This prevents the common criticism that structured frameworks are overkill for small tasks.

**Module Ecosystem.** BMAD's official modules are BMad Method (the core), BMad Builder (skill, workflow, and agent authoring), BMad Creative Intelligence Suite (innovation and storytelling), BMad Test Architect (test planning and release decisions, formerly branded TEA), BMad Loop (unattended epic execution), and BMad Game Dev Studio. `bmad-spec` and `bmad-ux` are planning skills inside BMad Method itself, not separate modules.

**Party Mode.** Multiple agent personas can be brought into a single session to collaborate, enabling cross-functional discussions within one context window.

## How It Works

BMAD operates through four sequential phases, each driven by the appropriate specialist agents:

**Phase 1: Analysis.** The Analyst agent conducts domain research, market research, and technical research. This phase produces a deep understanding of the problem space before any planning begins.

**Phase 2: Planning.** John (PM) drives the creation of product briefs, PRDs (Product Requirements Documents), and UX design documents. The emphasis is on the "WHY" — ensuring that what gets built actually serves users.

**Phase 3: Solutioning.** Winston (Architect) takes over for architecture design, epic and story breakdowns, and readiness checks. This phase ensures the technical approach is sound before implementation starts.

**Phase 4: Implementation.** Amelia (Dev) handles sprint planning, story development, and iteration. Teams that add the BMad Test Architect module get Murat for quality assurance. Retrospectives feed learnings back into the process.

All phases operate through slash commands in the AI IDE. The v6.12 stable line installs with `npx bmad-method install` and now takes bug fixes only — new feature work has moved to a V7 preview alpha. V7 drops the npm-only installer in favor of the Agent Skills format: `npx skills add bmad-code-org/BMAD-METHOD --skill '*'` installs the full method as skills, and Claude Code and Codex users can instead add a plugin marketplace (`bmad-code-org/bmad-plugins`) and ask the `bmad` skill to run `bmad setup`. This is BMAD's clearest move toward skills as managed, installable packages rather than a single framework bundle — but V7 is pre-beta, and its install path, skill names, and docs are still changing. BMAD also provides a lighter **Quick Flow** for smaller projects that compresses the full planning sequence.

BMAD's module line has also reorganized: `bmad-automator` is retired in favor of the Python-orchestrated `bmad-loop` (a separate repository, currently in early open beta, that runs BMAD stories unattended without an LLM in its control loop), while the in-method `bmad-dev-auto` skill is deprecated and forwards to `bmad-build-auto` for a single unattended iteration. Gemini and ChatGPT access remains through Web Bundles — a planning-only integration, not CLI or runtime parity with Claude Code, Cursor, or Copilot.

## Strengths

- **Broad lifecycle coverage.** BMAD spans analysis, planning, architecture, implementation, QA, and retrospectives through five named BMM agents (Mary, John, Winston, Sally, Amelia) plus Murat in the separate Test Architect module.
- **Scale-adaptive.** Automatically adjusts process weight to project complexity, partially addressing the "overkill for small projects" criticism that applies to enterprise-oriented frameworks.
- **Rich agent ecosystem.** Specialized agents and modules extend coverage into testing, game development, creative work, specification, UX, and unattended iteration.
- **Strong community.** Roughly 54.6K stars, 6.1K forks, an active Discord community, and multilingual READMEs.
- **Cross-platform support (V6).** While originally agent-agnostic in theory, V6 made cross-platform collaboration a first-class feature.
- **100% free and open source.** No paywalls, no gated content — the full framework is available to all users.

## Limitations

- **Heavy upfront investment.** More time is required for spec generation and planning than lighter approaches like GSD. The four-phase process front-loads significant work before implementation begins.
- **Overwhelming specification volume.** BMAD can generate large amounts of specification documents. For some projects, the review overhead of these artifacts approaches the effort of just writing the code directly.
- **Steep learning curve.** Numerous agents, workflows, and modules create a substantial surface area to learn. New users may struggle to find the right entry point.
- **May feel heavy for solo developers.** The team simulation — PM, Architect, UX Designer, and more if you add Test Architect — can feel overly ceremonial for a single developer building a small-to-medium project.
- **Trademark restrictions.** While the code is open source, the BMAD name carries a proprietary trademark, which may affect derivative works or competing distributions.

## Best For

- **Medium-to-large projects requiring production-grade structure** — projects where cutting corners in planning or architecture will create costly downstream problems.
- **Solo developers who want team-like discipline.** BMAD's agent roles enforce the kind of cross-functional review (PM challenge, architecture review, QA) that normally requires multiple people.
- **Projects with complex domain requirements.** The Analysis phase (domain research, market research, technical research) is valuable when the problem space itself is poorly understood.
- **Teams adopting agile practices with AI.** BMAD maps directly to agile workflows (sprints, stories, retrospectives), making it a natural fit for teams already using agile methodologies.

## Not Ideal For

- **Quick bug fixes or small scripts.** Even with Scale-Adaptive Intelligence and Quick Flow, BMAD's overhead is hard to justify for trivial tasks.
- **Projects where speed-to-first-code matters more than specification quality.** If the goal is a working prototype in hours, GSD's lighter approach or direct prompting may be more appropriate.
- **Environments requiring formal governance and audit trails.** BMAD focuses on development process, not enterprise compliance. HVE's constraint-based governance is designed for regulated environments.
- **Teams locked in to a single AI coding tool.** While V6 improved cross-platform support, the depth of integration still varies by tool.

## Community & Ecosystem

BMAD had roughly 54.6K stars and 6.1K forks on October 27, 2026. The module ecosystem extends into testing, game development, creative work, specification, UX planning, and unattended iteration through the separate `bmad-loop` project. The project maintains documentation at docs.bmad-method.org and offers multilingual READMEs. Official multi-platform support and Web Bundles have different scopes; Gemini CLI runtime support should still be treated as unavailable, and Codex support sits in the V7 preview alpha rather than the stable v6.12 line.

## Comparison Notes

**vs. GSD:** Both structure AI-assisted development, but they sit at different points on the weight spectrum. GSD Core uses a five-step project loop with fresh task contexts; BMAD provides specialized roles, modules, and four structured phases. BMAD's upfront investment is higher, but its lifecycle coverage is broader.

**vs. Squad:** Both use multi-agent orchestration, but with different philosophies. BMAD simulates a full team (PM, Architect, Dev, and QA when the Test Architect module is installed) within a single user's AI session — the agents are personas. Squad creates actual parallel agent instances with persistent memory, shared decision ledgers, and an autonomous work monitor (Ralph). BMAD is richer in structured process; Squad is richer in coordination infrastructure.

**vs. Superpowers:** BMAD simulates a full agile team through specialized roles and structured phases; Superpowers enhances individual developer effectiveness through mandatory behavioral skills. BMAD's strength is process simulation and modular lifecycle coverage. Superpowers' strength is process internalization through TDD, debugging, and review skills.

**vs. Ralph:** Ralph is a minimal autonomous loop. BMAD's unattended options split in two: `bmad-build-auto` runs one iteration inside the method's own artifacts and roles, while the separate `bmad-loop` project runs full stories unattended through a deterministic Python control loop — no LLM decides what happens next, only what gets written. Choose Ralph for minimalism and backend freedom; choose `bmad-loop` when you want unattended, auditable work inside BMAD's artifacts, and accept that it is still in early open beta.
