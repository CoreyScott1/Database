import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

cur.execute("""
CREATE TABLE Students
(StudentID INTERGER, StudentFirstName TEXT(15), StudentLastName TEXT(15), StudentAge INTERGER(2))
""")