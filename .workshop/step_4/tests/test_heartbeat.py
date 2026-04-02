"""TC_HEARTBEAT – Heartbeat LED timing."""
from park_logic import is_heartbeat_on


def test_heartbeat_on_at_zero():
    """LED is ON at the very start of the cycle."""
    assert is_heartbeat_on(0.0) is True

def test_heartbeat_on_within_100ms():
    # @ LED on within 100 ms, TI_HB_ON, test_impl, [TC_HEARTBEAT]
    """TC_HEARTBEAT: LED is ON within the first 100 ms."""
    assert is_heartbeat_on(0.05) is True

def test_heartbeat_off_at_100ms():
    # @ LED off at 100 ms, TI_HB_OFF, test_impl, [TC_HEARTBEAT]
    """TC_HEARTBEAT: LED turns OFF at exactly 100 ms."""
    assert is_heartbeat_on(0.1) is False

def test_heartbeat_off_mid_cycle():
    assert is_heartbeat_on(0.5) is False

def test_heartbeat_off_end_of_cycle():
    assert is_heartbeat_on(0.999) is False
