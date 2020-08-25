name = 'G1.txt'  # 输入文件名
f = open(name, 'r', encoding="UTF-8-SIG")
r = f.readlines()
f.close()
list1 = []
list_F = []
list_L = [(15, 0, 0)]
x3 = 0

########### arc former ########### (用于转化为G坐标之前)
from math import *
# from pattern_maker.Cir_new import *
def pri_tp (YN,cirx,ciry,cirz):
    print("N" + str(YN) + " X" + str(cirx) + " Y" + str(ciry) + " Z" + str(cirz))

def arc(p1, p2, YN, pat):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    cirz = (p1[2] + p2[2]) / 2
    r = ((dx ** 2 + dy ** 2) ** (1 / 2)) / 2
    cocx = (p1[0] + p2[0]) / 2
    cocy = (p1[1] + p2[1]) / 2

    for i in range(25):
        angle = (7.5 / 360) * 2 * pi * i

        # 1-横向右半圆 （由左到右）
        # 2-横向左半圆
        # 3-纵向下半圆 （由下到上）
        # 4-纵向上半圆

        if pat == 1:
            ciry = cocy - r * cos(angle)  # 根据趋势来定正负和三角函数 sin在（0，pi）中保持增量趋势为小大小, cos则是前半程加 后半程减
            cirx = cocx + r * sin(angle)
        elif pat == 2:
            ciry = cocy - r * cos(angle)
            cirx = cocx - r * sin(angle)
        elif pat == 3:
            ciry = cocy - r * sin(angle)
            cirx = cocx + r * cos(angle)
        elif pat == 4:
            ciry = cocy + r * sin(angle)
            cirx = cocx + r * cos(angle)

        pri_tp (YN,cirx,ciry,cirz)
def arc_tq(p1, r, YN):  # 由横到竖 3/4连接圆弧
    x = p1[0]
    y = p1[1]
    cirz = p1[2]
    cocx = x + r
    cocy = y + r
    for i in range(37):
        angle = (7.5 / 360) * 2 * pi * i
        if i <= 24:
            cirx = cocx + r * sin(angle)
            ciry = cocy - r * cos(angle)
        elif i >= 25:
            cirx = cocx - r * sin(angle - pi)
            ciry = cocy + r * cos(angle - pi)
        else:
            print(i)
            print('Error')

        pri_tp (YN,cirx,ciry,cirz)

list_P1_h =[]
list_P1_z =[]
list_P2_h =[]
list_P2_z =[]
list_P3_h =[]
list_P3_z =[]
list_P4_h =[]
list_P4_z =[]

for i in r:  # 获取初始纤维路径坐标
    try:
        if i[0] == "N":

            list2 = []
            YN = float(i.split("N")[1].split(" ")[0])
            x1 = i.split("X")[1].split(" ")[0]
            x2 = i.split("Y")[1].split(" ")[0]
            X3 = i.split("Z")[1].split(" ")[0]

            list2.append(float(x1))
            list2.append(float(x2))
            list2.append(float(x3))
            list2.append(int(YN))

            #分层加点
            if YN <= 17:
                if YN < 9: # 先是waft yarn
                    list_P1_h.append(list2)
                else:
                    list_P1_z.append(list2)

            elif YN > 17 and YN <= 35:
                if YN < 27:
                    list_P2_h.append(list2)
                else:
                    list_P2_z.append(list2)
            elif YN > 35 and YN <= 53:
                if YN < 45:
                    list_P3_h.append(list2)
                else:
                    list_P3_z.append(list2)
            elif YN > 53 and YN <= 71:
                if YN < 63:
                    list_P4_h.append(list2)
                else:
                    list_P4_z.append(list2)

        else:
            print ('Error')
    except:
        pass

count = 0 #用于记录纤维编号的变化
count_re =1
d = 4
pat = 0
j = 1
list_pri = []
list_pri_re = []
for i in list_P1_h: #分两批
    if i [3] % 2 ==0:
        list_pri.append(i)
    elif i[3]%2 != 0:
        list_pri_re.append(i)
    else:
        print ('Error')

#######横线部分
for i in list_pri:
    x = i[0]
    y = i[1]
    z = i[2]
    yn = i[3]

    if count == yn:
        pri_tp(yn, x, y, z)
    else:
        count = yn +2
        if yn % 2 ==0:
            arc((x,y,z),(x,y+d,z),yn,1)
            pat+=1
        else:
            print ('Error')

    if j == len(list_P1_h):
        arc_tq (i,1,i[3])
        break
    else:
        pass
    j += 2

for i in list_pri_re[::-1]:
    x = i[0]
    y = i[1]
    z = i[2]
    yn = i[3]
    if count == yn:
        pri_tp(yn, x, y, z)
    else:
        count_re = yn + 2 #因为列表是奇偶数分批的
        if yn % 2 !=0:
            arc((x, y, z), (x, y + d, z), yn, 2)
            pat += 1
        else:
            print ('Error1')

#####分别输出再排序
# print (list_P1_h)
'''
print (list_P1_h)

print (list_P1_z)
print (list_P2_h)
print (list_P2_z)
print (list_P3_h)
print (list_P3_z)
print (list_P4_h)
print (list_P4_z)
'''

