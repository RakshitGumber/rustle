from rich.table import Table
from rich.console import Console

console = Console()


def display_weather(data: dict) -> None:
    """Display weather data in a rich table."""
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


def generate_weather_html(data: dict) -> str:
    """Generate HTML for weather display."""
    current = data["current"]
    location = data["location"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rustle Weather</title>
        <style>
        body {{
            background:#111827;
            color:white;
            font-family:sans-serif;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }}
        .card {{
            background:#1f2937;
            padding:40px;
            border-radius:20px;
            width:400px;
        }}
        h1 {{ color:#60a5fa; }}
        .row {{ margin:15px 0; }}
        </style>
    </head>
    <body>
    <div class="card">
        <h1>🌤 Rustle Weather</h1>
        <h2>{location["name"]}</h2>
        <div class="row">Temperature: {current["temp_c"]}°C</div>
        <div class="row">Condition: {current["condition"]["text"]}</div>
        <div class="row">Humidity: {current["humidity"]}%</div>
        <div class="row">Wind: {current["wind_kph"]} km/h</div>
    </div>
    </body>
    </html>
    """
