import pytest
import django
django.setup()
from questions.models import Question
from ..model.request_processor import RequestProcessor

class TestClass(object):

    # check_request tests

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'What time is it?'}, Question)[0] == True 

    def test_check_request_returns_correct_address(self):
        assert RequestProcessor.check_request({'body': "what is today's date?"}, Question)[1] == 2 

    def test_check_request_throws_with_no_input(self):
        assert RequestProcessor.check_request({'body': ''}, Question) == False 

    def test_check_request_throws_with_invalid_question(self):
        assert RequestProcessor.check_request({'body': 'fake question'}, Question) == False 