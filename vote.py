age=int(input("enter age : "))
citizenship=input("enter citizenship : ")
if age>=18 and citizenship=="indian":
    print("eligible")
elif age<18 and citizenship=="indian":
    print("too young to vote")
elif age>=18 and citizenship!="indian":
    print("must be a citizen")  
elif age<18 and citizenship!="indian":
    print("too young to vote and not a citizen")
else:
    print("invalid") 