# Squad

## At a Glance
| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Squad                         |
| Category           | Multi-Agent Orchestration      |
| Source              | [bradygaster/squad](https://github.com/bradygaster/squad) / [bradygaster.github.io/squad](https://bradygaster.github.io/squad/) |
| Author/Org         | Brady Gaster (Microsoft)      |
| License            | MIT                           |
| First Released     | 2025                          |
| Current Version    | v0.8.21 (March 2026)         |
| Stars / Popularity | Active development · 1,454+ commits · Microsoft backing |
| Supported Tools    | GitHub Copilot (CLI and VS Code) |

## Overview

Squad is an AI agent orchestration system that creates a persistent, coordinated team of AI agents working within your repository. Created by Brady Gaster at Microsoft, it shifts AI-assisted development from "one brain talking to one brain" to a multi-agent architecture where specialized agents — frontend, backend, testing, documentation — work in parallel with explicit roles, clear boundaries, and written coordination.

The system applies Conway's Law to AI development: rather than trying to produce better output from a single agent through better prompts, Squad changes the structure. It introduces role separation, shared memory, decision tracking, and autonomous work monitoring. The agents don't just execute tasks — they accumulate knowledge, follow team decisions, and coordinate through a shared repository-based state.

## Core Concepts

**Coordinator Pattern.** A central Coordinator orchestrates all work. It receives user requests, routes them to the appropriate agent(s), manages parallel fan-out, and synthesizes results. The Coordinator never does domain work itself — it delegates.

**Persistent Agent Identity.** Each agent has a charter (`charter.md`) defining its role and boundaries, and a personal history (`history.md`) where it accumulates learnings. These files live in the repo and persist across sessions, giving agents continuity that ephemeral AI sessions lack.

**Decisions-as-Memory.** A shared `decisions.md` file acts as the team's collective brain. When an agent makes a decision that affects others (architecture choices, naming conventions, library selections), it gets recorded here. All agents read this file at spawn time, ensuring consistency.

**Casting System.** Agents receive character names drawn from fictional universes — an easter egg naming convention that makes the team feel distinct without introducing role-play or character behavior. Names are persistent identifiers, not personas.

**Ralph (Work Monitor).** An autonomous agent that continuously scans GitHub for issues, PRs needing review, CI failures, and untriaged work. Ralph keeps the pipeline moving by routing work to the right agents without waiting for human direction.

## How It Works

Squad creates a `.squad/` directory in the repository containing the team's state:

```
.squad/
├── team.md              # Agent roster with roles
├── routing.md           # Work assignment rules
├── decisions.md         # Shared decision ledger
├── ceremonies.md        # Structured team meetings
├── agents/
│   ├── {name}/charter.md   # Agent identity and boundaries
│   └── {name}/history.md   # Agent's accumulated knowledge
├── orchestration-log/   # Who did what, when, and why
└── log/                 # Session logs
```

**Team Assembly.** Squad assembles a team based on the project description — typically Lead, Frontend Dev, Backend Dev, Tester, and Scribe (the silent logger). The Coordinator handles routing, model selection, and parallel orchestration.

**Work Routing.** When a user gives a task, the Coordinator decomposes it, identifies which agents can start immediately, and spawns them in parallel. A tester can write test cases from requirements while the implementer builds the feature. Background agents report results; the Coordinator synthesizes and launches follow-up work.

**GitHub Integration.** Squad manages the full issue → branch → PR → merge lifecycle. Agents create branches (`squad/{issue-number}-{slug}`), make commits referencing issues, push, and open PRs via the GitHub CLI. Ralph monitors the queue and keeps work moving.

**SDK-First Mode (v0.8.21).** Squad offers type-safe team configuration through builder functions (`defineTeam()`, `defineAgent()`, `defineRouting()`) for teams that prefer code over Markdown configuration.

Additional features include **Ceremonies** (structured team meetings — design reviews, retrospectives, standups), **Worktree Support** (git worktrees for isolated issue work), **PRD Mode** (ingest product requirement documents as work source), **Human Team Members** (mix AI and human participants), and **Per-Agent Model Selection** (a multi-layer system for optimizing cost and quality per task).

## Strengths

- **True parallel orchestration.** Multiple agents work simultaneously on different parts of a problem, each in their own context. This is not sequential delegation — it is concurrent fan-out with dependency-aware scheduling.
- **Persistent memory across sessions.** Agent histories, team decisions, and orchestration logs persist in the repository. An agent picking up an issue today has access to what the team decided and learned yesterday. This is unique among the techniques compared here.
- **Autonomous work management (Ralph).** Ralph continuously scans for work — untriaged issues, CI failures, stalled PRs, approved merges — and routes it without human prompting. This enables a degree of autonomy that other frameworks leave to the user.
- **Full GitHub lifecycle integration.** Issues, branches, PRs, and merges are part of the core workflow, not an afterthought. Squad agents interact with GitHub natively via the CLI.
- **Reviewer rejection protocol.** Rejected work must be revised by a *different* agent — the original author is locked out. This enforces genuine review rather than rubber-stamping.
- **Extensible team composition.** Human team members, the GitHub Copilot coding agent (@copilot), and new AI agents can be added to the roster at any time.

## Limitations

- **Copilot-only.** Squad is tightly coupled to the GitHub Copilot ecosystem — CLI and VS Code. It does not work with Claude Code, Cursor, or other AI coding tools directly.
- **Still pre-1.0.** At v0.8.21 (March 2026), the API and workflow structure may still change. Early adopters should expect iteration.
- **Substantial directory overhead.** The `.squad/` directory contains team files, agent charters, histories, decision ledgers, orchestration logs, casting state, and session logs. For small projects, this infrastructure footprint is disproportionate.
- **Requires GitHub authentication.** The full feature set (Ralph, issue routing, PR lifecycle) depends on GitHub CLI authentication. Without it, Squad loses its autonomous capabilities.
- **Node.js dependency.** The CLI requires npm and Node.js, which may be a friction point for teams not already in the Node ecosystem.

## Best For

- **Teams building with GitHub Copilot** who want structured multi-agent orchestration with persistent memory and autonomous work management.
- **Projects managed through GitHub Issues and PRs.** Squad's lifecycle integration (issue → branch → PR → merge) is most valuable when GitHub is the central project management platform.
- **Medium-to-large projects with multiple concerns.** Projects where frontend, backend, testing, and documentation are all active simultaneously benefit from Squad's parallel agent model.
- **Teams that want autonomous background work.** Ralph's continuous monitoring and work routing is valuable for teams that want their AI agents to pick up work proactively, not just when prompted.

## Not Ideal For

- **Non-Copilot environments.** If the team uses Claude Code, Cursor, or another AI tool as their primary agent, Squad's Copilot dependency is a hard blocker.
- **Small, quick projects.** The `.squad/` directory structure, team assembly, and routing infrastructure are overkill for a weekend project or quick script.
- **Solo developers without GitHub Issues.** Squad's strengths — parallel agents, work routing, Ralph — assume a project management workflow centered on GitHub. Without issues and PRs, much of Squad's value is unused.
- **Teams needing enterprise governance.** Squad has reviewer protocols but lacks the formal constraint enforcement, policy-as-code, and audit trail capabilities of HVE.

## Community & Ecosystem

Squad is backed by Brady Gaster at Microsoft, with contributions from Jeffrey T. Fritz, Shayne Boyer, and others. It has been featured in YouTube videos, LinkedIn posts with significant engagement, and a detailed blog post by thomy.tech ("My First Coding Agent Fleet with Enterprise Tooling"). Microsoft teams have used it internally for demo scripts, QA systems, and Minecraft plugins. The project offers a CLI (17 commands), SDK with builder functions, documentation site, and workshop materials. While Squad's community is smaller than GSD (51K stars) or BMAD (44K stars) in raw GitHub metrics, its Microsoft backing and active development (1,454+ commits) provide institutional continuity.

## Comparison Notes

**vs. BMAD:** Both use multi-agent architectures, but the implementation is fundamentally different. BMAD simulates a team through agent personas within a single user's AI session — the agents are prompts with different roles. Squad creates actual parallel agent instances with persistent memory, shared decision ledgers, and autonomous work monitoring via Ralph. BMAD is richer in structured agile process (34+ workflows, four phases); Squad is richer in coordination infrastructure (persistent state, work queues, GitHub lifecycle).

**vs. GSD:** Different paradigms solving different problems. GSD is spec-driven, focused on context engineering and parallel task execution within a structured lifecycle. Squad is orchestration-focused, managing a persistent team with roles, memory, and autonomous work routing. GSD is lighter and Claude Code-native; Squad is heavier and Copilot-native. They occupy different categories entirely — Spec-Driven vs. Multi-Agent Orchestration.

**vs. HVE:** Both target structured, multi-agent development but at different scales. HVE is enterprise-grade with 49 agents, 102 instructions, constraint-based governance, and the RPI workflow. Squad is team-scale with typically 4-5 agents, persistent memory, and GitHub-centric work management. HVE emphasizes governance and audit trails; Squad emphasizes team coordination and autonomous work routing. HVE targets enterprise teams in regulated environments; Squad targets development teams that want AI agents working alongside their existing GitHub workflow.
