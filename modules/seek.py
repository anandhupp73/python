f=open("st.txt",'r')
c=f.read(4)
print(c)
t=f.tell()
print(t)
f.seek(0)#to move cursor to first index
a=f.read()
print(a)