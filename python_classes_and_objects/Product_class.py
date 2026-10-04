class Product:
    def show(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        print("Product name: ",self.name)
        print("Price: ",self.price)
        print("Quantity: ",self.quantity)
p = Product()
p.show("washingmachine",67000,2)
p.display()