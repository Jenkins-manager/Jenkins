import pytest
from Server.model.request_processor import RequestProcessor
class TestClass(object):

    def test_check_request_no_throw_with_vaid_input(self):
        assert RequestProcessor.check_request({'body': 'hello'}) == True 

    def test_check_request_throws_with_no_input(self):
        assert RequestProcessor.check_request({'body': ''}) == False 