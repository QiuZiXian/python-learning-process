# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/7/27  13:51
# @abstract    :

# -*- coding: utf-8 -*-
import pygame  # 导入pygame库
from sys import exit  # 向sys模块借用exit函数来退出程序

pygame.init()  # 初始化pygame

screen = pygame.display.set_mode((600, 170), 0, 32)
# 创建一个窗口，第一个参数为元祖，代表分辨率，第二个为标志位，默认0，如果为FULLSCREEN，则为全屏，第三个为色深
pygame.display.set_caption("Hello World!")  # 设置窗口标题
background = pygame.image.load('a.png').convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	screen.blit(background, (0, 0))  # 画背景图,第一个参数为surface对象，第二个参数为左上角的坐

	pygame.display.update()  # 刷新画面



####################
# 导入类库
import math
import random
import pygame
from pygame.locals import *
# 游戏初始化
pygame.init()
# 音频初始化
pygame.mixer.init() # music initial
# 设置屏幕宽高
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
# 加载图片和声音
player = pygame.image.load("resources/images/dude.png")
# 绘制图形
screen.blit(player, (100, 100)
hit = pygame.mixer.Sound("resources/audio/explode.wav")
# 设置音量
hit.set_volume(0.05)


# 圈出一块矩形区域
bullrect=pygame.Rect(arrow.get_rect())
# 设置矩形的坐标
bullrect.left=bullet_x
bullrect.top=bullet_y

# 圈出一块矩形区域
badrect = pygame.Rect(badguyimg.get_rect())
# 设置矩形的坐标
badrect.left = badguy_x
badrect.top = badguy_y
if badrect.colliderect(bullrect):
    print 'Shooted'


# 下面的是事件循环
while True:
    # 取出每一个事件对象
    for event in pygame.event.get():
        # 判断是否是退出事件
        if event.type == pygame.QUIT:
            # 退出游戏
            pygame.quit()
            exit(0)
        #     判断是否是键盘按下事件
        if event.type == pygame.KEYDOWN:
            # 判断 是否按下了q键
            if event.key == K_q:
                # 退出游戏
                pygame.quit()
                exit(0)
    # 刷新游戏的屏幕
    pygame.display.flip()

# 初始化字体设置
pygame.font.init()
# 设置24号字体
font = pygame.font.Font(None, 24)
# 使用上面的字体渲染出"Good job"文字
text = font.render("Good job", True, (255,0,0))
# 圈出一块矩形区域
textRect = text.get_rect()
# 设置矩形区域 的中心点坐标
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery+24
# 在缓冲区绘制图形
screen.blit(gameover, (0,0))
# 在缓冲区绘制上面的矩形
screen.blit(text, textRect)


# pygame应该有个事件队列 不停的从队列取出事件看看是不是退出事件 是的话 就退出pygame游戏