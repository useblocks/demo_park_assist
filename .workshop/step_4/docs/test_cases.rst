Test Cases
==========

Test Cases verify User Stories on the physical Metro RP2040 board.  Each test
is executed manually; automated CI is not available for CircuitPython targets.

.. note::

   All tests assume the board is fully assembled according to **hw.md Setup 2**
   and connected via USB-C.

----

Boot & Startup
--------------

.. test:: System boots without exception
   :id: TC_BOOT
   :status: open
   :verifies: US_BOOT

   **Precondition:** Board is connected; CircuitPython ``code.py`` is present.

   **Steps:**

   1. Power-cycle the board (unplug / replug USB-C).
   2. Open the serial console (115200 baud).

   **Expected result:**

   - Serial shows ``Metro RP2040 CircuitPython started``.
   - No ``Traceback`` or ``Exception`` output.
   - RUN_LED (D13) begins blinking within 5 seconds.


.. test:: OLED boot splash displayed for 3 seconds
   :id: TC_SPLASH
   :status: open
   :verifies: US_SPLASH

   **Precondition:** TC_BOOT passed.

   **Steps:**

   1. Power-cycle the board.
   2. Observe the OLED immediately after power-on.

   **Expected result:**

   - OLED shows "Park Assist v. 1.0" text for approximately 3 seconds.
   - Display then switches to the live UI showing "Dist: ---".


Heartbeat
---------

.. test:: Heartbeat LED blinks at 1 Hz
   :id: TC_HEARTBEAT
   :status: open
   :verifies: US_HEARTBEAT

   **Precondition:** TC_BOOT passed, board running normally.

   **Steps:**

   1. Observe the onboard LED (D13) and onboard NeoPixel.
   2. Count blink cycles for 10 seconds.

   **Expected result:**

   - Approximately 10 blink cycles in 10 seconds (1 Hz).
   - LED is ON for ≈ 100 ms and OFF for ≈ 900 ms per cycle.
   - Onboard NeoPixel pulses in sync with D13.


Distance Display
----------------

.. test:: OLED updates distance value each cycle
   :id: TC_DIST_UPDATE
   :status: open
   :verifies: US_DISTANCE

   **Precondition:** VL53L0X sensor wired to I2C (0x29), board running.

   **Steps:**

   1. Hold a flat object at 25 cm in front of the sensor.
   2. Observe the OLED ``Dist:`` line.
   3. Move the object closer and farther slowly.

   **Expected result:**

   - OLED shows ``Dist: 25.x cm`` (within ± 2 cm).
   - Value updates continuously without freezing.
   - Moving the object causes the reading to change accordingly.


.. test:: OLED shows out-of-range message
   :id: TC_OUT_OF_RANGE
   :status: open
   :verifies: US_DISTANCE

   **Precondition:** Sensor wired and initialised.

   **Steps:**

   1. Remove any object in front of the sensor (clear path > 2 m).

   **Expected result:**

   - OLED shows ``Dist: out of range``.
   - ``Color:`` and ``Status:`` lines show ``---``.
   - LED strip is completely off.


LED Strip Zones
---------------

.. test:: Strip shows green for dist > 30 cm
   :id: TC_LED_GREEN
   :status: open
   :verifies: US_LED

   **Steps:**

   1. Hold object at 35 cm in front of sensor.

   **Expected result:**

   - Strip LEDs are green.
   - Number of lit LEDs is proportional to distance (fewer LEDs than at 20 cm).
   - Buzzer is silent.


.. test:: Strip shows yellow for 20–30 cm
   :id: TC_LED_YELLOW
   :status: open
   :verifies: US_LED

   **Steps:**

   1. Hold object at 25 cm.

   **Expected result:**

   - Strip LEDs are yellow.
   - OLED ``Color:`` shows ``Yellow``.


.. test:: Strip shows solid red for 15–20 cm
   :id: TC_LED_RED
   :status: open
   :verifies: US_LED

   **Steps:**

   1. Hold object at 17 cm.

   **Expected result:**

   - Strip LEDs are solid red (not blinking).
   - OLED ``Status:`` shows ``Steady``.


.. test:: Strip blinks red for dist ≤ 15 cm
   :id: TC_LED_BLINK
   :status: open
   :verifies: US_LED

   **Steps:**

   1. Hold object at 10 cm.

   **Expected result:**

   - Strip alternates between red and off at ≈ 5 Hz (200 ms period).
   - OLED ``Status:`` shows ``Blinking``.


Buzzer Zones
------------

.. test:: Buzzer is silent in green zone
   :id: TC_BUZ_SILENT
   :status: open
   :verifies: US_BUZZER

   **Steps:**

   1. Hold object at 35 cm.

   **Expected result:**

   - No audible tone from buzzer.


.. test:: Buzzer slow-beeps in yellow zone
   :id: TC_BUZ_SLOW
   :status: open
   :verifies: US_BUZZER

   **Steps:**

   1. Hold object at 25 cm.

   **Expected result:**

   - Buzzer emits short beeps approximately once per second (1 Hz).


.. test:: Buzzer fast-beeps in red zone
   :id: TC_BUZ_FAST
   :status: open
   :verifies: US_BUZZER

   **Steps:**

   1. Hold object at 17 cm.

   **Expected result:**

   - Buzzer emits short beeps at approximately 2.5 Hz (every 0.4 s).


.. test:: Buzzer sounds continuously in critical zone
   :id: TC_BUZ_CONTINUOUS
   :status: open
   :verifies: US_BUZZER

   **Steps:**

   1. Hold object at 10 cm.

   **Expected result:**

   - Buzzer produces a continuous tone without interruption.
