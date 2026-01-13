import click
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live
from rich.text import Text

console = Console()

def print_banner():
    banner_text = Text.assemble(
        ("🚗 ", "bold bright_white"),
        ("CarCANex ", "bold cyan"),
        ("— ", "white"),
        ("CAN Explorer & eXchange", "italic blue"),
        ("\n", ""),
        ("Modern Vehicle CAN Analysis SDK", "dim white")
    )
    console.print(Panel(banner_text, border_style="bright_blue", padding=(1, 2), expand=False))

@click.group()
def cli():
    """CarCANex CLI - CAN Analysis & Vehicle Interface Utility"""
    pass

@cli.command()
@click.option('--dbc', type=click.Path(exists=True), help='Path to DBC file')
@click.option('--log', type=click.Path(exists=True), help='Path to CAN log file')
def parse(dbc, log):
    """Parse a CAN log using a DBC file and extract signals."""
    print_banner()
    if not dbc or not log:
        console.print("[bold red]❌ Error:[/bold red] Please provide both [bold cyan]--dbc[/bold cyan] and [bold cyan]--log[/bold cyan] arguments.")
        return

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Loading DBC database...", total=None)
        time.sleep(1) # Fake delay for aesthetic
        progress.add_task(description="Parsing CAN log entries...", total=None)
        time.sleep(1.5)

    table = Table(title="Captured CAN Signals", title_style="bold magenta")
    table.add_column("Timestamp", style="dim cyan", no_wrap=True)
    table.add_column("CAN ID", style="bold yellow")
    table.add_column("Signal Name", style="bold green")
    table.add_column("Value", justify="right", style="bold white")
    table.add_column("Unit", style="italic blue")

    # Mock data for demonstration
    table.add_row("1705132942.123", "0x201", "STEER_ANGLE", "12.5", "deg")
    table.add_row("1705132942.456", "0x201", "STEER_RATE", "2.1", "deg/s")
    table.add_row("1705132942.789", "0x301", "VEHICLE_SPEED", "88.4", "km/h")

    console.print(table)
    console.print("\n[bold green]✅ Success:[/bold green] Parsing complete. 3 signals extracted.")

@cli.command()
@click.option('--interface', default='can0', help='CAN interface (e.g., can0, vcan0)')
def monitor(interface):
    """Real-time CAN bus monitor with signal decoding."""
    print_banner()
    console.print(f"[bold cyan]🔍 Monitoring active on interface:[/bold cyan] [underline]{interface}[/underline]\n")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="yellow", width=8)
    table.add_column("DLC", style="white", width=4)
    table.add_column("Data (Hex)", style="green")
    table.add_column("Decoded Signal", style="cyan")

    with Live(table, refresh_per_second=4, screen=False):
        for i in range(5): # Simulating 5 packets
            time.sleep(0.5)
            table.add_row("0x123", "8", "00 FF 11 22 33 44 55 66", "SPEED: 120km/h")
            
    console.print("\n[bold yellow]⚠️  Monitoring stopped.[/bold yellow]")

@cli.command()
def version():
    """Show the version of CarCANex."""
    console.print(Panel("[bold cyan]CarCANex[/bold cyan] version [bold green]0.1.0[/bold green]", border_style="dim"))

def main():
    cli()

if __name__ == "__main__":
    main()
