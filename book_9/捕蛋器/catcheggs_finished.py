from itertools import cycle
from random import randrange
from tkinter import Canvas,Tk,messagebox,font

canvas_width = 800
canvas_height = 600

root = Tk()   #创建一个窗口
c = Canvas(root,width = canvas_width,height = canvas_height,\
    background = 'deep sky blue')
    #天蓝色画布，尺寸为800*400像素
c.create_rectangle(-5,canvas_height - 100,canvas_width+5,\
    canvas_height+5,fill='sea green',width=0)
    #创建草地
c.create_oval(-80,-80,120,120,fill= 'orange',width=0)
    #创建太阳
c.pack()   #pack（）通知程序画一个主窗口和里面的所有东西


color_cycle =cycle(['light blue','light green',\
    'light pink','light yellow','light cyan'])
    #cycle()函数让蛋在每种颜色之间轮换
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 90
egg_interval = 4000     #每隔4000毫秒出现一个新蛋
difficulty_factor = 0.95   #每次抓蛋成功之后，
                #蛋的下落速度和间隔时间改变量

catcher_color = 'blue'
catcher_width = 100
catcher_height = 100        #100圆，500圆锥曲线
#用于绘制圆的高度，圆用来绘制曲线
catcher_start_x = canvas_width/2- catcher_width/2
catcher_start_y = canvas_height - catcher_height-20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x,catcher_start_y,\
    catcher_start_x2,catcher_start_y2,\
    start = 200,extent = 140,\
    style = 'arc',outline = catcher_color,\
                       width = 3)
    #在圆的200度开始画圆弧，画出为140度的圆弧，画捕蛋器

game_font = font.nametofont('TkFixedFont')  #选择计算机字体
game_font.config(size = 18)  #确定文字大小

score = 0
score_text = c.create_text(10,10,anchor = 'nw',font=game_font,\
    fill='darkblue',text='score:'+str(score))

lives_remaining = 3   #三条命
lives_text = c.create_text(canvas_width-10,10,anchor='ne',\
    font= game_font,fill='darkblue',\
    text='lives '+str(lives_remaining))

eggs = []   #记录所有蛋的列表

def create_egg():
    x = randrange(10,740)      #选择随机位置
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,\
        fill=next(color_cycle),width=0)
    #创建一个椭圆
    eggs.append(new_egg)  #图形被添加到蛋的列表里
    root.after(egg_interval,create_egg)
    #每隔egg_interval秒以后，再次调用这个函数create_egg

def move_eggs():
    for egg in eggs:#循环经过每一个蛋
        (egg_x,egg_y,egg_x2,egg_y2)= c.coords(egg)
        #获取每一个蛋的坐标
        c.move(egg,0,10)
        #原数为c.move(egg,0,10)，改变速度（原来是90）和move，能看上去更顺滑
        #但是速度变小之后会造成值差异变大，使游戏持续时间变短
        if egg_y2 > canvas_height :   #蛋是否到达底部
            egg_dropped(egg)          #如果是，
            #用egg_dropped(egg)处理坠地的蛋
    root.after(egg_speed,move_eggs)
    #egg_speed变量中记录了一个时间，
    #经历该时间长度之后，再次调用这个函数

def egg_dropped(egg):
    eggs.remove(egg) #这个蛋从列表中移除
    c.delete(egg)   #这个蛋会从画布中消失
    lose_a_life()   #调用函数
    if lives_remaining == 0:
        messagebox.showinfo('gameover','final score:' + \
            str(score))
            #如果没命了，通知结果
        root.destroy()#游戏结束（缩进在if里）

def lose_a_life():
    global lives_remaining   #全局变量，因为函数需要修改它的值
    lives_remaining -= 1    #失去一条命
    c.itemconfigure(lives_text,text='lives'+str(lives_remaining))
    #更新屏幕上文字，显示最新生命值
def check_catch():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = \
    c.coords(catcher)
    #获取捕蛋器坐标
    for egg in eggs:
        (eggs_x,eggs_y,eggs_x2,eggs_y2)= c.coords(egg)
        #获取蛋坐标
        if catcher_x < eggs_x and eggs_x2 <catcher_x2 and catcher_y2- eggs_y2 < 40:
            #蛋是否落入捕蛋器的水平与垂直位置中
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)  #加分
    root.after(100,check_catch)  #100毫秒后再次调用函数

def increase_score(points):
    global score,egg_speed,egg_interval
    score += points   #增加分数
    egg_speed=int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text,text = 'score:' + str(score))
    #更新显示分数的文字

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1>0:  #是否碰到左侧墙壁
        c.move(catcher,-20,0)  #如果没有，继续移动捕蛋器

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2<canvas_width:#同上
        c.move(catcher,20,0)

c.bind('<Left>',move_left)
c.bind('<Right>',move_right)
#当按键被按下时，这几行代码调用移动控制函数
c.focus_set()

root.after(1000,create_egg)
root.after(1000,move_eggs)
root.after(1000,check_catch)
root.mainloop()


import time

from pygame import mixer

mixer.init()
beep = mixer.Sound(bgmusic.mp3)
beep.play()
time.sleep(5)