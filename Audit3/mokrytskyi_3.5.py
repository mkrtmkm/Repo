n = int(input())

t = 0
k = 1
while n > 0:
    d = n % 10
    t += d
    k *= d
    n = n // 10
    pass

s = k / t
print(f"{s:.3f}")