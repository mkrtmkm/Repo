n = int(input())
lst = []
i = 0
while len(lst) != n:
    if i % 2 != 0 and i % 3 != 0 and i % 5 !=0:
        lst.append(i)
    i += 1
print(*lst)
