import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("""UPDATE student
            SET std_marks=65
            WHERE std_id=191""")
p =cur.execute("SELECT *FROM student")
for x in p:
  print(x)