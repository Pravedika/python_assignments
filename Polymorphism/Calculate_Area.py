class Rectangle:
    def area(self,length,width):
        print("Area Of Rectangle: ",length*width)
class Circle:
   def area(self,radius):
         print("Area Of Circle: ",3.14*radius*radius)
r1 = Rectangle()
c1 =Circle()
r1.area(10,30)
c1.area(5)