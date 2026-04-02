"""
Park Assist – Workshop Step 5 – Starting Point
===============================================

Current state: display, buzzer (< 20 cm), and a simple red/green LED strip.

Your task
---------
Replace the simple two-colour logic with a full zone system using park_logic:

  Zone        Distance        LEDs            Buzzer
  ──────────  ──────────────  ──────────────  ───────────────
  Green       > 30 cm         fill green      silent
  Yellow      20 – 30 cm      fill yellow     slow beep (1 s)
  Red steady  15 – 20 cm      fill red        fast beep (0.4 s)
  Red blink   < 15 cm         blink red       continuous

The number of lit LEDs should also scale with distance (60 at 0 cm, 0 at 40 cm).

Use the helpers from park_logic.py (copy it to the board alongside this file):
    from park_logic import (
        mm_to_cm, format_dist_text, calc_num_leds, classify_zone, is_heartbeat_on,
        OFF, RED, GREEN, YELLOW, SPECIAL,
        DIST_MAX, VL53L0X_OUT_OF_RANGE_MM,
    )

Replace the inline if/else logic in the main loop with calls to
classify_zone() and calc_num_leds().
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

# ── Boot splash ───────────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="Park Assist",      scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Step 5 – Dynamic", scale=1, color=0xFFFFFF, x=4,  y=50))
display.root_group = boot_group
time.sleep(2)

# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label  = label.Label(terminalio.FONT, text="Dist: ---",    color=0xFFFFFF, x=4, y=10)
color_label = label.Label(terminalio.FONT, text="Color: ---",   color=0xFFFFFF, x=4, y=30)
status_label = label.Label(terminalio.FONT, text="Status: ---", color=0xFFFFFF, x=4, y=50)
splash.append(dist_label)
splash.append(color_label)
splash.append(status_label)

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

print("Step 5 start – simple LED, replace with dynamic logic")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    if vl53 is not None:
        raw_mm = vl53.range
        if raw_mm < 8190:
            dist_cm = raw_mm / 10.0
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)

            # Buzzer: simple threshold (to be replaced)
            if dist_cm < 20:
                buzzer.value = True
            else:
                buzzer.value = False

            # LED strip: simple red/green (to be replaced with zone logic)
            if dist_cm < 20:
                strip.fill(RED)
            else:
                strip.fill(GREEN)
            strip.show()

            # TODO Step 5: replace the blocks above with:
            #
            # zone = classify_zone(dist_cm, blink_state)
            # color_label.text  = "Color: "  + zone["color_name"]
            # status_label.text = "Status: " + zone["status"]
            #
            # Buzzer from zone["beep_interval"]
            # LED strip from calc_num_leds(dist_cm) + zone["color"]

        else:
            dist_label.text = "Dist: out of range"
            color_label.text  = "Color: ---"
            status_label.text = "Status: ---"
            buzzer.value = False
            strip.fill(OFF)
            strip.show()
