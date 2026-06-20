from rich.console import Console
from pyfiglet import Figlet

from rich.panel import Panel
from rich.table import Table

console = Console()


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
