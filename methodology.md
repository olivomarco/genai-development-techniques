# Research methodology

## Purpose and scope

This page explains how the comparison is researched, what counts as evidence, and how entries get added, updated, or removed. Read it before citing a claim from this site or before asking why a project is included, excluded, or described a certain way.

The scope is **techniques for directing AI coding agents** — methodologies, skill libraries, orchestrating modes, and the supporting skills-distribution layer. It is not a review of AI models, IDEs, or general-purpose agent runtimes, except where those are needed to explain the three-layer model (model, runtime, methodology) referenced throughout the site.

## What this is and is not

**This is:**

- A dated snapshot of publicly observable information — READMEs, release notes, changelogs, issue trackers, and primary-source blog posts.
- A structural comparison: what a technique does, what it requires, and what trade-offs it documents about itself.
- A living document, revised in discrete research passes with a recorded observation date.

**This is not:**

- A ranking or a "best technique" verdict.
- An adoption survey. Star counts and install figures are awareness signals, not evidence of production use.
- A benchmark of model or agent capability.
- An endorsement of any project, author, or vendor.
- The output of an advisory board, editorial committee, or formal review process. One person does this research and is responsible for its errors.

## Definitions

**Technique.** A documented, named approach to structuring how a human directs one or more AI coding agents — a methodology, a workflow, or a skill-based system with its own install path and maintained source.

**Ecosystem layer.** Infrastructure the techniques above plug into but that is not itself a technique — the Agent Skills specification, skill libraries, orchestrating modes, installer CLIs, and native plugin marketplaces. These are covered under [Skills and Agent Frameworks](techniques/skills-ecosystem.md) rather than as Tier 1 entries.

**Tier 1 inclusion.** A technique earns a dedicated comparison page when it meets all of the following:

1. A public, actively maintained source (repository, specification, or canonical write-up).
2. Enough documented structure to describe a repeatable workflow — not just a prompt or a one-off script.
3. Independent verifiability: someone other than the author can install it and observe the behavior it claims.
4. Enough adoption signal (releases, usage, community activity, or institutional backing) to justify research time, while adoption signal alone never substitutes for criteria 1-3.

Projects that fail this bar are not dismissed — they appear on the "projects to consider next" watchlist in the overview, with an explicit note on why they weren't promoted.

## Inclusion and exclusion criteria

A project is **included** when it has a canonical source, a license, and observable release history. A project is **excluded or demoted to watchlist** when:

- It has no releases or tags (undermines "what version is this" claims).
- Its license or ownership is ambiguous.
- It duplicates an already-covered technique without a distinct workflow.
- It could not be independently verified within the current research pass's time budget.

Exclusion is a statement about verification budget and current evidence, not a judgment of merit.

## Canonical-source preference

When a project is distributed through multiple mirrors, ports, or community adaptations, the canonical upstream source is the primary citation. Community ports are noted — often with real adoption signal of their own — but are clearly labeled as unofficial, and any drift from the canonical source's behavior is flagged rather than assumed to track it.

## Evidence labels

Every non-trivial claim on this site is implicitly or explicitly one of:

- **Verified.** Confirmed directly against a primary source during the current research pass — a README, release note, changelog entry, or the project's own canonical documentation.
- **Reported.** Stated by the project itself (release notes, blog posts, vendor claims) but not independently reproduced. Vendor-reported benchmark numbers and "N/N tests passed" release notes fall here.
- **Signal.** A proxy for relevance or momentum — star counts, install counts, newsletter subscriber counts, forum activity — that indicates attention, not correctness or adoption.

Where a page doesn't label a claim explicitly, assume **Reported** for anything attributed to a project's own materials and **Signal** for any bare metric.

## Observation dates and volatile metrics

Every page that cites metrics states an observation date. Star counts, install counts, release numbers, and plugin-marketplace contents change quickly and are treated as perishable: a figure from an earlier pass is marked as such rather than silently carried forward as current. If a metric could not be re-verified in the current pass, the page says so instead of restating the old number without qualification.

## Handling conflicting evidence and uncertainty

When sources disagree — a README claim contradicts an issue tracker, or a changelog doesn't match observed behavior — the page states both and explains the discrepancy rather than picking one silently. When something could not be verified at all, the page says so explicitly ("not re-verified this pass," "unverified," "pending confirmation") instead of omitting the gap.

## Update process

Updates happen in dated research passes, not on a fixed calendar. A pass re-checks canonical sources for the techniques and ecosystem layers in scope, records what changed, and logs the result in [Market Updates](market-updates.md). There is no promised cadence — passes happen when enough material has changed to justify one, and the site does not claim to track every release the moment it ships.

## Non-ranking policy

No page assigns an overall score, a star rating across techniques, or a single "winner." Comparison tables describe dimensions (setup complexity, governance, tool compatibility, and so on) side by side; the reader matches rows to their own situation using [Choosing Your Approach](techniques/choosing-your-approach.md). Any rating that does appear inside a page (for example, a per-scenario fit score) is scoped to that specific scenario, not a general verdict on the technique.

## Correction and removal policy

If a claim is found to be wrong, outdated beyond the point of being a useful signal, or sourced from content that no longer exists, it is corrected or removed in the next research pass and the change is logged in [Market Updates](market-updates.md). Removals are not silent: a technique dropped from Tier 1 status is noted, with the reason, rather than deleted without explanation.
