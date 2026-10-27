# GenAI development techniques

A comparison of techniques, methodologies, and frameworks for organizing and directing AI coding agents. It focuses on development practices, not the models or tools themselves.

## What this site covers

AI-assisted development is shifting from standalone frameworks toward models, runtimes, reusable skills, and governance controls that work together. This site compares those layers using dated research findings. It is not a ranking or an adoption survey.

---

## Start here

**[Choosing Your Approach](techniques/choosing-your-approach.md)** — Match a technique to your team size, project type, industry, and development activity.

**[Overview and comparison matrix](overview.md)** — Executive summary, full comparison table, and category analysis.

---

## Detailed guides

### Guide

| Document | Description |
|----------|-------------|
| [Overview](overview.md) | Executive summary, three-layer model, comparison matrix, and category analysis |
| [Choosing Your Approach](techniques/choosing-your-approach.md) | Which technique for which situation — by team size, project type, industry, methodology, and task type |
| [Research Methodology](methodology.md) | How this comparison is researched, inclusion criteria, evidence labels, and update policy |

### Spec-driven development

Star counts are snapshots observed on October 27, 2026. They are awareness signals, not adoption evidence.

| Technique | Description | Stars |
|-----------|-------------|-------|
| [GSD (Get Shit Done)](techniques/gsd.md) | Spec-driven workflow continued as GSD Core after the original repository was archived | ~10.9K* |
| [Spec Kit](techniques/spec-kit.md) | GitHub's official toolkit for spec-driven development — specs → plans → tasks | ~143K |
| [OpenSpec](techniques/openspec.md) | Change-centric SDD with delta specs, broad multi-tool support, and a vendor-neutral skills target | ~73K |

\* GSD migrated from an archived repository with ~64.7K stars to `open-gsd/gsd-core`; the successor repository started its own count.

### Multi-agent orchestration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Squad](techniques/squad.md) | Coordinator-based multi-agent orchestration with persistent memory, casting, and ceremonies | ~3.3K |
| [BMAD](techniques/bmad.md) | AI-driven agile framework with specialized roles, structured phases, and modular workflows | ~55K |

### Skill-based development

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Superpowers](techniques/superpowers.md) | Mandatory skills methodology — TDD, subagent-driven development, and review enforcement | ~306K |

### Autonomous iteration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Ralph](techniques/ralph.md) | Autonomous bash-loop methodology — tests as backpressure, git as memory, tool-agnostic | Community |

### Enterprise AI-native SDLC

| Technique | Description | Stars |
|-----------|-------------|-------|
| [HVE](techniques/hve.md) | Microsoft ISE's RPI workflow with constraint-based governance and a growing repository-level skills inventory | ~1.6K |

### Cross-cutting

| Technique | Description |
|-----------|-------------|
| [Context Engineering](techniques/context-engineering.md) | The practice of structuring project context via rules files across an 8-layer model |

### Skills and agent frameworks

These pages cover the infrastructure and libraries that support the techniques above. Superpowers is listed under skill-based development because it adds a mandatory workflow.

| Document | Description |
|----------|-------------|
| [State of the Skills Market](techniques/skills-ecosystem.md) | Market overview, taxonomy, and the shift toward versioned, managed skill packages |
| [Skill Libraries](techniques/skills-libraries.md) | `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections |
| [Orchestrating Modes](techniques/skills-orchestrating-modes.md) | `pstack/poteto-mode`, canonical-source and port-drift caveats |
| [Distribution and Governance](techniques/skills-management.md) | Agent Skills specification, marketplaces vs. vendored installs, provenance, permissions, and rollout guidance |
| [Choosing a Skills Approach](techniques/skills-choosing.md) | Decision guide across libraries, orchestrating modes, methodologies, and native runtimes |

---

**Audience:** Developers, tech leads, and engineering managers evaluating structured approaches to AI-assisted development.

The [Decision Guide](overview.md#4-decision-guide) provides a short selection table.
