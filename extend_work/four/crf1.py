# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/28  10:01
# @abstract    :

import os

import tensorflow as tf

import pickle



import data_utils

import model_utils

from model import Model


import pandas as pd


flags = tf.app.flags





flags.DEFINE_string('ckpt_path', os.path.join('modelfile', 'ckpt'), '保存模型的位置')

flags.DEFINE_string('map_file', 'maps.pkl', '存放字典映射及标签映射')

flags.DEFINE_string('config_file', 'config_file', '配置文件')



FLAGS = tf.app.flags.FLAGS





def evaluate_line():

  config = model_utils.load_config(FLAGS.config_file)

  tf_config = tf.ConfigProto()

  tf_config.gpu_options.allow_growth = True

  with open(FLAGS.map_file,"rb") as f:

    word_to_id, id_to_word, tag_to_id, id_to_tag = pickle.load(f)

  with tf.Session(config = tf_config) as sess:

    model = model_utils.create(sess, Model, FLAGS.ckpt_path, config)

    df = pd.read_excel('1.xlsx')

    for line in df['文本']:

      result = model.evaluate_line(sess, data_utils.input_from_line(line, word_to_id), id_to_tag)

      print(result)





def main(_):

  evaluate_line()









if __name__ == "__main__":

  tf.app.run(main)