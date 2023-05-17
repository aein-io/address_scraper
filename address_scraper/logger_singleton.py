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
