import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT count(*) FROM student")
for x in p:
    print(x)