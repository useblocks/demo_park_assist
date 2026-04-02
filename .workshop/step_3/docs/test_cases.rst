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


Buzzer
------

.. test:: Buzzer beeps continuously when obstacle is within 20 cm
   :id: TC_BUZZER_ON
   :status: open
   :verifies: US_BUZZER

   **Precondition:** Sensor wired, board running, buzzer wired to PWM pin.

   **Steps:**

   1. Hold a flat object at 15 cm in front of the sensor.
   2. Observe/listen to the buzzer.

   **Expected result:**

   - Buzzer emits a continuous tone.
   - No gaps or intermittent silence.


.. test:: Buzzer is silent when distance is 20 cm or more
   :id: TC_BUZZER_OFF
   :status: open
   :verifies: US_BUZZER

   **Precondition:** TC_BUZZER_ON passed.

   **Steps:**

   1. Move the object to 25 cm or further from the sensor.
   2. Observe/listen to the buzzer.

   **Expected result:**

   - Buzzer stops immediately.
   - No residual tone.
