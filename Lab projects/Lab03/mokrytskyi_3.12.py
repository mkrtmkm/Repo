m = int(input())
n = m
k = 0
i = 0
b = 0
l = 0
while m > 0:
    d = m % 10
    i = i * 10 + d
    m //= 10
else:
    while i != n:
        n += i
        i = 0
        l = n
        while n > 0:
            d = n % 10
            i = i * 10 + d
            n //= 10
        k += 1
        n = l
print(k)
