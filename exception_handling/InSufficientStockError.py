class InsufficientStockError(Exception):
    pass
try:
     present_stock= 100
     stock = int(input('Enter the stock you want to buy: '))
     if stock > present_stock:
        raise InsufficientStockError("Insufficient Stock")
     print("Sufficient Stock")
except InsufficientStockError as e:
       print("Error: ",e)
       