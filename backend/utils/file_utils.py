import os
import shutil
from typing import BinaryIO


class FileUtils:
    @staticmethod
    def delete(filepath: str) -> None:
        os.remove(filepath)

    @staticmethod
    def write(path: str, file: BinaryIO) -> None:
        with open(path, "wb+") as file_object:
            shutil.copyfileobj(file, file_object)

    @staticmethod
    def open(path: str) -> BinaryIO:
        return open(path, "rb")
