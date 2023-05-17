import argparse
import logging


class Logger:
    """
    A logger singleton that has two modes: INFO and DEBUG.

    Attribute:
        _instance (Logger): instance container for logger singleton

    Returns:
        Logger: the logger singleton
    """

    _instance = None

    def __new__(cls, name, logging_level):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.setup_logger(name, logging_level)
        return cls._instance

    def setup_logger(self, name, logging_level):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Create a file handler and set the log level
        file_handler = logging.FileHandler("log_file.log")
        file_handler.setLevel(logging_level)
        file_handler.setFormatter(formatter)

        # Create a console handler and set the log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging_level)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


def setup_args():
    """
    Defines and returns the arguments required by the scraper.
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

    MAXIMUM_API_REQUESTS = 10000

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
        default=MAXIMUM_API_REQUESTS,
    )

    parser.add_argument(
        "-l",
        "--limit",
        type=positive(int),
        help="API request limit per iteration",
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

    parser.add_argument(
        "-m",
        "--map",
        help="Display the output addresses to a map",
        action="store_true",
        required=False,
    )

    # create config dictionary
    args = parser.parse_args()
    config = {
        "state": args.state,
        "total": args.total,
        "limit": args.limit,
        "verbose": args.verbose,
        "map": args.map,
    }

    return config
