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
        format_dist_text, calc_num_leds, classify_zone, is_heartbeat_on,
        OFF, RED, GREEN, YELLOW, SPECIAL,
        DIST_MAX,
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

dist_label  = label.Label(terminalio.FONT, text="Dist: ---",    color=0xFFFFFF, x=4, y=10)
color_label = label.Label(terminalio.FONT, text="Color: ---",   color=0xFFFFFF, x=4, y=30)
status_label = label.Label(terminalio.FONT, text="Status: ---", color=0xFFFFFF, x=4, y=50)
splash.append(dist_label)
splash.append(color_label)
splash.append(status_label)

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

print("Step 5 start – simple LED, replace with dynamic logic")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    # @ ToF Distance Reading, IM_SENSOR_READ, impl, [AR_SENSOR]
    if vl53 is not None and vl53.data_ready:
        dist_cm = vl53.distance   # cm, or None when out of range
        vl53.clear_interrupt()
        if dist_cm is not None:
            dist_label.text = "Dist: {:.1f} cm".format(dist_cm)

            # @ Buzzer Interval Control, IM_BUZ_CTRL, impl, [AR_BUZZER]
            # Buzzer: simple threshold (to be replaced)
            if dist_cm < 20:
                buzzer.value = True
            else:
                buzzer.value = False

            # @ LED Strip Zone Output, IM_LED_STRIP, impl, [AR_LED]
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
