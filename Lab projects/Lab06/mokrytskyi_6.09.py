str1 = input()
res = 0
i = 0
lst = ['+', '-', '*', '/', '%']

while i < len(str1):
    if str1[i:i+2] == '**' or str1[i:i+2] == '//':
        res += 1
        i += 1
    elif str1[i] in lst:
        res += 1
    i += 1

print(res)