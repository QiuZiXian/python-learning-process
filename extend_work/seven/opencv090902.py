# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/9  13:55
# @abstract    :

import cv2
import os
import pandas as pd

# 1.用字典存储每一张像素块图及直方图
def build_index():
    print('正在计算各图片直方图')
    readPath = "D:\\save"
    files = os.listdir(readPath)
    dist = {}

    for file in files:
        imgPath = readPath + '\\' + file
        img = cv2.imread(imgPath)
        hist = []

        for i in range(3):
            ht = cv2.calcHist([img], [i], None, [256], [0, 256])
            hist.append(ht)
        dist[file] = hist

    print('各图片直方图计算已完成！')
    return dist


# 2.用相近的图代替原图
def match_replace(dist):
    print('正在替换图片：')
    image = cv2.imread('D:/a.png')
    # 自动取图的分辨率
    width, height = image.shape[1], image.shape[0]
    calcP = {}
    for i in range(0, height, 25):
        for j in range(0,width , 25):
            img = image[i:i + 25, j:j + 25, 0:3]

            hist = []
            for k in range(3):
                ht = cv2.calcHist([img], [k], None, [256], [0, 256])
                hist.append(ht)

            sim = 0.0
            rename = '11.png'
            for key in dist:
                match0 = cv2.compareHist(hist[0], dist[key][0], cv2.HISTCMP_CORREL)
                match1 = cv2.compareHist(hist[1], dist[key][1], cv2.HISTCMP_CORREL)
                match2 = cv2.compareHist(hist[2], dist[key][2], cv2.HISTCMP_CORREL)
                match = match0 + match1 + match2

                if match > sim:
                    sim = match
                    rename = key

            # 一张图分辨率不可能是25的整数，增加一个裁剪功能
            ph = (height - i) if i + 25 > height else 25
            pw = (width - j) if j + 25 > width else 25
            image[i:i + 25, j:j + 25, 0:3] = cv2.imread('D:\\save\\' + rename)[0:ph,0:pw,0:3]
            if calcP.get(rename, 0) == 0:calcP[rename] = 0
            calcP[rename] += 1
    cv2.imwrite('D:/b.png', image)
    pd.DataFrame({"name":list(calcP.keys()),"cnt":list(calcP.values())}).to_excel('D:/c.xlsx',index=False)
    print('图片替换已完成！')


# 3.混合图片
def mix_image():
    print('正在融合图片：')
    image1 = cv2.imread('D:/a.png')
    image2 = cv2.imread('D:/b.png')
    dst = cv2.addWeighted(image1, 0.2, image2, 0.8, 3)
    cv2.imwrite('D:/v_mix.png', dst)
    print('图片融合已完成！')


if __name__ == "__main__":
    dist = build_index()
    match_replace(dist)
    mix_image()