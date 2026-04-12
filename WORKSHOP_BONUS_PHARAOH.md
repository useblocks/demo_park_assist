# Bonus – Pharaoh: AI-Assisted Requirements Engineering

> **Prerequisite:** Workshop Step 5 completed (or run `make step_5`).
> **Starting state:** The Park Assist project is fully documented — User Stories → Architecture → Implementation → Test Cases.

Pharaoh is an AI agent framework for sphinx-needs projects. It combines structured
workflows with requirements engineering intelligence to help teams analyse, trace,
and validate requirements using AI.

This bonus exercise installs Pharaoh into the project and uses three of its agents:

| Agent | What it does |
|---|---|
| `@pharaoh.setup` | Detects the project, generates `pharaoh.toml`, recommends tooling |
| `@pharaoh.mece` | Structural analysis — gaps, orphans, redundancies, ID violations |
| `@pharaoh.change` | Change impact analysis — trace through all linked needs and code |

---

## Steps

**1. Install Pharaoh agents**

```bash
make step_bonus
```

This copies the Pharaoh Copilot agents into `.github/agents/` and `.github/prompts/`.
After the command completes, the `@pharaoh.*` agents are available in Copilot Chat.

---

**2. Set up Pharaoh**

Open a new Copilot Chat and run:

> @pharaoh.setup

The agent will:
- Detect the sphinx-needs project structure and need types
- Identify the link types (`realizes`, `verifies`)
- Ask for your preferred strictness mode (`advisory` or `enforcing`)
- Generate a `pharaoh.toml` configuration file
- Recommend ubCode and ubc CLI tooling if not installed

Accept the generated `pharaoh.toml` — the defaults work well for this project.

---

**3. Check the requirements structure (MECE analysis)**

> @pharaoh.mece

Pharaoh analyses the full traceability graph and reports:

- **Gaps** — needs missing required downstream links (e.g., a User Story with no Architecture element)
- **Orphans** — needs completely disconnected from the graph
- **Redundancies** — needs with nearly identical titles or content
- **ID violations** — IDs that don't match the project's naming convention

Review the report. The `step_5` baseline should be mostly clean — any findings are
intentional workshop artefacts or genuine issues worth discussing.

---

**4. Trace a single requirement**

Pick a User Story ID from the MECE report or from `docs/user_stories.rst`
(e.g. `US_BUZZER`) and run:

> @pharaoh.trace US_BUZZER

The agent renders a full traceability tree — upstream and downstream — across all
link types and into the source code via codelinks:

```
US_BUZZER (User Story: Buzzer alert) [open]
└── AR_BUZZER (Architecture: Buzzer component) [open] --realizes-->
    └── IM_BUZZER (Implementation: buzzer module) [open] --realizes-->
    │   └── TC_BUZZER_001 (Test Case: ...) [open] --verifies-->
    └── src/code.py:buzz() [codelink]
```

---

**5. Analyse a change**

Imagine the buzzer threshold needs to change from 20 cm to 30 cm. Run:

> @pharaoh.change US_BUZZER The distance threshold should change from 20 cm to 30 cm.

Pharaoh produces a **Change Document** listing every affected need and code file,
classified as:

| Action | Meaning |
|---|---|
| **Must update** | Change directly invalidates this item |
| **Review needed** | May be affected — human judgement required |
| **No change needed** | Linked but unaffected by this specific change |

At the end, the agent asks you to acknowledge the analysis. After acknowledging,
you can use `@pharaoh.author` to apply the changes in the correct order.

---

**6. Clean up (optional)**

To remove the Pharaoh agents from `.github/`:

```bash
make step_unbonus
```

This leaves `pharaoh.toml` in place if you generated one — delete it manually if
you want a clean reset.

---

## Further Agents

The Pharaoh repo contains additional agents not covered in this exercise:

| Agent | What it does |
|---|---|
| `@pharaoh.author` | Create or modify needs with correct IDs, types, and links |
| `@pharaoh.verify` | Validate implementations against their requirements |
| `@pharaoh.release` | Generate changelogs and traceability coverage metrics |
| `@pharaoh.plan` | Break changes into structured implementation tasks |

See [github.com/useblocks/pharaoh](https://github.com/useblocks/pharaoh) for the full documentation.
