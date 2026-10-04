class OfflineCourse:
    def start(self):
        print("online course provide portability")
class OnlineCourse:
    def start(self):
        print("offline course provide face to face interaction")
def show(report):
    report.start()
o1=OfflineCourse()
o2=OnlineCourse()
show(o1)
show(o2)