from tkinter import messagebox,simpledialog,Tk
def get_task():
    task = simpledialog.askstring('Task','do youwant to encrypt or decrypt?') #要求用户输入encrypt或decrypt，并把答案保存在task里
    return task     #把task值返回到函数代码里
def get_message():
    message=simpledialog.askstring('massage','enter the secret message:')       
    #要求用户输入一条消息，保存到变量massage里
    return message      #同上
root = Tk()
while True:
    task = get_task()       #确认用户想干嘛
    if task == 'encrypt':  
        message=get_message()   #获取要被加密的信息
        encrypted = swap_letters(message)
        messagebox.showinfo('ciphertext of the secret message is:',encrypted)
        #在一个信息框里显示机密信息
    elif task=='decrypt':
        message=get_message()       #获取要被解密的信息
        decrypted = swap_letters(message)
        messagebox.showinfo=('plaintext of the secret message is:', decrypted)#类似
    else:
        break

root.mainloop()     #让tkinter持续工作

def is_even(number):
	return number%2==0

def get_even_letters (message):
	even_letters=[]
	for counter in range (0,len(message)):
		if is_even (counter):
			even_letters.append(message[counter])
	return even_letters

def get_odd_letters(message):
	odd_letters = []
	for counter in range(0,len(message)):
		if not is_even(counter):
			odd_letters.append(message[counter])
	return odd_letters

def swap_letters(message):
	letter_list=[]
	if not is_even(len(message)):
		message=message+'x'
	even_letters=get_even_letters(message)
	odd_letters=get_odd_letters(message)
	for counter in range(0,int(len(message)/2)):
		letter_list.append(odd_letters[counter])
		letter_list.append(even_letters[counter])
	new_message = ''.join(letter_list)#join函数把保存在列表中的字母合并为字符串
	return new_message

