# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 02:02:28 2019

@author: hwdon
"""

import pygame, sys
from pygame.locals import *


WIDTH = 600                      # 窗口宽度
HEIGHT = 400                     # 窗口高度

BALL_RADIUS = 15                 #球的半径
ball_pos = [0,0]                 #球的位置
ball_vel = [0,0]                 #球的速度
PAD_WIDTH = 8                    #挡板宽
PAD_HEIGHT = 80                  #挡板高
HALF_PAD_WIDTH = PAD_WIDTH//2
HALF_PAD_HEIGHT = PAD_HEIGHT//2
paddle1_pos = [0,0]
paddle2_pos = [0,0]

paddle1_vel = 0         #左paddle速度(上下移动的速度)
paddle2_vel = 0
score1 = 0              #左paddle得分
score2 = 0              #右paddle得分    

#常用颜色 (R,G,B) (红黄蓝)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


import random 

# 数据：圆的参数
circle_pos = (0,0)
circle_radius = 0
circle_color = (0,0,0) 
circle_color = (255,255,255)

#初始化游戏窗口
def init_window():
    # 1. 初始化
    pygame.init()   #初始化 pygame
    
    #设置窗口的模式，（680，480）表示窗口像素，及（宽度，高度）
    #此函数返回一个用于绘制的Surface对象(相当于一块画布)
    surface = pygame.display.set_mode((WIDTH, HEIGHT))   
    
    pygame.display.set_caption('Game Engine')   #设置窗口标题
    return surface

def init_scene():
    #初始化左右paddle(挡板)的属性
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2                                    
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT // 2]
    paddle2_pos = [WIDTH - 1 - HALF_PAD_WIDTH, HEIGHT // 2]
    #paddle1_vel = [0, 0]
    #paddle2_vel = [0, 0]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    #初始化球的属性
    global ball_pos, ball_vel                 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    horizontal = random.randrange(2,4)    #随机生成的水平速度
    vertical = random.randrange(1,3)      #随机生成的垂直速度    
        
    if random.random()>0.5:               #随机的向左向右
        horizontal= -horizontal        
    if random.random()>0.5:               #随机的向上向下
        vertical= -vertical
     
    ball_vel = [horizontal,-vertical]


def ball_init():
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    horizontal = random.randrange(2,4)
    vertical = random.randrange(1,3)
    
    #表示向右    
    if random.random()>0.5:
        horizontal= -horizontal
    if random.random()>0.5:
        vertical= -vertical
     
    ball_vel = [horizontal,-vertical]
    


CICLE_RADIUS  = 70      #背景中的中心元半径

def draw(surface):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, score1, score2
    
    #绘制画面背景
    surface.fill(BLACK)              #背景颜色为黑色
    pygame.draw.line(surface, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(surface, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(surface, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(surface, WHITE, [WIDTH//2, HEIGHT//2], CICLE_RADIUS, 1)

   
    #绘制挡板 paddles和球 ball
    pygame.draw.circle(surface, WHITE, (int(ball_pos[0]),int(ball_pos[1])), BALL_RADIUS, 0)
    pygame.draw.rect(surface, GREEN, (int(paddle1_pos[0]) - HALF_PAD_WIDTH, int(paddle1_pos[1]) - HALF_PAD_HEIGHT, 
                                        PAD_WIDTH,PAD_HEIGHT))
    pygame.draw.rect(surface, GREEN, (int(paddle2_pos[0]) - HALF_PAD_WIDTH, int(paddle2_pos[1]) - HALF_PAD_HEIGHT, 
                                        PAD_WIDTH,PAD_HEIGHT))

    #绘制得分 scores
    drawText(surface,"Score1: "+str(score1),(50,20))
    drawText(surface,"Score2: "+str(score2), (470, 20))  
    
    pygame.display.flip()        #刷新画面

# 辅助函数：绘制文本。参数：文本、位置、字体名和字体大小，
def drawText(surface,text,pos=(1,1),color = RED,font_name="Comic Sans MS",font_size=20):
    myfont = pygame.font.SysFont(font_name,font_size)
    text_image = myfont.render(text,1,color)
    surface.blit(text_image, pos)  
    
    
#1. 游戏初始化
def init():
    surface = init_window()
    init_scene()
    return surface

# 键盘按下事件处理函数：更新挡板的垂直速度
def keydown(event):
    global paddle1_vel, paddle2_vel
 
    if event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8
    elif event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8

#键盘弹起事件处理函数：挡板速度重置为0
def keyup(event):
    global paddle1_vel, paddle2_vel
    
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0    

#2.1 处理（键盘、鼠标等）事件
def processEvent():
    for event in pygame.event.get():     #返回当前的所有事件           
        if event.type == pygame.QUIT:  #接收到窗口关闭事件                   
            return False                #退出游戏 
        
        elif event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        
    return True   

# 2.2 更新游戏的数据
def update():
    global ball_pos, ball_vel # these are vectors stored as lists
    global   score1, score2
    
    # 更新球
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])
    #上下墙碰撞，水平速度不变，垂直速度相反
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - 1 - BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        
     # 检测挡板是否和球碰撞  
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT and \
                      ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] * 1.1)       #挡板击中球
        else:                                  #挡板没挡住球，对方得分
            ball_init()
            score2 += 1
    elif ball_pos[0] > WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else:
            ball_init()
            score1 += 1
     
# 更新挡板的垂直位置
    if paddle1_pos[1] + paddle1_vel > HALF_PAD_HEIGHT and paddle1_pos[1]  + paddle1_vel < HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    
    if paddle2_pos[1] + paddle2_vel > HALF_PAD_HEIGHT and paddle2_pos[1] + paddle2_vel < HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel       


# ------游戏主函数-----
def game_engine():    
    surface = init()               #1. 初始化pygame和游戏数据
    
     #2. 循环，直到游戏结束
    running = True          
    while running == True: 
        running = processEvent()   #2.1 处理事件
        update()                   #2.2 更新数据
        draw(surface)              #2.3绘制场景
        
    pygame.quit()                  #3.退出程序
 
if __name__ == "__main__":
     game_engine()  