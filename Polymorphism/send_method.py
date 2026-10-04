class EmailNotification():
    def send(self,message):
        print("Email sent: ",message)
class SMSNotification():
    def send(self,message):
        print("SMS sent: ",message)
e = EmailNotification()
s = SMSNotification()
e.send("Hello, this is an email notification.")
s.send("Hello, this is an SMS notification.")