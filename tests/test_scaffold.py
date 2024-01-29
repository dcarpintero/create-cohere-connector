import unittest
import os
from connector.scaffold import Scaffolder


class TestScaffoldLogic(unittest.TestCase):
    """
    Test the logic of the Scaffolder class
    """
    scaffolder = Scaffolder()
    base_path = './tests/output/'
    project_template_path = './templates/project_template.py.jinja'

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

    def test_create_file(self):
        """
        Test create_file function
        """
        test_file = os.path.join(self.base_path, 'test_file.txt')

        self.scaffolder.create_file(test_file, 'Test content')
        self.assertTrue(os.path.isfile(test_file))
        with open(test_file, 'r', encoding='utf-8') as file: 
            content = file.read()
        self.assertEqual(content, 'Test content')
        # Clean up
        os.remove(test_file)

    def test_scaffold_cohere_connector(self):
        """
        Test scaffold_cohere_connector function
        """
        self.scaffolder.cohere_connector()
        self.assertTrue(os.path.isdir('provider'))
        self.assertTrue(os.path.isfile('deploy.py'))
        self.assertTrue(os.path.isfile('.env-template'))
        self.assertTrue(os.path.isfile('README.md'))
        self.assertTrue(os.path.isfile('pyproject.toml'))
        # Clean up
        os.remove('deploy.py')
        os.remove('.env-template')
        os.remove('README.md')
        os.remove('pyproject.toml')
        os.rmdir('provider')

if __name__ == '__main__':
    unittest.main()
