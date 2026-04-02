"""TC_006–TC_009 – Zone classification and LED count."""
from park_logic import (
    classify_zone, calc_num_leds,
    GREEN, YELLOW, RED, OFF, DIST_MAX,
)


# ── classify_zone ─────────────────────────────────────────────────────────────

def test_green_zone_color():
    """TC_006: dist > 30 cm -> green."""
    assert classify_zone(35)["color"] == GREEN

def test_green_zone_status():
    assert classify_zone(35)["status"] == "Steady"

def test_green_zone_name():
    assert classify_zone(35)["color_name"] == "Green"

def test_yellow_zone_color():
    """TC_007: 20 < dist <= 30 -> yellow."""
    assert classify_zone(25)["color"] == YELLOW

def test_yellow_zone_status():
    assert classify_zone(25)["status"] == "Steady"

def test_red_steady_zone_color():
    """TC_008: 15 < dist <= 20 -> solid red."""
    assert classify_zone(17)["color"] == RED

def test_red_steady_zone_status():
    """TC_008: status is Steady, not Blinking."""
    assert classify_zone(17)["status"] == "Steady"

def test_critical_zone_status():
    """TC_009: dist <= 15 -> Blinking."""
    assert classify_zone(10)["status"] == "Blinking"

def test_critical_zone_color_when_blink_on():
    """TC_009: blink_state=True -> RED."""
    assert classify_zone(10, blink_state=True)["color"] == RED

def test_critical_zone_color_when_blink_off():
    """TC_009: blink_state=False -> OFF."""
    assert classify_zone(10, blink_state=False)["color"] == OFF

def test_boundary_exactly_at_dist_green():
    """Exactly 30 cm falls into yellow zone (not green)."""
    assert classify_zone(30)["color"] == YELLOW

def test_boundary_exactly_at_dist_red():
    """Exactly 15 cm falls into critical zone."""
    assert classify_zone(15)["status"] == "Blinking"


# ── calc_num_leds ─────────────────────────────────────────────────────────────

def test_leds_zero_at_max_dist():
    assert calc_num_leds(DIST_MAX) == 0

def test_leds_sixty_at_zero():
    assert calc_num_leds(0) == 60

def test_leds_above_max_clamped():
    assert calc_num_leds(100) == 0

def test_leds_negative_clamped():
    assert calc_num_leds(-10) == 60

def test_leds_scale_closer_means_more():
    assert calc_num_leds(35) < calc_num_leds(25)
