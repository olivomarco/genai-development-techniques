# Market updates

A log of research passes and the resulting documentation changes, newest first. New entries are added without replacing earlier records. See [Research Methodology](methodology.md) for scope and evidence labels.

---

## October 27, 2026 — research pass and documentation restructuring

**Research findings (Verified unless noted):**

- **Skills-market taxonomy expanded.** The skills layer now spans at least six structurally distinct categories: specification, composable library, lifecycle library, orchestrating mode, methodology, and installer/marketplace/curated-channel distribution. See [State of the Skills Market](techniques/skills-ecosystem.md).
- **Addy Osmani's `addyosmani/agent-skills` and `pstack/poteto-mode` coverage added.** `addyosmani/agent-skills` (v0.6.13) is profiled as a lifecycle library mapping skills to define → plan → build → verify → review → ship stages. `pstack/poteto-mode`, canonically the `pstack/` directory in Cursor's [`cursor/plugins`](https://github.com/cursor/plugins) marketplace repository, is profiled as the category's lead example of an orchestrating mode — a dispatcher that routes requests to a library's other skills rather than acting as a standalone capability. See [Orchestrating Modes](techniques/skills-orchestrating-modes.md).
- **Skills now ship as managed packages.** Reusable skills are moving from loose file collections into versioned, updatable packages. Two channels distribute them: cross-agent installer CLIs (skills.sh's `npx skills`, vendored and reviewable) and native plugin marketplaces (Claude Code, GitHub Copilot, Codex — managed and auto-updating). No surface we examined signs, attests, or lockfile-pins a skill.
- **Model, runtime, and methodology remain separate layers.** As frontier models and first-party runtimes handle more bounded, checkable work, those tasks need less prescriptive methodology. Execution runtimes remain necessary, and not every harness is thin. See the three-layer model in the [overview](overview.md#the-three-layer-model-model-runtime-methodology).
- **Spec Kit and Squad confirmed past 1.0.** Spec Kit is at v1.2.3; Squad reached 1.0 in October 2026 and is at v1.1.0 stable, with a v2.0.0 prerelease channel active.
- **Superpowers at v7.0.1.** The brainstorming skill was rebuilt in v7.0.0 and retuned in v7.0.1; a native Antigravity Marketplace plugin manifest shipped alongside.
- **Framework version refresh (Reported/Signal, per-project labels as stated on each technique page):** GSD Core v1.19.0, OpenSpec v1.15.0, BMAD v6.12.4, HVE v3.2.2 stable with v3.3 prereleases, Ralph's `ralph-orchestrator` at v2.10.1.
- **Vercel's `vercel-labs/agent-skills`** (a domain-specific skill collection: Vercel/React/Next.js audits, React Native guidance, and writing-handbook checks) is distinct from `vercel-labs/skills`, the CLI behind skills.sh. Both are maintained by Vercel but serve different roles — content versus installer. See [Skill Libraries](techniques/skills-libraries.md).
- **Name-collision caveat recorded.** `pstack/poteto-mode` (an orchestrating mode) and `aryannaio/potato-mode-agent-skill` (a resource-throttling skill for low-spec machines) are unrelated projects with similar names. See [Orchestrating Modes](techniques/skills-orchestrating-modes.md) for the distinction.

**Documentation changes (not independent research findings):**

- Split `techniques/skills-ecosystem.md` from a single large catch-all page into a concise state-of-the-market overview plus four focused pages: [Skill Libraries](techniques/skills-libraries.md), [Orchestrating Modes](techniques/skills-orchestrating-modes.md), [Distribution and Governance](techniques/skills-management.md), and [Choosing a Skills Approach](techniques/skills-choosing.md). The `techniques/skills-ecosystem.md` URL was preserved to avoid breaking inbound links.
- Regrouped site navigation into three sections: **Guide** (Home, Overview, Choosing Your Approach, Research Methodology, Market Updates), **Techniques** (the eight Tier 1 methodologies plus Context Engineering), and **Skills and Agent Frameworks** (the five pages above plus Superpowers, moved here as a nav-only change — its URL and content are unchanged).
- Removed the duplicated detailed skills-selection section from `techniques/choosing-your-approach.md`, replacing it with a concise category summary and a link to [Choosing a Skills Approach](techniques/skills-choosing.md).
- Added this page and [Research Methodology](methodology.md) as new root-level pages.
- Added a short TL;DR to `README.md` and updated its document table to reflect the new navigation structure.

---

Earlier research passes, including August 8, 2026, predate this log and are not listed here.
