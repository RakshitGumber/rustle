import typer
from commands.health import health_app
from commands.weather import weather_app

from view.help import show_help

app = typer.Typer()

app.add_typer(health_app, name="health")
app.add_typer(weather_app, name="weather")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context, help: bool = typer.Option(None, "--help", "-h", is_eager=True)
):
    if ctx.invoked_subcommand is None:
        show_help()


if __name__ == "__main__":
    app()
