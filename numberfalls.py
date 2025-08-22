def range(number,start,end):
    return start<= number <=end
num=int(input("enter a number"))
start =1
end=10
if range(num,start,end):
    print("in range")
else:
    print("not in range")