#sum square difference
c=1
sumsq=0
sqsum=0
dif=0
while c<=100:
    sumsq = sumsq + (c*c)
    sqsum = sqsum + c
    c=c+1
sqsum=sqsum*sqsum
dif=sqsum-sumsq
print(dif)
