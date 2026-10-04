import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT min(std_marks),max(std_marks) FROM student")
for x in p:
    print(x)