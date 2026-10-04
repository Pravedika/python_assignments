import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT std_name FROM student WHERE std_id =185")
for x in p:
    print(x)
conn.commit()