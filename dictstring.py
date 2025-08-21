d={}
for i in range(3):
     string=input("enter string ")
     a=len(string)
     d.setdefault(string,a)
     i+1
print(d)
