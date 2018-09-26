"""
    Request Processing class: processes Http request data
    and fetches results from machine-learn
"""
from time import gmtime, strftime
from .answer_processor import AnswerProcessor
from .machine_learning.machine_learn import MachineLearn
from question_analysis import QuestionAnalysis

class RequestProcessor:

    @staticmethod
    def get_questions(serializer, question_class):
        questions = question_class.objects.all()
        return serializer(questions, many=True)

    @staticmethod
    def check_request(request, question_class):
        if request['body'] == '' :
            return False
        else:
            try:
                question_address = QuestionAnalysis.process_user_question(request['body'])         
                if question_address != None:
                    return True, question_address
                else:
                    raise('Question not found')
            except Exception:
                return False

    @staticmethod
    def process_request(question_address, answer_class):
        machine_learn = MachineLearn()
        answer = machine_learn.get_output(question_address)
        return RequestProcessor.get_answer(answer, answer_class)

    @staticmethod
    def get_answer(answer_address, answer_class):
        try:
            answer = answer_class.objects.get(address = answer_address)
            return eval(answer.body)
        except Exception, e:
            raise e
