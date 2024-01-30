import os
import subprocess
import typer
from .scaffold import Scaffolder

app = typer.Typer()

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        error_message = result.stderr.strip() or result.stdout.strip()
        raise Exception(f"Error executing {' '.join(command)}: {error_message}")

@app.command()
def create_connector_project(
    project_name: str = typer.Option("myconnector", prompt=True),
    api_framework: str = typer.Option("FastAPI", prompt=True),
    authentication: str = typer.Option("Bearer", prompt=True),
    caching: str = typer.Option("None", prompt=True),
):
    try:
        typer.echo("\n⏳ Creating Connector Project...\n")

        scaffolder = Scaffolder()
        scaffolder.cohere_connector(project_name)

        typer.echo("\n🏗️  Installing dependencies...\n")

        os.chdir(project_name)
        run_command(["poetry", "install", "--no-root"])

        typer.echo("\n✅ Project created successfully!\n")

    except Exception as e:
        typer.echo(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    app()
