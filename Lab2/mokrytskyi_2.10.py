n = abs(int(input()))
a = n // 100
b = n // 10 % 10
c = n % 10
if a > c:
    print(a)
elif a < c:
    print(c)
else:
    print("=")
