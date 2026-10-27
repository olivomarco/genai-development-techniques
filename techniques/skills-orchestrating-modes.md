# Orchestrating modes

> **Observation date:** October 27, 2026. Playbook counts and port parity are not re-verified every pass — treat specific counts as dated.

An orchestrating mode reads a request, classifies it, and selects a playbook or skill. It depends on a library to do the work. Unlike a composable or lifecycle library, it decides which capability to invoke. See [Skill Libraries](skills-libraries.md) for those categories.

## Lead example: `pstack` / `poteto-mode`

[`pstack`](https://github.com/cursor/plugins/tree/main/pstack) is maintained by Cursor engineer "poteto" (a member of the React core team) and distributed canonically as the `pstack/` directory inside Cursor's official [`cursor/plugins`](https://github.com/cursor/plugins) marketplace repository. Its README positions the project against the "AI writes too much slop code" critique directly: "throughput without quality is not a goal I aspire to. If you want to go fast, go deep first."

The **`poteto-mode`** skill is installed as `/poteto-mode`, or `/pstack:poteto-mode` in a host namespace such as Claude Code's. It reads the constraints in its `SKILL.md`, classifies the request, and selects a playbook and skill for architecture decisions, parallel work, contested designs, or commit and review checks:

- `architect` — cross-boundary design decisions
- `swarm` — parallel-agent coverage matrices
- `arena` — design bakeoffs between competing approaches
- `interrogate` — multi-model adversarial review before shipping

`poteto-mode` selects other `pstack` skills based on context; it does not perform their work itself. A lifecycle library's slash commands invoke capabilities directly.

`poteto-mode` dispatches across a documented set of playbooks and the library's other skills — reported at 23 playbooks in prior research and not re-counted this pass. Treat that figure as a signal of scope, not a current, re-verified count.

### Install paths and port drift

| Host | Install | Caveat |
|---|---|---|
| Cursor (canonical) | `/add-plugin pstack` | The source of truth — other hosts run a generated or adapted copy |
| Claude Code | `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins` | Auto-update is off by default for third-party marketplaces and must be enabled manually in the marketplaces tab |

Claude Code runs a generated adaptation of `pstack` from `harness/pstack/` at the repository root. CI checks that the generator keeps it in sync with the Cursor source.

Steps requiring Cursor-only features such as Bugbot or Automations are skipped on Claude Code with a one-line note. This is documented behavior, not a failure. Compare unexpected behavior with the canonical `cursor/plugins` source; synchronized files do not establish feature parity.

## The unrelated "potato-mode" name collision

`pstack/poteto-mode` is unrelated to **[`aryannaio/potato-mode-agent-skill`](https://github.com/aryannaio/potato-mode-agent-skill)**. The latter is a skill for Claude Code and Codex that measures memory, disk, and CPU headroom, then recommends conservative test-runner and build-tool worker limits. It limits resources for the agent's own commands and does not touch unrelated processes.

The similar names refer to different authors, repositories, and functions: `poteto-mode` routes requests to skills; `potato-mode` limits resource use.

## How this differs from adjacent categories

| Compared to... | The difference |
|---|---|
| **A composable library** ([Skill Libraries](skills-libraries.md)) | You select skills from a composable library. An orchestrating mode selects them based on the request. |
| **A lifecycle library** | A lifecycle library maps skills to fixed stages you invoke by name (`/spec`, `/build`). An orchestrating mode classifies free-form requests and routes dynamically — there's no fixed command per stage. |
| **A native runtime** | A runtime (Claude Code, Codex CLI, Cursor) executes tool calls and manages sessions; it has no opinion about which skill applies to a request. `poteto-mode` runs inside a runtime and supplies the classification logic the runtime itself doesn't provide. |
| **A methodology** (such as [Superpowers](superpowers.md)) | Superpowers prescribes an end-to-end sequence, including brainstorming before planning. `poteto-mode` selects skills per request without owning the full development lifecycle. |

## Connection to the long-horizon model thesis

Our interpretation follows the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology): as models improve at classifying requests, they may need less explicit routing for simple tasks. Routing may remain useful where playbook selection depends on project-specific judgment, such as contested designs or cross-boundary architecture.

The category is too new to establish how long that advantage will last. Adopt an orchestrating mode for a demonstrated routing need, not as a permanent architectural requirement.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — where orchestrating modes sit in the full taxonomy
- [Skill Libraries](skills-libraries.md) — the libraries an orchestrating mode dispatches into
- [Distribution and Governance](skills-management.md) — installation and compatibility mechanics, including native marketplace auto-update behavior
- [Choosing a Skills Approach](skills-choosing.md) — when to reach for an orchestrating mode versus a library or methodology
- [Superpowers](superpowers.md) — a skill-driven methodology, for comparison
