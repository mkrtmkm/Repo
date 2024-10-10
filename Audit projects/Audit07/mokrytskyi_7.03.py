x, y, z = [float(d) for (d) in input().split()]
res = min(max(x,y), max(y,z), x+y+z)
print(res)