# c=10
# def sum():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a+b)
# sum()
# print(c)
# def sum(x,y):
#     s=x+y
#     print(s)
# a=int(input("enter number"))
# b=int(input("enter number"))
# sum(a,b)
def sum(x,y):
    s=x+y
    sub=x-y
    p=x*y
    return s,sub,p
a=int(input("enter number"))
b=int(input("enter number"))
summ,diff,prod=sum(a,b)
print(summ,diff,prod)