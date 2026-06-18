import typer

from functions.weather.run import weather
from functions.greet.run import greet
from functions.health.run import health

app = typer.Typer()

app.command()(weather)
app.command()(greet)
app.command()(health)

if __name__ == "__main__":
    app()
