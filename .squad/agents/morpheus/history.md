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

