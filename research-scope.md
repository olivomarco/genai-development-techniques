# GenAI Development Techniques — Research Scope

**Scoped by:** Neo (Lead / Research Architect)  
**Requested by:** Marco Olivo  
**Date:** 2026-04-12  
**Status:** APPROVED — scope finalized by Marco

---

## 1. What This Project Is

A comprehensive comparison of techniques, methodologies, and frameworks that help developers use AI coding assistants more effectively, predictably, and at scale. The focus is on **how humans organize and direct AI-assisted development** — not on the AI models or LLMs themselves.

### Guiding Question

> "If I want to ship production software using AI coding agents, what structured approaches exist, how do they compare, and which should I use for my situation?"

---

## 2. Techniques Identified

### Tier 1 — Primary Subjects (Deep-Dive Documents)

| # | Name | Full Name / Meaning | Category | Source | One-Line Description |
|---|------|---------------------|----------|--------|----------------------|
| 1 | **GSD** | Get Shit Done | Spec-Driven Methodology | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) (51.1k stars) | Meta-prompting, context engineering, and spec-driven dev system for reliable AI development across Claude Code, Cursor, and other agents. |
| 2 | **BMAD** | Build More Architect Dreams | Multi-Agent Methodology | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) / docs.bmad-method.org | AI-driven agile framework with specialized agent roles (Analyst, PM, Architect, Dev, QA), scale-adaptive intelligence, and 34+ workflows. |
| 3 | **Spec Kit** | Spec Kit (GitHub) | Spec-Driven Toolkit | [github/spec-kit](https://github.com/github/spec-kit) | GitHub's open-source toolkit for spec-driven development; works with Copilot, Claude Code, and Gemini CLI. Specs → plans → implementation tasks. |
| 4 | **Squad** | Squad | Agent Orchestration System | [bradygaster/squad](https://github.com/bradygaster/squad) | Coordinator-based multi-agent orchestration with persistent memory, casting, ceremonies, and work routing for AI development teams. |
| 5 | **Ralph** | Ralph Wiggum | Autonomous Iteration Methodology | [ghuntley.com/ralph](https://ghuntley.com/ralph/) (Geoffrey Huntley) | Autonomous bash-loop methodology for iterating AI coding agents across multiple context windows; tool-agnostic, uses tests as backpressure and git as memory. |
| 6 | **HVE** | Hypervelocity Engineering | Enterprise AI-Native SDLC | [microsoft/hve-core](https://github.com/microsoft/hve-core) (919 stars, MIT) | Microsoft ISE's enterprise methodology with the RPI workflow (Research → Plan → Implement → Review), 49 agents, 102 instructions, and constraint-based governance. |
| 7 | **MetaGPT** | MetaGPT | Multi-Agent Framework | [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Open-source framework simulating a software company (PM, Architect, Engineer, QA) using SOPs. Philosophy: Code = SOP(Team). |
| 8 | **Context Engineering** | Context Engineering (Practice) | Development Practice | Community-driven / cross-tool | The practice of structuring project context via rules files (CLAUDE.md, .cursorrules, copilot-instructions.md, AGENTS.md) across an 8-layer model to steer AI agents. |

### Tier 2 — Supporting Subjects (Covered in Overview, Not Deep-Dive)

| # | Name | Category | Why Tier 2 |
|---|------|----------|------------|
| 9 | **Cursor Agent Mode** | AI IDE Feature | Implementation surface with rules files; not a methodology itself |
| 10 | **GitHub Copilot Agent Mode** | AI IDE Feature | Platform feature, not a methodology |
| 11 | **Claude Code** | AI Coding Tool | Tool that supports methodologies (GSD, etc.), not a methodology itself |
| 12 | **Aider** | AI Pair Programming | Terminal-based pair programming tool; lightweight, no structured methodology |
| 13 | **Cline** | AI Coding Assistant | IDE-based autonomous coding assistant |
| 14 | **OpenHands** | Autonomous Agent Platform | Open platform for AI software developers |
| 15 | **SWE-Agent** | Research Agent | Princeton/Stanford research-grade coding agent |

### Out of Scope

| Name | Why Excluded |
|------|-------------|
| LangGraph / LangChain | General-purpose agent orchestration, not specifically for AI-assisted *development* |
| CrewAI | Role-based agent automation for business processes, not dev-focused |
| AutoGen | Conversational multi-agent for research/enterprise, not dev methodology |
| Semantic Kernel | Enterprise .NET integration framework |

---

## 3. Taxonomy

```
┌─────────────────────────────────────────────────────────────┐
│              GenAI Development Techniques                   │
├──────────────┬──────────────┬───────────────┬───────────────┤
│ Spec-Driven  │ Multi-Agent  │ Autonomous    │ Enterprise    │
│ Development  │ Orchestration│ Iteration     │ AI-Native     │
│              │              │               │ SDLC          │
│ • GSD        │ • Squad      │ • Ralph       │ • HVE         │
│ • Spec Kit   │ • BMAD       │               │               │
│              │ • MetaGPT    │               │               │
├──────────────┴──────────────┴───────────────┴───────────────┤
│ Cross-Cutting: Context Engineering                          │
│ (Rules files, memory, project context management)           │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Document Structure

### 4.1 Repository Layout

```text
comparison/
├── README.md                          # Project overview + navigation
├── research-scope.md                  # This file (scope + inventory)
├── overview.md                        # Executive summary + comparison matrix
│
├── techniques/
│   ├── gsd.md                         # GSD deep-dive
│   ├── bmad.md                        # BMAD deep-dive
│   ├── spec-kit.md                    # Spec Kit deep-dive
│   ├── squad.md                       # Squad deep-dive
│   ├── ralph.md                       # Ralph (Wiggum) deep-dive
│   ├── hve.md                         # HVE (Hypervelocity Engineering) deep-dive
│   ├── metagpt.md                     # MetaGPT deep-dive
│   └── context-engineering.md         # Context Engineering practices
│
├── comparisons/
│   ├── spec-driven-vs-multi-agent.md  # Category comparison
│   ├── open-source-vs-commercial.md   # Licensing/access comparison
│   └── solo-dev-vs-team.md            # Scale comparison
│
└── appendix/
    ├── tools-landscape.md             # Tier 2 tools reference
    └── glossary.md                    # Terms: SDD, MCP, SOP, RPI, etc.
```

### 4.2 Per-Technique Document Template

Each deep-dive in `techniques/` follows this consistent format:

```markdown
# {Technique Name}

## At a Glance
| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          |                               |
| Category           | Spec-Driven / Multi-Agent / Autonomous Iteration / Enterprise SDLC / Practice |
| Source              | GitHub repo / website         |
| Author/Org         |                               |
| License            |                               |
| First Released     |                               |
| Current Version    |                               |
| Stars / Popularity |                               |
| Supported Tools    | Claude Code, Cursor, Copilot, etc. |

## Overview
What it is, why it exists, the problem it solves.

## Core Concepts
Key ideas, terminology, and mental model.

## How It Works
Step-by-step workflow. Diagrams where helpful.

## Strengths
What it does well. Evidence where available.

## Limitations
Known weaknesses, gaps, trade-offs.

## Best For
Ideal use cases, team sizes, project types.

## Not Ideal For
When to avoid this technique.

## Community & Ecosystem
Adoption, community size, documentation quality, ecosystem maturity.

## Comparison Notes
How it differs from the 2-3 most similar techniques (cross-references).
```

### 4.3 Overview Document Structure

`overview.md` contains:

1. **Executive Summary** — The landscape in 2-3 paragraphs
2. **Comparison Matrix** — All Tier 1 techniques scored across dimensions
3. **Decision Guide** — "If you want X, use Y" flowchart/table
4. **Category Summaries** — One paragraph per category
5. **Links** — To all deep-dive documents

---

## 5. Comparison Dimensions

| Dimension | What We're Measuring |
|-----------|---------------------|
| **Approach** | Spec-driven vs. agent-orchestrated vs. autonomous iteration vs. enterprise SDLC |
| **Human Control** | How much the developer stays in the loop (HITL vs. AFK vs. phased) |
| **Setup Complexity** | Time from zero to productive |
| **Tool Compatibility** | Which AI coding tools it works with (tool-agnostic vs. locked-in) |
| **Scale** | Solo developer → enterprise team |
| **Predictability** | How deterministic/repeatable are the results |
| **Context Management** | How it handles LLM context window limits (fresh windows, phases, memory files) |
| **Quality Gates** | Built-in review, testing, or verification steps |
| **Governance** | Constraint enforcement, audit trails, policy-as-code |
| **Learning Curve** | How long to become productive |
| **Ecosystem Maturity** | Docs, community, plugins, integrations |
| **Cost** | Free / API costs / subscription |
| **Open Source** | Licensing and extensibility |

---

## 6. Research Priorities

### Phase 1 — Core techniques (highest priority)
GSD, BMAD, Spec Kit, Squad — the most widely adopted.

### Phase 2 — Distinct paradigms
Ralph, HVE, Context Engineering — each represents a fundamentally different approach.

### Phase 3 — Supporting framework
MetaGPT — the academic/open-source multi-agent approach.

### Phase 4 — Cross-cutting comparisons
Category comparisons, decision guide, and the overview matrix.

---

## 7. What's Explicitly Out of Scope

- **LLM model comparisons** (GPT-4 vs Claude vs Gemini) — well-covered elsewhere
- **General prompt engineering** — too broad, not methodology-specific
- **Business agent frameworks** (CrewAI, AutoGen for non-dev tasks) — different domain
- **IDE feature comparisons** (Cursor vs Windsurf as products) — covered elsewhere; we reference their methodology features only
- **Pricing analysis** — changes too fast to be useful in a static document
