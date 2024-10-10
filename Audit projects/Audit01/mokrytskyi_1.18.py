x1, y1, x2, y2, x3, y3, x4, y4 = [float(d) for (d) in input().split()]
s = abs((x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1))/2
print(round(s))
