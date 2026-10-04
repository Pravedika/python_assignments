class BillingService:
    def generate_bill(self, patient, amount):
        print("Bill for", patient, ":", amount)

class Hospital:
    def generate_patient_bill(self, billing_service, patient, amount):
        billing_service.generate_bill(patient, amount)

Hospital().generate_patient_bill(BillingService(), "Ravi", 5000)
