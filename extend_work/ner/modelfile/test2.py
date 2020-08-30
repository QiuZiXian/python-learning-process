# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/28  20:22
# @abstract    :


# li = [1, 2, 3]
#
# print(li.insert(0, 1010))
# print(li)
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
# dog_set = wn.synsets('dog')
# print('dog的同义词集为：', dog_set)
# print('dog的各同义词集包含的单词有：',[dog.lemma_names() for dog in dog_set])
# print('dog的各同义词集的具体定义是：',[dog.definition() for dog in dog_set])
# print('dog的各同义词集的例子是：',[dog.examples() for dog in dog_set])


goods = wn.synsets('心脏病')
beautifuls = wn.synsets('心脏疾病')
bads = wn.synsets('bad')
dogs = wn.synsets('dog')
cats = wn.synsets('cat')
print('good和beautiful的语义相似度为： ', max([0 if good.path_similarity(beautiful) == None else good.path_similarity(beautiful) for good in goods for beautiful in beautifuls]))
print('good和bad的语义相似度为： ', max([0 if good.path_similarity(bad) == None else good.path_similarity(bad) for good in goods for bad in bads]))
print('dog和cat的语义相似度为： ', max([0 if dog.path_similarity(cat) == None else dog.path_similarity(cat) for dog in dogs for cat in cats]))

