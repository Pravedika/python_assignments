from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF report.")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report.")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report.")

reports = [PDFReport(), ExcelReport(), HTMLReport()]

for report in reports:
    report.generate()
