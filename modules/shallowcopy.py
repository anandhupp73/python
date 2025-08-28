# l=[1,2,3,4,5]
# l2=l
# l2[2]=10
# print(l)
l=[1,2,3,4,5,[6,7,8]]
l2=l.copy()#shallow copy
l2[5][2]=10
print(l)