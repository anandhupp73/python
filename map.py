from functools import reduce
#map(function,collection)
#withnormal function
l=[1,2,3,4,5]
def sqr(x):
    return x*x
sqrlist=list(map(sqr,l))
print(sqrlist)
#with lamda
l=[1,2,3,4,5]
sqrl=list(map(lambda x:x*x,l))
print(sqrl)
# filter(function,collection)

 #withnormal function
l = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2 == 0
filtered_list = list(filter(is_even, l))
 #with lamda
print(filtered_list)   
l=[1,2,3,4,5]
filterdlist=list(filter(lambda x:x%2==0,l))
print(filterdlist)

#reduce(function,collection)
l=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,l)
print(sum)

l=[1,3,5,6,7]
def sum(x,y):
    return x+y
sumd=reduce(sum,l)
print(sumd)

#avg of list 
