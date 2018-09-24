"""
    Machine Learning class
"""
import tensorflow as tf
from tensorflow import keras

class MachineLearn:

    VALUES_MIN = 1 # always 1
    VALUES_MAX = 4 # get all answers then see length of array

    def __init__(self):
        print("created")
        
    def normalize(self, address):
        return (address - MachineLearn.VALUES_MIN) / float(MachineLearn.VALUES_MAX - MachineLearn.VALUES_MIN)
    
    def de_normalize(self, normalized_address):
        return MachineLearn.VALUES_MIN + (normalized_address * (MachineLearn.VALUES_MAX - MachineLearn.VALUES_MIN))
    
    def train_network(self, value_set):
        print("train!")

    def get_output(self, value_set):
        self.value_set = value_set
    
    # run?