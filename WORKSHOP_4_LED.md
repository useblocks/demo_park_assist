# Step 4 – LED Strip

> **Prerequisite:** Display shows distance, buzzer beeps continuously at < 20 cm (Step 3 done).
> LED strip is wired but still off.

**Files for this step:** `workshop/step_4/code.py`

---

## Task

After the buzzer block in the main loop, add strip control:

```python
if dist_cm < 20:
    strip.fill(RED)
else:
    strip.fill(GREEN)
strip.show()
```

In the out-of-range branch (`else` block), also add:

```python
strip.fill(OFF)
strip.show()
```

The color constants `RED`, `GREEN`, and `OFF` are already defined at the top of the file.

---

## Deploy

Copy `workshop/step_4/code.py` to the `CIRCUITPY` drive as `code.py`.

---

## Verify

- Distance ≥ 20 cm → strip lights up solid **green**
- Distance < 20 cm → strip lights up solid **red**, buzzer on
- Sensor covered / out of range → strip off, buzzer silent

---

## Solution

`workshop/step_4/solutions/code.py`
