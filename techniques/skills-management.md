# Distribution and governance

> **Observation date:** October 27, 2026. Marketplace contents, lockfile support, and compatibility results are dated snapshots, including those marked Verified.

This page covers the skill specification, installation, updates, evaluation, permissions, and governance. Compare content in [Skill Libraries](skills-libraries.md), request routing in [Orchestrating Modes](skills-orchestrating-modes.md), and selection criteria in [Choosing a Skills Approach](skills-choosing.md).

## The Agent Skills specification

[Agent Skills](https://agentskills.io) is a vendor-neutral, Apache-2.0 specification maintained under the [`agentskills`](https://github.com/agentskills/agentskills) organization. Anthropic's own skills repository points readers to this specification rather than presenting the format as Anthropic-owned.

A skill is a `SKILL.md` file with required `name` and `description` fields. Optional fields include `license`, `compatibility`, `metadata`, and the experimental `allowed-tools`. A skill can also bundle `scripts/`, `references/`, and `assets/` directories.

**Progressive disclosure** is the specification's core context-management mechanism, in three stages:

1. **Discovery** — the runtime reads lightweight metadata (name, description) for every installed skill at session start.
2. **Activation** — the runtime loads the full skill instructions only when the metadata suggests it's relevant.
3. **Execution** — the runtime pulls in referenced scripts or resource files only as the skill's instructions call for them.

Only metadata uses context until a skill activates; the full library does not need to load at session start.

## Cross-harness portability: format vs. behavior

Specification compliance guarantees a `SKILL.md` *parses* in any compliant runtime. It does not guarantee the skill *behaves* the same way everywhere. A prior compatibility pass found basic skill content worked across all 18 compared agents, while hooks worked in 4 of those agents and `context: fork` in only 1. Treat portability as two separate claims:

- **Format portability** — does the file parse and the metadata resolve? Close to universal across compliant runtimes.
- **Behavioral portability** — do hooks, context forking, and other optional runtime features execute? Support is narrower and runtime-specific.

The shared `.agents/skills/` path is an emerging vendor-neutral convention independent of any single installer: the `skills` CLI uses it for several targets, OpenSpec (v1.15.0) writes both skills and slash commands there with delivery configurable per project, and it's the install target referenced across several of this site's spec-driven technique pages.

## Native plugin marketplaces vs. CLI-vendored installs

Two structurally different distribution channels now coexist:

[Diagram: Two skill installation paths](../diagrams/skill-distribution.html)

| | Native plugin marketplace | CLI-vendored copy |
|---|---|---|
| Example | Claude Code, GitHub Copilot, and Codex plugin marketplaces | skills.sh's `npx skills add ...`, `npx skills@latest update` |
| Who owns the copy | The publisher — you subscribe to a managed bundle | You — files are vendored directly into your project |
| Update timing | Automatic, often without a local review step (third-party Claude Code marketplaces default to auto-update *off*, requiring manual enablement) | Manual, triggered by you running an update command |
| Review opportunity | Limited — you're trusting the publisher's next push | Full — you can diff before accepting an update |
| Reproducibility | Weak — "current" means whatever the marketplace serves right now | Strong, if you pin a revision |

Both `mattpocock/skills` and `addyosmani/agent-skills` ship through both channels and warn against installing both ways for one agent. Choose one channel per library per agent to avoid duplicate skills.

## skills.sh: installer, discovery, and a conflict-of-interest caveat

[skills.sh](https://skills.sh), operated by Vercel, provides installation (`add`, `update`, `remove`, `use`, `init`), discovery (`find` and a public directory), and install-count rankings. Anonymous CLI telemetry records installs for automatic directory listings and leaderboards.

The CLI maps install paths across agent targets; `addyosmani/agent-skills` cites 70+ as of October 2026. It accepts GitHub, GitLab, arbitrary Git, local, and private-repository sources. Telemetry is on by default; disable it with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`.

The directory is not a curated trust store: entries can appear automatically, and audit coverage is incomplete. Vercel controls both the installer and its leaderboard, so consider that relationship when interpreting rankings.

skills.sh also aggregates third-party security findings. Coverage is partial, and some prominent skills showed medium-risk findings; these were not re-verified in detail this pass.

## Versioning, lockfiles, and dependencies

Skills increasingly use semver releases, changelogs, and staging-to-release processes, as in `mattpocock/skills`. Dependency management remains limited:

- **No standard lockfile.** Nothing observed in this pass pins a skill to an exact revision like `package-lock.json` or `go.sum`. Vendoring lets you control updates, but does not itself record the source revision or dependency resolution.
- **Per-skill installs can drop shared dependencies.** `addyosmani/agent-skills`'s own issue tracker documents a per-skill `npx skills add` install copying only `skills/<name>/`, not the repository-level `references/` directory another skill assumes is present ([issue #361](https://github.com/addyosmani/agent-skills/issues/361)). Check for shared references before trusting a partial install from any library.
- **Cross-channel version drift has no unified signal.** The same library can be "current" in one agent's native marketplace and "stale" in a vendored copy you haven't updated, with nothing surfacing that mismatch to you automatically.

## Provenance, signing, and compatibility

None of the installers, marketplaces, or libraries examined across this research provide cryptographic signing, attestation, or lockfile-style pinning for any install path. This is a layer-wide gap, not a weakness specific to one project.

Licensing and provenance can also differ *within* a single repository: `anthropics/skills` mixes Apache-2.0 skills with source-available ones (`docx`, `pdf`, `pptx`, `xlsx`) in the same collection. Review each skill's terms individually before reuse — don't assume a repository-level license badge covers every file inside it.

Check compatibility for the specific library version, runtime, and install path. A marketplace installation and a vendored copy can contain different versions of the same skill.

## Evaluation

Evidence of skill quality is almost entirely vendor-reported: release notes describing specific fixes or "N/N runs passed" test claims, written by the people who maintain the skill. This is useful as a signal of active maintenance but is not independent validation. Treat any specific test-pass figure, like any specific benchmark score elsewhere on this site, as **Reported**, not **Verified** — see [Research Methodology](../methodology.md#evidence-labels).

## Permissions, policy, and enterprise approval

Skills can contain scripts and instructions that influence a high-privilege agent. Review them as you would a dependency or CI action before team or enterprise use:

1. **Read `SKILL.md` and every referenced script** before installing.
2. **Verify ownership and licensing** — repository owner, license terms (checked per skill, not per repository), release history, and whether the project is actively maintained.
3. **Set an update policy.** Auto-updating marketplace installs reduce local review opportunities. Pinned vendored copies need manual updates but support review and reproducibility. Match the channel to your change-control requirements.
4. **Limit tool permissions and secrets** available to the agent running the skill — the experimental `allowed-tools` field in the specification is one lever, but it's explicitly marked experimental and shouldn't be your only control.
5. **Test in an isolated repository or worktree** before rolling a skill out broadly.
6. **Record the approved source revision** and review updates as code changes. This substitutes for the missing native lockfile pinning.

## Controlled rollout

For a team or enterprise rollout:

1. Pilot a skill in one project or one willing team, on a pinned vendored copy, before any org-wide install.
2. Record the approved source revision in an internal registry or pinned commit reference.
3. Route auto-updating marketplace installs through an explicit approval step rather than leaving default auto-update enabled for anything beyond individual experimentation.
4. Review each update as a dependency change; a passing smoke test does not cover every behavior change.
5. Keep the prior pinned revision available for rollback.

## No harness, thin harness, first-party runtime, opinionated methodology — where skills attach

Skills operate in the runtime and methodology layers of the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology). Integration depends on the harness:

- **No harness (direct API calls)** — skills have no install target; the caller would need to implement discovery and loading itself.
- **Thin generic harness** (for example [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent)) — skill support, if any, is whatever the minimal loop chooses to implement; not a given.
- **First-party runtime** (Claude Code, Codex CLI, GitHub Copilot) — native plugin marketplaces install managed skill bundles.
- **Opinionated methodology** (Superpowers, HVE) — skills stop being optional content and become mandatory workflow controls, enforced by the methodology layered on top of whichever runtime executes it.

## Current gaps

As of this observation date:

- No universal lockfile or pinning mechanism exists.
- Evaluation is vendor-reported, not independently audited.
- At least one major library shipped documented dependency-completeness failures — incomplete installs that silently dropped files another skill needed.
- No signal flags version drift across channels.
- No skill distribution path we examined provides signing or attestation.

Choose an update channel, record approved revisions, and define how updates will be reviewed.

## Related pages

- [State of the Skills Market](skills-ecosystem.md) — the market overview this page puts into practice
- [Skill Libraries](skills-libraries.md) — the content this page's mechanics apply to
- [Orchestrating Modes](skills-orchestrating-modes.md) — dispatchers with their own install and compatibility caveats
- [Choosing a Skills Approach](skills-choosing.md) — decision guide using these criteria
