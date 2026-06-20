import logging
import sys
from pathlib import Path

LOG_FILE = Path("logs/errors.log")


def setup_logger(name: str) -> logging.Logger:
    LOG_FILE.parent.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    )

    logger.addHandler(file_handler)
    return logger


def progress(msg: str):
    print(msg, flush=True)
