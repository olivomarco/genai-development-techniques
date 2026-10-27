# HVE (Hypervelocity Engineering)

## At a glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Hypervelocity Engineering     |
| Category           | Enterprise AI-Native SDLC     |
| Source             | [microsoft/hve-core](https://github.com/microsoft/hve-core) |
| Author/Org         | Microsoft ISE (Industry Solutions Engineering) |
| License            | MIT                           |
| First Released     | 2024 (internal), open-sourced 2025 |
| Current Version    | v3.2.2 stable (March 23, 2026); prereleases through v3.3.101 (April 25, 2026) |
| Stars / Popularity | ~1,580 stars · 343 forks |
| Supported Tools    | GitHub Copilot (VS Code extension and CLI) |

## Compatible coding agents

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

Hypervelocity Engineering (HVE) is Microsoft's enterprise methodology and tooling framework for AI-native application development. The ISE (Industry Solutions Engineering) team created it after delivering a reported 140+ AI solutions in two years. HVE structures the use of AI agents across the software development lifecycle.

Unlike lighter-weight approaches that focus on a single developer's workflow, HVE targets multidisciplinary teams of 4–5 people working on enterprise software. Its signature contribution is the RPI workflow (Research → Plan → Implement → Review), a four-phase development cycle where specialized AI agents handle each phase under constraint-based governance. The core insight, as the HVE documentation states: "When AI knows it cannot implement, it stops optimizing for 'plausible code' and starts optimizing for 'verified truth.' The constraint changes the goal."

HVE ships as a VS Code extension and a GitHub repository, both built for the GitHub Copilot ecosystem. On October 27, 2026, the `main` branch contained 71 `*.agent.md`, 60 `*.instructions.md`, zero `*.prompt.md`, and 88 `SKILL.md` files. The August 8, 2026 counts were 70, 80, 67, and 58, respectively; reusable prompt files have moved to skill packages. These are repository counts, not verified contents of the v3.2.2 stable package.

## Pros & cons at a glance

| Pros | Cons |
|------|------|
| ✅ Enterprise-grade governance — audit trails, validated artifacts, policy-as-code | ❌ Copilot lock-in — no support for Claude Code, Cursor, or other tools |
| ✅ Research before implementation | ❌ Large agent and instruction inventory can overwhelm small teams |
| ✅ Domain-specific skill collections across the lifecycle | ❌ Manual context clearing between RPI phases adds operational burden |
| ✅ Supply-chain security (SBOM, attestation, CodeQL, OpenSSF) | ❌ Some collections still experimental/preview |
| ✅ Reported enterprise use (AT&T, KT Corporation) | ❌ No autonomous iteration — each phase needs human initiation |
| ✅ Multi-stack support (no-code → pro-code) | ❌ Microsoft ecosystem tilt (Azure, M365, Power Platform) |

> HVE adds research, validation gates, audit trails, and policy-as-code for enterprise teams, at the cost of more setup and manual phase transitions.

## Core concepts

- **Velocity-as-Vector** — HVE defines velocity as a combination of speed, direction, and quality.
- **Constraint-Based Workflows** — Repository access controls, environment promotion rules, deployment targets, and policy enforcement define the boundaries within which agents can work.
- **Validated Artifacts** — Every output, whether from a human or an AI agent, must pass formal validation gates: automated tests, static analysis, security scans, and compliance checks.
- **Repeatable Patterns of Integration (RPI)** — Standardized integration patterns reduce fragility and make scaling predictable. The RPI acronym also names the core workflow.
- **Collection-based architecture** — Domain-specific bundles (hve-core, coding-standards, project-planning, security, design-thinking, data-science-engineering, rai, accessibility, and others) that teams adopt selectively. The `.github/skills/` tree held 15 top-level collection directories on October 27, 2026, up from the 10 named in earlier documentation; some additions (accessibility, engagement-reporting, hve-slides) are new domains rather than renames.

## How it works

The RPI workflow divides tasks into four phases. Each uses a dedicated AI agent with specialized instructions, with context cleared between phases.

[Diagram: HVE artifacts across four phases](../diagrams/hve-workflow.html)

| Phase | Agent | What It Does | Output |
|-------|-------|-------------|--------|
| Research | Task Researcher | Investigates the codebase, APIs, and documentation. Records evidence and sources, then recommends one approach. | `{date}-{topic}-research.md` |
| Plan | Task Planner | Creates planning files with checkboxes and line number references. Checks that research exists before proceeding. | Plan and details files |
| Implement | Task Implementor | Executes the plan task by task, verifying each step and recording changes. | Working code + `{date}-{topic}-changes.md` |
| Review | Task Reviewer | Checks the implementation against the research, plan, and conventions. Runs lint, build, and test suites. | `{date}-{topic}-review.md` |

Clear context (`/clear` or new chat) between phases. Each agent has different instructions; prior-phase context can interfere with them.

Beyond the RPI workflow, HVE includes:

| Type | Count on `main` | Description |
|------|-----------------|-------------|
| Agent files | 71 | Specialized AI assistants for research, planning, implementation, and domain tasks |
| Instruction files | 60 | Repository-specific coding guidelines |
| Prompt files | 0 | Reusable task templates — the category that existed on August 8, 2026 (67 files) has been fully migrated |
| `SKILL.md` files | 88 | Self-contained skill packages |

These counts describe the repository tree observed on October 27, 2026. The contents of the v3.2.2 stable VSIX were not inspected. HVE's contributor docs still describe `.prompt.md` as a supported artifact type, so the format is not formally retired — but no files in that format remain on `main` today.

## Strengths

- **Enterprise-grade governance.** Constraint-based workflows, validated artifacts, audit trails, and policy-as-code provide the kind of structured oversight that regulated industries require.
- **Research before implementation.** A separate Research phase requires investigation and documented findings before planning or code changes.
- **Repository coverage.** The `main` branch contains 71 agent files, 60 instruction files, and 88 skills as of October 27, 2026, with no remaining prompt files. Reusable task templates now use Agent Skills packages.
- **Multi-stack support.** Works across no-code (Copilot Studio), low-code (Power Platform), and pro-code (Azure, custom frameworks), making it suitable for organizations with mixed technology stacks.
- **Supply-chain security.** SBOM generation, attestation, OpenSSF Scorecard, and CodeQL analysis address enterprise security requirements.
- **Reported enterprise use.** HVE grew out of Microsoft's delivery of 140+ AI solutions. AT&T, KT Corporation, and other telcos are reported adopters; these reports are not independent outcome measurements.

## Limitations

- **GitHub Copilot lock-in.** Tightly coupled to the Copilot ecosystem. Teams using Claude Code, Cursor, or other AI tools cannot use HVE without significant adaptation.
- **Enterprise weight.** The large repository inventory can overwhelm solo developers or small teams. The framework is designed for organizations, not individuals.
- **Context management burden.** The RPI workflow requires manually clearing context between phases and switching agents, adding operational overhead that simpler approaches avoid.
- **Experimental collections.** The repository marks a dedicated `experimental` collection, and individual domain collections (security, rai, design-thinking) still carry preview-level content, with stability not guaranteed.
- **No autonomous iteration.** Unlike Ralph, HVE does not include an autonomous loop. Each phase requires explicit human initiation, which limits AFK productivity.
- **Microsoft ecosystem tilt.** While not exclusive to Microsoft tools, HVE has a natural bias toward Azure, Microsoft 365, and Power Platform.

## Best for

- **Enterprise teams (4–10+ developers)** building production software with governance, compliance, and audit requirements.
- **Organizations already invested in GitHub Copilot** who want a structured methodology around their existing tooling.
- **Multi-stack projects** mixing no-code, low-code, and pro-code components that need consistent quality standards.
- **Regulated industries** (financial services, healthcare, telecom) that require traceability and validated artifacts.
- **Teams onboarding new developers** who need documented conventions and instructions.

## Not ideal for

- **Solo developers or small teams** who find a large enterprise agent and instruction inventory excessive.
- **Teams committed to non-Copilot tools** (Claude Code, Cursor, Aider) — HVE's tight Copilot coupling makes portability impractical.
- **Rapid prototyping or hackathon-style development** where governance overhead slows down exploration.
- **Projects needing autonomous overnight iteration** — HVE's phased approach requires human presence at each phase transition.
- **Cost-sensitive teams** — the combination of GitHub Copilot subscription and Azure infrastructure may exceed the budget of smaller organizations.

## Community & ecosystem

The latest verified stable release is v3.2.2 from March 23, 2026. Prereleases have continued past v3.3.101 (April 25, 2026) without a new stable tag. Keep stable releases, prereleases, and unreleased repository activity distinct.

- **GitHub:** ~1,580 stars and 343 forks on October 27, 2026.
- **VS Code Extension:** Available on the VS Code Marketplace as "HVE Core" (ise-hve-essentials.hve-core), providing one-click install.
- **Microsoft Learn:** Featured on the HVE Accelerators Hub.
- **Public advocacy:** Robin Cole (VP Engineering, Microsoft) has presented at TMForum and on the Telco in 20 podcast (Ep 122). Valentina Alto published an end-to-end Medium walkthrough (April 2026). Paul Yuknewicz called it "rad" for Azure Functions development.
- **Enterprise adoption:** AT&T (using GitHub Copilot on Azure), KT Corporation (building development capability on Microsoft stack).
- **Documentation quality:** The official docs site (microsoft.github.io/hve-core/) is comprehensive. Valentina Alto's Medium article and Dave Davis's blog post provide third-party walkthroughs.
- **Ecosystem maturity:** Stable core with experimental edges. The collection-based architecture allows incremental adoption, but some collections need more time to mature.

## Comparison notes

**vs. Ralph:** Opposite ends of the autonomy-governance spectrum. Ralph is a bash loop with minimal structure; HVE has a large repository inventory and constraint-based governance. Ralph is tool-agnostic; HVE is Copilot-locked. Ralph enables AFK runs; HVE requires human presence at phase boundaries.

**vs. BMAD:** Both are multi-agent methodologies with structured roles. BMAD uses named personas and an agile-oriented module ecosystem. HVE uses specialized agents within a phased RPI workflow. BMAD is more tool-portable; HVE is Copilot-specific and Microsoft-backed.

**vs. GSD:** GSD Core is a spec-driven methodology with a five-step Discuss → Plan → Execute → Verify → Ship loop. HVE's RPI workflow adds formal research and review phases with enterprise validation gates. GSD is lighter and multi-runtime; HVE is heavier and Copilot-focused.

**vs. Superpowers:** Both enforce structured development workflows at different scales. HVE uses agents, constraint-based governance, validated artifacts, and audit trails for enterprise environments. Superpowers uses composable behavioral skills for individual developer discipline. HVE is Copilot-only; Superpowers is multi-tool. HVE provides formal governance that Superpowers lacks.

HVE's growth from 11 previously documented skills to 88 `SKILL.md` files on `main`, with `.prompt.md` files dropping to zero, reflects its move toward the [skills ecosystem](skills-ecosystem.md). It does not establish which files shipped in the latest stable VSIX.
