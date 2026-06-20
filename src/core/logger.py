import logging
from collections import deque

LOG_FILE = "rustle.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_error(message: str):
    logging.error(message)


def read_logs(lines: int = 20):
    try:
        with open(LOG_FILE, "r") as f:
            last_lines = deque(f, maxlen=lines)

        for line in last_lines:
            print(line.rstrip())

    except FileNotFoundError:
        print("No log file found.")
