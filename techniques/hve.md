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
| Current Version    | v3.2.2 stable (March 23, 2026); prereleases through v3.3.101 (April 25, 2026) |
| Stars / Popularity | ~1,300 stars · 251 forks |
| Supported Tools    | GitHub Copilot (VS Code extension and CLI) |

## Compatible Coding Agents

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ Primary — ships as a VS Code extension; repository inventory is larger than the latest verified stable-release inventory |
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

HVE ships as a VS Code extension and a GitHub repository. On August 8, 2026, the `main` branch contained 70 `*.agent.md`, 80 `*.instructions.md`, 67 `*.prompt.md`, and 58 `SKILL.md` files. These are repository-level counts, not verified contents of the v3.2.2 stable package. It is explicitly built for — and tightly coupled to — the GitHub Copilot ecosystem.

## Pros & Cons at a Glance

| Pros | Cons |
|------|------|
| ✅ Enterprise-grade governance — audit trails, validated artifacts, policy-as-code | ❌ Copilot lock-in — no support for Claude Code, Cursor, or other tools |
| ✅ Research-first philosophy prevents costly rework | ❌ Large agent and instruction inventory can overwhelm small teams |
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

| Type | Count on `main` | Description |
|------|-----------------|-------------|
| Agent files | 70 | Specialized AI assistants for research, planning, implementation, and domain tasks |
| Instruction files | 80 | Repository-specific coding guidelines |
| Prompt files | 67 | Reusable task templates |
| `SKILL.md` files | 58 | Self-contained skill packages |

These counts describe the repository tree observed on August 8, 2026. The contents of the v3.2.2 stable VSIX were not inspected.

## Strengths

- **Enterprise-grade governance.** Constraint-based workflows, validated artifacts, audit trails, and policy-as-code provide the kind of structured oversight that regulated industries require.
- **Research-first philosophy.** The Research phase forces the AI to investigate before implementing, producing higher-quality code and reducing rework. The separation of concerns between phases is its most distinctive contribution.
- **Comprehensive repository inventory.** The `main` branch contains 70 agent files, 80 instruction files, 67 prompt files, and 58 skills. The sharp increase in skills shows HVE repackaging more guidance onto the Agent Skills primitive.
- **Multi-stack support.** Works across no-code (Copilot Studio), low-code (Power Platform), and pro-code (Azure, custom frameworks), making it suitable for organizations with mixed technology stacks.
- **Supply-chain security.** SBOM generation, attestation, OpenSSF Scorecard, and CodeQL analysis address enterprise security requirements.
- **Proven at scale.** Evolved from Microsoft's internal delivery of 140+ AI solutions. Enterprise adoption by AT&T, KT Corporation, and other telcos provides real-world validation.

## Limitations

- **GitHub Copilot lock-in.** Tightly coupled to the Copilot ecosystem. Teams using Claude Code, Cursor, or other AI tools cannot use HVE without significant adaptation.
- **Enterprise weight.** The large repository inventory can overwhelm solo developers or small teams. The framework is designed for organizations, not individuals.
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

- **Solo developers or small teams** who find a large enterprise agent and instruction inventory excessive.
- **Teams committed to non-Copilot tools** (Claude Code, Cursor, Aider) — HVE's tight Copilot coupling makes portability impractical.
- **Rapid prototyping or hackathon-style development** where governance overhead slows down exploration.
- **Projects needing autonomous overnight iteration** — HVE's phased approach requires human presence at each phase transition.
- **Cost-sensitive teams** — the combination of GitHub Copilot subscription and Azure infrastructure may exceed the budget of smaller organizations.

## Community & Ecosystem

HVE has an ecosystem anchored by Microsoft's backing. The latest stable release remains v3.2.2 from March 23, 2026. Prereleases continued through v3.3.101 on April 25, and the repository was pushed on August 8. Keep stable, prerelease, and unreleased repository activity distinct.

- **GitHub:** ~1,328 stars and 251 forks on August 8, 2026.
- **VS Code Extension:** Available on the VS Code Marketplace as "HVE Core" (ise-hve-essentials.hve-core), providing one-click install.
- **Microsoft Learn:** Featured on the HVE Accelerators Hub, giving it institutional credibility.
- **Public advocacy:** Robin Cole (VP Engineering, Microsoft) has presented at TMForum and on the Telco in 20 podcast (Ep 122). Valentina Alto published an end-to-end Medium walkthrough (April 2026). Paul Yuknewicz called it "rad" for Azure Functions development.
- **Enterprise adoption:** AT&T (using GitHub Copilot on Azure), KT Corporation (building development capability on Microsoft stack).
- **Documentation quality:** The official docs site (microsoft.github.io/hve-core/) is comprehensive. Valentina Alto's Medium article and Dave Davis's blog post provide third-party walkthroughs.
- **Ecosystem maturity:** Stable core with experimental edges. The collection-based architecture allows incremental adoption, but some collections need more time to mature.

## Comparison Notes

**vs. Ralph:** Opposite ends of the autonomy-governance spectrum. Ralph is a bash loop with minimal structure; HVE has a large repository inventory and constraint-based governance. Ralph is tool-agnostic; HVE is Copilot-locked. Ralph enables AFK runs; HVE requires human presence at phase boundaries.

**vs. BMAD:** Both are multi-agent methodologies with structured roles. BMAD uses named personas and an agile-oriented module ecosystem. HVE uses specialized agents within a phased RPI workflow. BMAD is more tool-portable; HVE is Copilot-specific and Microsoft-backed.

**vs. GSD:** GSD Core is a spec-driven methodology with a five-step Discuss → Plan → Execute → Verify → Ship loop. HVE's RPI workflow adds formal research and review phases with enterprise validation gates. GSD is lighter and multi-runtime; HVE is heavier and Copilot-focused.

**vs. Superpowers:** Both enforce structured development workflows at different scales. HVE uses agents, constraint-based governance, validated artifacts, and audit trails for enterprise environments. Superpowers uses composable behavioral skills for individual developer discipline. HVE is Copilot-only; Superpowers is multi-tool. HVE provides formal governance that Superpowers lacks.

HVE's growth from 11 previously documented skills to 58 `SKILL.md` files on `main` also connects it to the [skills ecosystem](skills-ecosystem.md). That repository activity shows increased use of the skills primitive, but it does not prove those files shipped in the latest stable VSIX.
