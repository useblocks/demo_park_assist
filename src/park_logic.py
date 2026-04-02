"""
Park Assist Demo - Pure Logic Module
=====================================
All distance calculation, zone classification and formatting logic.
No board or hardware imports - fully testable on standard Python.
"""

# Distance thresholds (cm)
DIST_MAX    = 40   # above this: 0 LEDs lit
DIST_GREEN  = 30   # > 30 cm -> green, no beep
DIST_YELLOW = 20   # > 20 cm -> yellow, slow beep
DIST_RED    = 15   # > 15 cm -> solid red / <= 15 cm -> blinking

# VL53L0X returns 8190 mm when target is out of range
VL53L0X_OUT_OF_RANGE_MM = 8190

# Color constants (RGB tuples)
OFF     = (0,   0,   0)
RED     = (255, 0,   0)
GREEN   = (0,   255, 0)
BLUE    = (0,   0,   255)
YELLOW  = (255, 200, 0)
WHITE   = (255, 255, 255)
SPECIAL = (50,  200, 50)   # heartbeat color for onboard NeoPixel


def mm_to_cm(raw_mm):
    """Convert VL53L0X raw mm reading to cm.

    Returns float cm, or None when out-of-range (raw_mm >= VL53L0X_OUT_OF_RANGE_MM).
    """
    if raw_mm >= VL53L0X_OUT_OF_RANGE_MM:
        return None
    return raw_mm / 10.0


def format_dist_text(dist_cm):
    """Format distance value for the OLED dist_label.

    Args:
        dist_cm: float or None (out-of-range).

    Returns:
        str, e.g. "Dist: 25.0 cm" or "Dist: out of range"
    """
    if dist_cm is None:
        return "Dist: out of range"
    return "Dist: {:.1f} cm".format(dist_cm)


def calc_num_leds(dist_cm):
    """Calculate how many of the 60 strip LEDs should light up.

    Linear mapping: 0 LEDs at dist_cm >= DIST_MAX, 60 LEDs at dist_cm <= 0.

    Args:
        dist_cm: float, measured distance in cm.

    Returns:
        int 0-60
    """
    return max(0, min(60, int((DIST_MAX - dist_cm) * 60 / DIST_MAX)))


def classify_zone(dist_cm, blink_state=True):
    """Classify a distance value into one of four zones.

    Args:
        dist_cm:     float, measured distance in cm.
        blink_state: bool, current blink toggle (relevant only in critical zone).

    Returns:
        dict with keys:
            color         - RGB tuple for the LED strip
            color_name    - human-readable color name for OLED
            status        - "Steady" or "Blinking"
            beep_interval - None (silent), 0 (continuous), or float seconds
    """
    if dist_cm > DIST_GREEN:
        return {
            "color":         GREEN,
            "color_name":    "Green",
            "status":        "Steady",
            "beep_interval": None,
        }
    elif dist_cm > DIST_YELLOW:
        return {
            "color":         YELLOW,
            "color_name":    "Yellow",
            "status":        "Steady",
            "beep_interval": 1.0,
        }
    elif dist_cm > DIST_RED:
        return {
            "color":         RED,
            "color_name":    "Red",
            "status":        "Steady",
            "beep_interval": 0.4,
        }
    else:
        return {
            "color":         RED if blink_state else OFF,
            "color_name":    "Red",
            "status":        "Blinking",
            "beep_interval": 0,
        }


def is_heartbeat_on(elapsed):
    """Return True when the heartbeat LED should be ON.

    Pattern: 100 ms ON / 900 ms OFF per second.

    Args:
        elapsed: float, seconds since the last 1-second heartbeat reset
                 (i.e. now - last_heartbeat).

    Returns:
        bool
    """
    return elapsed < 0.1
