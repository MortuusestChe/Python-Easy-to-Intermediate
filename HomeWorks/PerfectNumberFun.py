def mukemmel(n): 
    sum = 0

    for c in range(1, n - 1):
        if (n % c == 0):
            sum = c + sum

    if (sum == n):
        return True
    else:
        return False
n = int(input("Bir Sayı Giriniz"))
mukemmel(n)
