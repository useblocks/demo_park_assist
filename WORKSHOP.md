# Park Assist Demo – Workshop

Welcome! This workshop walks you through a live project that combines
**CircuitPython firmware** with **sphinx-needs documentation** and **CodeLinks traceability**.

---

## Part 1 – Setup

**1. Open the repository on GitHub**
Navigate to the repository page.

**2. Start a Codespace**
Click **Code → Codespaces → Create codespace on main**.

**3. Wait for the initial setup to finish**
The post-create script runs automatically and installs all dependencies.
Watch the terminal until you see:
```
==> Setup complete.
```

**4. Explore the documentation**
Open `docs/index.rst` in the editor, then open the **ubCode** panel (sidebar)
to browse User Stories, Architecture and Test Cases interactively.

**5. Explore the source code**
Open `src/metro_rp2040/code.py` and `src/metro_rp2040/park_logic.py`.
Notice how the zone logic is separated from the hardware code.

**6. Connect your Metro RP2040 board via USB**

**7. Verify the board appears as a USB drive**
The board should show up as a mass storage device (e.g. `CIRCUITPY`).

**8. Check that the board already has the right files**
Confirm that `code.py` and `park_logic.py` on the board match the versions
in `src/metro_rp2040/`.

---

## Part 2 – Hands-on

**1. Confirm the board is connected and running**
The LED strip should be active and the OLED should show a distance value.

**2. Change a color in `park_logic.py`**
Open `src/metro_rp2040/park_logic.py` and modify a color constant, e.g.:
```python
GREEN = (100, 255, 100)
```

**3. Copy `park_logic.py` to the board**
Drag and drop (or use `cp`) the updated file onto the `CIRCUITPY` drive:
```bash
cp src/metro_rp2040/park_logic.py /media/$USER/CIRCUITPY/
```

**4. Watch the board restart automatically**
CircuitPython detects the file change and restarts.
Verify that the LED strip now shows the new color in the green zone.

---

> **Docs:** `make html && make serve` — builds and opens the Sphinx documentation in your browser.
> **Tests:** `make test` — runs the 35 boardless unit tests.
