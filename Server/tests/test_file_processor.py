"""
    FileProessor testing class
"""

import pytest
from ..model.file_processor import FileProcessor

class TestClass(object):

    def test_read_file_test_file(self):
        assert FileProcessor.read_from_file('../tests/test_fileIO/read_file_test.txt') == 'Hello World!'

    def test_read_file_throws_when_invalid_file(self):
        try:
            FileProcessor.read_from_file('invalid_file_path')
            fail('no exception thrown')
        except Exception, e:
            assert e == ''