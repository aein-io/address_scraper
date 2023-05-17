import argparse

MAX_API_REQUESTS = 10000
MAX_PAYLOAD_LIMIT = 200


def setup_args(arguments: list[str]) -> argparse.Namespace:
    """
    Defines and returns the arguments required by the scraper.

    Args:
        list_args (list): List of arguments
            -s --state (str): State or state code to scrape addresses from
            -t --total (int): Total number of addresses to scrape
            -l --limit (int): API request limit per iteration
            -v --verbose (bool): Whether to log debug messages
            -m --map (bool): Whether to display the output addresses to a map

    Returns:
        args: argparse.Namespace with fields:
            state (str): State or state code to scrape addresses from
            limit (int): API request limit per iteration
            total (int): Total number of addresses to scrape
            verbose (bool): Whether to log debug messages
            map (bool): Whether to display the output addresses to a map
    """

    def positive(numeric_type):
        """
        Raises a TypeError if input is not positive

        Args:
            numeric_type (float|int): the numeric type to enforce positivity on

        Raises:
            TypeError: if the number is not positive

        Returns:
            numeric_type: positive numeric type
        """

        def require_positive(value):
            number = numeric_type(value)
            if number <= 0:
                raise TypeError(f"Number {value} must be positive.")
            return number

        return require_positive

    parser = argparse.ArgumentParser(
        description="Scrape addresses from the web given a state or state code"
    )

    parser.add_argument(
        "-s",
        "--state",
        type=str,
        help="State or state code to scrape addresses from",
        required=True,
    )

    parser.add_argument(
        "-t",
        "--total",
        type=positive(int),
        help="Total number of addresses to scrape",
        required=False,
        default=MAX_API_REQUESTS,
    )

    parser.add_argument(
        "-l",
        "--limit",
        type=positive(int),
        help="API request limit per iteration",
        required=False,
        default=MAX_PAYLOAD_LIMIT,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Increase output verbosity",
        action="store_true",
        required=False,
    )

    parser.add_argument(
        "-m",
        "--map",
        help="Display the output addresses to a map",
        action="store_true",
        required=False,
    )

    return parser.parse_args(arguments)
