n = input()
lst = []

for i in n:
    if i != ' ':
        lst.append(i.lower())
if lst == lst[::-1]:
    print('YES')
else:
    print('NO')