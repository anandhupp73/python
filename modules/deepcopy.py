import copy
l=[1,2,3,4,5,[6,7,8]]
l2=copy.deepcopy(l)
l2[5][2]=20
print(l)
print(l2)