
# Import TKinter
from sqlite3 import Cursor
from tkinter import *
# Import Database
import pymysql
#Import tkinter messagebox for popup
import tkinter.messagebox as m

# Creating main window
r = Tk()
r.geometry("400x400")
r.title("Student Form")
r.configure(bg="Skyblue")

# Create a function for database pymysql
def CreateConn():
    return pymysql.Connect(host="localhost",database="myfile",user="root",password="",port=3306)

# Create a function for Insert Data
def InsertData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()

    if(r=="" or f=="" or l=="" or e==""):
        m.showinfo("Insert Status","All fields are Mandatory")

    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (r,f,l,e)
            query = "insert into student(rollno,fname,lname,email)values(%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status","Data Inserted")
            conn.close()
        except Exception as ee:
            print("Insert Exception : ",ee)        

#Adding Label in main window

rn = Label(r, text="Roll No")
rn.place(x=20,y=20)

fn = Label(r, text="First Name")
fn.place(x=20,y=60)

ln = Label(r, text="Last Name")
ln.place(x=20,y=100)

em = Label(r, text="Email")
em.place(x=20,y=140)

# Adding Entry Box into the main window

ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=60)

eln = Entry()
eln.place(x=100,y=100)

eem = Entry()
eem.place(x=100,y=140)

# Adding Button into main window

submit = Button(r, text="Submit", bg="white", command=InsertData)
submit.place(x=20,y=200)

# mainloop method called
mainloop()