"""
    Question analysis testing file
"""
import pytest
from ..model.question_analysis import QuestionAnalysis

class TestCLass(object):

    def test_question_destroy_can_break_question_into_words(self):
        assert QuestionAnalysis.question_destroy('what is your name') == ['what', 'your', 'name']

    def test_question_destroy_makes_all_lowercase(self):
        assert QuestionAnalysis.question_destroy('What Is your Name') == ['what', 'your', 'name']
    
    def test_question_destroy_with_no_question(self):
        assert QuestionAnalysis.question_destroy('') == []

    def test_remove_non_keywords_removes_correctly(self):
        assert QuestionAnalysis.remove_non_keywords(['what', 'your', 'name']) == ['your', 'name']

    def test_remove_non_keywords_dosent_remove_keyword(self):
        assert QuestionAnalysis.remove_non_keywords(['what', 'current', 'weather', 'today', 'like']) == ['current', 'weather', 'today']

    def test_non_keywords_list(self):
        assert QuestionAnalysis.non_keywords_list() == ['what', 'where', 'when',
                                                        'will', 'does', 'like', 'been']

    def test_get_question_keywords_contains_starting_words(self):
        assert QuestionAnalysis.get_question_keywords().items() >= {'name': 1, 'weather': 2, 'date': 3, 'time': 4}.items()
                                                        
    def test_match_keyword_to_address_sucess(self):
        assert QuestionAnalysis.match_keyword_to_address(['your', 'name']) == 1

    def test_match_keywords_fail(self):
        assert QuestionAnalysis.match_keyword_to_address(['nonexistant']) == None