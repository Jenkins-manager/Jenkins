"""
    Training Model class: holds the variables used by the machine_learn file
"""
import tensorflow as tf

tfe = tf.contrib.eager


class TrainingModel(object):

    def __init__(self, questions):
        self.questions = questions
        self.Q = tfe.Variable(questions)

    def __call__(self, inputs):
        return self.Q
