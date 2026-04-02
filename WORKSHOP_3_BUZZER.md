# Step 3 – Buzzer

> **Prerequisite:** The display already reads and shows the sensor distance.
> Buzzer and LED strip are wired but inactive.

**Files for this step:** `workshop/step_3/code.py`

---

## Workshop Steps Overview

| Step | Starting state                  | Your task              | New feature                       |
|------|---------------------------------|------------------------|-----------------------------------|
| 3    | Display shows distance          | Add buzzer             | Continuous beep when dist < 20 cm |
| 4    | Display + buzzer                | Add LED strip          | Red < 20 cm, green otherwise      |
| 5    | Display + buzzer + simple strip | Add zone logic         | 4 zones, dynamic LED count        |

---

## Task

In the main loop, inside the `if raw_mm < 8190:` block, add:

```python
if dist_cm < 20:
    buzzer.value = True    # continuous beep
else:
    buzzer.value = False   # silent
```

Also add `buzzer.value = False` in the `else` branch (out-of-range).

---

## Deploy

Copy `workshop/step_3/code.py` to the `CIRCUITPY` drive as `code.py`.

---

## Verify

Hold your hand in front of the sensor (< 20 cm) → buzzer sounds continuously.
Move it away (≥ 20 cm) → silence.

---

## Solution

`workshop/step_3/solutions/code.py`
