# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/11  16:06
# @abstract    :

import xlwings as xw
wb = xw.Book('1.xlsx')
sht = wb.sheets['sheet1']
new_wb = xw.Book()
new_sht = new_wb.sheets[0]
sht.api.Copy(Before = new_sht.api)
sht.range('A1:C10').value = new_sht.range('A1:C10').value