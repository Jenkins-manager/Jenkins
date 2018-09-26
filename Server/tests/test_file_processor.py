"""
    FileProessor testing class
"""

import pytest
from ..model.file_processor import FileProcessor

class TestClass(object):

    def test_make_file_path(self):
        assert 'Jenkins/Server/model/test_path' in FileProcessor.make_file_path('test_path')

    def test_read_file_test_file(self):
        assert FileProcessor.read_file('../tests/test_fileIO/read_file_test.txt') == 'Hello World!'

    def test_read_file_throws_when_invalid_file(self):
        try:
            FileProcessor.read_file('invalid_file_path')
            pytest.fail('no exception thrown')
        except Exception, e:
            assert 'No such file or directory' in str(e)

    def test_write_file_writes_test_file(self):
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'test content', 'w')
        result = FileProcessor.read_file('../tests/test_fileIO/write_to_file_test.txt')
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', '', 'w') # delete file contents
        assert result == 'test content'
    
    def test_write_file_throws_with_invalid_path(self):
        try:
            FileProcessor.write_file('invalid_path', 'will not save', 'w')
            pytest.fail('no exception thrown')
        except Exception, e:
            assert str(e) == 'file not found'

    def test_write_file_appends_text(self):
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'test content\n', 'w')
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', 'more test content', 'a')
        result = FileProcessor.read_file('../tests/test_fileIO/write_to_file_test.txt')
        FileProcessor.write_file('../tests/test_fileIO/write_to_file_test.txt', '', 'w') # delete file contents
        assert result == 'test content\nmore test content'

    def test_write_file_throws_with_invlaid_Action(self):
        try:
            FileProcessor.write_file('invalid_path', 'bad file type', 'Q')
            pytest.fail('no exception thrown')
        except Exception, e:
            assert str(e) == "mode string must begin with one of 'r', 'w', 'a' or 'U', not 'Q'"