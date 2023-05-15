from src.address_scraper import add_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5
