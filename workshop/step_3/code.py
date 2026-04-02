"""
Park Assist – Workshop Step 3 – Starting Point
===============================================

Current state: The display shows the measured distance.
Buzzer and LED strip are initialised but inactive.

Your task
---------
Add buzzer control to the main loop:
  - buzzer.value = True  → continuous beep when dist_cm < 20
  - buzzer.value = False → silent otherwise

Hint: dist_cm is available inside the `if raw_mm < 8190:` block.
"""

import board
import busio
import digitalio
import neopixel
import time
import displayio
import i2cdisplaybus
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1106
import adafruit_vl53l0x

# ── Onboard LED (D13) ────────────────────────────────────────────────────────
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# ── Onboard NeoPixel ─────────────────────────────────────────────────────────
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# ── NeoPixel Strip (D2) – stays off in this step ─────────────────────────────
strip = neopixel.NeoPixel(board.D2, 60, brightness=0.3, auto_write=False)
strip.fill((0, 0, 0))
strip.show()

# ── Buzzer (KY-012, D5) ───────────────────────────────────────────────────────
buzzer = digitalio.DigitalInOut(board.D5)
buzzer.direction = digitalio.Direction.OUTPUT
buzzer.value = False   # silent for now

# ── OLED Display (SH1106, 128×64, I2C 0x3C) ──────────────────────────────────
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)

# ── Boot splash ───────────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="Park Assist",  scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Step 3 – Buzzer", scale=1, color=0xFFFFFF, x=4,  y=50))
display.root_group = boot_group
time.sleep(2)

# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label = label.Label(terminalio.FONT, text="Dist: ---", color=0xFFFFFF, x=4, y=32)
splash.append(dist_label)

# ── Sensor init ───────────────────────────────────────────────────────────────
while not i2c.try_lock():
    pass
i2c.scan()
i2c.unlock()

try:
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    print("VL53L0X OK")
except Exception as e:
    vl53 = None
    dist_label.text = "Sensor error"
    print("Sensor error:", e)

print("Step 3 start – display only, buzzer pending")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    if vl53 is not None:
        raw_mm = vl53.range
        if raw_mm < 8190:
            dist_cm = raw_mm / 10.0
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)

            # ----------------------------------------------------------------
            # TODO Step 3: Add buzzer control here
            #
            #   if dist_cm < 20:
            #       buzzer.value = True    # continuous beep
            #   else:
            #       buzzer.value = False   # silent
            # ----------------------------------------------------------------

        else:
            dist_label.text = "Dist: out of range"
            buzzer.value = False
