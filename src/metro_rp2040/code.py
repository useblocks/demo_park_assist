"""
Metro RP2040 – CircuitPython Main Program
==========================================
Entry point: code.py (started automatically by CircuitPython)

Board:         Adafruit Metro RP2040 (AF5786)
Sensor:        GY-VL53L0X – adafruit_vl53l0x (range in mm, max ~2 m)
Requirements:  sw.md  (Setup 2)
Hardware:      hw.md  (Setup 2)
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

# ── NeoPixel Strip (ADA3636, 60 LEDs, D2) ────────────────────────────────────
# 3.3V supply: 60 LEDs at 30% brightness ≈ 324 mA (within 500 mA budget)
strip = neopixel.NeoPixel(board.D2, 60, brightness=0.3, auto_write=False)

# ── Buzzer (KY-012, D5) ───────────────────────────────────────────────────────
buzzer = digitalio.DigitalInOut(board.D5)
buzzer.direction = digitalio.Direction.OUTPUT

# ── OLED Display (SH1106, 128×64, I2C 0x3C) ──────────────────────────────────
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)

# ── Boot splash (3 s) ─────────────────────────────────────────────────────────
boot_group = displayio.Group()
boot_group.append(label.Label(terminalio.FONT, text="useblocks",          scale=2, color=0xFFFFFF, x=10, y=16))
boot_group.append(label.Label(terminalio.FONT, text="Workshop",           scale=1, color=0xFFFFFF, x=40, y=38))
boot_group.append(label.Label(terminalio.FONT, text="Park Assist v. 1.0", scale=1, color=0xFFFFFF, x=10, y=54))
display.root_group = boot_group
time.sleep(3)

# ── Main UI ───────────────────────────────────────────────────────────────────
splash = displayio.Group()
display.root_group = splash

dist_label = label.Label(terminalio.FONT, text="Dist: ---",    color=0xFFFFFF, x=4, y=10)
splash.append(dist_label)

color_label = label.Label(terminalio.FONT, text="Color: ---",  color=0xFFFFFF, x=4, y=30)
splash.append(color_label)

status_label = label.Label(terminalio.FONT, text="Status: ---", color=0xFFFFFF, x=4, y=50)
splash.append(status_label)

# ── Distance thresholds (cm) ─────────────────────────────────────────────────
DIST_MAX    = 40   # above this: 0 LEDs lit
DIST_GREEN  = 30   # > 20 cm → green, no beep
DIST_YELLOW = 20   # > 10 cm → yellow, slow beep
DIST_RED    = 15   

# VL53L0X returns 8190 mm when the target is out of range
_VL53L0X_OUT_OF_RANGE_MM = 8190

# ── Color constants ───────────────────────────────────────────────────────────
OFF     = (0,   0,   0)
RED     = (255, 0,   0)
GREEN   = (0,   255, 0)
BLUE    = (0,   0,   255)
YELLOW  = (255, 200, 0)
WHITE   = (255, 255, 255)
SPECIAL = (50,  200, 50)

# ── VL53L0X ToF Sensor (I2C) ─────────────────────────────────────────────────
# I2C scan: print all found addresses to serial + display
while not i2c.try_lock():
    pass
found = i2c.scan()
i2c.unlock()
print("I2C scan:", [hex(a) for a in found])
print("Sensor at 0x29:", 0x29 in found)

try:
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    # Optional: increase measurement budget for better accuracy (in microseconds)
    # vl53.measurement_timing_budget = 200000  # 200 ms – higher accuracy, slower rate
    dist_label.text = "Dist: sensor ready"
    print("VL53L0X sensor initialized")
except Exception as e:
    vl53 = None
    dist_label.text = "Err:" + str(e)[:18]
    print("VL53L0X init failed:", e)

# ── Initialization ────────────────────────────────────────────────────────────
print("Metro RP2040 CircuitPython started")
strip.fill(OFF)
strip.show()

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
    if now - last_heartbeat < 0.1:
        led.value = True
        pixel.fill(SPECIAL)
    else:
        led.value = False
        pixel.fill(OFF)

    # ToF distance reading (VL53L0X: synchronous, returns mm)
    if vl53 is not None:
        raw_mm = vl53.range
        if raw_mm < _VL53L0X_OUT_OF_RANGE_MM:
            dist = raw_mm / 10  # mm → cm
            dist_label.text = "Dist: {:.1f} cm".format(dist)

            # 0 LEDs at ≥ DIST_MAX cm, 60 LEDs at ≤ 0 cm
            num_leds = max(0, min(60, int((DIST_MAX - dist) * 60 / DIST_MAX)))

            if dist > DIST_GREEN:
                color = GREEN
                color_label.text  = "Color: Green"
                status_label.text = "Status: Steady"
                beep_interval = None        # no beep
            elif dist > DIST_YELLOW:
                color = YELLOW
                color_label.text  = "Color: Yellow"
                status_label.text = "Status: Steady"
                beep_interval = 1.0         # slow beep
            elif dist > DIST_RED:
                color = RED
                color_label.text  = "Color: Red"
                status_label.text = "Status: Steady"
                beep_interval = 0.4         # fast beep
            else:
                # Blink every 200 ms
                if now - last_blink >= 0.2:
                    blink_state = not blink_state
                    last_blink  = now
                color = RED if blink_state else OFF
                color_label.text  = "Color: Red"
                status_label.text = "Status: Blinking"
                beep_interval = 0           # continuous

            # Buzzer control
            if beep_interval is None:
                buzzer.value = False        # silent
            elif beep_interval == 0:
                buzzer.value = True         # continuous
            else:
                if now - last_beep >= beep_interval:
                    beep_on = not beep_on
                    buzzer.value = beep_on
                    if beep_on:             # short 80 ms pulse
                        last_beep = now - (beep_interval - 0.08)
                    else:                   # pause for full interval
                        last_beep = now

            for i in range(60):
                strip[i] = color if i >= (60 - num_leds) else OFF
            strip.show()
        else:
            dist_label.text   = "Dist: out of range"
            color_label.text  = "Color: ---"
            status_label.text = "Status: ---"
            strip.fill(OFF)
            strip.show()
            buzzer.value = False
