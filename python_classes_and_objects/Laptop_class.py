class laptop:
    def display(self,brand,ram,Processor,price):
        self.brand = brand
        self.ram=ram
        self.Processor=Processor
        self.price = price
    def show(self):
        print("Brand: ",self.brand)
        print("RAM: ",self.ram)
        print("Processor: ",self.Processor)
        print("Price: ",self.price)
l = laptop()
l.display("lenovo","16GB","Intel_i5",85000)
l.show()