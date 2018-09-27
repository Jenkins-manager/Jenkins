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

help_string = ("run this file to create and implmenet a new question" +
               "answer pair.\n enter the following details to create a" + 
               "complete pair:\n" +
               "    - question body\n" +
               "    - answer body (should be a function ideally)\n" +
               "     - question keywords (at least one)\n")

org_train_set = FileProcessor.read_file('machine_learning/data/value_set.jenk')
org_in_set = FileProcessor.read_file('machine_learning/data/output_set.jenk')
org_key_set = ast.literal_eval(FileProcessor.read_file('./key_words/keywords.jenk'))
org_q_list = FileProcessor.read_file('db/question_list.jenk').split('|')
org_q_list = map(lambda w: ast.literal_eval(w), org_q_list)
org_a_list = FileProcessor.read_file('db/answer_list.jenk').split('|')
org_a_list = map(lambda w: ast.literal_eval(w), org_a_list)

def revert_data_to_reset():
    FileProcessor.write_file('key_words/keywords.jenk', str(org_key_set) ,'w')
    FileProcessor.write_file('machine_learning/data/value_set.jenk', str(org_train_set) ,'w')
    FileProcessor.write_file('machine_learning/data/output_set.jenk', str(org_in_set) ,'w')
    FileProcessor.write_file('db/question_list.jenk', str(org_q_list), 'w')
    FileProcessor.write_file('db/answer_list.jenk', str(org_a_list), 'w')

def write_keyword_data(q_keyword, q_address):
    key_arr = q_keyword.split(" ")
    keywords = org_key_set
    try:
        for word in key_arr:
            keywords[word] = q_address
    except Exception, e:  
        print(str(e))
    finally:
        FileProcessor.write_file('key_words/keywords.jenk', str(keywords) ,'w')

def add_new_data_to_db_files(q_new, a_new):
    q_new_list = org_q_list
    a_new_list = org_a_list
    q_new_list.append({'body': q_new.body, 'address': q_new.address})
    a_new_list.append({'body': a_new.body, 'address': a_new.address})
    FileProcessor.write_file('db/question_list.jenk', "|".join(str(x) for x in q_new_list), 'w')
    FileProcessor.write_file('db/answer_list.jenk', "|".join(str(x) for x in a_new_list), 'w')

def add_to_training_set(q_address, a_address):
    training_set = org_train_set.split(",")
    input_set = org_in_set.split(",")
    training_set.append(float(q_address))
    input_set.append(float(a_address))
    input_set = ",".join(str(x) for x in input_set)
    training_set = ",".join(str(x) for x in training_set)
    FileProcessor.write_file('machine_learning/data/value_set.jenk', str(training_set) ,'w')
    FileProcessor.write_file('machine_learning/data/output_set.jenk', str(input_set) ,'w')

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
            print(help_string)
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
