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

**4. Finalize GitHub Copilot setup**
Click the **Copilot icon** in the bottom-right corner of VS Code and select
**"Finalize Copilot Setup"**. Follow the prompts to sign in.

**5. Explore the documentation**
Open `docs/index.rst` in the editor, then open the **ubCode** panel (sidebar)
to browse User Stories, Architecture and Test Cases interactively.

**5. Explore the source code**
Open `src/code.py` in the editor and read through it.

**6. Connect your Metro RP2040 board via USB**

**7. Verify the board appears as a USB drive**
The board should show up as a mass storage device (e.g. `CIRCUITPY`).

**8. Check that the board already has the right files**
Confirm that `code.py` on the board matches the version in `src/`.

---

## Part 2 – Hands-on

**1. Confirm the board is connected and running**
The OLED should show a distance value.

**2. Personalise the boot splash**
Open `src/code.py` in the editor and find the boot splash section.
Change `"useblocks"` to a short team name of your choice (max ~10 characters):
```python
boot_group.append(label.Label(terminalio.FONT, text="YourTeam", scale=2, color=0xFFFFFF, x=10, y=16))
```

**3. Copy `code.py` to the board**
Drag and drop (or use `cp`) the updated file onto the `CIRCUITPY` drive:
```bash
cp src/code.py /media/$USER/CIRCUITPY/
```

On some machines a plain file copy results in an empty `code.py` on the board.
If that happens, open `src/code.py` in the editor, select all, and paste the content directly into the file on `CIRCUITPY` instead.

**4. Watch the board restart automatically**
CircuitPython detects the file change and restarts.
Verify that the OLED boot splash now shows your team name.

---

> **Docs:** `make html && make serve` — builds and opens the Sphinx documentation in your browser.
> **Tests:** `make test` — runs the 35 boardless unit tests.
> **Reset state:** `make step_1` … `make step_5` — resets `src/code.py`, `docs/` and `tests/` to the reference solution of that step (`step_1` = clean start, `step_5` = fully complete). Use this to jump to any stage or recover a clean baseline.
> **Tip:** Targets can be combined — e.g. `make step_2 clean open` switches to step 2, clears the build cache and opens the docs in one go.


