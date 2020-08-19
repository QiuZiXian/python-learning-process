# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/7  10:47
# @abstract    :


import xml.etree.ElementTree as ET


pathname = "./conf.xml" # 文件路径
tree=ET.parse("conf.xml") # 解析文件进入内存，tree

root=tree.getroot() # 根节点
print(root.tag)

for child in root:  # 遍历根节点下 的每个子节点
	print(child.tag, child.attrib)

# 遍历 root树中的rank节点，对其进行修改
for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1 # rank.text 获取rank节点的文本内容
	rank.text = str(new_rank)
	rank.set("updated", "yes") # rank节点添加 updated属性，值为yes ； 即 updated = yes


	# 在某个节点下添加子节点 a = ET.Element("nodeName")
b = ET.SubElement(root, "fold") # 在root下添加fold节点
b.text = "filename" # fold节点内容


# 指定位置添加 多级节点, # root 为 0
newNode_1 = ET.Element("NewNode")
newNode_2 = ET.Element('Name')
newNode_2.text = 'NodeC'
newNode_1.append(newNode_2) # 子节点依次添加进父节点

root[0].insert(0, newNode_1) # 1级节点 添加进根节点指定位置
tree.write("output.xml")