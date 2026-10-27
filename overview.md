# GenAI development techniques — overview and comparison

---

## 1. Executive summary

As of October 27, 2026, AI-assisted development spans structured methodologies, multi-agent frameworks, autonomous loops, and enterprise workflows. The central question is no longer whether an agent can write code, but how you direct it with repeatable context, artifacts, verification, and governance.

The comparison retains ten Tier 1 approaches across five categories, with **context engineering** as a cross-cutting practice.

Alongside them sits the [skills ecosystem](techniques/skills-ecosystem.md). Reusable skills are becoming versioned, updatable packages instead of loose file collections.

Two channels distribute them. Cross-agent installer CLIs — skills.sh's `npx skills` — vendor editable files into any agent. Native plugin marketplaces, such as those for Claude Code, GitHub Copilot, and Codex, auto-update a managed bundle inside one runtime instead. `mattpocock/skills` and `addyosmani/agent-skills` ship through both paths; pick one per agent, because installing both duplicates every skill.

Some libraries now bundle an orchestrating mode alongside their skills. `pstack/poteto-mode` (canonically the `pstack/` directory in [`cursor/plugins`](https://github.com/cursor/plugins)) reads an incoming request, selects from a set of playbooks, and dispatches the library's other skills as each step needs them. That blurs the line between a skill library and a workflow framework.

What's missing: signing, attestation, and lockfile-style pinning. Most of what we examined lacks all three. None of this makes the skills layer an eleventh technique or a sixth methodology category — it's market infrastructure the methodologies above increasingly plug into. Star counts remain dated awareness signals; they do not establish production adoption.

The choice between these approaches is not about which is "best" — it's about matching the technique to your situation. A solo developer prototyping a weekend project has fundamentally different needs than an enterprise team shipping regulated software with audit requirements. This document provides the data and decision frameworks to make that match.

### The three-layer model: model, runtime, methodology

Every setup in this comparison stacks three layers, and the techniques below only occupy the top one:

1. **Model capability** — what the underlying LLM can reason about, plan, and execute reliably, holding everything else constant.
2. **Execution runtime / harness** — the tool loop around the model: context assembly, tool calls, retries and recovery, permissions, sandboxing, and state across turns. This layer itself spans a range:
   - **No harness** — direct API calls; the caller writes the loop.
   - **Thin generic harness** — a deliberately minimal, model-agnostic loop, such as [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent), a roughly 100-line agent built as a hackable research baseline rather than a product.
   - **First-party runtime** — a vendor-maintained product such as Claude Code, Codex CLI, or GitHub Copilot, which bundles tool access, sandboxing, approval modes, and multi-turn state behind a single surface.
3. **Development methodology** — the structured process layered on top: GSD's phases, Squad's charters, HVE's RPI workflow, BMAD's agile simulation, and so on. This is what the rest of this document compares, including the fourth harness variant: an **opinionated methodology**, which adds mandatory sequencing or enforcement (Superpowers' mandatory skills, HVE's constraint-based gates) on top of whichever runtime executes it.

**Our view.** As models improve, checkable tasks need less rigid upfront workflow. For a bounded repository task with a clear check — tests, lint, a reviewable diff — a capable model inside a competent runtime increasingly plans and sequences tools on its own, work that used to require an explicit methodology layer.

That doesn't make execution harnesses unnecessary, and it doesn't make every harness thin. First-party runtimes hide this work rather than remove it. Claude Code and Codex CLI still manage sandboxing, approval modes, and conversation state on your behalf ([Claude Code docs](https://code.claude.com/docs/en/overview); [Codex CLI](https://github.com/openai/codex)). They just don't require you to write that logic yourself the way a thin harness does. The structure moved; it didn't disappear.

**What the headline numbers do and don't say.** METR's time-horizon figures measure task *difficulty at a fixed success threshold*, not unattended autonomy or merge-ready work. The figure is the length of task, measured by human completion time, that a model can complete at a given reliability — commonly 50%.

METR fits a logistic success curve against human task duration and reports where that curve crosses the chosen probability. The method says nothing about whether a human reviewer would accept the output.

METR also ran a companion study of SWE-bench Verified PRs. Roughly half of the patches that passed the automated grader were not actually merged by real maintainers, even after adjusting for noise in human review. Benchmark graders miss regressions, style drift, and incomplete fixes. Agents, unlike human contributors, were not given a chance to revise after feedback.

Treat any single capability figure — time horizon, benchmark score, vendor-reported repository result — as one data point about task difficulty. None of them is a verdict on unattended autonomy or mergeability.

**Current examples, with caveats.** GPT-6 Astra and Claude Opus 5.5 are the current frontier models most often cited for strong repository-task results. Each result comes from the vendor's own agent runtime, not a bare model call, so it reflects the runtime as much as the model. No same-harness, same-benchmark comparison between the two exists that we could find. No independent METR-style time-horizon figure exists for either exact model at the time of writing. Read vendor-reported repository scores as a lower-confidence signal shaped by the runtime that produced them, not an independently reproduced capability measurement.

**A practical decision rule:**

1. Start with the model and its native runtime (Claude Code, Codex CLI, Copilot, or similar) — for a task that's bounded, clearly specified, and independently checkable, this is often sufficient on its own.
2. Add skills when the gap is reusable expertise the model doesn't reliably apply — a missing convention, a domain pattern, a house style.
3. Add a methodology when the gap is coordination or decision traceability — multiple agents, multiple people, or a need to reconstruct *why* a change was made.
4. Strengthen controls — governance, audit trails, approval gates, cost caps — as autonomy, task duration, blast radius, or compliance risk rises, not by default.

This rule doesn't replace the comparison below; it explains when reaching for a row in it is worth the overhead that row documents. See [Choosing Your Approach](techniques/choosing-your-approach.md#layer-check-model-runtime-or-methodology-first) for this rule applied scenario by scenario.

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
| **Ecosystem Maturity** | Active successor v1.19.0; archived predecessor retained its metrics | v6.12.4; active modules and community | v1.2.3; GitHub-backed, past 1.0, composable extensions | v1.15.0 stable; prerelease channel exists | v1.1.0 stable; v2.0.0 prerelease channel active | Canonical guide is static; ralph-orchestrator v2.10.1 | v7.0.1; large audience and active releases | v3.2.2 stable; v3.3 prereleases and newer repo activity | Established practice; skills packaging now standardized |
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
> The table below is a quick reference. The full guide covers solo developers, teams of 3, teams of 10, regulated environments (finance, healthcare, government), agile workflows, brownfield vs. greenfield, and more. Before picking a row, run the [layer check](techniques/choosing-your-approach.md#layer-check-model-runtime-or-methodology-first): confirm the model and its native runtime can't already do the job before adding a methodology on top.

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
| Reusable skills without a mandatory methodology | **[Skills and Agent Frameworks](techniques/skills-ecosystem.md)** | Choose a library, installer, and distribution model independently of your development process — see [Choosing a Skills Approach](techniques/skills-choosing.md). |
| To run AI agents overnight on mechanical tasks | **Ralph** | AFK mode with max-iteration and cost caps. |
| Lightweight spec-driven development for existing codebases | **OpenSpec** | Brownfield-first, change-centric workflow with delta specs and broad multi-tool support. |
| Tool-agnostic methodology that works with any AI CLI | **Ralph** or **Context Engineering** | Ralph works with any CLI that doesn't cap tool calls. Context engineering practices apply to every tool. |

---

## 5. Category summaries

### Spec-Driven Development — GSD, Spec Kit, OpenSpec

**GSD Core** continues the archived original project with a five-step loop and a multi-runtime installer. **Spec Kit** is GitHub's project-level specification toolkit, now past 1.0 at v1.2.3 with composable extensions for integrations, hooks, and bundled bug-fixing and idea-assessment processes. **OpenSpec** is the v1.15.0 brownfield specialist, using change folders and delta specs, and now ships standalone binaries that don't require Node.js. OpenSpec writes vendor-neutral skills to `.agents/skills/`, but remains a spec-driven methodology rather than a skills library.

### Skill-Based Development — Superpowers

Superpowers uses skills as mandatory workflow controls. Version 7.0.1 rebuilt its brainstorming skill to size work after it understands the request, delegate design review to a subagent that reads the spec as its future builder, and ship as a native Antigravity Marketplace plugin. This differs from `mattpocock/skills`, `addyosmani/agent-skills`, and other independently selectable libraries that offer capabilities without an enforced lifecycle.

### Multi-Agent Orchestration — Squad, BMAD

**BMAD** uses specialized roles, structured phases, and modules; v6.12.4 followed v6.12.0, which moved Build's ceremony decision to after it investigates a change and added evidence-backed review triage. **Squad** reached 1.0 in October and sits at v1.1.0 stable, with a v2.0.0 prerelease channel already hardening GitHub Actions workflow (`gh-aw`) lifecycle integration. Both trade simplicity for coordination.

### Autonomous Iteration — Ralph

Ralph stands alone in its category: a bash one-liner that runs an AI coding agent in a loop, using tests as backpressure and git commits as memory between iterations. Created by Geoffrey Huntley and named after Ralph Wiggum from *The Simpsons* ("keep going despite always making mistakes"), it's the philosophical opposite of enterprise frameworks. There is no governance, no agent roles, no structured phases — just a prompt, a loop, and a test suite. Its power lies in simplicity and overnight productivity: set it running before bed, wake up to completed features. The trade-off is unpredictability — Huntley himself calls it "deterministically bad in a nondeterministic world" — and it works best on greenfield projects with clear completion criteria.

### Enterprise AI-Native SDLC — HVE

HVE is the enterprise end of the spectrum. Its latest stable release remains v3.2.2, while v3.3 prereleases and newer repository activity exist separately. The August 8 repository tree contained 70 agent files, 80 instruction files, 67 prompt files, and 58 `SKILL.md` files; these counts were not re-verified for this update and should not be read as current stable-package contents.

### Cross-cutting: Context Engineering

Context engineering remains the foundational practice. Rules files are still fragmented by tool, but skills packaging has converged on the vendor-neutral [Agent Skills](https://agentskills.io) specification. Basic skill content is portable; optional features and execution semantics still vary across runtimes.

### Skills and Agent Frameworks

The [skills market](techniques/skills-ecosystem.md) sits beside the methodology taxonomy. Agent Skills defines the format; `mattpocock/skills`, `addyosmani/agent-skills`, and `anthropics/skills` supply content (see [Skill Libraries](techniques/skills-libraries.md)); skills.sh and native plugin marketplaces (Claude Code, Copilot, Codex) provide discovery, installation, and updates (see [Distribution and Governance](techniques/skills-management.md)); runtimes execute the result. The two distribution paths carry different trade-offs: a plugin marketplace keeps a bundle current automatically but hands upstream changes to you unreviewed, while a CLI-vendored copy (`npx skills@latest add ...`) stays editable but only updates when you ask. Some libraries now blur further into framework territory — `pstack/poteto-mode`, distributed as the `pstack/` directory in [`cursor/plugins`](https://github.com/cursor/plugins), reads a request and dispatches across 23 playbooks and the library's other skills, acting as an orchestrating layer rather than a single capability (see [Orchestrating Modes](techniques/skills-orchestrating-modes.md)). Provenance remains immature across all of it: the examined surfaces lacked signing, attestation, and lockfile-style pinning. Superpowers, profiled on its own page, is this category's lead skill-driven methodology. For a decision guide across the whole layer, see [Choosing a Skills Approach](techniques/skills-choosing.md).

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
- [Spec Kit](techniques/spec-kit.md) — GitHub's official SDD toolkit at v1.2.3.
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

### Skills and Agent Frameworks

- [State of the Skills Market](techniques/skills-ecosystem.md) — Taxonomy, what's changing, and links into the rest of this category.
- [Skill Libraries](techniques/skills-libraries.md) — `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections.
- [Orchestrating Modes](techniques/skills-orchestrating-modes.md) — `pstack/poteto-mode`, canonical-source and port-drift caveats.
- [Superpowers](techniques/superpowers.md) — Mandatory skills methodology with TDD and review enforcement.
- [Distribution and Governance](techniques/skills-management.md) — Specification, progressive disclosure, marketplaces vs. vendored installs, provenance, and rollout guidance.
- [Choosing a Skills Approach](techniques/skills-choosing.md) — Decision guide across the whole skills layer.

## 8. Further reading

- [Research Methodology](methodology.md) — How this comparison is researched, evidence labels, and update policy.
- [Market Updates](market-updates.md) — Dated log of research passes and documentation changes.

## 9. Projects to consider next

These projects were relevant to the August 8, 2026 research pass and have not been re-verified for this update; they are not Tier 1 methodologies.

| Priority | Projects | Why to watch |
|----------|----------|--------------|
| Must consider | [OpenHands](https://github.com/OpenHands/OpenHands), [Open SWE](https://github.com/langchain-ai/open-swe), [Goose](https://github.com/aaif-goose/goose), [Cline](https://github.com/cline/cline) | Active products, platforms, runtimes, or architectures. None exposed a portable methodology in this research pass. Open SWE had no releases or tags. |
| Maybe | Aider, OpenCode, Continue, Kilo Code, Pythagora/GPT Pilot, Roo Code | Significant ecosystem substrates or historically important coding-agent workflows. Include if future research finds distinct methodology beyond tool usage. Roo Code also needs verification because the observed repo was archived. |
| Watchlist | AutoGPT, SWE-agent | Important autonomous-agent lineage and benchmark/repair-agent context, but broader or less freshly verified than the core comparison scope. |

OpenHands is now past 1.0, Goose moved to the `aaif-goose` organization, and Cline ships separate core and desktop release trains. These status changes do not by themselves justify methodology pages.
