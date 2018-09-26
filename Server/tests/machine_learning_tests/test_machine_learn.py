"""
    Machine Learn testing class
"""
import pytest
from ...model.machine_learning.machine_learn import MachineLearn
from ...model.file_processor import FileProcessor

class TestClass(object):

    question_address = 2
    machine_learn = MachineLearn(question_address)
    training_set = [1.00, 2.00, 3.00, 4.00]

    def test_can_load_value_set(self):
        assert TestClass.machine_learn.value_set == TestClass.training_set

    def test_train_network(self):
        assert TestClass.machine_learn.train_network() == 3

    def test_thread_start(self):
        TestClass.machine_learn.start()
        assert TestClass.machine_learn.answer == 3
