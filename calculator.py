from tkinter import *

calculator=Tk()
calculator.title('Calculator')

e=Entry(calculator,width=55,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def click_number(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clickAdd():
    global math
    global first_num
    math='Add'
    first_num=e.get()
    e.delete(0,END)

def clickSub():
    global math
    global first_num
    math='Sub'
    first_num=e.get()
    e.delete(0,END)

def clickMul():
    global math
    global first_num
    math='Mul'
    first_num=e.get()
    e.delete(0,END)

def clickDiv():
    global math
    global first_num
    math='Div'
    first_num=e.get()
    e.delete(0,END)

def click_equal():
    second_num=e.get()
    e.delete(0,END)
    if math == 'Add':
        e.insert(0,int(first_num)+int(second_num))
    elif math == 'Sub':
        e.insert(0,int(first_num)-int(second_num))
    elif math == 'Mul':
        e.insert(0,int(first_num)*int(second_num))
    elif math == 'Div':
        e.insert(0,int(first_num)/int(second_num))

def click_clear():
    e.delete(0,END)

# button
button1=Button(calculator,text='1',padx=40,pady=20,command=lambda:click_number(1))
button2=Button(calculator,text='2',padx=40,pady=20,command=lambda:click_number(2))
button3=Button(calculator,text='3',padx=40,pady=20,command=lambda:click_number(3))

button4=Button(calculator,text='4',padx=40,pady=20,command=lambda:click_number(4))
button5=Button(calculator,text='5',padx=40,pady=20,command=lambda:click_number(5))
button6=Button(calculator,text='6',padx=40,pady=20,command=lambda:click_number(6))

button7=Button(calculator,text='7',padx=40,pady=20,command=lambda:click_number(7))
button8=Button(calculator,text='8',padx=40,pady=20,command=lambda:click_number(8))
button9=Button(calculator,text='9',padx=40,pady=20,command=lambda:click_number(9))

button0=Button(calculator,text='0',padx=40,pady=20,command=lambda:click_number(0))
buttonAdd=Button(calculator,text='+',padx=38.5,pady=20,command=clickAdd,fg='white',bg='black')
buttonSub=Button(calculator,text='-',padx=40,pady=20,command=clickSub,fg='white',bg='black')
buttonMul=Button(calculator,text='*',padx=40,pady=20,command=clickMul,fg='white',bg='black')
buttonDiv=Button(calculator,text='/',padx=40,pady=20,command=clickDiv,fg='white',bg='black')


buttonClear=Button(calculator,text='C',padx=39,pady=20,command=click_clear)
buttonEqual=Button(calculator,text='=',padx=40,pady=20,command=click_equal)

#button placement
#number
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)

buttonEqual.grid(row=4,column=2)
buttonClear.grid(row=4,column=1)
#mathematics signs
buttonAdd.grid(row=1,column=3)
buttonSub.grid(row=2,column=3)
buttonMul.grid(row=3,column=3)
buttonDiv.grid(row=4,column=3)


calculator.mainloop()
