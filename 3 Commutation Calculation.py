
from tkinter import *

def multiply():
    s1,s2=var1.get(),var2.get()
    if(s1.isdigit() and s2.isdigit()):
        print((float(var1.get()))*(((float(var2.get()))/(float(100)))* (float(12))))
    else:
        print("Please pass a valid number")
def sub():
    s1,s2=var1.get(),var2.get()
    if(s1.isdigit() and s2.isdigit()):
        print(((float(var1.get()))/(float(2)))- ((float(var1.get()))*(((float(var2.get()))/(float(100)))* (float(12)))))
    else:
        print("Please pass a valid number")
    
top=Tk()
var1=StringVar()
var2=StringVar()

l1=Label(top,text="Basic Pension")
l1.place(x=50,y=50)
t1=Entry(top,bd=5,textvariable=var1)
t1.place(x=310,y=50)
l2=Label(top,text="Pension to be Commuted(in %)[Maximum 40%]")
l2.place(x=50,y=100)
t2=Entry(top,bd=5,textvariable=var2)
t2.place(x=310,y=100)

b1=Button(top,text="Amount of Pension Commuted",command=multiply)
b1.place(x=180,y=150)
b2=Button(top,text="Reduced monthly Pension after commutation",command=sub)
b2.place(x=180,y=170)
top.mainloop()

