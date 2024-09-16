from math import*
x, y = map(float, input().split())
a = (sqrt(x**2 + y**2)/(x-y)**2)
b = (2*x*y)/(sqrt(x**2 + y**2))
print(f"{a-b:.3f}")