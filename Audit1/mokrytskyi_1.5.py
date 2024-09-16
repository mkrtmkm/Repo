from math import*
x1, y1, x2, y2, x3, y3 = [float(d) for (d) in input().split()]
a = sqrt((x2-x1)**2 + (y2-y1)**2)
b = sqrt((x3-x2)**2 + (y3-y2)**2)
c = sqrt((x3-x1)**2 + (y3-y1)**2)
P = a + b+ c
p = P/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
print(f"{P:.4f} {S:.4f}")
