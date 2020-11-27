from tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

   
root = Tk()
root.title('FBLA Community Service Hours Program')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Student", command=donothing)
filemenu.add_command(label="Chapter", command=donothing)
filemenu.add_command(label="Award Detail", command=donothing)
filemenu.add_command(label="Community Service", command=donothing)
filemenu.add_command(label="Coummunity Service Hours", command=donothing)
filemenu.add_command(label="Program Category", command=donothing)
#filemenu.add_command(label="Teacher (Administrator)", command=donothing)

filemenu.add_separator()


menubar.add_cascade(label="Add Data", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Student", command=donothing)
editmenu.add_command(label="Chapter", command=donothing)
editmenu.add_command(label="Award Detail", command=donothing)
editmenu.add_command(label="Community Service", command=donothing)
editmenu.add_command(label="Coummunity Service Hours", command=donothing)
editmenu.add_command(label="Program Category", command=donothing)
#editmenu.add_command(label="Teacher (Administrator)", command=donothing)

#editmenu.add_separator()

#editmenu.add_command(label="Cut", command=donothing)
#editmenu.add_command(label="Copy", command=donothing)
#editmenu.add_command(label="Paste", command=donothing)
#editmenu.add_command(label="Delete", command=donothing)
#editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Modify Data", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Chapter", command=donothing)
helpmenu.add_command(label="Student", command=donothing)
helpmenu.add_command(label="Program Category", command=donothing)
helpmenu.add_command(label="Community Service", command=donothing)
helpmenu.add_command(label="Coummunity Service Hours", command=donothing)
helpmenu.add_command(label="Award Detail", command=donothing)
#helpmenu.add_command(label="Teacher (Adminstrator)", command=donothing)
menubar.add_cascade(label="Search Data", menu=helpmenu)

exitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Quit", command=root.destroy)

root.config(menu=menubar)
root.mainloop()
