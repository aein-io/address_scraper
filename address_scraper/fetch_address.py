# NOTE: @aeinnor
import requests
from payload import payload, headers, url

# TODO:


def fetch_address(state, payload=payload, headers=headers, url=url):
    '''
    Fetches address from API
    '''
    payload["state_code"] = state

    response = requests.request("GET", url, headers=headers, params=payload)
    dataset = [parse_address(params=entities)
               for entities in response.json()["properties"]]

    return dataset


# TODO:


def parse_address(params="INPUT"):
    '''
    Parses address from API
    '''
    # TODO: Crawl JSON
    ...


def generate_coords():
    ...
