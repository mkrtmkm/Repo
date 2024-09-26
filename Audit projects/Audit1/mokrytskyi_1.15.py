n = abs(int(input()))
a = n // 100
b = n // 10 % 10
c = n % 10
d = a * b * c
f = a + b + c
print(d-f)