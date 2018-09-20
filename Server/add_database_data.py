import django
django.setup()
from questions.models import Question

def set_questions():
    return [{'body': 'What time is it?', 'address': 1},
            {'body': "what is today's date?", 'address': 2},
            {'body': 'What is the weather?', 'address': 3},
            {'body': 'What is my name?', 'address': 4}]

def add_questions():
    for i in range(len(set_questions())):
        q1 = Question(
            body=set_questions()[i]['body'],
            address=set_questions()[i]['address']
            )
        q1.save()

add_questions()