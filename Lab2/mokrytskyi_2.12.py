x = int(input())
if 0 <= x <= 1000:
    y = x**3 + 2*x**2 + 4*x - 6
else:
    y = x**3 - 7*x

print(y)