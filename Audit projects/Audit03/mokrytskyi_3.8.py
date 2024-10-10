n = int(input())
res = 0
i = 0
while n > 0:
    res += ((n % 10)*2**i)
    n //= 10
    i += 1
print(res)