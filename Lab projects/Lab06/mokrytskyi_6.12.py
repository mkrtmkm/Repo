lst = input()
n = int(input())
res = ""

lst1 = lst.upper()

for i in lst1:
    orig_pos = ord(i) - ord('A')
    new_pos = (orig_pos - n) % 26
    res += chr(new_pos + ord('A'))
print(res)