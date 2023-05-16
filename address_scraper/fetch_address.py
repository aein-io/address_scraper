import requests
from payload import payload, headers, url


def fetch_address(state_code: str, limit: int = payload["limit"], api_key: str = headers["X-RapidAPI-Key"], payload: dict = payload, headers: dict = headers, url: str = url) -> list:
    """
    Fetches addresses from the API.

    Args:
        state (string): The state input by the user.
        limit (int): Limit for the API request.
        api_key (string): The API key for the request.
        payload (dictionary): API request payload. 
        headers (dictionary): API request headers.
        url (string): API request url.

    Returns: 
        list: A list of dictionaries that store the addresses.
    """
    payload["state_code"] = state_code

    if api_key != headers["X-RapidAPI-Key"]:
        headers["X-RapidAPI-Key"] = api_key

    if limit != payload["limit"]:
        payload["limit"] = limit

    try:
        response = requests.post(url, json=payload, headers=headers)

        data = response.json()
        results = data["data"]["home_search"]["results"]

        dataset = [parse_address(result)
                   for result in results]

        return dataset
    except (requests.RequestException, requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
        return e


def parse_address(data: dict) -> dict:
    """
    Parses addresses from the API.

    Args:
        data (dict): The dictionary that stores data from the JSON request.

    Returns: 
        dict: A dictionary that stores the details of the address.
    """
    print(data)
    location = data["location"]
    address = location["address"]
    coordinate = address["coordinate"]

    details = {
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
        "lon": coordinate["lon"]
    }
    return details


def generate_coords(lat, lon):
    """
    Combines latitude and longitude into coordinates.

    Args:
        lat (float): The latitude. 
        lon (float): The longitude.

    Returns:
        str: A string that contains the coordinates.
    """
    return f"{lat},{lon}"
