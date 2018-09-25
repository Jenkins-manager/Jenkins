"""
    Machine Learning class
"""
from __future__ import absolute_import, division, print_function

import os
import sys
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras

from ...model.machine_learning.training_model import TrainingModel
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt

tf.enable_eager_execution()


class MachineLearn:

    VALUES_MIN = 1 # always 1
    VALUES_MAX = 4 # get all answers then see length of array

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

    def train_network(self, value_set):     
        tf.reset_default_graph()
        model = TrainingModel(value_set)
        desired_list = [4.00, 3.00, 2.00, 1.00]
        num_examples = 10000
        tvars = []
        
        desired_ans = desired_list[0]
        inputs = tf.random_normal(shape=[num_examples])
        Qs = []
        epochs = range(150)
        init_op = tf.global_variables_initializer()
        for _ in epochs:     
            Qs.append(model.Q.numpy())
            current_loss = self.loss(model.Q, desired_list)
            self.train(model, inputs, desired_list, 0.1)
            with tf.GradientTape() as t:
                current_loss = self.loss(model(inputs), desired_list)
                dQ = t.gradient(current_loss, model.Q)
                model.Q.assign_sub(0.1 * dQ)
            with tf.Session() as sess: 
                #saver = tf.train.Saver(tvars, defer_build=False)
                tvars = tf.trainable_variables(scope=None)
                #save_path = saver.save(sess, "./model/machine_learning/trained.ckpt",  global_step=0)
            
        plt.plot(epochs, Qs, 'r')
        plt.plot([desired_list] * len(epochs), 'r--')
        plt.legend(['Q', 'true q'])     
        plt.show()
    def get_output(self, value_set):
        self.value_set = value_set
    
    # run?

    """
    tf.reset_default_graph()
        model = TrainingModel(value_set)
        
        num_examples = 10000
        tvars = []
        
        desired_ans = desired_list[0]
        inputs = tf.random_normal(shape=[num_examples])
        Qs = []
        epochs = range(150)
        init_op = tf.global_variables_initializer()
        for _ in epochs:     
            Qs.append(model.Q.numpy())
            current_loss = self.loss(model.Q, desired_list)
            self.train(model, inputs, desired_list, 0.1)
            with tf.GradientTape() as t:
                current_loss = self.loss(model(inputs), desired_list)
                dQ = t.gradient(current_loss, model.Q)
                model.Q.assign_sub(0.1 * dQ)
            with tf.Session() as sess: 
                saver = tf.train.Saver(tvars, defer_build=False)
                tvars = tf.trainable_variables(scope=None)
                save_path = saver.save(sess, "./model/machine_learning/trained.ckpt",  global_step=0)
            
        # plt.plot(epochs, Qs, 'r')
        # plt.plot([desired_list] * len(epochs), 'r--')
        # plt.legend(['Q', 'true q'])     
        # plt.show()

    """