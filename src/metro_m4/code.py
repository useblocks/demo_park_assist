"""
Metro M4 Express – Deploy Notes
=================================
Both Setup 1 (Metro M4) and Setup 2 (Metro RP2040) now use the VL53L1X sensor
and the ``adafruit_vl53l1x`` library.  The source files in ``src/`` are shared.

To deploy on Metro M4:
  1. Copy src/code.py       → CIRCUITPY/code.py
  2. Copy src/park_logic.py → CIRCUITPY/park_logic.py
  3. Copy src/metro_m4/lib/ → CIRCUITPY/lib/

No code changes are needed – src/code.py already uses adafruit_vl53l1x.
"""

