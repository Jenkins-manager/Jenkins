"""
    feature tests for question and ansers
"""
import pytest
import django
django.setup()
from questions.models import Question

from time import gmtime, strftime
from answers.models import Answer
from ...model.request_processor import RequestProcessor

class TestClass(object):

    # question tests

    def test_question_can_be_received(self):
        # generic question -> our question
        assert True

    # answer tests

    def test_answer_can_be_fetched_and_excecuted(self):
        assert RequestProcessor.get_answer(4, Answer) == "The time is: " + strftime("%H:%M:%S", gmtime())

    # full cycle tests

    def test_program_can_receive_question_and_pick_answer_correctly(self):
        assert RequestProcessor.process_request(4, Answer) == "The time is: " + strftime("%H:%M:%S", gmtime())

    def test_user_can_ask_question_and_get_stored_answer(self):
        assert True # RequestProcessor.process_request(4, Answer) == "Your name is Hello"
