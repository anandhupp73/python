l=[1,3,5,6,7,8]
def fact(a):
    sum=0
    avg=0
    for i in a:
        sum+=i
        avg=sum/2
    print(avg)
    print(sum)
fact(l)