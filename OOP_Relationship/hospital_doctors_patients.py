class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Dr. Ravi"), Doctor("Dr. Sita")]
        self.patients = [Patient("Kumar"), Patient("Anu")]

    def display(self):
        print("Doctors:")
        for doctor in self.doctors:
            print(doctor.name)
        print("Patients:")
        for patient in self.patients:
            print(patient.name)

Hospital().display()
