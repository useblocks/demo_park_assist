# Welcome to Park Assist Demo 👋

This repository contains the **CircuitPython source code** and **Sphinx-Needs documentation**
for the Park Assist Demo project running on the **Adafruit Metro RP2040** (Setup 2).

---

## Quick Start

| Command | Description |
|---|---|
| `make test` | Run the 35 boardless pytest tests |
| `make html` | Build the Sphinx HTML documentation |
| `make serve` | Build docs and serve on port 8080 (opens in browser) |
| `make clean` | Remove build output |

---

## Repository Structure

```
src/metro_rp2040/
  code.py          CircuitPython main program (runs on board)
  park_logic.py    Pure Python logic – zone classification, distance, buzzer

docs/
  user_stories.rst  US_001–US_008
  architecture.rst  AR_001–AR_008 (with Mermaid diagrams)
  implementation.rst IM_001–IM_009 (CodeLinks – extracted from source)
  test_cases.rst    TC_001–TC_013

tests/
  test_distance.py  TC_004, TC_005
  test_heartbeat.py TC_003
  test_zone.py      TC_006–TC_009
  test_buzzer.py    TC_010–TC_013
```

---

## Setup

The virtual environment is created automatically when the Codespace starts.
If you need to recreate it manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
```

---

## Hardware (Setup 2 – Metro RP2040)

| Component | Part | Interface |
|---|---|---|
| MCU | Adafruit Metro RP2040 (AF5786) | – |
| ToF Sensor | GY-VL53L0X (SE01011) | I2C 0x29 |
| OLED Display | SH1106 128×64 (OLED-12864-B) | I2C 0x3C |
| LED Strip | NeoPixel 60 LEDs (ADA3636) | D2 |
| Buzzer | KY-012 Active Buzzer | D5 |
