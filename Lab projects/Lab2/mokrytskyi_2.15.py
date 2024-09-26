from math import*

a, b, c = [int(d) for (d) in input().split()]
D = b**2 - 4*a*c

if D > 0:
    x1 = int((-b + sqrt(D)) / (2*a))
    x2 = int((-b - sqrt(D)) / (2*a))
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    print(f"Two roots: {xmin} {xmax}")
elif D == 0:
    x = int(-b / (2*a))
    print(f"One root: {x}")
else:
    print("No roots")