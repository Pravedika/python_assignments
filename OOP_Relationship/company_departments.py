class Department:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR"),
            Department("Finance")
        ]

    def display_departments(self):
        for department in self.departments:
            print("Department:", department.name)

Company().display_departments()
