class RequestProcessor:

    @staticmethod
    def check_request(request, question_class):
        if request['body'] != '' :
            q1 = question_class(body=request['body'])
            q1.save()
            return True
        else:
            return False