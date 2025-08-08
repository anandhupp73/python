sum1=0
sum2=0
sum3=0
for i in range(1,11):
    sum1+=i
    if i%2==0:
        sum2+=i
    elif i%2!=0:
        sum3+=i
print(sum1,sum2,sum3)
