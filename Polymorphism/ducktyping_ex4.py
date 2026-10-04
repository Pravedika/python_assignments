class EmailService:
    def send(self):
        print("we provide email service")
class SMSService:
    def send(self):
        print("we provide sms service")
def show(sms):
    sms.send()
e=EmailService()
s=SMSService()
show(e)
show(s)
