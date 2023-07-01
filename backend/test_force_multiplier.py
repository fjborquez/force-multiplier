import asyncio
import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from backend.force_multiplier import apply_feedback, get_diff, remove_newlines, get_completion, \
    InadequateFeedbackException, process_result, apply_diff


class MyTestCase(unittest.TestCase):
    def test_apply_feedback_should_return_modified_document(self):
        to_compare = ''
        with patch('backend.force_multiplier.get_diff'), patch('backend.force_multiplier.apply_diff', return_value=''):
            result = asyncio.run(apply_feedback('', True, '', ''))
            self.assertEquals(to_compare, result)


    def test_get_diff_should_return_simplenamespace(self):
        with patch('backend.force_multiplier.get_completion', return_value='{}'):
            result = asyncio.run(get_diff('{}', True, '', ''))
            self.assertTrue(isinstance(result, SimpleNamespace))
    def test_remove_new_lines(self):
        text = 'test\n'
        result = remove_newlines(text)
        self.assertEquals('test', result)

    def test_get_completion_should_return_process_result(self):
        pass

    def test_get_completion_should_raise_inadequate_feedback_exception(self):
        with patch('backend.force_multiplier.openai.ChatCompletion.acreate'), \
                patch('backend.force_multiplier.USE_OPENAI_FUNCTIONS', return_value=True), \
                patch('backend.force_multiplier.process_result', side_effect=InadequateFeedbackException('')), \
                self.assertRaises(InadequateFeedbackException):
            asyncio.run(get_completion('', ''))

    def test_process_result_should_return_message_content_when_not_use_openai_functions(self):
        pass

    def test_process_result_should_raise_inadequate_feedback_exception_when_finish_reason_is_not_function_call(self):
        pass

    def test_process_result_should_raise_inadequate_feedback_exception_when_function_call_name_is_not_apply_diff(self):
        pass

    def test_process_result_should_return_function_call_argumentst(self):
        pass

    def test_apply_diff_should_return_document(self):
        pass


if __name__ == '__main__':
    unittest.main()
