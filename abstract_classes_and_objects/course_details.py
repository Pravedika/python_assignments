from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def display(self):
        pass

class OnlineCourse(Course):
    def display(self):
        print("Online Course:", self.course_name)
        print("Duration:", self.duration)

class OfflineCourse(Course):
    def display(self):
        print("Offline Course:", self.course_name)
        print("Duration:", self.duration)

OnlineCourse("Python", "3 Months").display()
OfflineCourse("Java", "6 Months").display()
