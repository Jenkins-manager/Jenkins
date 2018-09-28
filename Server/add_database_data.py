import ast
import logging
logging.basicConfig()

import django
django.setup()
from questions.models import Question
from answers.models import Answer
from users.models import User

from model.file_processor import FileProcessor

def set_questions():
    q_arr =  FileProcessor.read_file('db/question_list.jenk').split('|')
    return map(lambda w: ast.literal_eval(w), q_arr)

def set_answers():
    a_arr =  FileProcessor.read_file('db/answer_list.jenk').split('|')
    return map(lambda w: ast.literal_eval(w), a_arr)

def set_usernames():
    return [{'username': 'Battletoads'}]

def add_usernames():
    for i in range(len(set_usernames())):
        u1 = User(
            username=set_usernames()[i]['username']
            )
        u1.save()

def add_questions():
    for i in range(len(set_questions())):
        q1 = Question(
            body=set_questions()[i]['body'],
            address=set_questions()[i]['address']
            )
        q1.save()


def add_answers():
    for i in range(len(set_answers())):
        a1 = Answer(
            body=set_answers()[i]['body'],
            address=set_answers()[i]['address']
            )
        a1.save()

def add_data():
    logger = logging.getLogger('databaselogger')
    # try:
    if len(Question.objects.all()) != 0 or len(Answer.objects.all()) != 0:
        logger.warning('non empty database, clearing data...')
        Question.objects.all().delete()
        Answer.objects.all().delete()
    add_questions()
    add_answers()
    add_usernames()
    # except Exception, e:
    #     raise e


add_data()
