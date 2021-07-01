from tkinter import *
root = Tk()
root.title('Calculator GUI')

entry = Entry(root,width=101,borderwidth=22,bg='black',fg='white')
entry.grid(row=0,column=0,columnspan=15)
def button(num):
    save=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(save)+str(num))

def button_clear():
    entry.delete(0,END)

def button_add():
    save1=entry.get()
    entry.delete(0,END)
    global num
    num=int(save1)
    global operation
    operation='addition'

def button_sub():
    save1=entry.get()
    entry.delete(0,END)
    global num
    num=int(save1)
    global operation
    operation='subtraction'

def button_mul():
    save1=entry.get()
    entry.delete(0,END)
    global num
    num=int(save1)
    global operation
    operation='multiplication'

def button_div():
    save1=entry.get()
    entry.delete(0,END)
    global num
    num=int(save1)
    global operation
    operation='division'

def button_power():
    save1=entry.get()
    entry.delete(0,END)
    global num
    num=int(save1)
    global operation
    operation='power'

def button_equal():
    save2=entry.get()
    entry.delete(0,END)
    if operation == 'addition':
        entry.insert(0,int(num)+int(save2))
    if operation == 'subtraction':
        entry.insert(0,int(num)-int(save2))
    if operation == 'multiplication':
        entry.insert(0,int(num)*int(save2))
    if operation == 'division':
        entry.insert(0,int(num)/int(save2))
    if operation == 'power':
        entry.insert(0,int(num)**int(save2))  


button1 = Button(root,text='1',bg='black',fg='white',padx=58,pady=25,command=lambda:button(1)).grid(row=1,column=0)
button2 = Button(root,text='2',bg='black',fg='white',padx=57,pady=25,command=lambda:button(2)).grid(row=1,column=1)
button3 = Button(root,text='3',bg='black',fg='white',padx=58,pady=25,command=lambda:button(3)).grid(row=1,column=2)
button4 = Button(root,text='4',bg='black',fg='white',padx=59,pady=25,command=lambda:button(4)).grid(row=1,column=3)
button5 = Button(root,text='5',bg='black',fg='white',padx=57,pady=25,command=lambda:button(5)).grid(row=1,column=4)
button6 = Button(root,text='6',bg='black',fg='white',padx=58,pady=25,command=lambda:button(6)).grid(row=2,column=0)
button7 = Button(root,text='7',bg='black',fg='white',padx=57,pady=25,command=lambda:button(7)).grid(row=2,column=1)
button8 = Button(root,text='8',bg='black',fg='white',padx=58,pady=25,command=lambda:button(8)).grid(row=2,column=2)
button9 = Button(root,text='9',bg='black',fg='white',padx=59,pady=25,command=lambda:button(9)).grid(row=2,column=3)
button0 = Button(root,text='0',bg='black',fg='white',padx=57,pady=25,command=lambda:button(0)).grid(row=2,column=4)
button_clear = Button(root,text='clear',bg='black',fg='white',padx=309,pady=25,command=button_clear).grid(row=3,column=0,columnspan=25)
button_add = Button(root,text='+',bg='black',fg='white',padx=57,pady=25,command=button_add).grid(row=4,column=0)
button_sub = Button(root,text='-',bg='black',fg='white',padx=57,pady=25,command=button_sub).grid(row=4,column=1)
button_mul = Button(root,text='*',bg='black',fg='white',padx=58,pady=25,command=button_mul).grid(row=4,column=2)
button_div = Button(root,text='/',bg='black',fg='white',padx=59,pady=25,command=button_div).grid(row=4,column=3)
button_power = Button(root,text='**',bg='black',fg='white',padx=55,pady=25,command=button_power).grid(row=4,column=4)
button_equal = Button(root,text='=',bg='black',fg='white',padx=318,pady=25,command=button_equal).grid(row=5,column=0,columnspan=25)
button_exit = Button(root,text='exit',bg='black',fg='white',padx=313,pady=25,command=root.quit).grid(row=6,column=0,columnspan=25)
root.mainloop()