# Distribution and governance

> **Observation date:** October 27, 2026. Marketplace contents, lockfile support, and compatibility-pass results change quickly — treat specific counts as dated unless marked Verified in the current pass.

This page covers the operational layer of running skills in practice: the specification itself, how skills get installed and updated, and how to evaluate, permission, and govern them once they're in a project. For a comparison of the content itself, see [Skill Libraries](skills-libraries.md); for request-routing dispatchers, see [Orchestrating Modes](skills-orchestrating-modes.md); for a decision guide across the whole layer, see [Choosing a Skills Approach](skills-choosing.md).

## The Agent Skills specification

[Agent Skills](https://agentskills.io) is a vendor-neutral, Apache-2.0 specification maintained under the [`agentskills`](https://github.com/agentskills/agentskills) organization. Anthropic's own skills repository points readers to this specification rather than presenting the format as Anthropic-owned.

A skill is a `SKILL.md` file with required `name` and `description` fields. Optional fields include `license`, `compatibility`, `metadata`, and the experimental `allowed-tools`. A skill can also bundle `scripts/`, `references/`, and `assets/` directories.

**Progressive disclosure** is the specification's core context-management mechanism, in three stages:

1. **Discovery** — the runtime reads lightweight metadata (name, description) for every installed skill, cheaply, at session start.
2. **Activation** — the runtime loads the full skill instructions only when the metadata suggests it's relevant.
3. **Execution** — the runtime pulls in referenced scripts or resource files only as the skill's instructions call for them.

This keeps a large skill library from consuming context budget up front — a library with hundreds of skills can still bootstrap in a small number of tokens, because only metadata is loaded until a skill actually activates.

## Cross-harness portability: format vs. behavior

Specification compliance guarantees a `SKILL.md` *parses* in any compliant runtime. It does not guarantee the skill *behaves* the same way everywhere. A prior compatibility pass found basic skill content worked across all 18 compared agents, while hooks worked in 4 of those agents and `context: fork` in only 1. Treat portability as two separate claims:

- **Format portability** — does the file parse and the metadata resolve? Close to universal across compliant runtimes.
- **Behavioral portability** — do hooks, hereditary context forking, and other optional runtime features actually execute? Sharply narrower, and runtime-specific.

The shared `.agents/skills/` path is an emerging vendor-neutral convention independent of any single installer: the `skills` CLI uses it for several targets, OpenSpec (v1.15.0) writes both skills and slash commands there with delivery configurable per project, and it's the install target referenced across several of this site's spec-driven technique pages.

## Native plugin marketplaces vs. CLI-vendored installs

Two structurally different distribution channels now coexist:

| | Native plugin marketplace | CLI-vendored copy |
|---|---|---|
| Example | Claude Code, GitHub Copilot, and Codex plugin marketplaces | skills.sh's `npx skills add ...`, `npx skills@latest update` |
| Who owns the copy | The publisher — you subscribe to a managed bundle | You — files are vendored directly into your project |
| Update timing | Automatic, often without a local review step (third-party Claude Code marketplaces default to auto-update *off*, requiring manual enablement) | Manual, triggered by you running an update command |
| Review opportunity | Limited — you're trusting the publisher's next push | Full — you can diff before accepting an update |
| Reproducibility | Weak — "current" means whatever the marketplace serves right now | Strong, if you pin a revision |

Both `mattpocock/skills` and `addyosmani/agent-skills` ship through both channels, and both projects warn against installing the same library both ways for one agent — doing so duplicates every skill. Pick one channel per agent per library, deliberately, rather than by default.

## skills.sh: installer, discovery, and a conflict-of-interest caveat

[skills.sh](https://skills.sh), operated by Vercel, combines several roles in one surface: installer (`add`, `update`, `remove`, `use`, `init`), discovery (`find` and a public directory), registry (automatic listing when telemetry records an install), ranking (install-count leaderboards built from anonymous CLI telemetry), and a portability layer mapping paths across a large and growing number of agent targets (`addyosmani/agent-skills` cites 70+ as of October 2026). It accepts GitHub, GitLab, arbitrary Git, local, and private-repository sources. Telemetry is enabled by default and can be disabled with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`.

Two caveats worth weighing before treating the directory as a trust signal: the default directory is not a curated trust store — entries can appear automatically and audit coverage is incomplete — and Vercel controls both the dominant installer and its leaderboard, which is relevant when evaluating governance and ranking incentives on this surface. Separately, skills.sh aggregates security findings from third-party scanners, but coverage is partial and some prominent skills show medium-risk findings; this was not re-verified in detail this pass.

## Versioning, lockfiles, and dependencies

Skills increasingly ship as semver-versioned packages with changelogs and graduated/staging buckets — `mattpocock/skills`'s engineering-bucket graduation process is a direct example. But package-manager-grade dependency management is largely absent:

- **No standard lockfile.** Nothing observed in this pass pins a skill to an exact revision the way a `package-lock.json` or `go.sum` would. A vendored copy is reproducible only because you control when you run the update command — there's no file recording "this is exactly what you have installed and why."
- **Per-skill installs can drop shared dependencies.** `addyosmani/agent-skills`'s own issue tracker documents a per-skill `npx skills add` install copying only `skills/<name>/`, not the repository-level `references/` directory another skill assumes is present ([issue #361](https://github.com/addyosmani/agent-skills/issues/361)). Check for shared references before trusting a partial install from any library.
- **Cross-channel version drift has no unified signal.** The same library can be "current" in one agent's native marketplace and "stale" in a vendored copy you haven't updated, with nothing surfacing that mismatch to you automatically.

## Provenance, signing, and compatibility

None of the installers, marketplaces, or libraries examined across this research provide cryptographic signing, attestation, or lockfile-style pinning for any install path. This is a layer-wide gap, not a weakness specific to one project.

Licensing and provenance can also differ *within* a single repository: `anthropics/skills` mixes Apache-2.0 skills with source-available ones (`docx`, `pdf`, `pptx`, `xlsx`) in the same collection. Review each skill's terms individually before reuse — don't assume a repository-level license badge covers every file inside it.

Compatibility, similarly, is not a single property of a library — it's a property of a specific (library version, runtime, install path) triple. A skill current in Claude Code's marketplace may be several versions behind in a project's vendored copy, and vice versa.

## Evaluation

Evidence of skill quality is almost entirely vendor-reported: release notes describing specific fixes or "N/N runs passed" test claims, written by the people who maintain the skill. This is useful as a signal of active maintenance but is not independent validation. Treat any specific test-pass figure, like any specific benchmark score elsewhere on this site, as **Reported**, not **Verified** — see [Research Methodology](../methodology.md#evidence-labels).

## Permissions, policy, and enterprise approval

Skills can contain executable scripts and instructions that influence a high-privilege agent — apply the same scrutiny you'd apply to a new dependency or a CI action, not less. Before installing a skill into a team or enterprise environment:

1. **Read `SKILL.md` and every referenced script** before installing, not after something goes wrong.
2. **Verify ownership and licensing** — repository owner, license terms (checked per skill, not per repository), release history, and whether the project is actively maintained.
3. **Decide the update policy explicitly.** Native-marketplace auto-update trades review for convenience; a pinned vendored copy trades convenience for reproducibility and review. In regulated or audited environments, this is a decision to make on purpose, not a default to inherit from the installer.
4. **Limit tool permissions and secrets** available to the agent running the skill — the experimental `allowed-tools` field in the specification is one lever, but it's explicitly marked experimental and shouldn't be your only control.
5. **Test in an isolated repository or worktree** before rolling a skill out broadly.
6. **Record the source revision** for any approved skill and review future updates as you would a code change — this is the closest practical substitute for the lockfile pinning the layer doesn't yet provide natively.

## Controlled rollout

For a team or enterprise rollout, a conservative sequence that follows from the gaps above:

1. Pilot a skill in one project or one willing team, on a pinned vendored copy, before any org-wide install.
2. Record the approved source revision somewhere durable (an internal registry entry, a pinned commit reference, or equivalent) — treat this as your substitute lockfile.
3. Route auto-updating marketplace installs through an explicit approval step rather than leaving default auto-update enabled for anything beyond individual experimentation.
4. Re-review on every update, the same way you'd re-review a dependency bump, rather than trusting that a passing smoke test covers behavioral drift.
5. Revoke and roll back the same way you'd roll back a bad dependency — keep the prior pinned revision available.

## No harness, thin harness, first-party runtime, opinionated methodology — where skills attach

Skills are a layer-two-and-three artifact in the site's [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology): they ride on top of whatever runtime executes them, and some methodologies additionally make specific skills mandatory. How skills attach differs by harness variant:

- **No harness (direct API calls)** — skills have no install target; the caller would need to implement discovery and loading itself.
- **Thin generic harness** (for example [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent)) — skill support, if any, is whatever the minimal loop chooses to implement; not a given.
- **First-party runtime** (Claude Code, Codex CLI, GitHub Copilot) — these are exactly the runtimes with native plugin marketplaces, making them the primary distribution target for managed skill bundles.
- **Opinionated methodology** (Superpowers, HVE) — skills stop being optional content and become mandatory workflow controls, enforced by the methodology layered on top of whichever runtime executes it.

## Current gaps

As of this observation date:

- No universal lockfile or pinning mechanism exists.
- Evaluation is vendor-reported, not independently audited.
- At least one major library shipped documented dependency-completeness failures — incomplete installs that silently dropped files another skill needed.
- No signal flags version drift across channels.
- No surface we examined signs or attests anything.

None of this makes the layer unusable. It makes deliberate, documented governance choices — channel, pinning, review cadence — necessary rather than optional.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — the market overview this page puts into practice
- [Skill Libraries](skills-libraries.md) — the content this page's mechanics apply to
- [Orchestrating Modes](skills-orchestrating-modes.md) — dispatchers with their own install and compatibility caveats
- [Choosing a Skills Approach](skills-choosing.md) — decision guide using these criteria
