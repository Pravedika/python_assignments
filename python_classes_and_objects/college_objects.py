class College:
    def __init__(self, college_name, location, course):
        self.college_name = college_name
        self.location = location
        self.course = course

college_one = College("Aditya Polytechnic College", "Surampalem", "CSE")
college_two = College("ABC Polytechnic", "Kakinada", "ECE")
college_three = College("XYZ Polytechnic", "Rajahmundry", "EEE")

for college in [college_one, college_two, college_three]:
    print(college.college_name, college.location, college.course)
