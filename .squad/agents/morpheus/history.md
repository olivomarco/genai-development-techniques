# Morpheus — History

## Project Context
- **Project:** Comparison of GenAI development techniques
- **Goal:** Research and document frameworks like GSD, BMAD, SPEC-KIT, Squad, Ralph, and other techniques used to run GenAI development at scale
- **Stack:** Markdown documentation, research-heavy
- **User:** Marco Olivo
- **Created:** 2026-04-12

## Learnings

### 2026-04-12: Wrote first batch of technique deep-dives (GSD, BMAD, Spec Kit, Squad)
- Created `techniques/` directory with 4 deep-dive documents following the template from research-scope.md section 4.2
- Source material: research-raw-findings.md sections 1-4 and research-scope.md section 5 (comparison dimensions)
- Each doc follows the exact template: At a Glance table → Overview → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Comparison Notes
- Cross-references stay within the 8 Tier 1 techniques: GSD, BMAD, Spec Kit, Squad, Ralph, HVE, MetaGPT, Context Engineering
- Key pattern: GSD and Spec Kit are Spec-Driven; BMAD and Squad are Multi-Agent Orchestration — but BMAD simulates agents within a session while Squad spawns actual parallel instances
- Star counts as of April 2026: GSD ~51K, BMAD ~44K, Spec Kit (GitHub-backed, fewer stars), Squad (Microsoft-backed, 1,454+ commits)
- Spec Kit is earliest stage (v0.6.0), explicitly experimental; GSD most mature spec-driven (v1.35.0)
- BMAD has proprietary trademark on name despite being open source — noted in limitations
- Remaining: 4 more technique docs needed (Ralph, HVE, MetaGPT, Context Engineering)

### 2026-04-12: Wrote second batch of technique deep-dives (Ralph, HVE, Context Engineering, MetaGPT)
- Created 4 documents completing the `techniques/` directory: ralph.md, hve.md, context-engineering.md, metagpt.md
- Source material: research-raw-findings.md (sections 5, 13/14, 15), research-ralph-hve.md (detailed Ralph and HVE research), research-scope.md (template and tier list)
- Ralph and HVE had the richest source material (dedicated research-ralph-hve.md file plus raw findings sections)
- Context Engineering had moderate coverage (section 5 of raw findings) — synthesized into a practice-oriented document since it's not a framework but a cross-cutting discipline
- MetaGPT had thin coverage in raw findings (only 2 cross-cutting table mentions) — noted gaps explicitly in the document and worked from research-scope.md's description + publicly available project info. Flagged with "Research gap" annotations where deeper investigation would strengthen the analysis.
- Key insight: Ralph and HVE are opposite ends of the autonomy-governance spectrum (bash loop vs. 49 agents + 102 instructions). Context Engineering underpins all 8 techniques as a practice.
- MetaGPT is the most standalone of all Tier 1 techniques — no IDE integration, no rules file ecosystem integration. Stars (~50K+) comparable to GSD but community is more research-oriented.
- All 8 Tier 1 technique documents now complete in `techniques/` directory.

### 2026-04-14: Wrote Superpowers technique deep-dive
- Created `techniques/superpowers.md` following the established template (At a Glance → Compatible Coding Agents → Overview → Pros & Cons → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Comparison Notes)
- Source material: comprehensive pre-researched brief provided by Neo (no additional research needed)
- Superpowers introduces a NEW category: "Skill-Based Development" — distinct from Spec-Driven (GSD, Spec Kit) and Multi-Agent Orchestration (BMAD, Squad). This is the first technique in this comparison that defines its own category.
- Key differentiators: largest community by far (151K stars — 3× GSD), broadest multi-tool support (6 tools), self-improving skill system with persuasion-tested compliance
- Author Jesse Vincent (obra) has notable pedigree: Keyboardio founder, Best Practical co-founder (RT), Prime Radiant team
- Comparison notes written against GSD, BMAD, and Context Engineering — the three most relevant comparison points per the research brief
- Rapid version churn (v1→v5 in 6 months) noted as both a sign of active development and a potential risk for early adopters

### 2026-04-14: Scribe — Cross-agent update
- Neo integrated Superpowers across all interlinking docs (overview.md, choosing-your-approach.md, gsd.md, context-engineering.md)
- "Skill-Based Development" category accepted as fifth taxonomy category in decisions.md
- Technique count now 9, category count now 5 (plus Context Engineering cross-cutting)

### 2026-04-14: Community ports & unofficial adaptations update
- Updated 6 technique files with community port information from Trinity's research report (`.squad/research/community-ports-report.md`)
- **gsd.md:** Updated Cursor row with link to gsd-for-cursor (76★). Added "Community Ports & Unofficial Adaptations" section covering gsd-for-cursor, gsd-pro (66★), official --opencode/--codex/Gemini flags, grassroots Copilot effort via Kilo Code, and gaps (Windsurf, Roo Code).
- **bmad.md:** Added note in Community & Ecosystem that V6's official multi-platform support renders community ports unnecessary — the maintainer built cross-platform directly.
- **spec-kit.md:** Added "Community Ports & Unofficial Adaptations" section covering catalog infrastructure, spec-kit-github-issues, ADIK integration, and Issue #2066 integration catalog proposal.
- **ralph.md:** CRITICAL FIX — replaced unverified "8.7K+ stars" claim with verified numbers: how-to-ralph-wiggum (1.4K★, 127 forks) and ralph-orchestrator (2.7K★, 246 forks). Rewrote Community & Ecosystem with canonical doc repo, ralph-orchestrator (now a Rust-based multi-backend platform at v2.9.2), and ralph-local (4★).
- **superpowers.md:** Updated Copilot row from ❌ to ⚠️ Community with two VS Code Marketplace extensions (2,568 and 389 installs). Added "Community Ports & Unofficial Adaptations" section covering both marketplace extensions, two GitHub repos, and official v5.0.7 Copilot CLI support.
- **context-engineering.md:** Added educational resource note (Denis2054 book companion, 555 commits) and observation that no dominant framework has emerged.
- **squad.md and hve.md:** No changes — both already clearly document Copilot-only status with zero community ports.
- Key insight: techniques that start tool-agnostic (Ralph, Superpowers) attract the most community ports. Copilot-only tools (Squad, HVE) have zero. BMAD sidesteps the issue by going officially multi-platform.

### 2026-04-14: Wrote OpenSpec technique deep-dive
- Created `techniques/openspec.md` — the 10th technique deep-dive, 3rd in the Spec-Driven Development category alongside GSD and Spec Kit
- Source material: Trinity's research report (`.squad/decisions/inbox/trinity-openspec-research.md`) and Neo's scoping decision (`.squad/decisions/inbox/neo-openspec-scope.md`)
- Followed the established template exactly: At a Glance → Compatible Coding Agents → Overview → Pros & Cons → Core Concepts → How It Works → Strengths → Limitations → Best For → Not Ideal For → Community & Ecosystem → Community Ports & Unofficial Adaptations → Comparison Notes
- Key structural decisions:
  - Compatible Coding Agents table lists all 27+ tools individually (not grouped) — this is by far the largest agent table in the comparison, reflecting OpenSpec's unique breadth
  - Community Ports section explicitly notes that no ports are needed due to native 27+ tool support — a deliberate contrast to GSD (needed community forks) and Superpowers (needed marketplace extensions)
  - Comparison Notes written against 4 techniques: GSD (greenfield vs. brownfield), Spec Kit (comprehensive vs. lightweight), Context Engineering (practice vs. implementation), Superpowers (skill-based vs. spec-driven)
  - Positioned OpenSpec's unique differentiator as "change-centric" vs GSD's "task-centric" and Spec Kit's "project-centric" — this three-way taxonomy within Spec-Driven Development is clean and clarifying
- How It Works table includes all 10 opsx commands from Neo's scope: /opsx:new, /opsx:propose, /opsx:apply, /opsx:archive, /opsx:continue, /opsx:ff, /opsx:verify, /opsx:sync, /opsx:bulk-archive, /opsx:onboard
- Delta specs (ADDED/MODIFIED/REMOVED markers) are the most distinctive concept — no other technique has this
- Remaining work: overview.md, choosing-your-approach.md, and cross-reference comparison notes in gsd.md, spec-kit.md, context-engineering.md still need OpenSpec integration

