a, b, c = [int(d) for (d) in input().split()]
d = max(a, b, c)
e = min(a, b, c)
if a != d and a!= e:
    print(a)
elif b != d and b!= e:
    print(b)
else:
    print(c)