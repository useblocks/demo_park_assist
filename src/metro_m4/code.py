"""
Metro M4 Express – Delta vs. src/code.py (RP2040 baseline)
============================================================
The Metro M4 uses a different ToF sensor (VL53L1X instead of VL53L0X).
All other hardware and logic is identical to the RP2040 baseline.

To deploy on Metro M4:
  1. Copy src/code.py      → CIRCUITPY/code.py
  2. Copy src/park_logic.py → CIRCUITPY/park_logic.py
  3. Copy src/metro_m4/lib/ → CIRCUITPY/lib/
  4. Apply the three delta blocks below to CIRCUITPY/code.py

──────────────────────────────────────────────────────────────
DELTA 1 – Sensor import  (replaces: import adafruit_vl53l0x)
──────────────────────────────────────────────────────────────

import adafruit_vl53l1x

──────────────────────────────────────────────────────────────
DELTA 2 – Sensor init
  replaces:
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
──────────────────────────────────────────────────────────────

    vl53 = adafruit_vl53l1x.VL53L1X(i2c)
    vl53.distance_mode = 1   # 1 = short range (up to ~1.3 m)
    vl53.timing_budget = 50  # ms
    vl53.start_ranging()

──────────────────────────────────────────────────────────────
DELTA 3 – Sensor read  (replaces the VL53L0X read block)
  replaces:
    raw_mm = vl53.range
    dist   = mm_to_cm(raw_mm)

    if dist is not None:
        ...
    else:
        ...
──────────────────────────────────────────────────────────────

    if vl53.data_ready:
        dist = vl53.distance   # already in cm; None when out of range
        vl53.clear_interrupt()

        if dist is not None:
            ...              # same zone/buzzer/strip logic as baseline
        else:
            ...              # same out-of-range handling as baseline
"""

