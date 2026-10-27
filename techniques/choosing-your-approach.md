# Choosing your approach

Choose an AI-assisted development technique based on your team, project, and task. The tables explain each recommendation and its trade-offs.

---

## How to use this guide

The technique pages explain what each approach does and how it works. This guide explains when to use it.

Jump to the scenario that matches your situation:

- [Layer Check: Model, Runtime, or Methodology First?](#layer-check-model-runtime-or-methodology-first) — Place your situation in the stack before picking a row below
- [By Team Size](#by-team-size) — Solo, small team, medium team, large organization
- [By Project Type](#by-project-type) — Greenfield, brownfield, prototype, migration
- [By Industry & Compliance](#by-industry-compliance) — Regulated environments, auditable systems
- [By Development Activity](#by-development-activity) — Bug fixes, features, refactoring, tests, docs
- [By Development Methodology](#by-development-methodology) — Agile/Scrum, Kanban, waterfall-adjacent
- [Skills, in Brief](#skills-in-brief) — Choose a skills category and find the detailed decision guide
- [Quick Decision Flowchart](#quick-decision-flowchart) — A short route to a starting recommendation

---

## Layer check: model, runtime, or methodology first?

Before matching a row in the tables below, place your situation in the [three-layer model](../overview.md#the-three-layer-model-model-runtime-methodology): model capability, execution runtime/harness, and development methodology. The techniques in this repo are all methodology-layer choices — but a methodology is not always the layer that's missing.

Frontier models in first-party runtimes (Claude Code, Codex CLI, GitHub Copilot) increasingly handle bounded, clearly specified tasks without an added methodology. Tests, lint, or a reviewable diff provide independent checks. The runtime still assembles context, calls tools, recovers from errors, and enforces permissions. It handles more of this work for you than a thin generic harness such as [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent).

Work through this order before adding anything:

1. **Model + native runtime first.** Start with the frontier model you have and its own CLI or IDE integration. For a task that's bounded, clearly specified, and independently checkable, this is frequently enough on its own — no framework required.
2. **Add skills when expertise is missing.** If the model keeps missing a convention, domain pattern, or house style it can't infer from the repo, use a skill or rules file to supply it (see [Context Engineering](context-engineering.md)).
3. **Add a methodology when coordination or traceability is missing.** If the task spans multiple agents, multiple people, or needs a reconstructable record of *why* a decision was made, that's the signal to adopt GSD, Squad, BMAD, HVE, or another Tier 1 technique from this comparison.
4. **Strengthen controls as risk rises.** Governance, audit trails, approval gates, and cost caps should scale with autonomy, task duration, blast radius, and compliance exposure — not be the default starting posture for every task.

For a quick solo project, the tables suggest Context Engineering + Ralph as a low-overhead option. HVE or Squad adds value when coordination or governance needs justify the setup. See [Anti-Patterns](#anti-patterns-when-not-to-use-a-technique) for cases where a framework adds unnecessary work.

---

## Skills, in brief

"Skills" covers at least six structurally different things — a specification, composable libraries, lifecycle libraries, orchestrating modes, skill-driven methodologies, and native runtimes/custom catalogs — and a skill package is not automatically a development methodology. The short version:

| If you want... | Reach for... |
|----------------|--------------|
| A handful of practices you select and adapt yourself | A composable library such as `mattpocock/skills` |
| Skills mapped to lifecycle stages, without a mandatory gate | A lifecycle library such as `addyosmani/agent-skills` |
| Automatic request routing across a library's skills | An orchestrating mode such as `pstack/poteto-mode` |
| A mandatory individual workflow with TDD and review enforcement | A skill-driven methodology — [Superpowers](superpowers.md) |
| Team-scale coordination or enterprise governance, with skills as one ingredient | A multi-agent/runtime approach — [Squad](squad.md) or [HVE](hve.md) |

You can combine a library, orchestrating mode, or methodology with a specification framework. See [Choosing a Skills Approach](skills-choosing.md) for selection criteria, [State of the Skills Market](skills-ecosystem.md) for the taxonomy, [Skill Libraries](skills-libraries.md) and [Orchestrating Modes](skills-orchestrating-modes.md) for examples, and [Distribution and Governance](skills-management.md) for installation and provenance.

---

## Quick decision flowchart

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
│   │   └─→ GSD Core or Spec Kit
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
│   └─ Want a five-step project workflow?
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

## By team size

### Solo developer

For solo work, choose a technique whose planning and verification benefits justify its setup and process overhead.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Context Engineering** | ★★★★★ | Start with a rules file (copilot-instructions.md, .cursorrules, CLAUDE.md) to record conventions for future sessions. No framework setup required. |
| **Ralph** | ★★★★★ | Supports unattended solo work with clear specs and a test suite as backpressure. Best for greenfield; progress is not guaranteed. |
| **GSD** | ★★★★☆ | The five-step Discuss → Plan → Execute → Verify → Ship workflow uses fresh context to address context rot. The installer targets multiple runtimes, though feature parity is unverified. |
| **Spec Kit** | ★★★★☆ | Good if you use multiple tools. Lighter than GSD, focused on getting the spec right before building. GitHub-backed, agent-agnostic. |
| **OpenSpec** | ★★★★☆ | Strong for brownfield solo work. Change folders and delta specs help you make targeted changes without turning every task into a full project plan. |
| **BMAD** | ★★★☆☆ | Can feel ceremonial for one person — PM, Architect, Dev, QA agents simulating a team you don't have. The Quick Flow mode helps. Best when your project is complex enough that you'd benefit from the discipline of separate analysis, planning, and architecture phases. |
| **Squad** | ★★★★☆ | Squad's "team" is AI agents, not humans — a solo developer gets a coordinated team of specialized agents with persistent memory, parallel fan-out, and Ralph for autonomous work monitoring. Requires Copilot and benefits most when using GitHub Issues. |
| **Superpowers** | ★★★★★ | Mandatory behavioral skills prescribe TDD, code review, and systematic workflows across several tools. |
| **HVE** | ★☆☆☆☆ | Its enterprise agent and instruction inventory adds substantial overhead for most solo work outside regulated software. |

**Reported experiences:**

- Geoffrey Huntley (Ralph creator): "Ralph can replace the majority of outsourcing at most companies for greenfield projects." He built an entire programming language (CURSED) solo using Ralph — compiler, stdlib, LLVM backend.
- Y Combinator hackathon teams: "We put a coding agent in a while loop and it shipped 6 repos overnight" for $297 in API costs.
- Birgitta Böckeler (Thoughtworks): On spec-driven approaches for small tasks — "the time spent reviewing generated specification files was comparable to the time spent just coding directly." Context engineering via rules files is often enough.

**Recommended starting point:** Context Engineering (rules files) → add GSD, Squad, Superpowers, or Ralph depending on your tool and project size.

---

### Small team (2–3 people)

Small teams need shared conventions and clear work boundaries without much coordination overhead.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Context Engineering** | ★★★★★ | Shared rules files give every team member's AI sessions the same conventions. Agents can still ignore instructions, so verify their output. |
| **GSD** | ★★★★☆ | Each person runs a GSD Core workflow on different features. The installer targets several runtimes, but GSD still provides no shared team coordination. |
| **Spec Kit** | ★★★★☆ | Shared specs in the repo give everyone a common source of truth. Agent-agnostic — one person can use Copilot while another uses Claude Code. The specs coordinate, not the tools. |
| **OpenSpec** | ★★★★☆ | Strong for teams evolving an existing codebase. Delta specs make intent review explicit and work across a very broad set of coding tools. |
| **BMAD** | ★★★★☆ | The team simulation starts to make more sense. One person can run the PM/Architect phases while another starts implementation. Quick Flow keeps it light for small tasks. |
| **Squad** | ★★★★☆ | Strong fit if you're on Copilot. The Coordinator routes work across specialized AI agents, persistent memory keeps decisions consistent across sessions, and Ralph automates issue triage and backlog management. The .squad/ setup is automated — the Coordinator handles assembly. |
| **Ralph** | ★★★☆☆ | Individual team members can Ralph independently on separate branches. No built-in team coordination — you'll need to handle merge conflicts yourself. |
| **Superpowers** | ★★★☆☆ | Each person runs independently with their own skills. It structures individual work but needs external coordination for shared tasks. |
| **HVE** | ★★☆☆☆ | Still too heavy for most small teams. The large RPI inventory is designed for larger organizations. |

**Reported experiences:**
- Martin Fowler's blog: Shared specification review before implementation gives team members a communication artifact as well as an AI input.
- BMAD community: Small teams report value from Analysis and Solutioning, particularly the Architect's review of technical decisions.

**Recommended starting point:** Context Engineering + Spec Kit or GSD (depending on tool choice).

---

### Medium team (4–10 people)

As people specialize across frontend, backend, testing, and infrastructure, AI agents need access to shared decisions and explicit work assignments.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Squad** | ★★★★★ | Named agents with charters divide team responsibilities. The decisions ledger records past choices, Ralph monitors the GitHub board, and agents can work in parallel. |
| **BMAD** | ★★★★★ | Specialized roles cover product, architecture, development, and quality. Scale-adaptive intelligence adjusts process weight to task complexity. |
| **HVE** | ★★★★☆ | The RPI workflow separates investigation from implementation. Setup remains substantial, but more complex tasks can justify the governance layer. |
| **Context Engineering** | ★★★★☆ | Still essential as a foundation, but no longer sufficient alone. You need a framework on top to coordinate multi-person, multi-concern work. |
| **OpenSpec** | ★★★☆☆ | Useful for change-level intent tracking and multi-tool teams, but lacks multi-agent orchestration or team workspaces for larger coordination. |
| **GSD** | ★★★☆☆ | Good for individual contributors within the team, but no built-in team coordination. Each person runs GSD independently — you need something else (Squad, BMAD, or your own process) for cross-team orchestration. |
| **Spec Kit** | ★★★☆☆ | Useful for the specification phase, but you'll pair it with another technique for execution and coordination. |
| **Ralph** | ★★☆☆☆ | Individual contributors can still use Ralph for well-scoped tasks, but it offers nothing for team coordination. Teams using Ralph typically assign separate repos or features to separate Ralph loops. |
| **Superpowers** | ★★☆☆☆ | No team coordination features. Individual contributors can use Superpowers for their own tasks, but the framework has no mechanisms for cross-team orchestration or shared governance. |

**Reported experiences:**

- thomy.tech (on Squad): "My First Coding Agent Fleet with Enterprise Tooling" described multiple agents working on different parts of a project with persistent memory.
- BMAD community (Discord): Teams of 5-8 report that scale-adaptive planning reduces process overhead on simple feature branches.

**Recommended starting point:** Squad (if Copilot) or BMAD (if multi-tool) + Context Engineering as foundation.

---

### Large team / organization (10+ people, multiple teams)

Large organizations need documented conventions, governance, audit trails, and onboarding guidance. Different teams may still need different workflows.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | Enterprise collections, validated artifacts, and policy-as-code support organizational controls. The repository has added many skills, but stable-package contents differ from `main`. |
| **Context Engineering** | ★★★★★ | The foundation layer. Organization-wide rules files standardize AI behavior, while Agent Skills packages reusable capabilities above them. |
| **BMAD** | ★★★★☆ | The module ecosystem scales to enterprise needs. Cross-platform support lets teams use the same methodology across several tools, with runtime-depth caveats. |
| **Squad** | ★★★★☆ | Per-team Squad instances work well. Each team has its own .squad/ with its own agents, decisions, and routing. The SDK-first mode (squad.config.ts) is more enterprise-friendly than Markdown-only configuration. |
| **Spec Kit** | ★★★☆☆ | The constitution.md concept (project principles and guardrails) scales well for enforcing organizational standards. Pair with a heavier framework for execution. |
| **OpenSpec** | ★★☆☆☆ | Useful for brownfield change records, but current large-org fit is limited until workspace/multi-repo and enterprise governance features mature. |
| **GSD** | ★★☆☆☆ | Individual contributor tool within a larger framework. Not designed for organizational coordination. |
| **Superpowers** | ★★☆☆☆ | No governance or team features. Individual contributors can adopt Superpowers skills for personal workflows, but the framework provides no organizational coordination or audit capabilities. |
| **Ralph** | ★☆☆☆☆ | No governance, no audit trail, no team coordination. An organization using Ralph needs extensive wrapping and oversight. |

**Reported experiences:**

- Robin Cole (VP Engineering, Microsoft) on HVE at TMForum: Reported enterprise adoption by AT&T and KT Corporation.
- Birgitta Böckeler on harness engineering: "What's good for humans is good for AI" — organizations should invest in architectural constraints (custom linters, structural tests, context documentation) as "harnesses" that make AI agents more reliable. HVE's collection architecture implements this.

**Recommended starting point:** HVE (if on Copilot) or BMAD (if multi-tool) + Context Engineering as organizational standard.

---

## By project type

### Greenfield (starting from scratch)

All the techniques can support greenfield work, with different planning and setup costs.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★★ | Fresh context per iteration suits new projects with well-defined requirements and no existing code to preserve. |
| **GSD** | ★★★★★ | The five-step Discuss → Plan → Execute → Verify → Ship lifecycle provides strong greenfield scaffolding. |
| **BMAD** | ★★★★☆ | The Analysis phase (domain research, market research, technical research) is most valuable at greenfield stage when the problem space is poorly understood. |
| **Spec Kit** | ★★★★☆ | Constitution → specify → plan → tasks → implement maps naturally to the "blank slate" starting point. |
| **OpenSpec** | ★★★☆☆ | Can work for greenfield, but it is change-centric rather than project-centric. GSD or Spec Kit provide more full-project scaffolding. |
| **Squad** | ★★★★☆ | Team assembly, initial architecture decisions, and parallel agent fan-out are effective for scaffolding new projects. |
| **Superpowers** | ★★★★★ | Brainstorm → plan → implement with mandatory TDD and worktrees for parallel development. |
| **HVE** | ★★★☆☆ | Works, but the Research phase is less valuable when there's no existing codebase to investigate. More valuable later as the codebase grows. |
| **Context Engineering** | ★★★☆☆ | Essential but thin at the start — your rules file gets more valuable as the project evolves and conventions accumulate. |

### Brownfield (existing codebase)

The agent needs to understand existing behavior and conventions before changing code, or it may duplicate or break them.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | The AI investigates the existing codebase and documents findings before planning changes. This helps identify code that should be reused rather than regenerated. |
| **Context Engineering** | ★★★★★ | A rules file records existing architecture, conventions, and known pitfalls for the agent to consult. |
| **GSD** | ★★★★☆ | Has explicit Brownfield Support mode and fresh context per task to limit accumulated confusion. |
| **OpenSpec** | ★★★★★ | Built for this. Change folders and delta specs track how a targeted change modifies existing behavior, with proposal approval before code. |
| **BMAD** | ★★★★☆ | The Analysis phase can study the existing domain before changes begin. Scale-adaptive intelligence adjusts to task size within the existing codebase. |
| **Spec Kit** | ★★★☆☆ | The analyze command checks for inconsistencies, but in brownfield testing, spec-driven tools have been observed taking existing class descriptions as new specifications and generating duplicates. Careful scoping is needed. |
| **Squad** | ★★★☆☆ | Persistent agent memory helps — agents remember past decisions about the codebase. But the initial context loading needs careful setup. |
| **Superpowers** | ★★★★☆ | Systematic debugging skills and root-cause-tracing help navigate existing codebases. Skills can be customized for codebase-specific patterns. |
| **Ralph** | ★★☆☆☆ | Ralph's own documentation cautions against brownfield use. The nondeterministic ripgrep search problem is worst in brownfield — Ralph may conclude code hasn't been implemented when it has, creating duplicates. Community reports are emerging for brownfield use, but it remains risky. |

### Rapid prototyping / hackathons

For prototypes, prioritize a working result over process that the experiment does not need.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★★ | Y Combinator teams reported 6 repos overnight for $297. The anecdote was not re-verified in this pass. |
| **Context Engineering** | ★★★★☆ | A short rules file can establish the tech stack and coding style without framework setup. |
| **GSD** | ★★★☆☆ | Quick Mode compresses the workflow, but even the compressed version adds ceremony that slows down hackathon pace. |
| **OpenSpec** | ★★☆☆☆ | Lightweight for SDD, but proposal/review/archive still adds more intent tracking than most prototypes need. |
| **Superpowers** | ★★★☆☆ | TDD enforcement adds ceremony that can slow hackathon pace. The skills framework is valuable for disciplined prototyping, but pure speed favors lighter approaches. |
| **Spec Kit** | ★★☆☆☆ | Spec-plan-tasks-implement is too many steps when you want code running in hours. |
| **BMAD** | ★★☆☆☆ | Quick Flow reduces overhead, but the full PM → Architect → Dev → QA process adds work most prototypes do not need. |
| **Squad** | ★★☆☆☆ | Team assembly and casting add setup time. For a hackathon, the persistent memory and coordination aren't worth the upfront cost. |
| **HVE** | ★☆☆☆☆ | Research → Plan → Implement → Review adds governance overhead that slows prototype exploration. |

### Migration / refactoring

Migration and refactoring change an existing stack or pattern. Define what must change and which behavior must remain intact.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Ralph** | ★★★★☆ | Suits repetitive, mechanical migration steps with clear source and target patterns. Define both in the specs. |
| **HVE** | ★★★★☆ | Research phase documents the existing system. Plan phase maps the migration path. Implement phase executes task-by-task with verification. |
| **GSD** | ★★★★☆ | The parallel wave execution is valuable for migrations with many independent modules to port. |
| **OpenSpec** | ★★★★☆ | Delta specs are a good fit when migration work needs explicit intent review for changed behavior in an existing codebase. |
| **Context Engineering** | ★★★★☆ | Critical to document "old patterns → new patterns" in rules files so the AI consistently applies the transformation. |
| **BMAD** | ★★★☆☆ | The Analyst agent can study the existing system. But the full agile simulation may be overkill for a mechanical migration. |
| **Spec Kit** | ★★★☆☆ | Spec the migration requirements clearly. Constitution can enforce "always use new patterns." |
| **Superpowers** | ★★★☆☆ | Skills can be customized for migration patterns. The systematic approach helps, but Superpowers lacks migration-specific tooling. |
| **Squad** | ★★★☆☆ | Useful if the migration touches multiple concerns (frontend migration + backend migration + test migration in parallel). |

---

## By industry & compliance

### Regulated environments

These environments require audit trails, compliance evidence, and validated artifacts. Mistakes can have legal or safety consequences.

**Examples:**

- **Financial services** — SOX compliance, SEC reporting requirements, PCI-DSS for payment systems. Every code change affecting financial calculations needs traceability from requirement to implementation to test.
- **Healthcare / Life sciences** — HIPAA compliance, FDA software validation (21 CFR Part 11), GxP requirements. AI-generated code must be verifiable and its provenance documented.
- **Government / Defense** — FedRAMP, NIST 800-53, ITAR restrictions. Security clearances may restrict which cloud-based AI tools can be used at all.
- **Automotive** — ISO 26262 (functional safety), ASPICE. Safety-critical software requires formal verification and evidence chains.
- **Aerospace** — DO-178C (airborne software). Every line of code needs traceability to requirements. Modified Condition/Decision Coverage (MC/DC) for Level A software.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | Constraint-based workflows, validated artifacts, and supply-chain security tools (SBOM generation, attestation, OpenSSF Scorecard, CodeQL). RPI links Research documents → Plan → Implementation → Review, with collections for security and RAI (Responsible AI) planning. Telco adoption is reported, not evidence of compliance by itself. |
| **Context Engineering** | ★★★★★ | Constraint context in rules files (Layer 5 — "what the agent must NOT do") records forbidden patterns, security requirements, and compliance gates. Version control makes these instructions reviewable, but does not enforce them. |
| **BMAD** | ★★★☆☆ | Structured phases provide some process evidence, but no built-in compliance artifacts or policy enforcement. You'd need to add governance layers on top. |
| **Spec Kit** | ★★★☆☆ | The constitution.md concept can encode compliance requirements. Version-controlled specs provide some traceability. But no enforcement mechanism — the AI may still ignore the constitution. |
| **OpenSpec** | ★★★☆☆ | Proposal approval and archived change intent provide lightweight traceability, but there is no enterprise policy enforcement, SSO/SCIM, or compliance-grade audit layer. |
| **GSD** | ★★☆☆☆ | Verification gates help, but no formal audit trail, no compliance artifacts, no policy-as-code. |
| **Squad** | ★★☆☆☆ | The reviewer rejection protocol and decisions ledger provide some governance, but not at the level regulated industries require. |
| **Superpowers** | ★★☆☆☆ | TDD enforcement provides some structure, but no audit trails, governance mechanisms, or compliance artifacts. Every change would still need manual compliance review. |
| **Ralph** | ★☆☆☆☆ | No built-in governance or formal audit trail. Human review before each change lands limits the benefit of unattended execution. |

**Real-world guidance for regulated environments:**

1. **Never skip the research phase.** Whether using HVE's formal Research agent or doing it manually, the AI must investigate before implementing. As HVE's docs state: "When AI knows it cannot implement, it stops optimizing for 'plausible code' and starts optimizing for 'verified truth.'"
2. **Invest in harness engineering.** Custom linters, structural tests, and architectural constraints check defined requirements without depending on the LLM to follow instructions. They catch only the problems those checks cover.
3. **Pin model versions.** Context engineering research shows: "Production applications should pin to specific model snapshots, as router behavior changes between versions." For regulated environments, model version changes should go through the same change control as code changes.
4. **Verify output against the codebase.** GSD's verification gates and HVE's Review phase check the code rather than relying on the AI's claims. Keep independent checks in regulated workflows.

### Non-regulated / internal tools / startups

When the compliance burden is lower, faster iteration may matter more than formal process.

Any technique works. Choose based on team size and project type (see above). The key question is: **how much structure justifies its overhead?**

- **If speed matters most:** Ralph, GSD, or Superpowers
- **If you want process without governance:** BMAD, Squad, or Superpowers
- **If you're building a culture:** Context Engineering as foundation, pick a framework as the team grows

---

## By development activity

Not every task needs the same technique. Many teams use different approaches for different types of work.

### Bug fixes

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small, clear bug | Direct prompting + Context Engineering | For small, well-scoped bugs, spec-driven tools add overhead that exceeds the task effort. Just describe the bug, let the agent fix it. |
| Complex, multi-file bug | GSD or HVE (Research phase) | When the bug touches multiple systems, the research-first approach prevents the AI from "fixing" the wrong thing. Superpowers' systematic debugging skills and root-cause-tracing also help here. |
| Recurring bug pattern | Context Engineering | Add the pattern to your rules file: "When you see error X, the cause is usually Y, not Z." Future AI sessions benefit. |

### Feature development

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small feature (< 1 day) | GSD Quick Mode or Spec Kit | Just enough structure to prevent scope creep without heavy ceremony. |
| Medium feature (1-5 days) | GSD, BMAD Quick Flow, Squad, or Superpowers | Planning and verification become more useful as complexity increases. Superpowers makes TDD part of each implementation task. |
| Large feature (weeks+) | BMAD (full), Squad (full), or HVE | You need structured phases, quality gates, and persistent memory across sessions. |

### Test generation

| Approach | Recommendation | Why |
|----------|---------------|-----|
| Bulk test generation | Ralph | Repetitive, well-defined work can run unattended when test requirements and completion criteria are clear. |
| Test-driven development | GSD, Superpowers, or direct prompting | Write the test spec first, then let the AI implement. Superpowers enforces TDD as a mandatory skill. |
| Enterprise test suites | BMAD Test Architect module | Risk-based testing with structured QA agent involvement (run by its own agent, Murat). |

### Documentation

| Approach | Recommendation | Why |
|----------|---------------|-----|
| API docs, READMEs | Ralph or direct prompting | Routine documentation from code can suit unattended work when the scope and checks are clear. |
| Architecture docs | BMAD or HVE | Need the analysis/research phase to produce accurate architecture documentation. |
| Spec documentation | Spec Kit | The specs themselves become living documentation. |

### Refactoring

| Scale | Recommendation | Why |
|-------|---------------|-----|
| Small refactors | Direct prompting | Rename, extract method, simplify — these don't need a framework. |
| Large refactors | GSD (parallel waves), BMAD, or Superpowers | Multi-file refactors benefit from phase separation and parallel execution. Superpowers' systematic skills help maintain consistency. |
| Architecture migration | HVE + Context Engineering | Research the existing architecture, plan the migration, implement with verification. |

---

## By development methodology

### Agile / Scrum teams

Running sprints with stand-ups, retrospectives, and backlog grooming.

| Technique | Fit | Why |
|-----------|-----|-----|
| **BMAD** | ★★★★★ | BMAD *is* agile simulation. Sprint planning, stories, retrospectives, QA cycles — it maps 1:1 to Scrum. The Scrum Master agent facilitates ceremonies. |
| **Squad** | ★★★★☆ | Ceremonies (design reviews, retros, standups) are built-in. Ralph monitors the GitHub backlog continuously. The issue → branch → PR → merge lifecycle integrates with sprint-based work. |
| **HVE** | ★★★★☆ | The RPI workflow maps to sprint tasks: Research and Plan early in the sprint, Implement mid-sprint, Review at the end. Collections for GitHub, ADO, and Jira integrate with existing backlog tools. |
| **GSD** | ★★★☆☆ | The five-step workflow maps to individual sprint tasks, but GSD has no sprint-level coordination. Use it within sprints, not to manage them. |
| **Spec Kit** | ★★★☆☆ | Specs can map to user stories. The constitution can encode sprint conventions. But Spec Kit doesn't manage sprint process. |
| **Context Engineering** | ★★★☆☆ | Rules files can encode sprint conventions ("always reference the Jira ticket in commit messages"), but won't manage agile process. |
| **Ralph** | ★★☆☆☆ | Can be used for specific sprint tasks, but has no concept of sprints, backlogs, or ceremonies. |
| **Superpowers** | ★★★☆☆ | Individual agent workflow, not team process. Skills work well for sprint task execution but Superpowers has no sprint-level coordination or ceremonies. |

### Kanban / continuous flow

Work-in-progress limits, continuous delivery, no sprints.

| Technique | Fit | Why |
|-----------|-----|-----|
| **Squad** | ★★★★★ | Ralph (Work Monitor) continuously scans for work and routes it without sprint boundaries. |
| **GSD** | ★★★★☆ | Each ticket or card runs through the five-step workflow independently. No sprint coupling. |
| **Context Engineering** | ★★★★☆ | Rules files define the "how," the Kanban board defines the "what." Lightweight and flow-compatible. |
| **Ralph** | ★★★★☆ | The autonomous loop is inherently continuous. Pair with a GitHub Issues board for visual tracking. |
| **Superpowers** | ★★★☆☆ | Individual workflow fits continuous flow. Skills execute per-card naturally. No batch-like overhead, but no board-level awareness. |
| **BMAD** | ★★★☆☆ | Scale-adaptive intelligence adjusts, but the phases imply batching that conflicts with true continuous flow. |
| **Spec Kit** | ★★★☆☆ | Works per-card, but the multi-step workflow adds batch-like overhead. |
| **HVE** | ★★☆☆☆ | The RPI phases imply sequential processing that fights continuous flow. |

### Waterfall-adjacent / stage-gate

Sequential phases with formal gate reviews between them.

| Technique | Fit | Why |
|-----------|-----|-----|
| **HVE** | ★★★★★ | RPI *is* stage-gate: Research → gate → Plan → gate → Implement → gate → Review. Validated artifacts at each gate. |
| **BMAD** | ★★★★★ | Four sequential phases (Analysis → Planning → Solutioning → Implementation) with quality gates between each. |
| **Spec Kit** | ★★★★☆ | Constitution → specify → plan → tasks → implement is a natural stage pipeline. |
| **GSD** | ★★★☆☆ | The five-step workflow is sequential, but designed for iteration within stages rather than strict gates. |
| **Squad** | ★★☆☆☆ | More about parallel coordination than sequential phases. Can enforce phase gates through ceremonies, but it's not native. |
| **Ralph** | ★☆☆☆☆ | No formal phases or stage gates; iteration follows the loop and its test checks. |
| **Superpowers** | ★★☆☆☆ | Skills provide structure within tasks, but no formal phase gates or validated artifacts between stages. |
| **Context Engineering** | ★★☆☆☆ | Supports any process but provides no process of its own. |

---

## Combining techniques

These combinations assign different responsibilities to each technique. They are workflow suggestions, not independently tested integrations.

### Context Engineering + any framework

Use well-maintained rules files to supply project context alongside a framework or Ralph loop.

### Spec Kit + GSD or Squad

Use Spec Kit for the specification and planning phase, then hand off to GSD (for execution with parallel waves) or Squad (for multi-agent team execution). Spec Kit is deliberately narrow — it handles specs, not execution.

### OpenSpec + Superpowers or GSD

Use OpenSpec to govern the change intent for existing code, then use Superpowers or GSD to enforce disciplined implementation. This pairing works best when you need both reviewable "why" artifacts and stronger execution practices.

### Ralph + GSD

Use GSD's structured planning to create the spec and task breakdown. Then use Ralph to execute the tasks autonomously overnight. Ralph's prompt.md can reference GSD's planning artifacts.

### BMAD + Context Engineering

Use BMAD's agent personas for the process and maintained rules files for project knowledge that persists across sessions.

### HVE + Squad (Enterprise Copilot shops)

HVE provides the governance and methodology. Squad provides the team coordination and work monitoring. Use HVE's collections for domain standards and Squad's agents for execution.

### Superpowers + Context Engineering

Use rules files for project-level conventions and Superpowers skills for TDD, code review, and debugging workflows.

### Superpowers + Squad

Use Superpowers for individual agent skill development within Squad's team coordination. Each Squad agent can be enhanced with Superpowers skills for disciplined task execution, while Squad handles the cross-agent orchestration, persistent memory, and work routing that Superpowers lacks.

### Skills library + any methodology

Install selected skills — composable (`mattpocock/skills`), lifecycle-mapped (`addyosmani/agent-skills`), or orchestrated (`pstack/poteto-mode`) — alongside GSD, Spec Kit, OpenSpec, BMAD, Squad, Ralph, or HVE. Prefer a vendored, reviewed copy when reproducibility matters. Native plugin marketplaces reduce update work but require trust in upstream changes. See [Choosing a Skills Approach](skills-choosing.md) and [Distribution and Governance](skills-management.md) for the full packaging, provenance, and runtime criteria.

---

## Anti-patterns: when not to use a technique

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Using HVE or BMAD for a 30-minute bug fix | Framework overhead exceeds the task effort. For small, well-scoped tasks, direct prompting with good context engineering is faster and more effective. |
| Using Ralph in a large brownfield codebase without safeguards | Nondeterministic ripgrep searches lead to duplicate code and incorrect assumptions about what exists. Ralph's own documentation cautions against brownfield use without safeguards. |
| Using any SDD tool for exploratory prototyping | When you don't know what you're building yet, the time spent reviewing generated specification files can be comparable to the time spent just coding directly. Specs create drag during exploration. |
| Using Ralph without a test suite | Tests are Ralph's backpressure. Without them, the loop has no quality gate and can spend API credits without useful progress. |
| Assuming every GSD installer target has parity | GSD Core documents many targets, but equivalent hooks, subagents, commands, and execution semantics were not verified. Pilot your runtime before standardizing. |
| Forcing one technique on a team with mixed tools | If half the team uses Claude Code and half uses Copilot, a runtime-specific methodology creates friction. Use a portable specification or skills layer where possible. |
| Installing skills without reviewing provenance | Skills can bundle scripts and tool permissions. Registry presence or an audit badge is not a substitute for source review and pinning. |
| Using Superpowers for team coordination | Superpowers enhances individual agent workflows, not team orchestration. For team coordination, use Squad or BMAD. Superpowers can complement these frameworks for individual task execution. |

---

## Cost considerations

Costs include API credits, subscriptions, and compute. Parallel agents and long unattended loops can increase usage.

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

## Tool lock-in matrix

Check tool compatibility before adopting a technique:

| Technique | Primary Tool | Works With | Hard Blocker |
|-----------|-------------|-----------|--------------|
| **Context Engineering** | Any | All tools | None — universal practice |
| **Ralph** | Any CLI | Claude Code, Copilot CLI, Cursor CLI, Codex, Gemini CLI | Needs CLI mode — doesn't work in IDE-only tools |
| **Spec Kit** | Any | Copilot, Claude Code, Cursor, Windsurf, Gemini CLI | None — agent-agnostic by design |
| **OpenSpec** | Any | Broad native/pre-baked support, including vendor-neutral `.agents/skills/` output | Feature depth varies by runtime |
| **BMAD** | Claude Code, Cursor, Windsurf | Most tools via V6 cross-platform support | None (V6 broadened support) |
| **GSD** | Multi-runtime installer | Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more | Installer support does not prove runtime parity |
| **Superpowers** | Claude Code | Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode | Needs CLI mode for bootstrapping |
| **Squad** | GitHub Copilot | Copilot CLI + VS Code | Does not work with Claude Code, Cursor, or other tools |
| **HVE** | GitHub Copilot | VS Code extension only | Tightly coupled to Copilot — no other tool support |

---

## Summary: the one table

Use these as starting recommendations, subject to the runtime and governance checks above:

| Scenario | Primary Recommendation | Runner-Up |
|----------|----------------------|-----------|
| Solo dev, quick project | Context Engineering + Ralph | GSD or Superpowers |
| Solo dev, serious project | GSD (after validating host behavior) or Squad (Copilot) | Superpowers or BMAD |
| Small team (2-3), multi-tool | Spec Kit + Context Engineering | BMAD |
| Small team (2-3), brownfield | OpenSpec + Context Engineering | GSD |
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
