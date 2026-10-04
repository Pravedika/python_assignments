import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE student(
               std_id integer,
               std_name text,
               std_age integer,
                std_course text,
                std_marks integer)""")
print("Table created successfully")
conn.commit()