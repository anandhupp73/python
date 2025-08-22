def calc(a,b,oprtr):
    if oprtr == '+':
        return a+b
    elif oprtr == '*':
        return a*b
    elif oprtr == '-':
        return a-b
    elif oprtr == '/':
        if b!=0:
            return a/b
        else:
            return "inavid"
    else:
        return "invaid"
num1=int(input("enter a number"))
num2=int(input("enter a number"))
op=input("enter oprtr")
result=calc(num1,num2,op)
print("result",result)