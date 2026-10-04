import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("""DELETE FROM student WHERE std_id=111""")
p =cur.execute("SELECT *FROM student")
for x in p:
  print(x)