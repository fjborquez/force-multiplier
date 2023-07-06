import base64


class StringUtils:
    @staticmethod
    def decode(string: str) -> str:
        return base64.b64decode(string).decode('utf-8')

    @staticmethod
    def remove_newlines(string: str) -> str:
        return string.replace('\n', '')
