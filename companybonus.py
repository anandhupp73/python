service=int(input("year of service : "))
salary=int(input("enter salary : "))

if service>5:
    bonus=salary*5/100
    print("bonus : ",bonus)
else:
    print("no bonus")