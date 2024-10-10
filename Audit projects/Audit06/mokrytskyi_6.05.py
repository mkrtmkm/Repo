s = input()
res = ""
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        res += s[i]
if len(s) > 1:
    res += s[-1]
elif len(s) == 1:
    res += s[0]
print(res)