from tkinter import *
from tkinter import ttk
import sqlite3


con = sqlite3.connect("Students")
cur = con.cursor()

row = cur.execute('SELECT * FROM Students')
print("new")
print(row)






