import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT std_name,std_marks FROM student WHERE std_marks>75")
for x in p:
    print(x)