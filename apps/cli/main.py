import logging
from collections import deque
import requests

from pyfiglet import Figlet

from dotenv import load_dotenv
import os

from rich.console import Console
from rich.panel import Panel

console = Console()

from rich.table import Table

load_dotenv()

WEATHER_API = os.getenv("WEATHER_API")
BASE_URL = "https://api.weatherapi.com/v1"

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
def current(city: str = typer.Option("Delhi", "--city", "-c")):
    try:
        url = f"{BASE_URL}/current.json?key={WEATHER_API}&q={city}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            display_weather(data)
        else:
            print(f"Server returned status code: {response.status_code}")
            raise ValueError("Unable to fetch result")
    except Exception as e:
        print("Ran into an error x_x")
        log_error(str(e))
        raise typer.Exit(code=1)


def display_weather(data):
    current = data["current"]

    table = Table(show_header=False)
    table.add_row("☀ Condition", current["condition"]["text"])
    table.add_row("🌡 Temperature", f'{current["temp_c"]}°C')
    table.add_row("💧 Humidity", f'{current["humidity"]}%')
    table.add_row("💨 Wind", f'{current["wind_kph"]} km/h')
    table.add_row("☀ UV Index", str(current["uv"]))
    table.add_row("👁 Visibility", f'{current["vis_km"]} km')
    table.add_row("🌧 Rain Chance", f'{current["chance_of_rain"]}%')

    console.print(table)


@health_app.command()
def logs(lines: int = 20):
    try:
        with open(LOG_FILE, "r") as f:
            last_lines = deque(f, maxlen=lines)

        for line in last_lines:
            print(line, end="")

    except FileNotFoundError:
        print("No log file found.")


app.add_typer(health_app, name="health")
app.add_typer(weather_app, name="weather")


def show_banner():
    fig = Figlet(font="slant")
    banner = fig.renderText("Rustle")

    console.print(f"[bold cyan]{banner}[/bold cyan]")


def show_help():

    show_banner()

    console.print(
        Panel.fit(
            "[bold]Rustle[/bold]\n" "RSS Feed Engine & Utility Toolkit",
            border_style="cyan",
        )
    )

    commands = Table(title="Commands", show_header=True, header_style="bold cyan")

    commands.add_column("Command")
    commands.add_column("Description")

    commands.add_row("weather current", "Current weather information")

    commands.add_row("health status", "Check application health")

    commands.add_row("health logs", "View recent logs")

    console.print(commands)

    console.print()

    examples = Table(title="Examples", show_header=False)

    examples.add_row("[green]rustle weather current[/green]", "Delhi weather")

    examples.add_row(
        "[green]rustle weather current -c Mumbai[/green]", "Mumbai weather"
    )

    examples.add_row("[green]rustle health logs[/green]", "Last 20 logs")

    console.print(examples)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context, help: bool = typer.Option(None, "--help", "-h", is_eager=True)
):
    if ctx.invoked_subcommand is None:
        show_help()


if __name__ == "__main__":
    app()
