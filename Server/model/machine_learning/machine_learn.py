"""
    Machine Learning class
"""
import threading
import tensorflow as tf

from model.machine_learning.training_model import TrainingModel
from model.file_processor import FileProcessor

tf.enable_eager_execution()

class MachineLearn(threading.Thread):

    def __init__(self, question):
        threading.Thread.__init__(self)
        self.question = question
        self.answer = None
        try:
            self.value_set = FileProcessor.read_file('./machine_learning/data/value_set.jenk').split(',')
            self.value_set = map(float, self.value_set)
            self.desired_list = FileProcessor.read_file('./machine_learning/data/output_set.jenk').split(',')
            self.desired_list = map(float, self.desired_list)
        except Exception, e:
            raise e

    def run(self):
        print("starting training thread...")
        self.train_network()
        print("completed training thread")

    def loss(self, predicted_y, desired_y):
        return tf.reduce_mean(tf.square(predicted_y - desired_y))

    def train(self, model, inputs, outputs, learning_rate):
        with tf.GradientTape() as t_grad:
            current_loss = self.loss(model(inputs), outputs)

        d_q = t_grad.gradient(current_loss, model.Q)
        model.Q.assign_sub(learning_rate * d_q)

    def train_network(self):
        index = self.value_set.index(self.question)
        tf.reset_default_graph()
        model = TrainingModel(self.value_set)
        desired_list = self.desired_list
        num_examples = 10000
        num_epochs = 70
        inputs = tf.random_normal(shape=[num_examples])
        q_s = []
        epochs = range(num_epochs)
        for epoch in epochs:
            q_s.append(model.Q.numpy())
            current_loss = self.loss(model.Q, desired_list)
            self.train(model, inputs, desired_list, 0.1)
            with tf.GradientTape() as t_grad:
                current_loss = self.loss(model(inputs), desired_list)
                d_q = t_grad.gradient(current_loss, model.Q)
                model.Q.assign_sub(0.1 * d_q)
            if epoch == num_epochs - 1:
                self.answer = int(round(model.Q.numpy().tolist()[index]))
                return self.answer