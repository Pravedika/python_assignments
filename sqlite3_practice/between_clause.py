import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
p=cur.execute("SELECT *FROM  student WHERE std_marks BETWEEN 60 AND 90")
for x in p:
  print(x)