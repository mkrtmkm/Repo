n = int(input())
res = 0
if n == 1:
    for i in range(10, 100):
        if i % 10 < i // 10:
            res += 1

elif n == 2:
    for i in range(10, 100):
        if i % 10 > i // 10:
            res += 1

elif n == 3:
    for i in range(10, 100):
        if (i % 10) % 2 == (i // 10) % 2:
            res += 1

elif n == 4:
    for i in range(10, 100):
        if (i % 10) == (i // 10):
            res += i

elif n == 5:
    for i in range(10, 100):
        if (i % 10) % 2 == 0 and (i // 10) % 2 == 0:
            res += i

elif n == 6:
    for i in range(10, 100):
        if (i % 10) % 2 == 1 and (i // 10) % 2 == 1:
            res += i

print(res)