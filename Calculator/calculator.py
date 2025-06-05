import tkinter as tk
from tkinter import *

#window
root=Tk()
root.title("Calculator")
root.geometry('268x380')
root.config(bg="white",borderwidth="2",relief="solid")
display=StringVar()
displaystr=""

def btnclick(num):
    global displaystr
    display.set(displaystr+str(num))
    displaystr=displaystr+str(num)

def result():
    global displaystr
    try:
        res=eval(displaystr)
        display.set(res)
        displaystr=str(res)
    except (SyntaxError,ArithmeticError):
        display.set("Error")
        displaystr=""

def clrscreen():
    global displaystr
    displaystr=""
    display.set("")

def btnback():
    global displaystr
    displaystr=displaystr[:-1]
    display.set(displaystr)

# display Screen
w=Label(root,textvariable=display,bg="light green",fg="black",height="3",width=22,justify="right",borderwidth="3",relief="solid")
w.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
w.config(font=("Arial","15"))

# Buttons
# row 1
buttonclr=tk.Button(root,text="AC",bg="red4",fg="white",width="7",height="3",command=lambda:clrscreen())
buttonclr.config(font=("Arial","8","bold"))
buttonclr.grid(row=1,column=0,pady=1,padx=1)

buttonback=tk.Button(root,text="<",bg="gold3",fg="black",width="7",height="3",command=lambda:btnback())
buttonback.config(font=("Arial","8","bold"))
buttonback.grid(row=1,column=3,pady=1,padx=1)

# row 2
button7=tk.Button(root,text="7",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(7))
button7.config(font=("Arial","8","bold"))
button7.grid(row=2,column=0,pady=1,padx=1)

button8=tk.Button(root,text="8",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(8))
button8.config(font=("Arial","8","bold"))
button8.grid(row=2,column=1)

button9=tk.Button(root,text="9",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(9))
button9.config(font=("Arial","8","bold"))
button9.grid(row=2,column=2)

buttondiv=tk.Button(root,text="/",bg="gold",fg="black",width="7",height="3",command=lambda:btnclick("/"))
buttondiv.config(font=("Arial","8","bold"))
buttondiv.grid(row=2,column=3)

# row 3
button4=tk.Button(root,text="4",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(4))
button4.config(font=("Arial","8","bold"))
button4.grid(row=3,column=0,pady=1,padx=1)

button5=tk.Button(root,text="5",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(5))
button5.config(font=("Arial","8","bold"))
button5.grid(row=3,column=1)

button6=tk.Button(root,text="6",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(6))
button6.config(font=("Arial","8","bold"))
button6.grid(row=3,column=2)

buttonmul=tk.Button(root,text="X",bg="gold",fg="black",width="7",height="3",command=lambda:btnclick("*"))
buttonmul.config(font=("Arial","8","bold"))
buttonmul.grid(row=3,column=3)

# row 4
button1=tk.Button(root,text="1",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(1))
button1.config(font=("Arial","8","bold"))
button1.grid(row=4,column=0,pady=1,padx=1)

button2=tk.Button(root,text="2",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(2))
button2.config(font=("Arial","8","bold"))
button2.grid(row=4,column=1)

button3=tk.Button(root,text="3",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(3))
button3.config(font=("Arial","8","bold"))
button3.grid(row=4,column=2)

buttonsub=tk.Button(root,text="-",bg="gold",fg="black",width="7",height="3",command=lambda:btnclick("-"))
buttonsub.config(font=("Arial","8","bold"))
buttonsub.grid(row=4,column=3)

# row 5
button0=tk.Button(root,text="0",bg="black",fg="white",width="7",height="3",command=lambda:btnclick(0))
button0.config(font=("Arial","8","bold"))
button0.grid(row=5,column=0,pady=1,padx=1)

buttondec=tk.Button(root,text=".",bg="gold",fg="black",width="7",height="3",command=lambda:btnclick("."))
buttondec.config(font=("Arial","8","bold"))
buttondec.grid(row=5,column=1)

buttoneq=tk.Button(root,text="=",bg="chocolate1",fg="white",width="7",height="3",command=result)
buttoneq.config(font=("Arial","8","bold"))
buttoneq.grid(row=5,column=2)

buttonadd=tk.Button(root,text="+",bg="gold",fg="black",width="7",height="3",command=lambda:btnclick("+"))
buttonadd.config(font=("Arial","8","bold"))
buttonadd.grid(row=5,column=3)


root.mainloop()