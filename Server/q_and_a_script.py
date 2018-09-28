"""
    run this file to create and implmenet a new question /
    answer pair. enter the following details to create a 
    complete pair:
        - question body
        - answer body (should be a function ideally)
        - question keywords (at least one) 
"""
import sys
import ast

import django
django.setup()

from model.file_processor import FileProcessor
from questions.models import Question
from answers.models import Answer

HELP_STRING = ("run this file to create and implmenet a new question" +
               "answer pair.\n enter the following details to create a" + 
               "complete pair:\n" +
               "    - question body\n" +
               "    - answer body (should be a function ideally)\n" +
               "     - question keywords (at least one)\n")

ORG_TRAIN_SET = FileProcessor.read_file('machine_learning/data/value_set.jenk')
ORG_IN_SET = FileProcessor.read_file('machine_learning/data/output_set.jenk')
ORG_KEY_SET = ast.literal_eval(FileProcessor.read_file('./key_words/keywords.jenk'))
ORG_Q_LIST = FileProcessor.read_file('db/question_list.jenk').split('|')
ORG_Q_LIST = map(lambda w: ast.literal_eval(w), ORG_Q_LIST)
ORG_A_LIST = FileProcessor.read_file('db/answer_list.jenk').split('|')
ORG_A_LIST = map(lambda w: ast.literal_eval(w), ORG_A_LIST)

def revert_data_to_reset():
    FileProcessor.write_file('key_words/keywords.jenk', str(ORG_KEY_SET), 'w')
    FileProcessor.write_file('machine_learning/data/value_set.jenk', str(ORG_TRAIN_SET), 'w')
    FileProcessor.write_file('machine_learning/data/output_set.jenk', str(ORG_IN_SET), 'w')
    FileProcessor.write_file('db/question_list.jenk', str(ORG_Q_LIST), 'w')
    FileProcessor.write_file('db/answer_list.jenk', str(ORG_A_LIST), 'w')

def write_keyword_data(q_keyword, q_address):
    key_arr = q_keyword.split(" ")
    key_arr = map(lambda w: w.replace('_', ' '), key_arr)
    new_keywords = ORG_KEY_SET
    try:
        for word in key_arr:
            new_keywords[word] = q_address
    except Exception, e:  
        raise e
    finally:
        FileProcessor.write_file('key_words/keywords.jenk', str(keywords), 'w')

def add_new_data_to_db_files(q_new, a_new):
    q_new_list = ORG_Q_LIST
    a_new_list = ORG_A_LIST
    q_new_list.append({'body': q_new.body, 'address': q_new.address})
    a_new_list.append({'body': a_new.body, 'address': a_new.address})
    FileProcessor.write_file('db/question_list.jenk', "|".join(str(x) for x in q_new_list), 'w')
    FileProcessor.write_file('db/answer_list.jenk', "|".join(str(x) for x in a_new_list), 'w')

def add_to_training_set(q_address, a_address):
    training_set = ORG_TRAIN_SET.split(",")
    input_set = ORG_IN_SET.split(",")
    training_set.append(float(q_address))
    input_set.append(float(a_address))
    input_set = ",".join(str(x) for x in input_set)
    training_set = ",".join(str(x) for x in training_set)
    FileProcessor.write_file('machine_learning/data/value_set.jenk', str(training_set), 'w')
    FileProcessor.write_file('machine_learning/data/output_set.jenk', str(input_set), 'w')

def q_and_a_creation(q_body, a_body):
    length = len(Question.objects.all())
    q_new = Question(body=q_body, address=(length + 1))
    a_new = Answer(body=a_body, address=(length + 1))
    add_new_data_to_db_files(q_new, a_new)
    q_new.save()
    a_new.save()
    return [q_new.address, a_new.address]



print("This is the runner for adding questions and answers to the application\n" +
      "Please read the included instructions for more infomation, this can be done"+
      "by entering HELP! at any time, press QQQ to close the script at any time\n"+
      "Enter a question to begin:")

while True:
    try:
        command = sys.stdin.readline().rstrip()
        if command == "QQQ":
            break
        elif command == "HELP!":
            print(HELP_STRING)
            next

        q_body = command
        print("Now enter an answer please:")
        command = sys.stdin.readline().rstrip()
        a_body = command
        print("now enter your keywords:")
        command = sys.stdin.readline().rstrip()
        keywords = command

        if q_body == "" or a_body == "" or keywords == "":
            raise Exception("you must enter all three fields to continue")
        
        address_pair = q_and_a_creation(q_body, a_body)
        write_keyword_data(keywords, address_pair[0])
        add_to_training_set(address_pair[0], address_pair[1])
        print("saved sucessfully")
        break

    except Exception, e:
        print("an error occured, resetting files..")
        revert_data_to_reset()
        print("your error message is:")
        raise e
