import unittest
from unittest.mock import patch

from backend.prompts import get_system_prompt, get_user_prompt, get_openai_functions, _get_system_prompt_for_code, \
    _get_system_prompt_for_natural_language


class TestPrompts(unittest.TestCase):
    def test_get_system_prompt_should_return_get_system_prompt_for_code_when_is_code_is_true(self):
        is_code = True
        with patch('backend.prompts._get_system_prompt_for_code') as mock:
            get_system_prompt(is_code)
            mock.assert_called()

    def test_get_system_prompt_should_return_get_system_prompt_for_natural_language_when_is_code_is_false(self):
        is_code = False
        with patch('backend.prompts._get_system_prompt_for_natural_language') as mock:
            get_system_prompt(is_code)
            mock.assert_called()

    def test_get_user_prompt_should_return_prompt_when_is_code_is_true(self):
        needle = 'Here is the code and my feedback'
        is_code = True
        document, feedback = '', ''
        result = get_user_prompt(is_code, document, feedback)
        self.assertTrue(needle in result)

    def test_get_user_prompt_should_return_prompt_when_is_code_is_false(self):
        needle = 'Here is the document and my feedback'
        is_code = False
        document, feedback = '', ''
        result = get_user_prompt(is_code, document, feedback)
        self.assertTrue(needle in result)

    def test_get_openai_functions_should_return_json(self):
        result = get_openai_functions()
        length = 2
        self.assertEqual(length, len(result))

    def test_get_system_prompt_for_code_should_return_prompt_when_use_openai_functions_is_true(self):
        needle = 'You are an AI capable of editing code based on user feedback'
        with patch('backend.prompts.USE_OPENAI_FUNCTIONS', return_value=True):
            result = _get_system_prompt_for_code()
            self.assertTrue(needle in result)

    def test_get_system_prompt_for_code_should_return_prompt_when_use_openai_functions_is_false(self):
        needle = 'You are an AI capable of editing code based on user feedback'
        with patch('backend.prompts.USE_OPENAI_FUNCTIONS', return_value=False):
            result = _get_system_prompt_for_code()
            self.assertTrue(needle in result)

    def test_get_system_prompt_for_natural_language_should_return_prompt_when_use_openai_functions_is_true(self):
        needle = 'You will strictly call the apply_diff function with your response as arguments'
        with patch('backend.prompts.USE_OPENAI_FUNCTIONS', return_value=True):
            result = _get_system_prompt_for_natural_language()
            self.assertTrue(needle in result)

    def test_get_system_prompt_for_natural_language_should_return_prompt_when_use_openai_functions_is_false(self):
        needle = 'You will strictly return JSON conforming to the above spec'
        with patch('backend.prompts.USE_OPENAI_FUNCTIONS', False):
            result = _get_system_prompt_for_natural_language()
            self.assertTrue(needle in result)


if __name__ == '__main__':
    unittest.main()
