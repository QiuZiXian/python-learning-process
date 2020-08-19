#!/usr/bin/python
# coding:utf-8
import os
import time
import datetime as dt

# try:
# 	import xml.etree.cElementTree as ET
# except ImportError:
# 	import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element, ElementTree
import os
import xml.etree.ElementTree as ET


pathname = "./conf.xml" # 文件路径
tree=ET.parse("conf.xml")
# tree.parse(pathname)
# for item in tree.iter():
# 	print(item)
# delayday = 1
# handledate = str(dt.datetime.strftime(dt.datetime.today() - dt.timedelta(delayday), "%Y-%m-%d"))
#
# xmlDoc = ET.parse('./conf1.xml') # staff_info_mirror#staff_concurrent_post#company_senior_executives
# tableName = xmlDoc.find("tableName").text
# packageName = xmlDoc.find("packageName").text
# tableSchema = xmlDoc.find("schema").text

root=tree.getroot()
print(root.tag)

for child in root:
	print(child.tag, child.attrib)

# for rank in root.iter('rank'):
# 	new_rank = int(rank.text) + 1
# 	rank.text = str(new_rank)
# 	rank.set("updated", "yes")
b = ET.SubElement(root, "fold")
b.text = "filename"

newNode = ET.Element("NewNode")
newNodeName = ET.Element('Name')
newNodeName.text = 'NodeC'
newNode.append(newNodeName)
root[0].insert(0, newNode)
tree.write("output.xml")
# fold = Element("fold")
# fold.text= os.path.splitext(pathname) # 文件名
# root.append(fold)

# tree.write("./conf1.xml", encoding="utf-8", xml_declaration=True)

# ET.tostring(tree, encoding="us-ascii", method="xml")

# try:
# 	reparsed = mini.parseString(mini.parse('YOUR_FILE_NAME').toxml())
# 	pretty_string = '\n'.join([line for line in reparsed.toprettyxml(indent=' ' * 4).split('\n') if line.strip()])
#
# 	f = open('YOUR_FILE_NAME', 'w')
# 	f.write(pretty_string)
# finally:
# 	f.close()






