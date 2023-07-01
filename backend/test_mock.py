import unittest

from backend.mock import get_mock_completion


class TestMock(unittest.TestCase):
    def test_get_mock_completion_should_return_diff(self):
        result = get_mock_completion('a word')
        self.assertIn('diff', result)

    def test_get_mock_completion_should_return_none_when_words_length_is_0(self):
        result = get_mock_completion('')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
