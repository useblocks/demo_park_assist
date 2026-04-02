# Park Assist Demo – Workshop Part 2

> **Reset to starting state:** Run `make step_1` to set code, docs and tests to the correct baseline for this step.
> **Tip:** Targets can be combined — e.g. `make step_1 clean open` switches state, clears the build and opens the docs in one go.

## Working with Docs: Traceability, Schemas, and Fixing Problems

This session focuses on the sphinx-needs documentation, exploring it with
**ubCode** and **GitHub Copilot**, enforcing traceability rules via schemas,
and fixing link violations with AI assistance.

---

## Steps

**1. Initialise ubCode**

If you have not done so already, open `docs/index.rst` in the editor.
This triggers ubCode to index the project so that all Needs (user stories,
architecture elements, test cases, etc.) become available for queries and
diagnostics.

**2. Ask Copilot whether all test cases verify a user story**

Open the Copilot Chat panel and ask:

> @demo: Are all test cases linked to a user story via the verifies field?
> Or do any test cases verify an architecture element instead?

"@demo" will call a small agent, which is using the ubCode MCP server
to get determinsitc answers.

Copilot will query the ubCode index and check the `verifies` links of every
test case.

**3. Review the findings**

One test cases will be reported as linking to architecture elements instead
of user stories:

- `TC_004` — verifies `AR_003` (Sensor Module) instead of `US_004`

**4. Ask the `@ubCode` chat participant for a schema**

In Copilot Chat, address the ubCode participant and ask it to create a
schema that automatically flags this problem going forward:

> @ubCode Can you create a schema that ensures every test case only verifies
> user stories, not architecture elements?

The participant will propose a `schemas.json` file and a one-line addition
to `ubproject.toml`.

**5. Ask Copilot to fix the wrong links**

In Copilot Chat, ask:

> @demo Fix the test cases which have wrong links

Copilot will propose the corrected directives:

- `TC_004` → `:verifies: US_004`

Apply the changes and confirm the Problems panel violations disappear.

**6. Ask Copilot to create a missing test case**

Get a list of use cases without test cases from CoPilot via:

> @demo Which use cases are not covered by a test case

User story `US_007` ("Code runs exclusively on CircuitPython") has no test
case. Ask Copilot to write one:

> @demo US_007 has no test case. Can you create a test case that verifies
> this user story?

Review the generated test case, add it to `docs/test_cases.rst`, and
confirm it passes schema validation (no violation in the Problems panel).

**9. Open the graph view**
Go to the source code of Use Case UC_004, by searching it in the ubCode Needs Index
and clicking the "Got to source" button in its line.
Hint: You must have opend already a .rst file from the docs project, so that ubCode knows the scope for its daata (as it supports multi-doc--project setups in one repo).

Right-click the need ID of thje use case  in the
editor and select **"Show ubCode need ID in graph view"**.
The interactive graph displays the use case together with the architecture and test case elements  — giving a full traceability chain at a glance.
---

> **Tip:** `make html` rebuilds the full Sphinx documentation so you can
> review the rendered output of any changes in your browser.

