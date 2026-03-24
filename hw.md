# Hardware Description – Metro Board Project

> This file is evaluated by the `metro` agent and updated when necessary.

---

## Setup 1: Prototype – Metro M4 Express + VL53L1X

*Single unit. Original build.*

**Per-unit cost: 79,20 €**

### Microcontroller

| Part No.  | Name                            | Qty | Unit Price | Total   | Description |
|-----------|---------------------------------|-----|------------|---------|-------------|
| ADA3382   | Adafruit Metro M4 Express       | 1   | 30,25 €    | 30,25 € | Arduino UNO-compatible microcontroller with ATSAMD51J19 (Cortex-M4, 120 MHz). Natively supports CircuitPython. Onboard: NeoPixel, red LED (D13), 2 MB Flash, UF2 bootloader. Pinout identical to Arduino UNO. |

### Sensors

| Part No.  | Name                                     | Qty | Unit Price | Total   | Description |
|-----------|------------------------------------------|-----|------------|---------|-------------|
| PIM373    | VL53L1X Time-of-Flight (ToF) Sensor      | 1   | 19,90 €    | 19,90 € | Laser distance sensor from ST Microelectronics. Range up to ~4 m, I2C interface. Provides precise distance measurements regardless of object color or reflectivity. |
| HC-SR04P  | HC-SR04P Ultrasonic Distance Sensor *(Alternative, not available)* | – | – | – | Low-cost ultrasonic distance sensor, 3.3–5 V logic (P-variant). Range up to ~4 m, GPIO interface (Trig + Echo). CircuitPython library `adafruit_hcsr04` available in Adafruit Bundle. Not currently in use. |

### Display & Output

| Part No.      | Name                                           | Qty | Unit Price | Total   | Description |
|---------------|------------------------------------------------|-----|------------|---------|-------------|
| ADA3636       | Adafruit NeoPixel LED Side Light Strip, 1 m    | 1   | 19,75 €    | 19,75 € | 60 addressable RGB LEDs (WS2812B) on 1 m, side-emitting. Controlled via a single data wire. Nominal operating voltage 5 V; currently wired directly to the Metro's 3.3 V rail. Data line is connected directly without a series resistor. The bulk capacitor is not installed. |
| OLED-12864-B  | 1.3" OLED Display 128×64, SH1106, I2C, blue   | 1   | 6,70 €     | 6,70 €  | Monochrome OLED display with SH1106 controller. Resolution 128×64 px, I2C interface (address 0x3C/0x3D). Very low power consumption, high contrast, no backlight required. |
| KY-012        | Active Buzzer Module                           | 2   | 1,30 €     | 2,60 €  | Active piezo buzzer (generates tone without external frequency signal), directly drivable via GPIO. Operating voltage 3.3–5 V. |

---

## Setup 2: Workshop – Metro RP2040 + VL53L0X

*5 units, ordered 2026-03-11.*

**Per-unit cost: 56,16 € — Total for 5 units: 280,82 €**

> **Code note:** VL53L0X requires `adafruit_vl53l0x` library (different from `adafruit_vl53l1x` in Setup 1). Maximum range is 2 m instead of 4 m. Code adjustments pending.

### Microcontroller

| Part No.  | Name                                            | Qty | Unit Price | Total   | Description |
|-----------|-------------------------------------------------|-----|------------|---------|-------------|
| AF5786    | Adafruit Metro RP2040 133MHz, 16MB Flash, USB-C | 5   | 17,95 €    | 89,73 € | Arduino UNO-compatible microcontroller with RP2040 (dual-core Cortex-M0+, 133 MHz). Natively supports CircuitPython. Onboard: NeoPixel, red LED (D13), 16 MB Flash, USB-C port, UF2 bootloader. Pinout identical to Arduino UNO. |

### Sensors

| Part No.  | Name                                              | Qty | Unit Price | Total   | Description |
|-----------|---------------------------------------------------|-----|------------|---------|-------------|
| SE01011   | GY-VL53L0X Time-of-Flight Distance Sensor Module | 5   | 9,95 €     | 49,74 € | Carrier board for ST VL53L0X ToF sensor. Range up to 2 m, I2C interface (address 0x29). Requires `adafruit_vl53l0x` library. Runs directly on 3.3 V logic. |

### Display & Output

| Part No.      | Name                                           | Qty | Unit Price | Total   | Description |
|---------------|------------------------------------------------|-----|------------|---------|-------------|
| ADA3636       | Adafruit NeoPixel LED Side Light Strip, 1 m    | 5   | 19,75 €    | 98,75 € | 60 addressable RGB LEDs (WS2812B) on 1 m, side-emitting. Controlled via a single data wire. |
| OLED-12864-B  | 1.3" OLED Display 128×64, SH1106, I2C, blue   | 5   | 6,70 €     | 33,50 € | Monochrome OLED display with SH1106 controller. Resolution 128×64 px, I2C interface (address 0x3C/0x3D). |
| KY-012        | Active Buzzer Module                           | 7   | 1,30 €     | 9,10 €  | Active piezo buzzer, directly drivable via GPIO. Operating voltage 3.3–5 V. |

---

## Shared Tools & Consumables

*Not counted towards per-unit setup costs.*

### Passive Components

| Part No.      | Name                                                | Qty | Unit Price | Total  | Build   | Description |
|---------------|-----------------------------------------------------|-----|------------|--------|---------|-------------|
| ELK1M25VAWH   | Electrolytic Capacitor 1000 µF, 25 V, radial, THT  | 2   | 0,21 €     | 0,42 € | Setup 1 | Bulk capacitor for power supply. Smooths voltage spikes caused by NeoPixel strip. **Not currently installed.** |
| MSW330R.25    | Metal Film Resistor 330 Ω, 1/4 W, axial, THT       | 5   | 0,05 €     | 0,25 € | Setup 1 | Current-limiting / data line protection resistor. **Not installed on the NeoPixel data line in the current setup.** |

### Accessories & Power

| Part No.          | Name                                              | Qty | Unit Price | Total   | Build    | Description |
|-------------------|---------------------------------------------------|-----|------------|---------|----------|-------------|
| BB-830P           | Breadboard, 830 tie points                        | 6   | 1,90 €     | 11,40 € | Both     | Solderless prototyping board. 830 contacts, compatible with standard jumper wires and THT components. (1 × Setup 1, 5 × Setup 2) |
| DUPK-40-MM-10     | Jumper Wire Male–Male, 40-pin, 10 cm              | 3   | 1,60 €     | 4,80 €  | Both     | Short connection cables for direct wiring from board to breadboard. (1 × Setup 1, 2 × Setup 2) |
| JUMPER-WIRE-65    | Jumper Wire Kit, 65 wires in 4 lengths            | 1   | 1,40 €     | 1,40 €  | Setup 1  | Male jumper wire set for breadboard use. Various lengths for a tidy layout. |
| 45040             | USB-C Power Supply 5 V / 3 A                      | 1   | –          | –       | Setup 1  | Stationary power source for prototype. 3 A sufficient for Metro M4 + NeoPixel strip (max. ~3.6 A at full brightness). |
| 45735             | USB-C 2.0 Cable A–C, 1.0 m, black                | 5   | 2,90 €     | 14,50 € | Setup 2  | Data/power cable for workshop boards. |
| 53932             | Compact Powerbank, 5,000 mAh, black              | 2   | 12,09 €    | 24,18 € | Setup 2  | Mobile power supply for workshop use. |

---

## Interface Overview (Metro M4 – Setup 1)

| Interface | Pins                                      | Usage in Project               |
|-----------|-------------------------------------------|--------------------------------|
| I2C       | `board.SCL` / `board.SDA`                 | ToF sensor, OLED display       |
| GPIO      | `board.D5`, `board.D6`                    | Buzzer 1 (D5), Buzzer 2 (D6)  |
| NeoPixel  | `board.NEOPIXEL`                          | Onboard RGB LED                |
| GPIO      | `board.D2`                                | NeoPixel strip (ADA3636, 60 LEDs) |
| LED       | `board.LED` (D13)                         | Status / heartbeat             |

> Interface mapping for Metro RP2040 (Setup 2) is pending code adjustments.

---

## Notes (Setup 1 – Metro M4)

| Component      | Pin / Address         | Notes                              |
|----------------|-----------------------|------------------------------------|
| Buzzer 1       | `board.D5`            | KY-012, S→D5, +→5V, –→GND         |
| Buzzer 2       | `board.D6`            | KY-012, S→D6, +→5V, –→GND         |
| ToF Sensor     | I2C `0x29`            | SCL→SCL, SDA→SDA, VCC→3.3V, GND→GND |
| OLED Display   | I2C `0x3C`            | SCL→SCL, SDA→SDA, VCC→3.3V, GND→GND |
| NeoPixel Strip | `board.D2`            | DIN→D2 (no series resistor), VCC→3.3V, GND→GND. No bulk capacitor installed. |
