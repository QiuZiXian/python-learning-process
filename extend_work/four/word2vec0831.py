# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/31  19:28
# @abstract    :

# from gensim.models import Word2Vec
#
# sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
# model = Word2Vec(sentences, min_count=1)


from gensim.models import KeyedVectors


# wv_from_text = KeyedVectors.load_word2vec_format('./all_w2v_model_CBOW_no_comments.txt', binary=False)
# # print(wv_from_text.vectors)
# print(wv_from_text.index2word)
# print(wv_from_text.index2entity)
# print(wv_from_text.similarity_matrix)
# # print(wv_from_text)


# obj = {}
# with open('./0831.txt', "r") as f:
#     for text in list(f)[1:]:
#         tg = text.strip().split(" ")
#         key = tg.pop(0)
#         obj[key] = list(map(float,tg))
# # print(obj)
# for k, v in obj.items():
# 	print(v)

data = {}
with open('./0831.txt', 'r') as f:
	f.readline()
	for line in f.readlines():
		temp = line.strip().split(' ')
		k = temp.pop(0)
		data[k] = temp
		print(temp)