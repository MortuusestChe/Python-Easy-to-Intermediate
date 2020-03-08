#Largest Prime Factor
n=2
value=0
while 2 <= 600851475143:
    for i in range(2, n):
        if (n % i) == 0:
            break
    if(600851475143%n==0):
        value = n
        print(n)
    n = n + 1
