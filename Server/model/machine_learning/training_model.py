"""
    Training Model class: holds the variables used by the machine_learn file
"""
import tensorflow as tf

tf_e = tf.contrib.eager


class TrainingModel(object):

    def __init__(self, questions):
        self.questions = questions
        self.Q = tf_e.Variable(questions)

    def __call__(self, inputs):
        return self.Q
