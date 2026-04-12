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
| Current Version    | v6.3.0 (April 10, 2026)      |
| Stars / Popularity | ~44,400 stars · 5,300+ forks · 1,800+ commits |
| Supported Tools    | Claude Code, Cursor, Windsurf; cross-platform agent support in V6 |

## Overview

BMAD is a comprehensive AI-driven agile development framework that simulates an entire software development team using specialized AI agents. Where most AI coding tools produce linear output from a single agent, BMAD provides a suite of named agents — each with distinct roles, commands, and artifact outputs — that guide developers through a structured agile process from analysis to deployment.

The framework addresses the gap between casual AI prompting and production-grade development. It transforms AI coding from trial-and-error into a structured, repeatable workflow with clear phases, quality gates, and role separation. BMAD explicitly positions itself not as a tool that "does the thinking for you" but as expert collaborators guiding structured processes.

## Core Concepts

**Specialized Agent Roles.** BMAD defines distinct agent personas, each with specific responsibilities: John (PM) asks "WHY?" relentlessly to validate the product direction; Winston (Architect) balances pragmatism with innovation; Dev focuses on clean, maintainable implementation; Quinn (QA) handles quality assurance; and additional agents cover UX design, domain analysis, and scrum facilitation. The total roster is 12+ agents.

**Scale-Adaptive Intelligence.** BMAD automatically adjusts planning depth based on project complexity. A bug fix gets a lightweight process; an enterprise system gets the full agile treatment. This prevents the common criticism that structured frameworks are overkill for small tasks.

**Module Ecosystem.** BMAD is built around extensible modules: BMM (Core, 34+ workflows), BMad Builder (BMB, for custom agents and workflows), Test Architect (TEA, risk-based testing), Game Dev Studio (BMGD, for Unity/Unreal/Godot), and Creative Intelligence Suite (CIS, for innovation and design thinking).

**Party Mode.** Multiple agent personas can be brought into a single session to collaborate, enabling cross-functional discussions within one context window.

## How It Works

BMAD operates through four sequential phases, each driven by the appropriate specialist agents:

**Phase 1: Analysis.** The Analyst agent conducts domain research, market research, and technical research. This phase produces a deep understanding of the problem space before any planning begins.

**Phase 2: Planning.** John (PM) drives the creation of product briefs, PRDs (Product Requirements Documents), and UX design documents. The emphasis is on the "WHY" — ensuring that what gets built actually serves users.

**Phase 3: Solutioning.** Winston (Architect) takes over for architecture design, epic and story breakdowns, and readiness checks. This phase ensures the technical approach is sound before implementation starts.

**Phase 4: Implementation.** Dev handles sprint planning, story development, and iteration. Quinn (QA) runs quality assurance. Retrospectives feed learnings back into the process.

All phases operate through slash commands in the AI IDE. Installation is via `npx bmad-method install` (or `npx bmad-method@next install` for the latest). BMAD also provides a **Quick Flow** for smaller projects that compresses the four phases.

The V6 release introduced cross-platform agent team support, a skills architecture for better modularity, and dev loop automation for faster iteration. An AI-powered help system (`/bmad-help`) provides contextual guidance on what to do next.

## Strengths

- **Most comprehensive lifecycle coverage.** 34+ workflows spanning analysis, planning, architecture, implementation, QA, and retrospectives. No other technique in this comparison covers the full SDLC as thoroughly.
- **Scale-adaptive.** Automatically adjusts process weight to project complexity, partially addressing the "overkill for small projects" criticism that applies to enterprise-oriented frameworks.
- **Rich agent ecosystem.** 12+ specialized agents with distinct personalities and expertise areas. The Module Ecosystem (BMB, TEA, BMGD, CIS) extends coverage into testing, game development, and creative work.
- **Strong community.** 44K+ stars, 5,300+ forks, active Discord community, multiple language READMEs (English, Chinese, Vietnamese). Adoption spans solo developers to enterprise teams.
- **Cross-platform support (V6).** While originally agent-agnostic in theory, V6 made cross-platform collaboration a first-class feature.
- **100% free and open source.** No paywalls, no gated content — the full framework is available to all users.

## Limitations

- **Heavy upfront investment.** More time is required for spec generation and planning than lighter approaches like GSD. The four-phase process front-loads significant work before implementation begins.
- **Overwhelming specification volume.** BMAD can generate large amounts of specification documents. For some projects, the review overhead of these artifacts approaches the effort of just writing the code directly.
- **Steep learning curve.** 12+ agents, 34+ workflows, and multiple modules create a substantial surface area to learn. New users may struggle to find the right entry point.
- **May feel heavy for solo developers.** The team simulation — with PM, Architect, UX Designer, Scrum Master — can feel overly ceremonial for a single developer building a small-to-medium project.
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

BMAD is one of the two most popular AI development frameworks (alongside GSD), with 44K+ stars and 5,300+ forks. The community is active on Discord, Medium, and developer blogs. Coverage includes articles on GMO Recruit's blog, Benny Cheung's technical deep-dive, and multiple Medium writeups. The Module Ecosystem extends BMAD into testing (TEA), game development (BMGD), and creative work (CIS). The project maintains documentation at docs.bmad-method.org and offers multilingual READMEs. Installation is streamlined via npx, and the Builder module (BMB) allows users to create custom agents and workflows.

## Comparison Notes

**vs. GSD:** The most natural comparison. Both are popular spec-driven approaches, but they sit at different points on the weight spectrum. GSD uses ~50 Markdown files and a CLI helper to orchestrate parallel execution with fresh contexts; BMAD provides 12+ named agents, 34+ workflows, and four structured phases. A community-sourced summary: GSD is for a "solid build in a few hours," BMAD is for "complex or production-grade" projects. BMAD's upfront investment is higher, but its lifecycle coverage is more comprehensive.

**vs. Squad:** Both use multi-agent orchestration, but with different philosophies. BMAD simulates a full team (PM, Architect, Dev, QA) within a single user's AI session — the agents are personas. Squad creates actual parallel agent instances with persistent memory, shared decision ledgers, and an autonomous work monitor (Ralph). BMAD is richer in structured process; Squad is richer in coordination infrastructure.

**vs. MetaGPT:** Both simulate software company structures with role-based agents. MetaGPT takes an academic/SOPs approach ("Code = SOP(Team)") with a focus on standardized operating procedures. BMAD takes a practitioner/agile approach with scale-adaptive intelligence. MetaGPT is a framework with a Python runtime; BMAD is a set of prompts, workflows, and a CLI. BMAD's community (44K stars) is significantly larger than MetaGPT's, and its workflow coverage is broader.
