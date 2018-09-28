"""
    Machine Learn testing class
"""

from ...model.machine_learning.machine_learn import MachineLearn
from ...model.file_processor import FileProcessor

class TestClass(object):

    question_address = 2
    machine_learn = MachineLearn(question_address)
    training_set = FileProcessor.read_file('./machine_learning/data/value_set.jenk').split(',')
    desired_set = FileProcessor.read_file('./machine_learning/data/output_set.jenk').split(',')
    training_set = map(float, training_set)
    desired_set = map(float, desired_set)

    def test_can_load_value_set(self):
        assert  TestClass.machine_learn.value_set == TestClass.training_set

    def test_can_load_desired_set(self):
        assert  TestClass.machine_learn.desired_list == TestClass.desired_set

    def test_train_network(self):
        assert TestClass.machine_learn.train_network() == 2

    def test_thread_start(self):
        TestClass.machine_learn.start()
        assert TestClass.machine_learn.answer == 2
