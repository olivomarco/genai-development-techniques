# Skills ecosystem

> **Observation date:** August 8, 2026. Install counts, repository metrics, releases, and compatibility can change quickly.

Use this page when you want reusable agent capabilities without adopting a complete development methodology.

---

## Executive summary

Agent skills now form a distinct layer in AI-assisted development:

- **Agent Skills** defines a vendor-neutral `SKILL.md` specification.
- **Skill libraries** such as [`mattpocock/skills`](https://github.com/mattpocock/skills) distribute reusable engineering practices.
- **Installers and registries** such as [`vercel-labs/skills`](https://github.com/vercel-labs/skills) and [skills.sh](https://skills.sh) handle discovery and installation.
- **Curated channels** such as [`github/awesome-copilot`](https://github.com/github/awesome-copilot) package community content for a specific runtime.
- **Methodologies** such as [Superpowers](superpowers.md) use skills as mandatory workflow controls.

These roles overlap, but they are not interchangeable. A specification defines a format; a library supplies content; a registry helps you find it; a runtime executes it; and a methodology tells you when and how to use it.

`mattpocock/skills` leads this ecosystem profile because it demonstrates the library model at scale. It does not define an end-to-end SDLC and is not an eleventh Tier 1 technique.

## Layer map

| Layer | Example | What it provides | What it does not guarantee |
|---|---|---|---|
| Specification | [Agent Skills](https://agentskills.io) | `SKILL.md` structure, metadata, progressive disclosure, implementor guidance | Identical behavior in every runtime |
| Library | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Reusable engineering and productivity skills | A mandatory lifecycle or governance model |
| Reference implementation | [`anthropics/skills`](https://github.com/anthropics/skills) | Example skills, templates, and Claude Code plugin distribution | Uniform open-source licensing across every included skill |
| Installer and registry | [skills.sh](https://skills.sh) / [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | Discovery, install, update, ranking, and agent-path mapping | Curation, signing, attestation, or semantic parity |
| Curated channel | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | Copilot-focused agents, instructions, skills, plugins, and cookbook content | That community content is official GitHub guidance or portable beyond Copilot |
| Methodology | [Superpowers](superpowers.md) | Mandatory skills, lifecycle sequencing, TDD, review, and enforcement | Team orchestration or enterprise governance |
| Runtime | Claude Code, Copilot, Codex, Cline, Goose, and others | Skill discovery and execution | Support for every optional skill feature |

## Lead profile: `mattpocock/skills`

[`mattpocock/skills`](https://github.com/mattpocock/skills) is an MIT-licensed library of independently usable engineering and productivity skills. Its repository contains 35 `SKILL.md` files on `main`; skills.sh lists 51 entries for the source. The discrepancy is not verified, so neither number should be treated as the single authoritative catalog size.

As of August 8, 2026:

| Signal | Observation |
|---|---|
| Latest stable release | v1.2.3, published August 6, 2026 |
| Repository activity | Last push August 7, 2026 |
| Usage telemetry | skills.sh reports 14.4 million total installs across its 51 listed entries |
| Maintenance breadth | 3 listed non-anonymous contributors |
| Prerelease channel | None observed |

The install signal indicates substantial use, but it does not prove production outcomes. The small listed contributor base creates a clear bus-factor risk despite the large star and install counts.

### What it distributes

The stable repository content includes skills for:

- **Engineering:** TDD, code review, implementation, research, debugging, domain modeling, architecture, prototyping, specifications, tickets, triage, and merge conflicts.
- **Productivity:** alignment interviews, handoffs, teaching, questionnaires, and writing for agents.
- **Repository setup:** issue tracking, pre-commit configuration, and skill-specific guardrails.
- **Staging:** six skills under `in-progress`, which should not be treated as stable.

The library encodes opinionated practices, but it does not require a fixed sequence, lifecycle state machine, or governance model. You choose and adapt individual skills.

### Two distribution philosophies

The project documents two mutually exclusive installation approaches:

| Model | Install path | Benefits | Trade-offs |
|---|---|---|---|
| Managed subscription | Claude Code plugin marketplace | Read-only bundle and automatic updates | Upstream changes arrive without local editing; Claude-specific distribution |
| Vendored copy | `npx skills@latest add mattpocock/skills` | Editable files, explicit updates, repository ownership | You maintain local changes and update decisions |

Do not install both: the project warns that doing so duplicates every skill. After installation, `/setup-matt-pocock-skills` configures issue tracking, labels, and documentation paths for repository-dependent skills.

## Agent Skills specification

[Agent Skills](https://agentskills.io) is a vendor-neutral, Apache-2.0 specification maintained under the [`agentskills`](https://github.com/agentskills/agentskills) organization. Anthropic's own skills repository points readers to this specification rather than presenting the format as Anthropic-owned.

A skill uses a `SKILL.md` file with required `name` and `description` fields. Optional fields include `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. Skills can also include `scripts/`, `references/`, and `assets/`.

The specification uses progressive disclosure:

1. **Discovery:** the runtime reads lightweight metadata.
2. **Activation:** the runtime loads the relevant skill instructions.
3. **Execution:** the runtime uses referenced resources or scripts as needed.

This model reduces context pressure, but specification compliance does not create runtime parity. In the `skills` CLI compatibility matrix observed on August 8, basic skills worked across all 18 compared agents, while hooks worked in 4 and `context: fork` in only 1. Treat portability as format and content portability first, execution-semantic portability second.

The shared `.agents/skills/` path is also emerging as a vendor-neutral convention. The `skills` CLI uses it for several targets, and OpenSpec v1.8.0 independently added an `agents` target that writes there. This is meaningful convergence, not proof of universal support.

## Discovery and distribution

### skills.sh and the `skills` CLI

[skills.sh](https://skills.sh), operated by Vercel, combines several roles:

- **Installer:** `add`, `update`, `remove`, `use`, and `init`.
- **Discovery:** `find` and a public directory.
- **Registry:** automatic listing when telemetry records an install.
- **Ranking:** install-count leaderboards from anonymous CLI telemetry.
- **Portability layer:** path mapping for about 70 agent targets.

It accepts GitHub, GitLab, arbitrary Git, local, and private-repository sources. Telemetry is enabled by default and can be disabled with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`.

The default directory is not a curated trust store. Entries can appear automatically, audit coverage is incomplete, and the examined surfaces provide no signing, provenance attestation, or lockfile-style pinning. Vercel controls both the dominant installer and its leaderboard, which is relevant when evaluating governance and ranking incentives.

### Anthropic's reference skills

[`anthropics/skills`](https://github.com/anthropics/skills) provides examples, a template, a specification directory, and Claude Code plugin installation. Treat it as a reference implementation, not the governing standard.

Licensing varies within the repository. The README says many skills use Apache-2.0, while the `docx`, `pdf`, `pptx`, and `xlsx` skills are source-available rather than open source. The repository also describes its skills as demonstration and educational material. Review each skill's terms before reuse.

### GitHub's Copilot channel

[`github/awesome-copilot`](https://github.com/github/awesome-copilot) is a GitHub-owned distribution channel with a pre-registered Copilot marketplace. It contains agents, instructions, skills, plugins, and cookbook material.

The channel is official; its content is community-created and sourced from third parties. GitHub explicitly warns readers about that distinction. Skills may be readable by other `SKILL.md` consumers, but the broader agents, instructions, hooks, and plugin model is Copilot-shaped. Classify this as strong Copilot integration and limited cross-runtime portability.

### OpenSkills

[`numman-ali/openskills`](https://github.com/numman-ali/openskills) helped establish cross-agent installation, but it had not been pushed since January 18, 2026, when observed. Its license metadata also conflicted with its README badge. Treat it as a historical or watchlist project, not a current default.

## Security and provenance

Skills can contain executable scripts and instructions that influence high-privilege agents. Apply the same scrutiny you would apply to a dependency or CI action.

The ecosystem's controls remain incomplete:

- skills.sh aggregates findings from Gen Agent Trust Hub, Socket, and Snyk, but many entries remain pending and some prominent skills show medium-risk findings.
- The `skills` CLI documents conservative credential handling, but telemetry is opt-out.
- Agent Skills marks `allowed-tools` as experimental.
- None of the examined surfaces provided signing, attestation, or lockfile-style pinning.
- Repository ownership, skill licensing, and transitive script behavior can differ within one collection.

Before installing a skill:

1. Read `SKILL.md` and every referenced script.
2. Verify the repository owner, license, release, and maintenance history.
3. Prefer a pinned vendored copy when reproducibility matters.
4. Limit tool permissions and secrets available to the agent.
5. Test in an isolated repository or worktree.
6. Record the source revision and review updates as code changes.

## Choosing an approach

| Need | Choose |
|---|---|
| A few reusable practices that you can adapt | A library such as `mattpocock/skills` |
| Automatic updates and a managed bundle | A plugin subscription |
| Editable, reviewable, reproducible content | A vendored copy, preferably pinned |
| Discovery across many agents | skills.sh and the `skills` CLI, with independent trust review |
| Copilot-specific community content | `github/awesome-copilot` |
| A mandatory individual development lifecycle | Superpowers |
| Team roles, routing, and shared memory | Squad or BMAD |
| Enterprise constraints and audit artifacts | HVE |

Skills are additive. You can combine a library with GSD, Spec Kit, OpenSpec, Squad, BMAD, Ralph, or HVE. Check for duplicate instructions, conflicting lifecycle assumptions, and runtime-specific features before combining them.

## Related pages

- [Choosing your approach](choosing-your-approach.md)
- [Superpowers](superpowers.md)
- [Context engineering](context-engineering.md)
- [OpenSpec](openspec.md)
