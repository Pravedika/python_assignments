import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE student(
               std_id integer,
               std_name text,
               std_age integer,
                std_course text,
                std_marks integer,
                course fee decimal(5,2))""")
print("Table 1 created successfully")
cur.execute("""CREATE TABLE course(
              course_id int primary key,
              course_name,
              course_fee decimal(5,2))""")
print("Table 2 created successfully")
conn.commit()
