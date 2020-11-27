from tkinter import *
import cx_Oracle
import subprocess
import os
import test3

root=Tk()
root.geometry('500x500')
root.title('Login to FBLA Community Service Awards Program')

# Login function
def login():
    # Check if password is correct
    if schema.get() == 'fbla_csa' and passwd.get() == 'John!88954':
        command = "python test3.py"
        root.destroy()
        os.system(command)

        
    else:
        wrong_info = Label(root,text='The username or password is incorrect!')
        wrong_info.place(x=250,y=200)

# Login variables
schema = StringVar()
passwd = StringVar()

# Create and place Label Variables
schema_label = Label(root,text='Username:')
schema_label.place(x=100,y=50)

passwd_label = Label(root,text='Password:')
passwd_label.place(x=100,y=100)

# Create and place Entry Variables
schema_entry = Entry(root,textvariable=schema)
schema_entry.place(x=200,y=50)

passwd_entry = Entry(root,textvariable=passwd)
passwd_entry.config(show='*')
passwd_entry.place(x=200,y=100)

# Place and Create Login Button
login_button = Button(root,text='Login',command=login)
login_button.place(x=250,y=150)
