.. ──────────────────────────────────────────────────────────────────────────────
.. Workshop Step 2 – Solution A: fix wrongly linked test cases (step 7)
.. ──────────────────────────────────────────────────────────────────────────────
..
.. In docs/test_cases.rst, change the two violations found by the schema:
..
..   TC_DIST_UPDATE  :verifies: AR_SENSOR  →  :verifies: US_DISTANCE
..   TC_010  :verifies: AR_007  →  :verifies: US_006
..
.. After saving, the Problems panel violations for TC_DIST_UPDATE and TC_010 disappear.
.. ──────────────────────────────────────────────────────────────────────────────

.. ──────────────────────────────────────────────────────────────────────────────
.. Workshop Step 2 – Solution B: new test case for US_CIRCUITPYTHON (step 8)
.. ──────────────────────────────────────────────────────────────────────────────
..
.. Add the test case below to docs/test_cases.rst (e.g. a new section at the
.. end: "Non-Functional").  US_CIRCUITPYTHON ("Code runs exclusively on CircuitPython")
.. currently has no test case — Copilot generates this in the last step.
.. ──────────────────────────────────────────────────────────────────────────────

.. test:: All imports use CircuitPython-compatible libraries
   :id: TC_014
   :status: open
   :verifies: US_CIRCUITPYTHON

   **Precondition:** Board is connected and running ``code.py``.

   **Steps:**

   1. Open the serial console (115200 baud).
   2. Trigger a REPL prompt (Ctrl+C).
   3. Run the following in the REPL:

      .. code-block:: python

         import sys
         print(sys.modules.keys())

   **Expected result:**

   - No CPython-only module names (e.g. ``subprocess``, ``threading``,
     ``socket``) appear in the module list.
   - All listed modules are available in the CircuitPython standard library
     or the Adafruit CircuitPython Bundle (``adafruit_*``).
