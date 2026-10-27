# GenAI development techniques — comparison

An evidence-based comparison of techniques, methodologies, and frameworks for structured AI-assisted software development. The focus is on **how humans organize and direct AI coding agents** — not on the AI models or tools themselves.

## TL;DR

AI-assisted development is shifting from standalone frameworks toward a managed stack of frontier models, native runtimes, reusable skills, and governance controls. This site is a dated, evidence-based market map of that stack — not a ranking, and not an adoption survey.

Start with [Choosing Your Approach](techniques/choosing-your-approach.md) to match a technique to your situation, read the [Overview](overview.md) for the full comparison and three-layer model, and check [Market Updates](market-updates.md) for what changed in the most recent research pass.

---

## Start here

**[Choosing Your Approach](techniques/choosing-your-approach.md)** — Which technique fits your situation? Decision guide by team size, project type, industry, and development activity.

**[Overview and comparison matrix](overview.md)** — Executive summary, full comparison table, and category analysis.

---

## Deep-dive documents

### Guide

| Document | Description |
|----------|-------------|
| [Overview](overview.md) | Executive summary, three-layer model, comparison matrix, and category analysis |
| [Choosing Your Approach](techniques/choosing-your-approach.md) | Which technique for which situation — by team size, project type, industry, methodology, and task type |
| [Research Methodology](methodology.md) | How this comparison is researched, inclusion criteria, evidence labels, and update policy |
| [Market Updates](market-updates.md) | Dated log of research passes and the documentation changes that followed them |

### Spec-Driven Development

Star counts are snapshots observed on October 27, 2026. They are awareness signals, not adoption evidence.

| Technique | Description | Stars |
|-----------|-------------|-------|
| [GSD (Get Shit Done)](techniques/gsd.md) | Spec-driven workflow continued as GSD Core after the original repository was archived | ~10.9K* |
| [Spec Kit](techniques/spec-kit.md) | GitHub's official toolkit for spec-driven development — specs → plans → tasks | ~143K |
| [OpenSpec](techniques/openspec.md) | Change-centric SDD with delta specs, broad multi-tool support, and a vendor-neutral skills target | ~73K |

\* GSD migrated from an archived repository with ~64.7K stars to `open-gsd/gsd-core`; the successor repository started its own count.

### Multi-Agent Orchestration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Squad](techniques/squad.md) | Coordinator-based multi-agent orchestration with persistent memory, casting, and ceremonies | ~3.3K |
| [BMAD](techniques/bmad.md) | AI-driven agile framework with specialized roles, structured phases, and modular workflows | ~55K |

### Skill-Based Development

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Superpowers](techniques/superpowers.md) | Mandatory skills methodology — TDD, subagent-driven development, and review enforcement | ~306K |

### Autonomous Iteration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Ralph](techniques/ralph.md) | Autonomous bash-loop methodology — tests as backpressure, git as memory, tool-agnostic | Community |

### Enterprise AI-Native SDLC

| Technique | Description | Stars |
|-----------|-------------|-------|
| [HVE](techniques/hve.md) | Microsoft ISE's RPI workflow with constraint-based governance and a growing repository-level skills inventory | ~1.6K |

### Cross-cutting

| Technique | Description |
|-----------|-------------|
| [Context Engineering](techniques/context-engineering.md) | The practice of structuring project context via rules files across an 8-layer model |

### Skills and Agent Frameworks

This supporting market layer is not an eleventh Tier 1 technique or a sixth methodology category. Superpowers, the layer's lead skill-driven methodology, is profiled above under Skill-Based Development.

| Document | Description |
|----------|-------------|
| [State of the Skills Market](techniques/skills-ecosystem.md) | Market overview, taxonomy, and the shift toward versioned, managed skill packages |
| [Skill Libraries](techniques/skills-libraries.md) | `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections |
| [Orchestrating Modes](techniques/skills-orchestrating-modes.md) | `pstack/poteto-mode`, canonical-source and port-drift caveats |
| [Distribution and Governance](techniques/skills-management.md) | Agent Skills specification, marketplaces vs. vendored installs, provenance, permissions, and rollout guidance |
| [Choosing a Skills Approach](techniques/skills-choosing.md) | Decision guide across libraries, orchestrating modes, methodologies, and native runtimes |

---

**Audience:** Developers, tech leads, and engineering managers evaluating structured approaches to AI-assisted development.

**What this is not:** A ranking. Each technique serves different needs. The [Decision Guide](overview.md#4-decision-guide) in the overview helps match techniques to situations.
