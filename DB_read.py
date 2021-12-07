from tkinter import *
from tkinter import ttk
import sqlite3


con = sqlite3.connect("Students")
cur = con.cursor()

rows = cur.execute("""
SELECT StudentFirstName FROM Students
""").fetchall()





print(rows)
