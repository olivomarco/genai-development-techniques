# Skills ecosystem

> **Observation date:** October 27, 2026. Install counts, repository metrics, releases, and compatibility can change quickly.

Use this page when you want reusable agent capabilities without adopting a complete development methodology.

---

## Executive summary

Agent skills have grown past "a library of Markdown files" into a layered market with competing distribution channels:

- **Agent Skills** defines a vendor-neutral `SKILL.md` specification.
- **Composable libraries** such as [`mattpocock/skills`](https://github.com/mattpocock/skills) distribute small, independently selectable practices with no enforced sequence.
- **Lifecycle libraries** such as [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) map their skills onto development-lifecycle stages (define, plan, build, verify, review, ship) through dedicated slash commands, without becoming a full methodology.
- **Orchestrating modes** such as [`pstack/poteto-mode`](https://github.com/cursor/plugins/tree/main/pstack) read an incoming request, select from a set of playbooks, and dispatch a library's other skills as each step needs them — closer to a workflow engine than a single capability.
- **Methodologies** such as [Superpowers](superpowers.md) use skills as mandatory, sequenced workflow controls.
- **Installers and registries** such as [`vercel-labs/skills`](https://github.com/vercel-labs/skills) and [skills.sh](https://skills.sh) handle discovery and vendored installation.
- **Native marketplaces** built into Claude Code, GitHub Copilot, and Codex handle discovery and installation of managed, auto-updating plugin bundles inside one runtime.
- **Curated channels** such as [`github/awesome-copilot`](https://github.com/github/awesome-copilot) package community content for a specific runtime.

These roles overlap, but they are not interchangeable. A specification defines a format; a library supplies content; an orchestrating mode adds dispatch logic on top of a library; an installer or marketplace helps you find and update it; a runtime executes it; and a methodology tells you when and how to use it.

`mattpocock/skills` and `addyosmani/agent-skills` co-lead this ecosystem profile because they demonstrate two different library philosophies at scale — composable versus lifecycle-mapped. Neither defines an end-to-end SDLC, and neither is an eleventh Tier 1 technique.

## Taxonomy

| Category | Example | What it provides | What it does not guarantee |
|---|---|---|---|
| Specification | [Agent Skills](https://agentskills.io) | `SKILL.md` structure, metadata, progressive disclosure, implementor guidance | Identical behavior in every runtime |
| Composable library | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Small, independently selectable engineering and productivity skills | A mandatory lifecycle or governance model |
| Lifecycle library | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Skills mapped to development stages (define → plan → build → verify → review → ship) via slash commands | A single mandatory path through those stages — commands can be run independently |
| Orchestrating mode | [`pstack/poteto-mode`](https://github.com/cursor/plugins/tree/main/pstack) | A dispatcher that reads a request, selects a playbook, and routes to the library's other skills | A standalone capability — it depends entirely on the bundled skills it dispatches |
| Methodology | [Superpowers](superpowers.md) | Mandatory skills, lifecycle sequencing, TDD, review, and enforcement | Team orchestration or enterprise governance |
| Reference implementation | [`anthropics/skills`](https://github.com/anthropics/skills) | Example skills, templates, and Claude Code plugin distribution | Uniform open-source licensing across every included skill |
| Installer and registry | [skills.sh](https://skills.sh) / [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | Discovery, vendored install, update, ranking, and agent-path mapping | Curation, signing, attestation, or semantic parity |
| Native marketplace | Claude Code, GitHub Copilot, and Codex plugin marketplaces | Managed, auto-updating plugin bundles inside one runtime | Cross-runtime portability or a local, editable copy |
| Curated channel | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | Copilot-focused agents, instructions, skills, plugins, and cookbook content | That community content is official GitHub guidance or portable beyond Copilot |
| Runtime | Claude Code, Copilot, Codex, Cline, Goose, and others | Skill discovery and execution | Support for every optional skill feature |

## Lead profile: `mattpocock/skills` (composable library)

[`mattpocock/skills`](https://github.com/mattpocock/skills) is an MIT-licensed library of independently usable engineering and productivity skills, maintained by Matt Pocock. Its README is explicit about the composable-library philosophy: "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control... These skills are designed to be small, easy to adapt, and composable."

As of October 27, 2026:

| Signal | Observation |
|---|---|
| Latest stable release | v1.3.1 |
| Newsletter audience | ~60,000 subscribers (per repository README, a self-reported figure) |
| Install paths | Claude Code and Copilot plugin marketplaces (auto-update), a Codex plugin marketplace (auto-update at startup), Gemini CLI (manual), and the vendor-neutral `npx skills@latest add mattpocock/skills` path for any other agent |
| Prerelease channel | None observed |

Exact current `SKILL.md` counts on `main` were not re-verified for this pass; treat any specific number from an earlier snapshot as stale rather than re-stating it here. Repository star counts and contributor breadth were likewise not re-verified this pass — a known gap, not an omission.

### What it distributes

The library's content spans two buckets described in its own docs:

- **Engineering:** TDD, code review, implementation, research, debugging, domain modeling, architecture, prototyping, specifications, tickets, triage, and merge conflicts. The v1.3.1 release graduated `implement-spec` (whole-spec implementation via a task graph, parallel implementer subagents in worktrees, and a single integration branch), `pr` (a template for what a pull request body should contain), and `retro` (post-session suggestions for the agent's environment, not the code) into this bucket.
- **Productivity:** alignment interviews, handoffs, teaching, questionnaires, and writing for agents.
- **Repository setup:** issue tracking, pre-commit configuration, and skill-specific guardrails, configured once via `/setup-matt-pocock-skills`.

The library encodes opinionated practices, but it does not require a fixed sequence, lifecycle state machine, or governance model. You choose and adapt individual skills — the defining trait of a composable library versus a lifecycle library or a methodology.

### Two distribution philosophies

The project documents two mutually exclusive installation approaches, and this split is now typical of the whole composable/lifecycle library layer, not unique to this project:

| Model | Install path | Benefits | Trade-offs |
|---|---|---|---|
| Managed marketplace plugin | Claude Code, Copilot, or Codex plugin marketplace | Auto-updating bundle, zero manual update step | Upstream changes arrive without local review; runtime-specific distribution |
| Vendored copy | `npx skills@latest add mattpocock/skills -a <agent>` | Editable files, explicit update timing, repository ownership | You maintain local changes and update decisions by hand |

Do not install both for the same agent: the project warns that doing so duplicates every skill.

## Lead profile: `addyosmani/agent-skills` (lifecycle library)

[`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills), maintained by Addy Osmani, packages "production-grade engineering skills for AI coding agents" and organizes them explicitly around the software lifecycle: Define → Plan → Build → Verify → Review → Ship, each stage with its own slash command (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`, plus `/constraints`, `/webperf`, and `/code-simplify`).

As of October 27, 2026:

| Signal | Observation |
|---|---|
| Latest stable release | v0.6.13 |
| Skill count | 25 skills, installable individually or as a full set (`npx skills add addyosmani/agent-skills`) |
| Install paths | The open-source `skills` CLI (70+ agent targets per the repository's own claim), a Claude Code plugin marketplace, a documented Cursor setup (`.cursor/skills/` plus short policies in `.cursor/rules/*.mdc`), and an Antigravity CLI path |
| Known portability gap | A per-skill `npx` install copies only `skills/<name>/`, not the repository-level `references/` directory, so supplementary shared checklists referenced by that skill are unavailable unless you do a whole-repo integration (tracked as [issue #361](https://github.com/addyosmani/agent-skills/issues/361)) |

### What distinguishes it from a composable library

Unlike `mattpocock/skills`, which deliberately avoids owning a process, `addyosmani/agent-skills` maps its command set onto lifecycle stages and documents an automation shortcut: `/build auto` generates the plan and implements every approved task in one pass after a single plan approval. Skills also auto-activate based on detected activity — designing an API triggers `api-and-interface-design`, building UI triggers `frontend-ui-engineering`.

This is still short of a full methodology: there is no mandatory gate forcing you through `/spec` before `/build`, and you can invoke any lifecycle-stage command independently. The project's own v0.6.13 release notes (fixing broken code samples, a `test-driven-development` false-negative on pasted code, and clarifying that `/review` and `/test` run in the main session rather than spawning separate personas) show active maintenance on exactly this lifecycle-mapping layer.

## Lead profile: `pstack` / `poteto-mode` (orchestrating mode)

[`pstack`](https://github.com/cursor/plugins/tree/main/pstack), canonically distributed as the `pstack/` directory inside Cursor's official [`cursor/plugins`](https://github.com/cursor/plugins) marketplace repository, is maintained by Cursor engineer "poteto" (a member of the React core team). Its README frames the project directly against the "AI writes too much slop code" critique: "throughput without quality is not a goal I aspire to. If you want to go fast, go deep first."

The headline capability is **`poteto-mode`** (installed as `/poteto-mode`, or `/pstack:poteto-mode` once namespaced by a host like Claude Code): a dispatcher skill that reads the non-negotiables in its own `SKILL.md`, classifies the incoming request (architecture decision? parallel fan-out opportunity? contested design? pre-commit? pre-review?), and routes to the matching playbook and skill — for example the `architect` skill for cross-boundary design, `swarm` for parallel-agent coverage matrices, `arena` for design bakeoffs, or `interrogate` for multi-model adversarial review before shipping. This read-classify-dispatch loop is what separates an orchestrating mode from a library: `poteto-mode` has no standalone function of its own — its entire value is routing into a library's other skills based on context.

Install paths:

| Host | Install |
|---|---|
| Cursor | `/add-plugin pstack` |
| Claude Code | `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins` (auto-update is off by default for third-party marketplaces and must be enabled manually in the marketplaces tab) |

Claude Code installs a generated, harness-adapted copy of pstack from `harness/pstack/` at the repository root, kept in sync by a generator script the project's CI enforces. A Claude-Code-only limitation: a step needing a Cursor-only feature (Bugbot, Automations) is skipped with a one-line note rather than failing.

`poteto-mode` dispatches across a documented set of playbooks and the library's other skills (reported at 23 playbooks in prior research; not re-counted in this pass). Treat the orchestrating-mode category as a signal that some skill libraries are converging toward framework-like dispatch logic — without adopting a fixed, mandatory sequence the way Superpowers or GSD do.

## Agent Skills specification

[Agent Skills](https://agentskills.io) is a vendor-neutral, Apache-2.0 specification maintained under the [`agentskills`](https://github.com/agentskills/agentskills) organization. Anthropic's own skills repository points readers to this specification rather than presenting the format as Anthropic-owned.

A skill uses a `SKILL.md` file with required `name` and `description` fields. Optional fields include `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. Skills can also include `scripts/`, `references/`, and `assets/`.

The specification uses progressive disclosure:

1. **Discovery:** the runtime reads lightweight metadata.
2. **Activation:** the runtime loads the relevant skill instructions.
3. **Execution:** the runtime uses referenced resources or scripts as needed.

This model reduces context pressure, but specification compliance does not create runtime parity. A prior compatibility pass found basic skills worked across all 18 compared agents, while hooks worked in 4 and `context: fork` in only 1; treat portability as format and content portability first, execution-semantic portability second.

The shared `.agents/skills/` path is also emerging as a vendor-neutral convention. The `skills` CLI uses it for several targets, OpenSpec (now v1.15.0) writes both skills and slash commands there with delivery configurable per project, and it is the install target referenced across several of this site's spec-driven technique pages.

## The structural shift: packages, not file collections

The clearest change since the previous research pass is that reusable skills are consolidating from loose file collections into **versioned, updatable packages**, distributed through two structurally different channels:

- **Cross-agent installer CLIs.** skills.sh's `npx skills add ...` vendors editable files directly into your project for whichever agent you target. You own the copy; updates are explicit (`npx skills@latest update`).
- **Native plugin marketplaces.** The Claude Code, GitHub Copilot, and Codex plugin marketplaces install a managed bundle that auto-updates inside that one runtime. You don't own the copy; updates arrive without a local review step unless you opt out of auto-update.

Both `mattpocock/skills` and `addyosmani/agent-skills` ship through both paths, and both projects warn against installing the same library both ways for one agent — it duplicates every skill. Pick one channel per agent per library.

This split is creating a thin, still-forming **management layer** on top of the content layer:

- **Packaging.** Skills now ship as versioned packages (semver releases, changelogs, graduated/staging buckets) rather than loose files — `mattpocock/skills`' "Engineering" bucket graduation process is a direct example.
- **Update channel.** A managed marketplace plugin and a vendored CLI copy are structurally different update channels with different trust models, not two flavors of the same thing.
- **Portability.** A skill can be format-portable (the `SKILL.md` parses anywhere) without being behavior-portable (hooks, `context: fork`, and other optional runtime features vary sharply).
- **Provenance.** None of the surfaces examined for this page provide cryptographic signing, attestation, or lockfile-style pinning for any install path.
- **Evaluation.** Evidence of skill quality, where it exists at all, is vendor-reported (release notes describing fixed test cases) rather than independently audited.
- **Dependency completeness.** Installers can silently omit shared dependencies — `addyosmani/agent-skills`' own issue #361 documents a per-skill install that drops a shared `references/` directory another skill needs.
- **Compatibility.** The same library can be "current" in one agent's marketplace and "stale" in a vendored copy you haven't updated, with no unified cross-channel version signal.
- **Policy/control.** Auto-update by default (native marketplaces) versus manual update by default (vendored copies) is itself a policy choice teams need to make deliberately, not a detail to overlook.

None of this makes the skills layer an eleventh Tier 1 technique or a sixth methodology category. It is market infrastructure that the methodologies in this comparison increasingly plug into — OpenSpec writes to it, HVE has moved almost all of its reusable task templates onto it, and BMAD's V7 preview alpha is restructuring its own installer around it.

## Discovery and distribution

### skills.sh and the `skills` CLI

[skills.sh](https://skills.sh), operated by Vercel, combines several roles:

- **Installer:** `add`, `update`, `remove`, `use`, and `init`.
- **Discovery:** `find` and a public directory.
- **Registry:** automatic listing when telemetry records an install.
- **Ranking:** install-count leaderboards from anonymous CLI telemetry.
- **Portability layer:** path mapping across a large and growing number of agent targets (`addyosmani/agent-skills` cites 70+ as of October 2026).

It accepts GitHub, GitLab, arbitrary Git, local, and private-repository sources. Telemetry is enabled by default and can be disabled with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`.

The default directory is not a curated trust store. Entries can appear automatically, audit coverage is incomplete, and the examined surfaces provide no signing, provenance attestation, or lockfile-style pinning. Vercel controls both the dominant installer and its leaderboard, which is relevant when evaluating governance and ranking incentives.

### Native plugin marketplaces

Claude Code, GitHub Copilot, and Codex each now operate their own plugin marketplace for installing managed skill bundles (`claude plugin install ...`, `copilot plugin install ...`, `codex plugin add ...`). These are the fastest-updating channel — the bundle refreshes without you running an update command — but they are also the least reviewable: you are trusting the publisher's next push, not a pinned revision. `mattpocock/skills` ships through all three; `addyosmani/agent-skills` ships through the Claude Code marketplace; `pstack` ships through the Claude Code marketplace as a third-party addition on top of its native Cursor home.

### Anthropic's reference skills

[`anthropics/skills`](https://github.com/anthropics/skills) provides examples, a template, a specification directory, and Claude Code plugin installation. Treat it as a reference implementation, not the governing standard.

Licensing varies within the repository. The README says many skills use Apache-2.0, while the `docx`, `pdf`, `pptx`, and `xlsx` skills are source-available rather than open source. The repository also describes its skills as demonstration and educational material. Review each skill's terms before reuse.

### GitHub's Copilot channel

[`github/awesome-copilot`](https://github.com/github/awesome-copilot) is a GitHub-owned distribution channel with a pre-registered Copilot marketplace. It contains agents, instructions, skills, plugins, and cookbook material.

The channel is official; its content is community-created and sourced from third parties. GitHub explicitly warns readers about that distinction. Skills may be readable by other `SKILL.md` consumers, but the broader agents, instructions, hooks, and plugin model is Copilot-shaped. Classify this as strong Copilot integration and limited cross-runtime portability.

### OpenSkills

[`numman-ali/openskills`](https://github.com/numman-ali/openskills) helped establish cross-agent installation, but it had not been pushed since January 18, 2026, when last observed, and was not re-checked for this pass. Its license metadata also conflicted with its README badge at that time. Treat it as a historical or watchlist project, not a current default, pending re-verification.

## Methodologies compared against the expanded taxonomy

[Superpowers](superpowers.md), now at **v7.0.1** (October 2026), remains the clearest Tier-1 example of a skills-based methodology: mandatory skill search before acting, a fixed brainstorm → plan → subagent-driven TDD → review → finish sequence, and persuasion-tested compliance. Set against the taxonomy above:

- Superpowers is a **methodology**, not a library — it enforces a sequence and rejects the "pick what you want" model that both `mattpocock/skills` and `addyosmani/agent-skills` are built around.
- It is closer in spirit to an **orchestrating mode** than either library profiled here, since its bootstrap actively dispatches the agent into specific skills at specific phases — but unlike `poteto-mode`, that dispatch is the entire product, not a mode layered on an otherwise-composable library.
- Superpowers' v7.0.0/v7.0.1 brainstorming rebuild (context-gathering before questions, a design doc with human approval, a fresh "builder check" subagent reading the spec as its future implementer) is itself best read as a skill-authoring example other library maintainers can study, independent of whether you adopt Superpowers' enforcement model.

The practical choice is still: pick a methodology when you want the framework to constrain execution and sequence; pick a composable or lifecycle library when you want to select and adapt individual practices yourself; add an orchestrating mode when you want dispatch logic on top of a library without committing to a full methodology.

## Security and provenance

Skills can contain executable scripts and instructions that influence high-privilege agents. Apply the same scrutiny you would apply to a dependency or CI action.

The ecosystem's controls remain incomplete:

- skills.sh aggregates security findings from third-party scanners, but coverage is partial and some prominent skills show medium-risk findings; this was not re-verified in detail for this pass.
- The `skills` CLI documents conservative credential handling, but telemetry is opt-out by default.
- Agent Skills marks `allowed-tools` as experimental.
- None of the examined surfaces (installers, marketplaces, or the libraries themselves) provide signing, attestation, or lockfile-style pinning.
- Repository ownership, skill licensing, and transitive script behavior can differ within one collection — `anthropics/skills` is the clearest example, mixing Apache-2.0 and source-available skills in one repo.
- Per-skill installs can silently omit shared dependencies a skill assumes are present (`addyosmani/agent-skills` issue #361).

Before installing a skill:

1. Read `SKILL.md` and every referenced script.
2. Verify the repository owner, license, release, and maintenance history.
3. Prefer a pinned vendored copy when reproducibility matters; treat native-marketplace auto-update as a convenience/trust trade-off, not a neutral default.
4. Limit tool permissions and secrets available to the agent.
5. Test in an isolated repository or worktree.
6. Record the source revision and review updates as code changes.

## Choosing an approach

| Need | Choose |
|---|---|
| A few reusable practices you select and adapt yourself | A composable library such as `mattpocock/skills` |
| Skills organized around define/plan/build/verify/review/ship | A lifecycle library such as `addyosmani/agent-skills` |
| Automatic dispatch across a library's skills based on request type | An orchestrating mode such as `pstack/poteto-mode` |
| Automatic updates and a managed bundle, accepting less local review | A native plugin marketplace subscription |
| Editable, reviewable, reproducible content, with manual update timing | A vendored copy via skills.sh or the `skills` CLI, preferably pinned |
| Discovery across many agents | skills.sh and the `skills` CLI, with independent trust review |
| Copilot-specific community content | `github/awesome-copilot` |
| A mandatory individual development lifecycle | Superpowers |
| Team roles, routing, and shared memory | Squad or BMAD |
| Enterprise constraints and audit artifacts | HVE |

Skills are additive. You can combine a library with GSD, Spec Kit, OpenSpec, Squad, BMAD, Ralph, or HVE. Check for duplicate instructions, conflicting lifecycle assumptions, and runtime-specific features before combining them — and before combining two libraries that may define the same skill name twice.

## Related pages

- [Choosing your approach](choosing-your-approach.md)
- [Superpowers](superpowers.md)
- [Context engineering](context-engineering.md)
- [OpenSpec](openspec.md)
