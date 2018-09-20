"""
    Answer Processing class - calls a function then returns to request_processor
"""

from time import gmtime, strftime

class AnswerProcessor:

    @staticmethod
    def getTime():
        return strftime("%H:%M:%S", gmtime())

    @staticmethod
    def getName():
        return 0

    @staticmethod
    def getDate():
        return strftime("%Y-%m-%d", gmtime())

    @staticmethod
    def getWeather():
        return 0
