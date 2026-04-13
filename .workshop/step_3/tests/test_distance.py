"""TC_DIST_UPDATE, TC_OUT_OF_RANGE – Distance reading and OLED text formatting."""
import pytest
from park_logic import format_dist_text




# ── format_dist_text ─────────────────────────────────────────────────────────

def test_format_dist_text_normal():
    # @ OLED distance text format, TI_DIST_TEXT, test_impl, [TC_DIST_UPDATE]
    """TC_DIST_UPDATE: OLED shows distance in cm with one decimal."""
    assert format_dist_text(25.0) == "Dist: 25.0 cm"

def test_format_dist_text_decimal():
    assert format_dist_text(12.3) == "Dist: 12.3 cm"

def test_format_dist_text_out_of_range():
    # @ OLED out-of-range text, TI_OOR_TEXT, test_impl, [TC_OUT_OF_RANGE]
    """TC_OUT_OF_RANGE: OLED shows out-of-range message."""
    assert format_dist_text(None) == "Dist: out of range"
