# GenAI Development Techniques — Overview & Comparison

---

## 1. Executive Summary

The landscape of AI-assisted software development has matured dramatically by June 2026. What began as raw prompting and "vibe coding" has evolved into a rich ecosystem of structured methodologies, multi-agent frameworks, and enterprise-grade workflows — all designed to make AI coding agents more predictable, productive, and safe at scale. The core shift is philosophical: developers are no longer asking "can AI write code?" but "how do I *direct* AI to write the *right* code, reliably, every time?" The answer, across every technique studied, is some form of specification-first thinking combined with disciplined context engineering.

Ten distinct approaches have emerged as Tier 1 techniques, spanning five categories plus one cross-cutting practice. **Spec-driven development** (GSD, Spec Kit, OpenSpec) focuses on defining exactly what you want before the AI builds it. **Multi-agent orchestration** (Squad, BMAD) simulates development teams with specialized AI agents working in parallel. **Autonomous iteration** (Ralph) takes the radical approach of running AI agents in a bash loop overnight, using tests as backpressure. **Skill-based development** (Superpowers) teaches agents reusable behavioral skills — composable modules that enforce TDD, code review, and systematic workflows across any CLI-based AI tool. **Enterprise AI-native SDLC** (HVE) brings constraint-based governance and validated artifacts to the development lifecycle. Underneath them all sits **context engineering** — the cross-cutting discipline of curating what information fills the AI's context window. Superpowers is the largest by community with roughly 234K GitHub stars, reflecting strong demand for disciplined individual workflows.

The choice between these approaches is not about which is "best" — it's about matching the technique to your situation. A solo developer prototyping a weekend project has fundamentally different needs than an enterprise team shipping regulated software with audit requirements. This document provides the data and decision frameworks to make that match.

---

## 2. Comparison Matrix

All scores are derived from the research findings. Where a technique spans a range, the most representative value is used.

| Dimension | GSD | BMAD | Spec Kit | OpenSpec | Squad | Ralph | Superpowers | HVE | Context Engineering |
|-----------|-----|------|----------|---------|-------|-------|-------------|-----|---------------------|
| **Approach** | Spec-Driven | Multi-Agent | Spec-Driven | Spec-Driven | Multi-Agent | Autonomous Iteration | Skill-Based | Enterprise SDLC | Practice |
| **Human Control** | Semi-autonomous | HITL | HITL | HITL | Semi-autonomous | AFK / HITL | Semi-autonomous | Phased | HITL |
| **Setup Complexity** | Minutes | Hours | Minutes | Minutes | Hours | Minutes | Minutes | Hours–Days | Minutes |
| **Tool Compatibility** | Multi-tool (Claude Code primary; official Codex/OpenCode/Gemini-style runtime support plus community ports) | Multi-tool (Claude Code, Cursor, Windsurf, Copilot, Roo Code, Gemini Gems, ChatGPT Custom GPTs) | Multi-tool (Copilot, Claude Code, Gemini CLI, Cursor, Codex CLI, and 20+ more) | Multi-tool (27+ tools: Claude Code, Cursor, Copilot, Codex, Gemini CLI, Windsurf, and more — broadest in comparison) | Single-tool (GitHub Copilot) | Tool-agnostic (any AI CLI) | Multi-tool (Claude Code primary, Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode) | Single-tool (GitHub Copilot) | Tool-agnostic (all tools) |
| **Scale** | Solo–Small team | Solo–Enterprise | Solo–Small team | Solo–Small team | Small team–Enterprise | Solo | Solo–Small team | Large team–Enterprise | Solo–Enterprise |
| **Predictability** | High | High | Medium–High | Medium–High | Medium | Low–Medium | High | High | Varies by implementation |
| **Context Management** | Fresh agent per task; waves for parallelism | Agent personas + structured workflows | Spec files as context anchor | Change folders as context anchor; spec deltas track requirement evolution | Charter files + decision ledger + history | Fresh context each loop iteration; git as memory | Skill files as behavioral modules; token-light bootstrap (~2K tokens); lazy skill loading via CLI search; subagents for implementation | Clear context between RPI phases; research docs persist in files | Rules files layered by scope (8-layer model) |
| **Quality Gates** | Moderate (verification per phase) | Comprehensive (QA agent, readiness checks, retros) | Moderate (analyze + checklist commands) | Moderate (proposal approval, validate --strict, verify command) | Moderate (reviewer rejection protocol, ceremonies) | Basic (tests/linting as backpressure) | Comprehensive (mandatory skills, TDD enforcement, two-stage code review, pressure-tested compliance) | Comprehensive (validated artifacts, lint/build/test, review phase) | None (practice, not a system) |
| **Governance** | Light | Moderate | Light | Light | Moderate (decisions ledger, reviewer lockout) | None | Light | Heavy (constraint-based, audit trails, policy-as-code) | None |
| **Learning Curve** | Medium | High | Low–Medium | Low | Medium–High | Low | Medium | High | Low |
| **Ecosystem Maturity** | Established (~64K stars, active community, v1.42.3) | Established (~49K stars, Discord, docs site, v6.8.0) | Growing fast (GitHub-backed, ~114K stars, v0.11.3, still pre-1.0) | Established (~56K stars, 59 contributors, Discord, v1.4.1, YC W26) | Growing (~2.8K stars, Microsoft employee project, v0.10.0, SDK + CLI) | Growing (canonical guide is stable; ralph-orchestrator active at v2.9.3) | Established (~234K stars, active Discord, Prime Radiant backing, v6.0.3) | Established (Microsoft ISE, v3.2.2, active repo, Learn hub) | Established (cross-tool standard practice) |
| **Cost** | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for Copilot sub) | Free (API costs — can be high for long loops) | Free (API costs for AI tool) | Free (Copilot subscription) | Free |
| **Open Source** | Yes (MIT) | Partial (open source, trademark on name) | Yes (GitHub official) | Yes (MIT) | Yes (MIT) | Yes (technique is open; plugin is official) | Yes (MIT) | Yes (MIT) | Yes (community-driven) |

---

## 3. GitHub Star History

Frameworks with GitHub repositories — star growth over time:

[![Star History Chart](https://api.star-history.com/svg?repos=gsd-build/get-shit-done,bmad-code-org/BMAD-METHOD,github/spec-kit,Fission-AI/OpenSpec,bradygaster/squad,obra/superpowers,microsoft/hve-core&type=timeline)](https://star-history.com/#gsd-build/get-shit-done&bmad-code-org/BMAD-METHOD&github/spec-kit&Fission-AI/OpenSpec&bradygaster/squad&obra/superpowers&microsoft/hve-core&timeline)

*Ralph and Context Engineering are not included — Ralph is a technique (no central repo), and Context Engineering is a cross-tool practice.*

---

## 4. Decision Guide

> **For a comprehensive decision guide by team size, project type, industry, and development activity, see [Choosing Your Approach](techniques/choosing-your-approach.md).**
>
> The table below is a quick reference. The full guide covers solo developers, teams of 3, teams of 10, regulated environments (finance, healthcare, government), agile workflows, brownfield vs. greenfield, and more.

| If you want... | Use | Why |
|----------------|-----|-----|
| The simplest possible setup | **Ralph** | A bash one-liner. No framework, no dependencies, no configuration. Define a prompt, run the loop. |
| Structured solo development with clear phases | **GSD** | 6-step workflow (new → discuss → plan → execute → verify → complete) with fresh agents per task. ~64K stars for a reason. |
| A full agile team simulation | **BMAD** | 12+ specialized agent personas, 34+ workflows, scale-adaptive intelligence. The most comprehensive agile framework. |
| GitHub-backed spec-driven development | **Spec Kit** | GitHub's official SDD toolkit. Works with Copilot, Claude Code, Gemini CLI. Minimal footprint, strong institutional backing. |
| Parallel multi-agent orchestration with persistent memory | **Squad** | Named agents with charters, shared decisions, ceremonies, and Ralph-style work monitoring. Conway's Law for AI teams. |
| Enterprise governance and audit trails | **HVE** | Microsoft ISE's constraint-based RPI workflow with 49 agents, validated artifacts, and policy-as-code. Built for regulated environments. |
| To improve any AI tool's output without adopting a framework | **Context Engineering** | Rules files (copilot-instructions.md, .cursorrules, CLAUDE.md) work everywhere. Start here before committing to a framework. |
| A disciplined individual workflow with TDD and reusable skills | **Superpowers** | ~234K stars. Composable skills enforce systematic development. Works with Claude Code, Cursor, Codex, and more. |
| To run AI agents overnight on mechanical tasks | **Ralph** | AFK mode with max iteration cap. Y Combinator teams shipped 6+ repos overnight for $297 in API costs. |
| Lightweight spec-driven development for existing codebases | **OpenSpec** | Brownfield-first, change-centric workflow with delta specs. 27+ tool support — broadest in comparison. ~56K stars, YC W26. |
| Broadest AI tool compatibility with spec-driven workflow | **OpenSpec** | 27+ tools natively supported. Propose → Apply → Archive workflow with spec deltas for reviewing intent, not just code. |
| Tool-agnostic methodology that works with any AI CLI | **Ralph** or **Context Engineering** | Ralph works with any CLI that doesn't cap tool calls. Context engineering practices apply to every tool. |

---

## 5. Category Summaries

### Spec-Driven Development — GSD, Spec Kit, OpenSpec

Spec-driven development (SDD) is the most intuitive response to the chaos of unstructured AI coding: write down what you want before the AI builds it. **GSD** is the community champion — ~64K GitHub stars, a 6-step workflow, and a "Lean Orchestrator" that spawns fresh agents per task to avoid context rot. It was built for Claude Code and now has more substantial official multi-runtime support, especially Codex CLI, alongside community ports. **Spec Kit** is GitHub's official entry — a lighter-weight toolkit that organizes projects around `.specify/` directories with specs, plans, and tasks. It is still pre-1.0, but at ~114K stars and v0.11.3 it is no longer as nascent as the April snapshot implied. **OpenSpec** is the brownfield specialist — a YC-backed (W26) CLI from Fission AI with ~56K stars and the widest tool support in the comparison (27+ tools). Its change-centric workflow organizes development around individual changes rather than tasks or projects, using delta specs with ADDED/MODIFIED/REMOVED markers to track intent evolution. Where GSD is opinionated and greenfield-focused, Spec Kit is comprehensive and agent-agnostic, and OpenSpec is lightweight and brownfield-first. All three share the conviction that disciplined specification prevents the "AI assumed what I wanted" failure mode.

### Skill-Based Development — Superpowers

Superpowers introduces a distinct paradigm: rather than defining specifications or orchestrating agent teams, it teaches AI agents reusable behavioral *skills* — composable modules that encode development practices like TDD, code review, debugging, and architecture planning. With ~234K GitHub stars (the largest community in this comparison), Superpowers provides a token-light bootstrap (~2K tokens) that lazily loads skills on demand via CLI search, keeping context lean while enforcing rigorous methodology. The framework is built for Claude Code but officially supports Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode. Its quality gates are comprehensive: mandatory skills enforce TDD, two-stage code review, and pressure-tested compliance. Subagents handle implementation while the orchestrating agent maintains architectural oversight, with current scratch/progress state under `.superpowers/sdd/`. The trade-off is individual focus — Superpowers enhances a single developer's discipline rather than coordinating teams.

### Multi-Agent Orchestration — Squad, BMAD

Multi-agent systems simulate development teams where each AI agent has a specialized role. **BMAD** is the heavyweight — ~49K stars, 12+ named agent personas (PM, Architect, Dev, QA), scale-adaptive intelligence, and an extensible module ecosystem that now includes `bmad-spec` for compact intent distillation and `bmad-ux` for design and experience contracts. It's the closest to a full agile shop simulation. **Squad** takes a different approach: a coordinator spawns named agents in parallel, with persistent memory (charters, decisions, history files) and structured ceremonies. Version 0.10.0 added state backend maturity, governed memory, import/export, RAI review, and MCP/frontmatter improvements while staying tightly integrated with GitHub Copilot. Both prove that structuring AI collaboration produces better results than a single AI working alone, though they trade simplicity for coordination overhead.

### Autonomous Iteration — Ralph

Ralph stands alone in its category: a bash one-liner that runs an AI coding agent in a loop, using tests as backpressure and git commits as memory between iterations. Created by Geoffrey Huntley and named after Ralph Wiggum from *The Simpsons* ("keep going despite always making mistakes"), it's the philosophical opposite of enterprise frameworks. There is no governance, no agent roles, no structured phases — just a prompt, a loop, and a test suite. Its power lies in simplicity and overnight productivity: set it running before bed, wake up to completed features. The trade-off is unpredictability — Huntley himself calls it "deterministically bad in a nondeterministic world" — and it works best on greenfield projects with clear completion criteria.

### Enterprise AI-Native SDLC — HVE

Hypervelocity Engineering (HVE) is the enterprise end of the spectrum. Created by Microsoft's ISE team from lessons learned shipping 140+ AI solutions, it embeds AI agents across the entire development lifecycle through the RPI workflow: Research (investigate and document), Plan (create coordinated task files), Implement (execute with verification), Review (validate against plan). With 49 agents, 102 instructions, and 10 domain-specific collections, HVE provides constraint-based governance where "constraints enable safe autonomy." Its latest public release remains v3.2.2, but the repository and adoption have continued moving, with roughly 1.2K stars as of the June 2026 freshness pass. It's designed for multi-stack enterprise environments (no-code to pro-code) and trades setup simplicity for repeatable, auditable, governable AI-assisted development. The key insight: separating research from implementation changes the AI's optimization target from "plausible code" to "verified truth."

### Cross-Cutting: Context Engineering

Context engineering is not a framework — it's the foundational practice that every framework implements differently. Popularized by Andrej Karpathy's analogy ("the LLM is a CPU, the context window is RAM, and you are the operating system"), it's the discipline of curating exactly what fills the AI's context window. In practice, this manifests as an 8-layer model from system instructions down to auto-memory, implemented through tool-specific rules files: `copilot-instructions.md` (GitHub Copilot), `.cursorrules` (Cursor), `CLAUDE.md` (Claude Code), and `AGENTS.md`. GSD solves context rot through fresh agents per task. Ralph solves it through fresh loops. HVE clears context between RPI phases. The specific mechanism varies, but the principle is universal: what you put in the context window matters more than how you phrase the prompt.

---

## 6. Complexity vs. Speed Spectrum

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
  │ Rules   ││ Bash  │   │6-step    ││Skills +   ││Change-   ││Spec +   ││Multi- ││Full  ││RPI +    │
  │ files   ││ loop  │   │workflow  ││TDD +      ││centric   ││plan +   ││agent  ││agile ││49 agents│
  │ only    ││       │   │+ waves   ││subagents  ││+deltas   ││tasks    ││+ mem  ││sim   ││+ govern │
  └─────────┘└───────┘   └──────────┘└───────────┘└──────────┘└─────────┘└───────┘└──────┘└─────────┘
       │         │              │          │           │          │         │        │         │
   Minutes    Minutes        Minutes    Minutes     Minutes    Minutes    Hours    Hours   Hours–Days
       │         │              │          │           │          │         │        │         │
    Any tool   Any CLI     Claude Code+ Multi-tool  27+ tools  Any tool  Copilot  Any tool  Copilot
                                ports

  ◄── Solo dev, quick projects ──────────────────── Enterprise, governance ──►
  ◄── Low ceremony ──────────────────────────────── High ceremony ──────────►
  ◄── Low predictability ───────────────────────── High predictability ─────►
```

---

## 7. Navigation — Deep-Dive Documents

Each technique has a dedicated deep-dive document following a consistent template (At a Glance → Overview → **Pros & Cons at a Glance** → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Comparison Notes).

### Decision Guide

- [Choosing Your Approach](techniques/choosing-your-approach.md) — Which technique for which situation. By team size, project type, industry, and development activity.

### Spec-Driven Development

- [GSD (Get Shit Done)](techniques/gsd.md) — Meta-prompting, context engineering, and spec-driven dev. ~64K stars.
- [Spec Kit](techniques/spec-kit.md) — GitHub's official SDD toolkit. Specs → plans → tasks. ~114K stars.
- [OpenSpec](techniques/openspec.md) — Change-centric SDD with delta specs. Brownfield-first, 27+ tool support. ~56K stars.

### Multi-Agent Orchestration

- [Squad](techniques/squad.md) — Coordinator-based multi-agent orchestration with persistent memory and casting.
- [BMAD](techniques/bmad.md) — AI-driven agile framework with 12+ specialized agent personas.

### Autonomous Iteration

- [Ralph](techniques/ralph.md) — Autonomous bash-loop methodology. Tests as backpressure, git as memory.

### Skill-Based Development

- [Superpowers](techniques/superpowers.md) — Composable skills framework. TDD, subagent-driven development, and self-improving agent workflows. ~234K stars.

### Enterprise AI-Native SDLC

- [HVE (Hypervelocity Engineering)](techniques/hve.md) — Microsoft ISE's RPI workflow with 49 agents and constraint-based governance.

### Cross-Cutting

- [Context Engineering](techniques/context-engineering.md) — The practice of structuring project context via rules files across an 8-layer model.

## 8. Projects to Consider Next

These projects are important to the June 2026 landscape, but they are not promoted to full Tier 1 technique pages yet. Neo's current guidance is to preserve the methodology-first framing and treat most of these as agent platforms, runtimes, or ecosystem substrates until research shows a transferable development methodology.

| Priority | Projects | Why to watch |
|----------|----------|--------------|
| Must consider | OpenHands, Open SWE, Goose, Cline | High-activity autonomous development platforms or asynchronous coding-agent frameworks. They may define the next autonomous workflow category, but need a scope decision because they are closer to products/platforms than portable methodologies. |
| Maybe | Aider, OpenCode, Continue, Kilo Code, Pythagora/GPT Pilot, Roo Code | Significant ecosystem substrates or historically important coding-agent workflows. Include if future research finds distinct methodology beyond tool usage. Roo Code also needs verification because the observed repo was archived. |
| Watchlist | AutoGPT, SWE-agent | Important autonomous-agent lineage and benchmark/repair-agent context, but broader or less freshly verified than the core comparison scope. |

For today, the strongest additions to surface are **OpenHands**, **Open SWE**, **Goose**, and **Cline**. They are worth a scoped research pass before any new full deep-dive is created.
