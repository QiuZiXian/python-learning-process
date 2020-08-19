# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/8/1  11:31
# @abstract    :

#!/usr/bin/python
# -*- coding: UTF-8 -*-


#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import getopt
import pandas as pd



def init(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return inputfile, outputfile



def delete(input, output):
    data = pd.read_csv(input, sep='\t', converters={
                       'he_ID': str, 'xushi': str, 'sen': str, 'xushi.1': str})
    print(data)
    sort_count = data.groupby('sen').count().reset_index()
    sen_start = 0
    del_index = []
    for i in range(len(sort_count.lan)):
        for j in range(sen_start, sen_start+sort_count.lan[i]-1):
            if data.xushi[j] == '0':
                for k in range(sen_start, sen_start+sort_count.lan[i]-1):
                    if data.depID[j] == data.he_ID[k]:
                        data.iloc[k, 8:] = data.iloc[j, 8:]
                del_index.append(j)
        sen_start += sort_count.lan[i]
    data = data.drop(index=del_index)
    data.to_csv(output, index=False, sep='\t')



if __name__ == "__main__":
    # 命令行指令 python OAO.py -i in.csv -o out.csv
    input, output = init(sys.argv[1:])
    if input == '' or output == '':
        sys.exit()
    delete(input, output)