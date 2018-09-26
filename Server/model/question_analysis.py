"""
    Question analysis class: breaks down user questions and 
    selects appropriate database item
"""

import ast

from file_processor import FileProcessor

class QuestionAnalysis():

    @staticmethod
    def question_destroy(question):
        q_arr = question.split()
        return map(lambda w: w.lower(), list(filter(lambda w : len(w) > 3, q_arr)))

    @staticmethod
    def non_keywords_list():
        return FileProcessor.read_file('./key_words/non_keywords.jenk').split(" ")

    @staticmethod
    def remove_non_keywords(q_arr):
        non_keywords = QuestionAnalysis.non_keywords_list()
        return filter(lambda w: w not in non_keywords, q_arr)

    @staticmethod
    def match_keyword_to_address(q_arr):
        keyword_list = QuestionAnalysis.get_question_keywords()
        matched_word =  ''.join(filter(lambda w: w in keyword_list.keys(), q_arr ))
        return None if matched_word == '' else keyword_list[matched_word]

    @staticmethod
    def get_question_keywords():
        return ast.literal_eval(FileProcessor.read_file('./key_words/keywords.jenk'))
    
    @staticmethod
    def process_user_question(question):
        processed_question = QuestionAnalysis.remove_non_keywords(QuestionAnalysis.question_destroy(question))