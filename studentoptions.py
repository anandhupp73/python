students=[]
while(True):
    print('''1. add student
             2. search student
             3. delete student
             4. view all students
             5. exit
          ''')
    choice=int(input("enter your choice : "))
    if choice==1:
        print("add student")
        id=int(input("enter id"))
        name=input("enter name")
        age=int(input("enter age"))
        students.append([id,name,age])
    elif choice==2:
        print("search student")
        id=int(input("enter id"))
        for i in range(len(students)):
            if students[i][0]==id:
                print(students[i])
    elif choice==3:
       print("delete student")
       id=int(input("enter id"))
       for i in range(len(students)):
            if students[i][0]==id:
                students.pop(i)
    elif choice==4:
        print("view all students")
        print(students)
    elif choice==5:
        print("exit")
        break
        
    