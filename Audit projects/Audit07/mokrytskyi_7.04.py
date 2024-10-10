def function(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = [int(d) for (d) in input().split()]
res = function(a,b)
print(res)