students1 = [("alice",85),("Bob",93),("charlie",78),("diana",96)]
students2 = [("eve",88),("frank",75),("grace",94),("henry",82)]
print(sorted(students1,key=lambda x:x[1],reverse=True))
print(sorted(students2,key=lambda x:x[1],reverse=True))

