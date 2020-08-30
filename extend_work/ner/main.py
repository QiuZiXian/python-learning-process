#!/usr/bin/python
# -*- coding: UTF-8 -*-
#微信公众号 AI壹号堂 欢迎关注
#Author bruce

# 系统
import os
import tensorflow as tf
import pickle
import pandas as pd

# 自定义
import data_utils
import model_utils
from model import Model



flags = tf.app.flags




flags.DEFINE_string('ckpt_path', os.path.join('modelfile', 'ckpt'), '保存模型的位置')

flags.DEFINE_string('map_file', 'maps.pkl', '存放字典映射及标签映射')

flags.DEFINE_string('config_file', 'config_file', '配置文件')
flags.DEFINE_string('result_path', 'result', '结果路径')

FLAGS = tf.app.flags.FLAGS

local_file = 'D:/d/csdn/111.xlsx' # 输入文件
result_file = '222.xlsx'        # 输出 文件
types_num = 20  # type 个数
types_index = ['DIS', 'DRUG', 'OP', 'MAG', 'SIGN'] # 分类 类别


def handle(data):
    types_total = {types: [] for types in types_index}
    for item in data['entities']:
        if item['type'] in types_index:
            types_total[item['type']].append(item['word'])

    for k, v in types_total.items():
        if len(v) < types_num:
            v.extend([''] * (types_num - len(v)))
    out = []
    for k, v in types_total.items():
        out.extend(v)

    return out

def  evaluate_line():
    config = model_utils.load_config(FLAGS.config_file)
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True
    with open(FLAGS.map_file, "rb") as f:
        word_to_id, id_to_word, tag_to_id, id_to_tag = pickle.load(f)
    with tf.Session(config=tf_config) as sess:
        model = model_utils.create(sess, Model, FLAGS.ckpt_path, config)
        out = []
        df = pd.read_excel(local_file)
        for line in df['病历']:
            result = model.evaluate_line(sess, data_utils.input_from_line(line, word_to_id), id_to_tag)
            out.append(handle(result))
        columns = []
        for item in types_index:
            for i in range(1, types_num + 1):
                columns.append(item + str(i))

        df_out = pd.DataFrame(out, columns=columns)
        df_out.insert(loc=0, column='ID', value=df['ID'])
        df_out.to_excel(result_file, index=None)





def main(_):
    evaluate_line()




if __name__ == "__main__":
    tf.app.run(main)

