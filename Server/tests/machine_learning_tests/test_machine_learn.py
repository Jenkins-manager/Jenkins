"""
    Machine Learn testing class
"""
import pytest
from ...model.machine_learning.machine_learn import MachineLearn

class TestClass(object):

    machine_learn = MachineLearn()
    question_address = 2
    normalized_question = machine_learn.normalize(question_address)

    def test_normalize(self):
        assert(0 < TestClass.machine_learn.normalize(TestClass.question_address) < 1)
    
    def test_de_normalize(self):
        assert TestClass.machine_learn.de_normalize(TestClass.normalized_question) == TestClass.question_address

    def test_train_network(self):
        assert TestClass.machine_learn.train_network([1.00, 2.00, 3.00, 4.00], 2) == 3

    def test_get_output(self):
        assert TestClass.machine_learn.get_output(TestClass.question_address) == 3
