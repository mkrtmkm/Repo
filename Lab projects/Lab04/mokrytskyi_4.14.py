from math import*
n = int(input())
res = 1
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        if n != i:
            res = max(res, i)
        if n // i != n:
            res = max(res, n//i)
print(res)
