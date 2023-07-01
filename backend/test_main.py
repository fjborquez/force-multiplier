import asyncio
import unittest
from unittest.mock import patch

from fastapi import HTTPException
from openai.error import AuthenticationError
from starlette.responses import RedirectResponse

from backend.force_multiplier import InadequateFeedbackException
from backend.main import transcribe_audio, modify_document, DocumentFeedback, document, feedback, _decode


class TestMain(unittest.TestCase):
    def test_transcribe_audio_should_return_dictionary_with_feedback_key(self):
        with patch('backend.main.transcribe'):
            result = asyncio.run(transcribe_audio(None, ''))
            self.assertIn('feedback', result)

    def test_transcribe_audio_should_raise_an_authentication_error_exception(self):
        with patch('backend.main.transcribe', side_effect=AuthenticationError), self.assertRaises(HTTPException):
            asyncio.run(transcribe_audio(None, ''))

    def test_modified_document_should_return_modified_document(self):
        with patch('backend.main.apply_feedback'):
            document_feedback = DocumentFeedback(document='', document_is_code=True, feedback='')
            result = asyncio.run(modify_document(document_feedback, ''))
            self.assertIn('modified_document', result)

    def test_modified_document_should_raise_an_inadequate_feedback_exception(self):
        with patch('backend.main.apply_feedback', side_effect=InadequateFeedbackException('')), \
                self.assertRaises(HTTPException):
            document_feedback = DocumentFeedback(document='', document_is_code=True, feedback='')
            asyncio.run(modify_document(document_feedback, ''))

    def test_modified_document_should_raise_an_authentication_error_exception(self):
        with patch('backend.main.apply_feedback', side_effect=AuthenticationError), self.assertRaises(HTTPException):
            document_feedback = DocumentFeedback(document='', document_is_code=True, feedback='')
            asyncio.run(modify_document(document_feedback, ''))

    def test_document_should_return_a_redirect_response(self):
        result = asyncio.run(document())
        self.assertTrue(isinstance(result, RedirectResponse))

    def test_feedback_should_return_a_redirect_response(self):
        result = asyncio.run(feedback())
        self.assertTrue(isinstance(result, RedirectResponse))

    def test_decode_should_return_base64_decoded_string(self):
        to_compare = 'prueba'
        result = _decode('cHJ1ZWJh')
        self.assertEquals(to_compare, result)


if __name__ == '__main__':
    unittest.main()
