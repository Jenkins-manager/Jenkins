import pytest
from ..model.request_processor import RequestProcessor

class StubQuestion:

    def __init__(self, body):
        self.body = body

    def save(self):
        print('Saved')

class TestClass(object):

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'hello'}, StubQuestion) == True 

    def test_check_request_throws_with_no_input(self):
        assert RequestProcessor.check_request({'body': ''}, StubQuestion) == False 