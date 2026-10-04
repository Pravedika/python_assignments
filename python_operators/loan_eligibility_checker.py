salary = float(input("Enter salary: "))
age = int(input("Enter age: "))
credit_score = int(input("Enter credit score: "))
eligible = salary >= 30000 and 21 <= age <= 60 and credit_score >= 650
print("Loan eligible:", eligible)
