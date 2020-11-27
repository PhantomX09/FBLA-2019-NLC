from tkinter import *
import cx_Oracle

connstr = 'fbla_csa/fbla_csa@fbladb1'

labels = []
buttons = []
tboxes = []
dropdowns = []

def destroy_all():
   for label in labels:
      label.destroy()

   for button in buttons:
      button.destroy()

   for tbox in tboxes:
      tbox.destroy()

   for dropdowin in dropdowns:
      dropdown.destroy()     


def query_student(root):
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

def query_chapter(root):
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

def query_progcat(root):
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

def query_csa(root):
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

def query_csa_hour(root):
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

def query_award_det(root):
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

def add_student(root):
   destroy_all()

   def register_student():
      conn7 = cx_Oracle.connect(connstr)
      cur7 = conn7.cursor()
      command1 = f"""
            insert into student values ({sid.get()},'{fname.get()}',
            '{mname.get()}','{lname.get()}',
            '{grade.get()}','{school_name.get()}','{chap_id.get()}',
            '{gender.get()}','{dob.get()}')"""
      print(command1)
      cur7.execute(command1)
      conn7.commit()
      cur7.close()
   
   # Variables
   global gender
   sid = IntVar()
   fname = StringVar()
   mname = StringVar()
   lname = StringVar()
   grade = IntVar()
   school_name = StringVar()
   chap_id = IntVar()
   gender = StringVar()
   dob = StringVar()

   GRADES = [9,10,11,12]
   GENDER = ['M','F']
   
   # Label Variables
   title = Label(root, text='Add New Student')
   labels.append(title)
   title.place(x=650,y=0)
   
   sid_text = Label(root, text='Student:')
   labels.append(sid_text)
   sid_text.place(x=550,y=50)
   
   fname_text = Label(root, text='First Name:')
   labels.append(fname_text)
   fname_text.place(x=550,y=100)
   
   mname_text = Label(root,text='Middle Name:')
   labels.append(mname_text)
   mname_text.place(x=550,y=150)
   
   lname_text = Label(root,text='Last Name:')
   labels.append(lname_text)
   lname_text.place(x=550,y=200)
   
   grade_text = Label(root,text='Grade:')
   labels.append(grade_text)
   grade_text.place(x=550,y=250)

   school_name_text = Label(root,text='School Name:')
   labels.append(school_name_text)
   school_name_text.place(x=550,y=300)

   chap_id_text = Label(root,text='Chapter ID:')
   labels.append(chap_id_text)
   chap_id_text.place(x=550,y=350)

   gender_text = Label(root,text='Gender:')
   labels.append(gender_text)
   gender_text.place(x=550,y=400)

   dob_text = Label(root,text='Date of Birth (DD/MM/YYYY):')
   labels.append(dob_text)
   dob_text.place(x=550,y=450)

   # Entry Variables
   sid_entry = Entry(textvariable=sid,width=20)
   tboxes.append(sid_entry)
   sid_entry.place(x=550,y=75)

   fname_entry = Entry(textvariable=fname,width=20)
   tboxes.append(fname_entry)
   fname_entry.place(x=550,y=125)

   mname_entry = Entry(textvariable=mname,width=20)
   tboxes.append(mname_entry)
   mname_entry.place(x=550,y=175)

   lname_entry = Entry(textvariable=lname,width=20)
   tboxes.append(lname_entry)
   lname_entry.place(x=550,y=225)

   grade_entry = OptionMenu(root,grade,*GRADES)
   tboxes.append(grade_entry)
   grade_entry.place(x=550,y=275)

   school_entry = Entry(textvariable=school_name,width=20)
   tboxes.append(school_entry)
   school_entry.place(x=550,y=325)

   chap_id_entry = Entry(textvariable=chap_id,width=20)
   tboxes.append(chap_id_entry)
   chap_id_entry.place(x=550,y=375)

   gender_entry = OptionMenu(root,gender,*GENDER)
   tboxes.append(gender_entry)
   gender_entry.place(x=550,y=425)

   dob_entry = Entry(textvariable=dob,width=20)
   tboxes.append(dob_entry)
   dob_entry.place(x=550,y=475)

   # Register Button
   register1 = Button(root,text='Register',command=register_student)
   register1.place(x=550,y=525)
