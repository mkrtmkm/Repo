lst = list(map(int, input().split()))
res = []
for i in range(min(lst[0], lst[1]), max(lst[0], lst[1]) + 1):
    for j in range(min(lst[2], lst[3]), max(lst[2], lst[3]) + 1):
        k = i*j
        if k not in res:
            res.append(k)

print(len(res))
