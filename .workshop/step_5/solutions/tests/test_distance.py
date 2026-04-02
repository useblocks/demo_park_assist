"""TC_004, TC_005 – Distance reading and OLED text formatting."""
import pytest
from park_logic import mm_to_cm, format_dist_text, VL53L0X_OUT_OF_RANGE_MM


# ── mm_to_cm ─────────────────────────────────────────────────────────────────

def test_mm_to_cm_typical():
    # @ mm to cm conversion, TI_003, test_impl, [TC_004]
    """TC_004: normal reading converts correctly."""
    assert mm_to_cm(250) == pytest.approx(25.0)

def test_mm_to_cm_zero():
    assert mm_to_cm(0) == pytest.approx(0.0)

def test_mm_to_cm_max_range():
    assert mm_to_cm(2000) == pytest.approx(200.0)

def test_mm_to_cm_at_sentinel_is_none():
    # @ sentinel value returns None, TI_004, test_impl, [TC_005]
    """TC_005: sentinel value returns None."""
    assert mm_to_cm(VL53L0X_OUT_OF_RANGE_MM) is None

def test_mm_to_cm_above_sentinel_is_none():
    assert mm_to_cm(9000) is None


# ── format_dist_text ─────────────────────────────────────────────────────────

def test_format_dist_text_normal():
    # @ OLED distance text format, TI_005, test_impl, [TC_004]
    """TC_004: OLED shows distance in cm with one decimal."""
    assert format_dist_text(25.0) == "Dist: 25.0 cm"

def test_format_dist_text_decimal():
    assert format_dist_text(12.3) == "Dist: 12.3 cm"

def test_format_dist_text_out_of_range():
    # @ OLED out-of-range text, TI_006, test_impl, [TC_005]
    """TC_005: OLED shows out-of-range message."""
    assert format_dist_text(None) == "Dist: out of range"
