import os
import typer
from create_connector_project.scaffold import Scaffolder
from jinja2 import Environment, FileSystemLoader

app = typer.Typer()


@app.command()
def create_connector_project(
    project_name: str = typer.Option("myconnector", prompt=True),
    api_framework: str = typer.Option("FastAPI", prompt=True),
    authentication: str = typer.Option("Bearer", prompt=True),
    caching: str = typer.Option("None", prompt=True),
):
    typer.echo("\n⏳ Creating Connector Project...\n")

    scaffolder = Scaffolder()
    scaffolder.cohere_connector(project_name)

    typer.echo("\n🏗️  Installing dependencies...\n")

    os.chdir(project_name)
    os.system("poetry shell")
    os.system("poetry install --no-root")

    typer.echo("\n✅ Project created successfully!\n")


if __name__ == "__main__":
    app()
