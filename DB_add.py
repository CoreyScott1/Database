import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

cur.execute("""
INSERT INTO Students VALUES (324,'Corey','Scott',16)
""")