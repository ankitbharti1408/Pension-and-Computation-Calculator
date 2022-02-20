from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector
root=Tk()
root.geometry("600x300")
def validate():
    pension = mysql.connector.connect(host="localhost", user="root", password="Ab#14081999", database="EmployeePensionCalculatorDatabase")
    if(pension):
        db = pension.cursor()
        data ="SELECT * FROM logintable WHERE empid = '"+v1.get()+"' AND password = '"+v2.get()+"' AND mobile = '"+v3.get()+"'"
        db.execute(data)
        result = db.fetchall()
        if(result == []):
            MessageBox.showinfo("Warning", "Login Failed, Fill correct Employee id, Password and Mobile Number ")
        else:
            MessageBox.showinfo("Successfully", "logged in")

root.configure(bg="light blue")
title=Label(root,text="PENSION CALCULATOR",fg="black",bg="light blue",font=("bold",19))
title.place(x=90,y=30)
username=Label(root,text="Employee ID",fg="black",bg="light blue",font=("bold",13))
username.place(x=100,y=80)
password=Label(root,text="Password",fg="black",bg="light blue",font=("bold",13))
password.place(x=100,y=110)
mobile=Label(root,text="Mobile Number",fg="black",bg="light blue",font=("bold",13))
mobile.place(x=100,y=140)

v1 = StringVar()
t_username=Entry(textvariable=v1)
t_username.place(x=220,y=80)

v2 = StringVar()
t_pwd=Entry(textvariable=v2)
t_pwd.place(x=220,y=110)

v3 = StringVar()
t_mob=Entry(textvariable=v3)
t_mob.place(x=220,y=140)

submit=Button(root,text="Login",  command=validate)
submit.place(x=220,y=170)
root.mainloop()
