"""
    answer processor testing file
"""
import pytest
from ..model.answer_processor import AnswerProcessor
from time import gmtime, strftime

class TestClass(object):

    def test_getTime(self):
        assert AnswerProcessor.getTime() == strftime("%H:%M:%S", gmtime())

    def test_getDate(self):
        assert AnswerProcessor.getDate() == strftime("%Y-%m-%d", gmtime())
