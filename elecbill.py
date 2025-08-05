unit=int(input("enter unit : "))
if unit<=100:
    print("no charge")
elif unit>100 and unit<=200:
    amount=unit*5
    print("amount : ",amount)
elif unit>200:
    amount=unit*10
    print("amount : ",amount)
else:
    print("invalid")