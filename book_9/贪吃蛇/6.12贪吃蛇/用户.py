from tkinter import messagebox,simpledialog,Tk
def get_task():
    task = simpledialog.askstring('Task','do youwant to encrypt or decrypt?') #要求用户输入encrypt或decrypt，并把答案保存在task里
    return task     #把task值返回到函数代码里
def get_message:
    message=simpledialog.askstring('massage','enter the secret message:')       
    #要求用户输入一条消息，保存到变量massage里
    return message      #同上
root = Tk()
while True:
    task = get_task()       #确认用户想干嘛
    if task == 'encrypt':  
        message=get_message()   #获取要被加密的信息
        messagebox.showinfo('message to encrypt is:',message)
        #在一个信息框里显示机密信息
    elif task=='decrypt':
        message=get_message()       #获取要被解密的信息
        messagebox.showinfo=('message to decrypt is'message)#类似
    else:
        break

root.mainloop()     #让tkinter持续工作