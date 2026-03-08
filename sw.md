# Software Requirements – Metro Board CircuitPython

> This file is evaluated by the `metro` agent and updated when necessary.
> Describe here what the software is expected to do.

---

## Software Overview

| Property           | Value                             |
|--------------------|-----------------------------------|
| Platform           | CircuitPython                     |
| Board              | Adafruit Metro (see `hw.md`)      |
| Entry point        | `code.py`                         |
| Status             | In development                    |

---

## Dependencies / Libraries

| Library                  | Version | Source                        | Purpose                      |
|--------------------------|---------|-------------------------------|------------------------------|
| `adafruit_neopixel`           | –       | Adafruit CircuitPython Bundle | NeoPixel RGB LED control     |
| `adafruit_displayio_sh1106`   | –       | Adafruit CircuitPython Bundle | SH1106 OLED display driver   |
| `adafruit_display_text`       | –       | Adafruit CircuitPython Bundle | Text labels on display       |
| `adafruit_vl53l1x`            | –       | Adafruit CircuitPython Bundle | VL53L1X ToF distance sensor  |

---

## Functional Requirements

| ID    | Requirement                                  | Status       | Priority |
|-------|----------------------------------------------|--------------|----------|
| SW-01 | Board starts without errors                  | ☐ Open       | High     |
| SW-02 | Status LED (D13) blinks at heartbeat rate    | ☐ Open       | Medium   |
| SW-03 | OLED shows status text on startup            | ☐ Open       | Medium   |
| SW-04 | ToF distance displayed live on OLED         | ☐ Open       | High     |

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

| Module / File   | Description                                     |
|-----------------|-------------------------------------------------|
| `code.py`       | Main program, main loop                         |
| `boot.py`       | Board configuration at startup (optional)       |
| `lib/`          | External libraries (Adafruit Bundle)            |

---

## Open Issues / TODOs

- [ ] Complete hardware details in `hw.md`
- [ ] Add concrete requirements

---

## Changelog

| Date       | Change                           |
|------------|----------------------------------|
| 2026-03-07 | Initial file created             |
