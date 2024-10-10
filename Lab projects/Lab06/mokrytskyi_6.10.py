n = input()
res = ""
for i in n:
    if i.isalpha():
        i *= 2
        res += i
    else:
        res += i
print(res)

