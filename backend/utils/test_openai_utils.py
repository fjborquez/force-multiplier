import asyncio
import unittest
from unittest.mock import patch

from openai.openai_object import OpenAIObject

from backend.utils import OpenAIUtils


class TestOpenAIUtils(unittest.TestCase):
    async def test_transcribe_should_return_openai_response(self):
        with patch('openai.Audio.atranscribe'):
            response = await asyncio.run(OpenAIUtils.transcribe(audio=None, api_key=''))
            self.assertTrue(isinstance(response, OpenAIObject))


if __name__ == '__main__':
    unittest.main()
