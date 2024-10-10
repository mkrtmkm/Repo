n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
lst  = []
for i in lst1:
    if i not in lst2:
        lst.append(i)

print(len(lst))
print(*lst)
