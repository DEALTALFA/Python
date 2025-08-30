
# showcase how to use rich module
# from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel
from rich.text import Text
from time import sleep

# Initialize console
console = Console()

# Create a fancy table
table = Table(title="Sample Data")
table.add_column("ID", style="cyan")
table.add_column("Name", style="magenta")
table.add_column("Score", justify="right", style="green")

# Add rows to table
table.add_row("1", "Alice", "95")
table.add_row("2", "Bob", "87")
table.add_row("3", "Charlie", "92")

# Print table
console.print(table)

# Show progress bar
for step in track(range(10), description="Processing..."):
    sleep(0.1)

# Print styled text
console.print("[bold red]Error:[/bold red] Something went wrong!", style="bold")
console.print("[blue]Info:[/blue] Task completed successfully!", style="italic")

# Create a panel
text = Text("Welcome to Rich Demo!")
text.stylize("bold magenta")
panel = Panel(text, title="Message", border_style="green")
console.print(panel)

# Print dictionary with syntax highlighting
data = {
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"]
}
console.print(data)