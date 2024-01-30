"""	
Scaffold a custom Cohere connector project
"""
import os
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, select_autoescape


@dataclass
class ScaffolderConfig:
    """
    Configuration settings
    """
    TEMPLATES_DIR = './_templates_'
    OUTPUT_DIR = './output'
    PROJECT_TEMPLATE = 'project_template.py.jinja'
    DEPLOY_TEMPLATE = 'deploy_template.py.jinja'
    ENV_TEMPLATE = 'env_template.jinja'

class Scaffolder:
    """
    Scaffold a custom Cohere connector project
    """
    def __init__(self):
        self.config = ScaffolderConfig()


    def render_template(self, template_name, context=None):
        """
        Render a Jinja2 template
        """
        if context is None:
            context = {}

        env = Environment(
            loader=FileSystemLoader(searchpath=self.config.TEMPLATES_DIR),
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


    def cohere_connector(self, project_name):
        """
        Scaffold a custom Cohere connector project
        """
        # Create 'base' directory
        base_path = project_name
        self.create_directory(base_path)

        # Create 'provider' directory
        provider_path = os.path.join(base_path, 'provider')
        self.create_directory(provider_path)
        self.create_file(f'{provider_path}/__init__.py')

        # pyproject.toml
        pyproject_content = self.render_template(self.config.PROJECT_TEMPLATE, {'project_name': project_name})
        self.create_file(f'{project_name}/pyproject.toml', pyproject_content)

        # .env-template
        env_content = self.render_template(self.config.ENV_TEMPLATE)
        self.create_file(f'{project_name}/.env-template', env_content)

        # deploy.py
        deploy_content = self.render_template(self.config.DEPLOY_TEMPLATE)
        file_path = os.path.join(base_path, 'deploy.py')
        self.create_file(file_path, deploy_content)

        # README.md
        readme_content = self.render_template('README.md.jinja', {'project_name': project_name})
        self.create_file(f'{project_name}/README.md', readme_content)

        # .gitingore
        gitignore_content = self.render_template('.gitignore.jinja')
        self.create_file(f'{project_name}/.gitignore', gitignore_content)

        # provider/app.py
        app_content = self.render_template('app.py.jinja')
        file_path = os.path.join(provider_path, 'app.py')
        self.create_file(file_path, app_content)

        # provider/client.py
        client_content = self.render_template('client.py.jinja')
        file_path = os.path.join(provider_path, 'client.py')
        self.create_file(file_path, client_content)

        # provider/datamodels.py
        datamodels_content = self.render_template('datamodels.py.jinja')
        file_path = os.path.join(provider_path, 'datamodels.py')
        self.create_file(file_path, datamodels_content)