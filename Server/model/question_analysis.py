"""
    Question analysis class: breaks down user questions and 
    selects appropriate database item
"""

import ast

from difflib import SequenceMatcher
from thesaurus import Word

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
        matched_word =  list(filter(lambda w: w in keyword_list.keys(), q_arr ))
        return None if matched_word == [] else keyword_list[matched_word[0]]

    @staticmethod
    def get_question_keywords():
        return ast.literal_eval(FileProcessor.read_file('./key_words/keywords.jenk'))

    @staticmethod
    def compare_keyword_to_list(q_arr):
        keyword_list = QuestionAnalysis.get_question_keywords()
        for word in q_arr:
            for key in keyword_list.keys():
                if SequenceMatcher(None, word, key).ratio() > 0.8:
                    return keyword_list[key]

    @staticmethod
    def add_word_to_keyword_list(word, address, keywords):
        keywords[word] = address
        print(keywords)
        FileProcessor.write_file('./key_words/keywords.jenk', str(keywords), 'w')
        return keywords
    
    @staticmethod
    def find_synonym(q_arr):
        keyword_list = QuestionAnalysis.get_question_keywords()
        for word in q_arr:
            words = Word(word).synonyms()
            matches = list(filter(lambda w: w in keyword_list.keys(), words))
            if matches != []:
                QuestionAnalysis.add_word_to_keyword_list(word, keyword_list[matches[0]], keyword_list)
                return keyword_list[matches[0]]

    @staticmethod
    def process_user_question(question):
        # preparation stage
        processed_question = QuestionAnalysis.remove_non_keywords(QuestionAnalysis.question_destroy(question))
        keyword_list = QuestionAnalysis.get_question_keywords()
        
        # initial match
        match = QuestionAnalysis.match_keyword_to_address(processed_question)
        if match != None:
            return match
        
        # second stage
        match = QuestionAnalysis.compare_keyword_to_list(processed_question)
        if match != None:
            return match

        # third stage
        match = QuestionAnalysis.find_synonym(processed_question)
        if match != None:
            return match

        

        # third stage
