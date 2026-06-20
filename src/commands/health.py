import typer

from core.logger import read_logs

health_app = typer.Typer()


@health_app.command()
def status():
    print("Working: OK")


health_app.command()(read_logs)
