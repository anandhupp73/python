a=int(input("enter  number a : "))
b=int(input("enter  number b : "))
c=int(input("enter  number c : "))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("equilateral")
    elif a==b or a==c or b==c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("invalid")