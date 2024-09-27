n = int(input())
n = abs(n)
n = str(n)
res = 0
for i in n:
    num = int(i)
    if num % 2 == 0:
        res += num
if res > 0 or '0' in n:
    print(res)
else:
    print("-1")


