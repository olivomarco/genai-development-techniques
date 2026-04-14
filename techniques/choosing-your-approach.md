# Choosing Your Approach

How to pick the right AI-assisted development technique for your situation. This guide is organized by real-world scenarios — find yours, get a recommendation, understand the trade-offs.

---

## How to Use This Guide

Each technique page in this repo covers **what** a technique is and **how** it works. This page answers the question nobody else does clearly: **when should I use which one?**

Jump to the scenario that matches your situation:

- [By Team Size](#by-team-size) — Solo, small team, medium team, large organization
- [By Project Type](#by-project-type) — Greenfield, brownfield, prototype, migration
- [By Industry & Compliance](#by-industry--compliance) — Regulated environments, auditable systems
- [By Development Activity](#by-development-activity) — Bug fixes, features, refactoring, tests, docs
- [By Development Methodology](#by-development-methodology) — Agile/Scrum, Kanban, waterfall-adjacent
- [Quick Decision Flowchart](#quick-decision-flowchart) — Don't want to read? Start here.

---

## Quick Decision Flowchart

```text
START: What are you building?
│
├─ Quick fix / small task (< 1 hour of work)?
│   └─→ Context Engineering (rules files) + direct prompting
│       No framework needed. Write a good copilot-instructions.md / CLAUDE.md.
│
├─ Solo project, clear requirements?
│   ├─ Want to run it overnight / AFK?
│   │   └─→ Ralph
│   ├─ Want skills-based methodology with TDD?
│   │   └─→ Superpowers
│   ├─ Want structured phases with verification?
│   │   └─→ GSD (if Claude Code) or Spec Kit (if multi-tool)
│   ├─ Want a persistent AI team with memory?
│   │   └─→ Squad (if Copilot)
│   └─ Want full agile simulation?
│       └─→ BMAD
│
├─ Team of 2-5, using GitHub?
│   ├─ Already on Copilot?
│   │   └─→ Squad
│   ├─ Mixed tools (Claude Code + Cursor + Copilot)?
│   │   └─→ BMAD, Spec Kit + Context Engineering, or Superpowers
│   └─ Mainly Claude Code?
│       └─→ GSD
│
├─ Team of 5-15, enterprise product?
│   ├─ Regulated / auditable?
│   │   └─→ HVE (if on Copilot) or BMAD + custom governance
│   ├─ GitHub-centric workflow?
│   │   └─→ Squad + HVE collections
│   └─ Multi-tool environment?
│       └─→ BMAD + Context Engineering
│
└─ Large org / multiple teams?
    └─→ HVE + Context Engineering as foundation
        Add Squad per-team if using Copilot
```

---

## By Team Size

### Solo Developer

You're one person. You need to maximize output while maintaining quality. The overhead of any technique must be justified by productivity gains, not ceremony.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Context Engineering** | ★★★★★ | Start here. A good rules file (copilot-instructions.md, .cursorrules, CLAUDE.md) costs nothing and improves every session. Zero overhead. |
| **Ralph** | ★★★★★ | Perfect for solo. Set it running, go to bed, wake up to progress. Requires clear specs and a test suite as backpressure. Best for greenfield. |
| **GSD** | ★★★★☆ | Excellent if you use Claude Code. The 6-step workflow prevents the "context rot" that kills long solo sessions. Parallel agent execution makes one person feel like three. |
| **Spec Kit** | ★★★★☆ | Good if you use multiple tools. Lighter than GSD, focused on getting the spec right before building. GitHub-backed, agent-agnostic. |
| **BMAD** | ★★★☆☆ | Can feel ceremonial for one person — PM, Architect, Dev, QA agents simulating a team you don't have. The Quick Flow mode helps. Best when your project is complex enough that you'd benefit from the discipline of separate analysis, planning, and architecture phases. |
| **Squad** | ★★★★☆ | Squad's "team" is AI agents, not humans — a solo developer gets a coordinated team of specialized agents with persistent memory, parallel fan-out, and Ralph for autonomous work monitoring. Requires Copilot and benefits most when using GitHub Issues. |
| **Superpowers** | ★★★★★ | Built for this — skills-based discipline for individual developers. Composable behavioral skills enforce TDD, code review, and systematic workflows. 151K stars, multi-tool support (Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode). |
| **HVE** | ★☆☆☆☆ | 49 agents, 102 instructions, enterprise governance. Unless you're a solo developer shipping regulated software, this is a sledgehammer for a nail. |

**What real users say:**
- Geoffrey Huntley (Ralph creator): "Ralph can replace the majority of outsourcing at most companies for greenfield projects." He built an entire programming language (CURSED) solo using Ralph — compiler, stdlib, LLVM backend.
- Y Combinator hackathon teams: "We put a coding agent in a while loop and it shipped 6 repos overnight" for $297 in API costs.
- Birgitta Böckeler (Thoughtworks): On spec-driven approaches for small tasks — "the time spent reviewing generated specification files was comparable to the time spent just coding directly." Context engineering via rules files is often enough.

**Recommended starting point:** Context Engineering (rules files) → add GSD, Squad, Superpowers, or Ralph depending on your tool and project size.

---

### Small Team (2–3 People)

You know each other well, communication is natural, but you need AI agents that don't step on each other's toes. Coordination overhead must be minimal.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Context Engineering** | ★★★★★ | Non-negotiable. Shared rules files in the repo mean every team member's AI sessions follow the same conventions. This is your minimum viable coordination. |
| **GSD** | ★★★★☆ | Each person runs their own GSD workflow on different features. Parallel execution within GSD, plus human parallelism across features. Works well if the whole team is on Claude Code. |
| **Spec Kit** | ★★★★☆ | Shared specs in the repo give everyone a common source of truth. Agent-agnostic — one person can use Copilot while another uses Claude Code. The specs coordinate, not the tools. |
| **BMAD** | ★★★★☆ | The team simulation starts to make more sense. One person can run the PM/Architect phases while another starts implementation. Quick Flow keeps it light for small tasks. |
| **Squad** | ★★★★☆ | Strong fit if you're on Copilot. The Coordinator routes work across specialized AI agents, persistent memory keeps decisions consistent across sessions, and Ralph automates issue triage and backlog management. The .squad/ setup is automated — the Coordinator handles assembly. |
| **Ralph** | ★★★☆☆ | Individual team members can Ralph independently on separate branches. No built-in team coordination — you'll need to handle merge conflicts yourself. |
| **Superpowers** | ★★★☆☆ | No built-in team coordination — each person runs independently with their own skills. Individual discipline is excellent, but you'll need external coordination for shared work. |
| **HVE** | ★★☆☆☆ | Still too heavy. The RPI workflow adds value for complex features, but 49 agents and 102 instructions are designed for larger organizations. |

**What real users say:**
- Martin Fowler's blog: SDD tools like Spec Kit work best when both team members can review specs before implementation — the shared spec becomes a communication artifact, not just an AI input.
- BMAD community: Small teams report the biggest value from the Analysis and Solutioning phases — having "Winston" (Architect) challenge technical decisions catches issues before they become expensive.

**Recommended starting point:** Context Engineering + Spec Kit or GSD (depending on tool choice).

---

### Medium Team (4–10 People)

Now coordination matters. You have multiple concerns (frontend, backend, testing, infra), people specialize, and the "just talk to each other" approach hits limits. AI agents need to be aware of team decisions.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Squad** | ★★★★★ | This is Squad's sweet spot. Named agents with charters map to real team concerns. The decisions ledger ensures AI agents respect past choices. Ralph monitors the GitHub board. Parallel fan-out reflects real team parallelism. |
| **BMAD** | ★★★★★ | Also a sweet spot. 12+ agent personas cover every role a medium team needs. Scale-adaptive intelligence adjusts process weight automatically. The full agile simulation (sprints, retros, stories) maps to how medium teams actually work. |
| **HVE** | ★★★★☆ | The RPI workflow starts to pay off as task complexity increases. Research-first philosophy prevents expensive rework. Still heavy on setup, but the governance layer is increasingly justified. |
| **Context Engineering** | ★★★★☆ | Still essential as a foundation, but no longer sufficient alone. You need a framework on top to coordinate multi-person, multi-concern work. |
| **GSD** | ★★★☆☆ | Good for individual contributors within the team, but no built-in team coordination. Each person runs GSD independently — you need something else (Squad, BMAD, or your own process) for cross-team orchestration. |
| **Spec Kit** | ★★★☆☆ | Useful for the specification phase, but you'll pair it with another technique for execution and coordination. |
| **Ralph** | ★★☆☆☆ | Individual contributors can still use Ralph for well-scoped tasks, but it offers nothing for team coordination. Teams using Ralph typically assign separate repos or features to separate Ralph loops. |
| **Superpowers** | ★★☆☆☆ | No team coordination features. Individual contributors can use Superpowers for their own tasks, but the framework has no mechanisms for cross-team orchestration or shared governance. |

**What real users say:**
- thomy.tech (on Squad): "My First Coding Agent Fleet with Enterprise Tooling" — described running Squad with multiple agents handling different aspects of a project simultaneously, with persistent memory keeping everything aligned.
- BMAD community (Discord): Teams of 5-8 report the scale-adaptive intelligence actually works — it doesn't force enterprise process on a simple feature branch.

**Recommended starting point:** Squad (if Copilot) or BMAD (if multi-tool) + Context Engineering as foundation.

---

### Large Team / Organization (10+ People, Multiple Teams)

Governance, consistency, audit trails, and onboarding matter. You can't rely on tribal knowledge — new people join and need to be productive with AI agents immediately. Different teams may have different needs.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | Designed for this. 49 agents, 102 instructions, collection-based architecture. Teams adopt the collections they need (coding-standards, security, data-science). Enterprise governance, validated artifacts, policy-as-code. Microsoft ISE built this from shipping 140+ enterprise projects. |
| **Context Engineering** | ★★★★★ | The foundation layer. Organization-wide rules files standardize AI behavior across all teams. Layer 2 (organization rules) in the 8-layer model is specifically for this. |
| **BMAD** | ★★★★☆ | The Module Ecosystem (BMB, TEA, BMGD, CIS) scales to enterprise needs. Cross-platform support means teams using different tools can still use the same methodology. The 44K-star community provides extensive resources. |
| **Squad** | ★★★★☆ | Per-team Squad instances work well. Each team has its own .squad/ with its own agents, decisions, and routing. The SDK-first mode (squad.config.ts) is more enterprise-friendly than Markdown-only configuration. |
| **Spec Kit** | ★★★☆☆ | The constitution.md concept (project principles and guardrails) scales well for enforcing organizational standards. Pair with a heavier framework for execution. |
| **GSD** | ★★☆☆☆ | Individual contributor tool within a larger framework. Not designed for organizational coordination. |
| **Superpowers** | ★★☆☆☆ | No governance or team features. Individual contributors can adopt Superpowers skills for personal workflows, but the framework provides no organizational coordination or audit capabilities. |
| **Ralph** | ★☆☆☆☆ | No governance, no audit trail, no team coordination. An organization using Ralph needs extensive wrapping and oversight. |

**What real users say:**
- Robin Cole (VP Engineering, Microsoft) on HVE at TMForum: Enterprise adoption by AT&T and KT Corporation demonstrates viability at scale for telco-grade software.
- Birgitta Böckeler on harness engineering: "What's good for humans is good for AI" — organizations should invest in architectural constraints (custom linters, structural tests, context documentation) as "harnesses" that make AI agents more reliable. HVE's collection architecture implements this.

**Recommended starting point:** HVE (if on Copilot) or BMAD (if multi-tool) + Context Engineering as organizational standard.

---

## By Project Type

### Greenfield (Starting from Scratch)

Every technique works for greenfield — but some shine brighter.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★★ | Ideal for greenfield. Fresh context per iteration, clear specs, no legacy baggage. Ralph excels when starting from scratch with well-defined requirements. |
| **GSD** | ★★★★★ | The 6-step lifecycle (new → discuss → plan → execute → verify → complete) is designed for starting from nothing. Parallel wave execution builds multiple concerns simultaneously. |
| **BMAD** | ★★★★☆ | The Analysis phase (domain research, market research, technical research) is most valuable at greenfield stage when the problem space is poorly understood. |
| **Spec Kit** | ★★★★☆ | Constitution → specify → plan → tasks → implement maps naturally to the "blank slate" starting point. |
| **Squad** | ★★★★☆ | Team assembly, initial architecture decisions, and parallel agent fan-out are effective for scaffolding new projects. |
| **Superpowers** | ★★★★★ | Brainstorm→plan→implement with TDD enforcement. Parallel development via worktrees. Skills ensure disciplined greenfield development from the first commit. |
| **HVE** | ★★★☆☆ | Works, but the Research phase is less valuable when there's no existing codebase to investigate. More valuable later as the codebase grows. |
| **Context Engineering** | ★★★☆☆ | Essential but thin at the start — your rules file gets more valuable as the project evolves and conventions accumulate. |

### Brownfield (Existing Codebase)

Working with existing code is harder for AI. The agent needs to understand what's already there — and not duplicate or break it.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | The Research phase shines here. The AI investigates the existing codebase, documents findings, then plans changes. This prevents the "AI regenerated existing code" problem. |
| **Context Engineering** | ★★★★★ | Critical. A detailed rules file describing your existing architecture, conventions, and gotchas is the single most impactful thing you can do for brownfield AI work. |
| **GSD** | ★★★★☆ | Has explicit Brownfield Support mode. Fresh context per task prevents accumulated confusion about the existing codebase. |
| **BMAD** | ★★★★☆ | The Analysis phase can study the existing domain before changes begin. Scale-adaptive intelligence adjusts to task size within the existing codebase. |
| **Spec Kit** | ★★★☆☆ | The analyze command checks for inconsistencies, but in brownfield testing, spec-driven tools have been observed taking existing class descriptions as new specifications and generating duplicates. Careful scoping is needed. |
| **Squad** | ★★★☆☆ | Persistent agent memory helps — agents remember past decisions about the codebase. But the initial context loading needs careful setup. |
| **Superpowers** | ★★★★☆ | Systematic debugging skills and root-cause-tracing help navigate existing codebases. Skills can be customized for codebase-specific patterns. |
| **Ralph** | ★★☆☆☆ | Ralph's own documentation cautions against brownfield use. The nondeterministic ripgrep search problem is worst in brownfield — Ralph may conclude code hasn't been implemented when it has, creating duplicates. Community reports are emerging for brownfield use, but it remains risky. |

### Rapid Prototyping / Hackathons

Speed is everything. Polish later (or never).

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★★ | Y Combinator teams proved it: 6 repos overnight for $297. Set the loop, let it rip. |
| **Context Engineering** | ★★★★☆ | A quick rules file that sets the tech stack and coding style is enough. Don't overthink it. |
| **GSD** | ★★★☆☆ | Quick Mode compresses the workflow, but even the compressed version adds ceremony that slows down hackathon pace. |
| **Superpowers** | ★★★☆☆ | TDD enforcement adds ceremony that can slow hackathon pace. The skills framework is valuable for disciplined prototyping, but pure speed favors lighter approaches. |
| **Spec Kit** | ★★☆☆☆ | Spec-plan-tasks-implement is too many steps when you want code running in hours. |
| **BMAD** | ★★☆☆☆ | Quick Flow helps, but PM → Architect → Dev → QA phases are overkill for a prototype. |
| **Squad** | ★★☆☆☆ | Team assembly and casting add setup time. For a hackathon, the persistent memory and coordination aren't worth the upfront cost. |
| **HVE** | ★☆☆☆☆ | Research → Plan → Implement → Review is the opposite of "move fast and break things." |

### Migration / Refactoring

You're moving from one stack/pattern to another. The existing code is the input; the new code is the output.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★☆ | Migrations are mechanical — exactly the kind of repetitive, well-defined work Ralph excels at. A GSD community report describes a production iOS-to-Android port in 3 days. Combine with clear specs defining the "from" and "to." |
| **HVE** | ★★★★☆ | Research phase documents the existing system. Plan phase maps the migration path. Implement phase executes task-by-task with verification. |
| **GSD** | ★★★★☆ | The parallel wave execution is valuable for migrations with many independent modules to port. |
| **Context Engineering** | ★★★★☆ | Critical to document "old patterns → new patterns" in rules files so the AI consistently applies the transformation. |
| **BMAD** | ★★★☆☆ | The Analyst agent can study the existing system. But the full agile simulation may be overkill for a mechanical migration. |
| **Spec Kit** | ★★★☆☆ | Spec the migration requirements clearly. Constitution can enforce "always use new patterns." |
| **Superpowers** | ★★★☆☆ | Skills can be customized for migration patterns. The systematic approach helps, but Superpowers lacks migration-specific tooling. |
| **Squad** | ★★★☆☆ | Useful if the migration touches multiple concerns (frontend migration + backend migration + test migration in parallel). |

---

## By Industry & Compliance

### Regulated Environments

Industries where audit trails, compliance evidence, and validated artifacts are non-negotiable. Mistakes have legal or safety consequences.

**Examples:**
- **Financial services** — SOX compliance, SEC reporting requirements, PCI-DSS for payment systems. Every code change affecting financial calculations needs traceability from requirement to implementation to test.
- **Healthcare / Life sciences** — HIPAA compliance, FDA software validation (21 CFR Part 11), GxP requirements. AI-generated code must be verifiable and its provenance documented.
- **Government / Defense** — FedRAMP, NIST 800-53, ITAR restrictions. Security clearances may restrict which cloud-based AI tools can be used at all.
- **Automotive** — ISO 26262 (functional safety), ASPICE. Safety-critical software requires formal verification and evidence chains.
- **Aerospace** — DO-178C (airborne software). Every line of code needs traceability to requirements. Modified Condition/Decision Coverage (MC/DC) for Level A software.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | Purpose-built for this. Constraint-based workflows, validated artifacts, supply-chain security (SBOM generation, attestation, OpenSSF Scorecard, CodeQL). The RPI workflow creates an evidence chain: Research documents → Plan → Implementation → Review. Collections for security and RAI (Responsible AI) planning. Enterprise adoption by telcos demonstrates regulated-industry viability. |
| **Context Engineering** | ★★★★★ | Constraint context in rules files (Layer 5 — "what the agent must NOT do") is essential for regulated environments. Document forbidden patterns, security requirements, and compliance gates in version-controlled rules files that every AI session respects. |
| **BMAD** | ★★★☆☆ | Structured phases provide some process evidence, but no built-in compliance artifacts or policy enforcement. You'd need to add governance layers on top. |
| **Spec Kit** | ★★★☆☆ | The constitution.md concept can encode compliance requirements. Version-controlled specs provide some traceability. But no enforcement mechanism — the AI may still ignore the constitution. |
| **GSD** | ★★☆☆☆ | Verification gates help, but no formal audit trail, no compliance artifacts, no policy-as-code. |
| **Squad** | ★★☆☆☆ | The reviewer rejection protocol and decisions ledger provide some governance, but not at the level regulated industries require. |
| **Superpowers** | ★★☆☆☆ | TDD enforcement provides some structure, but no audit trails, governance mechanisms, or compliance artifacts. Every change would still need manual compliance review. |
| **Ralph** | ★☆☆☆☆ | Zero governance, zero audit trail. "Deterministically bad in a nondeterministic world" is not a phrase you want in a compliance review. Every change would need human review before landing, which negates Ralph's AFK advantage. |

**Real-world guidance for regulated environments:**
1. **Never skip the research phase.** Whether using HVE's formal Research agent or doing it manually, the AI must investigate before implementing. As HVE's docs state: "When AI knows it cannot implement, it stops optimizing for 'plausible code' and starts optimizing for 'verified truth.'"
2. **Invest in harness engineering.** Deterministic custom linters, structural tests, and architectural constraints create a safety net that doesn't depend on LLM compliance. The AI can hallucinate, but the harness catches it.
3. **Pin model versions.** Context engineering research shows: "Production applications should pin to specific model snapshots, as router behavior changes between versions." For regulated environments, model version changes should go through the same change control as code changes.
4. **Never trust AI self-reports.** GSD's verification gates and HVE's Review phase both check against the actual codebase, not the AI's claims. For regulated environments, this is non-negotiable.

### Non-Regulated / Internal Tools / Startups

Lower compliance burden, higher tolerance for iteration, speed matters more than ceremony.

Any technique works. Choose based on team size and project type (see above). The key question is: **how much structure justifies its overhead?**

- **If speed matters most:** Ralph, GSD, or Superpowers
- **If you want process without governance:** BMAD, Squad, or Superpowers
- **If you're building a culture:** Context Engineering as foundation, pick a framework as the team grows

---

## By Development Activity

Not every task needs the same technique. Many teams use different approaches for different types of work.

### Bug Fixes

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small, clear bug | Direct prompting + Context Engineering | For small, well-scoped bugs, spec-driven tools add overhead that exceeds the task effort. Just describe the bug, let the agent fix it. |
| Complex, multi-file bug | GSD or HVE (Research phase) | When the bug touches multiple systems, the research-first approach prevents the AI from "fixing" the wrong thing. Superpowers' systematic debugging skills and root-cause-tracing also help here. |
| Recurring bug pattern | Context Engineering | Add the pattern to your rules file: "When you see error X, the cause is usually Y, not Z." Future AI sessions benefit. |

### Feature Development

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small feature (< 1 day) | GSD Quick Mode or Spec Kit | Just enough structure to prevent scope creep without heavy ceremony. |
| Medium feature (1-5 days) | GSD, BMAD Quick Flow, Squad, or Superpowers | The planning and verification phases pay off as complexity increases. Superpowers' TDD enforcement ensures quality throughout. |
| Large feature (weeks+) | BMAD (full), Squad (full), or HVE | You need structured phases, quality gates, and persistent memory across sessions. |

### Test Generation

| Approach | Recommendation | Why |
|----------|---------------|-----|
| Bulk test generation | Ralph | The quintessential Ralph task: mechanical, well-defined, repetitive. Run overnight, wake up to coverage. |
| Test-driven development | GSD, Superpowers, or direct prompting | Write the test spec first, then let the AI implement. Superpowers enforces TDD as a mandatory skill. |
| Enterprise test suites | BMAD TEA (Test Architect module) | Risk-based testing with structured QA agent involvement. |

### Documentation

| Approach | Recommendation | Why |
|----------|---------------|-----|
| API docs, READMEs | Ralph or direct prompting | Mechanical documentation from code is a perfect AFK task. |
| Architecture docs | BMAD or HVE | Need the analysis/research phase to produce accurate architecture documentation. |
| Spec documentation | Spec Kit | The specs themselves become living documentation. |

### Refactoring

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small refactors | Direct prompting | Rename, extract method, simplify — these don't need a framework. |
| Large refactors | GSD (parallel waves), BMAD, or Superpowers | Multi-file refactors benefit from phase separation and parallel execution. Superpowers' systematic skills help maintain consistency. |
| Architecture migration | HVE + Context Engineering | Research the existing architecture, plan the migration, implement with verification. |

---

## By Development Methodology

### Agile / Scrum Teams

Running sprints with stand-ups, retrospectives, and backlog grooming.

| Technique | Fit | Why |
|-----------|-----|-----|
| **BMAD** | ★★★★★ | BMAD *is* agile simulation. Sprint planning, stories, retrospectives, QA cycles — it maps 1:1 to Scrum. The Scrum Master agent facilitates ceremonies. |
| **Squad** | ★★★★☆ | Ceremonies (design reviews, retros, standups) are built-in. Ralph monitors the GitHub backlog continuously. The issue → branch → PR → merge lifecycle integrates with sprint-based work. |
| **HVE** | ★★★★☆ | The RPI workflow maps to sprint tasks: Research and Plan early in the sprint, Implement mid-sprint, Review at the end. Collections for GitHub, ADO, and Jira integrate with existing backlog tools. |
| **GSD** | ★★★☆☆ | The 6-step workflow maps to individual sprint tasks, but GSD has no sprint-level coordination. Use within sprints, not to manage them. |
| **Spec Kit** | ★★★☆☆ | Specs can map to user stories. The constitution can encode sprint conventions. But Spec Kit doesn't manage sprint process. |
| **Context Engineering** | ★★★☆☆ | Rules files can encode sprint conventions ("always reference the Jira ticket in commit messages"), but won't manage agile process. |
| **Ralph** | ★★☆☆☆ | Can be used for specific sprint tasks, but has no concept of sprints, backlogs, or ceremonies. |
| **Superpowers** | ★★★☆☆ | Individual agent workflow, not team process. Skills work well for sprint task execution but Superpowers has no sprint-level coordination or ceremonies. |

### Kanban / Continuous Flow

Work-in-progress limits, continuous delivery, no sprints.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Squad** | ★★★★★ | Ralph (Work Monitor) continuously scans for work and routes it — this IS Kanban for AI agents. No sprint boundaries, just a flowing board. |
| **GSD** | ★★★★☆ | Each ticket/card runs through the 6-step workflow independently. No sprint coupling. |
| **Context Engineering** | ★★★★☆ | Rules files define the "how," the Kanban board defines the "what." Lightweight and flow-compatible. |
| **Ralph** | ★★★★☆ | The autonomous loop is inherently continuous. Pair with a GitHub Issues board for visual tracking. |
| **Superpowers** | ★★★☆☆ | Individual workflow fits continuous flow. Skills execute per-card naturally. No batch-like overhead, but no board-level awareness. |
| **BMAD** | ★★★☆☆ | Scale-adaptive intelligence adjusts, but the phases imply batching that conflicts with true continuous flow. |
| **Spec Kit** | ★★★☆☆ | Works per-card, but the multi-step workflow adds batch-like overhead. |
| **HVE** | ★★☆☆☆ | The RPI phases imply sequential processing that fights continuous flow. |

### Waterfall-Adjacent / Stage-Gate

Sequential phases with formal gate reviews between them.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | RPI *is* stage-gate: Research → gate → Plan → gate → Implement → gate → Review. Validated artifacts at each gate. |
| **BMAD** | ★★★★★ | Four sequential phases (Analysis → Planning → Solutioning → Implementation) with quality gates between each. |
| **Spec Kit** | ★★★★☆ | Constitution → specify → plan → tasks → implement is a natural stage pipeline. |
| **GSD** | ★★★☆☆ | The 6-step workflow is sequential, but designed for iteration within phases rather than strict gates. |
| **Squad** | ★★☆☆☆ | More about parallel coordination than sequential phases. Can enforce phase gates through ceremonies, but it's not native. |
| **Ralph** | ★☆☆☆☆ | The antithesis of stage-gate. No phases, no gates, just a loop. |
| **Superpowers** | ★★☆☆☆ | Skills provide structure within tasks, but no formal phase gates or validated artifacts between stages. |
| **Context Engineering** | ★★☆☆☆ | Supports any process but provides no process of its own. |

---

## Combining Techniques

Most real teams don't use a single technique in isolation. Here are battle-tested combinations:

### Context Engineering + Any Framework

**Every** framework benefits from well-maintained rules files. Context Engineering is the foundation layer — always use it, even if you're "just" doing Ralph loops.

### Spec Kit + GSD or Squad

Use Spec Kit for the specification and planning phase, then hand off to GSD (for execution with parallel waves) or Squad (for multi-agent team execution). Spec Kit is deliberately narrow — it handles specs, not execution.

### Ralph + GSD

Use GSD's structured planning to create the spec and task breakdown. Then use Ralph to execute the tasks autonomously overnight. Ralph's prompt.md can reference GSD's planning artifacts.

### BMAD + Context Engineering

BMAD provides the process; Context Engineering provides the persistent context. Use BMAD's Agent personas with rich rules files that accumulate project knowledge across sessions.

### HVE + Squad (Enterprise Copilot shops)

HVE provides the governance and methodology. Squad provides the team coordination and work monitoring. Use HVE's collections for domain standards and Squad's agents for execution.

### Superpowers + Context Engineering

Superpowers is arguably the most sophisticated implementation of context engineering — skills *are* context engineering, packaged as composable behavioral modules. The two are deeply complementary: use context engineering rules files to set project-level conventions, and Superpowers skills to enforce development methodology (TDD, code review, debugging workflows).

### Superpowers + Squad

Use Superpowers for individual agent skill development within Squad's team coordination. Each Squad agent can be enhanced with Superpowers skills for disciplined task execution, while Squad handles the cross-agent orchestration, persistent memory, and work routing that Superpowers lacks.

---

## Anti-Patterns: When NOT to Use a Technique

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Using HVE or BMAD for a 30-minute bug fix | Framework overhead exceeds the task effort. For small, well-scoped tasks, direct prompting with good context engineering is faster and more effective. |
| Using Ralph in a large brownfield codebase without safeguards | Nondeterministic ripgrep searches lead to duplicate code and incorrect assumptions about what exists. Ralph's own documentation cautions against brownfield use without safeguards. |
| Using any SDD tool for exploratory prototyping | When you don't know what you're building yet, the time spent reviewing generated specification files can be comparable to the time spent just coding directly. Specs create drag during exploration. |
| Using Ralph without a test suite | Tests are Ralph's backpressure. Without them, the loop has no quality gate and will drift indefinitely, burning API credits on garbage. |
| Using GSD without Claude Code | GSD is built on native Claude Code features (sub-agents, slash commands, hooks). Community ports exist but lose the tight integration that makes GSD effective. |
| Forcing one technique on a team with mixed tools | If half the team uses Claude Code and half uses Copilot, mandating GSD or Squad creates friction. Use Spec Kit or BMAD (agent-agnostic) as the shared layer, individual tools beneath. |
| Using Superpowers for team coordination | Superpowers enhances individual agent workflows, not team orchestration. For team coordination, use Squad or BMAD. Superpowers can complement these frameworks for individual task execution. |

---

## Cost Considerations

AI-assisted development costs money — API credits, subscriptions, compute. The cost profile varies dramatically by technique.

| Technique | Cost Profile | Notes |
|-----------|-------------|-------|
| **Context Engineering** | Lowest | Just rules files. No additional API cost beyond your normal tool usage. |
| **Spec Kit** | Low | Additional tokens for spec generation and planning, but human-driven pace limits spend. |
| **GSD** | Medium | Multiple parallel agents per wave consumes API credits faster. Typical: several dollars per phase. |
| **BMAD** | Medium | Multiple agent personas, but human-paced interaction limits total spend. |
| **Squad** | Medium–High | Parallel fan-out of background agents, persistent agent spawning, Scribe logging. Multiple agents per user request. |
| **Superpowers** | Medium | Subagent-per-task model consumes API credits, but skills keep context lean (~2K token bootstrap). Comparable to GSD in cost profile. |
| **HVE** | Medium | The RPI phases are sequential (one agent at a time), limiting parallel cost. But enterprise-scale usage adds up. |
| **Ralph** | Variable — can be HIGH | A 50-iteration loop on a large codebase: $50-100+ per run. Overnight AFK runs with Opus-class models can exceed $200. Set cost limits and max-iteration caps. |

---

## Tool Lock-In Matrix

An important practical concern: which techniques lock you into which AI coding tools?

| Technique | Primary Tool | Works With | Hard Blocker |
|-----------|-------------|-----------|--------------|
| **Context Engineering** | Any | All tools | None — universal practice |
| **Ralph** | Any CLI | Claude Code, Copilot CLI, Cursor CLI, Codex, Gemini CLI | Needs CLI mode — doesn't work in IDE-only tools |
| **Spec Kit** | Any | Copilot, Claude Code, Cursor, Windsurf, Gemini CLI | None — agent-agnostic by design |
| **BMAD** | Claude Code, Cursor, Windsurf | Most tools via V6 cross-platform support | None (V6 broadened support) |
| **GSD** | Claude Code | Community ports for Cursor, others | Best experience requires Claude Code's native features |
| **Superpowers** | Claude Code | Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode | Needs CLI mode for bootstrapping |
| **Squad** | GitHub Copilot | Copilot CLI + VS Code | Does not work with Claude Code, Cursor, or other tools |
| **HVE** | GitHub Copilot | VS Code extension only | Tightly coupled to Copilot — no other tool support |

---

## Summary: The One Table

For the reader who just wants one definitive recommendation per scenario:

| Scenario | Primary Recommendation | Runner-Up |
|----------|----------------------|-----------|
| Solo dev, quick project | Context Engineering + Ralph | GSD or Superpowers |
| Solo dev, serious project | GSD (Claude Code) or Squad (Copilot) | Superpowers or BMAD |
| Small team (2-3), multi-tool | Spec Kit + Context Engineering | BMAD |
| Small team (2-3), Copilot | Squad | GSD |
| Medium team (4-10) | Squad (Copilot) or BMAD (multi-tool) | HVE |
| Large org (10+) | HVE + Context Engineering | BMAD |
| Regulated environment | HVE | BMAD + custom governance |
| Greenfield | Ralph or GSD | Superpowers or BMAD |
| Brownfield | HVE or Context Engineering | GSD (brownfield mode) |
| Hackathon / prototype | Ralph | Direct prompting |
| Migration / refactoring | Ralph (mechanical) or HVE (complex) | GSD |
| Agile / Scrum | BMAD or Squad | HVE |
| Kanban / continuous flow | Squad (Ralph monitor) | GSD |
| Bug fixes | Direct prompting + Context Engineering | GSD Quick Mode |
| Overnight / AFK work | Ralph | Squad (Ralph monitor) |
