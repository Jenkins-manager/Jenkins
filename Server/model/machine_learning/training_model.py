"""
    Training Model class: holds the variables used by the machine_learn file
"""
import tensorflow as tf

tfe = tf.contrib.eager
tf.enable_eager_execution()

class TrainingModel(object):

    def __init__(self, questions):
        self.questions = questions
        self.Q = tfe.Variable(questions)
    
    def __call__(self, inputs):
        return self.Q
