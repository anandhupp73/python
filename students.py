students=[]
n=int(input("enter num of students"))
for i in range(1,n+1):
    id=int(input("enter id"))
    name=input("enter name")
    age=int(input("enter age"))
    students.append([id,name,age])
print(students)