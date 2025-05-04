import logging
from typing import Union


def setup_logger(
    name: str,
    log_file: str,
    level: Union[int, str] = logging.INFO,
    existing_logger: logging.Logger = None,
) -> tuple[logging.Logger, logging.FileHandler]:
    """Set up a named logger that writes to a specific file.
    if existing_logger is provided, it will be used instead of creating a new one,
    and another handler will be added to it.
    """
    logger = existing_logger
    if not logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)

    # # Check if the logger already has a handler
    # if not logger.handlers:

    file_handeler = logging.FileHandler(log_file)
    file_handeler.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handeler.setFormatter(formatter)

    logger.addHandler(file_handeler)
    logger.info(f"Test Logger {name} set up with file handler for {log_file}")
    return logger, file_handeler
