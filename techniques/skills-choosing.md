# Choosing a skills approach

> **Observation date:** October 27, 2026. See [State of the Skills Market](skills-ecosystem.md) for the taxonomy this guide applies, and [Choosing Your Approach](choosing-your-approach.md) for the technique-level decision guide this page complements.

"Skills" today covers at least six structurally different things. Before adopting any of them, identify which one you actually need — they compose, but they are not substitutes for each other.

## What kind of thing are you actually choosing?

| Category | Example | Choose it when... | Trade-off |
|---|---|---|---|
| **Composable skill library** | [`mattpocock/skills`](skills-libraries.md) | You want a handful of independently selectable practices (TDD, code review, debugging) that you mix, edit, or ignore | You retain full control, but nothing enforces sequence, coverage, or quality gates |
| **Lifecycle library** | [`addyosmani/agent-skills`](skills-libraries.md) | You want skills organized around development stages (define → plan → build → verify → review → ship) without a mandatory gate between them | Stage-mapped commands give more structure than a composable library, but each command can still be invoked out of order |
| **Orchestrating mode** | [`pstack/poteto-mode`](skills-orchestrating-modes.md) | You want a dispatcher that reads a request and automatically routes to the right skill or playbook in a library you already use | Adds request-classification logic on top of a library — it has no function of its own if the underlying skills aren't installed |
| **Skill-driven methodology** | [Superpowers](superpowers.md) | You want a mandatory individual workflow — skills you cannot skip, with TDD and review enforcement built in | Strong discipline, but more ceremony and no team coordination |
| **Native runtime** | Claude Code, Codex CLI, GitHub Copilot plugin marketplaces | You want the simplest path: subscribe to a managed, auto-updating skill bundle inside the agent you already use | Convenient, but you're trusting the publisher's next push over a reviewed, pinned copy |
| **Custom internal catalog** | A team- or org-maintained internal skills repository | You need house conventions, proprietary domain knowledge, or compliance-specific instructions that no public library provides | You own all the maintenance, evaluation, and governance work a public library's maintainer would otherwise do |

These categories compose. A specification framework like Spec Kit can install skills as one of its extension types; a multi-agent runtime like Squad can equip individual agents with Superpowers-style skills; an orchestrating mode is only useful layered on a library it can dispatch into; a custom internal catalog can wrap or fork public skills rather than starting from nothing. Pick the row that matches your immediate need, then check whether you also need a layer above or below it.

## Decision criteria

Before adopting any skill library, orchestrating mode, methodology, or internal catalog, check it against these criteria. Full detail on each is in [Distribution and Governance](skills-management.md).

| Criterion | Question to ask | Why it matters |
|---|---|---|
| **Task shape** | Is the gap "the model doesn't know a convention," or "there's no reconstructable record of why a decision was made"? | The first is a skills gap; the second is a methodology gap. Don't reach for a methodology to solve a skills problem or vice versa. |
| **Workflow ownership** | Do you want to select individual practices yourself, or have something else decide the sequence for you? | Composable libraries hand you the wheel; lifecycle libraries and methodologies take varying degrees of it from you. |
| **Update channel** | Does it auto-update through a native plugin marketplace, or do you pull updates manually via a CLI? | Auto-update is convenient but hands you upstream changes unreviewed. A vendored copy is reviewable but only as current as your last update run. |
| **Portability** | Does the `SKILL.md` just parse in your runtime, or do the hooks, scripts, and `context: fork` features it depends on actually execute there? | Format portability and behavioral portability are different claims — a skill can install everywhere and work almost nowhere beyond its primary runtime. |
| **Provenance** | Is there signing, attestation, or lockfile-style pinning — or just a repository URL and a star count? | As of this observation date, nothing examined across the skills layer provides signing or attestation. Pin a revision if reproducibility matters. |
| **Evaluation** | Is quality evidence independently verified, or vendor-reported release-note testing? | Treat "N/N runs passed" as a signal from the maintainer, not third-party proof. |
| **Dependency completeness** | Does a per-skill install pull everything that skill needs, or only the named directory? | Partial installs can silently drop shared dependencies — a documented failure mode in at least one lifecycle library's issue tracker. |
| **Compatibility** | Is the skill's current version the same across every agent and install path you use it from? | The same library can be current in one runtime's marketplace and stale in a vendored copy, with no cross-channel version signal today. |
| **Policy and control** | Who decided whether this auto-updates, and does that match your change-control policy? | Auto-update-by-default versus manual-update-by-default is a policy choice — make it explicitly, especially in regulated or audited environments. |
| **Team coordination** | Does the choice need to work the same way for every person on a team using different tools? | A runtime-locked methodology (Squad, HVE are both Copilot-only) creates friction on a mixed-tool team; a portable specification or skills layer avoids it. |
| **Risk** | What's the blast radius if the skill does something unexpected — a bad suggestion, an executed script, a leaked secret? | Skills can bundle scripts and tool permissions. Registry presence or an audit badge is not a substitute for source review, permission limits, and pinning. |

## Practical guidance by need

| If you want... | Choose | Trade-off |
|---|---|---|
| Reusable practices you can mix, edit, or ignore | A composable library such as [`mattpocock/skills`](skills-libraries.md) | You retain control, but nothing enforces sequence or quality gates |
| Skills mapped to lifecycle stages without a full methodology | A lifecycle library such as [`addyosmani/agent-skills`](skills-libraries.md) | More structure than a composable library, but each stage command is still independently callable |
| Automatic request routing across a library's skills | An orchestrating mode such as [`pstack/poteto-mode`](skills-orchestrating-modes.md) | Only useful paired with the library it dispatches into — not a standalone capability |
| A mandatory individual workflow | [Superpowers](superpowers.md) | Strong TDD and review discipline, with more ceremony |
| Project- or change-level artifacts driving implementation | A specification framework — [Spec Kit](spec-kit.md), [OpenSpec](openspec.md), [GSD](gsd.md), or [BMAD](bmad.md) | Heavier upfront spec-writing investment; pick brownfield-first OpenSpec vs. project-level Spec Kit/GSD vs. full-team-simulation BMAD based on scope |
| Team-scale coordination or enterprise governance | A multi-agent/runtime approach — [Squad](squad.md) or [HVE](hve.md) | Copilot lock-in for both; skills become one ingredient inside a larger, heavier runtime |
| Automatic upstream updates, accepting less local review | A native plugin marketplace subscription (Claude Code, Copilot, or Codex) | Convenient, but upstream changes arrive without a local review step |
| Reviewable, reproducible files you control | A vendored copy through skills.sh or the `skills` CLI, preferably pinned | You own updates, conflicts, and local modifications |
| House conventions or proprietary domain knowledge no public library covers | A custom internal catalog, optionally forked from a public library | Full control and fit, but you own all maintenance, evaluation, and governance that a public maintainer would otherwise carry |

Skills are additive: you can use a library, a lifecycle library, or an orchestrating mode with any Tier 1 methodology or specification framework. Check for duplicate instructions, conflicting workflows, runtime-specific features, and unreviewed scripts — and check the criteria above before you standardize on one.

## The decision rule

The same rule that governs the technique-level choice in [Choosing Your Approach](choosing-your-approach.md#layer-check-model-runtime-or-methodology-first) applies one layer down, inside the skills decision itself:

1. **Start with the model and its native runtime.** For a bounded, well-specified, independently verifiable task, this is often sufficient on its own — no skill required.
2. **Add skills when the gap is reusable expertise** the model doesn't reliably apply on its own — a missing convention, a domain pattern, a house style. Pick a composable or lifecycle library, or write your own, based on how much structure you want imposed.
3. **Add a methodology when the gap is coordination or traceability** — multiple agents, multiple people, or a need to reconstruct why a change was made. This is when a skill-driven methodology like Superpowers, or a heavier specification framework, earns its overhead.
4. **Strengthen controls as autonomy, duration, cost, or risk increase.** Governance, audit trails, approval gates, and pinned/reviewed installs should scale with blast radius and compliance exposure — not be the default starting posture for every skill you try.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — the taxonomy and market overview
- [Skill Libraries](skills-libraries.md) — composable and lifecycle library comparison
- [Orchestrating Modes](skills-orchestrating-modes.md) — dispatcher-pattern detail
- [Distribution and Governance](skills-management.md) — installation, versioning, and provenance mechanics
- [Superpowers](superpowers.md) — the skill-driven methodology profile
- [Choosing Your Approach](choosing-your-approach.md) — the technique-level decision guide this page complements
