"""
Park Assist – Workshop Step 5 – Solution
=========================================

Full dynamic park-assist system using park_logic.py:
  - 4 distance zones (green / yellow / red-steady / red-blinking)
  - LED count scales linearly with distance (0–60 LEDs)
  - Buzzer interval per zone (silent / 1 s / 0.4 s / continuous)
  - Heartbeat on onboard LED + NeoPixel
  - Colour and status shown on OLED

Copy both code.py AND park_logic.py to the CIRCUITPY drive.
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
from park_logic import (
    mm_to_cm, format_dist_text, calc_num_leds, classify_zone, is_heartbeat_on,
    OFF, RED, GREEN, YELLOW, SPECIAL,
    DIST_MAX, VL53L0X_OUT_OF_RANGE_MM,
)

# ── Onboard LED (D13) ────────────────────────────────────────────────────────
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# ── Onboard NeoPixel ─────────────────────────────────────────────────────────
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# ── NeoPixel Strip (ADA3636, 60 LEDs, D2) ────────────────────────────────────
strip = neopixel.NeoPixel(board.D2, 60, brightness=0.3, auto_write=False)

# ── Buzzer (KY-012, D5) ───────────────────────────────────────────────────────
buzzer = digitalio.DigitalInOut(board.D5)
buzzer.direction = digitalio.Direction.OUTPUT

# ── OLED Display (SH1106, 128×64, I2C 0x3C) ──────────────────────────────────
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)

# ── Boot splash ───────────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="Park Assist",    scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Step 5 – Done",  scale=1, color=0xFFFFFF, x=10, y=50))
display.root_group = boot_group
time.sleep(2)

# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label   = label.Label(terminalio.FONT, text="Dist: ---",    color=0xFFFFFF, x=4, y=10)
color_label  = label.Label(terminalio.FONT, text="Color: ---",   color=0xFFFFFF, x=4, y=30)
status_label = label.Label(terminalio.FONT, text="Status: ---",  color=0xFFFFFF, x=4, y=50)
splash.append(dist_label)
splash.append(color_label)
splash.append(status_label)

# ── Sensor init ───────────────────────────────────────────────────────────────
while not i2c.try_lock():
    pass
found = i2c.scan()
i2c.unlock()
print("I2C scan:", [hex(a) for a in found])

try:
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    dist_label.text = "Dist: sensor ready"
    print("VL53L0X OK")
except Exception as e:
    vl53 = None
    dist_label.text = "Err:" + str(e)[:18]
    print("VL53L0X init failed:", e)

strip.fill(OFF)
strip.show()
print("Step 5 solution – full dynamic system")

# ── Main loop ─────────────────────────────────────────────────────────────────
last_heartbeat = time.monotonic()
last_blink     = time.monotonic()
last_beep      = time.monotonic()
blink_state    = True
beep_on        = False

while True:
    now = time.monotonic()

    # Heartbeat: onboard LED + NeoPixel, 100 ms on / 900 ms off
    if now - last_heartbeat >= 1.0:
        last_heartbeat = now
    if is_heartbeat_on(now - last_heartbeat):
        led.value = True
        pixel.fill(SPECIAL)
    else:
        led.value = False
        pixel.fill(OFF)

    if vl53 is not None:
        raw_mm = vl53.range
        dist = mm_to_cm(raw_mm)
        if dist is not None:
            dist_label.text = format_dist_text(dist)
            num_leds = calc_num_leds(dist)

            # Critical zone: update blink state
            if dist <= 15:
                if now - last_blink >= 0.2:
                    blink_state = not blink_state
                    last_blink  = now

            zone          = classify_zone(dist, blink_state)
            color         = zone["color"]
            beep_interval = zone["beep_interval"]
            color_label.text  = "Color: "  + zone["color_name"]
            status_label.text = "Status: " + zone["status"]

            # Buzzer: silent / continuous / interval beep
            if beep_interval is None:
                buzzer.value = False
            elif beep_interval == 0:
                buzzer.value = True
            else:
                if now - last_beep >= beep_interval:
                    beep_on = not beep_on
                    buzzer.value = beep_on
                    if beep_on:
                        last_beep = now - (beep_interval - 0.08)
                    else:
                        last_beep = now

            # LED strip: num_leds lit from the right, colour from zone
            for i in range(60):
                strip[i] = color if i >= (60 - num_leds) else OFF
            strip.show()

        else:
            dist_label.text   = format_dist_text(None)
            color_label.text  = "Color: ---"
            status_label.text = "Status: ---"
            strip.fill(OFF)
            strip.show()
            buzzer.value = False
