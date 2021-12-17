from tkinter import *
window = Tk()
window.geometry("335x226")  
window.title("Calculator")
text = Entry(window,font=("arial",20))
text.pack(fill=X,padx=7,pady=7,ipadx=7,ipady=7)

def add(n):
    text.insert(END,n)
def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)
def button_clear():
    text.delete(0, END)

frame = Frame(window)
frame.pack(side=TOP,anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

btn1 = Button(frame1,text="1",width=9,height=2,fg='white',bg='black',command=lambda:add("1"))
btn1.pack(side=LEFT)
btn2 = Button(frame1,text="2",width=9,height=2,fg='white',bg='black',command=lambda:add("2"))
btn2.pack(side=LEFT)
btn3 = Button(frame1,text="3",width=9,height=2,fg='white',bg='black',command=lambda:add("3"))
btn3.pack(side=LEFT)
btnadd = Button(frame1,text="+",width=7,height=2,fg='white',bg='blue',command=lambda:add("+"))
btnadd.pack(side=LEFT)
btnclear = Button(frame1,text="clear",width=7,height=2,fg='white',bg='blue', command=button_clear)
btnclear.pack(side=LEFT)

frame2 = Frame(frame)
frame2.pack()

btn4 = Button(frame2,text="4",width=10,height=2,fg='white',bg='black', command=lambda:add("4"))
btn4.pack(side=LEFT)
btn5 = Button(frame2,text="5",width=10,height=2,fg='white',bg='black', command=lambda:add("5"))
btn5.pack(side=LEFT)
btn6 = Button(frame2,text="6",width=10,height=2,fg='white',bg='black', command=lambda:add("6"))
btn6.pack(side=LEFT)
btnsub = Button(frame2,text="-",width=12,height=2,fg='white',bg='blue', command=lambda:add("-"))
btnsub.pack(side=LEFT)

frame3 = Frame(frame)
frame3.pack()

btn7 = Button(frame3,text="7",width=10,height=2,fg='white',bg='black', command=lambda:add("7"))
btn7.pack(side=LEFT)
btn8 = Button(frame3,text="8",width=10,height=2,fg='white',bg='black', command=lambda:add("8"))
btn8.pack(side=LEFT)
btn9 = Button(frame3,text="9",width=10,height=2,fg='white',bg='black', command=lambda:add("9"))
btn9.pack(side=LEFT)
btnmul = Button(frame3,text="x",width=12,height=2,fg='white',bg='blue', command=lambda:add("*"))
btnmul.pack(side=LEFT)

frame4 = Frame(frame)
frame4.pack()

btnpoint = Button(frame4,text=".",width=9,height=2,fg='white',bg='black', command=lambda:add("."))
btnpoint.pack(side=LEFT)
btnzero = Button(frame4,text="0",width=9,height=2,fg='white',bg='black', command=lambda:add("0"))
btnzero.pack(side=LEFT)
btneq = Button(frame4,text="=",width=7,height=2,fg='white',bg='red', command=lambda:calculate())
btneq.pack(side=RIGHT)
btndiv = Button(frame4,text="/",width=7,height=2,fg='white',bg='blue', command=lambda:add("/"))
btndiv.pack(side=LEFT)
btnmod = Button(frame4,text="%",width=11,height=2,fg='white',bg='blue', command=lambda:add("%"))
btnmod.pack(side=LEFT)

window.mainloop()


