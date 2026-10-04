import sqlite3
conn = sqlite3.connect("college.db")
cur =conn.cursor()
data = [(101, 'Ravi', 18, 'CSE', 85),
(102, 'Priya', 19, 'ECE', 78),
(103, 'Kiran', 18, 'CME', 92),
(104, 'Anjali', 19, 'CSE', 88),
(105, 'Rahul', 20, 'EEE', 74),
(106, 'Sneha', 18, 'CME', 81),
(107, 'Arjun', 19, 'CSE', 95),
(108, 'Divya', 20, 'ECE', 69),
(109, 'Naveen', 18, 'EEE', 77),
(110, 'Keerthi', 19, 'CME', 90)]
cur.executemany("INSERT INTO student Values(?,?,?,?,?)",data)
conn.commit()
p =cur.execute("SELECT *FROM student")
for x in p:
    print(x)