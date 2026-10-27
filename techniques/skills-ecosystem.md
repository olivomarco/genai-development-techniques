# State of the skills market

> **Observation date:** October 27, 2026. Install counts, repository metrics, releases, and compatibility are snapshots, not live status.

This page maps the reusable agent skills market. It introduces [Skills and Agent Frameworks](skills-libraries.md), with links to library comparisons, request-routing modes, distribution, and selection guidance.

## What is changing

Reusable skills increasingly ship as **versioned, updatable packages** through two channels. Cross-agent installer CLIs, such as skills.sh's `npx skills`, copy editable files into the target agent's skill directory. Native plugin marketplaces for Claude Code, GitHub Copilot, and Codex install managed bundles inside one runtime, with marketplace-specific update policies.

Some libraries also bundle an **orchestrating mode**: a dispatcher that reads a request and selects a playbook or skill. This adds workflow decisions to a library of capabilities.

## Taxonomy

| Category | Example | What it provides | What it does not guarantee |
|---|---|---|---|
| Specification | [Agent Skills](https://agentskills.io) | `SKILL.md` structure, metadata, progressive disclosure | Identical behavior in every runtime |
| Composable library | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Small, independently selectable skills | A mandatory lifecycle or governance model |
| Lifecycle library | [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Skills mapped to development stages via slash commands | A single mandatory path through those stages |
| Orchestrating mode | [`pstack/poteto-mode`](https://github.com/cursor/plugins/tree/main/pstack) | A dispatcher that routes requests into a library's other skills | A standalone capability — it depends entirely on the library it dispatches into |
| Methodology | [Superpowers](superpowers.md) | Mandatory skills, lifecycle sequencing, TDD, review, enforcement | Team orchestration or enterprise governance |
| Reference implementation | [`anthropics/skills`](https://github.com/anthropics/skills) | Example skills, templates, Claude Code plugin distribution | Uniform open-source licensing across every included skill |
| Installer and registry | [skills.sh](https://skills.sh) / [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | Discovery, vendored install, update, ranking | Curation, signing, attestation, or semantic parity |
| Native marketplace | Claude Code, GitHub Copilot, Codex | Managed, auto-updating plugin bundles inside one runtime | Cross-runtime portability or a local, editable copy |
| Curated channel | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | Copilot-focused community content | That the content is official guidance or portable beyond Copilot |
| Runtime | Claude Code, Copilot, Codex, Cline, Goose, and others | Skill discovery and execution | Support for every optional skill feature |

These roles overlap but are not interchangeable. A specification defines a format; a library supplies content; an orchestrating mode selects skills; an installer or marketplace distributes them; a runtime executes them; a methodology prescribes their use.

## Why it matters

A runtime may parse a `SKILL.md` file without supporting every feature it uses.

A prior cross-runtime pass found basic skill content worked across all 18 agents checked. Hooks worked in only 4 of them. `context: fork` worked in just 1.

No installer, marketplace, or library we examined signs, attests, or lockfile-pins a skill on any install path. Most evaluation evidence comes from vendors, not independent audits. Check provenance and runtime behavior before standardizing on a library.

## What's changing, in short

- **Packaging.** Skills now ship as versioned packages (semver releases, changelogs, graduated/staging buckets) rather than loose files.
- **Update channel.** A managed marketplace plugin and a vendored CLI copy are structurally different update channels with different trust models.
- **Portability.** Format portability (parses anywhere) and behavioral portability (hooks and runtime-specific features actually execute) are separate claims.
- **Provenance.** No signing, attestation, or lockfile-style pinning was found on any surface examined.
- **Evaluation.** Quality evidence is vendor-reported, not independently audited.
- **Dependency completeness.** Per-skill installers can silently omit shared dependencies another skill needs.
- **Compatibility.** The same library can be current in one runtime's marketplace and stale in a vendored copy, with no unified cross-channel version signal.
- **Policy and control.** Auto-update-by-default versus manual-update-by-default is a policy choice teams need to make deliberately.

`mattpocock/skills` and `addyosmani/agent-skills` illustrate two library approaches: composable and lifecycle-mapped. Both ship through native marketplaces and installer CLIs. Neither defines an end-to-end SDLC.

## Relationship to the model, runtime, and methodology layers

Skills support the runtime and methodology layers of the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology). Runtimes load and execute them; some methodologies make them mandatory. OpenSpec generates skills, HVE has moved most reusable task templates to skills, and BMAD's V7 preview installs its method as skills.

Star counts and install figures indicate attention, not production adoption. See [Research Methodology](../methodology.md) for the evidence labels.

## Where to go next

- **[Skill Libraries](skills-libraries.md)** — a full comparison of `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections across composition, evaluation, portability, licensing, and distribution.
- **[Orchestrating Modes](skills-orchestrating-modes.md)** — a focused look at `pstack/poteto-mode`, canonical-source and port-drift caveats, and the unrelated `potato-mode` resource-throttling skill it's sometimes confused with by name.
- **[Distribution and Governance](skills-management.md)** — the Agent Skills specification, progressive disclosure, native marketplaces vs. CLI-vendored installs, versioning, provenance, permissions, and enterprise rollout guidance.
- **[Choosing a Skills Approach](skills-choosing.md)** — a decision guide across composable libraries, lifecycle libraries, orchestrating modes, skill-driven methodologies, native runtimes, and custom internal catalogs.
- **[Superpowers](superpowers.md)** — a skill-driven methodology with mandatory TDD and review.

## Related pages

- [Choosing Your Approach](choosing-your-approach.md)
- [Context Engineering](context-engineering.md)
- [OpenSpec](openspec.md)
