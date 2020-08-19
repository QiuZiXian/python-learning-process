# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:21:16 2020
http://www.sse.com.cn/market/stockdata/overview/day/
@author: 87875
"""

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
def get_table_content(tableId,queryContent):
 
    # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
    table_tr_list = driver.find_element_by_class_name(tableId).find_elements(By.TAG_NAME, "tr")
    table_list = []  #存放table数据
    for tr in table_tr_list:    #遍历每一个tr
        #将每一个tr的数据根据td查询出来，返回结果为list对象
        table_td_list = tr.find_elements(By.TAG_NAME, "td")
        row_list = []
        for td in table_td_list:    #遍历每一个td
            row_list.append(td.text)    #取出表格的数据，并放入行列表里
        table_list.append(row_list)
 
    # 循环遍历table数据，确定查询数据的位置
    for i in range(len(table_list)):
        for j in range(len(table_list[i])):
                print(table_list[i][j])
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
driver = Chrome()
#/datasearch/QueryList?tableId=26&searchF=Quick%20SearchK&pageIndex=1&pageSize=15
brower = driver.get('http://www.sse.com.cn/market/stockdata/overview/day/')     # get方式访问百度.
time.sleep(2)
get_table_content("table","");