import os
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import logging

@dataclass
class ScaffolderConfig:
    """
    Configuration settings
    """
    BASE_DIR = Path(__file__).resolve().parent
    TEMPLATES_DIR = BASE_DIR / '_templates_'
    PROJECT_TEMPLATE = 'project_template.py.jinja'
    DEPLOY_TEMPLATE = 'deploy_template.py.jinja'
    ENV_TEMPLATE = 'env_template.jinja'
    README_TEMPLATE = 'README.md.jinja'
    GITIGNORE_TEMPLATE = '.gitignore.jinja'
    APP_TEMPLATE = 'app.py.jinja'
    CLIENT_TEMPLATE = 'client.py.jinja'
    DATAMODELS_TEMPLATE = 'datamodels.py.jinja'

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
        try:
            template = env.get_template(template_name)
            return template.render(context)
        except Exception as e:
            logging.error(f"Error rendering template {template_name}: {e}")
            raise

    def create_directory(self, path):
        """
        Create a directory if it doesn't exist
        """
        try:
            os.makedirs(path, exist_ok=True)
            logging.info(f"Directory '{path}' created")
        except Exception as e:
            logging.error(f"Error creating directory {path}: {e}")
            raise

    def create_file(self, path, content=''):
        """
        Create a file if it doesn't exist
        """
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
                logging.info(f"File '{path}' created")
        except Exception as e:
            logging.error(f"Error creating file {path}: {e}")
            raise

    def cohere_connector(self, project_name):
        """
        Scaffold a custom Cohere connector project
        """
        try:
            # Create 'base' directory
            base_path = Path(project_name)
            self.create_directory(base_path)

            # Create 'provider' directory
            provider_path = base_path / 'provider'
            self.create_directory(provider_path)
            self.create_file(provider_path / '__init__.py')

            # pyproject.toml
            pyproject_content = self.render_template(self.config.PROJECT_TEMPLATE, {'project_name': project_name})
            self.create_file(base_path / 'pyproject.toml', pyproject_content)

            # .env-template
            env_content = self.render_template(self.config.ENV_TEMPLATE)
            self.create_file(base_path / '.env-template', env_content)

            # deploy.py
            deploy_content = self.render_template(self.config.DEPLOY_TEMPLATE)
            self.create_file(base_path / 'deploy.py', deploy_content)

            # README.md
            readme_content = self.render_template(self.config.README_TEMPLATE, {'project_name': project_name})
            self.create_file(base_path / 'README.md', readme_content)

            # .gitignore
            gitignore_content = self.render_template(self.config.GITIGNORE_TEMPLATE)
            self.create_file(base_path / '.gitignore', gitignore_content)

            # provider/app.py
            app_content = self.render_template(self.config.APP_TEMPLATE)
            self.create_file(provider_path / 'app.py', app_content)

            # provider/client.py
            client_content = self.render_template(self.config.CLIENT_TEMPLATE)
            self.create_file(provider_path / 'client.py', client_content)

            # provider/datamodels.py
            datamodels_content = self.render_template(self.config.DATAMODELS_TEMPLATE)
            self.create_file(provider_path / 'datamodels.py', datamodels_content)

            # provider provider.py
            provider_content = self.render_template('provider.py.jinja')
            self.create_file(provider_path / 'provider.py', provider_content)

            # provider exceptions.py
            exceptions_content = self.render_template('exceptions.py.jinja')
            self.create_file(provider_path / 'exceptions.py', exceptions_content)

            # provider config.py
            config_content = self.render_template('config.py.jinja')
            self.create_file(provider_path / 'config.py', config_content)

        except Exception as e:
            logging.error(f"Error in cohere_connector: {e}")
            raise
