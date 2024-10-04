n = int(input())
lst = list(map(int, input().split()))
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(*lst1)