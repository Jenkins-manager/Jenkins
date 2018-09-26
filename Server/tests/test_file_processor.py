"""
    FileProessor testing class
"""

import pytest
from ..model.file_processor import FileProcessor

class TestClass(object):

    def test_read_file_test_file(self):
        assert FileProcessor.read_file('../tests/test_fileIO/read_file_test.txt') == 'Hello World!'

    def test_read_file_throws_when_invalid_file(self):
        try:
            FileProcessor.read_file('invalid_file_path')
            pytest.fail('no exception thrown')
        except Exception, e:
            assert str(e) == 'file not found'

    def test_write_file_writes_test_file(self):
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'test content')
        result = FileProcessor.read_file('../tests/test_fileIO/write_to_file_test.txt') == 'test content!'
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', '') # delete file contents
        assert result == 'test_content'
    
    def test_write_file_throws_with_invalid_path(self):
        try:
            FileProcessor.write_file('invalid_path', 'will not save')
            pytest.fail('no exception thrown')
        except Exception, e:
            assert str(e) == 'file not found'

    def test_write_file_appends_text(self):
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'test content')
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'more test content')
        result = FileProcessor.read_file('../tests/test_fileIO/write_to_file_test.txt') == 'test content!'
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', '') # delete file contents