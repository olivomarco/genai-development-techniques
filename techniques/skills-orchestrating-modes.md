# Orchestrating modes

> **Observation date:** October 27, 2026. Playbook counts and port parity are not re-verified every pass — treat specific counts as dated.

An orchestrating mode is a dispatcher: it reads an incoming request, classifies it, and routes to a playbook or skill that does the actual work. It has no standalone function — its entire value is the routing logic layered on top of a library it depends on. This is a distinct category from a composable library (see [Skill Libraries](skills-libraries.md)), a lifecycle library, a native runtime, or a methodology, and this page exists to keep those distinctions clear using the category's lead example.

## Lead example: `pstack` / `poteto-mode`

[`pstack`](https://github.com/cursor/plugins/tree/main/pstack) is maintained by Cursor engineer "poteto" (a member of the React core team) and distributed canonically as the `pstack/` directory inside Cursor's official [`cursor/plugins`](https://github.com/cursor/plugins) marketplace repository. Its README positions the project against the "AI writes too much slop code" critique directly: "throughput without quality is not a goal I aspire to. If you want to go fast, go deep first."

The headline capability is **`poteto-mode`**, installed as `/poteto-mode` (or `/pstack:poteto-mode` once namespaced by a host like Claude Code). It is a dispatcher skill that reads the non-negotiables defined in its own `SKILL.md`, classifies the incoming request — architecture decision, parallel fan-out opportunity, contested design, pre-commit, pre-review — and routes to the matching playbook and skill:

- `architect` — cross-boundary design decisions
- `swarm` — parallel-agent coverage matrices
- `arena` — design bakeoffs between competing approaches
- `interrogate` — multi-model adversarial review before shipping

This read-classify-dispatch loop is the defining trait of the category: `poteto-mode` does nothing on its own. Its value is entirely in routing into `pstack`'s other skills based on context, the same way a lifecycle library's slash commands do work directly.

`poteto-mode` dispatches across a documented set of playbooks and the library's other skills — reported at 23 playbooks in prior research and not re-counted this pass. Treat that figure as a signal of scope, not a current, re-verified count.

### Install paths and port drift

| Host | Install | Caveat |
|---|---|---|
| Cursor (canonical) | `/add-plugin pstack` | The source of truth — other hosts run a generated or adapted copy |
| Claude Code | `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins` | Auto-update is off by default for third-party marketplaces and must be enabled manually in the marketplaces tab |

Claude Code runs a generated, harness-adapted copy of `pstack` from `harness/pstack/` at the repository root, kept in sync by a generator script the project's CI enforces. This matters for a specific reason: **the canonical source is Cursor-shaped**, and the Claude Code port is a derived artifact, not an independent implementation. A step that needs a Cursor-only feature (Bugbot, Automations) is skipped on Claude Code with a one-line note rather than failing — a documented, intentional port-drift point, not a bug. If you adopt `pstack` outside Cursor, verify against the canonical `cursor/plugins` source when behavior looks off, and don't assume feature parity across hosts just because the generator keeps files in sync.

## The unrelated "potato-mode" name collision

`pstack/poteto-mode` is unrelated to **[`aryannaio/potato-mode-agent-skill`](https://github.com/aryannaio/potato-mode-agent-skill)**, a resource-aware Agent Skill for Claude Code and Codex that measures available memory, disk, and CPU headroom and recommends conservative worker limits for test runners and build tools on low-spec or already-busy machines. The two projects share a near-identical spoken name ("poteto" vs. "potato") but solve different problems: `poteto-mode` is a request-classification dispatcher that routes work to other skills; `potato-mode` is a single skill that throttles resource usage for the agent's own commands and explicitly does not touch unrelated processes. Don't conflate them when searching, citing, or installing — they are different authors, different repositories, and different categories (orchestrating mode vs. a single composable skill).

## How this differs from adjacent categories

| Compared to... | The difference |
|---|---|
| **A composable library** ([Skill Libraries](skills-libraries.md)) | A composable library is a menu you choose from yourself. An orchestrating mode chooses for you, based on a read of the request — it adds a decision layer a library doesn't have. |
| **A lifecycle library** | A lifecycle library maps skills to fixed stages you invoke by name (`/spec`, `/build`). An orchestrating mode classifies free-form requests and routes dynamically — there's no fixed command per stage. |
| **A native runtime** | A runtime (Claude Code, Codex CLI, Cursor) executes tool calls and manages sessions; it has no opinion about which skill applies to a request. `poteto-mode` runs inside a runtime and supplies the classification logic the runtime itself doesn't provide. |
| **A methodology** (such as [Superpowers](superpowers.md)) | A methodology enforces a mandatory sequence end to end — you cannot skip brainstorming before planning. `poteto-mode` dispatches per request but does not own a full development lifecycle the way Superpowers does; it is closer to a methodology in spirit than a library, but its dispatch is layered on top of an otherwise-composable set of skills rather than being the entire product. |

## Connection to the long-horizon model thesis

Orchestrating modes are a data point for the site's broader three-layer thesis (see the [overview](../overview.md#the-three-layer-model-model-runtime-methodology)), not a counterexample to it. As models get better at classifying a request's shape themselves, some of what a dispatcher like `poteto-mode` does by hand — "is this an architecture decision or a quick fix?" — becomes something a sufficiently capable model handles inside its own reasoning, reducing the need for an explicit routing skill for simple cases. That does not make orchestrating modes, or harnesses generally, obsolete: `poteto-mode`'s value is concentrated in request types where the "right playbook" depends on project-specific judgment (contested designs, cross-boundary architecture) that a generic model call doesn't reliably infer on its own, and the category is still new enough that its long-run durability against model improvement hasn't been tested. Treat orchestrating modes as a bet that dispatch logic remains useful at the margin, not as a permanent architectural requirement.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — where orchestrating modes sit in the full taxonomy
- [Skill Libraries](skills-libraries.md) — the libraries an orchestrating mode dispatches into
- [Distribution and Governance](skills-management.md) — installation and compatibility mechanics, including native marketplace auto-update behavior
- [Choosing a Skills Approach](skills-choosing.md) — when to reach for an orchestrating mode versus a library or methodology
- [Superpowers](superpowers.md) — a skill-driven methodology, for comparison
