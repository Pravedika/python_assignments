import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p = cur.execute("SELECT std_course,count(std_course) FROM student GROUP BY std_course")
for x in p:
    print(x)