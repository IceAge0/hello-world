from turtle import *
from random import *
from math import *
from tkinter import Toplevel
from tkinter import *

setup(width=0.99, height=0.99, startx=None, starty=None)

def tree(n,l):
    pendown()#下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1,d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            penup()
            #飘落
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画叶子
            pendown()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            penup()
            #返回
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    penup()
    backward(l)#退回

colormode(255)#RGB整数模式
bgcolor(135,124,154)#背景色
colormode(1)#RGB小数模式
ht()#隐藏turtle
speed(10)#速度 1-10渐进，0 最快
tracer(0,0)
penup()#抬笔
backward(100)
left(90)#左转90度
penup()#抬笔
backward(300)#后退300
tree(12,100)#递归7层


#Tk().attributes('-fullscreen', True)

mainloop()
