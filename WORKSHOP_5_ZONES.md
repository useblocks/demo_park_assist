# Step 5 – Dynamic Zone System

> **Reset to starting state:** Run `make step_4` to set code, docs and tests to the correct baseline for this step.
> **Tip:** Targets can be combined — e.g. `make step_4 clean open` switches state, clears the build and opens the docs in one go.

> **Prerequisite:** Display, simple red/green strip, and buzzer working (Step 4 done).

---

## Steps

**1. Open the docs to initialise ubCode**

Open `docs/user_stories.rst` in the editor.

**2. Create everything from a single prompt**

> @demo The park assist system should use a 4-zone proximity model. Zone 1 (> 30 cm): green LEDs, buzzer silent. Zone 2 (20–30 cm): yellow LEDs, buzzer beeps every 1 s. Zone 3 (15–20 cm): red LEDs (solid), buzzer beeps every 0.4 s. Zone 4 (≤ 15 cm): red LEDs blinking, buzzer continuous. Out of range: LEDs off, buzzer silent. The number of LEDs (of 60) scales linearly with distance — 0 LEDs at ≥ 40 cm, 60 LEDs at 0 cm — and is filled from the right. Create a user story for this, then derive the architecture element and test cases from it, and implement everything.

**3. Build the docs and check the traceability graph**

```bash
make clean open
```

**4. Run the tests**

```bash
make test
```

All tests should pass.

**5. Deploy to the board and verify on hardware**

Copy `src/code.py` onto the board (the board mounts as a USB drive named `CIRCUITPY`):

```bash
cp src/code.py /media/$USER/CIRCUITPY/code.py
```

Then verify the manual test cases:

- Distance **> 30 cm** → strip lights up **green**, buzzer silent.
- Distance **20–30 cm** → strip turns **yellow**, buzzer beeps every 1 s.
- Distance **15–20 cm** → strip turns **red** (solid), buzzer beeps every 0.4 s.
- Distance **≤ 15 cm** → strip **blinks red**, buzzer continuous.
- Sensor **out of range** → strip **off**, buzzer silent.

---

> **Solution:** `.workshop/step_5/solutions/code.py`

---

## Zone Reference

| Distance     | Colour         | LEDs (of 60)    | Buzzer         |
|--------------|----------------|-----------------|----------------|
| > 30 cm      | Green          | scales linearly | silent         |
| 20 – 30 cm   | Yellow         | scales linearly | 1 s interval   |
| 15 – 20 cm   | Red (solid)    | scales linearly | 0.4 s interval |
| ≤ 15 cm      | Red (blinking) | full strip      | continuous     |
| out of range | off            | 0               | silent         |
