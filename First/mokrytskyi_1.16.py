n = abs(int(input()))
a = n // 100
b = n // 10 % 10
c = n % 10
print(c*100 + b*10 + a)