import tkinter
root=tkinter.Tk()
entry1=tkinter.Entry(root,      #创建单行文本框1
		    show="*",)  #设置显示的文本是*，（即输入任何字母都显示*，适合做密码保护）
entry1.pack()                   #将文本框添加到窗口

entry2=tkinter.Entry(root,
		    show="#",
		    width=50)           #设置文本框宽度
entry2.pack()

entry3=tkinter.Entry(root,
		    bg='red',       #文本框背景颜色
		    fg='blue')      #文本框前景颜色(即输入内容的颜色)
entry3.pack()

entry4=tkinter.Entry(root,
		    selectbackground='red',     #设置选中文本的bg
		    selectforeground='gray')    #设置选中文本的fg
entry4.pack()

entry5=tkinter.Entry(root,
		    state=tkinter.DISABLED)     #禁用文本框
entry5.pack()

edit1=tkinter.Text(root,            #多行文本框
		    selectbackground='red',
		    selectforeground='gray')
edit1.pack()
root.mainloop()
