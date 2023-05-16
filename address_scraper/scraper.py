
import logging

from fetch_address import fetch_address
from generate_csv import generate_csv

import initialize
import validate_state

# Path: address_scraper/scraper.py


def scraper(args=None):
    """CLI Program that scrapes addresses from the web given a state """

    if not args:
        args = initialize.setup_args()

    state = validate_state.get_state_code(args.state)
    if not state:
        raise ValueError("Invalid state or state code")

    requests = args.requests
    limit = args.limit

    logging_level = logging.DEBUG if args.verbose else logging.INFO
    logger = initialize.Logger(__name__, logging_level).logger

    logger.info(f"Scraping {state} for {requests} addresses")

    routines = limit/requests  # the number of routines to run

    while routines > 0:
        addresses = []
        for address in fetch_address(state, requests):
            addresses.append(address)

        csv_file = generate_csv(addresses)
        logger.info(f"Generated {csv_file} with {requests} addresses")

        # write csv file to disk
        with open(f"{state}_{routines}.csv", "a") as f:
            content = csv_file.getvalue()
            f.write(content)

        routines -= 1


if __name__ == "__main__":
    scraper()
