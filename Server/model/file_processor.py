"""
    file i/o file, used to CRUD file input
"""
import os

class FileProcessor:

    def __init__(self):
        pass

    @staticmethod
    def make_file_path(file_path):
        current_dir = os.path.dirname(__file__)
        return os.path.join(current_dir, file_path)

    @staticmethod
    def read_file(file_path):
        save_file = open(FileProcessor.make_file_path(file_path), 'r')
        return save_file.read()

    @staticmethod
    def write_file(file_path, content, mode):
        save_file = open(FileProcessor.make_file_path(file_path), mode)
        save_file.write(content)
