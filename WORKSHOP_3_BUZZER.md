# Step 3 – Buzzer

> **Reset to starting state:** Run `make step_2` to set code, docs and tests to the correct baseline for this step.
> **Tip:** Targets can be combined — e.g. `make step_2 clean open` switches state, clears the build and opens the docs in one go.

> **Prerequisite:** The display already reads and shows the sensor distance.
> Buzzer and LED strip are wired but inactive.

---

## Workshop Steps Overview

- **Step 3:**  
    - *Starting state:* Display shows distance  
    - *Your task:* Add buzzer — documented first, then implemented with Copilot  
    - *New feature:* Continuous beep when distance < 20 cm

- **Step 4:**  
    - *Starting state:* Display + buzzer  
    - *Your task:* Add LED strip  
    - *New feature:* Red LEDs when distance < 20 cm, green otherwise

- **Step 5:**  
    - *Starting state:* Display + buzzer + simple LED strip  
    - *Your task:* Add zone logic  
    - *New feature:* 4 zones, dynamic LED count

---

## Steps

**1. Open the docs to initialise ubCode**

Open `docs/user_stories.rst` in the editor.
This lets ubCode index the project so the `@demo` agent can query and write Needs.

**2. Create a user story for the buzzer**

> @demo The buzzer should beep continuously when something is closer than 20 cm, and be silent otherwise. Create a user story for this.

**3. Create the architecture  and test cases element**

> @demo Implement the architecture and test cases based on the buzzer user story.

Open the architecture.rst file and acitvate the preview mode of ubCode on the upper right corner. After the preview openes, you can also activate the "Rich preview" in the preview window, which renders the mermaid architecture images

**5. Build the docs and check the traceability graph**

```bash
make clean open
```

Right-click the buzzer user story ID in the editor and select **"Show ubCode need ID in graph view"**.
Confirm the chain `US_ → AR_ → TC_` is visible.

**6. Implement the buzzer in the code**

> @demo Implement the buzzer user story element in `src/code.py`.

**7. Add a unit-testable helper and write the tests**

> @demo Add a unit-testable helper for the buzzer logic to `src/park_logic.py` and create `tests/test_buzzer.py`.

**8. Run the tests**

```bash
make test
```

All tests should pass, including the new buzzer tests.

**9. Rebuild the docs and verify implementation traceability**

```bash
make clean open
```

Open the **Implementation** page — the buzzer codelink should appear, linked to the buzzer architecture element.

**10. Deploy to the board and verify on hardware**

Copy `src/code.py` onto the board (the board mounts as a USB drive named `CIRCUITPY`):

```bash
cp src/code.py /media/$USER/CIRCUITPY/code.py
```

Then execute the manual test cases TC_006 and TC_007:

- Hold a flat object **15 cm** in front of the sensor → buzzer should emit a **continuous tone**.
- Move the object to **25 cm or further** → buzzer should go **silent immediately**.

---

> **Solution:** `.workshop/step_3/solutions/code.py`
