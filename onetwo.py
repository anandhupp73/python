d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
n=int(input("number : "))
reverse = 0
while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(reverse)
for i in str(reverse):
    print(d[int(i)])
    
