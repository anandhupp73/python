try :
    f = open('newfile.txt','x')
except :
    print("file exists")
f=open('newfile.txt','w')
f.write('hello')
