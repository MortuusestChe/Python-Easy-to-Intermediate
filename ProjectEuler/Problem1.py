t=3 #Muptiples of 3 and 5
f=5
sum=0
c=1
while c<1000:
    if(c%f==0):
        sum = sum + c
    elif(c%t==0):
        sum = sum + c
    c = c+1
print(sum)