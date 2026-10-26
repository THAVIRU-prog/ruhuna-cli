import typer
import webbrowser
from rich import print
from rich.table import Table

# Initialize the Typer app
app = typer.Typer(help="Ruhuna CS Student Utility CLI 🚀")

@app.command()
def hello(name: str = "Student"):
    """Greet the user with a customized welcome message."""
    print(f"[bold green]✨ Hello, {name}! Welcome to your Ruhuna CS Developer CLI.[/bold green]")
    print("[italic dim]Built with Python, Typer, and Rich.[/italic dim]")

@app.command()
def links_official():
    """Open official University and Faculty web portals in your browser."""
    print("[bold cyan]🌐 Opening University of Ruhuna portal...[/bold cyan]")

    webbrowser.open("https://www.ruh.ac.lk/")

@app.command()
def links_scilms():
    """Open official university Science Faculty LMS web portal in your browser."""
    print("[bold cyan]🌐 Opening Faculty of science LMS...[/bold cyan]")

    webbrowser.open("http://scilms.ruh.ac.lk/science/login/index.php")


@app.command()
def gpa(M1c: float, M1g: float, M2c: float, M2g: float,M3c: float, M3g: float, M4c: float, M4g: float,M5c: float, M5g: float, M6c: float, M6g: float,M7c: float, M7g: float):
    """Calculate a simple semester GPA based on 7 modules."""
    total_credits = M1c+M2c+M3c+M4c+M5c+M6c+M7c
    total_points = (M1c * M1g) + (M2c * M2g) + (M3c * M3g) + (M4c * M4g) +(M5c * M5g) + (M6c * M6g) +(M7c * M7g) 
    
    if total_credits == 0:
        final_gpa = 0.0
    else:
        final_gpa = total_points / total_credits

    # Create a nice Rich table to display results
    table = Table(title="📊 GPA Calculation Results")
    table.add_column("Module", style="magenta")
    table.add_column("Credits", justify="right", style="cyan")
    table.add_column("Grade Points", justify="right", style="green")

    table.add_row("Module 1", str(M1c), str(M1g))
    table.add_row("Module 2", str(M2c), str(M2g))
    table.add_row("Module 3", str(M3c), str(M3g))
    table.add_row("Module 4", str(M4c), str(M4g))
    table.add_row("Module 5", str(M5c), str(M5g))
    table.add_row("Module 6", str(M6c), str(M6g))
    table.add_row("Module 7", str(M7c), str(M7g))

    print(table)
    print(f"\n[bold yellow]Your Estimated Semester GPA: {final_gpa:.2f}[/bold yellow]")

if __name__ == "__main__":
    app()