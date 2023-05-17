import logging

import initialize
import map as map_csv
import validate_state
from fetch_address import fetch_address
from generate_csv import generate_csv


def scraper(config=initialize.setup_args()) -> None:
    """
    CLI Program that scrapes addresses from the web given a state.

    Args:
        config : Argument list called by argparse. Defaults to None.

    Raises:
        ValueError: if the state or state code is invalid
    """

    logging_level = logging.DEBUG if config["verbose"] else logging.INFO
    logger = initialize.Logger(__name__, logging_level).logger

    state = validate_state.get_state_code(config["state"])
    if not state:
        raise ValueError("Invalid state or state code")

    total: int = config["total"]
    limit: int = config["limit"]

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
        addresses = [address for address in fetch_address(state, limit, offset=offset)]

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

    if config["map"]:
        map_csv.map(filename)


if __name__ == "__main__":
    scraper()
