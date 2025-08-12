l=[1,2,3,4,1,2,3,4]
sorted_list=[]
for i in l:
    if i not in sorted_list:
        sorted_list.append(i)
print(sorted_list)