"""
    Question analysis testing file
"""
import pytest
from ..model.question_analysis import QuestionAnalysis

class TestClass(object):

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
        assert QuestionAnalysis.get_question_keywords().items() <= {'name': 1, 'weather': 2, 'date': 3, 'time': 4}.items()
                                                        
    def test_match_keyword_to_address_sucess(self):
        assert QuestionAnalysis.match_keyword_to_address(['your', 'name']) == 1

    def test_match_keywords_fail(self):
        assert QuestionAnalysis.match_keyword_to_address(['nonexistant']) == None

    def test_match_keywords_using_two_keywords(self):
        assert QuestionAnalysis.match_keyword_to_address(['name', 'date']) == 1
    
    def test_match_keywords_using_spaced_words(self):
        assert QuestionAnalysis.match_keyword_to_address(['my name']) == 5

    def test_compare_keyword_to_list(self):
        assert QuestionAnalysis.compare_keyword_to_list(['uwotmate', 'dates']) == 3
    
    def test_compare_keyword_to_list_should_fail(self):
        assert QuestionAnalysis.compare_keyword_to_list(['uwotmate', 'data']) == None
    
    def test_compare_keyword_to_list_using_two_similar_words(self):
        assert QuestionAnalysis.compare_keyword_to_list(['dates', 'names']) == 3

    def test_find_synonym(self):
        assert QuestionAnalysis.find_synonym(['title']) == 1

    def test_find_synonym_no_match(self):
        assert True

    def test_find_synonym_multiple_matches(self):
        assert True

    def test_add_word_to_keyword_list(self):
        new_data = QuestionAnalysis.add_word_to_keyword_list('title', 1, {'name': 1, 'weather': 2, 'date': 3, 'time': 4})
        assert new_data == {'date': 3, 'title': 1, 'weather': 2, 'name': 1, 'time': 4}

    # full cycle tests

    def test_process_user_question_using_known_keyword(self):
        assert QuestionAnalysis.process_user_question('tell me my name please?') == 1
    
    def test_process_user_question_using_similar_keyword(self):
        assert QuestionAnalysis.process_user_question('tell me my names please?') == 1

    def test_process_user_question_using_thesauras(self):
        assert True # QuestionAnalysis.process_user_question('tell me my names please?') == 1