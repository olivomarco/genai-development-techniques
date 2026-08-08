# GSD Core capability follow-up — evidence for blocking finding B4

**Author:** Trinity (Researcher / Analyst)
**Date:** 2026-08-08
**Requested by:** Marco Olivo, via Oracle's rejection `.squad/research/review-2026-08-08.md` §B4
**Scope:** Narrow. Verify or disprove ten disputed current-capability claims in `techniques/gsd.md` (plus `overview.md` lines 27 and 122) against primary sources in `open-gsd/gsd-core`. No broader market research was performed.

---

## 1. Observation basis

| Item | Value |
|---|---|
| Repository | `https://github.com/open-gsd/gsd-core` |
| Observed | 2026-08-08 |
| `main` HEAD inspected | `b9f51836e644e71df07930ac36c12b8ea340f49d` (2026-08-08T16:05:17-04:00) |
| Stable release inspected | `v1.10.0` = commit `68a04ccf8ef74803bdb651e12c3b85b218bbccdf`, published 2026-08-08T05:07:19Z (GitHub Releases API) |
| Repo metadata | 7,917 stars · 551 forks · MIT · `archived: false` · pushed 2026-08-08T20:05:20Z (GitHub API) |
| npm | `@opengsd/gsd-core` — `latest` 1.10.0, `next` 1.7.0-rc.6; tarball `fileCount` 879, `unpackedSize` 11,199,326 bytes; runtime deps: `@anthropic-ai/claude-agent-sdk ^0.2.84`, `ws ^8.21.0` |
| Predecessor | `gsd-build/get-shit-done` — archived; `main` README is a 12-line redirect stub. Pre-migration content read at tag `v1.42.3` |

**Main vs. v1.10.0.** For every document cited below, `git diff v1.10.0 HEAD` is empty except `docs/COMMANDS.md`, which gained three unrelated paragraphs (milestone-archive guards and `/gsd-progress` scoping). **No disposition in this report differs between `main` and stable v1.10.0.** Where a claim depends on a `docs/COMMANDS.md` line, the same text is present at the tag (verified by `git show v1.10.0:docs/COMMANDS.md`).

**Method note.** All file paths below are repo-relative and resolvable as `https://github.com/open-gsd/gsd-core/blob/v1.10.0/<path>`. Evidence is quoted verbatim from a local clone of `main` at the SHA above.

---

## 2. Dispositions at a glance

| # | Disputed claim (`techniques/gsd.md` line) | Disposition |
|---|---|---|
| 1a | Wave-based parallel execution (44, 55, 90) | **CURRENT VERIFIED** |
| 1b | "5+ agents simultaneously" (44, 55, 90) | **CHANGED/REMOVED** — documented default is `3` |
| 2 | "Leverages Claude Code's native sub-agent spawning"; Claude Code as primary integration (23, 55) | **CURRENT VERIFIED but materially incomplete** |
| 3 | XML prompt formatting (59) | **CURRENT VERIFIED** |
| 4 | Quick Mode (83) | **CURRENT VERIFIED** |
| 5 | Brownfield support (83) | **CURRENT VERIFIED** |
| 6 | Workstreams (83) | **CURRENT VERIFIED** |
| 7 | Multi-project workspaces (83) | **CURRENT VERIFIED** |
| 8 | "~50 Markdown files and a CLI helper" (88) | **CHANGED/REMOVED** — off by ~10x |
| 9 | iOS-to-Android / 90+ sessions / 23 plans (89) | **NOT VERIFIED** — no primary source in either repo |
| 10 | `overview.md:27` "waves for parallelism"; `:122` "+ waves" | **CURRENT VERIFIED** |

---

## 3. Item-by-item evidence

### 3.1 Wave-based parallel execution — **CURRENT VERIFIED**

The wave model is first-class, documented, and shipped.

- `README.md:34` — "3. **Execute** — run plans in parallel waves; each executor starts with a clean 200k-token context"
- `docs/COMMANDS.md:298` — "Execute all plans in a phase with wave-based parallelization, or run a specific wave." The command exposes `--wave N` to run a single wave.
- `gsd-core/workflows/execute-phase.md:9` — "Execute all plans in a phase using wave-based parallel execution. Orchestrator stays lean — delegates plan execution to subagents."
- `gsd-core/workflows/execute-phase.md:473` — "Execute each selected wave in sequence. Within a wave: parallel if `PARALLELIZATION=true`, sequential if `false`."
- `docs/adr/1143-claude-orchestration-capability.md:28` — "GSD's `execute-phase` is wave-based: plans carry a `wave` number, waves run sequentially, and plans *within* a wave run in parallel when their `files_modified` sets do not overlap."
- Configuration surface: `docs/CONFIGURATION.md:834-840` documents `parallelization.enabled` (default `true`), `.plan_level` (`true`), `.task_level` (`false`), `.skip_checkpoints`, `.max_concurrent_agents`, `.min_plans_for_parallel` (`2`). Shipped default template: `gsd-core/templates/config.json:40`.

**Safe wording:** "Wave-based parallel execution: plans carry a wave number, waves run sequentially, and non-file-overlapping plans within a wave run in parallel."

### 3.2 "5+ agents simultaneously" — **CHANGED/REMOVED**

No primary source in `open-gsd/gsd-core` states five or more simultaneous agents. The only documented concurrency ceiling is **3**.

- `docs/CONFIGURATION.md:839` — "| `parallelization.max_concurrent_agents` | number | `3` | Maximum simultaneous agents |"
- `gsd-core/templates/config.json:40` — `"max_concurrent_agents": 3,` (the value actually written into a new project)
- Repository-wide search for `5+ agent` / `five agents` / `5 agents` across `docs/`, `README*.md`, `commands/`, `agents/` returns **no** capability statement. The only near-hit is a *cost warning*, not a capability: `docs/explanation/multi-agent-orchestration.md:207` — "**Model cost amplification.** Running five agents in parallel at Opus tier costs more than running one."
- The nearest documented concrete fan-out is four, and it is planning-stage, not execution: `docs/explanation/multi-agent-orchestration.md:190-191` — "the four researchers in a `plan-phase` run simultaneously, not sequentially."
- The same `3` default is present in the archived predecessor at `gsd-build/get-shit-done@v1.42.3:docs/CONFIGURATION.md:523`, so **"5+" was never sourced from either repository's documentation** — it appears to be a downstream embellishment, not an archived-era fact.

**Assessment.** `max_concurrent_agents` is user-configurable, so a user *may* set it above 5; but "the wave-based orchestrator runs 5+ agents simultaneously" asserts product behaviour that the documented default (3) contradicts. Recommend replacing with "configurable concurrency, default 3 simultaneous agents."

### 3.3 Claude Code-native sub-agent spawning / primary integration depth — **CURRENT VERIFIED but materially incomplete**

Claude Code is genuinely the deepest and reference integration, but GSD Core no longer *depends* on Claude-native spawning, and the dependency framing is now wrong.

Evidence that Claude Code remains deepest:
- `README.md:126` (closing line) — "**Claude Code is powerful. GSD Core makes it reliable.**"
- Sole runtime dependency is `@anthropic-ai/claude-agent-sdk ^0.2.84` (`package.json`).
- `gsd-core/workflows/execute-phase.md:22` — "**Claude Code:** Uses `Agent(subagent_type=\"gsd-executor\", ...)` — blocks until complete, returns result".
- `docs/reference/host-integration-capability-matrix.md` §claude records the strongest dispatch profile: `dispatch.nested true`, `maxDepth 5`, `background true`, `subagentToolkit full`, and uniquely `dispatch.isolation harness-worktree` — "The Claude Code Agent tool accepts an `isolation=\"worktree\"` harness primitive."

Evidence the claim is incomplete / no longer a dependency:
- `gsd-core/workflows/execute-phase.md:20-32` is titled "**Subagent spawning is runtime-specific:**" and defines explicit non-Claude paths, including "**Other runtimes:** If `Agent`/`agent` tool is genuinely unavailable … use sequential inline execution as the fallback for executor parallelization only … Check for actual tool availability, not runtime name."
- `docs/reference/host-integration-capability-matrix.md` carries **20 host sections** (claude, codex, opencode, cursor, cline, hermes, antigravity, augment, qwen, codebuddy, copilot, kilo, windsurf, trae, kimi, kimi-code, zcode, pi, vscode) with per-host cited dispatch axes; `capabilities/` holds 44 capability descriptors.
- `docs/adr/1239-gsd-embeddable-orchestration-engine.md:280` — "**Positive.** Codex gains wave parallelism with **no `runtime===` branch** in the scheduler — isolation becomes a declared, negotiated, tested capability instead of a hardcoded harness assumption."
- Claude Code is not uniformly best: `docs/adr/1143-...:30` — "Backgrounded agents on Claude Code have no `Agent`/`Task` tool, so they cannot nest subagents (#853). The autonomous loop therefore falls back to **inline sequential execution** — and with it silently drops wave parallelism, the plan-checker, and the verifier — on the single runtime most GSD users run." ADR-1143 is still **`[Proposed]`**, unratified as of the 2026-07-17 audit note in its own header.
- Copilot specifically degrades: `gsd-core/workflows/execute-phase.md:23-26` — "**Copilot:** Subagent spawning does not reliably return completion signals. **Default to sequential inline execution**"; and `:157-159` — "If running under Copilot, force sequential inline execution regardless of the `parallelization` setting." Matrix §copilot: `dispatch.nested false`, `maxDepth 1`, `dispatch.isolation undocumented` → "fails closed to `none` (sequential)".

**Assessment.** Keep "Claude Code is the deepest integration," drop "leverages Claude Code's native sub-agent spawning" as the mechanism. This is also the direct answer to Oracle's non-blocking observation 8 on `gsd.md:23`: the ✅ Primary row is defensible, but the parenthetical should not imply the system is *built on* Claude-only primitives. **New, citable, and worth adding:** parallelism degrades to sequential inline execution on Copilot by default — a documented limitation, not an inference.

### 3.4 XML prompt formatting — **CURRENT VERIFIED**

- `docs/FEATURES.md:305` — "REQ-PLAN-03: System MUST structure plans as XML with `<task>` elements containing `name`, `files`, `action`, `verify`, and `done` fields", followed by a worked `<task type="auto">` example at `docs/FEATURES.md:322-333`.
- `docs/AGENTS.md:173` — "Uses XML structure with `<task>` elements"; `:217` — "Follows XML task instructions precisely".
- Shipped artifacts, not just docs: `<task`-bearing files include `agents/gsd-planner.md`, `agents/gsd-executor.md`, `agents/gsd-plan-checker.md`, `gsd-core/workflows/execute-plan.md`, `gsd-core/workflows/execute-phase.md`, `gsd-core/workflows/new-project.md`. Prompt-level XML blocks are pervasive (e.g. `<runtime_compatibility>` at `execute-phase.md:20`, `<parallel_execution>` at `:715-733`).
- Continuity: the archived README carried the same self-description — `gsd-build/get-shit-done@v1.42.3:README.md:61` — "Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management."

Nuance worth preserving: XML is used for **plan structure and prompt sectioning**, not as a wire format for everything. `docs/CLI-TOOLS.md:621-635` shows `gsd-tools` emitting a raw `<agent_skills>` XML block by default with an opt-in `--json` typed IR.

### 3.5 Quick Mode — **CURRENT VERIFIED**

- `docs/COMMANDS.md:846-873` documents `/gsd-quick` — "Execute ad-hoc task with GSD guarantees", flags `--full`, `--validate`, `--discuss`, `--research`, and subcommands `list` / `status <slug>` / `resume <slug>`.
- `docs/explanation/context-engineering.md:120` — "**Ceremony for simple tasks.** … GSD Core provides `/gsd-quick` and `/gsd-fast` for ad-hoc work that does not warrant a full phase."
- `docs/explanation/the-phase-loop.md:90` — "\"Fix the typo in the README\" is below the threshold where the loop adds value; use `/gsd-quick` instead."
- Shipped: `commands/gsd/quick.md` and `skills/gsd-quick/SKILL.md` are both present in the published npm tarball.
- `docs/INVENTORY.md:98` lists `/gsd-quick` in the authoritative command inventory.

Naming caveat: the current docs name the **command** `/gsd-quick`; "Quick Mode" as a proper noun is archived-era phrasing (`docs/RELEASE-NOTES-LEGACY.md:92` — "1.7.0 | 2026-01-19 | Quick Mode for small ad-hoc tasks without optional agents"). There is also a sibling `/gsd-fast` (`docs/COMMANDS.md:1459`), explicitly narrower — `:1467` "Not a replacement for `/gsd-quick`".

### 3.6 Brownfield support — **CURRENT VERIFIED**

- `README.md:54` — "`/gsd-onboard       # existing codebase`", plus a linked tutorial "Onboarding an existing codebase".
- `docs/COMMANDS.md:61-76` — "Guide an existing codebase through first-time GSD onboarding…"; example at `:74` is literally "`/gsd-onboard           # Guided brownfield onboarding`".
- `docs/adr/1990-existing-code-onboarding.md` documents the shipped Existing Code Onboarding Module (`src/onboard-projection.cts` → `gsd-core/bin/lib/onboard-projection.cjs`), with deterministic brownfield detection, a vendor/generated-directory exclusion list (`node_modules`, `dist`, `build`, `.next`, `.nuxt`, `.svelte-kit`, `coverage`, `vendor`, `.venv`, `venv`), and unit tests in `tests/onboard-command.test.cjs`. Issue #1990 CLOSED/COMPLETED 2026-07-07; PR #1994 merged.
- Supporting: `/gsd-map-codebase` (`docs/COMMANDS.md:1241`), `/gsd-ingest-docs` (`:825`), and `.planning/codebase/` + `.planning/onboarding/` artifact trees (`docs/ARCHITECTURE.md:693-694`).
- Shipped: `commands/gsd/onboard.md`, `skills/gsd-onboard/SKILL.md`.

This is the **strongest** of the disputed items — it has a dedicated ADR, a named module, and named regression tests.

### 3.7 Workstreams — **CURRENT VERIFIED**

- `docs/COMMANDS.md:1107-1136` — "`/gsd-workstreams` — Manage parallel workstreams for concurrent work on different milestone areas," with subcommands `list`, `create`, `status`, `switch`, `progress`, `complete`, `resume`. "**Produces:** Workstream directories under `.planning/`, state tracking per workstream."
- Architectural backing: `docs/adr/0004-worktree-workstream-seam-module.md:6` — "The Module owns `.planning` path resolution, active workstream pointer policy, workstream-name invariants, and lock semantics".
- Runtime surface: `GSD_WORKSTREAM` environment variable and `loadConfig(cwd, {workstream})` (`docs/CONTEXT-INDEX.json`); workstream-scoped path projection is a tested invariant (`docs/issueevidence/1192-adr-test-audit-2026-06-13.md:202`).
- Shipped: `commands/gsd/workstreams.md`, `skills/gsd-workstreams/SKILL.md`.
- Continuity with archived era: `gsd-build/get-shit-done@v1.42.3:README.md:203` already referenced "workstream config inheritance".

### 3.8 Multi-project workspaces — **CURRENT VERIFIED (with a wording correction)**

- `docs/COMMANDS.md:80-108` — "`/gsd-workspace` — Manage GSD workspaces — create, list, or remove isolated workspace environments with repo copies and independent `.planning/` directories." Flags include `--repos repo1,repo2`, `--strategy worktree|clone`, `--path`, `--branch`.
- Stated use case at `docs/COMMANDS.md:97-98` — "**Multi-repo:** work on a subset of repos with isolated GSD state" / "**Feature isolation:** `--repos .` creates a worktree of the current repo". Example at `:102`: `/gsd-workspace --new --name feature-b --repos hr-ui,ZeymoAPI`.
- **Produces:** `WORKSPACE.md`, `.planning/`, repo copies.
- Shipped: `commands/gsd/workspace.md`, `skills/gsd-workspace/SKILL.md`.

**Correction to our wording.** The primary source describes **multi-repo workspaces with isolated GSD state**, not "managing multiple projects simultaneously." The isolation is the point; concurrency is not claimed. Recommend: "Workspaces isolate multi-repo work behind independent `.planning/` state, via git worktrees or clones."

### 3.9 "Low dependency footprint. ~50 Markdown files and a CLI helper" — **CHANGED/REMOVED**

Off by roughly an order of magnitude. Measured directly from the published `@opengsd/gsd-core@1.10.0` tarball (`tar tzf`, 879 entries — matching the registry's `fileCount`):

| Measure | Value |
|---|---|
| Total files in published package | **879** |
| Markdown files | **486** |
| `.js` / `.cjs` / `.mjs` files | **337** |
| Unpacked size | **11,199,326 bytes (~11.2 MB)** |
| Top-level payload dirs | `gsd-core/` 524, `scripts/` 92, `skills/` 71, `commands/` 71, `hooks/` 63, `agents/` 34 |

Repo-tree corroboration on `main`: 1,421 `*.md` files total; 479 `*.md` and 317 JS/CJS files within the directories listed in `package.json`'s `files` array.

There is **not** a single CLI helper. `package.json` declares **four** binaries: `gsd-core` → `bin/install.js`, `gsd-tools` → `gsd-core/bin/gsd-tools.cjs`, `gsd_run` → `gsd-core/bin/gsd_run`, `gsd-mcp-server` → `bin/gsd-mcp-server.js`. `docs/CLI-TOOLS.md:15` states `gsd-tools.cjs` is itself backed by "20 domain modules under `gsd-core/bin/lib/`".

What *is* still defensible and is the better claim: the **runtime dependency tree is tiny** — exactly two production dependencies, `@anthropic-ai/claude-agent-sdk ^0.2.84` and `ws ^8.21.0` (12 devDependencies). Recommend replacing the file-count claim with the dependency-count fact, which is both accurate and more meaningful. Note this also resolves Oracle's internal-inconsistency point: the pros table at `gsd.md:44` already dropped the figure; `:88` should not reinstate it.

### 3.10 iOS-to-Android port / 90+ AI sessions / 23 plans — **NOT VERIFIED**

Searched and found nothing in any primary source:

- `open-gsd/gsd-core` @ `main`: no match for `iOS`, `Android`, `90+`, or `23 plans` across `docs/`, `README*.md`, `CHANGELOG.md` (567 KB), or `docs/RELEASE-NOTES-LEGACY.md`.
- `gsd-build/get-shit-done` @ `main`: README is a 12-line redirect stub only.
- `gsd-build/get-shit-done` @ tags `v1.42.3`, `v1.20.0`, `v1.10.0`, `v1.0.0`: no README match for `android`, `90+`, `23 plans`, `markdown file`, or `5+`.
- Open web search returned no distinct primary artifact; the closest surfaces are a third-party DEV Community write-up and `getshitdone.help`, neither of which carries these figures.

**Assessment.** This is an unattributed, undated, unlocatable anecdote. It should be deleted rather than hedged. The same anecdote is also cited at `techniques/choosing-your-approach.md:240` ("A GSD community report describes a production iOS-to-Android port in 3 days") — **this second instance is outside B4's enumerated lines and must be handled in the same pass**, or the site will retain an unsourced claim after B4 is closed.

### 3.11 `overview.md:27` "waves for parallelism" and `:122` "+ waves" — **CURRENT VERIFIED**

Both are supported verbatim by `README.md:34`, `docs/COMMANDS.md:298`, and `gsd-core/workflows/execute-phase.md:9`. No change required to either line on the merits. If the team chooses to add a concurrency figure anywhere, it must be `3` (default), not `5+`.

---

## 4. Recommended dispositions for the B4 lines

| `techniques/gsd.md` | Action |
|---|---|
| 44 — "Parallel execution (5+ agents via wave-based orchestrator)" | Keep wave-based parallel execution; **delete "5+ agents"** or restate as "default 3 concurrent agents, configurable" |
| 55 — "Lean Orchestrator … up to 5+ agents … leverages Claude Code's native sub-agent spawning" | Delete "5+"; replace the Claude-native mechanism clause with runtime-negotiated dispatch, noting Claude Code is deepest |
| 59 — XML Prompt Formatting | **Keep as-is**, cite `docs/FEATURES.md:305` |
| 83 — Quick Mode / Brownfield / Workstreams / Multi-Project Workspaces | **Keep all four**; rename "Quick Mode" → `/gsd-quick`; restate workspaces as multi-repo isolation |
| 88 — "~50 Markdown files and a CLI helper" | **Replace** with "two runtime dependencies"; the file-count figure is ~486 MD / 879 files |
| 89 — iOS-to-Android anecdote | **Delete.** Also delete/attribute the duplicate at `choosing-your-approach.md:240` |
| 90 — "wave-based orchestrator runs 5+ agents simultaneously" | Keep wave orchestration; delete "5+" |
| 23 — Claude Code "✅ Primary — built on native Claude Code features" | Soften "built on" → "deepest integration"; optionally note Copilot forces sequential inline execution |

**New limitation worth adding (fully sourced):** parallelism is not portable. Copilot defaults to sequential inline execution (`gsd-core/workflows/execute-phase.md:23-26, 157-159`), and backgrounded Claude Code agents lose wave parallelism entirely (`docs/adr/1143-...:30`). This is a stronger, better-evidenced version of the "runtime parity is not verified" line already on the page.

---

## 5. Residual unknowns

| # | Item | Status |
|---|---|---|
| 1 | Whether any user actually runs >3 concurrent agents in practice | Not verified — `max_concurrent_agents` is configurable with no documented upper bound; no benchmark or reported figure exists in-repo |
| 2 | Whether ADR-1143 (Claude Workflow-tool orchestration backend) has been ratified | **Still `[Proposed]`** at `main`. The capability is shipped and wired (#2285, #1143 both CLOSED/COMPLETED) but the ADR's own sign-off condition — a recorded real Workflow-tool run — remains unmet |
| 3 | Provenance of the "5+ agents" figure | Not found in either repository at any inspected tag. Origin is downstream of both primary sources |
| 4 | Community ports (`gsd-for-cursor`, `gsd-pro`) post-migration | Still not re-verified (carried over from `market-refresh-2026-08-08.md` §8 item 3). The current README's Community table lists only `rokicool/gsd-opencode` ("Original OpenCode port") and the Discord — neither previously-tracked port appears |
