import requests
import config
import tempfile
import webbrowser
from pathlib import Path


def build_weather_url(city: str, endpoint: str = "current.json") -> str:
    """Build the API URL for weather requests."""
    return f"{config.BASE_URL}/{endpoint}?key={config.WEATHER_API}&q={city}&aqi=no"


def fetch_weather_data(city: str, endpoint: str = "current.json") -> dict:
    """Fetch weather data from the API."""
    url = build_weather_url(city, endpoint)
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Server returned status code: {response.status_code}")

    return response.json()


def open_html_in_browser(html: str, filename: str = "rustle_weather.html") -> None:
    """Save HTML to temp file and open in browser."""
    file = Path(tempfile.gettempdir()) / filename
    file.write_text(html, encoding="utf-8")
    webbrowser.open(file.as_uri())
