# GenAI Development Techniques — Comparison

A comprehensive, evidence-based comparison of techniques, methodologies, and frameworks for structured AI-assisted software development. The focus is on **how humans organize and direct AI coding agents** — not on the AI models or tools themselves.

---

## Start Here

**[Overview & Comparison Matrix](overview.md)** — Executive summary, full comparison table, decision guide, and category analysis.

---

## Deep-Dive Documents

### Spec-Driven Development
| Technique | Description | Stars |
|-----------|-------------|-------|
| [GSD (Get Shit Done)](techniques/gsd.md) | Meta-prompting, context engineering, and spec-driven dev system for reliable AI development | ~51K |
| [Spec Kit](techniques/spec-kit.md) | GitHub's official toolkit for spec-driven development — specs → plans → tasks | Growing |

### Multi-Agent Orchestration
| Technique | Description | Stars |
|-----------|-------------|-------|
| [Squad](techniques/squad.md) | Coordinator-based multi-agent orchestration with persistent memory, casting, and ceremonies | Growing |
| [BMAD](techniques/bmad.md) | AI-driven agile framework with 12+ specialized agent personas and 34+ workflows | ~44K |
| [MetaGPT](techniques/metagpt.md) | Open-source SOP-based software company simulation (PM, Architect, Engineer, QA) | Large |

### Autonomous Iteration
| Technique | Description | Stars |
|-----------|-------------|-------|
| [Ralph](techniques/ralph.md) | Autonomous bash-loop methodology — tests as backpressure, git as memory, tool-agnostic | Community |

### Enterprise AI-Native SDLC
| Technique | Description | Stars |
|-----------|-------------|-------|
| [HVE](techniques/hve.md) | Microsoft ISE's RPI workflow with 49 agents, constraint-based governance, and validated artifacts | ~919 |

### Cross-Cutting
| Technique | Description |
|-----------|-------------|
| [Context Engineering](techniques/context-engineering.md) | The practice of structuring project context via rules files across an 8-layer model |

---

## Supporting Documents

- [Research Scope](research-scope.md) — Full technique inventory, taxonomy, and comparison dimensions
- [comparisons/](comparisons/) — Category comparisons (spec-driven vs. multi-agent, solo vs. team, open source vs. commercial)
- [appendix/tools-landscape.md](appendix/tools-landscape.md) — Tier 2 tools reference (Cursor, Claude Code, Copilot, Aider, Cline, etc.)
- [appendix/glossary.md](appendix/glossary.md) — Terminology reference

---

**Audience:** Developers, tech leads, and engineering managers evaluating structured approaches to AI-assisted development.

**What this is not:** A ranking. Each technique serves different needs. The [Decision Guide](overview.md#3-decision-guide) in the overview helps match techniques to situations.
