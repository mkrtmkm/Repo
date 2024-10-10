n = int(input())

t = 0
k = 1
while n > 0:
    d = n % 10
    t += d #t = t + d
    k *= d #k = k * d
    n = n // 10

s = k / t
print(f"{s:.3f}")