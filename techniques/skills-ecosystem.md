# State of the skills market

> **Observation date:** October 27, 2026. Install counts, repository metrics, releases, and compatibility can change quickly — read this page as a dated snapshot, not a live status board.

Use this page when you want the market-level picture of reusable agent skills before going deeper into any one part of it. It's the entry point for [Skills and Agent Frameworks](skills-libraries.md) — the group of pages that cover libraries, orchestrating modes, distribution mechanics, and selection guidance in detail.

## What is changing

Agent skills are no longer just loose Markdown files. They've grown into a layered market with competing distribution channels. The clearest change since the previous research pass: reusable skills are consolidating from loose file collections into **versioned, updatable packages**, distributed through two structurally different channels — cross-agent installer CLIs (skills.sh's `npx skills` vendors editable files into any agent you target) and native plugin marketplaces (Claude Code, GitHub Copilot, and Codex each install a managed bundle that auto-updates inside that one runtime).

Some libraries now bundle an **orchestrating mode** alongside their skills — a dispatcher that reads an incoming request and routes it to the right playbook, blurring the line between a skill library and a workflow framework. This is a new structural category, not a repackaging of an old one.

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

These roles overlap but aren't interchangeable. A specification defines a format; a library supplies content; an orchestrating mode adds dispatch logic on top of a library; an installer or marketplace helps you find and update it; a runtime executes it; a methodology tells you when and how to use it. Full detail on each category lives in the dedicated pages linked below — this page stays at the market level.

## Why it matters

Parsing a `SKILL.md` file doesn't prove its features work. Those are two different claims, and the gap between them is where most of the real risk sits.

A prior cross-runtime pass found basic skill content worked across all 18 agents checked. Hooks worked in only 4 of them. `context: fork` worked in just 1.

No installer, marketplace, or library we examined signs, attests, or lockfile-pins a skill on any install path. Most evaluation evidence comes from vendors, not independent audits. This is the thin, still-forming layer for tracking and trusting skills, and it's the layer worth scrutinizing before you standardize on anything.

## What's changing, in short

- **Packaging.** Skills now ship as versioned packages (semver releases, changelogs, graduated/staging buckets) rather than loose files.
- **Update channel.** A managed marketplace plugin and a vendored CLI copy are structurally different update channels with different trust models.
- **Portability.** Format portability (parses anywhere) and behavioral portability (hooks and runtime-specific features actually execute) are separate claims.
- **Provenance.** No signing, attestation, or lockfile-style pinning was found on any surface examined.
- **Evaluation.** Quality evidence is vendor-reported, not independently audited.
- **Dependency completeness.** Per-skill installers can silently omit shared dependencies another skill needs.
- **Compatibility.** The same library can be current in one runtime's marketplace and stale in a vendored copy, with no unified cross-channel version signal.
- **Policy and control.** Auto-update-by-default versus manual-update-by-default is a policy choice teams need to make deliberately.

`mattpocock/skills` and `addyosmani/agent-skills` co-lead this market profile because they demonstrate two different library philosophies at scale — composable versus lifecycle-mapped — and both ship through both distribution channels. Neither defines an end-to-end SDLC, and neither is an eleventh Tier 1 technique.

## Relationship to the model, runtime, and methodology layers

None of this makes the skills layer an eleventh Tier 1 technique or a sixth methodology category (see the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology)). It's market infrastructure that the methodologies in this comparison increasingly plug into: OpenSpec writes to it, HVE has moved almost all of its reusable task templates onto it, and BMAD's V7 preview is restructuring its own installer around it. Skills themselves occupy layer two and three of that model — they ride on top of a runtime, and some methodologies additionally make specific skills mandatory. Star counts and install figures throughout this market remain dated awareness signals; they do not establish production adoption. See [Research Methodology](../methodology.md) for how this site labels that kind of evidence.

## Where to go next

- **[Skill Libraries](skills-libraries.md)** — a full comparison of `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections across composition, evaluation, portability, licensing, and distribution.
- **[Orchestrating Modes](skills-orchestrating-modes.md)** — a focused look at `pstack/poteto-mode`, canonical-source and port-drift caveats, and the unrelated `potato-mode` resource-throttling skill it's sometimes confused with by name.
- **[Distribution and Governance](skills-management.md)** — the Agent Skills specification, progressive disclosure, native marketplaces vs. CLI-vendored installs, versioning, provenance, permissions, and enterprise rollout guidance.
- **[Choosing a Skills Approach](skills-choosing.md)** — a decision guide across composable libraries, lifecycle libraries, orchestrating modes, skill-driven methodologies, native runtimes, and custom internal catalogs.
- **[Superpowers](superpowers.md)** — the clearest Tier 1 example of a skill-driven methodology, profiled in full on its own page.

## Related pages

- [Choosing Your Approach](choosing-your-approach.md)
- [Context Engineering](context-engineering.md)
- [OpenSpec](openspec.md)
