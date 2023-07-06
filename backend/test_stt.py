import asyncio
import unittest
from unittest.mock import patch

from fastapi import UploadFile

from backend.stt import transcribe


class TestSTT(unittest.TestCase):
    def test_transcribe_should_return_a_transcription(self):
        audio = UploadFile(file=None, filename='')
        key = ''
        with patch('backend.stt.FileUtils.open'), patch('backend.stt.FileUtils.delete'), \
                patch('backend.stt.AudioUtils'), patch('backend.stt.OpenAIUtils.transcribe', return_value={'text': ''}):
            result = asyncio.run(transcribe(audio, key))
            self.assertTrue(isinstance(result, str))


if __name__ == '__main__':
    unittest.main()
