def lcm(n):

    def gcd1(a, b):
        while b:
            a, b = b, a % b
            return a

    def lcm1(a, b):
        return abs(a*b)//gcd1(a, b)

    res = 1
    for i in range(2, n + 1):
        result = lcm1(res, i)

    return res

n = int(input())
print(lcm(n))
