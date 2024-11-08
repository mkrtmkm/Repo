def F(n):
    if n == 0:
        return 0
    elif n % 10 > 0:
        return n % 10
    else:
        return F(n // 10)


def S(p, q):
    return sum(F(i) for i in range(p, q + 1))


while True:
    line = input().strip()
    p, q = map(int, line.split())

    if p < 0 and q < 0:
        break

    print(S(p, q))
