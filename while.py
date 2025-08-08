i=1
natural=0
even=0
odd=0
while(i<=10):
    natural+=i
    if i%2==0:
        even+=i
    elif i%2!=0:
        odd+=i
    i=i+1
print(natural,even,odd)     
   