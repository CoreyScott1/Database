import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

cur.execute("""
CREATE TABLE Students
(StudentID text, StudentFirstName text, StudentLastName text, StudentAge text)
""")

con.close()
