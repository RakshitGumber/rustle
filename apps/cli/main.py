import typer

# from commands.weather.run import weather
# from commands.greet.run import greet
# from commands.health.run import health

app = typer.Typer()

health_app = typer.Typer()


def status():
    print("Working: OK")


health_app.command()(status)


# app.command()(weather)
# app.command()(greet)
app.add_typer(health_app, name="health")

if __name__ == "__main__":
    app()
