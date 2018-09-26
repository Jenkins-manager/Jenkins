"""
    request processor test file
"""

import pytest
import django
django.setup()
from questions.models import Question
from time import gmtime, strftime
from answers.models import Answer
from ..model.request_processor import RequestProcessor

class TestClass(object):

    # def test_get_questions(self):
    #     assert RequestProcessor.get_questions(QuestionSerializer, Question).data[0]['body'] == 'What time is it?'

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'What time is it?'}, Question)[0] == True

    def test_check_request_returns_correct_address(self):
        assert RequestProcessor.check_request({'body': "what is today's date?"}, Question)[1] == 2

    def test_check_request_throws_with_no_input(self):
        assert RequestProcessor.check_request({'body': ''}, Question) == False

    def test_check_request_throws_with_invalid_question(self):
        assert RequestProcessor.check_request({'body': 'fake question'}, Question) == False

    def test_get_answer(self):
        assert RequestProcessor.get_answer(4, Answer) == "The time is: " + strftime("%H:%M:%S", gmtime())

    # exception throwing tests

    def test_process_request_bad_question_address(self):
        try:
            RequestProcessor.process_request(-1, Answer)
            pytest.fail("no excetion thrown")
        except Exception, e:
            assert True

    def test_get_answer_invalid_answer(self):
        try:
            RequestProcessor.get_answer(400, Answer)
            pytest.fail("no exception thrown")
        except Exception, e:
            assert str(e) == 'Answer matching query does not exist.'
