"""TC_BUZZER_ON–TC_BUZZER_OFF – Buzzer threshold at 20 cm."""
from park_logic import buzzer_active


def test_buzzer_on_below_threshold():
    # @ Buzzer on below 20 cm, TI_BUZZER_ON, test_impl, [TC_BUZZER_ON]
    """TC_BUZZER_ON: buzzer active when dist_cm < 20."""
    assert buzzer_active(15) is True


def test_buzzer_off_at_threshold():
    # @ Buzzer off at 20 cm, TI_BUZZER_OFF_EXACT, test_impl, [TC_BUZZER_OFF]
    """TC_BUZZER_OFF: buzzer silent at exactly 20 cm."""
    assert buzzer_active(20) is False


def test_buzzer_off_above_threshold():
    # @ Buzzer off above 20 cm, TI_BUZZER_OFF_ABOVE, test_impl, [TC_BUZZER_OFF]
    """TC_BUZZER_OFF: buzzer silent above 20 cm."""
    assert buzzer_active(25) is False
