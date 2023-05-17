from address_scraper.address_scraper.fetch_address import fetch_address
from address_scraper.address_scraper.payload import url, payload, headers
from unittest.mock import Mock, patch


def test_fetch_address():
    """
    Test case for testing the successful execution of fetch_address.
    """
    state_code = "TX"
    expected_result = [
        {
            "city": "Colorado City",
            "line": "840 Chestnut St",
            "street_name": "Chestnut",
            "street_number": "840",
            "street_suffix": "St",
            "country": "USA",
            "postal_code": "79512",
            "state_code": "TX",
            "state": "Texas",
            "coordinates": "32.395367,-100.863693",
            "lat": 32.395367,
            "lon": -100.863693
        },
        {
            "city": "Canyon",
            "line": "606 College St",
            "street_name": "College",
            "street_number": "606",
            "street_suffix": "St",
            "country": "USA",
            "postal_code": "79015",
            "state_code": "TX",
            "state": "Texas",
            "coordinates": "34.977005,-101.91490967",
            "lat": 34.977005,
            "lon": -101.91490967
        }
    ]

    mock_response = Mock()
    mock_response.json.return_value = {
        "data": {
            "home_search": {
                "results": [
                    {
                        "location": {
                            "address": {
                                "city": "Colorado City",
                                "line": "840 Chestnut St",
                                "street_name": "Chestnut",
                                "street_number": "840",
                                "street_suffix": "St",
                                "country": "USA",
                                "postal_code": "79512",
                                "state_code": "TX",
                                "state": "Texas",
                                "coordinate": {
                                        "lat": 32.395367,
                                        "lon": -100.863693
                                }
                            }
                        }
                    },
                    {
                        "location": {
                            "address": {
                                "city": "Canyon",
                                "line": "606 College St",
                                "street_name": "College",
                                "street_number": "606",
                                "street_suffix": "St",
                                "country": "USA",
                                "postal_code": "79015",
                                "state_code": "TX",
                                "state": "Texas",
                                "coordinate": {
                                        "lat": 34.977005,
                                        "lon": -101.91490967
                                }
                            }
                        }
                    }
                ]
            }
        }
    }

    with patch("requests.post", return_value=mock_response) as mock_post:
        result = fetch_address(state_code)
        # convert address object to dict
        result = [address.dict() for address in result]

        mock_post.assert_called_once_with(
            url, json=payload, headers=headers)

        assert result == expected_result
