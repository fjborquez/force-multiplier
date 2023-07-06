import unittest

from backend.utils import StringUtils


class TestStringUtils(unittest.TestCase):
    def test_decode_should_return_base64_decoded_string(self):
        to_compare = 'prueba'
        result = StringUtils.decode('cHJ1ZWJh')
        self.assertEquals(to_compare, result)

    def test_remove_new_lines(self):
        text = 'test\n'
        result = StringUtils.remove_newlines(text)
        self.assertEquals('test', result)


if __name__ == '__main__':
    unittest.main()
