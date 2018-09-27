"""
    run this file to create and implmenet a new question /
    answer pair. enter the following details to create a 
    complete pair:
        - question body
        - answer body (should be a function ideally)
        - question keywords (at least one) 
"""

from model.file_processor import FileProcessor
from questions.models import Question
from answers.models import Answer

def write_keyword_data(q_keyword, q_address):
    keywords = FileProcessor.read_file('./model/key_words/keywords.jenk')
    keywords[q_keyword] = q_address
    FileProcessor.write_file('./model/key_words/keywords.jenk', str(keywords) ,'w')

def add_to_training_set(q_address, a_address):
    training_set = FileProcessor.read_file('./model/machine_learning/data/value_set.jenk')
    input_set = FileProcessor.read_file('./model/machine_learning/data/input_set.jenk')
    training_set.append(q_address)
    input_set.append(a_address)
    FileProcessor.write_file('./model/key_words/machine_learning/data/value_set.jenk', str(keywords) ,'w')
    FileProcessor.write_file('./model/key_words/machine_learning/data/input_set.jenk', str(keywords) ,'w')

def __main__(q_body, a_body, keywords):
    address_pair = 0
    q_new = Question(q_body)
    a_new = Answer(a_body)