# GenAI Development Techniques — Overview & Comparison

---

## 1. Executive Summary

The landscape of AI-assisted software development has matured dramatically by April 2026. What began as raw prompting and "vibe coding" has evolved into a rich ecosystem of structured methodologies, multi-agent frameworks, and enterprise-grade workflows — all designed to make AI coding agents more predictable, productive, and safe at scale. The core shift is philosophical: developers are no longer asking "can AI write code?" but "how do I *direct* AI to write the *right* code, reliably, every time?" The answer, across every technique studied, is some form of specification-first thinking combined with disciplined context engineering.

Eight distinct approaches have emerged as Tier 1 techniques, spanning four categories. **Spec-driven development** (GSD, Spec Kit) focuses on defining exactly what you want before the AI builds it. **Multi-agent orchestration** (Squad, BMAD, MetaGPT) simulates development teams with specialized AI agents working in parallel. **Autonomous iteration** (Ralph) takes the radical approach of running AI agents in a bash loop overnight, using tests as backpressure. **Enterprise AI-native SDLC** (HVE) brings constraint-based governance and validated artifacts to the development lifecycle. Underneath them all sits **context engineering** — the cross-cutting discipline of curating what information fills the AI's context window.

The choice between these approaches is not about which is "best" — it's about matching the technique to your situation. A solo developer prototyping a weekend project has fundamentally different needs than an enterprise team shipping regulated software with audit requirements. This document provides the data and decision frameworks to make that match.

---

## 2. Comparison Matrix

All scores are derived from the research findings. Where a technique spans a range, the most representative value is used.

| Dimension | GSD | BMAD | Spec Kit | Squad | Ralph | HVE | MetaGPT | Context Engineering |
|-----------|-----|------|----------|-------|-------|-----|---------|---------------------|
| **Approach** | Spec-Driven | Multi-Agent | Spec-Driven | Multi-Agent | Autonomous Iteration | Enterprise SDLC | Multi-Agent | Practice |
| **Human Control** | Semi-autonomous | HITL | HITL | Semi-autonomous | AFK / HITL | Phased | Semi-autonomous | HITL |
| **Setup Complexity** | Minutes | Hours | Minutes | Hours | Minutes | Hours–Days | Hours | Minutes |
| **Tool Compatibility** | Multi-tool (Claude Code primary, community ports) | Multi-tool (Claude Code, Cursor, Windsurf) | Multi-tool (Copilot, Claude Code, Gemini CLI, Cursor) | Single-tool (GitHub Copilot) | Tool-agnostic (any AI CLI) | Single-tool (GitHub Copilot) | Tool-agnostic (API-based) | Tool-agnostic (all tools) |
| **Scale** | Solo–Small team | Solo–Enterprise | Solo–Small team | Small team–Enterprise | Solo | Large team–Enterprise | Small team | Solo–Enterprise |
| **Predictability** | High | High | Medium–High | Medium | Low–Medium | High | Medium | Varies by implementation |
| **Context Management** | Fresh agent per task; waves for parallelism | Agent personas + structured workflows | Spec files as context anchor | Charter files + decision ledger + history | Fresh context each loop iteration; git as memory | Clear context between RPI phases; research docs persist in files | SOP-driven context per role | Rules files layered by scope (8-layer model) |
| **Quality Gates** | Moderate (verification per phase) | Comprehensive (QA agent, readiness checks, retros) | Moderate (analyze + checklist commands) | Moderate (reviewer rejection protocol, ceremonies) | Basic (tests/linting as backpressure) | Comprehensive (validated artifacts, lint/build/test, review phase) | Moderate (QA role in SOP pipeline) | None (practice, not a system) |
| **Governance** | Light | Moderate | Light | Moderate (decisions ledger, reviewer lockout) | None | Heavy (constraint-based, audit trails, policy-as-code) | Light | None |
| **Learning Curve** | Medium | High | Low–Medium | Medium–High | Low | High | Medium–High | Low |
| **Ecosystem Maturity** | Established (51K stars, active community) | Established (44K stars, Discord, docs site) | Growing (GitHub-backed, v0.6.0) | Growing (Microsoft employee project, SDK + CLI) | Growing (official plugin, community forks, VentureBeat coverage) | Established (Microsoft ISE, 23 releases, Learn hub) | Established (academic origins, large community) | Established (cross-tool standard practice) |
| **Cost** | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for AI tool) | Free (API costs for Copilot sub) | Free (API costs — can be high for long loops) | Free (Copilot subscription) | Free (API costs) | Free |
| **Open Source** | Yes (MIT) | Partial (open source, trademark on name) | Yes (GitHub official) | Yes (MIT) | Yes (technique is open; plugin is official) | Yes (MIT) | Yes (open source) | Yes (community-driven) |

---

## 3. GitHub Star History

Frameworks with GitHub repositories — star growth over time:

[![Star History Chart](https://api.star-history.com/svg?repos=gsd-build/get-shit-done,bmad-code-org/BMAD-METHOD,github/spec-kit,bradygaster/squad,microsoft/hve-core,FoundationAgents/MetaGPT&type=Date)](https://star-history.com/#gsd-build/get-shit-done&bmad-code-org/BMAD-METHOD&github/spec-kit&bradygaster/squad&microsoft/hve-core&FoundationAgents/MetaGPT&Date)

*Ralph and Context Engineering are not included — Ralph is a technique (no central repo), and Context Engineering is a cross-tool practice.*

---

## 4. Decision Guide

| If you want... | Use | Why |
|----------------|-----|-----|
| The simplest possible setup | **Ralph** | A bash one-liner. No framework, no dependencies, no configuration. Define a prompt, run the loop. |
| Structured solo development with clear phases | **GSD** | 6-step workflow (new → discuss → plan → execute → verify → complete) with fresh agents per task. 51K stars for a reason. |
| A full agile team simulation | **BMAD** | 12+ specialized agent personas, 34+ workflows, scale-adaptive intelligence. The most comprehensive agile framework. |
| GitHub-backed spec-driven development | **Spec Kit** | GitHub's official SDD toolkit. Works with Copilot, Claude Code, Gemini CLI. Minimal footprint, strong institutional backing. |
| Parallel multi-agent orchestration with persistent memory | **Squad** | Named agents with charters, shared decisions, ceremonies, and Ralph-style work monitoring. Conway's Law for AI teams. |
| Enterprise governance and audit trails | **HVE** | Microsoft ISE's constraint-based RPI workflow with 49 agents, validated artifacts, and policy-as-code. Built for regulated environments. |
| An academic/SOP-driven approach with full company simulation | **MetaGPT** | Software company simulation via standardized operating procedures. PM → Architect → Engineer → QA pipeline. |
| To improve any AI tool's output without adopting a framework | **Context Engineering** | Rules files (.cursorrules, CLAUDE.md, copilot-instructions.md) work everywhere. Start here before committing to a framework. |
| To run AI agents overnight on mechanical tasks | **Ralph** | AFK mode with max iteration cap. Y Combinator teams shipped 6+ repos overnight for $297 in API costs. |
| Tool-agnostic methodology that works with any AI CLI | **Ralph** or **Context Engineering** | Ralph works with any CLI that doesn't cap tool calls. Context engineering practices apply to every tool. |

---

## 5. Category Summaries

### Spec-Driven Development — GSD, Spec Kit

Spec-driven development (SDD) is the most intuitive response to the chaos of unstructured AI coding: write down what you want before the AI builds it. **GSD** is the community champion — 51K GitHub stars, a 6-step slash-command workflow, and a "Lean Orchestrator" that spawns fresh agents per task to avoid context rot. It was built for Claude Code but has community ports for other tools. **Spec Kit** is GitHub's official entry — a lighter-weight toolkit that organizes projects around `.specify/` directories with specs, plans, and tasks. Where GSD is opinionated and comprehensive, Spec Kit is minimal and agent-agnostic. Both share the conviction that disciplined specification prevents the "AI assumed what I wanted" failure mode.

### Multi-Agent Orchestration — Squad, BMAD, MetaGPT

Multi-agent systems simulate development teams where each AI agent has a specialized role. **BMAD** is the heavyweight — 44K stars, 12+ named agent personas (PM, Architect, Dev, QA), scale-adaptive intelligence, and an extensible module ecosystem. It's the closest to a full agile shop simulation. **Squad** takes a different approach: a coordinator spawns named agents in parallel, with persistent memory (charters, decisions, history files) and structured ceremonies. It's tightly integrated with GitHub Copilot and includes a built-in work monitor (Ralph) for continuous pipeline management. **MetaGPT** comes from the academic side — it codifies software development as standardized operating procedures (SOPs), with the philosophy "Code = SOP(Team)." All three prove that structuring AI collaboration produces better results than a single AI working alone, though they trade simplicity for coordination overhead.

### Autonomous Iteration — Ralph

Ralph stands alone in its category: a bash one-liner that runs an AI coding agent in a loop, using tests as backpressure and git commits as memory between iterations. Created by Geoffrey Huntley and named after Ralph Wiggum from *The Simpsons* ("keep going despite always making mistakes"), it's the philosophical opposite of enterprise frameworks. There is no governance, no agent roles, no structured phases — just a prompt, a loop, and a test suite. Its power lies in simplicity and overnight productivity: set it running before bed, wake up to completed features. The trade-off is unpredictability — Huntley himself calls it "deterministically bad in a nondeterministic world" — and it works best on greenfield projects with clear completion criteria.

### Enterprise AI-Native SDLC — HVE

Hypervelocity Engineering (HVE) is the enterprise end of the spectrum. Created by Microsoft's ISE team from lessons learned shipping 140+ AI solutions, it embeds AI agents across the entire development lifecycle through the RPI workflow: Research (investigate and document), Plan (create coordinated task files), Implement (execute with verification), Review (validate against plan). With 49 agents, 102 instructions, and 10 domain-specific collections, HVE provides constraint-based governance where "constraints enable safe autonomy." It's designed for multi-stack enterprise environments (no-code to pro-code) and trades setup simplicity for repeatable, auditable, governable AI-assisted development. The key insight: separating research from implementation changes the AI's optimization target from "plausible code" to "verified truth."

### Cross-Cutting: Context Engineering

Context engineering is not a framework — it's the foundational practice that every framework implements differently. Popularized by Andrej Karpathy's analogy ("the LLM is a CPU, the context window is RAM, and you are the operating system"), it's the discipline of curating exactly what fills the AI's context window. In practice, this manifests as an 8-layer model from system instructions down to auto-memory, implemented through tool-specific rules files: `.cursorrules` (Cursor), `CLAUDE.md` (Claude Code), `copilot-instructions.md` (GitHub Copilot), and `AGENTS.md`. GSD solves context rot through fresh agents per task. Ralph solves it through fresh loops. HVE clears context between RPI phases. The specific mechanism varies, but the principle is universal: what you put in the context window matters more than how you phrase the prompt.

---

## 6. Complexity vs. Speed Spectrum

```
                        COMPLEXITY vs. SPEED SPECTRUM
                        ─────────────────────────────

  Less Setup                                                    More Setup
  Faster Start                                                  More Structure
  ◄─────────────────────────────────────────────────────────────────────────►

       │         │              │          │         │        │         │
       ▼         ▼              ▼          ▼         ▼        ▼         ▼
  ┌─────────┐┌───────┐   ┌──────────┐┌─────────┐┌───────┐┌──────┐┌─────────┐
  │ Context ││ Ralph │   │   GSD    ││Spec Kit ││ Squad ││ BMAD ││   HVE   │
  │  Eng.   ││       │   │         ││         ││       ││      ││         │
  │ ─────── ││ ───── │   │ ─────── ││ ─────── ││ ───── ││ ──── ││ ─────── │
  │ Rules   ││ Bash  │   │6-step   ││Spec +   ││Multi- ││Full  ││RPI +    │
  │ files   ││ loop  │   │workflow ││plan +   ││agent  ││agile ││49 agents│
  │ only    ││       │   │+ waves  ││tasks    ││+ mem  ││sim   ││+ govern │
  └─────────┘└───────┘   └──────────┘└─────────┘└───────┘└──────┘└─────────┘
       │         │              │          │         │        │         │
   Minutes    Minutes        Minutes    Minutes    Hours    Hours   Hours–Days
       │         │              │          │         │        │         │
    Any tool   Any CLI     Claude Code+  Any tool  Copilot  Any tool  Copilot
                                ports

  ◄── Solo dev, quick projects ──────────────────── Enterprise, governance ──►
  ◄── Low ceremony ──────────────────────────────── High ceremony ──────────►
  ◄── Low predictability ───────────────────────── High predictability ─────►
```

*MetaGPT sits between Squad and BMAD on this spectrum — SOP-driven with moderate setup and a full company simulation model.*

---

## 7. Navigation — Deep-Dive Documents

Each technique has a dedicated deep-dive document following a consistent template (At a Glance → Overview → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Comparison Notes).

### Spec-Driven Development

- [GSD (Get Shit Done)](techniques/gsd.md) — Meta-prompting, context engineering, and spec-driven dev. 51K stars.
- [Spec Kit](techniques/spec-kit.md) — GitHub's official SDD toolkit. Specs → plans → tasks.

### Multi-Agent Orchestration

- [Squad](techniques/squad.md) — Coordinator-based multi-agent orchestration with persistent memory and casting.
- [BMAD](techniques/bmad.md) — AI-driven agile framework with 12+ specialized agent personas.
- [MetaGPT](techniques/metagpt.md) — SOP-based software company simulation. Code = SOP(Team).

### Autonomous Iteration

- [Ralph](techniques/ralph.md) — Autonomous bash-loop methodology. Tests as backpressure, git as memory.

### Enterprise AI-Native SDLC

- [HVE (Hypervelocity Engineering)](techniques/hve.md) — Microsoft ISE's RPI workflow with 49 agents and constraint-based governance.

### Cross-Cutting

- [Context Engineering](techniques/context-engineering.md) — The practice of structuring project context via rules files across an 8-layer model.

### Supporting Documents

- [Research Scope](research-scope.md) — Full technique inventory, taxonomy, and comparison dimensions.
- [comparisons/spec-driven-vs-multi-agent.md](comparisons/spec-driven-vs-multi-agent.md) — Category comparison.
- [comparisons/solo-dev-vs-team.md](comparisons/solo-dev-vs-team.md) — Scale comparison.
- [comparisons/open-source-vs-commercial.md](comparisons/open-source-vs-commercial.md) — Licensing comparison.
- [appendix/tools-landscape.md](appendix/tools-landscape.md) — Tier 2 tools reference (Cursor, Claude Code, Copilot, Aider, Cline, OpenHands, SWE-Agent).
- [appendix/glossary.md](appendix/glossary.md) — Terms: SDD, MCP, SOP, RPI, HITL, AFK, etc.
