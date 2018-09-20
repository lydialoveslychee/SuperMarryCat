from sys import exit
from cat import Cat
import pygame
from pygame.locals import *
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load("res/normal.png").convert()
cat = Cat(3, 10, "res/normal.png", 640, 480, screen, 100)
isForward = False
isBackward = False
isJumping = False
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
        if event.type == KEYDOWN:
            #键盘有按下？
            if event.key == K_LEFT:
                #按下的是左方向键的话，把x坐标减一
                isBackward = True
            elif event.key == K_RIGHT:
                #右方向键则加一
                isForward = True
            elif event.key == K_UP:
            	isJumping = True

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                isBackward = False
            elif event.key == K_RIGHT:
                isForward = False
    if isForward:
        cat.forward()
    if isBackward:
        cat.backward()
    if isJumping:
        isJumping = cat.jump()
 
    #计算出新的坐标
    screen.fill((0,0,0))
    cat.showCat()
    #在新的位置上画图
    pygame.display.update()