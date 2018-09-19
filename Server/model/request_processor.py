
class RequestProcessor:

    @staticmethod
    def check_request(request):
        if request['body'] != '' :
            return True
        else:
            return False