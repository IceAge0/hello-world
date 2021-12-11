import random
import turtle as t

t.bgcolor('yellow')     #黄色背景
caterpillar=t.Turtle()  #为毛毛虫创造新的乌龟
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)   #游戏开始前不让乌龟游动
caterpillar.penup()
caterpillar.hideturtle()


leaf = t.Turtle()    #画树叶
leaf_shape=((0,0),(14,2),(18,6),\
            (20,20),(6,18),(2,14))   #树叶坐标
t.register_shape('leaf',leaf_shape)  #树叶形状
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False    #判断游戏是否开始
text_turtle = t.Turtle()
text_turtle.write('press space to start',\
                   align='center',\
                   font=('Arial',16,'bold'))#在屏幕上书写文字
text_turtle.hideturtle()  #隐藏乌龟但不会隐藏文字

score_turtle = t.Turtle()   #添加一只乌龟书写分数
score_turtle.hideturtle()
score_turtle.speed(0)        #乌龟在这里固定的位置，以便更新分数

def outside_window():
    #通过比较毛毛虫坐标和墙的位置，判断是否出界
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    #窗口宽度为400，左墙距离中间距离为200，即坐标为-200，同理可得上面四个
    (x,y) = caterpillar.pos()     #一个函数返回两个值（一个元组）
    outside = \
            x < left_wall or \
            x > right_wall or \
            y < bottom_wall or \
            y > top_wall
    return outside    #如果上面有一个条件为TRUE，那么outside为TRUE

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center',font=('Arial',30,'normal'))
    #文字显示在屏幕中间

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50   #距离右边界50像素
    y = (t.window_height() / 2) - 50  #距离上边界50像素
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score),align = 'right', \
                       font = ('Arial',40,'bold'))

def place_leaf():
    leaf.ht()    #hideturtle缩写
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    #把树叶移动到随机坐标位置
    leaf.st()    #showturtle缩写

def start_game():
    global game_started
    if game_started:
        return
    game_started =  True

    #避免二次运行游戏

    score = 0
    text_turtle.clear()
    #去掉屏幕上的文字
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    #乌龟伸长成毛毛虫
    caterpillar.showturtle()
    display_score(score)
    place_leaf()#放第一片树叶

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            #当树叶和毛毛虫之间的距离小于二十像素,毛毛虫就会吃掉叶子
            place_leaf()#更新树叶
            caterpillar_length = caterpillar_length + 1    #这两行会让
            caterpillar.shapesize(1,caterpillar_length,1)  #毛毛虫变长
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    #if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        #if语句用于检查毛毛虫头的方向
        caterpillar.setheading(90)
    #把if语句条件注释掉就可以直接反方向走
def move_down():
    #if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    #if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    #if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game,'space')   #当玩家按下启动键，游戏就启动了
t.onkey(move_up,'Up')#当上移键按下时就能调用
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()













'''
 	class ClassName(object):
 		"""docstring for ClassName"""
 		def __init__(self, arg):
 			super(ClassName, self).__init__()
 			self.arg = arg

'''







'''
 except Exception as e:
 	raise
 else:
 	pass
 finally:
 	pass
'''
