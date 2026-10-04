import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("""INSERT INTO student VALUES
             (191,'sarayu',17,'CME',95),
             (185,'veda',17,'CME',98),
             (121,'shivani',19 ,'CCN',87),
              (122,'manoj',23,'ECE',78),
              (111,'deepak',21,'CIVIL',79)""")
print("Records inserted successfully!")
conn.commit()