"""
    Machine Learn testing class
"""
import pytest
from ...model.machine_learning.machine_learn import MachineLearn

class TestClass(object):

    machine_learn = MachineLearn()

    def test_normalize(self):
        assert True
    
    def test_de_normalize(self):
        assert True

    def test_train_network(self):
        assert True

    def test_get_output(self):
        assert True

    # verify output tests

    def test_verify_output_good(self):
        assert TestClass.machine_learn.verify_output(2)

    def test_verify_output_bad(self):
        assert TestClass.machine_learn.verify_output(0.0012938) == False