# GenAI development techniques — overview and comparison

---

## 1. Executive summary

As of August 8, 2026, AI-assisted development spans structured methodologies, multi-agent frameworks, autonomous loops, enterprise workflows, and a rapidly consolidating skills layer. The central question is no longer whether an agent can write code, but how you direct it with repeatable context, artifacts, verification, and governance.

The comparison retains ten Tier 1 approaches across five categories, with **context engineering** as a cross-cutting practice. A separate [skills ecosystem](techniques/skills-ecosystem.md) now covers the Agent Skills specification, libraries, registries, installers, and runtime support. It is supporting market context, not an eleventh technique or a sixth methodology category. Star counts remain dated awareness signals; they do not establish production adoption.

The choice between these approaches is not about which is "best" — it's about matching the technique to your situation. A solo developer prototyping a weekend project has fundamentally different needs than an enterprise team shipping regulated software with audit requirements. This document provides the data and decision frameworks to make that match.

---

## 2. Comparison matrix

All scores are derived from the research findings. Where a technique spans a range, the most representative value is used.

| Dimension | GSD | BMAD | Spec Kit | OpenSpec | Squad | Ralph | Superpowers | HVE | Context Engineering |
|-----------|-----|------|----------|---------|-------|-------|-------------|-----|---------------------|
| **Approach** | Spec-Driven | Multi-Agent | Spec-Driven | Spec-Driven | Multi-Agent | Autonomous Iteration | Skill-Based | Enterprise SDLC | Practice |
| **Human Control** | Semi-autonomous | HITL | HITL | HITL | Semi-autonomous | AFK / HITL | Semi-autonomous | Phased | HITL |
| **Setup Complexity** | Minutes | Hours | Minutes | Minutes | Hours | Minutes | Minutes | Hours–Days | Minutes |
| **Tool Compatibility** | 20 documented host profiles with capability negotiation; Copilot defaults to sequential inline execution | Multi-tool; Web Bundles are planning surfaces, not CLI parity | Multi-tool with many pre-baked prompts | Broad native/pre-baked support; runtime parity not verified | GitHub Copilot | Tool-agnostic AI CLI pattern | Multi-tool methodology | GitHub Copilot | Tool-agnostic practice |
| **Scale** | Solo–Small team | Solo–Enterprise | Solo–Small team | Solo–Small team | Small team–Enterprise | Solo | Solo–Small team | Large team–Enterprise | Solo–Enterprise |
| **Predictability** | High | High | Medium–High | Medium–High | Medium | Low–Medium | High | High | Varies by implementation |
| **Context Management** | Fresh agent per task; waves for parallelism | Agent personas + structured workflows | Spec files as context anchor | Change folders as context anchor; spec deltas track requirement evolution | Charter files + decision ledger + history | Fresh context each loop iteration; git as memory | Skill files as behavioral modules; token-light bootstrap (~2K tokens); lazy skill loading via CLI search; subagents for implementation | Clear context between RPI phases; research docs persist in files | Rules files layered by scope (8-layer model) |
| **Quality Gates** | Moderate (verification per phase) | Comprehensive (QA agent, readiness checks, retros) | Moderate (analyze + checklist commands) | Moderate (proposal approval, validate --strict, verify command) | Moderate (reviewer rejection protocol, ceremonies) | Basic (tests/linting as backpressure) | Comprehensive (mandatory skills, TDD enforcement, two-stage code review, pressure-tested compliance) | Comprehensive (validated artifacts, lint/build/test, review phase) | None (practice, not a system) |
| **Governance** | Light | Moderate | Light | Light | Moderate (decisions ledger, reviewer lockout) | None | Light | Heavy (constraint-based, audit trails, policy-as-code) | None |
| **Learning Curve** | Medium | High | Low–Medium | Low | Medium–High | Low | Medium | High | Low |
| **Ecosystem Maturity** | Active successor v1.10.0; archived predecessor retained its metrics | v6.10.0; active modules and community | v0.16.1; GitHub-backed, experimental, pre-1.0 | v1.8.0 stable; prerelease channel exists | v0.11.0; pre-1.0, unreleased repo activity continues | Canonical guide is static; ralph-orchestrator v2.10.1 | v6.2.0; large audience and active releases | v3.2.2 stable; v3.3 prereleases and newer repo activity | Established practice; skills packaging now standardized |
| **Cost** | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for Copilot sub) | Free (API costs — can be high for long loops) | Free (API costs for AI tool) | Free (Copilot subscription) | Free |
| **Open Source** | Yes (MIT) | Partial (open source, trademark on name) | Yes (GitHub official) | Yes (MIT) | Yes (MIT) | Yes (technique is open; plugin is official) | Yes (MIT) | Yes (MIT) | Yes (community-driven) |

---

## 3. GitHub star history

Frameworks with GitHub repositories — star growth over time:

[![Star History Chart](https://api.star-history.com/svg?repos=open-gsd/gsd-core,bmad-code-org/BMAD-METHOD,github/spec-kit,Fission-AI/OpenSpec,bradygaster/squad,obra/superpowers,microsoft/hve-core&type=timeline)](https://star-history.com/#open-gsd/gsd-core&bmad-code-org/BMAD-METHOD&github/spec-kit&Fission-AI/OpenSpec&bradygaster/squad&obra/superpowers&microsoft/hve-core&timeline)

*GSD's chart starts with the active successor repository; the archived predecessor retains its separate history. Ralph and Context Engineering are not included because they have no single comparable repository.*

---

## 4. Decision guide

> **For a comprehensive decision guide by team size, project type, industry, and development activity, see [Choosing Your Approach](techniques/choosing-your-approach.md).**
>
> The table below is a quick reference. The full guide covers solo developers, teams of 3, teams of 10, regulated environments (finance, healthcare, government), agile workflows, brownfield vs. greenfield, and more.

| If you want... | Use | Why |
|----------------|-----|-----|
| The simplest possible setup | **Ralph** | A bash one-liner. No framework, no dependencies, no configuration. Define a prompt, run the loop. |
| Structured solo development with clear phases | **GSD** | Five-step Discuss → Plan → Execute → Verify → Ship workflow with fresh task context. |
| A full agile team simulation | **BMAD** | Specialized roles, modular workflows, scale-adaptive planning, and optional unattended iteration. |
| GitHub-backed spec-driven development | **Spec Kit** | GitHub's official SDD toolkit. Works with Copilot, Claude Code, Gemini CLI. Minimal footprint, strong institutional backing. |
| Parallel multi-agent orchestration with persistent memory | **Squad** | Named agents with charters, shared decisions, ceremonies, and Ralph-style work monitoring. Conway's Law for AI teams. |
| Enterprise governance and audit trails | **HVE** | Microsoft ISE's constraint-based RPI workflow, validated artifacts, and policy-as-code. |
| To improve any AI tool's output without adopting a framework | **Context Engineering** | Rules files (copilot-instructions.md, .cursorrules, CLAUDE.md) work everywhere. Start here before committing to a framework. |
| A disciplined individual workflow with TDD and reusable skills | **Superpowers** | Mandatory skills enforce systematic development across several tools. |
| Reusable skills without a mandatory methodology | **Skills ecosystem** | Choose a library, installer, and distribution model independently of your development process. |
| To run AI agents overnight on mechanical tasks | **Ralph** | AFK mode with max-iteration and cost caps. |
| Lightweight spec-driven development for existing codebases | **OpenSpec** | Brownfield-first, change-centric workflow with delta specs and broad multi-tool support. |
| Tool-agnostic methodology that works with any AI CLI | **Ralph** or **Context Engineering** | Ralph works with any CLI that doesn't cap tool calls. Context engineering practices apply to every tool. |

---

## 5. Category summaries

### Spec-Driven Development — GSD, Spec Kit, OpenSpec

**GSD Core** continues the archived original project with a five-step loop and a multi-runtime installer. **Spec Kit** is GitHub's pre-1.0 project-level specification toolkit at v0.16.1. **OpenSpec** is the v1.8.0 brownfield specialist, using change folders and delta specs. OpenSpec now writes vendor-neutral skills to `.agents/skills/`, but remains a spec-driven methodology rather than a skills library.

### Skill-Based Development — Superpowers

Superpowers uses skills as mandatory workflow controls. Version 6.2.0 stores review state in plan-scoped `.superpowers/sdd/<plan-basename>/` workspaces and resumes implementers during review-fix loops. This differs from `mattpocock/skills`, which offers independently selectable capabilities without an enforced lifecycle.

### Multi-Agent Orchestration — Squad, BMAD

**BMAD** uses specialized roles, structured phases, and modules; v6.10.0 added `bmad-loop` and retired or deprecated older automation modules. **Squad** creates parallel agent instances with persistent memory; v0.11.0 added preset installation, cross-Squad discovery, Copilot App sub-sessions, and `cast` terminology. Both trade simplicity for coordination.

### Autonomous Iteration — Ralph

Ralph stands alone in its category: a bash one-liner that runs an AI coding agent in a loop, using tests as backpressure and git commits as memory between iterations. Created by Geoffrey Huntley and named after Ralph Wiggum from *The Simpsons* ("keep going despite always making mistakes"), it's the philosophical opposite of enterprise frameworks. There is no governance, no agent roles, no structured phases — just a prompt, a loop, and a test suite. Its power lies in simplicity and overnight productivity: set it running before bed, wake up to completed features. The trade-off is unpredictability — Huntley himself calls it "deterministically bad in a nondeterministic world" — and it works best on greenfield projects with clear completion criteria.

### Enterprise AI-Native SDLC — HVE

HVE is the enterprise end of the spectrum. Its latest stable release remains v3.2.2, while v3.3 prereleases and newer repository activity exist separately. The August 8 repository tree contained 70 agent files, 80 instruction files, 67 prompt files, and 58 `SKILL.md` files; these counts do not describe verified stable-package contents.

### Cross-cutting: Context Engineering

Context engineering remains the foundational practice. Rules files are still fragmented by tool, but skills packaging has converged on the vendor-neutral [Agent Skills](https://agentskills.io) specification. Basic skill content is portable; optional features and execution semantics still vary across runtimes.

### Skills ecosystem

The [skills ecosystem](techniques/skills-ecosystem.md) sits beside the methodology taxonomy. Agent Skills defines the format; `mattpocock/skills` and `anthropics/skills` supply content; skills.sh provides discovery and installation; runtimes execute the result. Provenance remains immature: the examined surfaces lacked signing, attestation, and lockfile-style pinning.

---

## 6. Complexity vs. speed spectrum

The spectrum below follows the accepted OpenSpec scoping decision: OpenSpec sits between Superpowers and Spec Kit because it is more structured than a skill layer but lighter and more change-centric than Spec Kit's project-level phase gates.

```text
                        COMPLEXITY vs. SPEED SPECTRUM
                        ─────────────────────────────

  Less Setup                                                    More Setup
  Faster Start                                                  More Structure
  ◄─────────────────────────────────────────────────────────────────────────►

       │         │              │          │           │          │         │        │         │
       ▼         ▼              ▼          ▼           ▼          ▼         ▼        ▼         ▼
  ┌─────────┐┌───────┐   ┌──────────┐┌───────────┐┌──────────┐┌─────────┐┌───────┐┌──────┐┌─────────┐
  │ Context ││ Ralph │   │   GSD    ││Superpwrs  ││ OpenSpec ││Spec Kit ││ Squad ││ BMAD ││   HVE   │
  │  Eng.   ││       │   │          ││           ││          ││         ││       ││      ││         │
  │ ─────── ││ ───── │   │ ──────── ││ ───────── ││ ──────── ││ ─────── ││ ───── ││ ──── ││ ─────── │
  │ Rules   ││ Bash  │   │5-step    ││Skills +   ││Change-   ││Spec +   ││Multi- ││Full  ││RPI +    │
  │ files   ││ loop  │   │workflow  ││TDD +      ││centric   ││plan +   ││agent  ││agile ││agents   │
  │ only    ││       │   │+ waves   ││subagents  ││+deltas   ││tasks    ││+ mem  ││sim   ││+ govern │
  └─────────┘└───────┘   └──────────┘└───────────┘└──────────┘└─────────┘└───────┘└──────┘└─────────┘
       │         │              │          │           │          │         │        │         │
   Minutes    Minutes        Minutes    Minutes     Minutes    Minutes    Hours    Hours   Hours–Days
       │         │              │          │           │          │         │        │         │
    Any tool   Any CLI      Multi-tool  Multi-tool  Multi-tool Any tool  Copilot  Any tool  Copilot

  ◄── Solo dev, quick projects ──────────────────── Enterprise, governance ──►
  ◄── Low ceremony ──────────────────────────────── High ceremony ──────────►
  ◄── Low predictability ───────────────────────── High predictability ─────►
```

GSD negotiates dispatch against documented host capabilities. The spectrum's “+ waves” label applies where parallel dispatch is available; on Copilot, GSD Core defaults execution to sequential inline mode.

---

## 7. Navigation — deep-dive documents

Each technique has a dedicated deep-dive document following a consistent template (At a Glance → Overview → **Pros & Cons at a Glance** → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Comparison Notes).

### Decision guide

- [Choosing Your Approach](techniques/choosing-your-approach.md) — Which technique for which situation. By team size, project type, industry, and development activity.

### Spec-Driven Development

- [GSD (Get Shit Done)](techniques/gsd.md) — Active successor workflow at `open-gsd/gsd-core`; original repository archived.
- [Spec Kit](techniques/spec-kit.md) — GitHub's experimental SDD toolkit at v0.16.1.
- [OpenSpec](techniques/openspec.md) — Change-centric SDD with delta specs and broad multi-tool support.

### Multi-Agent Orchestration

- [Squad](techniques/squad.md) — Coordinator-based multi-agent orchestration with persistent memory and casting.
- [BMAD](techniques/bmad.md) — AI-driven agile framework with specialized roles and modular workflows.

### Autonomous Iteration

- [Ralph](techniques/ralph.md) — Autonomous bash-loop methodology. Tests as backpressure, git as memory.

### Skill-Based Development

- [Superpowers](techniques/superpowers.md) — Mandatory skills methodology with TDD and review enforcement.

### Enterprise AI-Native SDLC

- [HVE (Hypervelocity Engineering)](techniques/hve.md) — Microsoft ISE's RPI workflow and constraint-based governance.

### Cross-cutting

- [Context Engineering](techniques/context-engineering.md) — The practice of structuring project context via rules files across an 8-layer model.

### Skills ecosystem

- [Skills ecosystem](techniques/skills-ecosystem.md) — Agent Skills, `mattpocock/skills`, skills.sh, Anthropic reference skills, GitHub's Copilot channel, and trust guidance.

## 8. Projects to consider next

These projects are relevant to the August 8, 2026 landscape, but they are not Tier 1 methodologies.

| Priority | Projects | Why to watch |
|----------|----------|--------------|
| Must consider | [OpenHands](https://github.com/OpenHands/OpenHands), [Open SWE](https://github.com/langchain-ai/open-swe), [Goose](https://github.com/aaif-goose/goose), [Cline](https://github.com/cline/cline) | Active products, platforms, runtimes, or architectures. None exposed a portable methodology in this research pass. Open SWE had no releases or tags. |
| Maybe | Aider, OpenCode, Continue, Kilo Code, Pythagora/GPT Pilot, Roo Code | Significant ecosystem substrates or historically important coding-agent workflows. Include if future research finds distinct methodology beyond tool usage. Roo Code also needs verification because the observed repo was archived. |
| Watchlist | AutoGPT, SWE-agent | Important autonomous-agent lineage and benchmark/repair-agent context, but broader or less freshly verified than the core comparison scope. |

OpenHands is now past 1.0, Goose moved to the `aaif-goose` organization, and Cline ships separate core and desktop release trains. These status changes do not by themselves justify methodology pages.
