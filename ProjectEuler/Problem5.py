#Smallest Multiple
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
c = 2520
val=0
while 1<2:
    if(c%11==0 and c%12==0 and c%13==0 and c%14==0 and c%15==0 and c%16==0 and c%17==0 and c%18==0 and c%19==0 and c%20==0):
        val=c
        break
    c= c+2520

print(val)