#Even Fibonacci Numbers Sum
n=4000000
a, b = 1, 2
sum=0
while a < n:
    if (a % 2 == 0):
        sum = sum + a
    a, b = b, a+b

print(sum)
