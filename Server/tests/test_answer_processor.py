"""
    answer processor testing file
"""
import pytest
from ..model.answer_processor import AnswerProcessor
from time import gmtime, strftime

class TestClass(object):

    def test_getTime(self):
        assert AnswerProcessor.getTime() == "The time is: " + strftime("%H:%M:%S", gmtime())

    def test_getDate(self):
        assert AnswerProcessor.getDate() == "Todays date is: " + strftime("%Y-%m-%d", gmtime())

    def test_get_weather(self):
        assert "C" in AnswerProcessor.getWeather()
