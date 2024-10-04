
n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

#print(*lst[::-1])

for i in range(n // 2):
    lst[i], lst[-i -1] = lst[-i -1], lst[i]
print(*lst)