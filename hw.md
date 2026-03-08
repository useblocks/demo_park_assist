# Hardware Description – Metro Board Project

> This file is evaluated by the `metro` agent and updated when necessary.

---

## Microcontroller

| Part No.  | Name                            | Qty | Description |
|-----------|---------------------------------|-----|-------------|
| ADA3382   | Adafruit Metro M4 Express       | 1   | Arduino UNO-compatible microcontroller with ATSAMD51J19 (Cortex-M4, 120 MHz). Natively supports CircuitPython. Onboard: NeoPixel, red LED (D13), 2 MB Flash, UF2 bootloader. Pinout identical to Arduino UNO. |

---

## Sensors

| Part No.  | Name                                     | Qty | Description |
|-----------|------------------------------------------|-----|-------------|
| PIM373    | VL53L1X Time-of-Flight (ToF) Sensor      | 1   | Laser distance sensor from ST Microelectronics. Range up to ~4 m, I2C interface. Provides precise distance measurements regardless of object color or reflectivity. |

---

## Display & Output

| Part No.      | Name                                           | Qty | Description |
|---------------|------------------------------------------------|-----|-------------|
| ADA3636       | Adafruit NeoPixel LED Side Light Strip, 1 m    | 1   | 60 addressable RGB LEDs (WS2812B) on 1 m, side-emitting. Controlled via a single data wire. Operating voltage 5 V, up to 60 mA per LED (RGB full white). |
| OLED-12864-B  | 1.3" OLED Display 128×64, SH1106, I2C, blue   | 1   | Monochrome OLED display with SH1106 controller. Resolution 128×64 px, I2C interface (address 0x3C/0x3D). Very low power consumption, high contrast, no backlight required. |
| KY-012        | Active Buzzer Module                           | 2   | Active piezo buzzer (generates tone without external frequency signal), directly drivable via GPIO. Operating voltage 3.3–5 V. Suitable for simple acoustic signals and alarms. |

---

## Passive Components

| Part No.      | Name                                                | Qty | Description |
|---------------|-----------------------------------------------------|-----|-------------|
| ELK1M25VAWH   | Electrolytic Capacitor 1000 µF, 25 V, radial, THT  | 2   | Bulk capacitor for the power supply. Smooths voltage spikes caused e.g. by switching on the NeoPixel strip. Place between the 5 V rail and GND. |
| MSW330R.25    | Metal Film Resistor 330 Ω, 1/4 W, axial, THT       | 5   | Current-limiting resistor for LEDs and signal lines. 330 Ω limits current to ~10 mA at 3.3 V logic. Typically used as data line protection resistor for the NeoPixel data pin. |

---

## Accessories & Tools

| Part No.          | Name                                              | Qty | Description |
|-------------------|---------------------------------------------------|-----|-------------|
| BB-830P           | Breadboard, 830 tie points                        | 1   | Solderless prototyping board. 830 contacts, compatible with standard jumper wires and THT components. |
| DUPK-40-MM-10     | Jumper Wire Male–Male, 40-pin, 10 cm              | 1   | Short connection cables for direct wiring from the Metro board to the breadboard. |
| JUMPER-WIRE-65    | Jumper Wire Kit, 65 wires in 4 lengths            | 1   | Male jumper wire set for breadboard use. Various lengths for a tidy layout. |

---

## Power Supply

| Part No.  | Name                          | Qty | Description |
|-----------|-------------------------------|-----|-------------|
| 45040     | USB-C Power Supply 5 V / 3 A  | 1   | Primary power source for the entire system. 3 A output is sufficient for Metro M4 + NeoPixel strip (max. ~3.6 A at full brightness — limit brightness if needed). |

---

## Interface Overview (Metro M4)

| Interface | Pins                                      | Usage in Project               |
|-----------|-------------------------------------------|--------------------------------|
| I2C       | `board.SCL` / `board.SDA`                 | ToF sensor, OLED display       |
| GPIO      | `board.D5`, `board.D6`                    | Buzzer 1 (D5), Buzzer 2 (D6)  |
| NeoPixel  | `board.NEOPIXEL`                          | Onboard RGB LED                |
| LED       | `board.LED` (D13)                         | Status / heartbeat             |

---

## Notes

| Component      | Pin / Address         | Notes                              |
|----------------|-----------------------|------------------------------------|
| Buzzer 1       | `board.D5`            | KY-012, S→D5, +→5V, –→GND         |
| Buzzer 2       | `board.D6`            | KY-012, S→D6, +→5V, –→GND         |
| ToF Sensor     | I2C `0x29`            | SCL→SCL, SDA→SDA, VCC→3.3V, GND→GND |
| OLED Display   | I2C `0x3C`            | SCL→SCL, SDA→SDA, VCC→3.3V, GND→GND |
