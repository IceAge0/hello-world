from tkinter import *
class MainWindow:
	def __init__(self):

		self.frame=Tk()

		self.label_name = Label(self.frame,text='name:')
		self.label_age = Label(self.frame,text='age:')
		self.label_sex = Label(self.frame,text='sex:')

		self.text_name = Text(self.frame,height='1',width=30)
		self.text_age = Text(self.frame,height='1',width=30)
		self.text_sex = Text(self.frame,height='1',width=30)
		#按照网格线排列文本框
		self.label_name.grid(row=0,colum=0)
		self.label_age.grid(row=1,colum=0)
		self.label_sex.grid(row=2,colum=0)

		self.button_ok =Button(self.frame,text='ok',width=10)
		self.button_cancel =Button(self.frame,text='cancel',width=10)



		self.frame.mainloop()

frame = MainWindow()