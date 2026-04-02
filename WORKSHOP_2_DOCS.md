# Park Assist Demo – Workshop Part 2

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

> Are all test cases linked to a user story via the verifies field?
> Or do any test cases verify an architecture element instead?

Copilot will query the ubCode index and check the `verifies` links of every
test case.

**3. Review the findings**

Two test cases will be reported as linking to architecture elements instead
of user stories:

- `TC_004` — verifies `AR_003` (Sensor Module) instead of `US_004`
- `TC_010` — verifies `AR_007` (Buzzer Module) instead of `US_006`

**4. Ask the `@ubCode` chat participant for a schema**

In Copilot Chat, address the ubCode participant and ask it to create a
schema that automatically flags this problem going forward:

> @ubCode Can you create a schema that ensures every test case only verifies
> user stories, not architecture elements?

The participant will propose a `schemas.json` file and a one-line addition
to `ubproject.toml`.

**5. Review the proposed schema**

Read through the generated `schemas.json` carefully. Verify that it:

- selects only needs of type `test`
- requires at least one `verifies` link
- validates that every link ID matches the pattern `US_\d{3}`

**6. Apply the schema and check Diagnostics**

Copy `schemas.json` next to `docs/ubproject.toml` and add the following
line to the `[needs]` section of `ubproject.toml`:

```toml
schema_definitions_from_json = "schemas.json"
```

Save the file. Open the **Problems** panel (`View → Problems`) and confirm
that `TC_004` and `TC_010` now appear as violations.

**7. Ask Copilot to fix the wrong links**

In Copilot Chat, ask:

> TC_004 and TC_010 verify architecture elements instead of user stories.
> Can you fix their :verifies: fields to point to the correct user stories?

Copilot will propose the corrected directives:

- `TC_004` → `:verifies: US_004`
- `TC_010` → `:verifies: US_006`

Apply the changes and confirm the Problems panel violations disappear.

**8. Ask Copilot to create a missing test case**

User story `US_007` ("Code runs exclusively on CircuitPython") has no test
case. Ask Copilot to write one:

> US_007 has no test case. Can you create a test case TC_014 that verifies
> this user story?

Review the generated test case, add it to `docs/test_cases.rst`, and
confirm it passes schema validation (no violation in the Problems panel).

**9. Open the graph view**

Right-click the need ID of any fixed test case (e.g. `TC_004`) in the
editor and select **"Show ubCode need ID in graph view"**.
The interactive graph displays the test case together with the user story it
verifies and the architecture elements that realize that story — giving a
full traceability chain at a glance.

---

> **Tip:** `make html` rebuilds the full Sphinx documentation so you can
> review the rendered output of any changes in your browser.

