from math import*
x, y = [float(d) for (d) in input().split()]
a = ((2*x*y)/(sqrt(x**2 + y**2)) - ((x+y-1)**2)/(x*y))
print(f"{a:.4f}")