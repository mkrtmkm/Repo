from math import*

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_mirror(n):
    reversed_n = int(str(n)[::-1])
    return is_prime(n) and is_prime(reversed_n)

def is_count(a, b):
    count = 0
    for x in range(a, b+1):
        if is_mirror(x):
            count+=1
    return count

a, b = [int(d) for (d) in input().split()]
res = is_count(a,b)
print(res)
