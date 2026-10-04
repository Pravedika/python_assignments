class AndroidPhone:
    def call(self):
        print("OS is Android")
class iPhone:
    def call(self):
        print("OS is IOS")
def show(report):
    report.call()
o1=AndroidPhone()
o2=iPhone()
show(o1)
show(o2)