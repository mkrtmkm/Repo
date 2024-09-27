n = int(input())
res = 0
for i in range(1,n):
    res = i**3
    if res < n:
        print(res, end=" ")