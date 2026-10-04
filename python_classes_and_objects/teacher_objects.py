class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teachers = [
    Teacher("Anil", "Python", 5),
    Teacher("Ravi", "Java", 7),
    Teacher("Priya", "SQL", 4)
]

for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience)
