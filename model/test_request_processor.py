import pytest
from request_processor import RequestProcessor 

class TestClass(object):

    def test_check_request_throws_with_no_input(this):
        assert(RequestProcessor.check_request({'body': ''}), False)