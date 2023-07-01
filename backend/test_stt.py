import unittest
from unittest.mock import patch

from backend.stt import delete_file, transcribe


class TestSTT(unittest.TestCase):
    def test_delete_file_should_remove_filepath(self):
        with patch('backend.stt.os.remove') as mock:
            delete_file('')
            mock.assert_called()

    def test_transcribe_should_return_a_transcription(self):
        pass


if __name__ == '__main__':
    unittest.main()
