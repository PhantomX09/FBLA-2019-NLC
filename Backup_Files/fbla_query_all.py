from tkinter import *
import cx_Oracle

connstr = 'fbla_csa/fbla_csa@fbladb1'

labels = []
buttons = []

def destroy_all():
   for label in labels:
      label.destroy()

   for button in buttons:
      button.destroy()
      
#def clear_frame(frame):
#   frame.grid_forget()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def query_student():
   destroy_all()
   #clear_button1 = Button(root, text='Clear Workspace',command=destroy_all)
   #clear_button1.grid(row=0,column=10)   
   #buttons.append(clear_button1)
   conn1 = cx_Oracle.connect(connstr)
   cur1 = conn1.cursor()
   cur1.execute("select * from student")
   result1 = cur1.fetchall()
   for index1, x1 in enumerate(result1):
      num1 = 0
      for y1 in x1: 
         lookup_label = Label(root, text=y1)
         labels.append(lookup_label)
         lookup_label.grid(row=index1,column=num1)
         num1 += 1

def query_chapter():
   destroy_all()
   #clear_button2 = Button(root, text='Clear Workspace',command=destroy_all)
   #clear_button2.grid(row=0,column=10)
   #buttons.append(clear_button2)
   conn2 = cx_Oracle.connect(connstr)
   cur2 = conn2.cursor()
   cur2.execute('select * from chapter')
   result2 = cur2.fetchall()
   for index2, x2 in enumerate(result2):
      num2 = 0
      for y2 in x2:
         chap_label = Label(root, text=y2)
         labels.append(chap_label)
         chap_label.grid(row=index2,column=num2)
         num2 += 1
#         clear_button = Button(root, text='Clear Workspace', command=lambda: clear_button.grid_remove())
#         clear_button.place(x=900,y=200)

def query_progcat():
   destroy_all()
   #clear_button3 = Button(root, text='Clear Workspace',command=destroy_all)
   #clear_button3.grid(row=0,column=10)
   #buttons.append(clear_button3)
   conn3 = cx_Oracle.connect(connstr)
   cur3 = conn3.cursor()
   cur3.execute('select * from program_category')
   result3 = cur3.fetchall()
   for index3, x3 in enumerate(result3):
      num3 = 0
      for y3 in x3:
         prog_label = Label(root, text=y3)
         labels.append(prog_label)
         prog_label.grid(row=index3,column=num3)
         num3 += 1

def query_csa():
   destroy_all()
   #clear_button4 = Button(root, text='Clear Workspace',command=destroy_all)
   #clear_button4.grid(row=0,column=15)
   #buttons.append(clear_button4)
   conn4 = cx_Oracle.connect(connstr)
   cur4 = conn4.cursor()
   cur4.execute('select * from community_service')
   result4 = cur4.fetchall()
   for index4, x4 in enumerate(result4):
      num4 = 0
      for y4 in x4:
         csa_label = Label(root, text=y4)
         labels.append(csa_label)
         csa_label.grid(row=index4,column=num4)
         num4 += 1

def query_csa_hour():
   destroy_all()
   #clear_button5 = Button(root, text='Clear Workspace',command=destroy_all)
   #clear_button5.grid(row=0,column=8)
   #buttons.append(clear_button5)
   conn5 = cx_Oracle.connect(connstr)
   cur5 = conn5.cursor()
   cur5.execute('select * from csa_hour')
   result5 = cur5.fetchall()
   for index5, x5 in enumerate(result5):
      num5 = 0
      for y5 in x5:
         hour_label = Label(root, text=y5)
         labels.append(hour_label)
         hour_label.grid(row=index5,column=num5)
         num5 += 1

def query_award_det():
   destroy_all()
   conn6 = cx_Oracle.connect(connstr)
   cur6 = conn6.cursor()
   cur6.execute('select * from program_category')
   result6 = cur6.fetchall()
   print(enumerate(result6))
   for index6, x6 in enumerate(result6):
      num6 = 0
      for y6 in x6:
         query_label = Label(root, text=y6)
         labels.append(query_label)
         query_label.grid(row=index6,column=num6)
         num6 += 1
