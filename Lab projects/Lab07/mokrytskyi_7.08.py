import math

def count_pairs(A, B):
    if B % A != 0:
        return 0

    target = B // A
    count = 0

    for x in range(1, int(math.sqrt(target)) + 1):
        if target % x == 0:
            y = target // x
            if math.gcd(x, y) == 1:
                count += 2 if x != y else 1
    return count

A, B = map(int, input().split())
print(count_pairs(A, B))