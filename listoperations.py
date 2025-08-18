numbers=[100,20,50,20,68,55,29]
num=int(input("enter a number" ))
count=numbers.count(num)
print("the number apperas in the list",count,"times")
if count > 0 :
    print("index positons are",end=" ")
    for i in range(len(numbers)):
        if numbers[i] == num:
            print(i,end=" ")
else:
    print("the num not exit")
    