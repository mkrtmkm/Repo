a, b, n = [int(d) for d in input().split()]
c = a * n # суто гривні
d = b * n # суто копійки
x = d//100
c = c + x
y = d%100
d = y
print(c, d)