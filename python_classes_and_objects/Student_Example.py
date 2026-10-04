class Student:
    def details(self,name,age,course):
      self.name=name
      self.age = age
      self.course = course
    def display(self):
       print("Student Details: ")
       print("Student Name: ",self.name)
       print("Age: ",self.age)
       print("Course: ",self.course)
s1=Student()
s2=Student()
s3=Student()
s1.details("Pravedika",17,"cme")
s2.details("Sandesh",17,"cse")
s3.details("Mohith",15,"mpc")
s1.display()
s2.display()
s3.display()
