from math import*
a, b, c, d, f = [float(d) for d in input().split()]
p1 = (a+b+f)/2
p2 = (c+d+f)/2
s1 = sqrt(p1*(p1-a)*(p1-b)*(p1-f))
s2 = sqrt(p2*(p2-c)*(p2-d)*(p2-f))
print(f"{(s1+s2):.4f}")