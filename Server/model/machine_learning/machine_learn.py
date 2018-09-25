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

rng = numpy.random


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
        learning_rate = 0.01
        training_epochs = 5000
        display_step = 50
        desired_list = [4.00, 6.00, 2.00, 1.00]
        model = TrainingModel(value_set)

        train_X = numpy.asarray(value_set)
        train_Y = numpy.asarray(desired_list)
        n_samples = train_X.shape[0]

        X = tf.placeholder("float")
        # Y = tf.placeholder("float")

        W = tf.Variable(rng.random(), name="weight")
        b = tf.Variable(rng.random(), name="bias")

        pred = tf.add(tf.multiply(X, W), b)

        cost = self.loss() #tf.reduce_sum(tf.pow(pred-X, 2))/(2*n_samples)

        optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

        init = tf.global_variables_initializer()

        with tf.Session() as sess:
            sess.run(init)
            for epoch in range(training_epochs):
                for x in train_X:
                    sess.run(optimizer, feed_dict={X: x})
                
                if(epoch+1) % display_step == 0:
                    c = sess.run(cost, feed_dict={X: train_X})
                    if (epoch+1) % display_step == 0:
                        c = sess.run(cost, feed_dict={X: train_X})
                        print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                            "W=", sess.run(W), "b=", sess.run(b))
        
            plt.plot(train_X, 'ro', label='Original data')
            plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
            plt.legend()
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