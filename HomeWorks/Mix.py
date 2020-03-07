val1=input("first word")
val2=input("second word")
a=val1[0:2]
nval1=""
nval1+=a
b=val2[0:2]
nval2=""
nval2+=b
for c in range(2,len(val1)):
    nval2 += val1[c]
for c in range(2,len(val2)):
    nval1 += val2[c]
print(nval2)
print(nval1)