class RequestProcessor:

    @staticmethod
    def check_request(request, question_class):
        if request['body'] == '' :
            # q1 = question_class(body=request['body'])
            # q1.save()
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
    def send_answer():
        return 0