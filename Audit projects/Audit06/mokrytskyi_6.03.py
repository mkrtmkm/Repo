n = input()
lst = ['a', 'e', 'i', 'o', 'u', 'y']
res = ""
for i in n:
    if i == lst[0] or i == lst[1] or i == lst[2] or i == lst[3] or i == lst[4] or i == lst[5]:
        i *= 2
    res += i
print(res)