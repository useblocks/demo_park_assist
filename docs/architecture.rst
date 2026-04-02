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
           LED13["Onboard LED\nD13"]
           NEOPX["Onboard NeoPixel\nboard.NEOPIXEL"]
       end

       subgraph code.py
           INIT["Initialization\nAR_001"]
           BOOT["Boot Splash\nAR_002"]
           SENSOR["Sensor Module\nAR_003"]
           ZONE["Distance Zone\nClassifier\nAR_004"]
           DISPLAY["OLED Display\nModule\nAR_005"]
           LEDS["LED Strip\nModule\nAR_006"]
           BUZ["Buzzer Module\nAR_007"]
           HB["Heartbeat\nModule\nAR_008"]
       end

       INIT --> SENSOR
       INIT --> DISPLAY
       INIT --> LEDS
       INIT --> BUZ
       INIT --> HB
       BOOT --> DISPLAY

       SENSOR -->|dist cm| ZONE
       ZONE --> DISPLAY
       ZONE --> LEDS
       ZONE --> BUZ

       HB --> LED13
       HB --> NEOPX
       SENSOR --- VL53L0X
       DISPLAY --- OLED
       LEDS --- STRIP
       BUZ --- BUZZER


Architecture Components
-----------------------

.. arch:: System Initialization
   :id: AR_INIT
   :status: done
   :realizes: US_BOOT

   Sets up all hardware peripherals in sequence: onboard LED, onboard NeoPixel,
   NeoPixel strip, buzzer, OLED display bus, I2C bus, and the ToF sensor.
   Ends with the strip cleared and the system ready to enter the main loop.

   **Sequence**

   .. mermaid::

      sequenceDiagram
          participant CP as CircuitPython
          participant GPIO as GPIO / I2C
          participant OLED as SH1106 OLED
          participant TOF as VL53L0X

          CP->>GPIO: configure LED, NeoPixel, strip, buzzer
          CP->>GPIO: I2C bus init (SCL/SDA)
          CP->>OLED: I2CDisplayBus + SH1106 init
          CP->>OLED: show boot splash (3 s)
          CP->>GPIO: I2C scan → detect 0x29
          CP->>TOF: VL53L0X() init
          CP-->>CP: strip.fill(OFF) → main loop


.. arch:: Boot Splash Display
   :id: AR_SPLASH
   :status: done
   :realizes: US_SPLASH

   Renders a static splash screen on the OLED for 3 seconds directly after
   display initialisation.  The splash is replaced by the live UI group before
   the main loop begins.


.. arch:: Sensor Module
   :id: AR_SENSOR
   :status: done
   :realizes: US_DISTANCE

   Reads the raw distance value from the VL53L0X via I2C in every main loop
   iteration.  Converts the mm value returned by the library to centimetres.
   Filters the out-of-range sentinel value ``8190 mm``.

   .. mermaid::

      flowchart LR
          A[vl53.range\nreturns mm] --> B{raw_mm < 8190?}
          B -- yes --> C[dist = raw_mm / 10\ncm]
          B -- no  --> D[out-of-range\nhandling]


.. arch:: Distance Zone Classifier
   :id: AR_ZONES
   :status: done
   :realizes: US_DISTANCE, US_LED, US_BUZZER

   Classifies the measured distance into one of four zones and derives output
   parameters (LED colour, LED count, buzzer interval) for downstream modules.

   .. list-table::
      :header-rows: 1
      :widths: 30 20 20 30

      * - Condition
        - LED colour
        - Buzzer
        - Strip LEDs
      * - dist > 30 cm
        - green
        - silent
        - linear (0–60)
      * - 20 cm < dist ≤ 30 cm
        - yellow
        - 1.0 s beep
        - linear (0–60)
      * - 15 cm < dist ≤ 20 cm
        - red (solid)
        - 0.4 s beep
        - linear (0–60)
      * - dist ≤ 15 cm
        - red (blink 5 Hz)
        - continuous
        - linear (0–60)
      * - out of range
        - — (off)
        - silent
        - all off


.. arch:: OLED Display Module
   :id: AR_DISPLAY
   :status: done
   :realizes: US_SPLASH, US_DISTANCE

   Maintains three ``label.Label`` objects on the display:

   - **Dist** – current distance in cm or "out of range".
   - **Color** – active zone colour name ("Green", "Yellow", "Red", "---").
   - **Status** – current state ("Steady", "Blinking", "---").


.. arch:: LED Strip Module
   :id: AR_LED
   :status: done
   :realizes: US_LED

   Controls the 60-LED NeoPixel strip (ADA3636) on ``board.D2``.
   Calculates how many LEDs to light based on a linear mapping from the
   distance range [0, DIST_MAX] to [60, 0] LEDs, and fills each LED with the
   zone colour or ``OFF``.


.. arch:: Buzzer Module
   :id: AR_BUZZER
   :status: done
   :realizes: US_BUZZER

   Drives the KY-012 active buzzer on ``board.D5`` with three modes:

   - **Silent** – GPIO stays LOW.
   - **Pulsed** – toggled at the interval defined by the zone classifier.
     Pulse width is fixed at 80 ms ON; remainder is the pause.
   - **Continuous** – GPIO stays HIGH.


.. arch:: Heartbeat Module
   :id: AR_HEARTBEAT
   :status: done
   :realizes: US_HEARTBEAT

   Drives the onboard LED (D13) and onboard NeoPixel to blink at 1 Hz
   (100 ms ON / 900 ms OFF) independently of the sensor loop, using
   ``time.monotonic()`` for non-blocking timing.
