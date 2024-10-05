str1 = input()
res = 0

for c in str1[1:]:
    if c in '+-*':
        res += 1
print(res)