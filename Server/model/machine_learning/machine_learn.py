"""
    Machine Learning class
"""

import tensorflow as tf
from tensorflow import keras
import threading
from ...model.machine_learning.training_model import TrainingModel
import tensorflow as tf
import numpy
# import matplotlib.pyplot as plt

tf.enable_eager_execution()


class MachineLearn(threading.Thread):

    VALUES_MIN = 1 # always 1
    VALUES_MAX = 4 # get all answers then see length of array

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self, value_set, question):
        print("starting thread")
        return self.train_network(value_set, question)

    def loss(self, predicted_y, desired_y):
        return tf.reduce_mean(tf.square(predicted_y - desired_y))

    def normalize(self, address):
        return (address - MachineLearn.VALUES_MIN) / float(MachineLearn.VALUES_MAX - MachineLearn.VALUES_MIN)

    def de_normalize(self, normalized_address):
        return MachineLearn.VALUES_MIN + (normalized_address * (MachineLearn.VALUES_MAX - MachineLearn.VALUES_MIN))

    def train(self, model, inputs, outputs, learning_rate):
        with tf.GradientTape() as t:
            current_loss = self.loss(model(inputs), outputs)

        dQ = t.gradient(current_loss, model.Q)
        model.Q.assign_sub(learning_rate * dQ)

    def train_network(self, value_set, question):
        index = value_set.index(question)
        tf.reset_default_graph()
        model = TrainingModel(value_set)
        desired_list = [4.00, 3.00, 2.00, 1.00]
        num_examples = 10000
        num_epochs = 70
        inputs = tf.random_normal(shape=[num_examples])
        Qs = []
        epochs = range(num_epochs)
        for epoch in epochs:
            Qs.append(model.Q.numpy())
            current_loss = self.loss(model.Q, desired_list)
            self.train(model, inputs, desired_list, 0.1)
            with tf.GradientTape() as t:
                current_loss = self.loss(model(inputs), desired_list)
                dQ = t.gradient(current_loss, model.Q)
                model.Q.assign_sub(0.1 * dQ)
            if(epoch == num_epochs - 1):
                print("Exited thread")
                return int(round(model.Q.numpy().tolist()[index]))

    def get_output(self, question):
        try:
            return self.run([1.00, 2.00, 3.00, 4.00], question)
        except Exception, e:
            return "question not found"

    # run?
