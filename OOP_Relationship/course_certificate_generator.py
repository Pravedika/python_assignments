class CertificateGenerator:
    def generate(self, student_name, course_name):
        print("Certificate generated for", student_name, "for", course_name)

class Course:
    def __init__(self, name):
        self.name = name

    def issue_certificate(self, generator, student_name):
        generator.generate(student_name, self.name)

Course("Python").issue_certificate(CertificateGenerator(), "Ravi")
