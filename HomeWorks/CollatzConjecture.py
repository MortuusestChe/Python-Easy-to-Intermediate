val = int(input("Enter a Number"))
c=0
while val > 1:
    if (val % 2 != 0):
        val = 3 * val + 1
    else:
        val = val /2
    c=c+1

print(c)


