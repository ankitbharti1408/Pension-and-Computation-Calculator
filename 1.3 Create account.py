from tkinter import *
import mysql.connector
import tkinter.messagebox


def create():
    e = empid_value.get()
    p = password_value.get()
    m = mobile_value.get()

    if e == '' or p == '' or m == '':
        tkinter.messagebox.showinfo("!!Warning!!", " Fill all entries")
    else:
        tkinter.messagebox.showinfo("Successful", "account created successfully")
        pension = mysql.connector.connect(host="localhost", user="root", password="Ab#14081999", database="EmployeePensionCalculatorDatabase")
        if (pension):
            db = pension.cursor()
            x = "INSERT INTO logintable (empid, password, mobile) VALUES(%s,%s,%s)"
            y = (e, p, m)
            db.execute(x, y)
            pension.commit()


root = Tk()
root.geometry("500x500")
root.configure(bg="aqua")
root.minsize(700, 500)
root.maxsize(1366, 768)
root.title("Registration for pension calculator")

Label(root, text="CREATE ACCOUNT ", width=21, bg="aqua", font=("Century 35 bold")).place(x=50, y=53)

empid_value = StringVar()
password_value = StringVar()
mobile_value = StringVar()


empid = Label(root, text="Employee Id", width=15, bg="aqua", font=("Century 16 bold"))
empid.place(x=70, y=140)

empid_entry = Entry(root, width=28, bd=5, textvariable=empid_value)
empid_entry.place(x=270, y=140)

password = Label(root, text="Password", width=15, bg="aqua", font=("Century 16 bold"))
password.place(x=70, y=190)

password_entry = Entry(root, width=28, bd=5, textvariable=password_value)
password_entry.place(x=270, y=190)

mobile = Label(root, text="Mobile Number", width=15, bg="aqua", font=("Century 16 bold"))
mobile.place(x=70, y=240)

mobile_entry = Entry(root, width=28, bd=5, textvariable=mobile_value)
mobile_entry.place(x=270, y=240)

Button(root, text='create account', width=20, bg='indigo', fg='white', command=create).place(x=290, y=290)

root.mainloop()