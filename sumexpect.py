sum=0
l=[1,2,3,"hello",4]
for i in l:
    try :
     sum+=i
    except TypeError:
        print("error ocuured")
print(sum)