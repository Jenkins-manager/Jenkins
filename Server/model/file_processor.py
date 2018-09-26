"""
    file i/o file, used to CRUD file input
"""
import os

class FileProcessor:

    @staticmethod
    def make_file_path(file_path):
        current_dir = os.path.dirname(__file__)
        return os.path.join(current_dir, file_path)

    @staticmethod
    def read_file(file_path):
        file = open(FileProcessor.make_file_path(file_path), 'r')
        return file.read()
    
    @staticmethod
    def write_file(file_path, content, mode):
        file = open(FileProcessor.make_file_path(file_path), mode)
        file.write(content)