n = int(input())
res = 0
i = 1
while res < n:
    res = i**3
    if res < n:
        print(res, end=" ")
        i += 1