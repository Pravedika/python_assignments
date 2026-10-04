class InvalidPatientError(Exception):
    pass

class Hospital:
    def add_patient(self, name, age):
        try:
            if name == "":
                raise InvalidPatientError("Patient name cannot be empty")

            if age <= 0:
                raise InvalidPatientError("Age must be greater than zero")

            print("Patient added successfully")
            print("Name:", name)
            print("Age:", age)
        except InvalidPatientError as e:
            print("Error:", e)

hospital = Hospital()
hospital.add_patient("Ravi", 25)
hospital.add_patient("", 25)
hospital.add_patient("Priya", -5)
