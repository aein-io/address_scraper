from address_scraper.address_scraper.validate_state import get_state_code


def test_get_state_abbrev():
    from validate_state import get_state_code
    assert get_state_code('California') == 'CA'
    assert get_state_code('New York') == 'NY'
    assert get_state_code('NY') == 'NY'
