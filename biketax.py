cost=int(input("enter cost : "))
if cost>100000:
    tax=cost*15/100
    print("tax : ",tax)
elif cost>50000 and cost<=100000:
    tax=cost*10/100
    print("tax : ",tax)
elif cost<=50000:
    tax=cost*5/100
    print("tax : ",tax)
else:
    print("invalid")