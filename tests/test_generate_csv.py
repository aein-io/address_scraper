import os

import pytest

from address_scraper.address_scraper.address import Address
from address_scraper.address_scraper.generate_csv import generate_csv


def generate_test_dataset(count=1):
    t_dataset = [
        Address(
            city="city",
            line="line",
            street_name="street_name",
            street_number="street_number",
            street_suffix="street_suffix",
            country="country",
            postal_code="postal_code",
            state_code="state_code",
            state="state",
            coordinates="coordinates",
            lat=0.0,
            lon=0.0,
        )
        for _ in range(count)
    ]
    t_csv = generate_csv(t_dataset)
    return t_csv


def test_generate_csv():
    # test the length of the csv file
    t_csv = generate_test_dataset()
    assert len(t_csv.readlines()) == 2
    t_csv = generate_test_dataset(10)
    assert len(t_csv.readlines()) == 11
    t_csv = generate_test_dataset(100)
    assert len(t_csv.readlines()) == 101

    with pytest.raises(IndexError):
        generate_csv([])


def test_csv_iswritten():
    t_csv = generate_test_dataset()

    assert t_csv.writable() is True

    assert t_csv.getvalue() == t_csv.read()

    with open("test.csv", "w") as f:
        f.write(t_csv.getvalue())

    assert os.path.exists("test.csv")

    os.remove("test.csv")


def test_written_csv():
    headers = [
        "city",
        "line",
        "street_name",
        "street_number",
        "street_suffix",
        "country",
        "postal_code",
        "state_code",
        "state",
        "coordinates",
        "lat",
        "lon",
    ]

    def test_line_count(file, count):
        file.seek(0)
        assert len(file.readlines()) == count

    def test_column_count(file, count):
        file.seek(0)
        assert len(file.readline().split(",")) == count

    def test_headers(file, headers):
        file.seek(0)
        assert list(map(str.strip, file.readline().split(","))) == headers

    def test_properties(count=1):
        t_csv = generate_test_dataset(count)
        # write to file
        with open("test.csv", "w") as f:
            f.write(t_csv.getvalue())

        # read from file
        with open("test.csv", "r") as f:
            test_line_count(f, count + 1)
            test_column_count(f, 12)
            test_headers(f, headers)

        os.remove("test.csv")

    test_properties()
    test_properties(10)
    test_properties(100)
    test_properties(1000)
