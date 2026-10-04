employee =[("washing machine",65000,4),
            ("MobilePhones",55000,3),
            ("Earphones",3000,5)
           ]
for _,price,quantity in employee:
    total_value = price*quantity
    print(total_value)