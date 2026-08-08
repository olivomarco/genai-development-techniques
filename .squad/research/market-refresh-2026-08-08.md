# Market & Freshness Research — 2026-08-08

**Researcher:** Trinity
**Requested by:** Marco Olivo
**Brief:** `.squad/research/refresh-brief-2026-08-08.md` (Neo)
**Common observation date:** 2026-08-08 (all metrics below are same-day snapshots unless noted)
**Boundary:** Raw research notes and evidence. Not final comparison prose. No public page was modified.

---

## 1. Executive market findings

### 1.1 The headline: skills became a specification, not just a feature

The single largest change since the June pass is that **Agent Skills is now a published, vendor-neutral specification with its own governance org**, not an Anthropic-proprietary convention. `agentskills.io` documents a formal `SKILL.md` format (required `name`, `description`; optional `license`, `compatibility`, `metadata`, `allowed-tools`), a three-stage progressive-disclosure model (discovery → activation → execution), and a "for client implementors" track. The spec repo `agentskills/agentskills` is Apache-2.0 with ~24.0K stars. Anthropic's own `anthropics/skills` README now explicitly defers to it: *"For information about the Agent Skills standard, see agentskills.io."*

This directly falsifies the current `context-engineering.md` framing that rules-file formats are fragmented with no standardization emerging. That was true for *rules files* (`.cursorrules`, `CLAUDE.md`, `copilot-instructions.md`) and remains partly true there — but a genuine cross-vendor packaging standard has now emerged one layer up. The honest current statement is: **rules files remain fragmented; skills packaging has converged on a documented spec.**

### 1.2 A shared on-disk convention is consolidating

`.agents/skills/` is emerging as the vendor-neutral install path. The `skills` CLI maps Amp, Replit, Codex, Antigravity, Cline, Zed, Warp, Dexto, Kimi Code CLI, Loaf and a "universal" target to `.agents/skills/`. Independently, OpenSpec v1.8.0 added a vendor-neutral `agents` target that "writes skills to the shared `.agents/skills/` that AGENTS.md-aware assistants read." Two unrelated projects converging on the same path is a real interoperability signal, not marketing.

**Caveat for Oracle:** convergence on a *path and file format* is not runtime parity. The `skills` CLI's own compatibility matrix proves this — across 18 agents, basic skills are universally supported, `allowed-tools` is supported by 16 of 18, hooks by only 4, and `context: fork` by exactly 1 (Claude Code). Portability of skill *content* is real; portability of skill *execution semantics* is not. This is the most important nuance for the new page.

### 1.3 Distribution split into two competing philosophies

The market now has two distinct, explicitly acknowledged distribution models, and `mattpocock/skills` documents both in its own README:

- **Managed subscription** — Claude Code plugin marketplace. Read-only bundle, updates arrive automatically, you subscribe rather than fork.
- **Vendored copy** — `npx skills add owner/repo`. Editable files land in your repo, nothing changes behind your back, you pull updates on demand.

This is the classic package-manager-vs-vendoring tradeoff arriving in the agent space. It is a genuinely useful decision axis for `choosing-your-approach.md` and is more durable than any star count.

### 1.4 Methodology vs. ecosystem is now an explicit market argument

`mattpocock/skills` is not neutral about the frameworks this repo documents. Its README argues directly against them: *"Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."* Its counter-position is small, composable, adaptable skills.

This validates Neo's taxonomy call. There is a real market split between **process-owning methodologies** (GSD, BMAD, Spec Kit, HVE, Squad) and **composable skill libraries** (mattpocock/skills, anthropics/skills, vercel-labs/agent-skills). Superpowers is the interesting hybrid: it uses the skill *primitive* but applies it to enforce a *mandatory methodology* — which is exactly the thing Pocock is arguing against. The two are best framed as opposing philosophies built on the same substrate, not as competitors on a single axis.

### 1.5 Security and provenance moved from absent to nascent

June's pass had nothing to say here. Now:

- **skills.sh runs a public security audit surface** aggregating three independent scanners (Gen Agent Trust Hub, Socket, Snyk) with per-skill verdicts. Coverage is partial — many entries show "Pending" — and even top-ranked skills carry "Med Risk" Snyk verdicts, so the presence of an audit page is not a clean bill of health.
- **The `skills` CLI documents credential handling explicitly**: it uses existing Git credentials, never executes `gh auth token`, and never copies the GitHub CLI credential into the Node process. Telemetry is on by default (`DISABLE_TELEMETRY` / `DO_NOT_TRACK` opt-out), and security-audit requests are limited to confirmed-public repos.
- **Skill authors are now writing defensive content.** `mattpocock/skills` v1.2.3 made `diagnosing-bugs` redact secrets by default.
- **Unresolved risk:** skills bundle executable `scripts/`, install into agent-readable paths, and the spec's `allowed-tools` is marked *Experimental*. There is no signing, no provenance attestation, and no lockfile-style pinning in any surface examined. Treat this as the ecosystem's clearest open weakness.

`github/awesome-copilot` carries an explicit third-party sourcing warning, which is the right posture and worth citing as a contrast to registries that do not.

### 1.6 Adoption evidence is strong in some places and weak in others

**Strong evidence:** skills.sh publishes per-skill install counts from CLI telemetry. `mattpocock/skills` shows 14.4M total installs across 51 listed skills, with `grill-me` at 799.2K. This is a materially better adoption signal than stars because it measures *use*, not bookmarking.

**Weak evidence, flag loudly:** the star counts across this entire market have inflated to a degree that makes them nearly useless for ranking. Superpowers at ~269K, `mattpocock/skills` at ~210K after six months, `anthropics/skills` at ~167K. A six-month-old skills library outranking GitHub's own Spec Kit (~126K) does not reflect a comparable depth of production adoption. **Recommendation: demote stars to a secondary signal in public tables and lead with install counts, release cadence, and contributor counts where available.**

Counter-evidence worth stating plainly: `mattpocock/skills` has only **3 listed non-anonymous contributors**. Huge star and install counts, essentially single-author maintenance. That is a real bus-factor risk and belongs on the page.

### 1.7 Two structural corrections that outrank everything else

**GSD's canonical repository is archived.** `gsd-build/get-shit-done` is `archived: true` as of the 2026-08-08 observation, with a README that reads "GSD Has Moved." Development continues as **GSD Core** at `open-gsd/gsd-core` (MIT, ~7.9K stars, v1.10.0 published 2026-08-08, npm `@opengsd/gsd-core`). Every GSD reference in the docs — source URL, version, star count, install command, star-history chart — is now wrong. This is the highest-priority fix in the whole refresh.

Note the metric discontinuity: the archived repo holds ~64.7K stars; the successor has ~7.9K. **Do not report this as GSD losing 57K stars.** It is a repository migration and the new repo is accumulating from zero. Any public table must footnote this or it will read as collapse.

**Two watchlist repos silently relocated.** `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`, and `block/goose` → `aaif-goose/goose`. Old URLs redirect today but should be updated.

---

## 2. Detailed profile — `mattpocock/skills`

### 2.1 Identity and metrics (observed 2026-08-08)

| Field | Value | Source |
|---|---|---|
| Canonical URL | `https://github.com/mattpocock/skills` | GitHub API |
| Owner | Matt Pocock (individual; TypeScript educator, aihero.dev) | repo owner, plugin.json |
| Description | "Skills for Real Engineers. Straight from my .agents directory." | GitHub API |
| License | MIT | GitHub API |
| Created | 2026-02-03 | GitHub API |
| Stars / forks | 209,856 / 18,134 | GitHub API |
| Last push | 2026-08-07 | GitHub API |
| Latest release | v1.2.3, published 2026-08-06 (stable; no prerelease channel observed) | Releases API |
| Prior releases | v1.2.2 (2026-08-05), v1.2.0 (2026-08-05), v1.1.0 (2026-07-08) | Releases API |
| Listed contributors | 3 | Contributors API |
| `SKILL.md` files in repo | 35 | Git tree API (untruncated) |
| Skills listed on skills.sh | 51 | skills.sh/mattpocock/skills |
| Total installs (skills.sh) | 14.4M | skills.sh/mattpocock/skills |

**Discrepancy, unresolved:** the repo contains 35 `SKILL.md` files on `main`, but skills.sh lists 51 skills for the same source. Possible causes include historical/removed skills retaining telemetry rows, plugin-bundle expansion, or directory-level counting differences. **Not verified — do not publish either number as "the" skill count without stating which surface it came from.**

### 2.2 What is actually distributed

Skills are organized into four active categories plus staging:

- `skills/engineering/` (18): `tdd`, `code-review`, `implement`, `research`, `diagnosing-bugs`, `domain-modeling`, `codebase-design`, `improve-codebase-architecture`, `prototype`, `grill-with-docs`, `to-spec`, `to-tickets`, `triage`, `wayfinder`, `wizard`, `resolving-merge-conflicts`, `ask-matt`, `setup-matt-pocock-skills`
- `skills/productivity/` (7): `grill-me`, `grilling`, `handoff`, `teach`, `to-questionnaire`, `wait-what`, `writing-for-agents`
- `skills/misc/` (4): `git-guardrails-claude-code`, `setup-pre-commit`, `scaffold-exercises`, `migrate-to-shoehorn`
- `skills/in-progress/` (6): explicitly staged, not stable
- Repo also carries `.agents/`, `.claude-plugin/`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `docs/`, `.out-of-scope/`

Top skills by install count: `grill-me` (799.2K), `grill-with-docs` (679.9K), `improve-codebase-architecture` (654.9K), `tdd` (633.3K), `setup-matt-pocock-skills` (581.4K).

### 2.3 Installation and discovery

Two documented paths, described by the author as "two ways in, two philosophies":

1. `claude plugins install mattpocock-skills` — official Claude Code marketplace, no marketplace registration needed, read-only managed bundle, auto-updates. Manifest: `.claude-plugin/plugin.json`, name `mattpocock-skills`, version 1.2.3, MIT.
2. `npx skills@latest add mattpocock/skills` — vercel-labs `skills` CLI, interactive skill and agent selection, writes editable files, `npx skills update` to pull changes.

The README warns that installing both leaves every skill duplicated. A native Codex plugin is on the roadmap per `.agents/adr/0002-ship-as-a-claude-code-plugin.md`.

**Required post-install step:** `/setup-matt-pocock-skills`, run once per repo. It configures issue tracker (GitHub, Linear, or local files), triage labels, and docs location. This is a genuine configuration step, not decoration — the `/triage` skill depends on the label config.

### 2.4 Which agents consume it

Claude Code natively via the official plugin. Any of the ~70 agents supported by the `skills` CLI via `npx skills add`. Verified compatibility is at the SKILL.md-reading level; per the CLI's own matrix, advanced features degrade by agent. **Do not claim uniform behavior across agents.**

### 2.5 Methodology or ecosystem?

**Ecosystem/library. It does not meet Neo's Tier 1 threshold.** Evidence:

- *Against methodology:* explicitly rejects process ownership ("Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process... they take away your control"). Skills are described as "small, easy to adapt, and composable." There is no mandated sequence, no phase gates, no lifecycle state machine, no governance layer. Skills are organized by topic, not by workflow stage.
- *Partially toward methodology:* it does encode opinionated practice — a `tdd` skill, a two-stage `code-review` skill, a `grill-me` alignment ritual the author says to "use every time," and a documented failure-mode taxonomy (misalignment, verbosity, etc.). The repo also documents its own skill-authoring discipline (`writing-great-skills`, `write-a-skill`).
- *Decisive:* criterion 2 (documented workflow with repeatable artifacts) is partially met per-skill but not end-to-end; criterion 3 (quality/verification/governance mechanisms) is met only within individual skills, with nothing enforcing them; criterion 6 (distinct decision value) is met — but as an *ecosystem* contrast to Superpowers, not as a competing SDLC.

**Disposition: lead profile on `techniques/skills-ecosystem.md`. Do not promote to the Tier 1 matrix.** This matches Neo's stated default and I found no evidence to overturn it.

### 2.6 Comparison with Superpowers

| Axis | mattpocock/skills | Superpowers |
|---|---|---|
| Nature | Skill library / ecosystem | Skills framework + development methodology |
| Enforcement | None; pick what you want | Mandatory skills enforce the workflow |
| Stated philosophy | Keep user control, stay adaptable | Enforce discipline, pressure-tested compliance |
| Composition | Topic-organized, independently usable | Orchestrated lifecycle (SDD, plan-scoped workspace) |
| Stars (2026-08-08) | 209,856 | 269,251 |
| Latest stable | v1.2.3 (2026-08-06) | v6.2.0 (2026-07-24) |
| Maintenance | 3 listed contributors | Broader contributor base, Prime Radiant backing |
| Install signal | 14.4M installs via skills.sh | Not published on the same surface |

The genuinely interesting framing for the page: both are built on the same `SKILL.md` primitive and reach opposite conclusions about whether skills should *constrain* the developer. That is a better comparison than any metric table.

---

## 3. Candidate dispositions (all nine)

### 3.1 `mattpocock/skills` — MANDATORY

**Disposition: include as lead ecosystem profile on `techniques/skills-ecosystem.md`. Not Tier 1.** Full profile in section 2. Confidence: high — all claims from primary sources (repo, plugin manifest, changelog, skills.sh).

### 3.2 Anthropic canonical Agent Skills documentation — HIGH

**Disposition: include on the ecosystem page as the format/standard anchor. Not a technique.**

Two distinct things, and the docs must not conflate them:

- **The standard:** `agentskills.io` + `agentskills/agentskills` (Apache-2.0, ~24.0K stars, ~1.7K forks, last push 2026-08-04, 51 open issues). Vendor-neutral org, not under `anthropics/`. Documents directory structure, frontmatter schema, progressive disclosure, file references, validation, a client showcase, and an "adding skills support" implementor guide. Has an official Discord.
- **Anthropic's reference implementation:** `anthropics/skills` (~167.0K stars, ~19.9K forks, last push 2026-08-07). **License is mixed and this matters:** GitHub reports no top-level SPDX license; the README states many skills are Apache-2.0, while the `docx`, `pdf`, `pptx`, `xlsx` document skills are **source-available, not open source**. The repo carries an explicit disclaimer that skills are "for demonstration and educational purposes only." It contains `./spec` and `./template` directories and is installable as a Claude Code plugin marketplace (`/plugin marketplace add anthropics/skills`).

**Interoperability claims documented:** "Cross-product reuse — build a skill once and use it across any skills-compatible agent." Report this as a documented *design goal* with a verified format basis, qualified by the observed feature-support gaps.

### 3.3 `skills.sh` and its canonical repository — HIGH

**Disposition: include on the ecosystem page as the registry/installer layer.**

- Canonical repo: **`vercel-labs/skills`** (MIT, ~28.4K stars, ~2.4K forks, created 2026-01-14, last push 2026-08-07, ~1000 open issues). Homepage `https://skills.sh`, which redirects to `https://www.skills.sh/`.
- npm package `skills`, latest **1.5.22**, with a separate `snapshot` channel at `1.5.12-snapshot.2`. Registry last modified 2026-08-05.
- **It is all four things at once** — this is the accurate answer to Neo's question. Installer (`add`, `update`, `remove`, `use`, `init`), registry/discovery (`find`, plus the skills.sh directory), ranking site (install-count leaderboard from anonymous CLI telemetry), and a *de facto* portability layer (~70 agent targets with per-agent path mapping). It is **not** the standard — it defers to agentskills.io.
- Sources supported: GitHub shorthand, full GitHub URL, deep tree paths, GitLab, arbitrary git URLs, local paths, and private repos via existing Git/gh/SSH auth.
- **Curation model:** essentially uncurated and user-submitted. Skills appear on the leaderboard *automatically* via telemetry once anyone installs them. There is an "Official" section and "Packs" (unlisted curated collections, Vercel sign-in to create), but the default surface is open.
- **Provenance/security controls:** the `/audits` page aggregates Gen Agent Trust Hub, Socket, and Snyk. Coverage is partial (many "Pending"); `find-skills` and `setup-matt-pocock-skills` both show "Med Risk" from Snyk. Credential handling is documented and conservative. Telemetry is opt-out, not opt-in. **No signing, no attestation, no pinning.**
- Vercel operates it ("Made with care by Vercel"). Worth noting as a governance consideration — the dominant installer and the leaderboard are controlled by one vendor.

### 3.4 GitHub Copilot skills ecosystem / `github/awesome-copilot` — HIGH

**Disposition: still canonical for Copilot. Include as a curated-but-community contrast case on the ecosystem page.**

- `github/awesome-copilot` (MIT, ~37.6K stars, ~4.7K forks, last push 2026-08-07). Website `awesome-copilot.github.com` with full-text search and a Learning Hub. Machine-readable `llms.txt` published.
- **Official vs community — the key distinction:** the repo is GitHub-owned and the marketplace is pre-registered in Copilot CLI/VS Code (`copilot plugin install <name>@awesome-copilot`), but the *content* is explicitly "community-created" and "sourced from third-party developers," with a stated caution. So: official *distribution channel*, community *content*. Do not describe the skills themselves as official GitHub guidance.
- Resource types: Agents, Instructions, Skills ("self-contained folders with instructions and bundled assets"), Plugins (curated bundles), Cookbook.
- **Portability beyond Copilot:** low. Content is organized around Copilot-specific surfaces (agents, instructions by file pattern, hooks, agentic workflows). Skills follow the SKILL.md shape and are therefore *readable* elsewhere, but instructions/agents/plugins are Copilot-shaped. Classify as readable-artifact compatibility, not portability.
- Corroborates the existing Squad/HVE lock-in observation from a different angle.

### 3.5 OpenSkills — HIGH

**Disposition: EXCLUDE from the ecosystem page except as a one-line historical/watchlist mention.**

- Canonical repo: `numman-ali/openskills` (~10.7K stars, ~669 forks, 43 open issues). npm `openskills`. License metadata reports `NOASSERTION` although the README badge claims Apache-2.0 — **inconsistent, not verified.**
- **Decisive finding: last push 2026-01-18.** Roughly seven months stale as of the observation date, in the fastest-moving segment of this market. Its stated value proposition — "brings Anthropic's skills system to every AI coding agent," "the universal installer for SKILL.md" — has been comprehensively superseded by `vercel-labs/skills` (~70 agents, active daily) and by the agentskills.io spec making universality a property of the format rather than of any one loader.
- The name is also ambiguous: at least four unrelated projects use "OpenSkills" (`instavm/open-skills` 445★, `LingyiChen-AI/OpenSkills` 68★, `Geeksfino/openskills` 67★). Any reference must be fully qualified.
- Does not meet Neo's criterion 4 (evidence of current maintenance). Adoption is insufficient and trending down.

### 3.6 OpenHands — CARRY-FORWARD

**Disposition: remain watchlist. No methodology profile. Update the URL.**

- **URL changed:** `All-Hands-AI/OpenHands` → **`OpenHands/OpenHands`** (MIT, ~83.5K stars, ~10.8K forks, last push 2026-08-08). Up from ~77.9K in June.
- Latest releases v1.12.0 and v1.11.0, both published 2026-08-07 — notably now past 1.0, so the "early platform" framing is outdated.
- Still self-describes as "AI-Driven Development" — a platform, not a transferable method. No evidence found of a documented, portable workflow with artifacts and quality gates that could be applied outside the platform. Fails criteria 1 and 6.

### 3.7 Open SWE — CARRY-FORWARD

**Disposition: remain watchlist as a substrate note only.**

- `langchain-ai/open-swe` (MIT, ~10.5K stars, ~1.2K forks, last push 2026-08-08). Up from ~10K in June.
- **No releases and no tags published** — verified via both endpoints. For a project this visible, the absence of any versioned release is a genuine maturity signal and should be stated.
- Asynchronous-agent architecture is an *architecture*, not a method a team can adopt independently of the framework. A substrate note next to Copilot coding agent / Devin-style background agents is the right treatment. Fails criterion 1.

### 3.8 Goose — CARRY-FORWARD

**Disposition: remain watchlist. No methodology profile. Update the URL.**

- **URL changed:** `block/goose` → **`aaif-goose/goose`** (Apache-2.0, ~52.6K stars, ~6.0K forks, last push 2026-08-08). Up from ~49.9K in June. The org move away from Block is itself worth a line in the status note.
- Latest release v1.45.0 (2026-07-29); v1.44.0 (2026-07-23). Active, regular cadence.
- Extensible agent runtime with MCP/ACP support. Notably, Goose appears as a supported target in the `skills` CLI and on skills.sh — reinforcing that it is a *consumer* of portable methods rather than a producer of one. Fails criterion 1.

### 3.9 Cline — CARRY-FORWARD

**Disposition: remain watchlist. Product, not methodology.**

- `cline/cline` (Apache-2.0, ~65.9K stars, ~7.1K forks, last push 2026-08-08). Up from ~63.6K in June.
- Latest: `desktop-v0.0.10` (2026-08-07) and `v4.1.6` (2026-08-06) — note the dual release train; a desktop app is now shipping alongside the core.
- Self-describes as "Autonomous coding agent as an SDK, IDE extension, or CLI assistant" — three product surfaces, no distinct portable method. Cline has its own skills documentation (`docs.cline.bot/features/skills`) and appears in the skills compatibility matrix supporting basic skills, `allowed-tools`, and hooks — again a consumer of the standard. Fails criterion 1.

---

## 4. Per-page change ledger

Legend for "required edit": **CRITICAL** = factually wrong today; **UPDATE** = stale figure; **REFRAME** = wording no longer defensible; **ADD** = new material.

### 4.1 `README.md`

| Old claim | Verified current claim (2026-08-08) | Source | Required edit |
|---|---|---|---|
| GSD linked to `gsd-build/get-shit-done`, "~64K" stars | Repo archived; active home is `open-gsd/gsd-core`, ~7.9K stars | GitHub API both repos | **CRITICAL** — relink and re-figure with a migration footnote |
| Spec Kit "~114K" | 125,881 | GitHub API | UPDATE → ~126K |
| OpenSpec "~56K", "27+ tool support" | 64,284; v1.8.0 added 3 more agent targets, so 27+ understates | GitHub API; v1.8.0 notes | UPDATE → ~64K; soften tool count or restate as "30+" only if a current count is verified |
| Squad "~2.8K" | 3,072 | GitHub API | UPDATE → ~3.1K |
| BMAD "~49K", "12+ personas and 34+ workflows" | 51,654; module set changed (bmad-loop added, bmad-automator deprecated, bmad-investigate retired) | GitHub API; v6.10.0 notes | UPDATE stars; **verify** persona/workflow counts before reuse — not re-verified this pass |
| Superpowers "~234K" | 269,251 | GitHub API | UPDATE → ~269K |
| HVE "~1.2K", "49 agents" | 1,328; repo now contains 70 `*.agent.md`, 80 `*.instructions.md`, 67 `*.prompt.md`, 58 `SKILL.md` | GitHub API; git tree | UPDATE stars; **REFRAME** — repo-level inventory ≠ released capability (latest release is still v3.2.2) |
| Deep-Dive tables list 10 Tier 1 pages | Unchanged | — | **ADD** Skills ecosystem row, explicitly outside the Tier 1 count |

### 4.2 `overview.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| "matured dramatically by June 2026" | Observation date is now 2026-08-08 | — | UPDATE framing |
| "Superpowers is the largest by community with roughly 234K stars" | 269,251; but `mattpocock/skills` at 209,856 and `anthropics/skills` at 167,036 are now adjacent | GitHub API | UPDATE figure; **REFRAME** — "largest" needs a stated comparison set (Tier 1 methodologies only) |
| Star-history chart includes `gsd-build/get-shit-done` | Archived; series will flatline | GitHub API | **CRITICAL** — swap to `open-gsd/gsd-core` |
| GSD row: "v1.42.3", "~64K stars", "Established" | GSD Core v1.10.0 (2026-08-08), ~7.9K stars, npm `@opengsd/gsd-core` | Releases API; npm registry | **CRITICAL** — rewrite row |
| BMAD "v6.8.0" | v6.10.0 (2026-07-03) | Releases API | UPDATE |
| Spec Kit "v0.11.3, still pre-1.0" | v0.16.1 (2026-08-07); still pre-1.0 | Releases API | UPDATE version; keep pre-1.0 caveat |
| OpenSpec "v1.4.1" | v1.8.0 (2026-08-05); prerelease channel exists (v1.6.0-beta.1) | Releases API | UPDATE |
| Squad "v0.10.0" | v0.11.0 (2026-06-30) | Releases API | UPDATE |
| Superpowers "v6.0.3", scratch state under `.superpowers/sdd/` | v6.2.0 (2026-07-24); workspace is now **plan-scoped**: `.superpowers/sdd/<plan-basename>/`, deleted after final clean review | Releases API; v6.2.0 notes | **CRITICAL** — path claim is now wrong |
| Ralph: "ralph-orchestrator active at v2.9.3" | v2.10.1 (2026-06-23); ~3,095 stars; **no push since 2026-07-25** | Releases API | UPDATE; soften "active" — six-week gap |
| HVE "v3.2.2, active repo" | v3.2.2 still latest **stable** (2026-03-23); prereleases exist up to `hve-core-v3.3.101` (2026-04-25); repo pushed 2026-08-08 | Releases API | UPDATE — separate stable / prerelease / repo activity |
| OpenSpec "broadest in comparison" (27+) | Supported-tool counts now moving across projects; not re-verified head-to-head | — | **REFRAME** — mutable superlative, drop or bound it |
| Context Engineering: rules files, 8-layer model | Skills spec now exists as a packaging layer above rules files | agentskills.io | **ADD** — skills as packaging/delivery layer |
| §8 "Projects to Consider Next": OpenHands, Goose URLs | `OpenHands/OpenHands`; `aaif-goose/goose` | GitHub API redirects | UPDATE URLs and figures |
| §8 framed against "June 2026 landscape" | — | — | UPDATE date framing |
| Complexity spectrum: 9 boxes, GSD "Claude Code + ports" | GSD Core installer covers Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf | gsd-core README | UPDATE GSD footer text; keep accepted spectrum order |
| — | — | — | **ADD** compact Skills ecosystem section |

### 4.3 `techniques/gsd.md` — highest priority

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| Source `gsd-build/get-shit-done` | **Archived** 2026-08-08; README: "GSD Has Moved" → `open-gsd/gsd-core` | GitHub API; raw README | **CRITICAL** |
| Author/Org "TÂCHES / gsd-build" | Now `open-gsd` org; homepage `opengsd.net` | gsd-core repo | **CRITICAL** |
| Current Version v1.42.3 (May 16, 2026) | **v1.10.0** (2026-08-08) under new versioning; npm `@opengsd/gsd-core` latest 1.10.0, `next` 1.7.0-rc.6 | Releases API; npm | **CRITICAL** — note the version-number reset or readers will think it regressed |
| "~64,400 stars · 5,500+ forks · active development" | Old repo 64,735/5,472 frozen (last commit 2026-05-31); new repo 7,916/551, pushed 2026-08-08, 144 open issues | GitHub API | **CRITICAL** + migration footnote |
| Install `npx get-shit-done-cc` | `npx @opengsd/gsd-core@latest`; old npm package last modified 2026-05-23 | gsd-core README; npm | **CRITICAL** |
| Copilot "❌ Not natively supported"; Windsurf "❌"; Cursor "⚠️ Community" | gsd-core README lists Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf "and more" via installer | gsd-core README | **CRITICAL** — compatibility table is inverted for Copilot/Windsurf/Cursor. Verify each before asserting depth; README lists installer targets, which is documented support, **not proven parity** |
| 6-step workflow (new → discuss → plan → execute → verify → complete) | GSD Core documents a **five-step** loop: Discuss → Plan → Execute → Verify → Ship; entry commands `/gsd-new-project`, `/gsd-onboard` | gsd-core README | **CRITICAL** — workflow shape changed |
| Community ports: gsd-for-cursor, gsd-pro | Not re-verified against the migration; relevance unclear now that Cursor is an official installer target | — | **Not verified** — flag, do not silently retain |
| "Recent releases strengthened Codex CLI support..." (v1.42.x era) | Superseded by the migration | — | REFRAME |

Also: gsd-core now has multilingual READMEs (pt-BR, zh-CN, ja-JP, ko-KR), a Discord, and CI test badges — a maturity signal worth one line.

### 4.4 `techniques/superpowers.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v6.0.3 | v6.2.0 (2026-07-24) | Releases API | UPDATE |
| ~234K stars / ~20.8K forks | 269,251 / 24,046 | GitHub API | UPDATE |
| SDD scratch at `.superpowers/sdd/` | Plan-scoped `.superpowers/sdd/<plan-basename>/`; `review-package` now takes the plan file as first arg; ledger names its plan on line 1; workspace deleted after final clean review | v6.2.0 notes | **CRITICAL** |
| — | v6.2.0 review-fix loop now resumes the implementer rather than restarting | v6.2.0 notes | ADD |
| — | Release notes cite 25/25 baseline and GREEN eval runs documented in `docs/specs/` and `docs/plans/` | v6.2.0 notes | ADD — rare, genuinely attributable evidence; cite as vendor-reported |
| Ecosystem/format claims | Superpowers skills sit on the same SKILL.md primitive now formalized at agentskills.io | agentskills.io | **ADD** comparison with mattpocock/skills (see §2.6) |

### 4.5 `techniques/context-engineering.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| Rules-file formats are fragmented, no standardization emerged | Still true for rules files; **false for skills packaging** — agentskills.io publishes a formal spec, Apache-2.0, vendor-neutral org, ~24.0K stars, with a client-implementor track | agentskills.io; agentskills/agentskills | **CRITICAL REFRAME** |
| 8-layer model via `copilot-instructions.md`, `.cursorrules`, `CLAUDE.md`, `AGENTS.md` | Still accurate; add skills as a layer above | — | ADD |
| — | `.agents/skills/` emerging as shared install path (skills CLI universal target; OpenSpec v1.8.0 `agents` target) | skills README; OpenSpec v1.8.0 | ADD |
| — | Progressive disclosure (discovery → activation → execution) is the documented context-efficiency mechanism | agentskills.io | ADD |
| — | Feature support is uneven: basic skills 18/18, `allowed-tools` 16/18, hooks 4/18, `context: fork` 1/18 | skills README compatibility matrix | ADD — **do not declare a universal standard**; state format convergence with runtime divergence |

### 4.6 `techniques/spec-kit.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v0.11.3 | v0.16.1 (2026-08-07); five releases since 2026-07-31 | Releases API | UPDATE |
| ~114K stars | 125,881 / 11,243 forks | GitHub API | UPDATE |
| Install via `uv tool install` | Confirmed: `uv tool install specify-cli --from git+...@v0.16.1` | v0.16.1 notes | No change |
| Extensions: Multi-Model Review, Token Economy | v0.16.1 is a hardening release (non-UTF-8 catalog, malformed YAML bundle manifests, escaping in `specify init`, bounded catalog fetch) — integration/extension catalog is real and being defensively hardened | v0.16.1 notes | UPDATE — cadence and hardening focus |
| Experimental / pre-1.0 | Still pre-1.0 | Releases API | Keep caveat |
| Skills as first-class distribution? | **No evidence found.** Spec Kit's ecosystem is extensions/presets/bundles, not SKILL.md | v0.16.1 notes | **Not verified — answer is no as of this pass** |

### 4.7 `techniques/openspec.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v1.4.1 | v1.8.0 (2026-08-05); v1.7.0, v1.6.0, and prerelease v1.6.0-beta.1 in between | Releases API | UPDATE + note prerelease channel exists |
| ~56K stars | 64,284 / 4,430 forks | GitHub API | UPDATE |
| 27+ supported tools | v1.8.0 adds vendor-neutral `agents`, MiniMax Code, Rovo Dev CLI → at least 30; exact current count not verified | v1.8.0 notes | UPDATE cautiously; **do not restate "broadest"** without same-day comparison |
| Workspace claims | v1.8.0 does not resolve the multi-repo/team-workspace question | v1.8.0 notes | **Preserve the accepted support-breadth vs runtime-parity caveat** |
| — | v1.8.0: 34 merged PRs from 15 contributors; GitHub Copilot cloud-agent file generation is **opt-in, defaults to No**; `retire_capabilities: true` on archive | v1.8.0 notes | ADD |
| — | Vendor-neutral `agents` target writes to `.agents/skills/` — OpenSpec now participates in the skills convention | v1.8.0 notes | ADD — direct link to the new ecosystem page |

### 4.8 `techniques/bmad.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v6.8.0 | v6.10.0 (2026-07-03); v6.9.0 (2026-06-22) | Releases API | UPDATE |
| ~49K stars | 51,654 / 5,913 forks | GitHub API | UPDATE |
| License: proprietary trademark caveat | GitHub still reports `NOASSERTION` | GitHub API | Keep caveat |
| Module list incl. `bmad-automator` | **`bmad-automator` deprecated**, replaced by **`bmad-loop`** (installable module, driven by new `bmad-dev-auto` skill: single-iteration unattended worker on a spec-frontmatter state machine); **`bmad-investigate` retired** | v6.10.0 notes | **CRITICAL** — breaking change |
| — | party-mode anti-consensus room; sharper code-review/edge-case-hunter severity triage | v6.10.0 notes | ADD |
| "12+ personas, 34+ workflows" | Not re-verified; module churn makes these unsafe to carry forward | — | **Not verified** — re-count or soften |
| Web Bundles (Gemini Gems, ChatGPT Custom GPTs) | Not contradicted; `web-bundles-v1.0.0` tag exists | Releases API | Keep, retain planning-bundle framing per accepted decision |
| — | `bmad-loop` is unattended dev-loop orchestration — converges toward Ralph's territory from the structured end | v6.10.0 notes | ADD — good cross-reference for ralph.md |

### 4.9 `techniques/squad.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v0.10.0 | v0.11.0 (2026-06-30) | Releases API | UPDATE |
| ~2.8K stars / ~428 forks | 3,072 / 475; 120 open issues; pushed 2026-08-08 | GitHub API | UPDATE |
| v0.10.0 feature set (state backends, governed memory, import/export, RAI reviewer, MCP frontmatter) | Still valid as history; v0.11.0 adds `squad preset install <source>` from GitHub URLs/local paths, cross-squad discovery, **`cast` terminology replacing `hire`** (old workflows still work), Copilot App sub-sessions, memory tools via `squad_state`, slimmer satellite skills | v0.11.0 notes | UPDATE + ADD |
| — | Toolchain: `@github/copilot-sdk` 1.0.4, TypeScript 6, Vitest 4, Ink 7, OpenTelemetry 2.x; 104 merged PRs from 8 authors; Windows-hardening pass | v0.11.0 notes | ADD |
| Copilot-centric, no community ports | Unchanged; still Copilot/GitHub-centric | — | Keep lock-in caveat |
| Pre-1.0 | Still pre-1.0 | — | Keep |
| — | **Note:** last release 2026-06-30 but repo pushed 2026-08-08 — unreleased activity, do not present as shipped | GitHub API | Framing guard |

### 4.10 `techniques/ralph.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| ralph-orchestrator v2.9.3 | v2.10.1 (2026-06-23); v2.10.0 (2026-06-22) | Releases API | UPDATE |
| ralph-orchestrator ~2.95K stars, active | 3,095 / 286 forks; **last push 2026-07-25** — ~2 weeks before observation, no release in ~7 weeks | GitHub API | UPDATE; soften "active" |
| how-to-ralph-wiggum ~1.7K stars | 1,734 / 145; **last push 2026-01-11** — static guide, no license metadata | GitHub API | UPDATE; keep canonical-method vs active-implementation split |
| "$297 API costs, 6+ repos overnight" (YC teams) | Anecdotal, not re-verified this pass | — | **Mark explicitly as anecdotal / attributed** |
| — | BMAD `bmad-loop` (v6.10.0) is a structured competitor for unattended dev loops | v6.10.0 notes | ADD comparison |
| Safety guidance | No new primary safety guidance found; skills ecosystem's lack of signing/pinning is a related risk | — | Keep existing; optionally cross-reference |

### 4.11 `techniques/hve.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| v3.2.2 (Mar 2026) | Still latest **stable** (2026-03-23) — ~4.5 months without a stable release | Releases API | UPDATE framing, keep version |
| — | Prereleases exist: `hve-core-v3.3.101` (2026-04-25), v3.3.41, v3.3.27, v3.3.10 — all marked prerelease | Releases API | **ADD** — separate stable from prerelease channel |
| ~1.2K stars | 1,328 / 251 forks; pushed 2026-08-08 | GitHub API | UPDATE |
| "49 agents, 102 instructions, 63 prompts, 11 skills"; "10 domain-specific collections" | Repo tree on `main`: **70** `*.agent.md`, **80** `*.instructions.md`, **67** `*.prompt.md`, **58** `SKILL.md` | Git tree API (untruncated) | **CRITICAL** — every count is wrong. **REFRAME:** these are repo-level file counts on `main`, not released-package contents. Instruction count went *down* (102 → 80) while skills went sharply *up* (11 → 58) |
| Copilot surfaces, enterprise examples, Learn hub | Not re-verified this pass | — | **Not verified** — leave unchanged or re-verify before editing |

The 11 → 58 skills jump is the notable HVE story: Microsoft's enterprise methodology is repackaging heavily onto the skills primitive. That connects HVE to the new ecosystem page.

### 4.12 `techniques/choosing-your-approach.md`

| Old claim | Verified current claim | Source | Required edit |
|---|---|---|---|
| GSD tool-lock-in framing | GSD Core installer spans nine-plus runtimes | gsd-core README | UPDATE |
| Stale versions/metrics throughout | See rows above | — | UPDATE |
| — | New decision axis: **skills library vs skills methodology** — mattpocock/skills (adapt freely, no enforcement) vs Superpowers (mandatory enforcement) | §2.6 | **ADD** |
| — | New decision axis: **managed plugin vs vendored copy** distribution | mattpocock/skills README | **ADD** |
| — | Skills are additive — adoptable alongside any Tier 1 methodology, since installs are per-agent-path | skills README | ADD to combinations |
| — | Do not put ecosystem profiles in methodology score tables (Neo's instruction) | brief §2 | Structural guard |

### 4.13 `mkdocs.yml`

Add `techniques/skills-ecosystem.md` to nav with a label consistent with README and overview. Keep it visually separate from the five methodology categories so it does not read as a sixth category or an eleventh technique.

---

## 5. Source table

All observations made 2026-08-08 unless stated.

| # | URL | Source date / release tag | Exact claim supported |
|---|---|---|---|
| 1 | `https://github.com/mattpocock/skills` | pushed 2026-08-07; created 2026-02-03 | 209,856 stars; 18,134 forks; MIT; not archived; desc "Skills for Real Engineers" |
| 2 | `https://github.com/mattpocock/skills/releases` | v1.2.3, 2026-08-06 | Latest stable v1.2.3; v1.2.2, v1.2.0 (2026-08-05), v1.1.0 (2026-07-08); no prerelease channel observed |
| 3 | `https://raw.githubusercontent.com/mattpocock/skills/main/README.md` | fetched 2026-08-08 | Dual install (Claude plugin vs `npx skills add`); "two ways in, two philosophies"; anti-process-ownership position naming GSD/BMAD/Spec-Kit; `/setup-matt-pocock-skills` required; ~60,000 newsletter subscribers (self-reported); Codex plugin on roadmap |
| 4 | `mattpocock/skills` git tree, `main` | fetched 2026-08-08, untruncated | 35 `SKILL.md` files across engineering(18)/productivity(7)/misc(4)/in-progress(6) |
| 5 | `mattpocock/skills/.claude-plugin/plugin.json` | v1.2.3 | Plugin name `mattpocock-skills`; MIT; author Matt Pocock / aihero.dev |
| 6 | `mattpocock/skills/CHANGELOG.md` | v1.2.3 | `diagnosing-bugs` now redacts secrets (PR #779) |
| 7 | `mattpocock/skills` contributors API | 2026-08-08 | 3 listed non-anonymous contributors |
| 8 | `https://skills.sh/mattpocock/skills` | 2026-08-08 | 51 skills; 14.4M total installs; `grill-me` 799.2K, `grill-with-docs` 679.9K, `improve-codebase-architecture` 654.9K, `tdd` 633.3K |
| 9 | `https://agentskills.io/home` | 2026-08-08 | Agent Skills = "lightweight, open format"; SKILL.md required; progressive disclosure (discovery/activation/execution); "cross-product reuse"; official Discord |
| 10 | `https://agentskills.io/specification` | 2026-08-08 | Frontmatter: `name` (≤64ch, lowercase alnum + hyphens), `description` (≤1024ch) required; `license`, `compatibility` (≤500ch), `metadata`, `allowed-tools` (Experimental) optional; `scripts/`, `references/`, `assets/` optional dirs |
| 11 | `https://github.com/agentskills/agentskills` | pushed 2026-08-04; created 2025-12-16 | 24,029 stars; 1,742 forks; Apache-2.0; 51 open issues; vendor-neutral org |
| 12 | `https://github.com/anthropics/skills` | pushed 2026-08-07; created 2025-09-22 | 167,036 stars; 19,911 forks; no top-level SPDX license reported |
| 13 | `anthropics/skills` README | 2026-08-08 | Defers to agentskills.io for the standard; many skills Apache-2.0 but docx/pdf/pptx/xlsx are source-available not open source; "demonstration and educational purposes only"; `./spec` and `./template` dirs; Claude Code plugin marketplace install |
| 14 | `https://github.com/vercel-labs/skills` | pushed 2026-08-07; created 2026-01-14 | 28,356 stars; 2,405 forks; MIT; ~1000 open issues; homepage skills.sh |
| 15 | `vercel-labs/skills` README | 2026-08-08 | ~70 agent target rows; `.agents/skills/` universal path; commands add/use/list/find/remove/update/init; GitHub/GitLab/git/local/private sources; credential handling ("does not execute `gh auth token`"); telemetry opt-out via `DISABLE_TELEMETRY`/`DO_NOT_TRACK`; compatibility matrix (basic 18/18, `allowed-tools` 16/18, hooks 4/18, `context: fork` 1/18) |
| 16 | `https://registry.npmjs.org/skills` | modified 2026-08-05 | npm `skills` latest 1.5.22; `snapshot` 1.5.12-snapshot.2; MIT; repo vercel-labs/skills |
| 17 | `https://skills.sh/audits` | 2026-08-08 | Aggregates Gen Agent Trust Hub, Socket, Snyk; many "Pending"; `find-skills` and `setup-matt-pocock-skills` = Med Risk (Snyk) |
| 18 | `https://skills.sh/docs/faq` | 2026-08-08 | Leaderboard from anonymous CLI telemetry; skills listed automatically on install; Packs are unlisted collections, Vercel sign-in to create; install of a pack needs no sign-in |
| 19 | `https://github.com/github/awesome-copilot` | pushed 2026-08-07 | 37,585 stars; 4,732 forks; MIT |
| 20 | `github/awesome-copilot` README | 2026-08-08 | "Community-created collection"; marketplace pre-registered in Copilot CLI/VS Code; `copilot plugin install <name>@awesome-copilot`; Agents/Instructions/Skills/Plugins/Cookbook; `llms.txt`; third-party sourcing caution |
| 21 | `https://github.com/numman-ali/openskills` | **pushed 2026-01-18** | 10,666 stars; 669 forks; license metadata NOASSERTION (README badge claims Apache-2.0 — inconsistent); ~7 months stale |
| 22 | `https://github.com/gsd-build/get-shit-done` | **archived: true**; last commit 2026-05-31 | 64,735 stars; 5,472 forks; MIT; 0 open issues; README states "GSD Has Moved" → open-gsd/gsd-core |
| 23 | `https://github.com/open-gsd/gsd-core` | pushed 2026-08-08; created 2026-05-22 | 7,916 stars; 551 forks; MIT; 144 open issues; homepage opengsd.net |
| 24 | `open-gsd/gsd-core` releases | v1.10.0, 2026-08-08 | v1.10.0 latest; v1.9.1, v1.9.0 (2026-07-31), v1.8.0 (2026-07-22), v1.7.0 (2026-07-15) |
| 25 | `open-gsd/gsd-core` README | 2026-08-08 | Five-step loop Discuss→Plan→Execute→Verify→Ship; `npx @opengsd/gsd-core@latest`; installer targets Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf "and more"; `/gsd-new-project`, `/gsd-onboard`; multilingual READMEs; Discord |
| 26 | `https://registry.npmjs.org/@opengsd/gsd-core` | modified 2026-08-08 | latest 1.10.0; `next` 1.7.0-rc.6; MIT |
| 27 | `https://registry.npmjs.org/get-shit-done-cc` | modified 2026-05-23 | Old package frozen at latest 1.42.3, next 1.43.0-rc2 |
| 28 | `https://github.com/obra/superpowers` | pushed 2026-08-08 | 269,251 stars; 24,046 forks; MIT |
| 29 | `obra/superpowers` release v6.2.0 | 2026-07-24 | Plan-scoped `.superpowers/sdd/<plan-basename>/`; `review-package` takes plan file as first arg; ledger names plan on line 1; workspace deleted after clean final review; review-fix loop resumes implementer; 25/25 baseline and GREEN eval runs cited |
| 30 | `https://github.com/github/spec-kit` | pushed 2026-08-07 | 125,881 stars; 11,243 forks; MIT |
| 31 | `github/spec-kit` release v0.16.1 | 2026-08-07 | Install via `uv tool install specify-cli --from git+...@v0.16.1`; hardening fixes (non-UTF-8 catalog, malformed YAML bundle manifest, `specify init` escaping, bounded catalog fetch); v0.16.0 2026-08-05, v0.15.2 2026-08-03, v0.15.1 2026-07-31 |
| 32 | `https://github.com/Fission-AI/OpenSpec` | pushed 2026-08-07 | 64,284 stars; 4,430 forks; MIT |
| 33 | `Fission-AI/OpenSpec` release v1.8.0 | 2026-08-05 | 34 PRs from 15 contributors; new targets `agents` (writes to `.agents/skills/`), MiniMax Code, Rovo Dev CLI; Copilot cloud-agent generation opt-in defaulting to No; `retire_capabilities: true`; prerelease v1.6.0-beta.1 exists (2026-07-08) |
| 34 | `https://github.com/bmad-code-org/BMAD-METHOD` | pushed 2026-08-08 | 51,654 stars; 5,913 forks; license NOASSERTION |
| 35 | `BMAD-METHOD` release v6.10.0 | 2026-07-03 | `bmad-loop` installable module + `bmad-dev-auto` skill; `bmad-automator` deprecated (breaking); `bmad-investigate` retired; party-mode anti-consensus room; code-review/edge-case-hunter severity triage; v6.9.0 2026-06-22 |
| 36 | `https://github.com/bradygaster/squad` | pushed 2026-08-08 | 3,072 stars; 475 forks; MIT; 120 open issues |
| 37 | `bradygaster/squad` release v0.11.0 | 2026-06-30 | `squad preset install <source>`; cross-squad discovery; `cast` replaces `hire` (hire still works); Copilot App sub-sessions; memory tools via `squad_state`; `@github/copilot-sdk` 1.0.4, TypeScript 6, Vitest 4, Ink 7, OpenTelemetry 2.x; 104 PRs from 8 authors |
| 38 | `https://github.com/microsoft/hve-core` | pushed 2026-08-08 | 1,328 stars; 251 forks; MIT |
| 39 | `microsoft/hve-core` releases | stable hve-core-v3.2.2 2026-03-23 | Latest stable v3.2.2; prereleases v3.3.101 (2026-04-25), v3.3.41, v3.3.27, v3.3.10 |
| 40 | `microsoft/hve-core` git tree, `main` | 2026-08-08, untruncated | 70 `*.agent.md`; 80 `*.instructions.md`; 67 `*.prompt.md`; 58 `SKILL.md` |
| 41 | `https://github.com/mikeyobrien/ralph-orchestrator` | pushed 2026-07-25 | 3,095 stars; 286 forks; MIT; latest v2.10.1 (2026-06-23), v2.10.0 (2026-06-22) |
| 42 | `https://github.com/ghuntley/how-to-ralph-wiggum` | pushed 2026-01-11 | 1,734 stars; 145 forks; no license metadata; static |
| 43 | `https://github.com/OpenHands/OpenHands` | pushed 2026-08-08 | 83,482 stars; 10,788 forks; MIT; v1.12.0 and v1.11.0 both 2026-08-07; redirected from All-Hands-AI/OpenHands |
| 44 | `https://github.com/langchain-ai/open-swe` | pushed 2026-08-08 | 10,516 stars; 1,221 forks; MIT; **no releases and no tags** |
| 45 | `https://github.com/aaif-goose/goose` | pushed 2026-08-08 | 52,561 stars; 5,958 forks; Apache-2.0; v1.45.0 2026-07-29, v1.44.0 2026-07-23; redirected from block/goose |
| 46 | `https://github.com/cline/cline` | pushed 2026-08-08 | 65,884 stars; 7,074 forks; Apache-2.0; desktop-v0.0.10 2026-08-07, v4.1.6 2026-08-06 |

---

## 6. Recommendations under Neo's criteria

### 6.1 Include on `techniques/skills-ecosystem.md`

1. **`mattpocock/skills`** — lead profile. Meets the ecosystem bar decisively: shapes authoring (skill-writing skills), packaging (dual distribution), and adoption (14.4M installs). Fails the methodology bar by its own explicit design intent.
2. **Agent Skills specification (agentskills.io / `agentskills/agentskills`)** — the format anchor. Everything else on the page depends on it. Present as spec + governance, separate from Anthropic's reference implementation.
3. **`anthropics/skills`** — reference implementation and largest first-party skill collection. Must carry the mixed-license and "demonstration purposes only" caveats.
4. **`vercel-labs/skills` / skills.sh** — the installer, registry, discovery, and ranking layer. Must carry the uncurated-by-default, telemetry-on-by-default, partial-audit-coverage, and single-vendor-control caveats.
5. **`github/awesome-copilot`** — the curated-channel contrast case, and the concrete example of official distribution with community content.

### 6.2 Exclude

- **OpenSkills (`numman-ali/openskills`)** — fails criterion 4 (current maintenance); stale since 2026-01-18, superseded in function, ambiguous name, inconsistent license metadata. At most one watchlist line.
- **OpenHands, Open SWE, Goose, Cline** — all four remain products/platforms/runtimes. None exposes a portable method independent of its own runtime. Keep in "Projects to Consider Next" with corrected URLs and figures. Open SWE additionally has no release history.
- **No Tier 1 promotions this pass.** The technique count stays at ten. The Skills ecosystem page is supporting market context.

### 6.3 Cross-cutting recommendations

- **Demote star counts** to a secondary signal. Counts above 100K no longer discriminate between projects of very different production maturity. Lead with release cadence, contributor counts, and install telemetry where published.
- **Add a standing "distribution and trust" note** to the ecosystem page: no signing, no attestation, no lockfile pinning anywhere in the examined surfaces; `allowed-tools` is Experimental; skills bundle executable code. This is the most decision-relevant weakness in the segment.
- **Adopt a consistent support vocabulary** and apply it to the corrected GSD table: *official support* / *official-but-limited* / *community adaptation* / *readable-artifact compatibility* / *inferred*. The GSD installer target list is documented support, not proven parity.

---

## 7. Material status changes — watchlist (not researched deeply)

- **Roo Code** — carried forward from June as needing rebrand/archive follow-up. **Still unresolved; not re-verified this pass.**
- **OpenCode** — noted in June under `anomalyco/opencode` at ~176.7K stars. Not re-verified. Appears as a supported target in the skills CLI and gsd-core installer.
- **Aider, Continue, Kilo Code, SWE-agent, AutoGPT, Pythagora/GPT Pilot** — not re-verified this pass, per the bounded scope.
- Several of these (OpenCode, Continue, Cline, Kilo, Roo) now appear as skills-CLI targets, which strengthens the "substrate that consumes portable methods" framing rather than arguing for promotion.

---

## 8. Unresolved and not-verifiable items

| # | Item | Status |
|---|---|---|
| 1 | `mattpocock/skills` skill count: 35 in repo vs 51 on skills.sh | **Not verified.** Do not publish a single number without naming the surface. |
| 2 | GSD Core's real per-runtime feature depth (Copilot, Windsurf, Cursor) | **Not verified.** README lists installer targets only. Do not claim parity. |
| 3 | Whether GSD's community ports (gsd-for-cursor, gsd-pro) tracked the migration | **Not verified.** Flag rather than silently retain. |
| 4 | BMAD "12+ personas, 34+ workflows" after v6.10.0 module churn | **Not verified.** Re-count or soften. |
| 5 | OpenSpec's exact current supported-tool count | **Not verified.** At least 30 after v1.8.0; avoid a precise figure and avoid "broadest." |
| 6 | HVE released-package contents vs repo `main` file counts | **Partially verified.** Repo counts are exact; released v3.2.2 VSIX contents were not inspected. Attribute counts to the repo tree. |
| 7 | HVE `activeRepoStatus: false` custom property (flagged in June) | **Not re-verified.** Do not interpret publicly. |
| 8 | Ralph "$297 / 6+ repos overnight" YC anecdote | **Not re-verified.** Mark as anecdotal and attributed. |
| 9 | Superpowers eval claims (25/25 baseline, GREEN runs) | **Vendor-reported**, from release notes. Attribute; do not present as independent. |
| 10 | `numman-ali/openskills` license: NOASSERTION vs Apache-2.0 badge | **Inconsistent, unresolved.** Moot given exclusion. |
| 11 | skills.sh audit methodology and refresh cadence | **Not verified.** Verdicts observed; the process behind them is undocumented on the public page. |
| 12 | Real-world production adoption behind large star counts | **Not verifiable** from available sources. Install counts are the best proxy and exist only for skills.sh-tracked skills. |
| 13 | Whether GitHub Copilot skills follow the agentskills.io spec exactly | **Not verified.** The skills CLI lists Copilot as supporting basic skills and `allowed-tools`; first-party GitHub spec conformance docs were not located. |
