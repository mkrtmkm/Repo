n = int(input())
n = str(n)
res = ""
for i in n:
    num = int(i)
    if num % 2 == 0:
        res += str((num + 1))
    else:
        res += str((num - 1))
print(int(res))
