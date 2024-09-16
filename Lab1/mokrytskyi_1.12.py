x1, y1, x2, y2, a = [float(d) for (d) in input().split()]
x = (x1 + a * x2) / (1 + a)
y = (y1 + a * y2) / (1 + a)
print(f"{x:.2f}", f"{y:.2f}")