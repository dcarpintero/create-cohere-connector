import unittest
import os
from connector.scaffold import Scaffolder


class TestScaffoldLogic(unittest.TestCase):
    """
    Test the logic of the Scaffolder class
    """
    scaffolder = Scaffolder()
    base_path = './temp'
    project_template_path = './_templates_/project_template.py.jinja'
    project_template_path = 'project_template.py.jinja'

    def test_render_template(self):
        """
        Test render_template function
        """
        template_content = self.scaffolder.render_template(self.project_template_path, {'project_name': 'weather_connector'})
        self.assertIn('weather_connector', template_content)

    def test_create_directory(self):
        """
        Test create_directory function
        """
        test_dir = os.path.join(self.base_path, 'test_dir')

        self.scaffolder.create_directory(test_dir)
        self.assertTrue(os.path.isdir(test_dir))
        # Clean up
        os.rmdir(test_dir)
        os.rmdir(self.base_path)

    def test_create_file(self):
        """
        Test create_file function
        """
        test_file = os.path.join(self.base_path, 'test_file.txt')

        self.scaffolder.create_directory(self.base_path)
        self.scaffolder.create_file(test_file, 'Test content')
        self.assertTrue(os.path.isfile(test_file))
        with open(test_file, 'r', encoding='utf-8') as file: 
            content = file.read()
        self.assertEqual(content, 'Test content')
        # Clean up
        os.remove(test_file)
        os.rmdir(self.base_path)

    def test_scaffold_cohere_connector(self):
        """
        Test scaffold_cohere_connector function
        """
        base = 'myconnector'
        self.scaffolder.cohere_connector(base)

        self.__test_file(base, 'deploy.py')
        self.__test_file(base, 'README.md')
        self.__test_file(base, 'pyproject.toml')
        self.__test_file(base, '.env-template')
        self.__test_file(base, '.gitignore')
        self.__test_file(os.path.join(base, 'provider'), '__init__.py')
        self.__test_file(os.path.join(base, 'provider'), 'app.py')
        self.__test_file(os.path.join(base, 'provider'), 'client.py')


    def __test_file(self, project_name, file_name):
        """
        Test if a file exists, and remove it
        """
        file_path = os.path.join(project_name, file_name)
        self.assertTrue(os.path.isfile(file_path))
        #os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
