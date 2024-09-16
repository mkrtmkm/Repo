x, y, x1, y1, x2, y2 = [float(d) for (d) in input().split()]

xmin = min(x1, x2)
xmax = max(x1, x2)
ymin = min(y1, y2)
ymax = max(y1, y2)

if xmin <= x <= xmax and ymin <= y <= ymax:
    print(1)
else:
    print(0)