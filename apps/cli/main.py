import logging
from collections import deque

import typer

app = typer.Typer()

health_app = typer.Typer()
weather_app = typer.Typer()

LOG_FILE = "rustle.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_error(message: str):
    logging.error(message)


@health_app.command()
def status():
    try:
        print("Working: OK")
        # raise ValueError("Database connection failed")
    except Exception as e:
        log_error(str(e))
        raise typer.Exit(code=1)


@weather_app.command()
def current():
    try:
        raise ValueError("Failed to fetch weather")
    except Exception as e:
        print("Ran into an error x_x")
        log_error(str(e))
        raise typer.Exit(code=1)


@app.command()
def logs(lines: int = 20):
    """
    Show the last N lines from the log file.
    """
    try:
        with open(LOG_FILE, "r") as f:
            last_lines = deque(f, maxlen=lines)

        for line in last_lines:
            print(line, end="")

    except FileNotFoundError:
        print("No log file found.")


app.add_typer(health_app, name="health")
app.add_typer(weather_app, name="weather")

if __name__ == "__main__":
    app()
