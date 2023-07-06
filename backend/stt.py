import logging

from fastapi import UploadFile

from utils import FileUtils, AudioUtils, OpenAIUtils


async def transcribe(audio: UploadFile, api_key: str) -> str:
    converted_filepath = AudioUtils.convert(audio)
    read_file = FileUtils.open(converted_filepath)

    res = await OpenAIUtils.transcribe(audio=read_file, api_key=api_key)
    transcription = res["text"]
    logging.info('user prompt: %s', transcription)

    FileUtils.delete(converted_filepath)

    return transcription
