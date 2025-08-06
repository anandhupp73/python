age=int(input("enter age : "))
day=input("enter day : ")
member=input("are you member yes/no : ")
if age<12:
    price=8
elif age<65:
    price=10
else:
    price=15
if day=="tuesday":
    price*=0.8
elif day=="sunday" or day=="saturday":
    price+=2
    if member=="yes":
        price*=0.9
        
print("price : ",price)    