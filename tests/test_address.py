from address_scraper.address_scraper.address import Address
from pydantic import ValidationError
from pytest import raises

valid = {
    "city": "San Francisco",
    "line": "1600 Pennsylvania Ave NW",
    "street_name": "Pennsylvania",
    "street_number": "1600",
    "street_suffix": "Ave",
    "country": "US",
    "postal_code": "20500",
    "state_code": "NY",
    "state": "New York",
    "coordinates": "40.714224,-73.961452",
    "lat": 40.714224,
    "lon": -73.961452,
}

invalid_types = {
    "city": "",
    "line": "",
    "street_name": "",
    "street_number": "",
    "street_suffix": "",
    "country": 1.50,
    "postal_code": None,
    "state_code": None,
    "state": 1.40,
    "coordinates": None,
    "lat": "40.714224",
    "lon": "-73.961452",
}


address = Address(**valid)


def test_address():
    assert address.city == "San Francisco"
    assert address.line == "1600 Pennsylvania Ave NW"
    assert address.street_name == "Pennsylvania"
    assert address.street_number == "1600"
    assert address.street_suffix == "Ave"
    assert address.country == "US"
    assert address.postal_code == "20500"
    assert address.state_code == "NY"
    assert address.state == "New York"
    assert address.coordinates == "40.714224,-73.961452"
    assert address.lat == 40.714224
    assert address.lon == -73.961452


def test_address_types():
    # TODO: @aaron validate address types
    with raises(ValidationError):
        Address(**invalid_types)


def test_mutability():

    with raises(TypeError):
        address.city = "New York"
    with raises(TypeError):
        address.line = "1600 Pennsylvania Ave NW"
    with raises(TypeError):
        address.street_name = "Pennsylvania"
    with raises(TypeError):
        address.street_number = "1600"
    with raises(TypeError):
        address.street_suffix = "Ave"
    with raises(TypeError):
        address.country = "US"
    with raises(TypeError):
        address.postal_code = "20500"
    with raises(TypeError):
        address.state_code = "NY"
    with raises(TypeError):
        address.state = "New York"
    with raises(TypeError):
        address.coordinates = "40.714224,-73.961452"
    with raises(TypeError):
        address.lat = 40.714224
    with raises(TypeError):
        address.lon = -73.961452
