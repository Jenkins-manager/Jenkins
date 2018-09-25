import pytest
import django
django.setup()
from questions.models import Question
# from questions.serializers import QuestionSerializer
from answers.models import Answer
from ..model.request_processor import RequestProcessor

class TestClass(object):

    # def test_get_questions(self):
    #     assert RequestProcessor.get_questions(QuestionSerializer, Question).data[0]['body'] == 'What time is it?'

    # check_request tests

    # helper function for convert answer
    def add_one(i):
        return i + 1

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'What time is it?'}, Question)[0] == True 

    def test_check_request_returns_correct_address(self):
        assert RequestProcessor.check_request({'body': "what is today's date?"}, Question)[1] == 2 

    def test_check_request_throws_with_no_input(self):
        assert RequestProcessor.check_request({'body': ''}, Question) == False 

    def test_check_request_throws_with_invalid_question(self):
        assert RequestProcessor.check_request({'body': 'fake question'}, Question) == False 
    
    def test_get_answer(self):
        assert RequestProcessor.get_answer(1, Answer).body == 'getName()'

    def test_convert_answer(self):
        assert RequestProcessor.convert_answer("print(\"hello\")") == True
        # assert RequestProcessor.convert_answer() == True
   