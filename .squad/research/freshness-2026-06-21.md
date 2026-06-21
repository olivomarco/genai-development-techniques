# Freshness Research Pass — 2026-06-21

**Researcher:** Trinity  
**Requested by:** Marco Olivo  
**Scope:** Existing documented projects plus additional comparable projects to consider today.  
**Boundary:** Raw research notes only. Do not treat this as final comparison prose.

---

## Executive Findings

The current docs are directionally strong but several quantitative claims and version references are stale after roughly two months of rapid project movement.

Biggest updates:

- Spec Kit, Superpowers, GSD, OpenSpec, Squad, BMAD, and Ralph-orchestrator all shipped post-April releases.
- Star counts moved materially: Superpowers, Spec Kit, OpenSpec, and GSD grew especially fast.
- Squad crossed a meaningful maturity marker from v0.9.1 to v0.10.0, adding state backends, import/export, governed memory, RAI reviewer, MCP/frontmatter work, and broader Copilot CLI skill-path support.
- BMAD broadened beyond IDE workflows with Web Bundles for Gemini Gems and ChatGPT Custom GPTs, plus new `bmad-spec` and `bmad-ux` planning shapes.
- GSD moved deeper into multi-runtime support, especially Codex CLI, and changed emitted command conventions away from the older colon-form slash commands in some runtimes.
- HVE remains active at repo level, but latest release is still v3.2.2 from March 2026; substantial current activity appears unreleased or in post-release development.
- Ralph should continue to be described as a technique/ecosystem, not a single project. The canonical guide is mostly static, while ralph-orchestrator is the active implementation to watch.

---

## Existing Projects Freshness

### GSD — Get Shit Done

**Official source:** https://github.com/gsd-build/get-shit-done  
**Latest observed release:** v1.42.3, published 2026-05-16  
**Observed repo signal:** ~64.4K stars, ~5.5K forks, pushed 2026-05-31  
**Docs baseline:** v1.35.0, ~51.1K stars, ~4.3K forks.

Major changes since docs:

- Strong adoption growth: roughly +13K stars and +1.1K forks since the April baseline.
- Latest release notes emphasize Codex CLI support: `--codex` installs now materialize routable `$gsd-*` skills for Codex CLI 0.130.0+.
- User-facing command emission became runtime-aware: Claude/Cursor/OpenCode/Kilo-style runtimes emit `/gsd-<cmd>`, while Codex emits `$gsd-*`; older `/gsd:<cmd>` colon-form commands are no longer emitted at runtime according to v1.42.3 notes.
- Security/correctness fix: `check.ship-ready` moved from shell-interpolated `execSync` to argv-based subprocess execution, closing a shell-injection class through git ref names.
- More lifecycle guardrails: `phase_status` now gates planning against closed phases; executor agents are forbidden from `git stash` to preserve worktree isolation.

Suggested doc updates:

- Update current version and popularity numbers.
- Update command examples if docs imply colon-form commands are still the emitted runtime default.
- Strengthen “multi-tool support” language: GSD is still Claude Code-centered philosophically, but official Codex/OpenCode/Kilo-like runtime support is now substantial enough that “Claude Code primary, ports elsewhere” undersells the project.
- Mention Codex CLI 0.130.0+ requirement if documenting Codex support.

Sources:

- https://github.com/gsd-build/get-shit-done
- https://github.com/gsd-build/get-shit-done/releases/tag/v1.42.3

### BMAD Method

**Official source:** https://github.com/bmad-code-org/BMAD-METHOD  
**Docs:** https://docs.bmad-method.org  
**Latest observed release:** v6.8.0, published 2026-05-25  
**Observed repo signal:** ~49.4K stars, ~5.7K forks, pushed 2026-06-21  
**Docs baseline:** v6.3.0, ~44.4K stars, ~5.3K forks.

Major changes since docs:

- Growth remains strong: about +5K stars since the April baseline.
- v6.8.0 adds important planning artifacts: `bmad-spec` and `bmad-ux`.
- `bmad-spec` supersedes/retired `bmad-distillator` and produces a compact `SPEC.md` kernel from messy intent, PRDs, transcripts, or briefs. This is directly relevant to this repo’s spec-driven taxonomy.
- `bmad-ux` replaces the old single-spine UX skill with a two-file contract: `DESIGN.md` for visual identity/tokens and `EXPERIENCE.md` for behavior, flow, IA, states, and accessibility.
- Web Bundles were added for Gemini Gems and ChatGPT Custom GPTs, bringing BMAD planning bundles outside IDE-only usage while preserving schema parity with IDE skills.
- `bmad-automator` landed on the next channel; `bmad-method-ui` shipped as a community-alpha VS Code dashboard and standalone Next.js UI.
- 19 new elicitation techniques were added.
- Release notes call out strengthened activation guardrails across 23+ skills after agents skipped activation sequences.

Suggested doc updates:

- Update version and popularity numbers.
- Add `bmad-spec` as a major new core capability; it makes BMAD more directly comparable to Spec Kit/OpenSpec at the “intent distillation” layer.
- Add Web Bundles under supported environments; BMAD now reaches Gemini Gems and ChatGPT Custom GPTs, not just coding IDEs/agents.
- Mention `bmad-ux` if frontend/design workflow depth is discussed.
- Keep proprietary trademark caveat; GitHub license metadata still reports `NOASSERTION`/Other.

Sources:

- https://github.com/bmad-code-org/BMAD-METHOD
- https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.8.0
- https://docs.bmad-method.org

### HVE — Hypervelocity Engineering

**Official source:** https://github.com/microsoft/hve-core  
**Latest observed release:** hve-core-v3.2.2, published 2026-03-23  
**Observed repo signal:** ~1.18K stars, ~209 forks, pushed 2026-06-21  
**Docs baseline:** v3.2.2, 919 stars, 141 forks.

Major changes since docs:

- Version claim remains current: latest release is still v3.2.2.
- Repo activity is current despite no newer release; pushed 2026-06-21.
- Adoption increased moderately: about +260 stars and +68 forks.
- Open issue count is high (~431), which may reflect active development/support load rather than inactivity.
- GitHub custom properties include `activeRepoStatus: false`; unclear meaning without internal Microsoft context. Do not overinterpret publicly, but worth watching.
- Release assets confirm HVE is packaged as multiple VSIX/collection bundles with SBOM/signature artifacts: core, installer, coding standards, project planning, security, data science, GitHub, ADO, design thinking, RAI planning, etc.

Suggested doc updates:

- Update popularity numbers.
- Do not mark as inactive; repo push activity is current.
- Note that latest public release predates the April docs, so “progress since written” is mostly repo activity/adoption rather than a new release.
- Consider adding a “watch for next release” note if Morpheus wants freshness nuance.

Sources:

- https://github.com/microsoft/hve-core
- https://github.com/microsoft/hve-core/releases/tag/hve-core-v3.2.2

### OpenSpec

**Official source:** https://github.com/Fission-AI/OpenSpec  
**Official site:** https://openspec.dev/  
**Latest observed release:** v1.4.1, published 2026-06-03  
**Observed repo signal:** ~55.8K stars, ~3.9K forks, pushed 2026-06-13  
**Docs baseline:** v1.3.0, ~39.9K stars, ~2.7K forks.

Major changes since docs:

- Major adoption growth: roughly +16K stars and +1.2K forks since April baseline.
- Latest release is v1.4.1, a small update fix for `openspec update` in projects with their own `workspace.yaml`.
- The project remains active and highly watched; open issue count is high (~420), likely reflecting rapid adoption.
- Current docs should not imply v1.3.0 is current.

Suggested doc updates:

- Update version and popularity numbers.
- If the docs mention “daily commits,” soften to “active development” unless reverified each time; pushed within June 2026 is enough.
- Keep brownfield/change-centric positioning; no evidence this has changed.
- Workspaces/multi-repo should still be treated carefully. v1.4.1 touches `workspace.yaml` update behavior but does not by itself prove full team workspace/multi-repo feature availability.

Sources:

- https://github.com/Fission-AI/OpenSpec
- https://github.com/Fission-AI/OpenSpec/releases/tag/v1.4.1
- https://openspec.dev/

### Ralph / Ralph Wiggum Technique

**Canonical technique source:** https://ghuntley.com/ralph/  
**Canonical guide repo:** https://github.com/ghuntley/how-to-ralph-wiggum  
**Active implementation to watch:** https://github.com/mikeyobrien/ralph-orchestrator  
**Latest observed ralph-orchestrator release:** v2.9.3, published 2026-05-08  
**Observed repo signal:** how-to-ralph-wiggum ~1.7K stars, ~144 forks; ralph-orchestrator ~2.95K stars, ~280 forks, pushed 2026-05-26.

Major changes since docs:

- Canonical `how-to-ralph-wiggum` grew from ~1.4K to ~1.7K stars but has not been pushed since January 2026; it is a guide, not active software.
- `ralph-orchestrator` grew from ~2.7K to ~2.95K stars and released v2.9.3 in May 2026.
- `ralph-orchestrator` release artifacts now show a mature multi-binary distribution: `ralph-cli`, `ralph-api`, `ralph-bench`, `ralph-e2e`, npm packages, shell installers, and platform binaries.
- Repository topics include `codex-cli`, `gemini-cli`, `kiro`, `kiro-cli`, and `opencode`, suggesting the multi-backend ecosystem is broadening beyond the earlier Claude/Roo/Copilot/Pi framing.

Suggested doc updates:

- Update star/fork numbers.
- Separate “canonical method documentation is stable/static” from “ralph-orchestrator is active software.”
- Consider adding `ralph-orchestrator` as an increasingly important implementation rather than only a community port.
- Keep warning that Ralph is best understood as methodology/ecosystem; avoid assigning a single “current version” to Ralph itself.

Sources:

- https://ghuntley.com/ralph/
- https://github.com/ghuntley/how-to-ralph-wiggum
- https://github.com/mikeyobrien/ralph-orchestrator
- https://github.com/mikeyobrien/ralph-orchestrator/releases/tag/v2.9.3

### Spec Kit

**Official source:** https://github.com/github/spec-kit  
**Official site:** https://github.github.com/spec-kit/  
**Latest observed release:** v0.11.3, published 2026-06-19  
**Observed repo signal:** ~114.4K stars, ~10.1K forks, pushed 2026-06-19  
**Docs baseline:** v0.6.2, 87.8K+ stars.

Major changes since docs:

- Major growth: roughly +26K stars since the current deep dive baseline.
- Version moved from v0.6.2 to v0.11.3, still pre-1.0 but no longer as early as the docs imply.
- v0.11.3 release highlights extension/ecosystem maturation: isolated per-extension failures, GitHub issue skipping for already-created issues, `SPECIFY_INIT_DIR`, Multi-Model Review extension update, Token Economy extension added to community catalog.
- Claude integration improved: `/analyze` can run in a forked subagent.
- Docs strengthened agent disclosure around commits and per-round comments.

Suggested doc updates:

- Update version and popularity numbers.
- Adjust “earliest-stage technique” language; still experimental/pre-1.0, but very high adoption and active extension catalog make it feel less nascent.
- Update community extensions section with Token Economy and Multi-Model Review, plus better extension failure isolation.
- Keep the “experimental” caveat because it remains pre-1.0 and under active change.

Sources:

- https://github.com/github/spec-kit
- https://github.github.com/spec-kit/
- https://github.com/github/spec-kit/releases/tag/v0.11.3

### Squad

**Official source:** https://github.com/bradygaster/squad  
**Docs:** https://bradygaster.github.io/squad/  
**Latest observed release:** v0.10.0, published 2026-06-07  
**Observed repo signal:** ~2.84K stars, ~428 forks, pushed 2026-06-18  
**Docs baseline:** v0.9.1, active development / 1,454+ commits.

Major changes since docs:

- Crossed from v0.9.1 to v0.10.0.
- Substantial release body with many contributors and architecture-level work.
- Added state backend documentation and wiring across operations: worktree, git-notes, orphan, two-layer.
- Added `SQUAD_HOME` environment variable and preset system.
- Added import/export of Squad configuration to/from GitHub repos, preserving decisions/team/routing content.
- Added governed memory model, provider boundaries, diagnostics, and CLI validation.
- Added a built-in RAI reviewer agent, “Rai.”
- Added MCP frontmatter option to `squad init` and portable `squad_state` MCP config fixes.
- Improved skill scanning across all five Copilot CLI skill paths.
- Performance fixes: memoized squad-dir lookups, parallel charter discovery, non-blocking script task execution.
- Still Copilot/GitHub-centric; no evidence of community ports to Claude/Cursor/etc.

Suggested doc updates:

- Update version and adoption metrics.
- Add v0.10.0 maturity points: state backends, governed memory, import/export, built-in RAI reviewer, MCP frontmatter/config support.
- If docs currently say v0.9.1 SDK-first mode, broaden to v0.10.0 state/memory maturity.
- Keep “pre-1.0” caveat.

Sources:

- https://github.com/bradygaster/squad
- https://bradygaster.github.io/squad/
- https://github.com/bradygaster/squad/releases/tag/v0.10.0

### Superpowers

**Official source:** https://github.com/obra/superpowers  
**Latest observed release:** v6.0.3, published 2026-06-18  
**Observed repo signal:** ~234.4K stars, ~20.8K forks, pushed 2026-06-18  
**Docs baseline:** v5.0.7, ~151K stars, ~13.1K forks.

Major changes since docs:

- Enormous growth: about +83K stars and +7.7K forks since April baseline.
- Version moved to v6.0.3.
- v6.0.3 changed subagent-driven development scratch storage: task briefs, implementer reports, review diffs, and progress ledger moved from `.git/sdd/` to self-ignoring `.superpowers/sdd/` because Claude Code protects `.git/` from agent writes.
- This is a meaningful operational update: docs explaining internals should avoid saying SDD scratch lives in `.git/sdd/`.
- The framework remains highly active and should still be treated as the largest skill-based system in this comparison.

Suggested doc updates:

- Update version and popularity numbers.
- Add `.superpowers/sdd/` as the current subagent-driven development scratch/progress location if implementation details are described.
- Reassess “broadest multi-tool support” wording: Superpowers has broad support, but OpenSpec and Spec Kit now clearly exceed it numerically in tool count. Say “broad multi-tool support” rather than “broadest” unless comparing only skill-based frameworks.

Sources:

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/releases/tag/v6.0.3

### Context Engineering

**Practice source:** no canonical repo  
**Representative educational repo:** https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems  
**Observed representative repo signal:** ~251 stars, ~85 forks, pushed 2026-06-17.

Major changes since docs:

- No dominant canonical context-engineering framework has emerged based on this pass.
- The Denis2054 repo is active but smaller than prior notes implied; current stars are ~251, not a large adoption signal. Prior “555 commits” style signal should be rechecked before reuse.
- Context engineering continues to be absorbed into concrete systems: GSD runtime-specific skills, Spec Kit extension catalogs, Squad governed memory, Superpowers skills, HVE instruction collections.
- The practice remains diffuse and tool-format dependent.

Suggested doc updates:

- Avoid over-weighting a single educational repo.
- Emphasize that context engineering is becoming an embedded layer inside agent frameworks rather than consolidating into one standalone project.
- Keep “cross-cutting practice” classification.

Sources:

- https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems

---

## Additional Projects Worth Considering Today

The filter here is comparability to the repo’s scope: agentic development workflows, spec-driven development, multi-agent/software-delivery orchestration, context/skills systems, or autonomous coding workflows. Pure coding assistants are included only when they expose a reusable methodology or agent platform shape.

### Must Consider

#### OpenHands

**Source:** https://github.com/OpenHands/OpenHands  
**Site:** https://openhands.dev  
**Observed signal:** ~77.9K stars, ~9.9K forks, pushed 2026-06-20.

Rationale:

- Describes itself as “AI-Driven Development,” not just autocomplete.
- Mature open-source autonomous development platform with strong adoption.
- Comparable to autonomous coding workflows and agent execution environments rather than spec-driven methodology.
- Useful counterpoint to Ralph: more platformized, less “bash loop minimalism.”

Potential category:

- Autonomous Coding Platform / Agentic Dev Environment.

Why not already Tier 1:

- It is more of a product/platform than a technique for directing arbitrary coding agents. Morpheus/Neo should decide whether the repo wants platforms alongside methodologies.

#### Open SWE

**Source:** https://github.com/langchain-ai/open-swe  
**Related blog/homepage:** https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents  
**Observed signal:** ~10K stars, ~1.1K forks, pushed 2026-06-21.

Rationale:

- Explicitly “An Open-Source Asynchronous Coding Agent.”
- More workflow-comparable than many IDE assistants because it frames asynchronous internal coding agents.
- LangChain backing gives institutional momentum.
- Strong fit for the “autonomous/asynchronous coding workflow” slice next to Squad, HVE, and Ralph.

Potential category:

- Asynchronous Coding Agent / Autonomous Workflow.

Why must consider:

- This is close to GitHub Copilot Coding Agent / Devin-style background agents, which the current docs only touch indirectly.

#### Goose

**Source:** https://github.com/aaif-goose/goose  
**Docs:** https://goose-docs.ai/  
**Observed signal:** ~49.9K stars, ~5.3K forks, pushed 2026-06-21.

Rationale:

- Open-source extensible AI agent that can install, execute, edit, and test with any LLM.
- MCP and ACP topics make it relevant to tool/context orchestration, not only coding UI.
- Good candidate for “general agent runtime applied to development,” especially where teams want local extensibility.

Potential category:

- Extensible Agent Runtime / Autonomous Coding Agent.

Why must consider:

- Adoption and activity are high, and it overlaps with Ralph/OpenHands/OpenCode as a practical autonomous agent layer.

#### Cline

**Source:** https://github.com/cline/cline  
**Site:** https://cline.bot  
**Observed signal:** ~63.6K stars, ~6.7K forks, pushed 2026-06-20.

Rationale:

- Describes itself as an autonomous coding agent available as SDK, IDE extension, or CLI assistant.
- Large ecosystem and active development.
- Important because many frameworks listed here support Cline/Roo/Kilo as target agents; Cline itself may deserve a “platform/tool, not methodology” profile or appendix entry.

Potential category:

- Autonomous Coding Agent / Tool Platform.

Why must consider:

- Even if excluded from Tier 1 methodology comparison, Cline is a major substrate in the ecosystem and should be surfaced explicitly.

### Maybe

#### Aider

**Source:** https://github.com/Aider-AI/aider  
**Site:** https://aider.chat/  
**Observed signal:** ~46.5K stars, ~4.6K forks, pushed 2026-05-22.

Rationale:

- Mature terminal pair-programming agent with strong adoption.
- Less of a methodology/framework than GSD/BMAD/Superpowers, but has distinct git-centric workflow patterns.
- Useful baseline for CLI-first AI coding before heavier process frameworks.

Why maybe:

- The repo’s current scope says “not the tools themselves.” Aider is mostly a tool, unless Morpheus frames it as a git-native agentic workflow.

#### OpenCode

**Source:** https://github.com/anomalyco/opencode  
**Site:** https://opencode.ai  
**Observed signal:** ~176.7K stars, ~21.6K forks, pushed 2026-06-21.

Rationale:

- Massive adoption signal and active development.
- Major open-source coding agent; GSD and OpenSpec already list/support it.
- Relevant as a target runtime and as evidence of CLI-agent standardization.

Why maybe:

- It appears more like a coding agent product than a technique. Include if the comparison grows an “agent platforms and runtimes” appendix.

#### Continue

**Source:** https://github.com/continuedev/continue  
**Site:** https://continue.dev  
**Observed signal:** ~34.2K stars, ~4.75K forks, pushed 2026-06-21.

Rationale:

- Open-source coding agent with broad adoption.
- Important substrate for custom AI workflows and organization-level rules.

Why maybe:

- Mostly a tool/platform. Comparable only if repo expands to include agent substrates, not just methodologies.

#### Kilo Code

**Source:** https://github.com/Kilo-Org/kilocode  
**Site:** https://kilo.ai/  
**Observed signal:** ~23.4K stars, ~2.7K forks, pushed 2026-06-20.

Rationale:

- Describes itself as an “all-in-one agentic engineering platform.”
- Supports VS Code, JetBrains, CLI-related topics, and common LLM providers.
- Relevant because the current docs already mention Kilo as a bridge/target in community ports.

Why maybe:

- More platform than method. Worth a short “ecosystem substrate” note.

#### Pythagora / GPT Pilot

**Source:** https://github.com/Pythagora-io/gpt-pilot  
**Observed signal:** ~33.7K stars, ~3.5K forks, pushed 2026-06-18.

Rationale:

- Earlier “AI developer” lineage; historically important for autonomous app-building workflows.
- Still active and sizable.

Why maybe:

- Less obviously aligned with the current repo’s “humans organize and direct AI coding agents” framing than BMAD/Spec Kit/Squad.

#### Roo Code

**Source observed via redirect:** https://github.com/RooCodeInc/Roo-Code  
**Site:** https://roocode.com  
**Observed signal:** ~24.3K stars, ~3.3K forks, archived true, pushed 2026-05-15.

Rationale:

- Describes itself as “a whole dev team of AI agents in your code editor,” so conceptually comparable to multi-agent coding workflows.
- Current repository is archived, which is a major caveat. Need follow-up to confirm whether development moved elsewhere or product restructured.

Why maybe:

- Include only after resolving archival/rebrand status. Current archived flag makes it risky as a recommended project.

### Watchlist

#### AutoGPT

**Source:** https://github.com/Significant-Gravitas/AutoGPT  
**Site:** https://agpt.co  
**Observed signal:** ~185K stars, ~46K forks, pushed 2026-06-20.

Rationale:

- Historically central autonomous-agent project and still active.
- Broader than software delivery; not specifically a coding workflow methodology.

Why watchlist:

- Useful context for agent autonomy lineage, but likely outside the repo’s focused scope unless adding a history/background section.

#### SWE-agent

**Source:** https://github.com/swe-agent/SWE-agent  
**Status:** API fetch returned 403 during this pass; needs direct follow-up.

Rationale:

- Important for SWE-bench style autonomous repair agents and benchmark-driven workflows.
- Likely relevant to autonomous coding/research, but needs fresh official metadata before ranking higher.

Why watchlist:

- Strong conceptual relevance, but this pass did not verify current repo state.

#### Roo Code successor/rebrand path

**Observed source:** https://github.com/RooCodeInc/Roo-Code archived.  
**Status:** Needs follow-up.

Rationale:

- The archived flag suggests either project inactivity or a migration/rebrand.
- Because many AI workflow tools list Roo support, knowing whether Roo is active matters for compatibility tables.

---

## Cross-Cutting Gaps / Inconsistencies to Flag

- **Star chart and README counts are stale.** Superpowers, Spec Kit, GSD, OpenSpec, BMAD, Squad, HVE, and Ralph numbers all need updating.
- **Spec Kit and Superpowers have outgrown April scale assumptions.** Spec Kit is now over 100K stars; Superpowers is over 230K stars.
- **“Broadest support” claims need precision.** OpenSpec appears broadest by number of supported tools. Spec Kit is also broad. Superpowers is broad for a skills methodology, but not broader than OpenSpec by tool count.
- **Tool vs. methodology boundary is now the central scoping decision.** OpenHands, Cline, Goose, OpenCode, Aider, Continue, and Kilo are too important to ignore, but most are agent platforms rather than methodologies. Recommend an appendix or “substrates” section unless Neo wants to expand Tier 1 scope.
- **Copilot-only lock-in remains accurate for Squad and HVE.** Squad improved Copilot CLI/MCP integration, not portability to other AI coding agents. HVE remains GitHub Copilot-centered.
- **Ralph ecosystem split should be explicit.** Canonical guide is static; ralph-orchestrator is active. Treating either as “Ralph current version” is misleading.

---

## Suggested Candidate Ranking Summary

| Rank | Project | Why |
|---|---|---|
| Must consider | OpenHands | Major open-source autonomous development platform; strong adoption; closest platformized comparison to Ralph/autonomous workflows. |
| Must consider | Open SWE | Asynchronous coding agent framework from LangChain; directly relevant to background coding agents. |
| Must consider | Goose | Extensible agent runtime with MCP/ACP signals and strong adoption; useful autonomous workflow substrate. |
| Must consider | Cline | Major autonomous coding agent as SDK/IDE/CLI; ecosystem substrate used by/alongside many frameworks. |
| Maybe | Aider | Mature git/terminal AI pair programming workflow; mostly a tool, but useful baseline. |
| Maybe | OpenCode | Huge adoption and target runtime for several techniques; mostly an agent product. |
| Maybe | Continue | Open-source coding agent platform; more substrate than methodology. |
| Maybe | Kilo Code | Agentic engineering platform and compatibility target; more platform than method. |
| Maybe | Pythagora / GPT Pilot | Historically important autonomous app-building workflow; scope fit is less crisp. |
| Maybe | Roo Code | Conceptually relevant multi-agent coding IDE, but current observed repo is archived. Verify rebrand/successor first. |
| Watchlist | AutoGPT | Important autonomous-agent lineage, but too broad for software-delivery methodology comparison. |
| Watchlist | SWE-agent | Likely relevant to benchmark/autonomous repair workflows; needs fresh metadata after API fetch 403. |
