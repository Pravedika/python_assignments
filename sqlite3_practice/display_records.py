import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT *FROM student")
for x in p:
    print(x)
conn.commit()