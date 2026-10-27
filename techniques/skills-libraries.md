# Skill libraries

> **Observation date:** October 27, 2026. Release numbers, skill counts, and install paths are dated snapshots, including those labeled Verified.

A skill library is a collection of `SKILL.md` packages you select, install, and adapt. It does not enforce a development sequence. [Superpowers](superpowers.md) adds a mandatory methodology; [Orchestrating Modes](skills-orchestrating-modes.md) select skills based on the request. See [Distribution and Governance](skills-management.md) for installation, versioning, and controls.

This page compares four libraries covered in the research pass: `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, and `vercel-labs/agent-skills`. Two other collections appear on the watchlist.

## At a glance

| Library | Maintainer | Philosophy | Latest release | License |
|---|---|---|---|---|
| [`mattpocock/skills`](https://github.com/mattpocock/skills) | Matt Pocock | Composable — small, independently selectable practices | v1.3.1 | MIT |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Addy Osmani | Lifecycle-mapped — define → plan → build → verify → review → ship | v0.6.13 | Reported as open source in repository docs; per-license text not re-verified this pass |
| [`anthropics/skills`](https://github.com/anthropics/skills) | Anthropic | Reference implementation and demonstration material | Unversioned reference repo (no single semver release tracked) | Mixed — Apache-2.0 for most skills; `docx`, `pdf`, `pptx`, `xlsx` are source-available, not open source |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | Vercel | Domain-specific — Vercel/React/Next.js/React Native audits and writing-handbook checks | Unversioned at time of observation; distributed via `npx skills add vercel-labs/agent-skills` | MIT (per repository badge) |

[`vercel-labs/skills`](https://github.com/vercel-labs/skills) is the CLI behind [skills.sh](https://skills.sh), not a skill collection. Vercel maintains both repositories, but one installs skills and the other supplies them.

## Composition

- **`mattpocock/skills`** ships in three buckets: engineering (TDD, code review, implementation, research, debugging, domain modeling, architecture, prototyping, specifications, tickets, triage, merge conflicts), productivity (alignment interviews, handoffs, teaching, questionnaires, writing for agents), and repository setup (issue tracking, pre-commit configuration, skill-specific guardrails via `/setup-matt-pocock-skills`). Skills graduate from staging into the engineering bucket as they mature — `implement-spec`, `pr`, and `retro` graduated in v1.3.1.
- **`addyosmani/agent-skills`** ships 25 skills, installable individually or as a set, organized around nine slash commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`, plus `/constraints`, `/webperf`, `/code-simplify`). Several skills auto-activate on detected activity — designing an API triggers `api-and-interface-design`; building UI triggers `frontend-ui-engineering`.
- **`anthropics/skills`** provides example skills, a starter template, a specification directory, and document-handling skills (`docx`, `pdf`, `pptx`, `xlsx`) distributed as a Claude Code plugin. It is explicitly demonstration and educational material, not a production content catalog.
- **`vercel-labs/agent-skills`** is narrowly scoped to Vercel's own domain: `vercel-optimize` (cost/performance/reliability audits using Vercel's observability metrics), `react-best-practices` (40+ rules across 8 categories), `web-design-guidelines` (100+ accessibility/UX rules), `writing-guidelines` (80+ rules from Vercel's writing handbook), and `react-native-guidelines` (16 rules across 7 sections).

## Lifecycle coverage

Only `addyosmani/agent-skills` claims explicit lifecycle-stage mapping. `mattpocock/skills` and `vercel-labs/agent-skills` are both composable: you select a skill for a task, with no stage model behind it. `anthropics/skills` is neither — it's a reference set, not a workflow.

Lifecycle mapping does not enforce a sequence. `addyosmani/agent-skills` documents `/build auto` as an automation shortcut, but you can invoke `/build` without running `/spec` first. Superpowers prescribes a sequence instead.

## Evaluation

Evidence of quality is vendor-reported across all four libraries — none examined in this pass publish independent third-party audits:

- `mattpocock/skills` release notes describe fixed issues and graduated skills but no systematic test-suite results.
- `addyosmani/agent-skills` v0.6.13 release notes cite specific fixes (broken code samples, a `test-driven-development` false-negative on pasted code) — concrete, but still self-reported.
- `anthropics/skills` is framed as educational; Anthropic does not claim production-grade evaluation of the examples.
- `vercel-labs/agent-skills` rules are sourced from "Vercel Engineering" practice documents; no external validation was found for this pass.

Treat every "N rules" or "N/N passed" figure in this section as **Reported**, not **Verified** — see [Research Methodology](../methodology.md#evidence-labels).

## Portability

All four target the Agent Skills `SKILL.md` format, which parses across any compliant runtime. Behavioral portability is narrower:

- `mattpocock/skills` and `addyosmani/agent-skills` both ship through multiple native plugin marketplaces (Claude Code, Copilot, and for `mattpocock/skills`, Codex) in addition to the vendor-neutral `npx skills@latest add ...` path.
- `vercel-labs/agent-skills` is installed exclusively through the `skills` CLI (`npx skills add vercel-labs/agent-skills`); no native-marketplace listing was found this pass.
- `anthropics/skills` installs as a Claude Code plugin; cross-runtime install paths are not its focus.

A prior cross-runtime compatibility pass (cited in [State of the Skills Market](skills-ecosystem.md)) found basic skill content portable across all 18 compared agents, while hooks and `context: fork` support dropped sharply — a gap that applies to any library in this table, not one specifically.

## Maintenance

- `mattpocock/skills`: active, versioned releases with a visible staging-to-graduation process for new skills.
- `addyosmani/agent-skills`: active, with release notes describing specific bug fixes as well as feature additions.
- `anthropics/skills`: maintained as reference material; update cadence is tied to the specification and Claude Code plugin ecosystem rather than a standalone release train.
- `vercel-labs/agent-skills`: maintained alongside Vercel's own engineering practice documents; no public changelog was found this pass.

## Licensing and provenance

Licensing is not uniform even within a single repository. `anthropics/skills` is the clearest example: most skills are Apache-2.0, but `docx`, `pdf`, `pptx`, and `xlsx` are source-available rather than open source. `mattpocock/skills` and `vercel-labs/agent-skills` are MIT. `addyosmani/agent-skills`'s precise license text per skill was not re-verified this pass.

None of the four libraries provide cryptographic signing, attestation, or lockfile-style pinning for any install path — a gap shared across the entire skills layer (see [Distribution and Governance](skills-management.md#provenance-signing-and-compatibility)).

## Dependency completeness

`addyosmani/agent-skills` documents an incomplete-install problem in [issue #361](https://github.com/addyosmani/agent-skills/issues/361). A per-skill `npx skills add` install copies `skills/<name>/` but omits the repository-level `references/` directory. Shared checklists can go missing without a whole-repo integration. Check dependencies when installing individual skills from any library with shared references.

## Distribution

| Library | Native marketplace | CLI-vendored | Notes |
|---|---|---|---|
| `mattpocock/skills` | Claude Code, Copilot, Codex | `npx skills@latest add mattpocock/skills` | Warns against installing both paths for one agent — duplicates every skill |
| `addyosmani/agent-skills` | Claude Code | `npx skills add addyosmani/agent-skills` | Also documents a Cursor setup (`.cursor/skills/` plus `.cursor/rules/*.mdc`) and an Antigravity CLI path |
| `anthropics/skills` | Claude Code | Manual clone/reference | Positioned as reference material, not a general install target |
| `vercel-labs/agent-skills` | None found this pass | `npx skills add vercel-labs/agent-skills` | CLI-only distribution as observed |

## Strengths and limitations

| Library | Strengths | Limitations |
|---|---|---|
| `mattpocock/skills` | Broadest general-engineering scope; explicit composable philosophy; widest marketplace reach (three native channels) | No lifecycle structure if you want one; skill counts on `main` were not re-verified this pass |
| `addyosmani/agent-skills` | Clearest lifecycle mapping of the four; active bug-fix-driven maintenance; auto-activation on detected task type | Documented dependency-completeness gap (issue #361); narrower marketplace reach than `mattpocock/skills` |
| `anthropics/skills` | Canonical reference for the specification; useful templates and starter examples | Mixed licensing within one repo; explicitly not production-audited; not meant as a general-purpose catalog |
| `vercel-labs/agent-skills` | Deep, narrow domain expertise (Vercel/React/Next.js/React Native/writing); high rule-count specificity | Single-vendor domain scope; no native-marketplace listing; no public changelog found this pass |

## Watchlist collections

- **[`numman-ali/openskills`](https://github.com/numman-ali/openskills)** helped establish cross-agent skill installation early, but had not been pushed since January 18, 2026 when last observed, and its license metadata conflicted with its README badge at that time. Not re-checked this pass — treat as historical, not current, pending re-verification.
- **[`github/awesome-copilot`](https://github.com/github/awesome-copilot)** is a GitHub-owned curated channel (agents, instructions, skills, plugins, cookbook content) with a pre-registered Copilot marketplace listing. GitHub explicitly distinguishes the channel's official status from its community-sourced content — treat it as strong Copilot integration with limited cross-runtime portability, not a vetted content library.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — the market overview this page details
- [Orchestrating Modes](skills-orchestrating-modes.md) — dispatchers that route into a library's skills
- [Distribution and Governance](skills-management.md) — installation, versioning, and provenance mechanics
- [Choosing a Skills Approach](skills-choosing.md) — decision guide across the whole skills layer
- [Superpowers](superpowers.md) — a mandatory workflow built from skills
