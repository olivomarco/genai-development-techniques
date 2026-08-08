# August 2026 site refresh brief

**Owner:** Neo  
**Research cutoff:** August 8, 2026  
**Research lead:** Trinity  
**Writer:** Morpheus  
**Reviewer:** Oracle  

## 1. Recommended site taxonomy

Keep the methodology-first comparison and its five current categories:

1. Spec-Driven Development
2. Multi-Agent Orchestration
3. Skill-Based Development
4. Autonomous Iteration
5. Enterprise AI-Native SDLC

Keep Context Engineering as a cross-cutting practice. Add a separate **Skills ecosystem** section for portable skill libraries, authoring systems, registries, discovery tools, and emerging interoperability conventions. This section is supporting market context, not an eleventh Tier 1 technique and not a sixth methodology category.

Represent `mattpocock/skills` as the lead profile on a new `techniques/skills-ecosystem.md` page, subject to Trinity verifying its current purpose, ownership, activity, installation model, supported agents, license, and relationship to other skills catalogs or standards. Compare it with Superpowers as follows:

- **Superpowers:** a development methodology that uses mandatory skills to enforce a workflow.
- **mattpocock/skills:** an ecosystem/library/distribution candidate whose importance may come from reusable skill content and portability, not from prescribing a complete SDLC.

Do not add `mattpocock/skills` to the Tier 1 comparison matrix unless research proves that it defines a transferable end-to-end development methodology with workflow, quality gates, and clear adoption guidance.

## 2. Existing pages to refresh

| File | Required refresh |
|---|---|
| `README.md` | Update the dated snapshot, counts, navigation, and Deep-Dive Documents tables. Add the Skills ecosystem page outside the Tier 1 technique count. |
| `overview.md` | Change the June 2026 framing and all time-sensitive versions, metrics, support claims, and maturity language. Add a compact Skills ecosystem section and revise “Projects to Consider Next.” Keep the accepted complexity spectrum unless evidence justifies a separate decision. |
| `techniques/choosing-your-approach.md` | Add guidance for when to adopt a skills library versus a skills methodology. Update tool-lock-in, combinations, recommendations, and stale market claims. Do not force ecosystem profiles into every methodology score table. |
| `techniques/superpowers.md` | Reverify release, adoption, official integrations, skill format, installation, and ecosystem claims. Add a precise comparison with `mattpocock/skills` and other verified portable-skill efforts. |
| `techniques/context-engineering.md` | Refresh rules-file formats and claims about fragmentation or lack of standardization. Explain skills as a packaging and delivery layer for context, without declaring a universal standard unless primary sources support it. |
| `techniques/gsd.md` | Reverify release, commands, runtime support, popularity, and whether its skill-based runtime packaging has changed since v1.42.3. |
| `techniques/spec-kit.md` | Reverify release, supported agents, extensions, installation, experimental status, and adoption. Check whether skills are now a first-class distribution mechanism. |
| `techniques/openspec.md` | Reverify release, command surface, supported-tool count, workspace claims, maturity, and adoption. Preserve the support-breadth versus runtime-parity caveat. |
| `techniques/bmad.md` | Reverify current release, modules, agents/workflows, Web Bundle scope, license/trademark language, and runtime support. |
| `techniques/squad.md` | Reverify release, state and memory architecture, supported Copilot surfaces, GitHub lifecycle claims, and adoption. |
| `techniques/ralph.md` | Refresh the canonical-method versus active-implementation split, current implementations, backend support, costs, and safety guidance. |
| `techniques/hve.md` | Reverify release status, inventory counts, collections, Copilot surfaces, enterprise examples, and adoption. Avoid treating repository activity as a released capability. |
| `mkdocs.yml` | Add the Skills ecosystem page to navigation and keep labels consistent with README and overview. |

Every deep dive receives a freshness check. Morpheus should make material edits only where Trinity supplies changed evidence.

## 3. Inclusion criteria and bounded candidate list

### Inclusion criteria

A candidate receives a full Tier 1 methodology page only when it has:

1. A transferable method for directing coding agents, not only a product interface.
2. A documented workflow with repeatable artifacts or behaviors.
3. Meaningful quality, verification, or governance mechanisms.
4. Evidence of current maintenance and real adoption.
5. Enough primary documentation to distinguish official behavior from community adaptation.
6. A distinct decision value not already covered by an existing page.

A candidate receives an ecosystem profile when it materially shapes skill authoring, discovery, packaging, portability, or agent runtime practice but does not meet the methodology threshold. Products and runtimes remain in a bounded market/watchlist section unless they expose a distinct portable method.

### Trinity verification queue

Stop after these nine candidates unless Neo approves an expansion:

| Priority | Candidate | Verification question |
|---|---|---|
| Mandatory | `https://github.com/mattpocock/skills` | What exactly is distributed, how is it installed/discovered, which agents consume it, and does it define a methodology or an ecosystem layer? |
| High | Anthropic's canonical Agent Skills documentation/repository | Is there an official portable skill format or reference implementation, and what interoperability claims are documented? |
| High | `skills.sh` and its canonical repository/owner | Is it a registry, installer, ranking site, or standard; what are its provenance and security controls? |
| High | GitHub's official or curated Copilot skills ecosystem, including `github/awesome-copilot` if still canonical | Which skill surfaces are official, which are community content, and how portable are they beyond Copilot? |
| High | OpenSkills and its canonical repository | Does it provide cross-agent installation or compatibility, and is its adoption sufficient for the ecosystem page? |
| Carry-forward | OpenHands | Has it developed a transferable workflow beyond being an autonomous development platform? |
| Carry-forward | Open SWE | Does its asynchronous-agent architecture warrant a methodology profile or only a substrate note? |
| Carry-forward | Goose | Does its extensible runtime expose a reusable software-delivery method? |
| Carry-forward | Cline | Is there a distinct documented methodology beyond SDK, CLI, and IDE product capabilities? |

OpenCode, Aider, Continue, Kilo Code, Roo Code, SWE-agent, AutoGPT, and Pythagora/GPT Pilot remain watchlist-only for this pass. Trinity may mention a material status change but should not research them deeply.

## 4. Files Morpheus may create or update

Morpheus may create:

- `techniques/skills-ecosystem.md`

Morpheus may update:

- `README.md`
- `overview.md`
- `mkdocs.yml`
- `techniques/choosing-your-approach.md`
- `techniques/superpowers.md`
- `techniques/context-engineering.md`
- `techniques/gsd.md`
- `techniques/spec-kit.md`
- `techniques/openspec.md`
- `techniques/bmad.md`
- `techniques/squad.md`
- `techniques/ralph.md`
- `techniques/hve.md`

No additional public page, category, or Tier 1 promotion is in scope without a new decision. Research notes may be added under `.squad/research/`.

## 5. Source, date, and claim standards

- Use **August 8, 2026** as the common observation date. Label later observations separately.
- Prefer primary sources in this order: official documentation, releases/tags, repository files, official announcements, then reputable independent analysis.
- Record the source URL, observation date, release/tag date, and the exact claim each source supports.
- Treat stars, forks, contributors, issue counts, and marketplace installs as dated snapshots, never timeless facts. Round only in public summary tables.
- Separate latest stable release, prerelease/next channel, and unreleased repository activity.
- Distinguish official support, official-but-limited support, community adaptation, readable artifact compatibility, and inferred compatibility.
- Never infer runtime parity from a supported-tools list, bundle, prompt file, or successful installation.
- For skill catalogs, verify provenance, license, update mechanism, installation path, supported agents, conflict resolution, trust/security model, and whether entries are curated or user-submitted.
- Attribute performance, cost, adoption, and outcome claims. Mark anecdotal evidence as anecdotal.
- Do not repeat mutable superlatives such as “largest,” “broadest,” or “most popular” without a defined comparison set and same-day evidence.
- Preserve uncertainty explicitly. Use “not verified” rather than filling gaps with inference.

## 6. Reviewer and build gates

1. **Trinity evidence gate:** Deliver a source table for every changed quantitative, compatibility, maturity, and “current” claim. Include a disposition for all nine candidates.
2. **Neo scope gate:** Approve taxonomy placement before Morpheus creates `techniques/skills-ecosystem.md`. Any Tier 1 promotion requires a separate accepted decision.
3. **Morpheus consistency gate:** Keep README, overview, choosing guide, page counts, category labels, support language, and navigation synchronized. Follow sentence-case headings, active voice, present tense, and scannable formatting.
4. **Oracle claim gate:** Check primary-source traceability, date consistency, support-versus-parity wording, superlatives, and contradictions across pages. Block unsupported claims.
5. **Link gate:** Verify every new external link and every internal navigation link. No dead, redirected-to-unrelated, or ambiguous canonical sources.
6. **Build gate:** Run `python scripts/build_docs.py && mkdocs build --strict`. The refresh is incomplete until the strict build succeeds.
7. **Diff gate:** Confirm that no page outside the authorized file list changed and that generated `docs-staging/` or `site/` artifacts are not committed unless repository policy explicitly requires them.
