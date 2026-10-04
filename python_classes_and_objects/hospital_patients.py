class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

patients = [
    Hospital("Ravi", 30, "Fever", "Dr. Kumar"),
    Hospital("Priya", 25, "Cold", "Dr. Anil"),
    Hospital("Anil", 40, "Diabetes", "Dr. Rao")
]

for patient in patients:
    print(patient.patient_name, patient.age, patient.disease, patient.doctor_name)
