"""
    Machine Learn testing class
"""
import pytest
from ...model.machine_learning.machine_learn import MachineLearn

class TestClass(object):

    question_address = 2
    machine_learn = MachineLearn(question_address)

    def test_train_network(self):
        assert TestClass.machine_learn.train_network() == 3

    def test_thread_start(self):
        TestClass.machine_learn.start()
        assert TestClass.machine_learn.answer == 3
