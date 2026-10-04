class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,length,breadth):
         print("Area Of Rectangle:",length*breadth)
class  Circle(Shape):
    def area(self,radius):
     print("Area Of Circle:",3.14*radius*radius)
class Triangle(Shape):
    def area(self,height,breadth):
        print('Area of Triangle:',0.5*height*breadth)
r = Rectangle()
c = Circle()
t = Triangle()
r.area(10,12)
c.area(5)
t.area(12,5)