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
import adafruit_vl53l1x

RED   = (255, 0,   0)
GREEN = (0,   255, 0)
OFF   = (0,   0,   0)

# @ Hardware Peripheral Initialization, IM_HW_INIT, impl, [AR_INIT]
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

# @ Boot Splash Screen, IM_BOOT_SPLASH, impl, [AR_SPLASH]
# ── Boot splash ───────────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="useblocks",          scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Workshop",           scale=1, color=0xFFFFFF, x=40, y=38))
boot_group.append(label.Label(terminalio.FONT, text="Park Assist v. 1.0", scale=1, color=0xFFFFFF, x=10, y=54))
display.root_group = boot_group
time.sleep(3)

# @ Main UI Label Setup, IM_DISPLAY_SETUP, impl, [AR_DISPLAY]
# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label = label.Label(terminalio.FONT, text="Dist: ---", color=0xFFFFFF, x=4, y=32)
splash.append(dist_label)

# @ VL53L1X Sensor Initialization, IM_SENSOR_INIT, impl, [AR_SENSOR]
# ── Sensor init ───────────────────────────────────────────────────────────────
while not i2c.try_lock():
    pass
i2c.scan()
i2c.unlock()

try:
    vl53 = adafruit_vl53l1x.VL53L1X(i2c)
    vl53.distance_mode = 2   # long range (up to ~4 m); better no-target detection
    vl53.timing_budget = 100  # ms – 100 ms recommended for reliable readings
    vl53.start_ranging()
    print("VL53L1X OK")
except Exception as e:
    vl53 = None
    dist_label.text = "Sensor error"
    print("Sensor error:", e)

print("Step 4 start – display + buzzer, LED strip pending")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    # @ ToF Distance Reading, IM_SENSOR_READ, impl, [AR_SENSOR]
    if vl53 is not None and vl53.data_ready:
        dist_cm = vl53.distance   # cm, or None when out of range
        vl53.clear_interrupt()
        if dist_cm is not None:
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)

            # @ Buzzer Control, IM_BUZZER_CTRL, impl, [AR_BUZZER]
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
