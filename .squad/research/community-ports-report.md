# Community Ports & Adaptations Report

**Researcher:** Trinity  
**Date:** 2026-04-14  
**Requested by:** Marco Olivo  

---

## 1. GSD (Get Shit Done)

### Official Multi-Platform Support (UPDATE)
GSD's official installer (`npx get-shit-done-cc`) now supports flags beyond Claude Code:
- `--opencode` — OpenCode integration
- `--codex` — Codex CLI integration
- Gemini CLI support documented in official install docs

These are **not community ports** — they are first-party. The doc page we have may be out of date.

### Community Ports Found

#### rmindel/gsd-for-cursor
- **Repo:** https://github.com/rmindel/gsd-for-cursor
- **Stars/Forks:** 76 ★ / 15 forks
- **Author:** rmindel (appears to be a real developer)
- **Description:** Full Cursor IDE adaptation of GSD. Includes Shell/PowerShell install scripts, docs directory, migration guide from GSD Master, contribution guide. 14 commits.
- **Last Updated:** ~Apr 8, 2026
- **Legitimacy:** ✅ LEGIT — Meaningful star count, real content (not a placeholder), active as of April 2026.

#### GSD for Copilot (Community Fork — No Standalone Repo Found)
- **Source:** GitHub Issue #600 on gsd-build/get-shit-done ("Feature: Native Support for Github Copilot via --copilot install")
- A user reported forking GSD and letting Claude adapt it to VS Code / GitHub Copilot Pro on Windows. Not a standalone published repo — it was a personal fork.
- **Reddit Post:** r/GithubCopilot — "GSD (Get Shit Done) now works with GitHub Copilot — ported from the Claude Code → Kilo Code chain." This appears to be the same effort or a related one routing through Kilo Code as a bridge.
- **Legitimacy:** ⚠️ QUESTIONABLE — No standalone repo published. Exists as personal forks and Reddit posts, not a reusable package.

#### itsjwill/gsd-pro
- **Repo:** https://github.com/itsjwill/gsd-pro
- **Stars/Forks:** 66 ★
- **Description:** "GSD Pro — The most powerful AI coding workflow for Claude Code. Free alternative to Cursor Composer, Copilot Workspace, Devin & Bolt. Multi-model routing, rollback/recovery, adaptive context. Fork of 30K★ original."
- **Legitimacy:** ✅ LEGIT — Fork with added features (multi-model routing, rollback/recovery). Active.

#### Chaturaphut/gsd-openclaw
- **Repo:** https://github.com/Chaturaphut/gsd-openclaw
- **Stars/Forks:** 3 ★
- **Description:** "GET-SHIT-DONE-OPENCLAW" — integrates GSD with OpenClaw multi-agent workflows.
- **Last Updated:** Apr 13, 2026
- **Legitimacy:** ✅ LEGIT but tiny — Real content, actively maintained, but negligible adoption.

### Ports NOT Found
- **GSD for Windsurf:** No dedicated port found.
- **GSD for Roo Code:** No dedicated port found.
- **GSD for Gemini CLI:** Covered officially (see above).

---

## 2. BMAD Method

### Key Finding: BMAD V6 Went Officially Multi-Platform
BMAD V6 is NOT community-ported — it is **officially cross-platform** now. V6 supports:
- Claude Code (primary)
- Cursor
- Windsurf
- GitHub Copilot (VS Code)
- Roo Code (shown working in YouTube demos)

BMAD also has an **MCP Server** that works with VS Code / Claude Desktop / Cursor (posted to r/GithubCopilot).

### Community Ports/Adaptations Found

#### BMAD + GitHub Copilot Integration Issues
- **GitHub Issue #1482:** "GitHub Copilot Integration: Config Access, Agent Handover & Features" — consolidates multiple issues affecting Copilot + VS Code integration with BMAD agents.
- **GitHub Issue #2131:** "Visual Studio 2026 doesn't recognise BMad agents with BMad v6.2.2" — compatibility issue with VS 2026.
- **GitHub Discussion #1568:** "Possibility of using BMad Method + GitHub CoPilot+ autonomously" — user asking about autonomous workflow with Copilot.

These are **integration issues with the official product**, not community ports.

### Ports NOT Found
- **BMAD for Gemini CLI:** No dedicated port or adaptation found.
- No significant unofficial forks or community adaptations beyond the official multi-platform support.

### Assessment
BMAD doesn't need community ports because the maintainer (bmad-code-org) built official cross-platform support into V6. The "port" story here is that the official project already covers it.

---

## 3. Squad

### Ports NOT Found
No community ports exist for Squad. It remains **GitHub Copilot-only** by design.

- No "Squad for Claude Code" repo found
- No "Squad for Cursor" repo found
- No unofficial adaptations found

Squad is tightly coupled to Copilot's agent mode and `.github/agents/` file structure. Porting it would require re-implementing the agent dispatch mechanism for a different platform.

### Assessment
Squad has **zero community ports**. This is a gap worth noting in the comparison doc.

---

## 4. HVE (Hypervelocity Engineering)

### Ports NOT Found
No community ports exist for HVE. It remains **GitHub Copilot-only** (microsoft/hve-core).

- No "HVE for Claude Code" repo found
- No "HVE for Cursor" repo found
- No unofficial adaptations found

HVE is deeply integrated into the Copilot + VS Code ecosystem with 49 agents, 102 instructions, and a VS Code extension. Its enterprise governance model makes it hard to port.

### Assessment
HVE has **zero community ports**. Like Squad, this creates platform lock-in for teams that adopt it.

---

## 5. Spec Kit

### Official Status
Spec Kit (github/spec-kit) is already agent-agnostic by design. It has:
- An **extension catalog** system (`extensions/catalog.json` + `extensions/catalog.community.json`)
- A **preset catalog** system (`presets/catalog.json`)
- An **integration catalog** proposal (Issue #2066, filed Apr 2, 2026) for community-contributed integrations

### Community Extensions Found

#### Fatima367/spec-kit-github-issues
- **Repo:** https://github.com/Fatima367/spec-kit-github-issues
- **Stars/Forks:** 1 ★ / 0 forks
- **Description:** Community extension that generates spec artifacts from GitHub Issues, bridging issue tracking and SDD workflows. Has full extension structure with 7 files.
- **Last Updated:** Apr 12, 2026 (v1.0.0 released)
- **Legitimacy:** ✅ LEGIT but brand new — Real content with extension.yml, commands, and docs. Very early stage.

#### mateors1/adik.md Spec Kit Extension
- **Source:** Spec Kit GitHub Discussions
- **Description:** A community member (Mateo/@mateors1) submitted a Spec Kit extension as part of the ADIK (Agentic Development and Implementation Kit) framework. Includes full extension structure, integration guide, and 10-part technical analysis comparing the two frameworks.
- **Legitimacy:** ✅ LEGIT — Real work with documentation, submitted to community catalog.

### Assessment
Spec Kit's community extension ecosystem is **nascent but architecturally ready**. The catalog infrastructure exists; community contributions are just starting to trickle in. Issue #2066 would formalize a full integration catalog system matching extensions and presets.

---

## 6. Ralph

### Official Repos Status

#### ghuntley/how-to-ralph-wiggum
- **Repo:** https://github.com/ghuntley/how-to-ralph-wiggum
- **Stars/Forks:** 1,400 ★ / 127 forks (forked from ClaytonFarr/ralph-playbook)
- **Author:** Geoffrey Huntley (original creator)
- **Last Updated:** Active (posted to r/ClaudeCode ~3 months ago)
- **Note:** Our docs said 8.7K stars — that appears to be **outdated or incorrect**. Current count is ~1.4K.
- **Legitimacy:** ✅ LEGIT — The canonical Ralph technique documentation.

#### mikeyobrien/ralph-orchestrator
- **Repo:** https://github.com/mikeyobrien/ralph-orchestrator
- **Stars/Forks:** 2,700 ★ / 246 forks
- **Author:** Mikey O'Brien (mikeyobrien) — real developer, active on GitHub with multiple projects
- **Description:** Full orchestration system in Rust implementing the Ralph Wiggum technique. Now at v2.9.2 with:
  - **Multiple backends:** Claude Code, Roo Code, Copilot, Pi (and Forge CLI requested in Issue #281)
  - Web dashboard (alpha), MCP server mode, TUI interface
  - Agent waves for parallel execution
  - 492 commits, ~300 issues, active community PRs
- **Last Updated:** Apr 10, 2026 (v2.9.2)
- **Legitimacy:** ✅ VERY LEGIT — One of the most actively developed community tools in the entire SDD ecosystem. Rust-based, well-tested, multi-backend, cited in Anthropic's Ralph plugin documentation.

#### Soul-Brews-Studio/ralph-local
- **Repo:** https://github.com/Soul-Brews-Studio/ralph-local
- **Stars/Forks:** 4 ★ / 1 fork
- **Description:** Ralph Loop plugin — local fork with session isolation and multi-agent support. Claude Code plugin format.
- **Last Updated:** Recent (14 commits)
- **Legitimacy:** ✅ LEGIT but small — Niche fork adding session isolation features.

### Assessment
Ralph has a **thriving community ecosystem**. The ralph-orchestrator is a standout — it's grown from a simple loop into a 2.7K-star multi-backend orchestration platform with Rust RPC, web dashboard, and support for Claude, Roo Code, Copilot, and more. This is far beyond what most "community port" means — it's a production-grade implementation.

**Correction needed:** Our docs reference 8.7K stars for ralph-claude-code. Can't confirm that number. The main repos are ghuntley/how-to-ralph-wiggum (1.4K★) and mikeyobrien/ralph-orchestrator (2.7K★).

---

## 7. Superpowers

### Official Multi-Platform Support (UPDATE)
As of Superpowers v5.0.7, the official project supports:
- Claude Code (primary)
- Cursor
- Codex
- OpenCode
- Gemini CLI
- **Copilot CLI** (added via `additionalContext` support in Copilot CLI v1.0.11)

The official project includes a tool mapping reference table (Claude Code tool names → Copilot CLI equivalents).

### Community Ports Found

#### dwaintr.superpowers-vscode (VS Code Marketplace Extension)
- **Marketplace:** Superpowers for Copilot Chat by Kaan Aslan (DwainTR)
- **Installs:** 2,568
- **Description:** Brings Superpowers skills to GitHub Copilot Chat in VS Code as a `@superpowers` chat participant with 14 slash commands (/brainstorming, /tdd, /debug, /plan, /execute, /subagent, /parallel, /review, /receive-review, /verify, /worktree, /finish, /write-skill, /superpowers). Custom skills support via `~/.copilot/skills/superpowers/`.
- **Based on:** Skills by Jesse Vincent (official Superpowers author)
- **Legitimacy:** ✅ LEGIT — Published extension, 2.5K+ installs, full feature set.

#### anothel.superpowers-copilot-agents (VS Code Marketplace Extension)
- **Marketplace:** Superpowers Copilot Agents by anothel
- **Installs:** 389
- **Description:** Converts Superpowers workflow skills into VS Code Copilot agents (14 agents auto-registered). On activation, copies agent files to `~/.superpowers-copilot/agents/` and registers the path in VS Code settings.
- **Legitimacy:** ✅ LEGIT — Different approach (agents vs. chat participant), smaller but legitimate.

#### varunr89/superpowers-copilot
- **Repo:** https://github.com/varunr89/superpowers-copilot
- **Stars/Forks:** 4 ★ / 1 fork
- **Description:** GitHub Copilot adaptation of Superpowers. Includes .copilot, .codex, and .claude-plugin directories. 119 commits, MIT license.
- **Legitimacy:** ✅ LEGIT — Real content, multi-platform adaptation, but low adoption.

#### jsloat/superpowers-for-copilot
- **Repo:** https://github.com/jsloat/superpowers-for-copilot
- **Stars/Forks:** 3 ★ / 0 forks
- **Description:** "Fork of obra/superpowers to work with Copilot CLI." Includes skills directory, install instructions. 7 commits.
- **Legitimacy:** ✅ LEGIT — Clean fork, documented differences from Claude Code.

### Community Demand Evidence
- **Issue #217** on obra/superpowers: "Can superpowers support GitHub Copilot?" — confirmed working with in-UI VS Code Local Agent chat.
- **Issue #764** on obra/superpowers: "GitHub Copilot (VS Code) integration" — feature request for official Copilot support (opened Mar 16, 2026 by tjgoldblatt).
- **Reddit post** in r/GithubCopilot: "Github Copilot CLI - Superpowers Plugin Ready For Use" — announced VS Code Extension publication.

### Assessment
Superpowers has the **most active community porting activity** of any technique in this survey. Two VS Code Marketplace extensions, two GitHub repos, official feature requests, and Reddit announcements. The official project also added Copilot CLI support natively, closing the gap from both sides.

---

## 8. Context Engineering

### Nature of the Technique
Context engineering is a **practice/discipline**, not a framework with a repo you port. There is no "context engineering repo" to port to different platforms. However, there are community efforts to package and share context engineering knowledge.

### Notable Community Repos

#### Denis2054/Context-Engineering-for-Multi-Agent-Systems
- **Repo:** https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems
- **Stars:** Not visible from search (needs direct check), but 555 commits
- **Description:** Book companion repo — "production-ready blueprint for the Agentic Era." 10 chapters covering architecture, context, agents, and code. MCP integration. MIT license. Live workshop cohorts.
- **Last Updated:** Active (555 commits)
- **Legitimacy:** ✅ LEGIT — Comprehensive educational resource with code examples.

#### bonigarcia/context-engineering
- **Repo:** https://github.com/bonigarcia/context-engineering
- **Description:** "Top GitHub Context Engineering repositories" — an auto-aggregated index of public repos related to context engineering.
- **Legitimacy:** ✅ LEGIT — Aggregator/index, not a tool.

#### GitHub Topics
- `context-engineering` and `context-engineering-framework` topics exist on GitHub but have sparse repositories.
- No single dominant "context engineering framework" repo has emerged.

### Assessment
Context engineering remains a **diffuse practice** without a dominant community tool or framework. The Denis2054 repo is the most comprehensive educational resource. No standardization effort has coalesced — it's still practiced through per-tool mechanisms (CLAUDE.md, .cursorrules, copilot-instructions.md, etc.).

---

## Summary Table

| Technique | Community Ports Found | Most Significant | Platform Gap |
|---|---|---|---|
| **GSD** | 3 (Cursor, Copilot/Kilo, OpenClaw) | rmindel/gsd-for-cursor (76★) | Windsurf, Roo Code |
| **BMAD** | 0 (went officially multi-platform) | N/A — V6 covers it | Gemini CLI |
| **Squad** | 0 | None | Claude Code, Cursor, everything non-Copilot |
| **HVE** | 0 | None | Claude Code, Cursor, everything non-Copilot |
| **Spec Kit** | 2 community extensions | GitHub Issues extension | Already agent-agnostic |
| **Ralph** | 3+ significant | ralph-orchestrator (2.7K★) | Already multi-backend |
| **Superpowers** | 4 repos + 2 VS Code extensions | dwaintr.superpowers-vscode (2.5K installs) | Windsurf, Roo Code (no dedicated ports) |
| **Context Engineering** | Educational repos only | Denis2054 book companion | N/A — practice, not framework |

## Key Insights

1. **The "Copilot-only" tools (Squad, HVE) have zero community ports.** This is the biggest gap in the ecosystem. Teams adopting these are locked to Copilot.

2. **Tools that start tool-agnostic attract the most community activity.** Ralph and Superpowers both have vibrant port ecosystems precisely because their core concepts aren't tied to one platform.

3. **Official projects are catching up.** GSD added --opencode/--codex/Gemini, BMAD went multi-platform in V6, Superpowers added Copilot CLI. The "community port" phase may be transitional — successful ports get adopted upstream.

4. **ralph-orchestrator is an outlier.** At 2.7K stars with multi-backend support (Claude, Roo, Copilot, Pi), it's evolved far beyond a simple port — it's a standalone platform.

5. **Star count corrections needed:** Our docs may reference "ralph-claude-code 8.7K stars" which I could not verify. The repos I found are ghuntley/how-to-ralph-wiggum (1.4K★) and mikeyobrien/ralph-orchestrator (2.7K★).
