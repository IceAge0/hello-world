import tkinter
root=tkinter.Tk()								#创建主窗口
button1=tkinter.Button(root,					#创建按钮1
					anchor = tkinter.E,#设置文本对齐方式
					text="Button1",#设置按钮上显示的文本
					width = 30,#高度
					height=7)#宽度
button1.pack()#将按钮添加到窗口

button2=tkinter.Button(root,
					text="Button2",
					bg='blue')
button2.pack()

button3=tkinter.Button(root,
					text="Button3",
					width = 12,
					height=1)
button3.pack()

button4=tkinter.Button(root,
					text="Button4",
					width = 40,
					height=7,
					state=tkinter.DISABLED)
button4.pack()
root.mainloop()