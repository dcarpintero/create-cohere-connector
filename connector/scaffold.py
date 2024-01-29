"""	
Scaffold a custom Cohere connector project
"""
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


class Scaffolder:
    def __init__(self):
        pass

    def render_template(self, template_name, context=None):
        """
        Render a Jinja2 template
        """
        if context is None:
            context = {}

        env = Environment(
            loader=FileSystemLoader(searchpath="./templates"),
            autoescape=select_autoescape()
        )
        template = env.get_template(template_name)
        return template.render(context)

    def create_directory(self, path):
        """
        Create a directory if it doesn't exist
        """
        try:
            os.makedirs(path)
            print(f"Directory '{path}' created")
        except FileExistsError:
            print(f"Directory '{path}' already exists")

    def create_file(self, path, content=''):
        """
        Create a file if it doesn't exist
        """
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"File '{path}' created")

    def project(self, project_name):
        """
        Scaffold a Python Poetry project
        """

        # Render pyproject.toml template
        pyproject_content = self.render_template('pyproject_template.toml', {
                                            'project_name': project_name})
        self.create_file(f'{project_name}/pyproject.toml', pyproject_content)

    def cohere_connector(self):
        """
        Scaffold a custom Cohere connector project
        """
        # Create 'provider' directory
        self.create_directory('provider')

        # Create 'app.py' inside the 'provider' directory
        app_content = ""
        self.create_file('provider/app.py', app_content)

        # Render and create 'deploy.py' using Jinja2
        deploy_content = self.render_template('deploy_template.py.jinja')
        self.create_file('deploy.py', deploy_content)

        # Create '.env-template', 'README.md', and 'pyproject.toml' at the root
        self.create_file('.env-template', '# Environment variables template')
        self.create_file('README.md', '# Project Title\n\nDescription of your project.')
        self.create_file('pyproject.toml',
                    '[tool.poetry]\nname = "provider"\nversion = "0.1.0"')


def main():
    """
    Scaffold a custom Cohere connector project
    """
    scaffolder = Scaffolder()
    scaffolder.cohere_connector()


if __name__ == "__main__":
    main()