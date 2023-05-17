from collections.abc import Generator

import requests
from address import Address
from payload import headers
from payload import payload
from payload import url


def fetch_address(
    state_code: str,
    limit: int = payload["limit"],
    offset: int = payload["offset"],
    api_key: str = headers["X-RapidAPI-Key"],
    payload: dict = payload,
    headers: dict = headers,
    url: str = url,
) -> Generator:
    """
    Fetches addresses from the API.

    Args:
        state (string): The state input by the user.

        limit (int, optional): Limit for the API request.
            Defaults to payload["limit"].

        offset (int, optional): Offset for the API request.
            Defaults to payload["offset"].

        api_key (string, optional): The API key for the request.
            Defaults to headers["X-RapidApi-Key"].

        payload (dict, optional): API request payload. Defaults to payload.

        headers (dict, optional): API request headers. Defaults to headers.

        url (string, optional): API request url. Defaults to url.

    Returns:
        list: A list of dictionaries that store the addresses

    """

    payload["state_code"] = state_code
    if api_key != headers["X-RapidAPI-Key"]:
        headers["X-RapidAPI-Key"] = api_key

    if limit != payload["limit"]:
        payload["limit"] = limit

    if offset != payload["offset"]:
        payload["offset"] = offset

    try:
        response: requests.Response = requests.post(
            url, json=payload, headers=headers)
        response.raise_for_status()

        data: dict = response.json()
        results: list = data["data"]["home_search"]["results"]

        for result in results:
            yield parse_address(result)

    except (
        requests.RequestException,
        requests.ConnectionError,
        requests.HTTPError,
        requests.Timeout,
    ) as e:
        yield e


def parse_address(data: dict) -> dict:
    """
    Parses addresses from the API.

    Args:
        data (dict): The dictionary that stores data from the JSON request.

    Returns:
        dict: A dictionary that stores the details of the address.
    """
    location: dict = data["location"]
    address: dict = location["address"]
    coordinate: dict = address["coordinate"]

    for key, value in address.items():
        if value is None:
            address[key] = ""

    if coordinate is None:
        coordinate = {"lat": 0.0, "lon": 0.0}

    details: dict = {
        "city": address["city"],
        "line": address["line"],
        "street_name": address["street_name"],
        "street_number": address["street_number"],
        "street_suffix": address["street_suffix"],
        "country": address["country"],
        "postal_code": address["postal_code"],
        "state_code": address["state_code"],
        "state": address["state"],
        "coordinates": generate_coords(coordinate["lat"], coordinate["lon"]),
        "lat": coordinate["lat"],
        "lon": coordinate["lon"],
    }

    address = Address(**details)  # type: ignore
    return address


def generate_coords(lat: float, lon: float) -> str:
    """
    Combines latitude and longitude into coordinates.

    Args:
        lat (float): The latitude.
        lon (float): The longitude.

    Returns:
        str: A string that contains the coordinates.
    """
    return f"{lat},{lon}"
