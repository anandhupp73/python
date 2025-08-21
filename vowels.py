def vovels(str):
    count=0
    for i in str:
        if i in 'aeiou':
            count+=1
    print(count)
string=input("enter the string : ")
vovels("string")