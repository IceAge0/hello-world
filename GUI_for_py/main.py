'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''


from tkinter import *
root=Tk()
root.title('hello,py')
root.geometry('300x200')

Label(root,text='xiaoxun',font=('Arial',20)).pack()
rfrm = Frame(root)
#左侧
frm_L=Frame(rfrm)
Label(frm_L,text='houde',font=('Arial',15)).pack(side=TOP)
Label(frm_L,text='boxue',font=('Arial',15)).pack(side=TOP)
frm_L.pack(side=LEFT)

frm_R=Frame(rfrm)
Label(frm_R,text='houde',font=('Arial',15)).pack(side=TOP)
Label(frm_R,text='boxue',font=('Arial',15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

rfrm.pack()

root.mainloop()
