import unittest
from unittest.mock import patch

from fastapi import UploadFile

from backend.utils import AudioUtils


class TestAudioUtils(unittest.TestCase):
    def test_convert_should_return_converted_filepath(self):
        file = UploadFile(file=None, filename='')
        with patch('backend.utils.audio_utils.FileUtils.write'), patch('backend.utils.audio_utils.ffmpeg'), \
                patch('backend.utils.audio_utils.FileUtils.delete'):
            result = AudioUtils.convert(file)
            self.assertTrue(isinstance(result, str))


if __name__ == '__main__':
    unittest.main()
