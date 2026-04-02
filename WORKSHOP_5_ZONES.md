# Step 5 – Dynamic Zone System

> **Reset to starting state:** Run `make step_4` to set code, docs and tests to the correct baseline for this step.
> **Tip:** Targets can be combined — e.g. `make step_4 clean open` switches state, clears the build and opens the docs in one go.

> **Prerequisite:** Display, simple red/green strip, and buzzer working (Step 4 done).

**Files for this step:** `workshop/step_5/code.py` + `src/metro_rp2040/park_logic.py`

---

## Task

Replace the simple if/else logic with the full zone system from `park_logic.py`.

### 1. Add the import

```python
from park_logic import (
    mm_to_cm, format_dist_text, calc_num_leds, classify_zone, is_heartbeat_on,
    OFF, RED, GREEN, YELLOW, SPECIAL,
    DIST_MAX, VL53L0X_OUT_OF_RANGE_MM,
)
```

### 2. Add timing variables before the main loop

```python
last_heartbeat = time.monotonic()
last_blink     = time.monotonic()
last_beep      = time.monotonic()
blink_state    = True
beep_on        = False
```

### 3. Replace the simple buzzer and strip blocks

```python
now = time.monotonic()

# Heartbeat: onboard LED + NeoPixel (100 ms on / 900 ms off)
if now - last_heartbeat >= 1.0:
    last_heartbeat = now
if is_heartbeat_on(now - last_heartbeat):
    led.value = True;  pixel.fill(SPECIAL)
else:
    led.value = False; pixel.fill(OFF)

# Zone classification
if dist_cm <= 15:
    if now - last_blink >= 0.2:
        blink_state = not blink_state
        last_blink  = now

zone          = classify_zone(dist_cm, blink_state)
color         = zone["color"]
beep_interval = zone["beep_interval"]
color_label.text  = "Color: "  + zone["color_name"]
status_label.text = "Status: " + zone["status"]

# Buzzer: silent / continuous / timed interval
if beep_interval is None:
    buzzer.value = False
elif beep_interval == 0:
    buzzer.value = True
else:
    if now - last_beep >= beep_interval:
        beep_on = not beep_on
        buzzer.value = beep_on
        last_beep = now - (beep_interval - 0.08) if beep_on else now

# LED strip: number of LEDs scales with distance, filled from the right
num_leds = calc_num_leds(dist_cm)
for i in range(60):
    strip[i] = color if i >= (60 - num_leds) else OFF
strip.show()
```

---

## Zone Table

| Distance       | Colour   | LEDs            | Buzzer          |
|----------------|----------|-----------------|-----------------|
| > 30 cm        | Green    | few             | silent          |
| 20 – 30 cm     | Yellow   | moderate        | 1 s interval    |
| 15 – 20 cm     | Red      | many            | 0.4 s interval  |
| < 15 cm        | Blinking | full strip      | continuous      |

---

## Deploy

Copy **both** files to the `CIRCUITPY` drive:

- `workshop/step_5/code.py` → `code.py`
- `src/metro_rp2040/park_logic.py` → `park_logic.py`

---

## Verify

Walk through all four distance zones — strip, buzzer, and OLED all respond dynamically.

---

## Solution

`workshop/step_5/solutions/code.py`
