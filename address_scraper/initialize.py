import argparse
import logging

DEFAULT_LIMIT = 10000

# TODO: @aaron pls add type hints :>


class Logger:
    """
    #TODO: Add summary

    Attribute:
        _instance (_type_): #TODO: Add type and desc

    Returns:
        _type_: #TODO: Add type and desc
    """
    _instance = None

    def __new__(cls, name, level=logging.DEBUG):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger(name)
            cls._instance.logger.setLevel(level)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            # Create console handler and set level to INFO
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(console_handler)

            # Create file handler and set level to DEBUG
            file_handler = logging.FileHandler(f"{name}.log")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)

        return cls._instance


def setup_args():
    """
    Defines and returns the arguments required by the scraper.
    """

    def positive(numeric_type):
        """
        #TODO: Add summary

        Args:
            numeric_type (_type_): #TODO: Add type and desc

        Returns:
            _type_: #TODO: Add type and desc
        """
        def require_positive(value):
            """
            #TODO: Add summary

            Args:
                value (_type_): #TODO: Add type and desc

            Raises:
                TypeError: If #TODO: Complete the statement

            Returns:
                _type_: #TODO: Add type and desc
            """
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
        "-l",
        "--limit",
        type=positive(int),
        help="Number of addresses to scrape",
        required=False,
        default=DEFAULT_LIMIT,
    )

    parser.add_argument(
        "-r",
        "--requests", type=positive(int),
        help="Number of requests per iteration",
        required=False,
        default=200,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Increase output verbosity",
        action="store_true",
        required=False,
    )

    return parser.parse_args()
