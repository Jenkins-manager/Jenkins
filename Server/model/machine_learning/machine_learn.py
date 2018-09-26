"""
    Machine Learning class
"""
import numpy
import threading
import tensorflow as tf
from tensorflow import keras

from model.machine_learning.training_model import TrainingModel
from model.file_processor import FileProcessor
# import matplotlib.pyplot as plt

tf.enable_eager_execution()


class MachineLearn(threading.Thread):

    VALUES_MIN = 1 # always 1
    VALUES_MAX = 4 # get all answers then see length of array

    def __init__(self, question):
        threading.Thread.__init__(self)
        self.question = question
        self.answer = None
        try:
            self.value_set = FileProcessor.read_file('./machine_learning/data/value_set.jenk').split(',')
            self.value_set = map(float, self.value_set)
            print(self.value_set)
        except Exception, e:
            raise e

    def run(self):
        print("starting training thread...")
        self.train_network()
        print(self.answer)
        print("completed training thread")

    def loss(self, predicted_y, desired_y):
        return tf.reduce_mean(tf.square(predicted_y - desired_y))

    def train(self, model, inputs, outputs, learning_rate):
        with tf.GradientTape() as t:
            current_loss = self.loss(model(inputs), outputs)

        dQ = t.gradient(current_loss, model.Q)
        model.Q.assign_sub(learning_rate * dQ)

    def train_network(self):
        index = self.value_set.index(self.question)
        tf.reset_default_graph()
        model = TrainingModel(self.value_set)
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
                self.answer = int(round(model.Q.numpy().tolist()[index]))
                return self.answer