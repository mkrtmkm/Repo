n = int(input())
res = 0

for i in range(10, 100):
    a = (i // 10) + (i % 10)
    k = i * n
    b = sum(map(int, str(k)))
    if a == b:
        res += 1
print(res)
