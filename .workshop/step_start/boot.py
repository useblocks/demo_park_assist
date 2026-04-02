"""
Metro RP2040 – CircuitPython Boot Configuration
================================================
boot.py runs once at startup, BEFORE code.py.

NOTE: Changes here require a board reset to take effect.
"""

import usb_cdc

# Enable serial console (REPL over USB)
usb_cdc.enable(console=True, data=False)
