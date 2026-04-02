SW Architecture
===============

The Park Assist Demo is a single-file CircuitPython application (``code.py``)
running on the Adafruit Metro RP2040.  The architecture is intentionally flat
to match the constraints of a microcontroller environment without an OS.

System Overview
---------------

.. mermaid::

   graph TD
       subgraph Hardware
           VL53L0X["VL53L0X\nToF Sensor\n(I2C 0x29)"]
           OLED["OLED SH1106\n128×64\n(I2C 0x3C)"]
           STRIP["NeoPixel Strip\n60 LEDs ADA3636\n(D2)"]
           BUZZER["Buzzer KY-012\n(D5)"]
       end

       subgraph code.py
           INIT["Initialization\nAR_001"]
           BOOT["Boot Splash\nAR_002"]
           SENSOR["Sensor Module\nAR_003"]
           DISPLAY["OLED Display\nModule\nAR_005"]
           LEDS["LED Strip\nModule\nAR_006"]
           BUZ["Buzzer Module\nAR_007"]
       end

       INIT --> SENSOR
       INIT --> DISPLAY
       INIT --> LEDS
       INIT --> BUZ
       BOOT --> DISPLAY

       SENSOR --- VL53L0X
       DISPLAY --- OLED
       LEDS --- STRIP
       BUZ --- BUZZER


Architecture Components
-----------------------

.. arch:: System Initialization
   :id: AR_001
   :status: done
   :realizes: US_001

   Sets up all hardware peripherals in sequence: NeoPixel strip, buzzer,
   OLED display bus, I2C bus, and the ToF sensor.  Ends with the strip
   cleared and the system ready to enter the main loop.

   **Sequence**

   .. mermaid::

      sequenceDiagram
          participant CP as CircuitPython
          participant GPIO as GPIO / I2C
          participant OLED as SH1106 OLED
          participant TOF as VL53L0X

          CP->>GPIO: configure strip (D2), buzzer (D5)
          CP->>GPIO: I2C bus init (SCL/SDA)
          CP->>OLED: I2CDisplayBus + SH1106 init
          CP->>OLED: show boot splash (3 s)
          CP->>GPIO: I2C scan → detect 0x29
          CP->>TOF: VL53L0X() init
          CP-->>CP: strip.fill(OFF) → main loop


.. arch:: Boot Splash Display
   :id: AR_002
   :status: done
   :realizes: US_003

   Renders a static splash screen on the OLED for 3 seconds directly after
   display initialisation.  The splash is replaced by the live UI group before
   the main loop begins.


.. arch:: Sensor Module
   :id: AR_003
   :status: done
   :realizes: US_004

   Reads the raw distance value from the VL53L0X via I2C in every main loop
   iteration.  Converts the mm value returned by the library to centimetres.
   Filters the out-of-range sentinel value ``8190 mm``.

   .. mermaid::

      flowchart LR
          A[vl53.range\nreturns mm] --> B{raw_mm < 8190?}
          B -- yes --> C[dist = raw_mm / 10\ncm]
          B -- no  --> D[out-of-range\nhandling]


.. arch:: OLED Display Module
   :id: AR_005
   :status: done
   :realizes: US_003, US_004

   Maintains a ``label.Label`` object on the display:

   - **Dist** – current distance in cm or "out of range".


.. arch:: LED Strip Module
   :id: AR_006
   :status: done
   :realizes: US_005

   Controls the 60-LED NeoPixel strip (ADA3636) on ``board.D2``.
   Sets all LEDs to red when dist ≤ 20 cm, green when dist > 20 cm,
   and off when out of range.


.. arch:: Buzzer Module
   :id: AR_007
   :status: done
   :realizes: US_006

   Drives the KY-012 active buzzer on ``board.D5``:

   - **Silent** – GPIO stays LOW when out of range or dist > 20 cm.
   - **Continuous** – GPIO stays HIGH when dist ≤ 20 cm.
