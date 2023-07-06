import logging
import os
import time
from typing import Coroutine, BinaryIO, Any

import openai
from openai.openai_object import OpenAIObject

LANGUAGE = os.getenv("LANGUAGE", "en")


class OpenAIUtils:
    @staticmethod
    async def transcribe(audio: BinaryIO, api_key: str, model: str = 'whisper-1') -> \
            Coroutine[Any, Any, list | OpenAIObject | dict]:
        start_time = time.time()
        logging.debug("calling whisper")
        response = await openai.Audio.atranscribe(model=model, file=audio, api_key=api_key, language=LANGUAGE)
        logging.info("STT response received from whisper in %s %s", time.time() - start_time, 'seconds')
        return response

    @staticmethod
    async def completion(**arguments):
        start_time = time.time()
        logging.debug("calling ChatCompletion")
        response =  await openai.ChatCompletion.acreate(**arguments)
        logging.info("Response received from ChatCompletion in %s %s", time.time() - start_time, 'seconds')
        return response
