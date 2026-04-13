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
           VL53L1X["VL53L1X\nToF Sensor\n(I2C 0x29)"]
           OLED["OLED SH1106\n128×64\n(I2C 0x3C)"]
       end

       subgraph code.py
           INIT["Initialization\nAR_001"]
           BOOT["Boot Splash\nAR_002"]
           SENSOR["Sensor Module\nAR_003"]
           DISPLAY["OLED Display\nModule\nAR_005"]
       end

       INIT --> SENSOR
       INIT --> DISPLAY
       BOOT --> DISPLAY

       SENSOR --- VL53L1X
       DISPLAY --- OLED


Architecture Components
-----------------------

.. arch:: System Initialization
   :id: AR_INIT
   :status: done
   :realizes: US_BOOT

   Sets up all hardware peripherals in sequence: OLED display bus, I2C bus,
   and the ToF sensor.  Ends with the system ready to enter the main loop.

   **Sequence**

   .. mermaid::

      sequenceDiagram
          participant CP as CircuitPython
          participant GPIO as GPIO / I2C
          participant OLED as SH1106 OLED
          participant TOF as VL53L1X

          CP->>GPIO: I2C bus init (SCL/SDA)
          CP->>OLED: I2CDisplayBus + SH1106 init
          CP->>OLED: show boot splash (3 s)
          CP->>GPIO: I2C scan → detect 0x29
          CP->>TOF: VL53L1X() init
          CP-->>CP: main loop


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

   Reads the distance from the VL53L1X via I2C in every main loop iteration.
   The library returns the value directly in centimetres, or ``None`` when the
   target is out of range.

   .. mermaid::

      flowchart LR
          A[vl53.distance\nreturns cm] --> B{dist is None?}
          B -- no  --> C[use dist cm]
          B -- yes --> D[out-of-range\nhandling]


.. arch:: OLED Display Module
   :id: AR_DISPLAY
   :status: done
   :realizes: US_SPLASH, US_DISTANCE

   Maintains a ``label.Label`` object on the display:

   - **Dist** – current distance in cm or "out of range".
