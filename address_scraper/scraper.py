
import logging

from fetch_address import fetch_address
from generate_csv import generate_csv

import initialize
import validate_state

# TODO: Tanggalin ba to
# Path: address_scraper/scraper.py


def scraper(args=None):
    """
    CLI Program that scrapes addresses from the web given a state.

    Args:
        #TODO: Add type and desc
        args (_type_, optional): _description_. Defaults to None.

    Raises:
        #TODO: Add desc
        ValueError: _description_
    """

    if not args:
        args = initialize.setup_args()

    logging_level = logging.DEBUG if args.verbose else logging.INFO
    logger = initialize.Logger(__name__, logging_level).logger

    state = validate_state.get_state_code(args.state)
    if not state:
        raise ValueError("Invalid state or state code")

    requests: int = args.requests
    limit: int = args.limit

    routines = limit/requests  # the number of routines to run

    offset: int = requests
    headerflag: bool = True

    logger.info(f"Scraping {state} for {requests} addresses")
    while routines > 0:

        addresses = [address for address in fetch_address(
            state, requests, offset=offset)]

        csv_file = generate_csv(addresses, flag=headerflag)
        logger.info(f"Generated {csv_file} with {requests} addresses")

        # write csv file to disk
        with open(f"{state}_{limit}.csv", "a") as f:
            content = csv_file.getvalue()
            f.write(content)
            logger.debug(f"Wrote {requests} addresses to {f.name}")
            logger.debug(f"\t {content}")

        routines -= 1
        offset += requests
        headerflag = False


if __name__ == "__main__":
    scraper()
