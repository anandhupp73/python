try :
    f=open("multi.txt","x")
except:
    print("file exists")
f=open("multi.txt","a")
n=int(input("enter num "))
for i in range(1,11):
    f.write(f"{i} * {n}={i*n}\n")
       