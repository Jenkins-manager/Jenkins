"""
    Question analysis testing file
"""
import pytest
from ..model.question_analysis import QuestionAnalysis

class TestCLass(object):

    def test_question_destroy_can_break_question_into_words(self):
        assert QuestionAnalysis.question_destroy('what is your name') == ['what', 'your', 'name']

    def test_question_destroy_with_no_question(self):
        assert QuestionAnalysis.question_destroy('') == []

    def test_remove_non_keywords_removes_correctly(self):
        assert QuestionAnalysis.remove_non_keywords(['what, your, name']) == 'name'

    def test_remove_non_keywords_dosent_rmove_keyword(self):
        assert QuestionAnalysis.remove_non_keywords(['what is the current weather today like?']) == 'current weather'

    def test_non_keywords_list(self):
        assert QuestionAnalysis.non_keywords_list() == ['what', 'where', 'when',
                                                        'will', 'does', 'like', 'been']