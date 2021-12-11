from tkinter import HIDDEN,NORMAL,Tk,Canvas
'''
绘图指令用到了x和y坐标，y从上往下变大，x从左往右变大
'''

import random

def change_color():
    pet_color=['SkyBlue1','tomato','yellow','purple','green','orange']
    #这个列表储存屏幕宠物所有可能的颜色
    c.body_color=random.choice(pet_color)#从列表中随机选择另一个颜色
    c.itemconfigure(body,outline=c.body_color,fill=c.body_color)
    c.itemconfigure(ear_left,outline=c.body_color,fill=c.body_color)
    c.itemconfigure(ear_right,outline=c.body_color,fill=c.body_color)
    c.itemconfigure(foot_left,outline=c.body_color,fill=c.body_color)
    c.itemconfigure(foot_right,outline=c.body_color,fill=c.body_color)
    #设置身体，脚，耳朵颜色
    root.after(5000,change_color)#5秒后再次调用

def toggle_eyes():
    current_color=c.itemcget(eye_left,'fill')
    new_color=c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left,'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left,state=new_state)
    c.itemconfigure(pupil_right,state=new_state)
    c.itemconfigure(eye_left,fill=new_color)
    c.itemconfigure(eye_right,fill=new_color)

def blink():
    '''def toggle_left_eye():
        def wink(event):
            toggle_left_eye()
            root.after(250,toggle_left_eye)
        current_color=c.itemconfigure(eye_left,'fill')
        new_color=c.body_color if current_color == 'white' else 'white'
        current_state=c.itemconfigure(pupil_left,'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        c.itemconfigure(pupil_left,state=new_state)
        c.itemconfigure(eye_left,fill=new_color)'''
    toggle_eyes()#闭上眼
    root.after(250,toggle_eyes)#250毫秒后睁眼
    root.after(3000,blink)#3000毫秒后再次眨眼（执行）

def toggle_left_eye():
    #首先程序检查眼睛的颜色，白色表示睁眼状态，蓝色表示闭眼状态
    current_color=c.itemconfigure(eye_left,'fill')
    new_color=c.body_color if current_color == 'white' else 'white'
    #这一行把眼睛的颜色new_color设置为与当前相反的颜色
    current_state=c.itemconfigure(pupil_left,'state')
    #程序会检查眼睛的状态是NORNAL还是HIDDEN
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    #把眼睛的状态设置为相反的状态
    c.itemconfigure(pupil_left,state=new_state)
    c.itemconfigure(pupil_right,state=new_state)
#这两行改变
#眼珠的可见性

    c.itemconfigure(eye_left,fill=new_color)
    c.itemconfigure(eye_right,fill=new_color)
    #这两行改变
#眼睛的填充色

'''def wink(event):
    toggle_left_eye()#会切换一只眼睛的状态
    root.after(250,toggle_left_eye)#挤眼睛
'''
def toggle_pupils():
    #这个代码检查是否处于对眼状态
    if not c.eye_crossed:#如果不是对眼
        c.move(pupil_left,10,-5)
        c.move(pupil_right,-10,-5)#那么这行代码让眼珠向内靠拢
        c.eye_crossed=True#这一行设置变量说明眼珠处于对眼状态
    else:#眼珠已经对眼（否则）
        c.move(pupil_left,-10,5)
        c.move(pupil_right,10,5)
        #这两行代码
#变回正常状态
        c.eye_crossed=False
        #这两行设置标志变量
#说明眼珠处于对眼状态



def cheeky(event):
    toggle_tongue()#伸出舌头
    toggle_pupils()#变成对眼
    hide_happy(event)#隐藏快乐的表情
    root.after(1000,toggle_tongue)#在一秒之后，把舌头缩回去
    root.after(1000,toggle_pupils)#一秒之后对眼消失
    return

def toggle_tongue():
    if not c.tongue_out:#这一行代码检查舌头是否伸出来了
        c.itemconfigure(tongue_tip,state=NORMAL)
        c.itemconfigure(tongue_main,state=NORMAL)
        #如果舌头没有伸出来
#这两行代码会让他伸出来
        c.tongue_out=True
        #这一行设置标志变量，
#说明舌头处于伸出状态
    else:#舌头已经伸出（否则）
        c.itemconfigure(tongue_tip,state=HIDDEN)
        c.itemconfigure(tongue_main,state=HIDDEN)#这两行代码再次隐藏舌头
        c.tongue_out = False#这一行设置标志变量，说明舌头诶没有伸出

def show_happy(event):
    if (20<=event.x <=350) and (20 <= event.y <=350):
    #if语句检查鼠标是否在宠物上面
    #event.x  event.y是鼠标坐标
        c.itemconfigure(cheek_left,state=NORMAL)
        c.itemconfigure(cheek_right,state=NORMAL)#显示粉嘟嘟的脸
        c.itemconfigure(mouth_happy,state=NORMAL)#显示快乐的嘴巴
        c.itemconfigure(mouth_normal,state=HIDDEN)#隐藏正常的嘴巴
        c.itemconfigure(mouth_sad,state=HIDDEN)#隐藏悲伤的嘴巴
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left,state=HIDDEN)
    c.itemconfigure(cheek_right,state=HIDDEN)#隐藏粉红色的面颊
    c.itemconfigure(mouth_happy,state=HIDDEN)#隐藏快乐的嘴巴
    c.itemconfigure(mouth_normal,state=NORMAL)#显示平常的嘴巴
    c.itemconfigure(mouth_sad,state=HIDDEN)#隐藏悲伤的嘴巴
    return

def sad():
    if c.happy_level == 0:#检查c.happy_level的值等于0时，隐藏快乐和正常表情
        c.itemconfigure(mouth_happy,state=HIDDEN)
        c.itemconfigure(mouth_normal,state=HIDDEN)
        c.itemconfigure(mouth_sad,state=NORMAL)#设为悲伤
    else:
        c.happy_level-=1#把c.happy_level的值减去1
    root.after(5000,sad)#重置值



root=Tk()
c=Canvas(root,width=400,height=400)
c.configure(bg='dark blue',highlightthickness=0)

c.body_color='SkyBlue1'
#把身体的颜色储存在变量c.body_color中，就不需要总是录入Skyblue了
body=c.create_oval(35,20,365,350,outline=c.body_color,\
    fill=c.body_color)
ear_left=c.create_polygon(75,80,75,10,165,70,\
    outline=c.body_color,fill=c.body_color)
ear_right=c.create_polygon(255,45,325,10,320,70,\
    outline=c.body_color,fill=c.body_color)
foot_left=c.create_oval(65,320,145,360,\
    outline=c.body_color,fill=c.body_color)
foot_right=c.create_oval(250,320,330,360,\
    outline=c.body_color,fill=c.body_color)
eye_left=c.create_oval(130,110,160,170,\
    outline='black',fill='white')
pupil_left=c.create_oval(140,145,150,155,\
    outline='black',fill='black')
eye_right=c.create_oval(230,110,260,170,\
    outline='black',fill='white')
pupil_right=c.create_oval(240,145,250,155,\
    outline='black',fill='black')
#为了眨眼，把眼睛涂上天蓝色，同时眼珠消失不见。这样也便于检查
mouth_normal=c.create_line(170,250,200,272,230,250,\
    smooth=1,width=2,state=NORMAL)
#这几对坐标定义了嘴巴的起始位置，中间位置和结束位置
#嘴巴是一个光滑的线条，有两个像素那么粗
mouth_happy=c.create_line(170,250,200,282,230,250,\
    smooth=1,width=2,state=HIDDEN)#创建快乐的嘴巴
mouth_sad=c.create_line(170,250,200,232,230,250,\
    smooth=1,width=2,state=HIDDEN)#创建悲伤的嘴巴
tongue_main=c.create_rectangle(170,250,230,290,\
    outline='red',fill='red',state=HIDDEN)
tongue_tip=c.create_oval(170,285,230,300,\
    outline='red',fill='red',state=HIDDEN)
cheek_left=c.create_oval(70,180,120,230,\
    outline='pink',fill='pink',state=HIDDEN)
cheek_right=c.create_oval(280,180,330,230,\
    outline='pink',fill='pink',state=HIDDEN)#这两行创建粉脸
#所有c.开头的命令都与画布有关
c.pack()
c.bind('<Motion>',show_happy)#这一行指令把移动的鼠标指针和快乐脸联系起来
c.bind('<Leave>',hide_happy)#把leave事件和hide_happy事件联系起来
c.bind('<Double-1>',cheeky)#<Double- 1>是Tkinter的事件名称，表示在窗口中双击了鼠标
#c.bind('<Double-1>',wink)#把cheeky()改成wink()
c.happy_level=10#屏幕宠物在开始的时候幸福值为10
c.eye_crossed=False#这些是用于舌头和眼珠的标志变量
c.tongue_out=False
root.after(1000,blink)#等待一秒后执行blink
root.after(5000,sad)
root.after(5000,change_color)
root.mainloop()
#检测输入事件函数，包括点击鼠标等


#body=c.create_oval(15,20,395,350,outline=c.body_color,fill=c.body_color)
#设置一段代码，可以模拟喂养宠物
#改变宠物身体椭圆大小
#清理便便，同喂食
