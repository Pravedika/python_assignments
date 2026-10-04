class computer:
    def role(self):
        pass
class laptop(computer):
    def process(self):
        print("display on webpage")
class desktop(computer):
    def process(self):
        print("designed to stay in one location")
class server(computer):
   def process(self):
        print("provide services ")
l =laptop()
d =desktop()
s = server()
l.process()
d.process()
s.process()
