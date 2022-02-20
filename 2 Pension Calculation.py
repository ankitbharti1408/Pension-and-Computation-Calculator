
from tkinter import *
def divide():
    s4=var4.get()
    if(s4.isdigit()):
        print((float(var4.get()))/(float(2)))
    else:
        print("Please pass a valid number")
def multiply():
    s4=var4.get()
    if(s4.isdigit()):
        print((float(var4.get()))*(float(0.3)))
    else:
        print("Please pass a valid number")
def divide():
    s4=var4.get()
    if(s4.isdigit()):
        print((float(var4.get()))/(float(2)))
    else:
        print("Please pass a valid number")
    
top=Tk()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

l1=Label(top,text="Date of Birth[DD/MM/YYYY]")
l1.place(x=50,y=50)
t1=Entry(top,bd=5,textvariable=var1)
t1.place(x=310,y=50)
l2=Label(top,text="Date of Retirement[DD/MM/YYYY]")
l2.place(x=50,y=100)
t2=Entry(top,bd=5,textvariable=var2)
t2.place(x=310,y=100)
l3=Label(top,text="Total Qualifying Service[Year/Months]")
l3.place(x=50,y=150)
t3=Entry(top,bd=5,textvariable=var3)
t3.place(x=310,y=150)
l4=Label(top,text="Last Month's Emoluments[In Rs.]")
l4.place(x=50,y=200)
t4=Entry(top,bd=5,textvariable=var4)
t4.place(x=310,y=200)


b1=Button(top,text="Basic Pension",command=divide)
b1.place(x=180,y=300)
b2=Button(top,text="Normal Family Pension",command=multiply)
b2.place(x=180,y=320)
b3=Button(top,text="Enhanced Family Pension",command=divide)
b3.place(x=180,y=340)

top.mainloop()

 
 
