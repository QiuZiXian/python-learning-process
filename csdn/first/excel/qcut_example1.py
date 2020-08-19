# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:09:26 2020

@author: 87875
"""
import pandas as pd



df = pd.read_excel("D:/d/csdn/1.xlsx")
# =============================================================================
df.fillna(0, inplace=True)
# =============================================================================
newDf = df[['target', 'score1']].copy()
# newDf.dropna(axis=0, how='any', inplace=True)
newDf.fillna(0, inplace=True)
newDf['id'] = df.index.values
newDf.target = df.index.values
# print(newDf)
# =============================================================================
newDf.sort_values(by=['score1'], inplace=True)
labels = ['a', 'b', 'c', 'd', 'e']
newDf['result'] =pd.qcut(newDf.id, q=5, duplicates='drop', labels=labels)
counts = newDf['result'].value_counts()
# print(newDf['result'].value_counts())
groups = newDf.groupby('result')

for name, group in groups:
	print(name, ":====================>")
	print(group)
	print(group.target.value_counts(1))
	break



