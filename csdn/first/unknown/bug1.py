# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/30  19:22
# @abstract    :

# coding=utf-8

import numpy as np

from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt

# from keras.utils.visualize_util import plot

import DNN


def select_input_datasets(data, y, x, step):
	inputs = data[x].values.tolist()

	new_input_sets = []

	for i in range(len(inputs)):

		x = []  # 2D

		for j in range(step - 1, -1, -1):

			if (i - j) < 0:

				x.append([0] * len(inputs[0]))

			else:

				x.append(inputs[i - j])

		new_input_sets.append(x)

	# print np.array(new_input_sets).shape

	return {'y': np.array(data[y].values), 'x': np.array(new_input_sets)}


def read_data(train_file_name):
	print("The train data is loading")

	return read_csv(train_file_name)


def training(train_data_name=None, time_step=None, x_variables=None, target=None,

			 dim_hidden_layer=None, lr=None, loss=None, batch_size=None, nb_epoch=None, validation_split=None,

			 best_model_weight_name=None, last_model_weight_name=None):
	original_train_data = read_data(train_data_name)

	train_input = select_input_datasets(original_train_data,

										y=target,

										x=x_variables,

										step=time_step)

	DNN_model = DNN.DNN(train_input)

	# build a DNN model

	DNN_model.build_model(dim_hidden_layer=dim_hidden_layer, lr=lr, loss=loss)

	DNN_model.shows_model()

	# fit the model according to training data

	DNN_model.fit_model(batch_size=batch_size, nb_epoch=nb_epoch, validation_split=validation_split, best_model_weight_name=best_model_weight_name)

	DNN_model.save_model_to_file(last_model_weight_name)

	DNN_model.predict(train_input, show=True)

	DNN_model.evaluate(train_input)

	return DNN_model


def testing(test_data_name=None, time_step=None, x_variables=None, target=None,

			restore_model_weight_name=None):
	original_test_data = read_data(test_data_name)

	testing_input = select_input_datasets(original_test_data,

										  y=target,

										  x=x_variables,

										  step=time_step)

	testing_input['x'] = testing_input['x'][0:]

	testing_input['y'] = testing_input['y'][0:]

	DNN_model = DNN.DNN(testing_input)

	DNN_model.restore_model_from_file(restore_model_weight_name)

	DNN_model.predict(testing_input, show=True)

	DNN_model.evaluate(testing_input)

	return DNN_model


if __name__ == "__main__":

	# **************************************************

	# training or testing

	only_test = False

	a = '0'

	# 'Best_model.weights' or 'last_model'

	restore_model_weight_name = 'C:\\Users\\Iron\\Desktop\\0\\best_model.weights'

	# data

	train_data_name = 'C:\\Users\\Iron\\Desktop\\0\\train_data.csv'

	test_data_name = 'C:\\Users\\Iron\\Desktop\\0\\test_data.csv'

	target = 'w'

	x_variables = [

		"a1", "a2", "a3", "a4",

		"a6", "a6", "a7", "a8",

		"a9", "a10"

	]

	# model param

	time_step = 2

	dim_hidden_layer = 64

	lr = 0.001

	loss = 'mape'

	# fit param

	batch_size = 2

	nb_epoch = 15000

	validation_split = 0.05

	# save

	best_model_weight_name = 'C:\\Users\\Iron\\Desktop\\0\\best_model.weights'

	last_model_weight_name = 'C:\\Users\\Iron\\Desktop\\0\\last_model.weights'

	# **************************************************

	if not only_test:
		model = training(train_data_name=train_data_name,

						 time_step=time_step,

						 x_variables=x_variables, target=target,

						 dim_hidden_layer=dim_hidden_layer, lr=lr, loss=loss,

						 batch_size=batch_size, nb_epoch=nb_epoch, validation_split=validation_split,

						 best_model_weight_name=best_model_weight_name,

						 last_model_weight_name=last_model_weight_name)

	if only_test:
		model = testing(test_data_name=test_data_name,

						time_step=time_step,

						x_variables=x_variables, target=target,

						restore_model_weight_name=restore_model_weight_name, )