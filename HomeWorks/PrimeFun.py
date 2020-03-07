def prime(n):
    list=[]
    while 2<=n:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            list.append(n)
        n=n-1
    list.reverse()
    print(list)
n=int(input("enter a number"))
prime(n)
