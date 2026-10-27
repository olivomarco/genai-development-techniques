# Context engineering

## At a glance

| Field              | Value                         |
|--------------------|-------------------------------|
| Full Name          | Context Engineering (practice/discipline) |
| Category           | Cross-Cutting Practice        |
| Source             | Community-driven; no single repository |
| Author/Org         | Popularized by Andrej Karpathy (June 2025); widely adopted across the AI development community |
| License            | N/A (practice, not software)  |
| First Released     | Emerged mid-2025 as a named discipline; underlying practices date to 2023–2024 |
| Current Version    | N/A (evolving practice)       |
| Stars / Popularity | No dedicated repo — the practice permeates every major AI development framework |
| Supported Tools    | All: Claude Code (CLAUDE.md), Cursor (.cursorrules), GitHub Copilot (copilot-instructions.md), Gemini, and any tool supporting context/rules files |

## Compatible coding agents

Context engineering is a universal practice — any agent that supports rules files or system-level instructions benefits from it.

| Agent | Support |
|-------|--------|
| GitHub Copilot (VS Code) | ✅ via `copilot-instructions.md` and `.github/instructions/` |
| GitHub Copilot Coding Agent (github.com) | ✅ via `copilot-instructions.md` |
| Claude Code | ✅ via `CLAUDE.md` and `.claude/rules/` |
| Cursor | ✅ via `.cursorrules` and `.cursor/rules/` |
| Windsurf | ✅ via rules files |
| OpenAI Codex (CLI) | ✅ via `AGENTS.md` |
| Gemini CLI | ✅ via `.gemini/` |
| Roo Code | ✅ via `.roo/` rules |

## Overview

Context engineering is the practice of structuring, curating, and managing the information in an AI model's context window. Prompt engineering focuses on individual prompts; context engineering also covers the rules, retrieved files, memory, and tool outputs supplied throughout a task.

Andrej Karpathy described it in June 2025: "The LLM is a CPU, the context window is RAM, and you are the operating system responsible for loading exactly the right information for each task."

Context engineering is a practice, not a framework or product. GSD, BMAD, Squad, HVE, Ralph, and Spec Kit apply it in different ways. You can also use rules files and curated context without adopting a framework.

## Pros & cons at a glance

| Pros | Cons |
|------|------|
| ✅ Universal — works with every AI coding tool | ❌ No structure by itself — a practice, not a workflow |
| ✅ Low setup cost — create a rules file in 5 minutes | ❌ Rules files remain fragmented across tools |
| ✅ Compounds over time — knowledge accumulates in rules files | ❌ Quality depends entirely on the practitioner's curation |
| ✅ Foundation for other techniques — GSD, BMAD, Squad, and HVE each implement it differently | ❌ No built-in quality gates or enforcement mechanisms |
| ✅ Version-controllable — lives in git, reviewed in PRs | ❌ Birgitta Böckeler's warning: "Illusion of control" — AI may still ignore instructions |
| ✅ Model-portable — principles transfer across LLM families | ❌ Invisible when done well — hard to demonstrate or get buy-in for |

> Context engineering supplies the project information and constraints that agents need, through rules files, memory, retrieved material, and tool outputs.

## Core concepts

- **Context rot** — The gradual degradation of AI output quality as context windows fill up during long sessions. This is the core problem that every framework in this comparison attempts to solve, whether through fresh windows (GSD, Ralph), phased workflows (HVE), or structured memory files (Squad).
- **Where this sits in the three-layer model** — Runtimes and methodologies curate context for the model (see the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology)). The model still has to apply the supplied instructions. That model describes who manages context; the 8-layer model below describes where context comes from within a session.
- **The 8-layer context model** — Context arrives at an AI agent through multiple layers, each under different control:
  1. **System/platform instructions** (set by the AI provider)
  2. **Organization rules** (set by IT/admin)
  3. **Project rules** (committed to the repo — copilot-instructions.md, .cursorrules, CLAUDE.md)
  4. **Directory-scoped rules** (subfolder-specific instructions)
  5. **User preferences** (personal settings, local overrides)
  6. **Session context** (conversation history, current task)
  7. **Retrieved context** (files, docs, search results pulled in by the agent)
  8. **Tool outputs** (results from MCP servers, terminal commands, API calls)
- **Prompt-as-code** — Treating prompts and rules files as source code: version-controlled, reviewed, tested, and iterated.
- **Model-specific preferences** — Different model families (Claude, GPT, Gemini) respond differently to the same context. Context engineering requires understanding these differences rather than assuming one-size-fits-all.
- **Context budget** — The finite capacity of the context window. Select the information needed for the task rather than loading everything available.

## How it works

Context engineering operates through rules files — persistent, version-controlled documents that AI tools read before every session. Each major tool has its own format:

| Tool | Rules File | Scoping |
|------|-----------|---------|
| Claude Code | `CLAUDE.md`, `.claude/rules/` | Project → directory → user → organization |
| Cursor | `.cursorrules`, `.cursor/rules/` | Project → user (with glob-based file scoping) |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` | Repo-wide → path-specific (via glob frontmatter) |
| Gemini | `.gemini/` | Project-level |

Rules files remain tool-specific, but skills packaging has converged further. [Agent Skills](https://agentskills.io) now defines a vendor-neutral `SKILL.md` format with progressive disclosure: discovery, activation, then execution. The shared `.agents/skills/` path is also emerging through the `skills` CLI and OpenSpec's vendor-neutral `agents` target.

This convergence applies to packaging, not complete execution semantics. In the `skills` CLI compatibility matrix observed on August 8, 2026, basic skills worked across all 18 compared agents, `allowed-tools` across 16, hooks across 4, and `context: fork` in 1. Treat skills as a portable context-delivery layer with runtime-specific capabilities.

**Runtime behavior matters.** A thin harness such as [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent), a roughly 100-line agent loop, passes context through with little independent interpretation. Claude Code and GitHub Copilot add retrieval, summarization, permission checks, and state management ([Claude Code docs](https://code.claude.com/docs/en/overview)). The same `CLAUDE.md` or `copilot-instructions.md` content can therefore produce different behavior across runtimes.

**Practical implementation layers:**

1. **Project context** — Define what the project is, its tech stack, coding conventions, architecture patterns. Every team member (human or AI) reads this.
2. **Role context** — Define what each AI agent should know about its responsibilities. Used by multi-agent frameworks (Squad charters, BMAD personas, HVE agent instructions).
3. **Task context** — Define the specific work to be done. Specs, plans, issue descriptions, acceptance criteria.
4. **Memory context** — What the agent should remember from prior sessions. Decision logs (Squad), progress files (Ralph), research docs (HVE).
5. **Constraint context** — What the agent must NOT do. Security rules, forbidden patterns, quality gates.

**Key research findings that shaped the practice (as of 2026):**

- "Think step by step" now *hurts* reasoning models (GPT-5's router handles reasoning internally).
- Long prompts degrade performance — reasoning quality drops around 3,000 tokens of instructions.
- Few-shot chain-of-thought no longer improves reasoning; it's only useful for format alignment.
- Over-prompting with too many examples can hurt performance (arXiv:2509.13196).
- Zero-shot should be tried before reaching for few-shot.
- Production applications should pin to specific model snapshots, as router behavior changes between versions.

## Strengths

- **Portable principles.** Context curation, budgeting, and scoping apply across AI coding tools, even where formats and behavior differ.
- **Low barrier to entry.** Creating a `CLAUDE.md` or `.cursorrules` file requires no installation, no framework, and no dependencies. A developer can start in five minutes.
- **Compounds over time.** Well-maintained rules files accumulate project knowledge that benefits every session and every team member, human or AI.
- **Useful across frameworks.** GSD's fresh windows, Squad's charters, HVE's instructions, and Ralph's prompt files all apply context-engineering principles.
- **Version-controllable.** Rules files live in git and can be reviewed in PRs. Their history records which instructions changed, though it does not guarantee reproducible agent behavior.
- **Model-portable.** While specific file formats differ between tools, the underlying principles (curate context, manage the budget, scope appropriately) are universal.

## Limitations

- **No structure by itself.** Context engineering is a practice, not a workflow. It tells you *what* to put in the window but not *when* or *how* to organize a development process around it.
- **Fragmented rules, uneven skill semantics.** Rules files still use tool-specific locations and scoping. Agent Skills standardizes packaging, but optional features and execution behavior vary by runtime.
- **Quality depends on the practitioner.** A poorly maintained `CLAUDE.md` with outdated information or conflicting instructions can actively degrade AI output. The practice requires ongoing curation.
- **No built-in quality gates.** Unlike HVE's validated artifacts or GSD's verification phases, context engineering alone provides no mechanism to check that the AI followed the rules correctly.
- **Partial standardization.** Agent Skills provides a canonical format and implementor guidance for reusable skill packages. Broader context-engineering practices, rules files, and certification remain fragmented.
- **Invisible when done well.** Context engineering is hard to demonstrate or showcase because its success looks like "the AI just worked." This makes it harder to get organizational buy-in compared to frameworks with visible workflows.

## Best for

- **Any developer using AI coding tools** who wants to improve output quality without adopting a full framework.
- **Teams evaluating frameworks** — understanding context engineering clarifies what each framework actually does and helps compare them on equal footing.
- **Multi-tool environments** where the team uses different AI tools across projects or team members and needs a portable skill.
- **Early-stage projects** where a lightweight rules file is sufficient and a full framework would be premature.
- **Organizations building custom AI workflows** who want to design their own approach from first principles.

## Not ideal for

- **Teams that need a complete development methodology** — context engineering is a skill, not a process. It won't tell you how to decompose work, manage agents, or run reviews.
- **Developers who want a turnkey solution** — there's no installer, no CLI, no single repo to clone.
- **Projects requiring governance and audit trails** — context engineering provides no enforcement mechanism. Combine with HVE, BMAD, or Squad for governance needs.
- **Situations where the problem is workflow, not context** — if the issue is how work is organized rather than what the AI knows, a framework like GSD or BMAD is the right answer.

## Community & ecosystem

Context engineering has no single community hub. Resources include:

- **Key voices:** Andrej Karpathy (foundational framing), the-ai-corner.com (guides), fungies.io (developer guides), Thomas Wiegold (best practices blog).
- **Academic research:** arXiv:2509.13196 on the effects of over-prompting with examples.
- **Community resources:** cursor.directory (community-shared Cursor rules), copilot-instructions.md templates in GitHub docs, various CLAUDE.md examples shared on GitHub.
- **Documentation quality:** Scattered. Each tool documents its own rules file format. No unified documentation for context engineering as a discipline exists.
- **Ecosystem maturity:** The underlying practice is established. Rules remain fragmented, while the skills layer now has a published vendor-neutral specification and an emerging shared install path.
- **Industry adoption:** Universal — every team using AI coding tools practices context engineering to some degree, whether they use the term or not.
- **Educational resources:** [Denis2054/Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems) — an active book companion repo with roughly 251 stars, 85 forks, MCP integration, and workshop material — is a useful community educational resource, but not a dominant framework. No dominant "context engineering framework" has emerged; the practice remains diffuse and is increasingly embedded inside concrete systems such as GSD runtime-specific skills, Spec Kit extension catalogs, Squad governed memory, Superpowers skills, and HVE instruction collections.

## Comparison notes

**vs. GSD:** GSD Core applies context engineering in a five-step workflow, using fresh task context and verification gates.

**vs. Squad:** Squad uses charter files, decision ledgers, agent histories, and routing rules for persistent multi-agent context. It adds orchestration that context engineering alone does not provide.

**vs. HVE:** HVE implements context engineering through repository-level instruction collections, the RPI phased workflow, and constraint-based governance. HVE's research phase directly applies the context engineering principle that AI should gather verified information before acting. Among the Tier 1 techniques, HVE is the dedicated enterprise implementation of these practices.

**vs. Superpowers:** Superpowers supplies methodology, constraints, and workflows through composable skills. Its ~2K-token bootstrap and on-demand CLI skill loading manage context use. It adds mandatory TDD, code review, and development sequencing to the underlying context-engineering practice.

**vs. the skills ecosystem:** Context engineering is the broad discipline. [Agent Skills and skill libraries](skills-ecosystem.md) package selected context into discoverable, reusable units. A library delivers capabilities; a methodology such as Superpowers adds sequencing and enforcement.

**vs. the three-layer model:** Context engineering is not itself a runtime or a methodology — it's the practice of curating what layer two (the runtime) and layer three (the methodology) feed to layer one (the model). See the [overview's three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology) for how model capability, execution runtime, and development methodology interact, and the [decision rule in Choosing Your Approach](choosing-your-approach.md#layer-check-model-runtime-or-methodology-first) for when a rules file is enough versus when it needs a methodology layered on top.
