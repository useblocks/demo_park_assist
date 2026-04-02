"""TC_LED_GREEN–TC_LED_BLINK – Zone classification and LED count."""
from park_logic import (
    classify_zone, calc_num_leds,
    GREEN, YELLOW, RED, OFF, DIST_MAX,
)


# ── classify_zone ─────────────────────────────────────────────────────────────

def test_green_zone_color():
    # @ green zone colour, TI_ZONE_GREEN, test_impl, [TC_LED_GREEN]
    """TC_LED_GREEN: dist > 30 cm -> green."""
    assert classify_zone(35)["color"] == GREEN

def test_green_zone_status():
    assert classify_zone(35)["status"] == "Steady"

def test_green_zone_name():
    assert classify_zone(35)["color_name"] == "Green"

def test_yellow_zone_color():
    # @ yellow zone colour, TI_ZONE_YELLOW, test_impl, [TC_LED_YELLOW]
    """TC_LED_YELLOW: 20 < dist <= 30 -> yellow."""
    assert classify_zone(25)["color"] == YELLOW

def test_yellow_zone_status():
    assert classify_zone(25)["status"] == "Steady"

def test_red_steady_zone_color():
    # @ solid red zone colour, TI_ZONE_RED, test_impl, [TC_LED_RED]
    """TC_LED_RED: 15 < dist <= 20 -> solid red."""
    assert classify_zone(17)["color"] == RED

def test_red_steady_zone_status():
    # @ solid red zone status, TI_ZONE_RED_STATUS, test_impl, [TC_LED_RED]
    """TC_LED_RED: status is Steady, not Blinking."""
    assert classify_zone(17)["status"] == "Steady"

def test_critical_zone_status():
    # @ critical zone status blinking, TI_ZONE_BLINK_STATUS, test_impl, [TC_LED_BLINK]
    """TC_LED_BLINK: dist <= 15 -> Blinking."""
    assert classify_zone(10)["status"] == "Blinking"

def test_critical_zone_color_when_blink_on():
    # @ critical zone red when blink on, TI_ZONE_BLINK_RED, test_impl, [TC_LED_BLINK]
    """TC_LED_BLINK: blink_state=True -> RED."""
    assert classify_zone(10, blink_state=True)["color"] == RED

def test_critical_zone_color_when_blink_off():
    # @ critical zone off when blink off, TI_ZONE_BLINK_OFF, test_impl, [TC_LED_BLINK]
    """TC_LED_BLINK: blink_state=False -> OFF."""
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
