"""
Metro Board – CircuitPython Main Program
========================================
Entry point: code.py (started automatically by CircuitPython)

Requirements:  sw.md
Hardware:      hw.md
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

# ── Onboard LED (D13) ────────────────────────────────────────────────────────
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# ── Onboard NeoPixel ─────────────────────────────────────────────────────────
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# ── Buzzer (KY-012, D5) ───────────────────────────────────────────────────────
buzzer = digitalio.DigitalInOut(board.D5)
buzzer.direction = digitalio.Direction.OUTPUT

# ── OLED Display (SH1106, 128×64, I2C 0x3C) ──────────────────────────────────
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64)

splash = displayio.Group()
display.root_group = splash

dist_label = label.Label(terminalio.FONT, text="Dist: --- mm", color=0xFFFFFF, x=4, y=10)
splash.append(dist_label)

scroll_label = label.Label(terminalio.FONT, text="Hello Richard!", color=0xFFFFFF, x=128, y=50)
splash.append(scroll_label)
# Each char is ~6px wide; text width ≈ 14 chars × 6 = 84px
SCROLL_TEXT_WIDTH = 84

# ── Color constants ───────────────────────────────────────────────────────────
# RGB = Rot, Grün, Blau  = 0-255 == 0- 100%
OFF   = (0,   0,   0)
RED   = (255, 0,   0)
GREEN = (0,   255, 0)
BLUE  = (0,   0,   255)
RICHARD  = (200,   50,   50)
LEONIE = (50,  200,  50)

# ── VL53L1X ToF Sensor (I2C) ────────────────────────────────────────────────
# I2C scan: print all found addresses to serial + display
while not i2c.try_lock():
    pass
found = i2c.scan()
i2c.unlock()
print("I2C scan:", [hex(a) for a in found])
print("Sensor at 0x29:", 0x29 in found)
dist_label.text = "0x29:" + ("OK" if 0x29 in found else "MISS") + \
                  " 0x3c:" + ("OK" if 0x3C in found else "MISS")
time.sleep(3)  # pause so scan result is readable

try:
    vl53 = adafruit_vl53l1x.VL53L1X(i2c)
    vl53.distance_mode = 1  # 1 = short range (up to ~1.3 m), 2 = long range (up to ~4 m)
    vl53.timing_budget = 50  # ms
    vl53.start_ranging()
    dist_label.text = "Dist: sensor ready"
    print("VL53L1X sensor initialized")
except Exception as e:
    vl53 = None
    dist_label.text = "Err:" + str(e)[:18]
    print("VL53L1X init failed:", e)

# ── Initialization ────────────────────────────────────────────────────────────
print("Metro CircuitPython started")

# ── Main loop ─────────────────────────────────────────────────────────────────
last_beep = time.monotonic()

while True:
    now = time.monotonic()

    # Buzzer: 0.1 s beep every 2 s
    # if now - last_beep >= 2.0:
    #     buzzer.value = True
    #     time.sleep(0.1)
    #     buzzer.value = False
    #     last_beep = time.monotonic()

    # Heartbeat LED
    led.value = True
    pixel.fill(LEONIE)
    time.sleep(0.1)
    led.value = False
    pixel.fill(OFF)
    time.sleep(0.05)

    # ToF distance reading
    if vl53 is not None and vl53.data_ready:
        dist = vl53.distance
        if dist is not None:
            dist_label.text = "Dist: {} mm".format(dist)
        else:
            dist_label.text = "Dist: out of range"
        vl53.clear_interrupt()

    # Scroll "Hello Richard!" from right to left
    scroll_label.x -= 4
    if scroll_label.x < -SCROLL_TEXT_WIDTH:
        scroll_label.x = 128
