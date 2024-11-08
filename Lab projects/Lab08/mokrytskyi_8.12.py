def mod_exp(k, n, m):
    res = 1
    base = k % m
    while n > 0:
        if n % 2 == 1:
            res = (res * base) % m
        base = (base * base) % m
        n //= 2
    return res

case_number = 1
while True:
    k, n, t = map(int, input().strip().split())

    if k == 0 and n == 0 and t == 0:
        break

    m = 10 ** t
    result = mod_exp(k, n, m)
    print(f"Case #{case_number}: {result}")
    case_number += 1
