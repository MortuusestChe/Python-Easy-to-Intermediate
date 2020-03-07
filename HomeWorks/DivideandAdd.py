sum = 0.0
n = 0
while 1<2:
    val = input("")
    if (val == ''):
        break
    try:
        float(val)
        res = True
    except:
        res = False
    else:
        n = float(val)
        nf = round(n)
        print(nf)
        if (n < nf):
            n = n - 1
            sum = sum + 1000 / n
            print(nf)
        elif(n!=0): #
            n = round(n)
            sum = sum + 1000/n
        else:
            continue
sum=round(sum)
print(sum)