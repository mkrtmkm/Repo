
n = int(input())
res = 0
if n == 1:
    print(4)
else:
    res = 10**n - 10**(n-1)
    res //= 2
print(res)



