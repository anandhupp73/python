def case(string):
    uppercount=0
    lowercount=0
    
    for char in string:
        if char.isupper():
            uppercount+=1
        elif char.islower():
            lowercount+=1
    return uppercount,lowercount
str=input("enter string : ")
upper,lower=case(str)
print("uppercount = ",upper)
print("lowercount = ",lower)