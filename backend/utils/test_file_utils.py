import unittest
from unittest.mock import patch

from backend.utils import FileUtils


class TestFileUtils(unittest.TestCase):
    def test_delete_file_should_remove_filepath(self):
        with patch('os.remove') as mock:
            FileUtils.delete('')
            mock.assert_called()

    def test_write_should_create_a_new_file(self):
        with patch('backend.utils.file_utils.open'), patch('shutil.copyfileobj') as mock:
            FileUtils.write('', None)
            mock.assert_called()

    def test_open_should_open_a_filepath(self):
        with patch('backend.utils.file_utils.open'):
            FileUtils.open('')


if __name__ == '__main__':
    unittest.main()
