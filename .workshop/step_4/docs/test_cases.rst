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
   :id: TC_001
   :status: open
   :verifies: US_001

   **Precondition:** Board is connected; CircuitPython ``code.py`` is present.

   **Steps:**

   1. Power-cycle the board (unplug / replug USB-C).
   2. Open the serial console (115200 baud).

   **Expected result:**

   - Serial shows ``Park Assist started``.
   - No ``Traceback`` or ``Exception`` output.


.. test:: OLED boot splash displayed for 3 seconds
   :id: TC_002
   :status: open
   :verifies: US_003

   **Precondition:** TC_001 passed.

   **Steps:**

   1. Power-cycle the board.
   2. Observe the OLED immediately after power-on.

   **Expected result:**

   - OLED shows "Park Assist v. 1.0" text for approximately 3 seconds.
   - Display then switches to the live UI showing "Dist: ---".


Distance Display
----------------

.. test:: OLED updates distance value each cycle
   :id: TC_004
   :status: open
   :verifies: AR_003

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
   :id: TC_005
   :status: open
   :verifies: US_004

   **Precondition:** Sensor wired and initialised.

   **Steps:**

   1. Remove any object in front of the sensor (clear path > 2 m).

   **Expected result:**

   - OLED shows ``Dist: out of range``.
   - LED strip is completely off.


LED Strip Zones
---------------

.. test:: Strip shows green for dist > 20 cm
   :id: TC_006
   :status: open
   :verifies: US_005

   **Steps:**

   1. Hold object at 25 cm in front of sensor.

   **Expected result:**

   - Strip LEDs are green.
   - Buzzer is silent.


.. test:: Strip shows yellow for 20–30 cm
   :id: TC_007
   :status: open
   :verifies: US_005

   **Steps:**

   1. Hold object at 25 cm.

   **Expected result:**

   - Strip LEDs are yellow.


.. test:: Strip shows red for dist ≤ 20 cm
   :id: TC_008
   :status: open
   :verifies: US_005

   **Steps:**

   1. Hold object at 15 cm.

   **Expected result:**

   - Strip LEDs are solid red.


.. test:: Strip blinks red for dist ≤ 15 cm
   :id: TC_009
   :status: open
   :verifies: US_005

   **Steps:**

   1. Hold object at 10 cm.

   **Expected result:**

   - Strip alternates between red and off at ≈ 5 Hz (200 ms period).


Buzzer Zones
------------

.. test:: Buzzer is silent when dist > 20 cm
   :id: TC_010
   :status: open
   :verifies: AR_007

   **Steps:**

   1. Hold object at 25 cm.

   **Expected result:**

   - No audible tone from buzzer.


.. test:: Buzzer sounds continuously when dist ≤ 20 cm
   :id: TC_011
   :status: open
   :verifies: US_006

   **Steps:**

   1. Hold object at 15 cm.

   **Expected result:**

   - Buzzer produces a continuous tone.


.. test:: Buzzer beeps in yellow zone (20–30 cm)
   :id: TC_012
   :status: open
   :verifies: US_006

   **Steps:**

   1. Hold object at 25 cm.

   **Expected result:**

   - Buzzer emits short beeps approximately once per second (1 Hz).


.. test:: Buzzer sounds continuously in critical zone (≤ 15 cm)
   :id: TC_013
   :status: open
   :verifies: US_006

   **Steps:**

   1. Hold object at 10 cm.

   **Expected result:**

   - Buzzer produces a continuous tone without interruption.
