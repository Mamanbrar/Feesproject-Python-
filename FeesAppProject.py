from tkinter import *
from tkinter.ttk import Label
import sqlite3
from turtle import bgcolor

window1 = Tk()
window1.title("FEES APP")
window1.geometry("1600x800")
window1.configure(bg='grey')

# Databases

# Create a database or connect to one
con = sqlite3.connect('databook.db')

# Create cursor
d = con.cursor()

# Create table

d.execute("""CREATE TABLE data (
		Name text,
		Uid text,
		Number text,
        Fees integer
		)""")


def register1():
    global window2
    window2=Tk()
    window2.title("Registering")
    window2.geometry("1600x800")
    #window2.configure(bg='grey')
    #space = Label(window2,text="          ")
    #space.grid(row=0,column=0)
    name_label=Label(window2,text="Name           : ",font=("Arial", 30))
    name_label.grid(row=0,column=0,padx=(300,0),pady=(150,0))              
    uid_label=Label(window2,text="UID              : ",font=("Arial", 30))
    uid_label.grid(row=1,column=0,padx=(300,0))              
    course=Label(window2,text="Course          : ",font=("Arial", 30))
    #course.grid(row=2,column=0,padx=(300,0)) 
    number_label=Label(window2,text="Mobile Number : ",font=("Arial", 30)) 
    number_label.grid(row=2,column=0,padx=(300,0))  
    Fees_label=Label(window2,text="Fees           : ",font=("Arial", 30)) 
    Fees_label.grid(row=3,column=0,padx=(300,0))  

    global name
    global number
    global uid
    global fees
    name = Entry(window2,width=35,borderwidth=5)
    name.grid(row=0,column=1,pady=(150,0))
    uid = Entry(window2,width=35,borderwidth=5)
    uid.grid(row=1,column=1)
    number=Entry(window2,width=35,borderwidth=5)
    number.grid(row=2,column=1)
    fees=Entry(window2,width=35,borderwidth=5)
    fees.grid(row=3,column=1)

    save_btn = Button(window2,text="SAVE",font=("Arial", 30),command=save)
    save_btn.grid(row=5,column=0,columnspan=4,ipadx=100,padx=(500,0),pady=(150,0))
    
def save():
	# Create a database or connect to one
	con = sqlite3.connect('data_book.db')
	# Create cursor
	d = con.cursor()
	# Insert Into Table
	d.execute("INSERT INTO data VALUES (:Name, :Uid, :Number, :Fees)",
		{
			'Name': name.get(),
			'Uid': uid.get(),
			'Number': number.get(),
			'Fees': fees.get()
		})
	#Commit Changes
	con.commit()
	# Close Connection 
	con.close()
	name.delete(0,END)
	fees.delete(0, END) 
	uid.delete(0,END)
	number.delete(0,END)
	response = Label(window2,text="INFORMATION SAVED!",font=("Arial", 20))
	response.grid(row=6,column=8,padx=200,pady=(20,0))
	back = Button(window2,text="BACK",font=("Arial", 35),command=window2.destroy)
	back.grid(row=6,column=0,pady=20,padx=300)


    
              
def todeposit():
    global window3
    window3=Tk()
    window3.title("FEES DEPOSIT")
    window3.geometry("1600x800")
    #window3.configure(bg='grey')
    global uid
    global fees
    uid_label=Label(window3,text="UID     : ",font=("Arial", 40))
    uid_label.grid(row=0,column=0,padx=(100,0),pady=(150,0))

    uid = Entry(window3,width=35,borderwidth=5)
    uid.grid(row=0,column=1,pady=(150,0))

    Fees_label=Label(window3,text="Fees   : ",font=("Arial", 40)) 
    Fees_label.grid(row=2,column=0,padx=(100,0))

    fees=Entry(window3,width=35,borderwidth=5)
    fees.grid(row=2,column=1)

    deposit_btn = Button(window3,text="Deposit",font=("Arial", 40),command=deposit)
    deposit_btn.grid(row=3,column=0,columnspan=7,rowspan=5,ipadx=100,padx=100,pady=(50,0))

def deposit():
	# Create a database or connect to one
	con = sqlite3.connect('data_book.db')
	# Create cursor
	d = con.cursor()
	d.execute("SELECT Fees FROM data WHERE Uid =" + uid.get())
	records = d.fetchall()
	FEES = int(fees.get())
	UIDs= uid.get()
	for record in records[0]:
		fee=record
	feesleft = fee-FEES	
	print(feesleft)
	d.execute("UPDATE data SET Fees = :fees WHERE Uid = :uid",
		{
		'fees': feesleft,
		'uid': uid.get()
		})
	d.execute("SELECT Name FROM data WHERE Uid =" + UIDs)
	records = d.fetchall()	
	for record in records[0]:
		Names=record
	con.commit()
	# Close Connection 
	con.close()
	fees.delete(0, END) 
	uid.delete(0,END)
	recipt = Label(window3,text="PAYMENT RECIPT ",font=("Arial", 35))
	name = Label(window3,text="              Name : "+Names,font=("Arial", 20))
	uids = Label(window3,text="           UID : "+str(UIDs),font=("Arial", 20))
	fee = Label(window3,text="Amount Paid : "+str(FEES),font=("Arial", 20))
	feeleft = Label(window3,text=" Amount Left : "+str(feesleft),font=("Arial", 20))
	back = Button(window3,text="BACK",font=("Arial", 35),command=window3.destroy)

	recipt.grid(row=0,column=9,columnspan=3,padx=300)
	name.grid(row=1,column=9,padx=200)
	uids.grid(row=2,column=9,padx=200)
	fee.grid(row=3,column=9,padx=200)
	feeleft.grid(row=4,column=9,padx=200)
	back.grid(row=5,column=9,pady=100)


def delete():
    window4=Tk()
    window4.title("FEES APP")
    window4.geometry("1600x800")
    window4.configure(bg='grey')
    return    
label1 = Label(window1,text="**************FEES APP**************",font=("Arial", 30),justify=CENTER)

label1.pack(pady=(100,0))

button1=Button(window1,text="Register New Student",command=register1,font=("Arial", 25),bg='red',fg="white")
button1.pack(pady=40)

button2=Button(window1,text="To Deposite Fees",command=todeposit,font=("Arial", 25),bg='red',fg="white")
button2.pack(pady=40)

button3=Button(window1,text="Deleting a Student Data",command=delete,font=("Arial", 25),bg='red',fg="white")
button3.pack(pady=40)

label1 = Label(window1,text="👉😎🤟 ਬਰਾੜ ਤਮਕੋਟਿਆਂ  🤟😎👈 ",font=("Arial", 30),justify=CENTER)
label1.pack()

#Commit Changes
con.commit()

# Close Connection 
con.close()

window1.mainloop()
