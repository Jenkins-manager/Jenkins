"""
    feature tests for question and ansers
"""


from time import gmtime, strftime

import django
django.setup()

from answers.models import Answer
from ...model.request_processor import RequestProcessor

class TestClass(object):

    # question tests

    def test_question_can_be_received(self):
        # generic question -> our question
        assert True

    # answer tests

    def test_answer(self):
        assert RequestProcessor.get_answer(4, Answer) == ("The time is: " +
                                                          strftime("%H:%M:%S", gmtime()))

    # full cycle tests

    def test_receive_question_and_pick_answer(self):
        assert RequestProcessor.process_request(4, Answer) == ("The time is: " +
                                                               strftime("%H:%M:%S", gmtime()))

    def test_ask_question_get_stored_answer(self):
        assert RequestProcessor.process_request(1, Answer) == "Your name is Battletoads"
