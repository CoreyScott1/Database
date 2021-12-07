from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

def Write():
	IDinput = sID.get(1.0,"end")
	FNAMEinput = sFNAME.get(1.0,"end")
	SNAMEinput = sLNAME.get(1.0,"end")
	AGEinput = sAGE.get(1.0,"end")
	
	print("submit")
	print(IDinput)
	print(FNAMEinput)
	print(SNAMEinput)
	print(AGEinput)


	cur.execute("""
	INSERT INTO Students VALUES (?,?,?,?)
	""",(IDinput,FNAMEinput,SNAMEinput,AGEinput))

def Read():
	print("temp")




root = Tk()
root.title("Student Database")
root.geometry("380x400")

frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Label(root, text="Student ID").grid(column=4, row=1)
sID = Text(root, height = 1, width = 20)

ttk.Label(root, text="Student First Name").grid(column=4, row=3)
sFNAME = Text(root, height = 1, width = 20)

ttk.Label(root, text="Student Last Name").grid(column=4, row=5)
sLNAME = Text(root, height = 1, width = 20)

ttk.Label(root, text="Student Age").grid(column=4, row=7)
sAGE = Text(root, height = 1, width = 20)

sID.grid(column=4, row=2)
sFNAME.grid(column=4, row=4)
sLNAME.grid(column=4, row=6)
sAGE.grid(column=4, row=8)

ttk.Button(root, text="Submit", command = Write).grid(column=4, row=9)
ttk.Button(root, text="Read Data", command = Read).grid(column=4, row=10)

ttk.Label(root, text = "ID").grid(column=6,row=2)
ttk.Label(root, text = "Fname").grid(column=8,row=2)
ttk.Label(root, text = "Sname").grid(column=10,row=2)
ttk.Label(root, text = "Age").grid(column=12,row=2)

root.mainloop()

