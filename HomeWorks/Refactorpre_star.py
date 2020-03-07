val=str(input("Enter a Word"))
l=len(val)
w=val[0]
for c in range(1,l):
    if(val[c]==val[0]):
        w+='*'
    else:
        w+=val[c]
print(w)

