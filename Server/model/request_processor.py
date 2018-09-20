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
                question = question_class.objects.get(body=request['body'])
                return True, question.address
            except Exception, e:
                print(str(e))
                return False

    @staticmethod
    def process_request(question_address):
        print(question_address)
        return 0

    @staticmethod
    def get_answer(answer_address, answer_class):
        answer = answer_class.objects.get(address = answer_address)

        return answer
