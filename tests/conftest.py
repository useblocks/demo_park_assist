"""
conftest.py – make park_logic importable without adding src/metro_rp2040 to
sys.path. Adding that directory would shadow Python's stdlib 'code' module
with the CircuitPython code.py entry point, breaking pytest internals.
"""
import importlib.util
import pathlib
import sys

_LOGIC_FILE = (
    pathlib.Path(__file__).parent.parent
    / "src" / "park_logic.py"
)

spec = importlib.util.spec_from_file_location("park_logic", _LOGIC_FILE)
module = importlib.util.module_from_spec(spec)
sys.modules["park_logic"] = module
spec.loader.exec_module(module)
