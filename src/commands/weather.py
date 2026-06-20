import typer

from core.logger import log_error

from services.weather_service import fetch_weather_data, open_html_in_browser
from view.weather_view import display_weather, generate_weather_html

weather_app = typer.Typer()


def handle_error(error: Exception, message: str = "Ran into an error x_x") -> None:
    """Handle errors with logging and exit."""

    print(message)
    log_error(str(error))
    raise typer.Exit(code=1)


@weather_app.command()
def current(city: str = typer.Option("Delhi", "--city", "-c")):
    try:
        data = fetch_weather_data(city)
        display_weather(data)
    except Exception as e:
        handle_error(e)


@weather_app.command()
def open(city: str = "Delhi"):
    try:
        data = fetch_weather_data(city)
        html = generate_weather_html(data)
        open_html_in_browser(html)
    except Exception as e:
        handle_error(e)
