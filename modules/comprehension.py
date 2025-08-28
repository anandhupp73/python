#newlist=[expressrion for itervariable in iterable if condition]
l=[1,2,3,4,5]
even=[x for x in l if x%2==0]
sqr=[x**2 for x in l]
print(even)
print(sqr)