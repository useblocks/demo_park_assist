"""
Park Assist – Workshop Step 4 – Starting Point
===============================================

Current state: display shows distance, buzzer beeps when dist < 20 cm.
LED strip is initialised but stays off.

Your task
---------
Add LED strip control in the main loop:
  - All 60 LEDs RED   when dist_cm < 20
  - All 60 LEDs GREEN when dist_cm >= 20
  - Strip off         when out of range

Useful constants:
    RED   = (255, 0,   0)
    GREEN = (0,   255, 0)
    OFF   = (0,   0,   0)

Useful methods:
    strip.fill(color)  – set all LEDs to one color
    strip.show()       – push the changes to the hardware
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

RED   = (255, 0,   0)
GREEN = (0,   255, 0)
OFF   = (0,   0,   0)

# @ Hardware Peripheral Initialization, IM_001, impl, [AR_001]
# ── Onboard LED (D13) ────────────────────────────────────────────────────────
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# ── Onboard NeoPixel ─────────────────────────────────────────────────────────
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# ── NeoPixel Strip (D2) ───────────────────────────────────────────────────────
strip = neopixel.NeoPixel(board.D2, 60, brightness=0.3, auto_write=False)
strip.fill(OFF)
strip.show()

# ── Buzzer (KY-012, D5) ───────────────────────────────────────────────────────
buzzer = digitalio.DigitalInOut(board.D5)
buzzer.direction = digitalio.Direction.OUTPUT
buzzer.value = False

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

print("Step 4 start – display + buzzer, LED strip pending")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    # @ ToF Distance Reading and Unit Conversion, IM_006, impl, [AR_003]
    if vl53 is not None:
        raw_mm = vl53.range
        if raw_mm < 8190:
            dist_cm = raw_mm / 10.0
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)

            # @ Buzzer Interval Control, IM_008, impl, [AR_007]
            # Buzzer: continuous beep below 20 cm
            if dist_cm < 20:
                buzzer.value = True
            else:
                buzzer.value = False

            # ----------------------------------------------------------------
            # TODO Step 4: Add LED strip control here
            #
            #   if dist_cm < 20:
            #       strip.fill(RED)
            #   else:
            #       strip.fill(GREEN)
            #   strip.show()
            # ----------------------------------------------------------------

        else:
            dist_label.text = "Dist: out of range"
            buzzer.value = False
            # TODO Step 4: also turn off the strip when out of range
            #   strip.fill(OFF)
            #   strip.show()
