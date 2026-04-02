"""TC_010–TC_013 – Buzzer interval per zone."""
from park_logic import classify_zone


def test_silent_in_green_zone():
    # @ buzzer silent in green zone, TI_014, test_impl, [TC_010]
    """TC_010: no buzzer above 30 cm."""
    assert classify_zone(35)["beep_interval"] is None

def test_slow_beep_in_yellow_zone():
    # @ buzzer slow beep in yellow zone, TI_015, test_impl, [TC_011]
    """TC_011: 1 s beep interval in yellow zone."""
    assert classify_zone(25)["beep_interval"] == 1.0

def test_fast_beep_in_red_zone():
    # @ buzzer fast beep in red zone, TI_016, test_impl, [TC_012]
    """TC_012: 0.4 s beep interval in solid-red zone."""
    assert classify_zone(17)["beep_interval"] == 0.4

def test_continuous_in_critical_zone():
    # @ buzzer continuous in critical zone, TI_017, test_impl, [TC_013]
    """TC_013: continuous tone (interval == 0) in critical zone."""
    assert classify_zone(10)["beep_interval"] == 0

def test_out_of_range_is_silent():
    """Out-of-range distance maps to green zone -> silent."""
    # dist=50 > DIST_MAX -> green zone -> None
    assert classify_zone(50)["beep_interval"] is None
