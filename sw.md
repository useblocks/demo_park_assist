# Software Requirements – Metro Board CircuitPython

> This file is evaluated by the `metro` agent and updated when necessary.
> Describe here what the software is expected to do.

---

## Software Overview

| Property           | Value                                      |
|--------------------|--------------------------------------------|
| Platform           | CircuitPython                              |
| Boards             | Metro M4 Express (Setup 1), Metro RP2040 (Setup 2) |
| Source folders     | `src/metro_m4/`, `src/metro_rp2040/`       |
| Entry point        | `code.py`                                  |
| Status             | In development                             |

---

## Setup 1 – Metro M4 Express

### Dependencies

| Library                       | Source                        | Purpose                      |
|-------------------------------|-------------------------------|------------------------------|
| `neopixel`                    | Adafruit CircuitPython Bundle | NeoPixel RGB LED control     |
| `adafruit_displayio_sh1106`   | Adafruit CircuitPython Bundle | SH1106 OLED display driver   |
| `adafruit_display_text`       | Adafruit CircuitPython Bundle | Text labels on display       |
| `adafruit_vl53l1x`            | Adafruit CircuitPython Bundle | VL53L1X ToF distance sensor  |

### Sensor Notes (VL53L1X)

- Library: `adafruit_vl53l1x`
- Distance returned in **cm**
- Supports `distance_mode`, `timing_budget`, `start_ranging()`, `data_ready`, `clear_interrupt()`
- Max range: ~4 m

---

## Setup 2 – Metro RP2040

### Dependencies

| Library                       | Source                        | Purpose                      |
|-------------------------------|-------------------------------|------------------------------|
| `neopixel`                    | Adafruit CircuitPython Bundle | NeoPixel RGB LED control     |
| `adafruit_displayio_sh1106`   | Adafruit CircuitPython Bundle | SH1106 OLED display driver   |
| `adafruit_display_text`       | Adafruit CircuitPython Bundle | Text labels on display       |
| `adafruit_vl53l0x`            | Adafruit CircuitPython Bundle | VL53L0X ToF distance sensor  |

### Sensor Notes (VL53L0X)

- Library: `adafruit_vl53l0x`
- Distance returned in **mm** → converted to cm via `range / 10`
- Out-of-range value: `8190 mm` (handled as no measurement)
- No `distance_mode`, `timing_budget`, `start_ranging()`, `data_ready`, or `clear_interrupt()`
- Optional accuracy tuning: `sensor.measurement_timing_budget` (in µs)
- Max range: ~2 m

---

## Functional Requirements

Apply to both setups unless noted.

| ID    | Requirement                                    | Setup   | Status       | Priority |
|-------|------------------------------------------------|---------|--------------|----------|
| SW-01 | Board starts without errors                    | Both    | ☐ Open       | High     |
| SW-02 | Status LED (D13) blinks at heartbeat rate      | Both    | ☐ Open       | Medium   |
| SW-03 | OLED shows status text on startup              | Both    | ☐ Open       | Medium   |
| SW-04 | ToF distance displayed live on OLED            | Both    | ☐ Open       | High     |
| SW-05 | NeoPixel strip reflects distance zone (color)  | Both    | ☐ Open       | High     |
| SW-06 | Buzzer beeps according to distance zone        | Both    | ☐ Open       | High     |

**Status legend:** ☐ Open · 🔄 In Progress · ✅ Done · ❌ Rejected

---

## Non-Functional Requirements

| ID     | Requirement                                                  | Status  |
|--------|--------------------------------------------------------------|---------|
| NFR-01 | Code runs exclusively on CircuitPython (no CPython)          | ☐ Open  |
| NFR-02 | RAM usage stays below 80% of available RAM                   | ☐ Open  |
| NFR-03 | No blocking infinite waits without watchdog                  | ☐ Open  |

---

## Architecture / Modules

| Path                          | Description                                            |
|-------------------------------|--------------------------------------------------------|
| `src/metro_m4/code.py`        | Main program for Metro M4 (VL53L1X)                    |
| `src/metro_m4/boot.py`        | Boot config for Metro M4                               |
| `src/metro_m4/lib/`           | Libraries for Metro M4 (incl. `adafruit_vl53l1x`)     |
| `src/metro_rp2040/code.py`    | Main program for Metro RP2040 (VL53L0X)                |
| `src/metro_rp2040/boot.py`    | Boot config for Metro RP2040                           |
| `src/metro_rp2040/lib/`       | Libraries for Metro RP2040 (incl. `adafruit_vl53l0x`)  |

---

## Open Issues / TODOs

- [ ] Verify RP2040 code on hardware (Setup 2)
- [ ] Test VL53L0X distance accuracy and out-of-range handling

---

## Changelog

| Date       | Change                                                    |
|------------|-----------------------------------------------------------|
| 2026-03-07 | Initial file created                                      |
| 2026-03-25 | Split into two board setups; added RP2040 / VL53L0X notes |
