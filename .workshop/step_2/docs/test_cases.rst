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

   - Serial shows ``Park Assist started``.
   - No ``Traceback`` or ``Exception`` output.


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


Distance Display
----------------

.. test:: OLED updates distance value each cycle
   :id: TC_DIST_UPDATE
   :status: open
   :verifies: US_DISTANCE

   **Precondition:** VL53L1X sensor wired to I2C (0x29), board running.

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


