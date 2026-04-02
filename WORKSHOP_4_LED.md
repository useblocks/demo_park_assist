# Step 4 – LED Strip

> **Reset to starting state:** Run `make step_3` to set code, docs and tests to the correct baseline for this step.
> **Tip:** Targets can be combined — e.g. `make step_3 clean open` switches state, clears the build and opens the docs in one go.

> **Prerequisite:** Display shows distance, buzzer beeps continuously at < 20 cm (Step 3 done).
> LED strip is wired but still off.

---

## Workshop Steps Overview

- **Step 4:**  
    - *Starting state:* Display + buzzer  
    - *Your task:* Add LED strip — documented first, then implemented with Copilot  
    - *New feature:* Red LEDs when distance < 20 cm, green otherwise, off on out-of-range

- **Step 5:**  
    - *Starting state:* Display + buzzer + simple LED strip  
    - *Your task:* Add zone logic  
    - *New feature:* 4 zones, dynamic LED count

---

## Steps

**1. Open the docs to initialise ubCode**

Open `docs/user_stories.rst` in the editor.
This lets ubCode index the project so the `@demo` agent can query and write Needs.

**2. Create a user story for the LED strip**

> @demo The LED strip should light up red when something is closer than 20 cm, green when the distance is 20 cm or more, and turn off when the sensor is out of range. Create a user story for this.

**3. Create the architecture, test cases, and implement in code**

> @demo Based on the LED strip user story, create the architecture element and test cases, then implement them in `src/code.py`.

Open `docs/architecture.rst` and activate the ubCode preview mode (upper right corner).
You can also enable **Rich preview** to render the mermaid diagrams.

**4. Build the docs and check the traceability graph**

```bash
make clean open
```

Right-click the LED strip user story ID in the editor and select **"Show ubCode need ID in graph view"**.
Confirm the chain `US_ → AR_ → TC_` is visible, and that the implementation codelink appears on the **Implementation** page.

**5. Run the tests**

```bash
make test
```

All tests should pass.

**6. Deploy to the board and verify on hardware**

Copy `src/code.py` onto the board (the board mounts as a USB drive named `CIRCUITPY`):

```bash
cp src/code.py /media/$USER/CIRCUITPY/code.py
```

Then verify the manual test cases:

- Distance **≥ 20 cm** → strip lights up solid **green**, buzzer silent.
- Distance **< 20 cm** → strip lights up solid **red**, buzzer beeps continuously.
- Sensor **out of range** → strip **off**, buzzer silent.

---

> **Solution:** `.workshop/step_4/solutions/code.py`

