class ExcelReport:
    def generate(self):
        print("excel report was generated")
class PDFReport:
    def generate(self):
        print("pdf report was generated")
def show(report):
    report.generate()
e=ExcelReport()
p=PDFReport()
show(e)
show(p)