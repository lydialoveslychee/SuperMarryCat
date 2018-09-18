# -*- coding: cp936 -*-
# python大作业 5110309443 杨荔雅
import pygame
from pygame.locals import *
import random
from gameobjects.vector2 import Vector2

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("pythonhomework--super stupid cat")

background=pygame.image.load("background.png").convert()
cat=pygame.image.load("normal.png").convert_alpha()
cat_hitted=pygame.image.load("hitted.png").convert_alpha()
cat_rewarded=pygame.image.load("rewarded.png").convert_alpha()
cloud_bad=pygame.image.load("cloud2.png").convert_alpha()
cloud_nice=pygame.image.load("cloud1.png").convert_alpha()
wood=pygame.image.load("floor.png").convert_alpha()
flower=pygame.image.load("flower.png").convert_alpha()
turtle=pygame.image.load("turtle.png").convert_alpha()
shooter1=pygame.image.load("shooter1.png").convert_alpha()
shooter2=pygame.image.load("shooter2.png").convert_alpha()
cat_died=pygame.image.load("died.png").convert_alpha()
monster1=pygame.image.load("monster1.png").convert_alpha()
monster2=pygame.image.load("monster2.png").convert_alpha()
monster3=pygame.image.load("monster3.png").convert_alpha()
mushroom=pygame.image.load("mushroom.png").convert_alpha()
badmushroom=pygame.image.load("badmushroom.png").convert_alpha()
money=pygame.image.load("money.png").convert_alpha()
block=pygame.image.load("block.png").convert_alpha()
block2=pygame.image.load("block2.png").convert_alpha()

key_direction=Vector2(0,0)
cat_pos=Vector2(0,300)
x2,y2=0,100
x3,y3=0,390
x4,y4=400,480
x5,y5=100,50
x6,y6=390,370
x7,y7=100,350


move={K_LEFT:0,K_RIGHT:0}
clock=pygame.time.Clock()
move_y=0
speed_y=250
speed_cat=250
speed_cloud=100
speed_cloud2=80
speed_flower=150
while True:
    time_passed=clock.tick(30)
    time_passed_seconds=time_passed/1000.0
    
#cat------
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()

        if event.type==KEYDOWN:
            if event.key ==K_RIGHT:
                key_direction.x=+1
            if event.key==K_LEFT:
                key_direction.x=-1

            if event.key==K_UP:
                move_y=-150
                speed_y=250

        if event.type==KEYUP:
            if event.key in move:
                key_direction.x=0
                
                   
    if cat_pos.x<0:
        key_direction.x=0
        cat_pos.x=0

    else:
        
        if 450<cat_pos.x<565:
            pass
        if 320<cat_pos.x<340 and cat_pos.y>260:
            key_direction.x=0
            cat_pos.x=320
        if 440<cat_pos.x<460 and cat_pos.y>260:
            key_direction.x=0
            cat_pos.x=460
        if cat_pos.x>565:
            key_direction.x=0
            cat_pos.x=565
                
    #if cat_pos.y<180:
        #key_direction.y=-key_direction.y
    #elif cat_pos.y>300:
        #key_direction.y=0
        #cat_pos.y=300
        
    key_direction.normalize()

    cat_pos.y+=move_y+speed_y*time_passed_seconds

    cat_pos+=key_direction*speed_cat*time_passed_seconds

    #badcloud-----------------------------------------

    x2+=speed_cloud*time_passed_seconds
    if x2>640-cloud_bad.get_width():
        speed_cloud = -speed_cloud
        x2= 640-cloud_bad.get_width()
    elif x2<0:
        speed_cloud = -speed_cloud
        x2=0

    #nicecloud-----------------------------------------

    x5+=speed_cloud2*time_passed_seconds
    if x5>640-cloud_nice.get_width():
        speed_cloud2 = -speed_cloud2
        x5= 640-cloud_nice.get_width()
    elif x5<0:
        speed_cloud2 = -speed_cloud2
        x5=0

    #flower------------------------------------------------

    y4-=speed_flower*time_passed_seconds
    if y4<300:
        speed_flower=-speed_flower
        y4=300
    elif y4>480:
        speed_flower=-speed_flower
        y4=480

    
    #draw the game-----------------------------------------    

    screen.blit(background,(0,0))
    screen.blit(wood,(x3,y3))
    screen.blit(flower,(x4,y4))
    screen.blit(block,(x6,y6))
    screen.blit(cloud_nice,(x5,y5))
    screen.blit(cloud_bad,(x2,y2))
    #screen.blit(mushroom,(0,200))
    #screen.blit(badmushroom,(100,200))
    #screen.blit(shooter1,(200,200))
    #screen.blit(shooter2,(300,200))
    #screen.blit(monster1,(400,200))
    #screen.blit(monster2,(500,200))
    screen.blit(monster3,(x7,y7))
    #screen.blit(turtle,(400,0))
    #screen.blit(money,(300,0))
    screen.blit(block2,(0,250))
    screen.blit(cat,cat_pos)
    

    pygame.display.update()
        
