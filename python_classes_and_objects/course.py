class Course:
    institute_name = "ABC Institute"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

courses = [Course("Python Full Stack", "6 Months"), Course("Java Full Stack", "6 Months")]

for course in courses:
    print(course.institute_name, course.course_name, course.duration)
