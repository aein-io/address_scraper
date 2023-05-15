from address_scraper.validate_state import get_state_abbrev


def test_get_state_abbrev():
    assert get_state_abbrev('California') == 'CA'
    assert get_state_abbrev('New York') == 'NY'
