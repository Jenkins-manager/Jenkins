"""
    Answer Processing class - calls a function then returns to request_processor
"""

import datetime

class AnswerProcessor:

    @staticmethod
    def getTime():
        print(datetime.datetime.now().time())
