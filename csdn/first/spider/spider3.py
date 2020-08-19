# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/20  19:28
# @abstract    :	模拟鼠标功能，点击另存为 至指定位置

from selenium import webdriver
import time
import win32clipboard
import win32api
import win32con
from selenium.webdriver.common.action_chains import ActionChains




def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,0,0)


def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)




VK_CODE={'enter':0x0D,'down_arrow':0x28}


url2='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&step_word=&hs=0&pn=1&spn=0&di=49500&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1680238894%2C752784316&os=1456076808%2C2964036578&simid=4162351635%2C532680339&adpicid=0&lpn=0&ln=1219&fr=&fmq=1462357247335_R&fm=&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201709%2F07%2F20170907142921_VEUnJ.thumb.700_0.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fn2_z%26e3Bxtvt_z%26e3BgjpAzdH3FtvijAzdH3F14w-mccdmmc_z%26e3Bip4s&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'


#browser= webdriver.Chrome(executable_path=r'D:/Automation/chromedriver.exe')
browser= webdriver.Chrome()
browser.maximize_window()


browser.get(url2)

time.sleep(2)

path='E:\\'
win32clipboard.OpenClipboard()


win32clipboard.EmptyClipboard()


win32clipboard.SetClipboardText(path)


win32clipboard.CloseClipboard()

img=browser.find_element_by_xpath('//*[@id="currentImg"]')


action = ActionChains(browser).move_to_element(img)


action.context_click(img).perform()


time.sleep(1)


win32api.keybd_event(86,0,0,0)


time.sleep(1)


win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x56, 0, 0, 0)
win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)

win32api.keybd_event(0x0D,0,0,0)


win32api.keybd_event(0x12, 0, 0, 0)
win32api.keybd_event(0x53, 0, 0, 0)
win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x12, 0, win32con.KEYEVENTF_KEYUP, 0)




keyDown('enter')


keyUp('enter')


time.sleep(1)


print('over')


#browser.quit()