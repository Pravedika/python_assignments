import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p=cur.execute("SELECT std_name,std_marks FROM student ORDER BY std_marks DESC")
for x in p:
    print(x)
conn.commit()