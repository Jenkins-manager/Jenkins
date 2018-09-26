"""
    Question analysis testing file
"""
import pytest
from ..model.question_analysis import QuestionAnalysis

class TestCLass(object):

    def test_question_destroy_can_break_quewtion_into_words(self):
        assert QuestionAnalysis.question_destroy('what is your name') == ['what', 'is', 'your', 'name']