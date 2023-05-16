import requests
from payload import payload, headers, url


def fetch_address(state_code: str, api_key=headers["X-Rapid-API-Key"], payload: dict = payload, headers: dict = headers, url: str = url) -> list:
    """
    Fetches addresses from the API.

    Args:
        state (string): The state input by the user.
        payload (dictionary): API request payload. 
        headers (dictionary): API request headers.
        url (string): API request url.

    Returns: 
        list: A list of dictionaries that store the addresses.
    """
    payload["state_code"] = state_code

    if api_key != headers["X-Rapid-Api"]:
        headers["X-Rapid-Api"] = api_key

    try:
        response = requests.post(url, json=payload, headers=headers)

        data = response.json()
        index = data["data"]["home_search"]["results"]

        dataset = [parse_address(index)
                   for _ in index]

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
    location = data["location"]

    details = {
        "city": location["city"],
        "line": location["line"],
        "street_name": location["street_name"],
        "street_number": location["street_number"],
        "street_suffix": location["street_suffix"],
        "country": location["country"],
        "postal_code": location["postal_code"],
        "state_code": location["state_code"],
        "state": location["state"],
        "coordinates": generate_coords(location["coordinate"]["lat"], location["coordinate"]["lon"]),
        "lat": location["coordinate"]["lat"],
        "lon": location["coordinate"]["lon"]
    }
    return details


def generate_coords(lat, lon):
    """
    Combines latitude and longitude into a coordinates.

    Args:
        lat (float): The latitude. 
        lon (float): The longitude.

    Returns:
        str: A string that contains the coordinates.
    """
    return f"{lat},{lon}"
