'''
关于event
活动名称写前面，逗号隔开，日/月/年格式输入日期
'''

from tkinter import Tk,Canvas
from datetime import date,datetime
#导入模块
def get_events():
    list_events = []#1
    with open('events.txt') as file:#2
        for line in file:#3
            line = line.rstrip('\n')#4
            current_event = line.split(',')#5
            event_date = datetime.strptime(current_event[1],'%d/%m/%y').date()#6
            current_event[1] = event_date
            list_events.append(current_event)#7
    return list_events

'''
1创建一个空的列表叫做事件列表
2打开一个文本文件
3运行for循环处理文本的每一行数据
4剔除每一行末尾的‘新行’字符（在Python中，\
n表示新行）
5把活动数据从逗号所在分成两部分
6把列表中第二个数据从字符转换为日期；
下面一行把列表第二个数据设为活动日期
（列表的下标从0开始，所以current_event[1] 会转换为一个日期）
7循环结束

'''

'''
>>> from datetime import *
>>> print(date(2007,12,4).weekday())
1
以上三行是IDLE的输入输出
第一句导入模块，*不可省略
用年月日输入日期
返回的数字表示星期几，周一是0，周日是6
所以2表示周二，即2007.12.04是周二
'''

def days_between_dates(date1,date2):
    days_between = str(date1 - date2)
    number_of_days = days_between.split()
    return number_of_days[0]


root = Tk()#创建一个tkinter窗口
c = Canvas(root,width = 800,height=800,bg='black')
c.pack()
c.create_text(100,50,anchor='w',fill='orange',font='Arial 28 bold ',\
                text='My Countdown Calendar')
'''
该部分
第二行创建高800像素，宽800的画布，命名为c
第三行展开画布
第4，5行把文字放在画布上面
文字开始的位置为x100，y50.起始位置在位子文字左边
fill更改颜色

'''
events = get_events()
today = date.today()

vertical_space=100

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1],today)
    display='it is %s days until %s' % (days_until,event_name)
    c.create_text(100,vertical_space,anthor='w',fill='lightblue',\
                  font='Arial 28 bold',\
                  text=display)

    vertical_space=vertical_space+30