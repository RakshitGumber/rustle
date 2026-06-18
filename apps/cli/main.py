import typer

from functions.weather.weather import weather
from functions.greet.greet import greet
from functions.health.doctor import doctor

app = typer.Typer()

app.command()(weather)
app.command()(greet)
app.command()(doctor)

if __name__ == "__main__":
    app()
