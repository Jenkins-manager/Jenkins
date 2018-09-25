import django
django.setup()
from questions.models import Question
from answers.models import Answer

def set_questions():
    return [{'body': 'What time is it?', 'address': 1},
            {'body': "what is today's date?", 'address': 2},
            {'body': 'What is the weather?', 'address': 3},
            {'body': 'What is my name?', 'address': 4}]

def set_answers():
    return [{'body': 'AnswerProcessor.getName()', 'address': 1},
            {'body': 'AnswerProcessor.getWeather()', 'address': 2},
            {'body': "AnswerProcessor.getDate()", 'address': 3},
            {'body': "AnswerProcessor.getTime()", 'address': 4}]

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
    add_questions()
    add_answers()

add_data()