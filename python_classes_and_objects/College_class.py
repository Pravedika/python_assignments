class College:
    def display(self,name,location,course):
        self.name = name 
        self.location = location
        self.course=course
    def show(self):
       print("College Name: ",self.name)
       print("Location: ",self.location)
       print("Course: ",self.course)
l = College()
l.display("Aditya University","Surampalem","CME")
l.show()