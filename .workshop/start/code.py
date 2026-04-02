"""
Park Assist – Metro RP2040 – CircuitPython Main Program
========================================================
Entry point: code.py (started automatically by CircuitPython)

Board:   Adafruit Metro RP2040 (AF5786)
Sensor:  GY-VL53L0X – adafruit_vl53l0x (range in mm, max ~2 m)

Deploy
------
Copy this file as code.py to the CIRCUITPY drive.

Requirements: sw.md  Hardware: hw.md
"""

import board
import busio
import time
import displayio
import i2cdisplaybus
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1106
import adafruit_vl53l0x

# ── OLED Display (SH1106, 128×64, I2C 0x3C) ──────────────────────────────────
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)

# @ Boot Splash Screen, IM_002, impl, [AR_002]
# ── Boot splash ───────────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="useblocks",          scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Workshop",           scale=1, color=0xFFFFFF, x=40, y=38))
boot_group.append(label.Label(terminalio.FONT, text="Park Assist v. 1.0", scale=1, color=0xFFFFFF, x=10, y=54))
display.root_group = boot_group
time.sleep(3)

# @ Main UI Label Setup, IM_003, impl, [AR_005]
# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label = label.Label(terminalio.FONT, text="Dist: ---", color=0xFFFFFF, x=4, y=32)
splash.append(dist_label)

# @ VL53L0X Sensor Initialization, IM_004, impl, [AR_003]
# ── VL53L0X ToF Sensor (I2C) ─────────────────────────────────────────────────
time.sleep(0.5)  # allow sensor to power up before init
while not i2c.try_lock():
    pass
i2c.scan()
i2c.unlock()

try:
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    print("VL53L0X OK")
except Exception as e:
    vl53 = None
    dist_label.text = "Err:" + str(e)[:18]
    print("Sensor error:", e)

print("Park Assist started – display only")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    # @ ToF Distance Reading and Unit Conversion, IM_006, impl, [AR_003]
    if vl53 is not None:
        raw_mm = vl53.range
        if raw_mm < 8190:
            dist_cm = raw_mm / 10.0
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)
        else:
            dist_label.text = "Dist: out of range"
