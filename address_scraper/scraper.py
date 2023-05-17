import logging
from sys import argv

import initialize
import map as map_csv
from fetch_address import fetch_address
from generate_csv import generate_csv
from logger_singleton import Logger
from validate_state import get_state_code


def scraper(config=initialize.setup_args(argv[1:])) -> None:
    """
    CLI Program that scrapes addresses from the web given a state.

    Args:
        config (optional): Dictionary of arguments
            state (str): State or state code to scrape addresses from
            limit (int): API request limit per iteration
            total (int): Total number of addresses to scrape
            verbose (bool): Whether to log debug messages
            map (bool): Whether to display the output addresses to a map


    Raises:
        ValueError: if the state or state code is invalid
    """
    state = get_state_code(config.state)
    if not state:
        raise SystemExit("Invalid state or state code")

    logging_level = logging.DEBUG if config.verbose else logging.INFO
    logger = Logger(__name__, logging_level).logger

    total: int = config.total
    limit: int = config.limit

    if limit > total:
        raise SystemExit("Limit cannot be greater than total")
    if limit > initialize.MAX_PAYLOAD_LIMIT:
        raise SystemExit("Total cannot be greater than 200")
    if total > initialize.MAX_API_REQUESTS:
        raise SystemExit("Total cannot be greater than 10000")

    offset: int = limit
    headerflag: bool = True

    routines = total / limit  # the number of routines to run
    logger.info(f"Scraping {state} for {limit} addresses")
    filename = f"{state}_{total}.csv"

    # remove any existing files named filename
    with open(filename, "w") as f:
        f.write("")
        logger.debug(f"Removed existing file {f.name}")

    while routines > 0:
        addresses = [address for address in fetch_address(
            state, limit, offset=offset)]

        try:
            csv_file = generate_csv(addresses, flag=headerflag)
        except IndexError:
            logger.error("Invalid address")
            continue

        logger.info(f"Generated {csv_file} with {limit} addresses")

        # write csv file to disk
        with open(filename, "a") as f:
            content = csv_file.getvalue()
            f.write(content)
            logger.debug(f"Wrote {limit} addresses to {f.name}")
            logger.debug(f"\t {content}")

        routines -= 1
        offset += limit
        headerflag = False

    if config.map:
        map_csv.map(filename, logger.debug)


if __name__ == "__main__":
    scraper()
