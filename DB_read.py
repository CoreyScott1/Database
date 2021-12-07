from tkinter import *
from tkinter import ttk
import sqlite3


con = sqlite3.connect("Students")
cur = con.cursor()


for row in cur.execute('SELECT * FROM Students'):
	print("new")
	print(row)

con.close()






