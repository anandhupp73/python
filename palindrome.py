# str1=input("enter string: ")
# str2=str1[::-1]
# if str1==str2:
#     print("palindrome")
# else:
#     print("not palindrome")
str1=input("enter string: ")
reverse=''
for i in str1:
    reverse=i+reverse
print(reverse)
if str1==reverse:
        print("palindrome")
else:
        print("not palindrome")
    