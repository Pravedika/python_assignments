class person:
    def role(self):
        pass
class Student(person):
    def role(self):
        print("Student Studies")
class Teacher(person):
    def role(self):
        print("Teacher teaches")
class Doctor(person):
    def role(self):
        print("Doctor treats paitents")
s =Student()
t =Teacher()
d =Doctor()
s.role()
t.role()
d.role()
