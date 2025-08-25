try :
    f=open("studentfile.txt","x")
except:
    print("file exists")
f=open("studentfile.txt","w")
n=int(input("enter num of students"))
for i in range(n):
        print("Enter details for student:")
        name = input("Name: ")
        f.write(f"Name: {name},\n")


