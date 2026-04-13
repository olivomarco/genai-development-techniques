# HVE (Hypervelocity Engineering)

## At a Glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Hypervelocity Engineering     |
| Category           | Enterprise AI-Native SDLC     |
| Source             | [microsoft/hve-core](https://github.com/microsoft/hve-core) |
| Author/Org         | Microsoft ISE (Industry Solutions Engineering) |
| License            | MIT                           |
| First Released     | 2024 (internal), open-sourced 2025 |
| Current Version    | v3.2.2 (23 releases as of April 2026) |
| Stars / Popularity | 919 stars, 141 forks, 54 contributors |
| Supported Tools    | GitHub Copilot (VS Code extension and CLI) |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Primary — ships as a VS Code extension with 49 agents and 102 instructions |
| GitHub Copilot Coding Agent (github.com) | ⚠️ Partial — instruction files are readable but the RPI workflow requires interactive phase switching |
| Claude Code | ❌ Not supported — tightly coupled to Copilot ecosystem |
| Cursor | ❌ Not supported |
| OpenAI Codex (CLI) | ❌ Not supported |
| Windsurf | ❌ Not supported |
| Gemini CLI | ❌ Not supported |
| Roo Code | ❌ Not supported |

## Overview

Hypervelocity Engineering (HVE) is Microsoft's enterprise methodology and tooling framework for AI-native application development. Created by the ISE (Industry Solutions Engineering) team — the same group that shipped 140+ AI solutions in two years — HVE provides a structured approach to integrating AI agents across the entire software development lifecycle.

Unlike lighter-weight approaches that focus on a single developer's workflow, HVE targets multidisciplinary teams of 4–5 people working on enterprise software. Its signature contribution is the RPI workflow (Research → Plan → Implement → Review), a four-phase development cycle where specialized AI agents handle each phase under constraint-based governance. The core insight, as the HVE documentation states: "When AI knows it cannot implement, it stops optimizing for 'plausible code' and starts optimizing for 'verified truth.' The constraint changes the goal."

HVE ships as a VS Code extension and a GitHub repository containing 49 agents, 102 instructions, 63 prompts, 11 skills, and 10 domain-specific collections. It is explicitly built for — and tightly coupled to — the GitHub Copilot ecosystem.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Enterprise-grade governance — audit trails, validated artifacts, policy-as-code | ❌ Copilot lock-in — no support for Claude Code, Cursor, or other tools |
| ✅ Research-first philosophy prevents costly rework | ❌ 49 agents + 102 instructions can overwhelm small teams |
| ✅ Comprehensive tooling — 10 domain-specific collections | ❌ Manual context clearing between RPI phases adds operational burden |
| ✅ Supply-chain security (SBOM, attestation, CodeQL, OpenSSF) | ❌ Some collections still experimental/preview |
| ✅ Proven at enterprise scale (AT&T, KT Corporation) | ❌ No autonomous iteration — each phase needs human initiation |
| ✅ Multi-stack support (no-code → pro-code) | ❌ Microsoft ecosystem tilt (Azure, M365, Power Platform) |

> **In one sentence:** HVE is the enterprise weapon — built from Microsoft ISE's experience shipping 140+ AI solutions, it trades simplicity for the governance, audit trails, and research-first rigor that regulated industries demand.

## Core Concepts

- **Velocity-as-Vector** — Speed alone is insufficient. HVE measures velocity as speed + direction + quality combined. Moving fast in the wrong direction is not progress.
- **Constraint-Based Workflows** — Constraints (repository access controls, environment promotion rules, deployment targets, policy enforcement) don't slow teams down — they enable safe autonomy by defining bounded exploration spaces.
- **Validated Artifacts** — Every output, whether from a human or an AI agent, must pass formal validation gates: automated tests, static analysis, security scans, and compliance checks.
- **Repeatable Patterns of Integration (RPI)** — Standardized integration patterns reduce fragility and make scaling predictable. The RPI acronym also names the core workflow.
- **Collection-based architecture** — Domain-specific bundles (hve-core, coding-standards, project-planning, security, design-thinking, data-science, github, ado, jira, rai-planning) that teams adopt selectively.

## How It Works

The RPI workflow transforms complex coding tasks through four structured phases. Each phase uses a dedicated AI agent with specialized instructions, and context is explicitly cleared between phases.

```
Uncertainty → Knowledge → Strategy → Working Code → Validated Code
```

| Phase | Agent | What It Does | Output |
|-------|-------|-------------|--------|
| 🔬 **Research** | Task Researcher | Investigates codebase, APIs, documentation. Documents findings with evidence and sources. Creates one recommended approach. | `{date}-{topic}-research.md` |
| 📋 **Plan** | Task Planner | Creates planning files with checkboxes and line number references. Validates that research exists before proceeding. | Plan and details files |
| ⚡ **Implement** | Task Implementor | Executes the plan task by task with verification at each step. Tracks all changes in a changes log. | Working code + `{date}-{topic}-changes.md` |
| ✅ **Review** | Task Reviewer | Validates the implementation against the research and plan. Checks convention compliance. Runs lint, build, and test suites. | `{date}-{topic}-review.md` |

**Critical operational rule:** Always clear context (`/clear` or new chat) between phases. Each agent operates under different instructions, and accumulated context from prior phases causes confusion and quality degradation.

Beyond the RPI workflow, HVE includes:

| Type | Count | Description |
|------|-------|-------------|
| Agents | 49 | Specialized AI assistants for research, planning, implementation, and domain tasks |
| Instructions | 102 | Repository-specific coding guidelines applied automatically |
| Prompts | 63 | Reusable templates for common tasks (commits, PRs, etc.) |
| Skills | 11 | Self-contained packages with cross-platform scripts and guidance |
| Collections | 10 | Domain-specific bundles ranging from stable to experimental |

## Strengths

- **Enterprise-grade governance.** Constraint-based workflows, validated artifacts, audit trails, and policy-as-code provide the kind of structured oversight that regulated industries require.
- **Research-first philosophy.** The Research phase forces the AI to investigate before implementing, producing higher-quality code and reducing rework. The separation of concerns between phases is its most distinctive contribution.
- **Comprehensive tooling.** 49 agents, 102 instructions, 63 prompts, and 11 skills cover a wide range of development scenarios out of the box, reducing the need for custom setup.
- **Multi-stack support.** Works across no-code (Copilot Studio), low-code (Power Platform), and pro-code (Azure, custom frameworks), making it suitable for organizations with mixed technology stacks.
- **Supply-chain security.** SBOM generation, attestation, OpenSSF Scorecard, and CodeQL analysis address enterprise security requirements.
- **Proven at scale.** Evolved from Microsoft's internal delivery of 140+ AI solutions. Enterprise adoption by AT&T, KT Corporation, and other telcos provides real-world validation.

## Limitations

- **GitHub Copilot lock-in.** Tightly coupled to the Copilot ecosystem. Teams using Claude Code, Cursor, or other AI tools cannot use HVE without significant adaptation.
- **Enterprise weight.** 49 agents and 102 instructions can overwhelm solo developers or small teams. The framework is designed for organizations, not individuals.
- **Context management burden.** The RPI workflow requires manually clearing context between phases and switching agents, adding operational overhead that simpler approaches avoid.
- **Experimental collections.** Several domain collections (security, jira, rai-planning, design-thinking) remain experimental or preview, with stability not guaranteed.
- **No autonomous iteration.** Unlike Ralph, HVE does not include an autonomous loop. Each phase requires explicit human initiation, which limits AFK productivity.
- **Microsoft ecosystem tilt.** While not exclusive to Microsoft tools, HVE has a natural bias toward Azure, Microsoft 365, and Power Platform.

## Best For

- **Enterprise teams (4–10+ developers)** building production software with governance, compliance, and audit requirements.
- **Organizations already invested in GitHub Copilot** who want a structured methodology around their existing tooling.
- **Multi-stack projects** mixing no-code, low-code, and pro-code components that need consistent quality standards.
- **Regulated industries** (financial services, healthcare, telecom) where traceability and validated artifacts are non-negotiable.
- **Teams onboarding new developers** who benefit from codified instruction sets over tribal knowledge.

## Not Ideal For

- **Solo developers or small teams** who find 49 agents and 102 instructions excessive for their workflow.
- **Teams committed to non-Copilot tools** (Claude Code, Cursor, Aider) — HVE's tight Copilot coupling makes portability impractical.
- **Rapid prototyping or hackathon-style development** where governance overhead slows down exploration.
- **Projects needing autonomous overnight iteration** — HVE's phased approach requires human presence at each phase transition.
- **Cost-sensitive teams** — the combination of GitHub Copilot subscription and Azure infrastructure may exceed the budget of smaller organizations.

## Community & Ecosystem

HVE has a moderate but growing ecosystem anchored by Microsoft's backing:

- **GitHub:** 919 stars, 141 forks, 54 contributors, 23 releases — modest compared to community-driven frameworks (GSD has 51K+), but meaningful for an enterprise methodology.
- **VS Code Extension:** Available on the VS Code Marketplace as "HVE Core" (ise-hve-essentials.hve-core), providing one-click install.
- **Microsoft Learn:** Featured on the HVE Accelerators Hub, giving it institutional credibility.
- **Public advocacy:** Robin Cole (VP Engineering, Microsoft) has presented at TMForum and on the Telco in 20 podcast (Ep 122). Valentina Alto published an end-to-end Medium walkthrough (April 2026). Paul Yuknewicz called it "rad" for Azure Functions development.
- **Enterprise adoption:** AT&T (using GitHub Copilot on Azure), KT Corporation (building development capability on Microsoft stack).
- **Documentation quality:** The official docs site (microsoft.github.io/hve-core/) is comprehensive. Valentina Alto's Medium article and Dave Davis's blog post provide third-party walkthroughs.
- **Ecosystem maturity:** Stable core with experimental edges. The collection-based architecture allows incremental adoption, but some collections need more time to mature.

## Comparison Notes

**vs. Ralph:** Opposite ends of the autonomy-governance spectrum. Ralph is a bash loop with zero structure; HVE is 49 agents with constraint-based governance. Ralph is tool-agnostic; HVE is Copilot-locked. Ralph enables AFK overnight runs; HVE requires human presence at phase boundaries. Ralph optimizes for individual throughput on scoped tasks; HVE optimizes for team consistency and enterprise compliance.

**vs. BMAD:** Both are multi-agent methodologies with structured roles, but BMAD uses named persona agents (Analyst, PM, Architect, Dev, QA) within a more agile-oriented framework with 34+ workflows. HVE uses specialized unnamed agents within a phased RPI workflow. BMAD is tool-portable and community-driven (44K+ stars); HVE is Copilot-specific and Microsoft-backed (919 stars). BMAD supports scale-adaptive intelligence for solo-to-team use; HVE is explicitly designed for enterprise teams.

**vs. GSD:** GSD is a spec-driven methodology with a 6-step workflow (new project → discuss → plan → execute → verify → complete milestone) focused on preventing context rot through fresh agent spawning. HVE's RPI workflow similarly uses phased separation but adds formal research and review phases with validation gates. GSD is lighter-weight and Claude Code-focused (51K+ stars); HVE is heavier and Copilot-focused. GSD is more accessible to solo developers; HVE scales better for enterprise teams.
