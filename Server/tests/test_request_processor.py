"""
    request processor test file
"""
from time import gmtime, strftime

import pytest
import django
django.setup()

from answers.models import Answer
from ..model.request_processor import RequestProcessor

class TestClass(object):

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'What time is it?'})[0]

    def test_check_request_returns_correct_address(self):
        assert RequestProcessor.check_request({'body': "what is the weather like my good friend Jenkins"})[1] == 2

    def test_check_request_throws_with_no_input(self):
        assert not RequestProcessor.check_request({'body': ''})

    def test_check_request_throws_with_invalid_question(self):
        assert not RequestProcessor.check_request({'body': 'fake question'})

    def test_get_answer(self):
        assert RequestProcessor.get_answer(4, Answer) == "The time is: " + strftime("%H:%M:%S", gmtime())

    # exception throwing tests

    def test_process_request_bad_q_address(self):
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
