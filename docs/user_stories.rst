User Stories
============

User Stories describe the expected behaviour of the Park Assist Demo system
from the perspective of the operator and the workshop participant.

Functional Stories
------------------

.. story:: System boots without errors
   :id: US_001
   :status: open

   As a user, I want the board to start up cleanly so that I can rely on the
   system being ready without manual intervention.

   **Acceptance criteria**

   - CircuitPython starts ``code.py`` automatically.
   - No exception is raised during boot.
   - Serial console shows the startup message.


.. story:: Status LED blinks at heartbeat rate
   :id: US_002
   :status: open

   As a user, I want the onboard LED (D13) to blink at a regular interval so
   that I can confirm the board is alive and running.

   **Acceptance criteria**

   - LED blinks with 100 ms on / 900 ms off pattern (≈ 1 Hz).
   - Onboard NeoPixel pulses in sync with the LED.


.. story:: OLED shows status text on startup
   :id: US_003
   :status: open

   As a user, I want a boot splash screen on the OLED display so that I can
   identify the demo and confirm the display is working.

   **Acceptance criteria**

   - Display shows "Park Assist v. 1.0" text for at least 3 seconds.
   - Splash is replaced by the live UI after the delay.


.. story:: Live ToF distance shown on OLED
   :id: US_004
   :status: open

   As a user, I want the measured distance to be displayed in real time on the
   OLED so that I can read the current sensor value.

   **Acceptance criteria**

   - Distance is displayed in centimetres (one decimal place).
   - Display updates every main loop cycle.
   - Out-of-range condition shows "Dist: out of range".


.. story:: NeoPixel strip reflects distance zone
   :id: US_005
   :status: open

   As a user, I want the NeoPixel strip colour and fill level to change
   depending on how close an obstacle is, so that the distance is visible
   from across the room.

   **Acceptance criteria**

   - ``dist > 30 cm`` → strip is green.
   - ``20 cm < dist ≤ 30 cm`` → strip is yellow.
   - ``15 cm < dist ≤ 20 cm`` → strip is solid red.
   - ``dist ≤ 15 cm`` → strip blinks red at 5 Hz.
   - Number of lit LEDs scales linearly from 0 (≥ 40 cm) to 60 (≤ 0 cm).
   - Out-of-range → all LEDs off.


.. story:: Buzzer alerts according to distance zone
   :id: US_006
   :status: open

   As a user, I want the buzzer to produce an audible alert that becomes more
   urgent as the obstacle gets closer.

   **Acceptance criteria**

   - ``dist > 30 cm`` → buzzer silent.
   - ``20 cm < dist ≤ 30 cm`` → buzzer beeps slowly (1 s interval).
   - ``15 cm < dist ≤ 20 cm`` → buzzer beeps fast (0.4 s interval).
   - ``dist ≤ 15 cm`` → buzzer sounds continuously.
   - Out-of-range → buzzer silent.


Non-Functional Stories
----------------------

.. story:: Code runs exclusively on CircuitPython
   :id: US_007
   :status: open

   As a developer, I want the code to use only CircuitPython-compatible
   libraries so that it runs without modification on the target board.

   **Acceptance criteria**

   - No CPython-only imports or constructs.
   - All libraries are sourced from the Adafruit CircuitPython Bundle.


.. story:: RAM usage stays below 80 %
   :id: US_008
   :status: open

   As a developer, I want RAM consumption to stay below 80 % of available
   memory so that the system remains stable during long-running sessions.

   **Acceptance criteria**

   - ``gc.mem_free()`` shows at least 20 % free after full initialisation.
