class Notification:
    def send(self):
        pass
class Email(Notification):
     def send(self):
         print("this is email notification")
class SMS(Notification):
    def send(self):
        print("sms is sent")
class Whatsapp(Notification):
    def send(self):
        print("this is whatsapp notification")
e = Email()
s =SMS()
w = Whatsapp()
e.send()
s.send()
w.send()