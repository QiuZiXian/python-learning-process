# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/28  16:57
# @abstract    :

types_num = 20
types_index = ['DIS', 'DRUG', 'OP', 'MAG', 'SIGN'] # 分类 类别
types_total = {types:[] for types in types_index}


data = {'string': '出院诊断：1.脑梗死(大动脉粥样硬化型)2.高血压病3级（极高危）3.2型糖尿病4.右眶上神经痛。 住院天数：12天。 入院情况：主要症状及体征：徐,男,70岁,汉族，已婚，因“突发头晕及左侧肢体无力3天余。 ”。 门诊拟“脑梗死”于2015-06-29收入院。 入院查体：NIHSS评分3分，洼田饮水试验1分，神志清楚，构音障碍，双侧瞳孔等大等圆，直径约3mm，直接、间接对光反射均灵敏，右眼不能内收，有复视。 双侧额纹对称，双侧闭目有力，双侧鼻唇沟对称，右侧肢体肌力5级，左侧上下肢肌力5级—，左侧Babinski征、Chaddock征均＋。 住院期间主要检查结果：头颅CT（2015-6-29长海医院 片号1774627）：老年脑。 头颅MRI（2015-6-29长海医院 检查号1776699）：脑干新鲜梗塞灶。，基底动脉中段狭窄，右侧大脑后动脉P2段狭窄，头颈动脉多发血管硬化。 2015-6-30 肝功能：间接胆红素8.9umol/L，直接胆红素6.5umol/L，丙氨酸氨基转移酶22U/L，门冬氨酸氨基转移酶18U/L，电解质：钠144mmol/L，钾3.5mmol/L，氯104mmol/L，肾功能：尿素5.5mmol/L，肌酐96umol/L，血糖6.6mmol/L，血脂：总胆固醇3.94mmol/L，甘油三酯1.46mmol/L，高密度脂蛋白胆固醇0.88mmol/L，低密度脂蛋白胆固醇2.61mmol/L，糖化血红蛋白6.7%，血沉2mm/H，甲状腺功能：游离T3：4.67Pmol/L，游离T4：15.95Pmol/L，促甲状腺激素TSH4.90mIU/L。 诊疗经过：治疗情况：予阿司匹林+氯吡格雷双联抗血小板治疗，予他汀调脂稳定斑块治疗，辅以活血、清除自由基、营养神经、改善微循环等药物治疗。 出院情况：患者目前病情稳定，一般情况良好，较入院时有改善，经上级医师指示，与患者及家属沟通同意后，予以出院。 ', 'entities': [{'word': '脑梗死(大动脉粥样硬化型)', 'start': 7, 'end': 20, 'type': 'DIS'}, {'word': '高血压病3级（极高危', 'start': 22, 'end': 32, 'type': 'DIS'}, {'word': '2型糖尿病', 'start': 35, 'end': 40, 'type': 'DIS'}, {'word': '右眶上神经痛', 'start': 42, 'end': 48, 'type': 'DIS'}, {'word': '头', 'start': 92, 'type': 'BODY'}, {'word': '左侧肢体', 'start': 94, 'end': 98, 'type': 'BODY'}, {'word': '脑梗死', 'start': 112, 'end': 115, 'type': 'DIS'}, {'word': '双侧瞳孔', 'start': 166, 'end': 170, 'type': 'BODY'}, {'word': '右眼', 'start': 195, 'end': 197, 'type': 'BODY'}, {'word': '双侧额', 'start': 207, 'end': 210, 'type': 'BODY'}, {'word': '双侧鼻唇沟', 'start': 221, 'end': 226, 'type': 'BODY'}, {'word': '右侧肢体', 'start': 229, 'end': 233, 'type': 'BODY'}, {'word': '左侧上下肢', 'start': 238, 'end': 243, 'type': 'BODY'}, {'word': '头颅', 'start': 285, 'end': 287, 'type': 'BODY'}, {'word': '脑', 'start': 318, 'type': 'BODY'}, {'word': '头颅', 'start': 320, 'end': 322, 'type': 'BODY'}, {'word': '脑干', 'start': 352, 'end': 354, 'type': 'BODY'}, {'word': '右侧大脑后动脉', 'start': 370, 'end': 377, 'type': 'BODY'}, {'word': '头颈动脉', 'start': 383, 'end': 387, 'type': 'BODY'}, {'word': '间接胆红素', 'start': 409, 'end': 414, 'type': 'LAB'}, {'word': '直接胆红素', 'start': 424, 'end': 429, 'type': 'LAB'}, {'word': '丙氨酸氨基转移酶', 'start': 439, 'end': 447, 'type': 'LAB'}, {'word': '门冬氨酸氨基转移酶', 'start': 453, 'end': 462, 'type': 'LAB'}, {'word': '钠', 'start': 471, 'end': 473, 'type': 'LAB'}, {'word': '，钾', 'start': 482, 'end': 484, 'type': 'LAB'}, {'word': '，氯', 'start': 493, 'end': 495, 'type': 'DRUG'}, {'word': '尿素', 'start': 509, 'end': 511, 'type': 'LAB'}, {'word': '肌酐', 'start': 521, 'end': 523, 'type': 'LAB'}, {'word': '血糖', 'start': 532, 'end': 534, 'type': 'LAB'}, {'word': '血脂：总胆固醇', 'start': 544, 'end': 551, 'type': 'LAB'}, {'word': '甘油三酯', 'start': 562, 'end': 566, 'type': 'LAB'}, {'word': '高密度脂蛋白胆固醇', 'start': 577, 'end': 586, 'type': 'LAB'}, {'word': '低密度脂蛋白胆固醇', 'start': 597, 'end': 606, 'type': 'LAB'}, {'word': '血红蛋白', 'start': 618, 'end': 623, 'type': 'LAB'}, {'word': '甲状腺激素', 'start': 676, 'end': 681, 'type': 'LAB'}, {'word': '阿司匹林', 'start': 706, 'end': 710, 'type': 'DRUG'}, {'word': '氯吡格雷', 'start': 711, 'end': 715, 'type': 'DRUG'}]}

# print(data['entities'])


for item in data['entities']:
	if item['type'] in types_index:
		types_total[item['type']].append(item['word'])

for k,v in types_total.items():
	if len(v) < types_num:
		v.extend(['']*(types_num - len(v)))

for k,v in types_total.items():
	print(v[0:types_num])



#=================================================

import os
import tensorflow as tf
import pickle

import data_utils
import model_utils
from model import Model

import openpyxl


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
    book = openpyxl.load_workbook(r'输入文件.xlsx')
    sh = book.active
    arr = []
    for r in list(sh.rows)[1:]:
        line = r[1].value
        result = model.evaluate_line(sess, data_utils.input_from_line(line, word_to_id), id_to_tag)
        arr.append({"id":r[0].value,"data":result})
    print(arr)

    newbook = openpyxl.Workbook()
    sh = newbook.active
    headtype = {
        'DIS':{"name":'疾病',"num":20},
        '症状的type':{"name":'症状',"num":20},
        'DURG':{"name":'药物',"num":20}
    }
    harr = ['ID']
    for n,t in headtype.items():
        t['start'] = len(harr)
        for i in range(1,t['num']+1):
            harr.append(t['name']+str(i))
    sh.append(harr)
    for t in arr:
        larr = ['']*len(harr)
        larr[0] = t['id']
        htc = { k:obj['start'] for k,obj in headtype.items()}
        for entitie in t['data']['entities']:
            larr[htc[entitie['type']]] = entitie['word']
            htc[entitie['type']] += 1
        sh.append(larr)
    newbook.save(r'输出文件.xlsx')


def main(_):
  evaluate_line()

if __name__ == "__main__":
  tf.app.run(main)
