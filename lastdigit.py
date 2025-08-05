num=int(input("enter a number : "))
lastdigit=num%10
if lastdigit%3==0:
    print("last digit is divisible by 3")
else:  
    print("last digit is not divisible by 3")