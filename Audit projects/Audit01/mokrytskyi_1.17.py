from math import*
a, b, c = [float(d) for (d) in input().split()]
P = a + b+ c
p = P/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
h1 = 2*S/a
h2 = 2*S/b
h3 = 2*S/c
print(f"{h1:.2f} {h2:.2f} {h3:.2f}")
