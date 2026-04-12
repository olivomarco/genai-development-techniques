# Context Engineering

## At a Glance

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

## Compatible Coding Agents

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

Context engineering is the practice of structuring, curating, and managing the information that fills an AI model's context window during development. It has replaced "prompt engineering" as the core skill for AI-assisted software development. The shift is significant: prompt engineering focuses on crafting individual prompts; context engineering focuses on building systems that consistently deliver the right information to the right agent at the right time.

Andrej Karpathy articulated the foundational mental model in June 2025: "The LLM is a CPU, the context window is RAM, and you are the operating system responsible for loading exactly the right information for each task." This framing recast the developer's role — from someone who writes clever prompts to someone who designs information architectures for AI agents.

Context engineering is not a framework, a tool, or a product. It is a cross-cutting discipline that underlies every framework in this comparison. GSD, BMAD, Squad, HVE, Ralph, Spec Kit, and MetaGPT all implement context engineering in their own ways. Understanding context engineering as a standalone practice helps developers make informed choices about which framework to adopt — or whether to build their own approach from first principles.

## Core Concepts

- **Context rot** — The gradual degradation of AI output quality as context windows fill up during long sessions. This is the core problem that every framework in this comparison attempts to solve, whether through fresh windows (GSD, Ralph), phased workflows (HVE), or structured memory files (Squad).
- **The 8-layer context model** — Context arrives at an AI agent through multiple layers, each under different control:
  1. **System/platform instructions** (set by the AI provider)
  2. **Organization rules** (set by IT/admin)
  3. **Project rules** (committed to the repo — CLAUDE.md, .cursorrules, copilot-instructions.md)
  4. **Directory-scoped rules** (subfolder-specific instructions)
  5. **User preferences** (personal settings, local overrides)
  6. **Session context** (conversation history, current task)
  7. **Retrieved context** (files, docs, search results pulled in by the agent)
  8. **Tool outputs** (results from MCP servers, terminal commands, API calls)
- **Prompt-as-code** — Treating prompts and rules files as source code: version-controlled, reviewed, tested, and iterated.
- **Model-specific preferences** — Different model families (Claude, GPT, Gemini) respond differently to the same context. Context engineering requires understanding these differences rather than assuming one-size-fits-all.
- **Context budget** — The finite capacity of the context window. Context engineering is fundamentally about allocation: which information earns its place in the window, and which doesn't.

## How It Works

Context engineering operates through rules files — persistent, version-controlled documents that AI tools read before every session. Each major tool has its own format:

| Tool | Rules File | Scoping |
|------|-----------|---------|
| Claude Code | `CLAUDE.md`, `.claude/rules/` | Project → directory → user → organization |
| Cursor | `.cursorrules`, `.cursor/rules/` | Project → user (with glob-based file scoping) |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` | Repo-wide → path-specific (via glob frontmatter) |
| Gemini | `.gemini/` | Project-level |

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

- **Universal applicability.** Context engineering works with every AI coding tool. It's the one practice that transfers completely between Claude Code, Cursor, Copilot, and any future tool.
- **Low barrier to entry.** Creating a `CLAUDE.md` or `.cursorrules` file requires no installation, no framework, and no dependencies. A developer can start in five minutes.
- **Compounds over time.** Well-maintained rules files accumulate project knowledge that benefits every session and every team member, human or AI.
- **Foundation for everything else.** Understanding context engineering makes every framework in this comparison more effective. It's the "why" behind GSD's fresh windows, Squad's charters, HVE's instructions, and Ralph's prompt files.
- **Version-controllable.** Rules files live in git, are reviewed in PRs, and evolve with the project. This makes AI behavior auditable and reproducible.
- **Model-portable.** While specific file formats differ between tools, the underlying principles (curate context, manage the budget, scope appropriately) are universal.

## Limitations

- **No structure by itself.** Context engineering is a practice, not a workflow. It tells you *what* to put in the window but not *when* or *how* to organize a development process around it.
- **Fragmented tooling.** Each AI tool has its own rules file format, location, and scoping mechanism. There is no universal standard, requiring parallel maintenance for multi-tool teams.
- **Quality depends on the practitioner.** A poorly maintained `CLAUDE.md` with outdated information or conflicting instructions can actively degrade AI output. The practice requires ongoing curation.
- **No built-in quality gates.** Unlike HVE's validated artifacts or GSD's verification phases, context engineering alone provides no mechanism to check that the AI followed the rules correctly.
- **Limited community standardization.** While resources exist (fungies.io, the-ai-corner.com, Karpathy's talks), there is no canonical reference or certification. Best practices are still emerging and vary widely.
- **Invisible when done well.** Context engineering is hard to demonstrate or showcase because its success looks like "the AI just worked." This makes it harder to get organizational buy-in compared to frameworks with visible workflows.

## Best For

- **Any developer using AI coding tools** who wants to improve output quality without adopting a full framework.
- **Teams evaluating frameworks** — understanding context engineering clarifies what each framework actually does and helps compare them on equal footing.
- **Multi-tool environments** where the team uses different AI tools across projects or team members and needs a portable skill.
- **Early-stage projects** where a lightweight rules file is sufficient and a full framework would be premature.
- **Organizations building custom AI workflows** who want to design their own approach from first principles.

## Not Ideal For

- **Teams that need a complete development methodology** — context engineering is a skill, not a process. It won't tell you how to decompose work, manage agents, or run reviews.
- **Developers who want a turnkey solution** — there's no installer, no CLI, no single repo to clone.
- **Projects requiring governance and audit trails** — context engineering provides no enforcement mechanism. Combine with HVE, BMAD, or Squad for governance needs.
- **Situations where the problem is workflow, not context** — if the issue is how work is organized rather than what the AI knows, a framework like GSD or BMAD is the right answer.

## Community & Ecosystem

Context engineering is practiced universally but has no single community hub:

- **Key voices:** Andrej Karpathy (foundational framing), the-ai-corner.com (guides), fungies.io (developer guides), Thomas Wiegold (best practices blog).
- **Academic research:** arXiv:2509.13196 on the effects of over-prompting with examples.
- **Community resources:** cursor.directory (community-shared Cursor rules), various CLAUDE.md examples shared on GitHub, copilot-instructions.md templates in GitHub docs.
- **Documentation quality:** Scattered. Each tool documents its own rules file format. No unified documentation for context engineering as a discipline exists.
- **Ecosystem maturity:** The underlying practice is mature and battle-tested, but the discipline's identity as "context engineering" is recent (mid-2025). Standardization is in its early stages.
- **Industry adoption:** Universal — every team using AI coding tools practices context engineering to some degree, whether they use the term or not.

## Comparison Notes

**vs. GSD:** GSD is an explicit implementation of context engineering principles in a structured 6-step workflow. GSD's fresh-agent-per-task pattern and verification gates are specific context engineering decisions packaged into a repeatable process. Context engineering is the "why"; GSD is one "how."

**vs. Squad:** Squad implements context engineering through charter files, decision ledgers, agent history files, and routing rules — a persistent memory system designed for multi-agent coordination. Context engineering principles explain why Squad's architecture works; Squad provides the orchestration layer that context engineering alone lacks.

**vs. HVE:** HVE implements context engineering through 102 instruction files, the RPI phased workflow, and constraint-based governance. HVE's research phase is a direct application of the context engineering principle that AI should gather verified information before acting. HVE is the most comprehensive implementation of context engineering in an enterprise setting among the Tier 1 techniques.
