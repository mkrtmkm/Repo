n = input()
res = 0
if any(i.islower() for i in n):
    res += 1
if any(i.isupper() for i in n):
    res += 1
if any(i.isdigit() for i in n):
    res +=1
if any(i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+'] for i in n):
    res += 1
if len(n) >= 8:
    res +=1
print(res)