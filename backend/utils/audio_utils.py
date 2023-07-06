import logging
import uuid

import ffmpeg
from fastapi import UploadFile

from .file_utils import FileUtils

class AudioUtils:
    @staticmethod
    def convert(source: UploadFile) -> str:
        initial_filepath = f"/tmp/{uuid.uuid4()}{source.filename}"
        converted_filepath = f"/tmp/ffmpeg-{uuid.uuid4()}{source.filename}"

        FileUtils.write(initial_filepath, source.file)

        logging.debug("running through ffmpeg")
        (
            ffmpeg
            .input(initial_filepath)
            .output(converted_filepath, loglevel="error")
            .run()
        )
        logging.debug("ffmpeg done")

        FileUtils.delete(initial_filepath)

        return converted_filepath
