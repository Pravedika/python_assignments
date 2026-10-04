class Food:
    def role(self):
        pass
class Pizza(Food):
    def prepare(self):
        print("Pizza is being prepared")
class Burger(Food):
      def prepare(self):
        print("Burger is being prepared")
class Biryani(Food):
      def prepare(self):
       print("Biryani is being prepared")
s =Pizza()
t =Biryani()
d =Burger()
s.prepare()
t.prepare()
d.prepare()
